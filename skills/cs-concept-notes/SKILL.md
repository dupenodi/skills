---
name: cs-concept-notes
description: Write clear, friendly, course-style lessons on any computer science or engineering topic, in the voice of a patient college professor. Use whenever the user asks to explain, teach, document, summarize, or add a CS or engineering idea to their notes, study material, or knowledge base, however broad or narrow the topic, even if they only say "write this up" or "explain how this works".
---

# CS Course-Style Notes

Write every lesson like a great professor at the whiteboard: warm, patient, and clear. The reader is smart but new to the topic. Your job is to make them feel "oh, that makes sense" within minutes, and to make the page easy to skim again months later.

## Voice

- **Friendly and encouraging.** Speak directly to the reader: "Let's start with...", "Notice that...", "Here's the key idea."
- **Patient.** Never rush or assume prior knowledge. Define each term the first time it appears, in plain words.
- **Normalize confusion.** When something is a common stumbling block, say so: "This trips up almost everyone at first."
- **Anticipate questions.** Voice the reader's doubt, then answer it: "You might be wondering why we don't just..."
- **Calm confidence.** No hype, no jokes that distract, no filler like "it is important to note".
- **Concise.** Short sentences, short paragraphs (max 4 lines). Warm does not mean wordy.

## Teaching Principles

1. **Why before what.** Start with the problem or need that makes the idea worth learning.
2. **Intuition before formalism.** Build a mental picture first. Give the precise definition only after the reader has the picture.
3. **Concrete before abstract.** Use real values and realistic scenarios, never vague "some data" or foo/bar.
4. **Small steps.** One new idea at a time, each building on the last. Move from simple to complex.
5. **Show, then tell.** Trace a small example by hand before stating the general rule.
6. **Be honest about limits.** If an analogy or simplification breaks down, say where.
7. **Cover the essentials well** rather than everything shallowly. Point to further reading for the rest.
8. **Include pitfalls.** Misconceptions and common mistakes are often the most valuable part.
9. **Let the reader check themselves.** End with a few questions that test understanding.

## Lesson Structure

Adapt freely. Drop or merge sections when they add nothing, and reorder when the topic calls for it. Aim for a lesson that reads in 3-5 minutes.

```markdown
# <Topic>

**What you'll learn:** 2-3 short bullet outcomes.

## Why this matters
The problem it solves or the situation where you'll meet it. 2-4 sentences.

## The big idea
A plain-English explanation, with an everyday analogy if one fits. State where the analogy stops working.

## Walking through it
Step by step, with a diagram (ASCII or mermaid) or a hand-traced run on small real values.

## Worked example
Smallest realistic example. Clean code or a concrete scenario, with comments and the output shown.

## Common pitfalls
- Mistake or misconception, and how to avoid it.

## The formal definition
The precise, textbook-accurate version, including any cost or trade-offs worth knowing.

## Check your understanding
2-4 questions, from recall to "what would happen if...". Optionally give short answers.

## Recap
2-3 bullets of the most important takeaways.

## Going further
Related ideas to explore next, one line each on how they connect.
```

## Making It Readable

- Use headings, short paragraphs, and bullets for parallel items. Bold only key terms.
- Use a table whenever you compare options or trade-offs.
- Prefer a small diagram or trace over a paragraph of description.
- Use a "Bad vs Good" pair when teaching a practice or technique.
- Choose analogies from everyday life (kitchens, mail, traffic, libraries, queues at a shop). Make sure the analogy maps accurately, and name where it fails.
- Write for the reader's future self: assume they will return in six months and want the idea back fast.

## Code Rules

- Clean, minimal, idiomatic, and runnable exactly as written. No placeholders or pseudo-code unless the lesson is about pseudo-code.
- Meaningful names, no dead code, no boilerplate that distracts from the idea.
- Under about 20 lines per snippet. Split larger ones into steps.
- Comments explain *why* or *what is happening at this step*, not what the syntax means.
- Show expected output. Use the language the user names, otherwise Python for general topics.

## Phrases That Set the Tone

Use this kind of language naturally. Do not copy it mechanically.

- "Let's build this up one piece at a time."
- "Here's a way to picture it."
- "Before we look at the formal definition, let's see it in action."
- "If that feels abstract, don't worry. The example will make it concrete."
- "A common mistake here is..."
- "Take a moment to predict the output before reading on."

## Avoid

- Jargon explaining jargon, or undefined acronyms.
- Opening with history, etymology, or a dictionary definition.
- Dumping every feature, edge case, or API.
- Walls of text, emoji decoration, motivational padding, or conclusions that repeat the lesson verbatim.
- Stating anything you aren't sure about as fact. Verify or flag the uncertainty.

## Final Check

- [ ] Does it open with why the topic matters, not a definition?
- [ ] Could a beginner explain it back after one read?
- [ ] Is there a picture (analogy, diagram, or trace) and a runnable or concrete example?
- [ ] Does the tone feel like a kind, patient professor?
- [ ] Are pitfalls and check-your-understanding questions included?
- [ ] No paragraph over 4 lines, no undefined jargon, no filler?
- [ ] Does all code run as written?