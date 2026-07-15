# ScriptForge Development Journal

## Milestone 0 - Project Bootstrap

### Built
- Designed initial project architecture.
- Initialized Git repository.
- Connected GitHub remote.
- Created Python virtual environment.
- Configured .gitignore.
- Added README and requirements.txt.

### Learned
- Git workflow
- Virtual environments
- Project structure

### Notes
- Established package-based project layout.

## Milestone 1 - Image Loader

### Built
- Implemented reusable image loader.
- Added input validation.
- Added preprocessing loader test.

### Learned
- cv2.imread()
- NumPy image representation
- Separation of engine and tests

### Notes
- First reusable preprocessing module completed.

## Milestone 2 - Image Resize

### Built
- Implemented aspect ratio preserving resize.
- Added configurable target width.
- Added resize test module.

### Learned
- Aspect ratio
- cv2.resize()
- Running modules using `python -m`

### Notes
- Verified resize mathematically and visually.

## Milestone 3 - Grayscale Conversion

### Built
- Implemented grayscale conversion module.
- Added grayscale preprocessing test.
- Verified image shape transformation and visual output.

### Learned
- `cv2.cvtColor()`
- BGR → Grayscale conversion
- Image channel representation

### Notes
- Grayscale removes the color channel while preserving image dimensions.

# Current Pipeline

- [x] Image Loader
- [x] Image Resize
- [x] Grayscale
- [ ] Gaussian Blur
- [ ] Edge Detection
- [ ] Page Detection
- [ ] Perspective Transform
- [ ] Lighting Normalization
- [ ] Adaptive Threshold
- [ ] Morphology
- [ ] Character Segmentation
- [ ] Glyph Cleaning
- [ ] Glyph Library Builder
- [ ] Writer Profile Builder
- [ ] Layout Engine
- [ ] Handwriting Renderer
- [ ] Notebook Generator
- [ ] PNG/PDF Export