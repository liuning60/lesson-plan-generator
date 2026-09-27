# Case Engine (case-engine)

Goal: eliminate "hollow content" — every knowledge/skill point is supported by a **specific, verifiable, actionable** case. Lesson learned: hollow cases come from "background only, no process; concept only, no steps" — the six-element format forces cases to be real.

## Dual-Channel Acquisition

By priority:
1. **Search the web for real cases**: search by knowledge point/theme for real industry projects, official software cases, well-known works, current-event cases.
   - Example: for AE VFX, search actual production cases of a variety show intro or an ad; for digital visual design, search AI marketing campaigns, famous IPs, film cases.
   - Cite sources for retrieved cases; content compiled from search must note "public case, compiled from sources — please verify".
   - Case images should prefer real web images (see image-engine).
2. **Built-in case templates as fallback**: when no suitable case is found, generate one from the themed framework below so a case always exists.

## Structured Case Format (Six Elements, Required)

Each case outputs all six sections (no "teaching delivery advice" element):

```
Background            — what the case is, where/when/who
Relation to objectives — why this case teaches this point
Implementation process — how the teacher walks students through it (stepwise, actionable, ≥3 steps, each step a concrete action)
Results & data         — what was produced (work/data/result); if no public data write "qualitative outcome, no public data" — never fabricate numbers
Teaching comment       — what's good, what's easy to get wrong, what it transfers to
Class questions        — ≥2 questions for students (can include answer hints)
```

### Key Requirements (from production testing)
- **Implementation process must be detailed and actionable**: at least 3 steps, each written as "what to do, how" (e.g. "① set the character as a smart-but-playful pink fox, ② accumulate fans through park interaction and short-video personas") — never vague lines like "demonstrate the case".
- **Results & data is optional**: not every case has public data. Only write specific numbers with a reliable source (marked "compiled from public sources, please verify"); otherwise write qualitative outcome — **never invent data**.
- **Qualitative-outcome template (no public data, v1.1)**: write in the three-part form "what was done → what effect/standard was reached → verifiable basis"; never invent numbers. Examples:
  - "Students completed the《××》dynamic poster and it was played on the campus digital screen, meeting the client acceptance standard (in-class qualitative outcome, no public data)"
  - "The work was shortlisted for the campus innovation exhibition and passed instructor acceptance (qualitative outcome, no public quantitative data)"
- **Industry-academia link (optional, vocational schools, v1.1)**: for higher/secondary vocational courses, if a case's implementation maps to a real job task, add one line "industry-academia: corresponds to the ×× job task of the ×× course" (e.g. an e-commerce graphic designer's detail-page task). Write it when a clear job mapping exists, skip otherwise — never force or invent a job title.
- **Cases must serve the session's objectives**; no padding cases for bulk.
- At least 1 case per new knowledge point; 2 for key/difficult points (one deep + one transfer).

## Built-in Case Templates (Fallback, by Subject)

| Subject | Example framework |
|---|---|
| Computer / digital media | Real project review: an app/film/game segment → break down technical steps → students replicate key steps → compare with the original |
| Economics / management | Well-known corporate decision: background → data/decision → result → correspondence with theory → discussion points |
| Law / politics | Typical case or precedent: facts → disputed issue → ruling/basis → verification of concept → extended thinking |
| Language / literature | Close-reading case: excerpt → language features → link to theory/era → imitation task |
| Science/engineering / medicine | Classic experiment or accident: phenomenon → principle → supporting data → safety/ethics extension |
| Art / design | Masterpiece breakdown: work → technique/style elements → step demonstration → student creation task |
| Secondary school | Life-context case: scenario → knowledge link → inquiry activity → conclusion |

Fallback cases must be marked "example case — please replace with a local real case".

### Full Example (v1.1, for replication, engineering/medicine)

Using "centrifugal pump cavitation" (chemical-process machinery basics) as the full six-element example:

```
Background: A chemical plant's circulating-water pump lost flow and ran noisily after 3 months; inspection found honeycomb pitting at the impeller inlet.
Relation to objectives: teaches "cavitation and its hazards", grounding the abstract bubble theory in a real equipment failure.
Implementation process: ① show pump-disassembly photos/animation, locate the pitting; ② explain the cavitation chain: inlet pressure < vapor pressure → bubbles form → collapse at the high-pressure zone → impact erodes the metal surface; ③ use the NPSH (net positive suction head) formula to check whether this pump meets the requirement; ④ propose a fix (raise inlet level / replace pump).
Results & data: failure photos and maintenance records (class demo material, no public data — qualitative outcome).
Teaching comment: students easily confuse "cavitation" with "air binding" — cavitation is inside the impeller, air binding in the suction line; transferable to feed pumps, ship propellers, etc.
Class questions: ① Why does cavitation occur mostly at the back of the impeller inlet? ② How do you tell cavitation from air binding when pump flow drops?
```

> Frameworks are structure-only; production cases should be completed to the full form above; engineering courses should ship at least one full subject-specific example.

## Case Title Convention

Case title in the plan: `Case N (six elements) · case name` (e.g. "Case 1 (six elements) · Tmall 618 'AI Play Action'"). On render: case name bold on its own line; six elements as separate blocks (bold labels 【Background】【Relation to objectives】【Implementation process】【Results & data】【Teaching comment】【Questions】 + content lines) — see lesson-structures formatting rules.
