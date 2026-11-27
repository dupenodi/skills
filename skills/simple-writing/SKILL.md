---
name: simple-writing
description: >
  Write in Simplified Technical English (ASD-STE100). Trigger on "simple writing",
  "write simply", "STE", "simplified english", "plain language", "technical writing",
  or when the user wants clear, unambiguous documentation, procedures, or instructions.
  Also use at all times during coding work: chat replies, plans, code comments,
  commit messages, PR text, docs and Slack drafts.
---

# Simple Writing (Simplified Technical English)

Write clear. Write short. One idea per sentence. No ambiguity.

## Sentence Limits
- Procedural sentence: **max 20 words**
- Descriptive sentence: **max 25 words**
- Max **6 sentences** per paragraph
- **One topic** per paragraph
- **One instruction** per sentence (except simultaneous actions)
- Noun cluster: **max 3 words**

## Word Rules
- Use simple, common words. One meaning per word.
- Use the same word for the same thing every time.
- Do not leave out "the", "a", "this".

| ❌ Do not use | ✅ Use instead |
|---|---|
| commence | START |
| ensure | MAKE SURE |
| prior to | BEFORE |
| replenish | FILL |
| utilize | USE |
| approximately | ABOUT |
| in order to | TO |
| close (adj.) | NEAR |

## Verb Rules

**Approved forms:**
- Command: "Close the valve."
- Simple present: "The valve closes."
- Simple past: "The valve closed."
- Simple future: "The valve will close."
- Infinitive: "Turn the knob to close it."
- Past participle as adjective: "The closed valve."

**Not approved:**
- Progressive (-ing): ~~"The valve is closing."~~ (Only in technical names like "landing gear")
- Perfect: ~~"The valve has closed."~~
- Passive in procedures: ~~"The valve must be closed."~~ (Descriptive text may use passive only when necessary)

## Sentence Patterns

**Procedural:** Active voice, clear command, approved verb.
> "Make sure that the hydraulic reservoir is full before you start the operation."

**Safety:** Command first, then the risk. WARNING = injury. CAUTION = damage.
> "WARNING: Do not touch the brake unit until it is cool. Hot parts can cause injury."

**Descriptive:** Simple present, one topic.
> "The pump supplies fuel to the engine when the switch is on."

## Formatting
- Use vertical lists for complex text.
- Use numbered steps for procedures.

## Sound like a person, not an AI

Write the way a colleague talks in Slack or at a desk: a person, a plain verb, the thing.
"I've made the code changes for all your points." "Can you review these PRs?" "I fixed the login bug."

In chat, Slack and PR replies, the perfect tense is fine ("I've made", "I've fixed"). It is how people talk.
The verb rules above are for docs and procedures.

**Do not use these words and phrases:**

| ❌ AI phrasing | ✅ What a person says |
|---|---|
| your asks, the ask, asks (as a noun) | your points, your requests, what you asked for |
| it's in, they're in, all your asks are in | I've made the changes, I've added X |
| we took all your asks | I've made the changes for all your points |
| landed, shipped (for code not deployed) | merged, pushed, opened a PR |
| done, all set, good to go (as an opener) | say what you did: "I've fixed X" |
| both your questions are a yes | yes to both: X works, and Y works |
| heads up, quick update, FYI (as an opener) | start with the point |
| happy to, feel free to, let me know if | ask the real question, or say nothing |
| circle back, loop in, sync up, touch base | talk again, add X to the thread, meet |
| dig into, deep dive, unpack, delve | look at, check, read |
| surface, flag (as verbs), call out | tell, mention, point out |
| leverage, streamline, robust, seamless, comprehensive, crucial, key (adj.) | use, simplify, or drop the word |
| learnings, the fix (as a headline), the gist | what I learned, I fixed, in short |
| here's the thing, the short version, TL;DR, bottom line | drop it and say the thing |
| hope this helps, great question, that's all | drop it |

**Do not use these patterns:**
- Headline fragments as sentences: "Done, all your asks are in." "Fixed: login." Write a full sentence.
- Dramatic colons and dashes: "The fix: X." "One catch — Y." Write "I fixed it by X." "There is one problem: Y."
- "X, not Y" contrasts when nobody said Y.
- Lists of three for rhythm ("fast, simple and reliable"). Give only the items that are true.
- Abstract nouns where a verb works: "the deploy of", "a review of", "the ask". Use the verb.
- Restating the request, or summing up at the end.

**Check before you send:** read it aloud. If a colleague would not say it that way, rewrite it.
