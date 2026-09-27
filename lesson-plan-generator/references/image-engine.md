# Image Engine (image-engine)

Goal: eliminate "walls of text" — every lesson plan is illustrated and readable. Lesson learned: software-operation/lab courses lose images the fastest; enforce **image minimums** and guard against two hard defects in AI-generated images: watermarks and OCR typos.

## Image Minimums (Required, by Course Type)

- **Lab / practice courses: ≥6 images per session**
- **Mixed courses (theory + lab): ≥5 per session**
- **Theory courses: ≥4 per session**

Verify per session in whole-book mode; any session below the minimum must be topped up. Batch generation must not "cut corners" — every session gets its full quota.

## Combination Strategy (by Priority)

1. **Case images prefer real web images**: for case-related content (real works, case screenshots, photos, similar works) use image search / general search.
   - Cases are the core — real images greatly boost persuasiveness (e.g. for an IP topic find Ling Na Bei Er or Pop Mart official images; for posters find famous posters).
   - Third-party images: note the source in the caption ("public case, compiled from sources — please verify"); never deliver a third-party URL as the artifact.
   - **Tradeoff rule**: web images only for "real case/work display"; skip images of uncertain copyright, with watermarks, or blurry — degrade to AI generation or placeholder. Let the user confirm adoption in interactive review (the "2 = regenerate images" dimension).
2. **AI-generated teaching diagrams**: when no suitable image is found (abstract content: flows, architectures, comparisons, diagrams, interface concepts), generate with the host image-generation capability.
   - **Force in prompts: "no watermark, no logo, no text watermark, no border"** — eliminates watermarks not allowed in teaching from the source.
   - For abstract visualization; caption notes "AI-generated".
   - **Check AI images for OCR typos after generation**: embedded titles/text often have typos (e.g. "color three elements" garbled). Regenerate any image with a typo — never ship a typo'd image.
3. **Placeholder fallback**: when nothing above fits (or the user chose UI option B), write "insert XX image here (suggested source: textbook page N / official site / photo)".

## UI Image Options (must-ask before generation)

- **Option A (recommended)**: all AI-generated teaching diagrams, **no screenshot placeholders**. Teachers usually don't take their own screenshots; A is less work and immediately usable.
- **Option B**: leave "insert XX screenshot here" placeholders for the teacher to add their own classroom screenshots later.

## Structural-Accuracy Risk (engineering courses — read first, v1.1)

For **structure-sensitive images** (equipment cutaways, section views, circuit diagrams, mechanical assemblies, piping layouts), AI generation can draw the **structure wrong** (flange reversed, wrong impeller blade count, wrong circuit connections, wrong piping direction) — far worse for teaching than a typo.

- For engineering courses, **structural/principle diagrams prefer web or teacher-provided images** (textbook figures, manufacturer manual figures, real photos); AI generation is only for rough illustration.
- If AI-generated, **verify the structure part by part** after generation: part counts, orientation, and connections against textbook common sense; when unsure, switch to a web image or a placeholder "insert textbook page N diagram here".
- This joins the OCR-typo check under the "2 = regenerate images" human-verification dimension.

## Sources & Copyright

- Prefer: textbook images, official sites, official case images, commercially usable sources (note author/site).
- Always note sources; skip images of uncertain copyright, degrading to AI generation or placeholder.
- Never deliver a third-party image URL as the artifact; real images enter the plan as "source note + caption".

## Position & Captions

- Place images near the knowledge point they illustrate, with a caption: "Fig N ｜ title ｜ source (AI-generated / public case)".
- Number captions continuously per session (Fig 1-1, 1-2 …; session N uses the N- prefix), consistent with the image folder naming (lesson<N>_img<M>.jpg).

## Embedding into docx & Size Control

- Insert images via the host's document flow (asset handling, proportional scaling, no cropping of original information).
- **Size control (a real production lesson)**: embedding 108 AI originals (2048px-class) directly balloons a docx to 240MB+. Compress before embedding: **long edge ≤1000px, JPEG quality 85** — 108 images total ~7-8MB; also strip legacy images from the source template (the template itself may be 40MB+; make an image-free clean copy before filling).
- Keep compressed and original images separately: originals (PNG) archived; compressed JPEGs used for embedding and the delivered image folder.
