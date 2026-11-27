---
name: design-slop
description: Catch and remove AI design slop — the visual and copy tells that make a page look machine-generated. Use when building or restyling any UI, landing page, website, artifact, deck or component, when reviewing a design, or when the user says something looks "AI-made", "generic", "templated" or "sloppy".
---

**Slop** is a default that got shipped without a reason. Each tell below is fine once, chosen on purpose. Slop is when it appears because it's what models reach for, and especially when several appear together. The test for every tell: *can I name why this page, for this product, needs it?* If not, it goes.

Source: two short-form reels, "20 AI Design Slop Indicators" and "20 Design Laws to Give Claude". The tells and laws below are transcribed from their example panels; the percentages quoted are the reel's own claims, not measured facts.

## Steps

1. **Before designing, pick a direction with a reason.** Write one sentence: who this is for and what the page must make them do or feel. Choose type, color and layout from that sentence, not from habit. If the plan resembles one of the **slop archetypes** below, change it now. Done when the sentence exists and no archetype matches.
2. **Build, applying the laws.** Use [DESIGN-LAWS.md](DESIGN-LAWS.md) whenever you make a form, flow, list, pricing table, onboarding, chart, empty state or confirmation. That's where the before/after fixes live.
3. **Scan.** Run `python3 -I ~/.claude/skills/design-slop/scripts/scan.py <files or dirs>` on the HTML/CSS/JSX/TSX/Vue/Svelte/MD you produced. It catches the mechanical tells (#1, 2, 4, 5, 6, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20) and flags candidates for the rest. It's a heuristic: a hit is a question, not a verdict.
4. **Audit all 20 tells by eye**, including the ones the scanner can't see (#3, 7, 9, 14, 18 are mostly judgment). Look at the rendered page (screenshot it if you can), not just the code. Done when every tell is either absent, removed, or kept with a one-line reason you could say to the user.
5. **Report** the tells you removed and any you kept deliberately, in one or two lines.

When **reviewing** someone else's design, run steps 3–4 and report hits as `#n Tell — where — what to do instead`.

Project taste beats this list. If the project has a documented deliberate style (e.g. a pixel-art world that uses dithering in transitions), that is a reason and the tell is not slop there.

## The 20 tells

| # | Tell | What it looks like (from the reel) | Do instead |
|---|---|---|---|
| 1 | **Arrows on every button** | "Deploy your first agent ↗", "Explore the SDK →". Reel: "Claude →, GPT ↗". | Plain verb labels. An arrow only where it carries meaning: ↗ for a link that truly leaves the site, → at most on one primary "next step". Never on every CTA. |
| 2 | **Interpuncts between words** | "macOS · Linux · Windows · MIT licensed"; also in bylines "Alba Ruiz · Producer, …". | Use real structure: a short sentence, commas, a list, or separate labeled items. |
| 3 | **Overused eyebrows** | Tiny uppercase, letter-spaced, often boxed or colored label above every heading: "THE GAP", "HOW IT WORKS", "■ SPECIALTY COFFEE. EVERYDAY MAGIC." Reel: "On 93% of AI pages". | Let the heading stand alone. If a section truly needs a category label, use one, once, and not on every section. |
| 4 | **Cream backgrounds** | Warm off-white page, "Often #F4F1EA", paired with a dark condensed serif and a red/oxblood accent. | Pick the background from the brand and content. Pure white, a cool grey, a real brand color or a dark theme are all fine. Cream needs a reason (print/paper metaphor the brand actually owns). |
| 5 | **One italic word in the headline** | "Ship from the *shell*.", "A better kind of *everyday*.", "Research, *illuminated*.", usually the italic word in a contrasting color. Reel: "On half of AI sites". | Set the headline in one style. Emphasis comes from the words. If one word must stand out, it should be the word a reader would stress out loud, and only in one headline on the page. |
| 6 | **Sparkle icons** | ✨ / four-point sparkle glyph on "Start for free", purple-to-pink gradient button. Reel: "On non-AI buttons too". | No icon on the CTA, or an icon that depicts the action. Sparkle never means anything; skip it even for AI features unless it's an established product convention. |
| 7 | **Everything in a card** | Feature blocks as bordered dark cards, each with its own eyebrow chip, title, paragraph, and a code block in a *nested* card. Reel: "Gemini's favourite". | Use whitespace, alignment and dividers to group (laws: proximity, common region). Reserve a card for an object the user acts on (an item, a plan, a file). Never cards inside cards. |
| 8 | **The word "quiet"** | "Four quiet rules". Reel: "Claude loves it". Same family: *unhurried*, *gently*, *calm*, *thoughtful*, *crafted*. | Say the concrete thing. "Four rules", or name what makes them so. |
| 9 | **Numbered sections** | Big thin italic serif "01", "02" (often in pale accent color) atop step cards: "Tell us your taste", "We roast to order". Reel: "On 17% of AI pages". | Number only real sequences the user follows, and then plain small numerals are enough. Otherwise drop the numbers. |
| 10 | **Pulsing green dots** | Status pill with a glowing/pulsing green dot + mono uppercase "CONSTELLATION 48/48 NOMINAL". Reel: "Every page is 'live'". | A status indicator only when it shows real, live state from a real source. Never decorative. |
| 11 | **Blurry glows behind the hero** | Soft radial color blobs (pale mint, purple) behind centered hero text. Reel: "Light with no source". | Flat background, a real image, or a deliberate graphic. If there's light, it should come from something on the page. |
| 12 | **Instrument Serif** | Condensed high-contrast display serif for headlines: "Be in the meeting.", "Coffee worth", "Intelligence, seen". Reel: "AI's go-to serif". | Choose a typeface for this brand's voice. If you want a serif, pick deliberately and avoid the current default (Instrument Serif; also watch for reflexive Fraunces / Playfair / DM Serif). |
| 13 | **Colored left borders** | Quote/callout with a thin red/accent left rule and italic serif text. Reel: "Claude's callout look". | Set quotes with typography (size, hanging quote marks, attribution). Callouts with background tint or an icon only if the content is a true warning or note. |
| 14 | **Three icon cards in a row** | Three equal cards, tiny tinted icon top-left, one-word title ("Declarative", "Fast", "Cross-platform"), two-line blurb. Reel: "The most common tell". | Show the product doing the thing: a screenshot, a real code sample, a demo, a comparison. If listing features, vary weight by importance (Pareto), don't force three equals. |
| 15 | **Pills above the headline** | Rounded chip above the H1: "v2.4 parallel sub-agents are here →", "Backed by Y Combinator │ W25", "New · AI-powered". Reel: "Says 'New' or 'v2.4'". | Put news in the body or a changelog. Social proof goes where it earns trust, not stacked on top of the H1. |
| 16 | **The word "real"** | "for people who do *the real work*." Reel: "Every model". Same family: *actually*, *genuinely*, *truly*. | Delete it, then say what makes the work or result specific. |
| 17 | **Made-up stats** | "RUNTIME UPTIME SLA 99.99%", "AGENT STEPS / MONTH 12B+", "10k+ teams", "10x faster". Reel: "Never measured". | Only numbers the user supplied or that come from a cited source. Otherwise use a qualitative claim or leave the slot out. Never invent a metric. |
| 18 | **Two-word sentences** | "One gateway. Every agent.", "Your books, done.", "Your models. Your frameworks. Your cloud." Reel: "GPT's favourite". | Write one plain sentence that says what the product does. Fragments in a staccato triplet are the tell. |
| 19 | **Sections fading on scroll** | Every section slides up and fades in as it enters the viewport. Reel: "Slide up, fade in, repeat". | Content is visible on arrival. Use motion only where it explains something (a state change, a transition the user caused), and respect `prefers-reduced-motion`. |
| 20 | **Dithering** | Ordered-dither / halftone dot imagery as decoration. Reel: "Dots only". | Use real photography or illustration. Dithering only when the art direction genuinely calls for it (retro/pixel aesthetic the project owns). |

## Slop archetypes

The tells cluster. If a design matches one of these, start over from step 1 rather than patching single tells:

- **Editorial cream:** #F4F1EA-ish background, condensed serif (Instrument Serif) headline with one red italic word, tracked-out uppercase eyebrow, "01 / 02" step cards, "unhurried"/"quiet" copy, left-border pull quote with "Name · Title" byline.
- **Dev-tool dark:** near-black background, huge sans headline with one neon-lime word, monospace uppercase labels, version pill above the H1, pulsing green status dot, nested cards with code blocks, invented uptime/throughput stats, staccato "One X. Every Y." copy.
- **SaaS glow:** centered hero on a pale radial gradient glow, "Backed by…" pill, two-line headline with the second line in brand color, three icon cards below, gradient CTA with sparkle and arrow, everything fading in on scroll.
