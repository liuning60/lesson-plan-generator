# School Template & Old-Plan Update (template-and-update)

Every school has its own lesson-plan format. This skill does not assume one format — it "reads the structure and fills by fields". Supports multiple templates: users can provide several school templates and pick one as the framework for this generation. Word read/write/acceptance follows the host's document capability (Doubao = word skill flow; other platforms per the SKILL.md cross-platform mapping), with identical acceptance criteria.

## Scenario A · Apply a School Template

User provides a school template .docx (.doc converted to .docx baseline first).

Flow:
1. **Read & parse the template structure** (via the host document flow):
   - Cover fields (school name, semester, department, instructor, course, class …)
   - Course info table columns (objectives, key points, methods, textbook …)
   - Per-session table columns (time, hours, mode, title, objectives, key points, content/methods, summary, homework)
   - Distinguish fixed content (e.g. "Issued by Academic Affairs Office", page setup, headers/footers) from example content: **example content gets replaced, fixed content is preserved**
2. **Build the column mapping**: template columns ↔ this skill's content-engine fields, forming a fill plan (template-plan).
3. **Fill by template**: cover with school info; info table with course info; each session table filled continuously by number, hours summing to the total; images inserted into corresponding columns per the image engine.
4. **Acceptance**: verify column by column against the template (audit + template-plan check); fixed content untouched, example content cleaned.

## Scenario B · Update an Old Lesson Plan

User provides an old .docx and states the updates.

Flow:
1. **Read the old plan**, identify its structure (cover / info table / session tables or single-session table).
2. **Collect update points**: new textbook / changed hours / replace cases / add knowledge points / update objectives etc. (user may describe in natural language).
3. **Targeted in-place update**: change only the columns/content the user named; everything else (paragraphs, tables, images, formatting) stays exactly as-is.
4. **Output the new Word**; also ask whether they want a "rewrite from scratch for the new course name" version for comparison.

## Production Pitfalls & Fixes (must follow)

### 1. Locating the template content row: by the "header row", never by the content row's leading text
- In the same template, each session table's content row may start with completely different text (e.g. one starts "Teaching process:", another "Split-noise:", "1. Fast box blur:").
- **Wrong**: locate by the content row's leading keywords ("teaching process"/"case steps") → tables with different openings are missed, leaving that session's content and images unfilled (in a real 18-session whole book, 2 sessions were missed).
- **Correct**: locate the "Teaching content" header row (fixed in every table), take the **first cell of the row below it** as the content area.

### 2. Cover replacement: watch for spaces
- Template covers often contain spaces ("主 讲 教 师 刘宁" = spaced text). Matching "主讲教师" directly fails. **Strip spaces before matching** (`text.replace(' ','')`), then locate the original run to replace.

### 3. Clean the template's legacy example content
- Old-plan templates may embed many legacy images (e.g. 194 images, 48MB). Before filling, make an "image-free clean copy" (remove all w:drawing, media relationships, media files); otherwise the output docx balloons (240MB+).
- Use the clean copy as the audit --source.

### 4. Image size control
- Compress generated images before embedding: long edge ≤1000px, JPEG quality 85; 108 images total ~7-8MB. Keep PNG originals archived separately.

### 5. Word file-lock: cannot overwrite while open
- Overwriting a docx open in Word raises PermissionError. Handle: generate to a temp filename first (e.g. "-formatted-v2.docx") → audit/verify → ask the user to close the original → replace (Move-Item -Force) → re-run audit and verification before delivery.
- When iterating, always output to a new temp filename to avoid locking yourself.

### 6. Don't duplicate the time-arrangement line
- If the data layer's first process line already contains "【Time arrangement】", don't prepend another one in the script (that yields two time lines, one terse one detailed). Render the original process list directly.

### 7. OCR typo check on generated images
- AI-generated image titles often have typos (e.g. "color three elements" garbled). Inspect every image before delivery and regenerate any with a typo.

## General Constraints

- All Word read/write/template/acceptance must use the host's full document flow — never hand-roll a simplified reader.
- Template example text and fictional data are not facts; the user's requirements and materials decide actual content.
- Don't touch template content the user didn't ask to change.
