# ScriptForge

ScriptForge is a Writer Modeling Engine — a system that learns how a specific 
person writes, and can then generate new handwritten text that behaves like 
that person's natural handwriting, rather than simply rendering pretty fonts.

The renderer is one application of the underlying Writer Model. The real goal 
is capturing and representing *how* someone writes: letterforms, spacing, 
drift, rhythm, and context-dependent variation — not just *what* their letters 
look like.

## Project Status: Architectural Pivot (V1 in progress)

ScriptForge originally began as a paper-based handwriting pipeline built 
around OpenCV (document preprocessing, contour detection, perspective 
correction, glyph segmentation). That work is preserved in this repo as a 
future **Paper Acquisition** module — it remains valuable for a subset of 
handwriting information (static glyph shape and geometry) and as a computer 
vision learning project in its own right.

The project has since pivoted to be **digital-first**. Writing captured 
directly on a touchscreen/trackpad canvas provides strictly more information 
than a scanned page — timestamps, stroke order, velocity, and pen-lift 
timing — none of which can be recovered from a static image. This unlocks a 
tractable path to real behavior modeling (via sequence models) rather than 
only static image synthesis.

**Current focus (V1): the Digital Writer Acquisition System only.**

Prompt shown → user writes on canvas → pointer events captured
→ raw strokes saved → Writer Profile grows over sessions

No ML, rendering, or handwriting generation yet. V1 is purely about 
collecting clean, structured, well-modeled raw handwriting data — 
correctly, once — so that every future version can extract more from it 
without ever asking the user to write again.

The V1 data model is frozen and documented in `docs/v1_data_model.md`.

## Tech Stack

- Python, OpenCV, NumPy — paper acquisition pipeline (existing)
- HTML/JS (Pointer Events API, Canvas) — digital acquisition prototype (new)
- Flask — UI only

## Project Structure

scriptforge/
│
├── engine/ # paper acquisition pipeline (OpenCV)
├── digital/ # digital acquisition system (new, in progress)
├── docs/ # dev journal, data model
├── tests/
├── data/
├── app.py
└── README.md

## Long-Term Vision

- A layered Writer Model: raw capture → derived features → learned 
  distributions → ML style embeddings — each layer regenerable from the 
  one below it, so no version ever requires re-collecting from the user
- A sequence-model-based renderer (pretrained on public online-handwriting 
  data, personalized per writer via fine-tuning on a small captured sample)
- Support for both Digital and Paper acquisition modes long-term, tagged 
  by provenance so their differing information density is never conflated
- Eventually: contextual letterforms, baseline/slant drift, writing rhythm, 
  and other natural writer-specific behaviors — learned, not hardcoded