# Lesson Plan Generator

Generate **submission-ready Word lesson plans** from a course name — whole-term lesson-plan books (cover + course info + per-session tables) or single sessions; apply school Word templates or refresh old lesson plans.

Solves the two core weaknesses of AI-generated lesson plans:
- **Hollow content** — every knowledge point embeds a six-element real case (Background / relation to objectives / implementation process / results & data / teaching comment / class questions); implementation steps are actionable; never fabricate data
- **Poor readability (no images)** — image minimums enforced (lab/practice ≥6 per session, mixed ≥5, theory ≥4), counting **real images only**; deterministic diagrams are added as Word-native "supplementary content"

Also guarantees:
- **Exact time budgeting** — "time arrangement" row per session; lab phases split into "student independent practice + teacher roving coaching"; phase minutes sum to the session total
- **Strict formatting** — headings on their own lines, six-element case blocks, spacing rules — ready to submit
- **Lazy-friendly review** — reply with a single number (1 continue / 0 generate all / 2 images / 3 cases / 4 content / 5·6·7 combos / 9 redo)
- **Pre-research for whole books** — searches talent-training plans first, drafts a ~500-word objectives & content framework, waits for your verification

## Image Engine v1.5 (2026-10 rework)

"Images" vs "supplementary content" — fixes three real-world pain points: "AI-generated images look bad", "web-image-first still ends up 95% generated images", and "deterministic diagrams waste quota".

- **"Images" = strictly real pictures** — the image minimums (lab/practice ≥6 per session, mixed ≥5, theory ≥4) count only real images: real case-work shots, real software UI screenshots, real industry scenes / on-site photos, real output shots; sourced from the web with attribution
- **UI images = real screenshots (from the web)** — official software Help / real tutorial screenshots; no AI-faked UIs, no Word-drawn stand-ins; fall back to an "insert XX screenshot here" placeholder only when none can be found
- **Deterministic diagrams = Word native graphics (supplementary content)** — flows / structures / UI layouts / charts / trends drawn in Word (shapes + text boxes + arrows): zero quota, editable, **not counted in the image minimums**; trend/comparison charts must never fabricate data
- **AI generation = last resort** — only for case content that Word cannot draw AND no qualified real image can be found online (saves quota); when required, follow the anti-AI-taste checklist, texture discipline (from cinema-dna), 7-point prompt self-check and prompt archiving
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
        ├── ai-image-engine.md      image enhancement: real-image-first, Word native graphics, anti-AI-taste & texture discipline, 7-point prompt check & archiving (v1.5)
        ├── case-engine.md          six-element cases & retrieval strategy
        ├── image-engine.md         image minimums (real images only), Word supplementary graphics, size control
        ├── interaction-protocol.md numeric review protocol
        ├── lesson-structures.md    university/secondary structures, time budget, formatting
        ├── template-and-update.md  school templates, old-plan updates, pitfall fixes
        └── lessons-learned.md      production pitfalls & acceptance checklist
```

## License

MIT — free to use, modify, and redistribute, including commercially (see LICENSE).
