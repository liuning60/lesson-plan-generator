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

## Image Engine v1.4 (2026-10 upgrade)

Fixes two real-world pain points: "AI-generated images look bad" and "web-image-first still ends up 95% generated images".

- **Web-image-first actually works** — extract searchable entities from cases (work names / brand names / software UI / prototypes), search in both Chinese and English, filter ≥640px; only switch to AI generation after confirming the type has no web source (flows / principles / structures and other abstract diagrams)
- **Anti-AI-taste checklist** — no purple-blue gradients, no glassmorphism cards, no meaningless decoration, no fake chart clutter; no "8K / hyperreal" quality-word stacking
- **Texture discipline (absorbed from cinema-dna)** — banned prompt words (rich detail / epic / CGI render / game cinematic etc.), density restraint (1 primary clue + ≤1 secondary clue per image), one texture base per set, controlled imperfection
- **Realistic-image division of labor** — case works → web images first; objects/scenes → AI realistic (detailed photographic language: lens / light source / material / action); people & atmosphere → light accents only
- **7-point prompt self-check** — content correctness / text risk / AI-taste scan / negative words / type match / hard constraints / archive-ready; never send a prompt that fails any check
- **Prompts archived with images** — every generated image is saved with its full prompt (`lesson{N}-prompts.md`), traceable, reusable, re-generable
- **UI images: all types, default option B** — desktop software (incl. pro tools like CAD/MATLAB) / mobile apps / web pages; default "screenshot placeholder" for teachers to fill in real shots (AI always garbles pro-software UIs)
- **Free execution channel, no forced visual uniformity** — no paid image APIs; content/knowledge type outranks visual consistency

## Install

### Option 1: Xiaping marketplace (free trial, one-click)

Search for "Lesson Plan Generator" on Xiaping (https://xiaping.coze.com/skill/3b262f38-d510-4d93-87b6-f1565d599ab7), or just tell your agent "install the lesson-plan-generator skill".

### Option 2: GitHub (Doubao / Claude Code / Cursor and other Agent-Skills environments)

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
└── lesson-plan-generator/        ← the skill
    ├── SKILL.md
    └── references/
        ├── ai-image-engine.md      image enhancement: web-image-first, anti-AI-taste & texture discipline, 7-point prompt check & archiving (v1.4)
        ├── case-engine.md          six-element cases & retrieval strategy
        ├── image-engine.md         image minimums, watermarks, web-vs-AI, size control
        ├── interaction-protocol.md numeric review protocol
        ├── lesson-structures.md    university/secondary structures, time budget, formatting
        ├── template-and-update.md  school templates, old-plan updates, pitfall fixes
        └── lessons-learned.md      production pitfalls & acceptance checklist
```

## License

MIT — free to use, modify, and redistribute, including commercially (see LICENSE).
