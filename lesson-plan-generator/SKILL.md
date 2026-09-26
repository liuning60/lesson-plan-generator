---
name: lesson-plan-generator
description: Generate lesson plans from a course name — full-term lesson plan books (cover + course info + per-session tables) or single sessions; apply school Word templates or refresh old lesson plans. Solves the two core AI lesson-plan weaknesses: hollow content (no concrete cases) and poor readability (no images). Ensures precise time budgeting and strict, submission-ready formatting. Use when the user asks to "generate a lesson plan", "write a lesson plan", "prepare a class", "create a lesson plan from a course name", "fill a school template", or "update an old lesson plan".
---

# Lesson Plan Generator

Generates Word lesson plans with concrete cases, images, exact time budgets, and strict formatting that teachers can submit directly. Collect required inputs before generating; emphasize **structured cases (six elements)** and **illustration minimums**; when applying a school template, fill its fields and preserve fixed content.

## Workflow Overview

1. **Collect inputs** (9 must-ask items + optional items, one question at a time)
2. **Confirm mode** (whole book / single session — always ask)
3. **Whole-book mode: pre-research & verify** (search talent-training plans → draft teaching objectives & content framework → user verifies)
4. **Generate content** (case engine + image engine + time budget, first session or whole book)
5. **Interactive review** (numeric protocol drives iteration)
6. **Output Word** (free layout / school template / old-plan update; formatting rules apply)

## 1 · Collect Inputs

Ask one question at a time (never dump all at once). Design replies to be lazy-user friendly: a number or single word should suffice.

**Must-ask (in order)**
1. **Mode**: whole-book lesson plan / single-session lesson plan (most important, see section 2)
2. **Level & subject**: secondary school / university (higher vocational 高职, secondary vocational 中职 follow university template); subject name
3. **Course name** (e.g. "Digital Visual Design", "VFX Production Techniques")
4. **Hours**: whole-book mode needs "weeks × sessions per week = total hours" (e.g. 18 weeks × 4 sessions = 72 hours → usually 18 sessions × 4 hours each); single-session mode needs hours of that session
5. **Course type & time composition**: pure theory / computer lab / lab + practice / mixed; sessions per week, lab vs practice split, session length (e.g. 4 sessions/week, 2 lab + 2 practice, 180 min per session). **Set the time budget before writing content** — never write content that under-fills or overflows the class time
6. **Image preference**: all AI-generated / web images first / mixed (case images prefer real web images with sources, the rest AI-generated). **Case images are the core** — real images for real cases are best; the rest AI-generated
7. **UI image option**: A = all AI-generated, no screenshot placeholders (recommended; teachers usually do not take their own screenshots); B = leave "insert XX screenshot here" placeholders
8. **Template**: whether to apply a school template (user provides .docx/.doc); when multiple school templates exist ask which one, or adapt any template via "read structure, fill by fields"
9. **Runtime platform**: default Doubao; options Doubao / Claude Code / Cursor / other — determines tool calls (see "Cross-Platform Tool Mapping" in section 4.5; the content flow is identical on all platforms)

**Optional** (fill if available, never block on them)
- Textbook name & edition
- Teaching objectives / requirements / differentiated instruction (group students by level?)
- Key points & difficulties
- Class, teacher, semester/academic year

**Fallback when only a course name is given**: first search online for the course's common textbook outline, chapter structure, syllabus, and relevant talent-training plans to build the content framework; content assembled from search must be marked "compiled from public sources, please verify with your teacher/school".

## 2 · Confirm Mode

- **Always ask**: generate everything at once (whole book) or a single session. Do not default, do not skip.
- **Single-session mode**: around the course's talent-training plan / objectives, generate one session → numeric review → finalize.
- **Whole-book mode**: default **session-by-session review** — generate one session, user confirms, continue; user reply `0` switches to one-shot generation of all remaining sessions without per-session confirmation.
- When asking about mode, also explain the numeric protocol (section 4) so users know how to reply from the start.

## 3 · Generate Content

### 3.1 Whole-book pre-research & verify (required; fixes "content without basis")
- Before generating sessions, **search the web for the course's talent-training plan / professional teaching standard** (e.g. MOE higher-vocational teaching standards, college talent-training plans) as the basis for teaching objectives.
- Produce an ~500-word **teaching objectives & content framework** (level & course goals → competency requirements → content modules & week arrangement) and **wait for user verification** (users read this carefully). Only after confirmation proceed to per-session or batch generation.
- Cite sources for anything retrieved; never invent specific figures without a reliable source.

### 3.2 Case engine (fixes hollow content; six elements)
- Embed a case in every knowledge/skill point in a fixed six-element structure (**no "teaching delivery advice" element**):
  `Background → relation to teaching objectives → implementation process (stepwise, actionable) → results & data → teaching comment → class questions (≥2)`
- **Results & data is optional**: not every case has public data; write "qualitative outcome, no public data" when absent — never fabricate numbers.
- Cases must be **detailed and actionable** (implementation process in steps, replicable operations); never write vague lines like "this case demonstrates XX".
- See `references/case-engine.md`.

### 3.3 Image engine (fixes poor readability)
- Image minimums by course type: **lab/practice courses ≥6 images/session; mixed ≥5; theory ≥4**.
- Combination strategy: case-related images prefer web search for real images (similar works, case screenshots, photos) with sources noted; the rest AI-generated teaching diagrams (**prompts must force "no watermark, no logo, no text watermark"**).
- UI option A: no screenshot placeholders; option B: write "insert XX screenshot here" placeholders.
- Check AI-generated images for OCR typos in embedded titles (common defect) and regenerate if found.
- See `references/image-engine.md`.

