# Claude Skills

The skills I use with Claude Code and Cursor. Each skill is a folder with a `SKILL.md`.

- `skills/`: skills I wrote.
- `third-party/`: open-licensed skills by other authors, copied unchanged with their licenses. Credit and copyright stay with those authors.

## My skills

| Skill | What it does |
|---|---|
| [`design-slop`](skills/design-slop) | Catches and removes AI design slop (20 tells, e.g. cream backgrounds, one italic headline word, three icon cards). Includes 20 UX laws to use instead and a scanner script. |
| [`component-structure`](skills/component-structure) | One folder per UI primitive with a tiny public export (Beautiful UI / shadcn layout rules). |
| [`cs-concept-notes`](skills/cs-concept-notes) | Course-style CS/engineering lessons in a patient-professor voice. |
| [`i-have-adhd`](skills/i-have-adhd) | Shapes responses for a reader with ADHD. |
| [`launch-video-studio`](skills/launch-video-studio) | Creative direction for motion/launch videos made in code. |
| [`product-launch-video`](skills/product-launch-video) | Remotion workflow: brief → storyboard → render → review → iterate. |

## Third-party skills included

| Folder | Author / source | License |
|---|---|---|
| [`third-party/mattpocock/`](third-party/mattpocock) | Matt Pocock, [mattpocock/skills](https://github.com/mattpocock/skills) @ `d574778` | MIT |
| [`third-party/interface-design/`](third-party/interface-design) | Damola Akinleye, [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) | MIT |
| [`third-party/img2threejs/`](third-party/img2threejs) | [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) @ `6e60b5e` | Apache-2.0 |
| [`third-party/anthropic/`](third-party/anthropic) | Anthropic, [anthropics/skills](https://github.com/anthropics/skills): `docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`, `theme-factory`, `web-artifacts-builder` | Apache-2.0 (per folder) |

The Matt Pocock skills are `ask-matt`, `code-review`, `codebase-design`, `diagnosing-bugs`, `domain-modeling`, `git-guardrails-claude-code`, `grill-me`, `grill-with-docs`, `grilling`, `handoff`, `implement`, `improve-codebase-architecture`, `prototype`, `research`, `setup-matt-pocock-skills`, `tdd`, `to-spec`, `to-tickets`, `triage`, `wayfinder` and `writing-great-skills`.

## Also in my setup, not copied here

These aren't openly licensed (or have no license), so get them from their source:

- **Anthropic, built into Claude:** `computer-use`, `chrome-browser`, `built-in-browser` (© Anthropic, all rights reserved), plus `docs`, `morning`, `deep-research`, `import-memory`, `google-workspace`.
- **Claude plugin skills:** `api-design-principles`, `database-schema-design`, `technical-rfc`, `writing-skills`, `web-design-guidelines`, `find-skills`, `minimi-memory-retrieval`.
- **Zoku app:** `zoku-orchestration`, installed by the Zoku app.

## Install

Copy or symlink a skill folder into your skills directory:

```sh
ln -s "$PWD/skills/design-slop" ~/.claude/skills/design-slop
ln -s "$PWD/skills/design-slop" ~/.cursor/skills/design-slop
```
