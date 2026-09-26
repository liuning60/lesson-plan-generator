# Interaction Protocol (interaction-protocol)

Drives the "generate → review → iterate → finalize" loop. **Production lesson: the old three-number scoring (content/case/image 0-10) is unfriendly to lazy teachers and has been removed; replaced by a single-number command protocol.**

## Numeric Protocol (the only protocol)

After each session is generated, prompt the user to reply with **a single number** (no typing, lazy-friendly):

```
1 = continue to next session (this one is OK, pass)
0 = generate all remaining sessions, no more per-session review (whole-book mode)
2 = regenerate images
3 = regenerate cases
4 = regenerate content
5 / 6 / 7 = regenerate specified combinations (agree meanings on first interaction, e.g.
            5 = content+images, 6 = content+cases, 7 = cases+images)
9 = redo everything
```

- The number is the instruction; if parsing fails, restate the format and ask again — never guess.
- Natural confirmations like "ok", "good", "fine", or "1" also count as "continue to next session".
- In single-session mode, "continue" = finalize that session; in whole-book mode, "continue" = move to the next session.

## Regeneration Handling

- **2 images** → rerun the image engine (add/replace images, regenerate typo'd images), say which images changed.
- **3 cases** → rerun the case engine (re-search real cases / swap cases / strengthen six-element detail), say which case changed and how.
- **4 content** → rewrite richer (more detail, steps, logic; especially check implementation-process actionability and whether the time budget is fully filled).
- **5/6/7 combinations** → redo the agreed dimensions simultaneously.
- **9 all** → redo the whole session.
- After every redo, **say what changed** and ask for the number again.
- Max 3 automatic iterations per session; after 3, ask the user for specific changes — no infinite loops.

## Confirm & Continue

- User replies `1` (or ok/good/fine) = pass:
  - Single-session mode → finalize, output Word, task done.
  - Whole-book mode (default per-session review) → next session, repeat "generate → numeric confirm".
- User replies `0` → whole-book mode switches to fast mode: output all remaining sessions at once, no more per-session confirmation; when delivering, note "you can ask to adjust a specific session by number".

## Whole-Book Flow

1. Ask at start: per-session review (default) or fast mode (all at once)?
2. **Do pre-research & verify first** (see SKILL.md 3.1): search talent-training plans → draft ~500-word teaching objectives & content framework → user verifies (users read this carefully). After confirmation proceed to per-session or batch generation.
3. Per-session review: generate → numeric confirm → next on pass; assemble and deliver the whole book after all sessions pass.
4. Fast mode: generate all sessions from the verified framework at once; note that specific sessions can be adjusted on request.
5. After whole-book delivery, if the user flags a specific problem (e.g. images not showing in a session, missing content), redo that session by number; re-verify after regeneration (audit + per-session image count).

## Record

- Record each session's numeric feedback; reflect the user's choices (continue / redo dimension) in the delivery notes for the teacher's archive.
