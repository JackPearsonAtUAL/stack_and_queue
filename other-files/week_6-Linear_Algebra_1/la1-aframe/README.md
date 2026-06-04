# Linear Algebra 1 — A-Frame 3D Visualisations

Interactive 3D scenes for each concept in the Linear Algebra 1 introduction.
No build step. No npm. Open `index.html` in a browser.

## Structure

```
la1-aframe/
├── index.html          ← landing page / table of contents
├── la-utils.js         ← shared math + A-Frame helpers (no numpy equivalent)
├── 01-vectors.html     ← Vectors: meaning and representation
├── 02-addition.html    ← Vector addition (tip-to-tail in 3D)
├── 03-scalar.html      ← Scalar multiplication
├── 04-dot.html         ← Dot product (three cases)
├── 05-cross.html       ← Cross product and parallelogram area
├── 06-normalise.html   ← Unit vectors and normalisation onto the unit sphere
├── 07-span.html        ← Span (line / plane / parallel cases)
├── 08-data.html        ← Vector representation of data (students in 3D feature space)
├── 09-transform.html   ← Linear transformations (interactive: identity/scale/rotate/shear)
└── 10-projection.html  ← Projection, residual, right-angle marker
```

## Dependencies

- [A-Frame 1.6](https://aframe.io) — loaded from CDN, no install needed
- `la-utils.js` — pure JS math helpers (vectors, dot, cross, norm, etc.)

## Controls

| Action | Control |
|---|---|
| Look around | Mouse drag |
| Move | W A S D |
| Back to index | Link top-right of each scene |

## Running locally

```bash
# Any static file server works — e.g.
python3 -m http.server 8080
# then open http://localhost:8080
```

Or just open `index.html` directly in Chrome/Firefox (A-Frame works without a server for local files).
