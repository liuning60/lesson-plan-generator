# Production Pitfalls (lessons-learned)

This file records problems discovered and fixed during a real production run of lesson-plan-generator (higher-vocational "Digital Visual Design" whole book: 18 sessions × 6 images each = 108 images, using a college template). Read this before executing to avoid repeating the same mistakes.

## I. User Feedback (v1 → v2 redesign basis)

| # | Feedback | Final solution |
|---|---|---|
| 1 | No school template / formats differ by school | Template flow "read structure, fill by fields"; multiple templates supported; column mapping between template and content engine |
| 2 | Should search talent-training plans first and output teaching objectives & content for user verification (users read carefully, ~500 words) | Whole-book mode requires "pre-research & verify": search talent-training plans/teaching standards → ~500-word objective framework → user verifies before generation |
| 3 | Image count per session must have a minimum | Image minimums: lab/practice ≥6, mixed ≥5, theory ≥4 (per session) |
| 4 | Lazy review: reply with a number, no typing | Replaced three-number scoring with single-number protocol: 1 continue ｜ 0 generate all ｜ 2 images ｜ 3 cases ｜ 4 content ｜ 5/6/7 combos ｜ 9 redo all |
| 5 | Long class hours with not enough content; need detailed content with student practice and teacher coaching time | Time budget: "time arrangement" row in every session table; lab phases must split "independent practice X′ + roving coaching X′"; phase minutes sum to session total |
| 6 | Batch generation cut corners; software-operation courses missed images badly | Enforce image minimums; verify image counts per session; count blips per table after generation |
| 7 | AI images have watermarks, not allowed in teaching | Force "no watermark, no logo, no text watermark" in generation prompts; skip watermarked web sources |
| 8 | Web case images can be used directly; tradeoff needs user review | Case images prefer real web images with sources; skip uncertain copyright/watermark/blurry → degrade to AI or placeholder; user confirms via the image dimension (2) |
| 9 | Cases not detailed/actionable | Six-element case format: background/relation to objectives/implementation process (≥3 actionable steps)/results & data (write qualitative if none)/teaching comment/class questions (≥2) |

## II. v2 Additions (user-confirmed)

- **Differentiated instruction**: ask whether tasks should be leveled by student ability → added to must-ask items.
- **Image preference must-ask**: all AI / web-first / mixed; case images are core — real images best, rest AI.
- **UI image option must-ask**: A = all AI, no screenshot placeholders (teachers usually don't take their own screenshots); B = leave screenshot placeholders.
- **Six elements drop "teaching delivery advice"**: only six elements remain; results & data optional (not every case has data).
- **Numeric protocol refined**: 0 = generate all, no more review; removed three-number scoring; added combo numbers (5/6/7).
- **AI woven throughout (AIGC)**: all content uses AI (AI-generated assets, AI-assisted design, human judgment & refinement).

## III. Formatting Iteration ("content crammed together" problem)

| Version | Problem | Solution |
|---|---|---|
| v1 | Teaching process as long crammed text | Paragraph-ize: one paragraph per line + 1.15 line spacing + space before/after |
| v2 | Still long lines; phase/case titles not prominent | Headings on own lines: phase titles, case names, six-element labels, 【Time arrangement】 all bold on their own lines; content "① ② ③" each on its own line; lab splits "Task… / Independent practice 45′ roving coaching 15′"; assessment items each on own line |
| Final | Two time-arrangement lines (terse + detailed) | The data's first process line already contains 【Time arrangement】 — script no longer prepends another |

## IV. Engineering Pitfalls (full docx generation flow)

1. **Template legacy images bloat size**: template carried 194 legacy images (48.7MB) → make an "image-free clean copy" (remove w:drawing + media relationships + media files, 0.1MB) before filling → final 5.9-6.8MB.
2. **Originals bloat when embedded**: 2048px-class PNG ×108 → 246MB; compress to long edge 1000px JPEG quality 85 → 7.2MB.
3. **Missed-row location**: locate the content area by the row below the "Teaching content" header row, never by the content row's leading text (openings differ per table) → had missed sessions 13 & 15 (content + images empty, blips only 96/108).
4. **Cover space matching**: "主 讲 教 师 刘宁" contains spaces → strip spaces to match keywords, then replace the old value in the original run.
5. **Word-lock overwrite failure**: target open in Word → PermissionError; output a temp filename → user closes the original → Move-Item -Force replace → re-run audit + verification.
6. **OCR typos in generated images**: embedded titles garbled ("color three elements" etc.) → inspect every image, regenerate any with a typo.
7. **Delivery**: copy compressed images to a user-visible folder (lesson01-18 subdirectories) for self-check; deliver the docx via the presentation tool; state fill-in placeholders (instructor name / class / course code / title).

## IV.5. Community Review Feedback & v1.1 Improvements (xiaping trial)

After publishing the trial version on Xiaping, 8 reviews arrived (5× five-star + 3× four-star, weighted 4.6). Each was verified against the actual files; 5 adopted, 1 rejected:

| Source | Suggestion | Verification | Action |
|---|---|---|---|
| 燕老板 | Whole-book review is too heavy; add week/module spot checks | Partly true (0 = batch existed, no spot-check tier) | Added `W{week}` spot-check command + fast-track collection |
| 土匪 / QClaw | Weak coverage of engineering/other subjects; one-line templates, no full examples | True | Added full six-element "centrifugal pump cavitation" example; structural-risk note into image-engine |
| 燕老板 | Higher-vocational courses need industry-academia links; force job-task mapping | True | Added optional "industry-academia link" enhancement (not forced) |
| Liễu Hồ Yên Thiểm | No auto-validation script (time sums / image counts / OCR) | True | Added scripts/validate_lesson_plan.py (auto-checks time budget & image minimums) |
| QClaw | Results & data optional but no "qualitative description" template | True | Added three-part qualitative-outcome template in case-engine |
| 小阿飘Agent | image-engine.md / interaction-protocol.md are empty | **Not true** (both files complete; reviewer read them in a broken environment) | Not adopted |

## V. Acceptance Checklist (after every generation)

- [ ] Audit (--source clean template) exits 0
- [ ] Per-session image count = sessions × minimum per session (e.g. 18 × 6 = 108)
- [ ] Each session has exactly one 【Time arrangement】 line; phase minutes sum to session total
- [ ] Cover placeholders explicit (××× to fill); no invented instructor/class/course code
- [ ] No fabricated case data (no numbers without sources; write "qualitative outcome, no public data")
- [ ] No typo'd or watermarked images anywhere
- [ ] Template fixed content untouched; example content cleaned
