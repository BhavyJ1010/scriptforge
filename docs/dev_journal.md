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

## Milestone 4 - Gaussian Blur

### Built
- Implemented Gaussian blur module.
- Added blur test module.
- Verified smoothing visually.

### Learned
- cv2.GaussianBlur()
- Kernel size
- Gaussian weighting
- Sigma

### Notes
- Blur reduces noise before edge detection.

## Milestone 5 - Document Contour Detection

### Built
- Implemented Canny edge detection.
- Added morphological closing for edge refinement.
- Implemented contour extraction and sorting.
- Added polygon approximation.

### Learned
- Canny edge detection
- Morphological closing
- Contour hierarchy and area
- Polygon approximation (approxPolyDP)

### Notes
- Clean contours require complete page boundaries.
- This stage prepares the image for perspective correction.

# Current Pipeline
- [x] Image Loader
- [x] Image Resize
- [x] Grayscale
- [x] Gaussian Blur
- [x] Edge Detection
- [x] Contour Detection
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