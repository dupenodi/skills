#!/usr/bin/env python3
"""Heuristic scanner for AI design slop tells (see ../SKILL.md).

Usage: python3 -I scan.py <file-or-dir> [...]
Scans .html .htm .css .scss .js .jsx .ts .tsx .vue .svelte .astro .md .mdx
A hit is a question to answer, not a verdict. Exit code 1 if any hits.
"""
import os
import re
import sys

EXTS = {".html", ".htm", ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts",
        ".tsx", ".vue", ".svelte", ".astro", ".md", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".nuxt", "out",
             "coverage", ".svelte-kit", "vendor", ".turbo", ".cache"}

I = re.IGNORECASE

# (tell number, name, regex, flags). Line-level checks.
LINE_RULES = [
    (1, "Arrow in button/link label",
     r"(<(button|a)\b[^>]*>[^<]*[→↗↘➜➔⟶›»]|[→↗➜➔⟶]\s*</(button|a)>|"
     r"(ArrowRight|ArrowUpRight|ChevronRight|MoveRight|ArrowRightIcon)\b)", 0),
    (2, "Interpunct separator", r"\S\s+(·|&middot;|&#183;|\\u00b7|•)\s+\S", 0),
    (3, "Eyebrow (tiny tracked uppercase label)",
     r"(uppercase[^\"'\n]*tracking-(wide|wider|widest|\[)|tracking-(wider|widest|\[)[^\"'\n]*uppercase|"
     r"text-transform:\s*uppercase[^}]*letter-spacing|letter-spacing:\s*0?\.\d+em[^}]*text-transform:\s*uppercase|"
     r"class(Name)?=[\"'][^\"']*\beyebrow\b)", I),
    (4, "Cream background", r"(#f4f1ea|#f5f1e8|#f7f3ec|#faf7f0|#f3efe6|#f5f0e6|#fbf8f1|#f6f1e7|#efe9dd|"
     r"bg-(stone|amber|orange)-50\b|\b(cream|ivory|parchment|linen|eggshell)\b)", I),
    (5, "Italic word inside a headline",
     r"(<h[1-3]\b[^>]*>(?:(?!</h[1-3]>).)*<(em|i)\b|<h[1-3]\b[^>]*>(?:(?!</h[1-3]>).)*\bitalic\b)", I),
    (6, "Sparkle icon", r"(✨|✦|✧|❇|\bSparkles?\b|sparkle|\bWandSparkles\b|\bStars\b)", 0),
    (8, "The word 'quiet' (and kin)", r"\b(quiet(ly)?|unhurried|gently|calm(ly)?|thoughtful(ly)?|"
     r"crafted|considered)\b", I),
    (9, "Numbered section label (01, 02...)", r"(>\s*0[1-9]\s*<|[\"'`]0[1-9][\"'`]|^\s*0[1-9]\s*$|"
     r"\b0[1-9]\s*[—–/.]\s+[A-Z])", 0),
    (10, "Pulsing status dot", r"(animate-(pulse|ping)|animation:[^;]*\b(pulse|ping|blink|glow)\b|"
     r"@keyframes\s+(pulse|ping|blink|glow)|\b(NOMINAL|OPERATIONAL|ALL SYSTEMS)\b|status-dot|live-dot)", 0),
    (11, "Blurry glow", r"(blur-(2xl|3xl|\[\d{2,}px\])|filter:\s*blur\(\s*\d{2,}px|"
     r"radial-gradient\(|class(Name)?=[\"'][^\"']*\b(glow|blob|orb|aurora)|"
     r"\.(glow|blob|orb|aurora)[\w-]*\s*[{,])", I),
    (12, "Instrument Serif (or reflexive display serif)",
     r"(Instrument[\s_+-]?Serif|Fraunces|Playfair[\s_+-]?Display|DM[\s_+-]?Serif)", I),
    (13, "Colored left border", r"(border-l-(2|4|8|\[)|border-left:\s*\d+px\s+solid|border-left-width|"
     r"border-inline-start:\s*\d+px)", I),
    (14, "Three-column grid (icon cards?)", r"(grid-cols-3|md:grid-cols-3|lg:grid-cols-3|"
     r"grid-template-columns:\s*repeat\(\s*3\s*,)", I),
    (15, "Pill/badge above headline", r"(\bv\d+\.\d+\b[^<\n]{0,40}(is here|now|new|launch)|"
     r">\s*(New|NEW|Beta|BETA|Just launched)\s*[·•|]?|Backed by Y ?Combinator|"
     r"rounded-full[^\"'\n]*(px-[23]|text-xs)[^\"'\n]*(border|bg-))", 0),
    (16, "The word 'real' (and kin)", r"\b(real|actually|genuinely|truly)\b", I),
    (17, "Stat-like number (verify it's sourced)", r"(\b\d{2}\.\d{1,3}\s*%|\b\d+(\.\d+)?\s*[KMB]\+|"
     r"\b\d{1,3}(,\d{3})+\+|\b\d+x\s+(faster|more|better)|\b\d+k\+)", I),
    (19, "Scroll fade-in", r"(IntersectionObserver|whileInView|data-aos|\bAOS\.init|ScrollTrigger|"
     r"\breveal\b|fade-?(in|up)|slide-?up|animate-on-scroll|useInView)", I),
    (20, "Dithering", r"(dither|halftone|bayer|floyd|steinberg)", I),
]

