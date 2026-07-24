# ScriptForge — Digital Acquisition Engine
## Architecture Document (V1)

This document defines the architecture of the Digital Writer Acquisition 
System before implementation. All code should be written against this 
document. If a decision here needs to change, update this document first, 
then change the code — not the other way around.

---

## 1. Purpose

The Digital Acquisition Engine's only responsibility is capturing raw 
handwriting data from a user, as faithfully and completely as possible, and 
saving it in a self-contained, forward-compatible format.

It does **not** do rendering, ML, feature extraction, or handwriting 
generation. Those are future systems that will consume what this engine 
produces.

---

## 2. Module Tree

```
digital/
  index.html
  style.css
  prompts/
    prompts_v1.json
  recordings/
  js/
    app.js
    ui.js
    canvas.js
    capture.js
    prompts.js
    exporter.js
    models/
      point.js
      stroke.js
      recording.js
      session.js
```

---

## 3. Module Responsibilities

**capture.js**
Listens to Pointer Events (`pointerdown`, `pointermove`, `pointerup`, 
`pointerleave`). Converts raw events into Point and Stroke data. Owns 
nothing about how strokes look on screen or how they get saved. Its only 
output is data.

**canvas.js**
Owns visual rendering only — drawing strokes to the screen as the user 
writes. Takes point/stroke data and draws it. Knows nothing about prompts, 
saving, or acquisition metadata. Could be swapped out (different pen style, 
smoothing, replay animation) without touching capture logic.

**prompts.js**
Loads `prompts_v1.json` and serves "what is the current prompt" and "what's 
next." Owns prompt ordering logic. Knows nothing about strokes or canvas.

**exporter.js**
Takes a completed Recording object, serializes it to JSON, and triggers a 
file download. Doesn't know how strokes were captured — only consumes the 
final Recording shape.

**ui.js**
Owns DOM manipulation: displaying prompt text, enabling/disabling buttons, 
advancing the visible prompt. Thin glue layer, no business logic.

**app.js**
The only module allowed to know about all the others. Owns current 
Recording/Session state. Coordinates actions: e.g., on Save click, asks 
capture.js for current strokes, builds a Recording, hands it to exporter.js, 
tells ui.js to advance to the next prompt.

---

## 4. Ownership Rule

> **Only `app.js` may coordinate other modules.**
> Every other module must be usable in isolation, without needing to know 
> the other modules exist.

If any module other than app.js needs to reach into another module's state 
directly, that's a sign the boundary is breaking down — route it through 
app.js instead.

---

## 5. Data Flow

Strictly one-directional:

```
Pointer Events
      ↓
capture.js  (produces Point/Stroke data)
      ↓
app.js  (holds current Recording state)
      ↓                    ↓
canvas.js              exporter.js
(displays strokes)     (saves Recording as JSON)

```

canvas.js and ui.js are pure output — they never feed data back upstream 
into capture.js or app.js's state.

---

## 6. Data Models (V1 — plain objects, not classes)

Plain objects for now. Promote to classes only if/when they gain real 
behavior (e.g. `stroke.duration()`, `recording.validate()`) — not before.

```
Point
  x
  y
  t              // ms, relative to stroke start

  pressure       // 0 when unavailable
  tilt_x         // 0 when unavailable
  tilt_y         // 0 when unavailable
  twist          // 0 when unavailable

Stroke
  id
  points[]       // list of Point

Recording
  schema_version
  prompt
    id
    version
    text
    category
  device
    pointer_type        // "pen" | "touch" | "mouse" | "unknown"
    device_pixel_ratio
    canvas_width
    canvas_height
  acquisition
    app_version
    recording_start_time
    mode                 // "digital"
  strokes[]      // list of Stroke

Session          // shape defined now, NOT wired up in V1
  id
  writer_id
  timestamp
  recordings[]   // list of Recording ids

Writer           // shape defined now, NOT wired up in V1
  id
  sessions[]     // list of Session ids

```

Note the split inside Recording: `device` and `acquisition` are **context 
metadata**, not writer-behavior data. Keep this distinction — it matters 
once feature extraction begins later, so context never gets conflated with 
signal.

---

## 7. Recording Schema Versioning

Every saved Recording begins with `schema_version`. When new fields are 
added later (e.g. `pressure` on Point), bump the version. Old recordings 
remain valid and parseable under their original version — nothing is ever 
retroactively rewritten.

---

## 8. Core Design Principle: Self-Contained Recordings

A single Recording JSON file must contain everything needed to replay, 
analyze, extract features from, or train on that writing instance — with no 
dependency on session state, app state, or any other file.

This is what makes "collect once, extract more later" true at the code 
level: as long as exporter.js always produces fully self-contained JSON, 
every other part of the system (UI, prompt library, even the entire 
frontend) can be redesigned later without touching already-collected data.

---

## 9. V1 Scope

In scope:
- Single canvas, prompt sequence loaded from prompts_v1.json
- Pointer Events capture (position, time, pointer type, pressure, tilt, twist)
- Save produces one self-contained Recording JSON, downloaded locally
- Prompt sequence loaded from `prompts_v1.json`

Explicitly out of scope for V1:
- Backend/database storage (local file download only for now)
- Session/Writer wiring (shapes defined, not implemented)
- Session/Writer wiring (shapes defined, not implemented)
- Backend/database storage (local file download only for now)
- Any ML, rendering, or replay
- Rejected-attempt retention (only the accepted recording is saved)
- Any ML, rendering, or replay
- Rejected-attempt retention (only the accepted recording is saved)

---

## 10. Future Extension Points (do not build now)

- Wire up Session → multiple Recordings per sitting
- Wire up Writer → multiple Sessions over time (incremental profile growth)
- Adaptive/targeted prompting based on Writer Profile gaps
- Annotation mode for character-level ground truth (V2 idea)
- Faint ruling on canvas to reduce baseline-drift acquisition noise

---

## 11. Git Discipline

Refactor `capture.js` into the module tree above. Verify exported JSON 
shape is unchanged before committing. Commit the refactor as one coherent 
milestone once verified — not mid-refactor.
```