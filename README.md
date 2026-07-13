# ScriptForge

ScriptForge is a handwriting rendering engine that generates realistic handwritten notebook pages from user-provided handwriting samples.

Unlike traditional font generators, ScriptForge models a writer's handwriting by extracting glyphs from scanned templates and rendering arbitrary text using those glyphs while preserving the natural appearance of handwritten notes.

## Version 1 Goals

- Preprocess scanned handwriting pages
- Extract individual characters
- Build a reusable glyph library
- Generate realistic ruled notebook pages
- Export handwritten pages as PNG and PDF

## Tech Stack

- Python
- OpenCV
- NumPy
- Flask (UI only)

## Project Structure

```
scriptforge/
│
├── engine/
├── docs/
├── tests/
├── data/
├── app.py
└── README.md
```

## Current Status

🚧 Milestone 1: Document Preprocessing

The current focus is building a preprocessing pipeline capable of converting mobile-phone photographs of handwritten pages into clean scanner-like document images suitable for character extraction.

## Long-Term Vision

Future versions may include:

- Machine Learning based handwriting synthesis
- React frontend
- FastAPI backend
- User accounts
- Cloud deployment
- Multiple handwriting styles