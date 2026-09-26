# Lesson Plan Generator

Generate **submission-ready Word lesson plans** from a course name — whole-term lesson-plan books (cover + course info + per-session tables) or single sessions; apply school Word templates or refresh old lesson plans.

Solves the two core weaknesses of AI-generated lesson plans:
- **Hollow content** — every knowledge point embeds a six-element real case (Background / relation to objectives / implementation process / results & data / teaching comment / class questions); implementation steps are actionable; never fabricate data
- **Poor readability (no images)** — image minimums enforced (lab/practice ≥6 per session, mixed ≥5, theory ≥4); case images prefer real web images with sources; AI images are watermark-free and typo-checked

Also guarantees:
- **Exact time budgeting** — "time arrangement" row per session; lab phases split into "student independent practice + teacher roving coaching"; phase minutes sum to the session total
- **Strict formatting** — headings on their own lines, six-element case blocks, spacing rules — ready to submit
- **Lazy-friendly review** — reply with a single number (1 continue / 0 generate all / 2 images / 3 cases / 4 content / 5·6·7 combos / 9 redo)
- **Pre-research for whole books** — searches talent-training plans first, drafts a ~500-word objectives & content framework, waits for your verification

## Install (Doubao / Claude Code / Cursor and other Agent-Skills environments)

```bash
npx skills add https://github.com/liuning60/lesson-plan-generator -skill lesson-plan-generator
```

Or manual: copy the `lesson-plan-generator/` folder into your environment's skills directory and restart.

## Usage Example

> "Generate a whole-book lesson plan for 'Digital Visual Design', higher vocational, 18 weeks × 4 sessions/week, using the Zhengzhou Tourism College template"

Answer the 9 must-ask items (mode / level & subject / course name / hours / course type & time composition / image preference / UI image option / template / runtime platform) and get a whole-book or single-session plan.

## Cross-Platform

- Default runtime is Doubao; also runs on Claude Code / Cursor and others (see SKILL.md "Cross-Platform Tool Mapping" — the flow and acceptance criteria are identical, only the tool channel differs)
- Chinese version: https://github.com/liuning60/jiaoan-skill

## Layout

```
lesson-plan-generator/
├── README.md
├── LICENSE              (MIT)
└── lesson-plan-generator/        ← the skill (English)
    ├── SKILL.md
    └── references/
        ├── case-engine.md         six-element cases & retrieval strategy
        ├── image-engine.md        image minimums, watermarks, web-vs-AI, size control
        ├── interaction-protocol.md numeric review protocol
        ├── lesson-structures.md   university/secondary structures, time budget, formatting
        ├── template-and-update.md school templates, old-plan updates, pitfall fixes
        └── lessons-learned.md     production pitfalls & acceptance checklist
```

## License

MIT — free to use, modify, and redistribute, including commercially (see LICENSE).
