---
name: component-structure
description: >
  Place and author frontend UI as one folder per primitive with a tiny public
  export. Use when adding, moving, renaming, scaffolding, or refactoring React
  components, Beautiful UI / beautifui primitives, atoms, gallery cards, or
  component CSS; when choosing between atoms, primitives, app/, components/ui,
  or type-folders (hooks/, types/, styles/); when running shadcn add against
  the Beautiful UI registry; or when the user mentions component structure,
  file structure, or folder-per-component.
---

# Component structure

Every UI primitive is a **folder** with one public export. Group by the thing a caller imports, never by file type.

Read this before creating or moving any file under `components/` or adding CSS for a primitive.

## Canonical tree

```
app/                              # routes + global CSS only
  page.tsx
  globals.css                     # @import only
  styles/
    foundation.css                # Beautiful UI tokens / @theme / keyframes
components/
  atoms/                          # shared, no product meaning
    button.tsx
    entity-chip.tsx
    glide-menu.tsx
    shimmer.tsx
    stream-text.tsx
    value-pill.tsx
  primitives/
    approval-card/
      index.ts                    # public exports only
      approval-card.tsx
    records-table/
      index.ts
      records-table.tsx
      records-table.css           # only if Tailwind cannot express it
```

Callers import `@/components/primitives/approval-card`. Never a deep file path.

## Place it

| What | Where | Why |
| --- | --- | --- |
| Reused building block (`Button`, `GlideMenu`, `Shimmer`) | `components/atoms/<name>.tsx` | No product meaning. Flat until it needs a CSS companion. |
| Beautiful UI / product primitive (`ApprovalCard`, `PromptBar`) | `components/primitives/<kebab-name>/` | Always a folder. |
| Route / gallery / page composition | `app/**` | Screens assemble primitives. They do not own primitive source. |
| Design tokens, `@theme`, shared keyframes | `app/styles/foundation.css` | One global foundation. |
| Primitive-only CSS | next to that primitive | Owner is obvious. |
| shadcn leftover (`components/ui/*`) | do not add | Second Button. Ignore unless the user asks for shadcn UI. |

If unsure: **atom** if two or more primitives would import it; **primitive** if a human would name it on a gallery card; **page** if it wires data or navigation.

## Folder contents

Required:

- `index.ts` — re-export the component and its **public** types only
- `<name>.tsx` — UI + local UI state

Add only when the file is actually large or the extra file has a distinct job:

| File | When |
| --- | --- |
| `<name>.css` | Non-Tailwind rules (RecordsTable, SidebarNav) |
| `<name>.types.ts` | Public types used by several callers |
| `<name>.demo.ts` | Ice-cream / gallery fixtures |
| `use-<name>.ts` | Hook is a real public interface or reused |

Do **not** create `hooks/`, `types/`, `styles/`, `utils/` folders under a primitive. Do **not** create those folders under `components/` either.

Keep one `.tsx` until it hurts. `ApprovalCard` stays one file. `RecordsTable` may split CSS. Splitting early is noise.

## Public export

```ts
// components/primitives/approval-card/index.ts
export { default } from "./approval-card";
export type { ApprovalQuestion, ApprovalLabels } from "./approval-card";
```

Rules:

- Default export the component. Named-export public types.
- Demo constants, internal helpers, and CSS selectors stay private.
- Props take data in (`questions`, `rows`) and events out (`onSubmit`). No fetch, no route, no store.
- Ice-cream defaults belong in `<name>.demo.ts` or `app/page.tsx`, not baked into the primitive as the only way to render.

## CSS

1. Import foundation once from `app/globals.css`.
2. Co-locate owner CSS and `@import` it from `app/globals.css` (Tailwind v4).
3. Do not `@import "tailwindcss"` or `shadow-plugin` inside a primitive CSS file.
4. Paid `@central-icons-react` is banned. Use `lucide-react` and keep the same local names.

## New primitive

1. Create `components/primitives/<kebab-name>/`.
2. Write `<name>.tsx` + `index.ts`. CSS only if needed.
3. Import from the folder path on the page that uses it.
4. If installing from Beautiful UI: `npx shadcn add https://www.beautifului.dev/r/<name>.json`, then immediately move the dumped flat file into this folder and fix imports.

Registry items dump to `components/primitives/FooBar.tsx` and `app/beautifui/*.css`. That dump is not the finished layout — relocate the same turn.

## Forbidden

- New files in `components/ui/`
- Flat `components/primitives/FooBar.tsx` (legacy dump — migrate on touch)
- Cross-cutting `components/hooks`, `components/types`, `components/styles`
- Importing `@/components/primitives/approval-card/approval-card`
- Putting primitive source under `app/`
- A second `Button` (atoms already owns it)
- Copying `foundation.css` into a primitive folder

## On touch

If you open a flat primitive (`components/primitives/ApprovalCard.tsx`), migrate that one folder before adding features. Do not migrate the whole tree unless asked.

```
components/primitives/ApprovalCard.tsx
  → components/primitives/approval-card/approval-card.tsx
  → components/primitives/approval-card/index.ts
```

Update imports in the same turn. Leave siblings alone.
