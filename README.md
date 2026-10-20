# Claude Skills

My personal skills for Claude Code and Cursor. Each folder in `skills/` is one skill with a `SKILL.md`.

| Skill | What it does |
|---|---|
| `component-structure` | One folder per UI primitive with a tiny public export (Beautiful UI / shadcn layout rules) |
| `interface-design` | Crafted UI for dashboards, admin panels, SaaS apps and tools |
| `cs-concept-notes` | Course-style CS/engineering lessons in a patient-professor voice |
| `i-have-adhd` | Shapes responses for a reader with ADHD |
| `launch-video-studio` | Creative direction for motion/launch videos made in code |
| `product-launch-video` | Remotion workflow: brief → storyboard → render → review → iterate |

## Install

Copy or symlink a skill folder into your skills directory:

```sh
ln -s "$PWD/skills/component-structure" ~/.claude/skills/component-structure
ln -s "$PWD/skills/component-structure" ~/.cursor/skills/component-structure
```