### 3.4 Time budget (budget first, then content; fixes "content can't fill the hours")
- Add a **"time arrangement"** line to every session table listing phases with minutes: introduction, lecture, demo, student practice, roving coaching, summary & comments.
- **Lab/practice phases must split into "student independent practice X min" + "teacher roving coaching X min"**.
- **All phase minutes must sum to the session total** (e.g. 4 hours = 180 min). Budget first, then write content.

### 3.5 Lesson plan structure
- Secondary vs university structures differ; pick by level; single-session vs whole-book differ; pick by mode.
- See `references/lesson-structures.md`.

## 4 · Interactive Review (numeric protocol, lazy-user friendly)

After each session, prompt the user to reply with **a single number** (no typing):

```
1 = continue to next session (this one is OK)
0 = generate all remaining sessions, no more per-session review (whole-book mode)
2 = regenerate images
3 = regenerate cases
4 = regenerate content
5 / 6 / 7 = regenerate specified combinations (agree the mapping on first interaction, e.g. 5=content+images, 6=content+cases, 7=cases+images)
9 = redo everything for this session
```

Rules:
- The number is the instruction; if parsing fails, restate the format and ask again — never guess.
- On regenerate triggers, rerun the corresponding engine (weak cases → re-search/swap; bad images → add/replace; hollow content → rewrite richer), say what changed, ask for the number again.
- Max 3 automatic iterations per session; after 3, ask the user for specific changes — no infinite loops.
- Full rules: `references/interaction-protocol.md`.

## 4.5 · Cross-Platform Tool Mapping

The content flow (collect → pre-research → cases → images → review → formatting → output) is platform-independent; only tool calls differ by host. Doubao is the default; on other platforms substitute the corresponding capability below — the flow and acceptance criteria stay the same:

| Capability | Doubao (default) | Claude Code / Cursor | Other AI |
|---|---|---|---|
| Web search (talent plans, cases) | general_search / web_fetch | web search / fetch tools | host search |
| Real case image search | image_search | platform image search | host image search |
| AI teaching image generation | image_gen | platform image generation | host image generation |
| Word create/template/audit | word skill (read.py / audit.py / catalogue.py / template branch) | python-docx + platform document tools (parse template → fill → verify) | host document capability (same acceptance criteria) |
| Local file / batch work | PowerShell / Python | Bash / Python | host shell |
| Image compression | Python + Pillow | same | same |

**Content protocols (must-asks / pre-research / six elements / time budget / numeric review / formatting rules) are identical on every platform** — only the tool channel differs.

## 5 · Output Word

- Default deliverable: editable Word (.docx), standard naming, no emoji.
- **Free layout**: standard structure per `references/lesson-structures.md` (cover → course info table → per-session tables).
- **School template**: user uploads template .docx (.doc converted to .docx baseline) → parse structure (cover / course info table / session tables) → fill by fields, keep fixed content, **clean example content and stale data (e.g. old-plan images)**.
- **Old-plan update**: user uploads old .docx → identify structure → targeted in-place updates only where the user asks.
- **Formatting rules (required; fixes "content crammed together")**: headings on their own lines (phase/case titles bold on their own line), content split into lines (① ② ③ each on its own line), case six elements as separate blocks (bold labels 【Background】【Implementation】【Results】【Teaching comment】【Questions】+ content lines), time arrangement on separate lines, line spacing 1.15, space before/after paragraphs, whitespace before images and after captions, caption for every image.
- **Size control**: compress AI images before embedding (long edge ≤1000px, JPEG quality 85) to avoid huge docx; clean template-borne legacy example images before generation.
- **File-lock handling**: if the target docx is open in Word it cannot be overwritten — output to a temp filename first (e.g. "-formatted-v2.docx"), verify, then ask the user to close the original before replacing; rerun audit after replacement.
- On **Doubao**, Word read/create/template/audit always uses the word skill flow (read.py, audit.py, catalogue.py, template branch) — never hand-roll a simplified reader; on other platforms substitute per the mapping table, keeping the same acceptance criteria.
- See `references/template-and-update.md`.

## Lessons Learned

This skill has been through a full production test (higher-vocational "Digital Visual Design", whole book, 18 sessions × 6 images). Discovered issues and fixes are recorded in `references/lessons-learned.md` — read it before executing, especially: template content-row location failures (locate by header row), duplicated time-arrangement lines, OCR typos in generated images, Word file locks, template legacy images bloating file size.

## Reference Docs

| File | Content |
|---|---|
| `references/lesson-structures.md` | Secondary / university, session / whole-book structures, formatting rules |
| `references/case-engine.md` | Six-element case format, dual-channel acquisition, built-in case templates |
| `references/image-engine.md` | Image minimums, web-vs-AI tradeoffs & copyright, watermark handling, UI image options, docx embedding & size control |
| `references/interaction-protocol.md` | Numeric protocol full rules, regeneration handling, whole-book flow |
| `references/template-and-update.md` | School-template and old-plan update flows, Word-lock replacement |
| `references/lessons-learned.md` | Production pitfalls (location failures, time duplication, OCR typos, size, replacement) and fixes |