# Two-word sentences: 2+ consecutive "Word word." fragments in visible text.
STACCATO = re.compile(r"(?:\b[A-Z][\w'’-]*(?:\s+[\w'’-]+)?[.!]\s+){2,}")
CARD = re.compile(r"(\bcard\b|rounded-(xl|2xl|3xl)[^\"'\n]*\bborder\b|\bborder\b[^\"'\n]*rounded-(xl|2xl|3xl))", I)
TAG = re.compile(r"<[^>]+>")
CODEY = {".css", ".scss", ".sass", ".less"}


def files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, fs in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
                for f in fs:
                    if os.path.splitext(f)[1].lower() in EXTS and not f.endswith(".min.js"):
                        yield os.path.join(root, f)


def scan(path):
    hits = []
    ext = os.path.splitext(path)[1].lower()
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError as e:
        return [(0, 0, "error", str(e))]
    lines = text.splitlines()
    copy_only = {8, 16, 17}  # copy tells: skip in pure stylesheets
    for n, line in enumerate(lines, 1):
        if len(line) > 2000:
            line = line[:2000]
        for num, name, pat, fl in LINE_RULES:
            if ext in CODEY and num in copy_only | {2, 5, 9, 15}:
                continue
            m = re.search(pat, line, fl)
            if m:
                hits.append((n, num, name, m.group(0).strip()[:70]))
        if ext not in CODEY:
            visible = TAG.sub(" ", line)
            m = STACCATO.search(visible)
            if m and len(m.group(0).split()) <= 8:
                hits.append((n, 18, "Two-word sentences", m.group(0).strip()[:70]))
    if ext not in CODEY:
        cards = len(CARD.findall(text))
        if cards >= 6:
            hits.append((0, 7, "Everything in a card", f"{cards} card-like elements in file; check for nesting"))
    return hits


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__.strip())
        return 0
    total, by_tell = 0, {}
    for f in files(args):
        hits = scan(f)
        if not hits:
            continue
        print(f"\n{f}")
        for n, num, name, snippet in sorted(hits, key=lambda h: (h[0], h[1])):
            loc = f"{n}" if n else "-"
            print(f"  {loc:>5}  #{num:<2} {name}: {snippet}")
            by_tell[num] = by_tell.get(num, 0) + 1
            total += 1
    if total:
        print("\nSummary: " + ", ".join(f"#{k}×{v}" for k, v in sorted(by_tell.items())))
        print("Not machine-checkable, audit by eye: #3 overuse, #7 nesting, #9, #14, #18 tone.")
        return 1
    print("No mechanical tells found. Still audit #3, #7, #9, #14, #18 by eye.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
