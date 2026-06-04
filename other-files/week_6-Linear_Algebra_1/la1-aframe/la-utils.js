/* la-utils.js — shared helpers for all Linear Algebra A-Frame scenes */

// ── Pure math ──────────────────────────────────────────────────────────────
const LA = {
  add:  (a, b) => a.map((v,i) => v + b[i]),
  sub:  (a, b) => a.map((v,i) => v - b[i]),
  scale:(s, a) => a.map(v => v * s),
  dot:  (a, b) => a.reduce((s,v,i) => s + v*b[i], 0),
  mag:  a => Math.sqrt(a.reduce((s,v) => s + v*v, 0)),
  norm: a => { const m = LA.mag(a); return m ? a.map(v=>v/m) : a; },
  cross:(a, b) => [
    a[1]*b[2] - a[2]*b[1],
    a[2]*b[0] - a[0]*b[2],
    a[0]*b[1] - a[1]*b[0],
  ],
};

// ── A-Frame arrow (cylinder shaft + cone head) ────────────────────────────
// Returns an <a-entity> group representing an arrow from `from` to `to`.
function makeArrow(from, to, color='#5ec4ff', opacity=1, tubeR=0.03, headR=0.07, headH=0.18) {
  const dx = to[0]-from[0], dy = to[1]-from[1], dz = to[2]-from[2];
  const len = Math.sqrt(dx*dx + dy*dy + dz*dz);
  if (len < 1e-6) return document.createElement('a-entity');

  const wrap = document.createElement('a-entity');

  // Shaft
  const shaft = document.createElement('a-cylinder');
  shaft.setAttribute('radius', tubeR);
  shaft.setAttribute('height', Math.max(len - headH, 0.01));
  shaft.setAttribute('color', color);
  shaft.setAttribute('opacity', opacity);
  shaft.setAttribute('segments-radial', 8);

  // Head
  const head = document.createElement('a-cone');
  head.setAttribute('radius-bottom', headR);
  head.setAttribute('radius-top', 0);
  head.setAttribute('height', headH);
  head.setAttribute('color', color);
  head.setAttribute('opacity', opacity);
  head.setAttribute('segments-radial', 8);

  // Midpoint for shaft, tip offset for head
  const mx = from[0] + dx*0.5, my = from[1] + dy*0.5, mz = from[2] + dz*0.5;
  const hx = to[0] - dx/len*headH*0.5;
  const hy = to[1] - dy/len*headH*0.5;
  const hz = to[2] - dz/len*headH*0.5;

  shaft.setAttribute('position', `${mx} ${my} ${mz}`);
  head.setAttribute('position',  `${to[0]} ${to[1]} ${to[2]}`);

  // Rotation: default cylinder/cone point along Y; we need to rotate to (dx,dy,dz)
  const rotQuat = dirToQuat([dx,dy,dz]);
  shaft.setAttribute('rotation', rotQuat);
  head.setAttribute('rotation',  rotQuat);

  wrap.appendChild(shaft);
  wrap.appendChild(head);
  return wrap;
}

// Rotation string to align +Y to a target direction vector
function dirToQuat(dir) {
  const len = Math.sqrt(dir[0]*dir[0]+dir[1]*dir[1]+dir[2]*dir[2]);
  const d = [dir[0]/len, dir[1]/len, dir[2]/len];
  const up = [0,1,0];
  // cross up × d
  const axis = [
    up[1]*d[2]-up[2]*d[1],
    up[2]*d[0]-up[0]*d[2],
    up[0]*d[1]-up[1]*d[0],
  ];
  const axLen = Math.sqrt(axis[0]*axis[0]+axis[1]*axis[1]+axis[2]*axis[2]);
  if (axLen < 1e-6) {
    // parallel — either 0° or 180°
    if (d[1] > 0) return '0 0 0';
    return '180 0 0';
  }
  const angle = Math.acos(Math.max(-1, Math.min(1, up[0]*d[0]+up[1]*d[1]+up[2]*d[2])));
  const ax = [axis[0]/axLen, axis[1]/axLen, axis[2]/axLen];
  // Convert axis-angle to Euler (via THREE if available, else approximate)
  if (typeof THREE !== 'undefined') {
    const q = new THREE.Quaternion().setFromAxisAngle(
      new THREE.Vector3(...ax), angle);
    const e = new THREE.Euler().setFromQuaternion(q, 'XYZ');
    return `${THREE.MathUtils.radToDeg(e.x)} ${THREE.MathUtils.radToDeg(e.y)} ${THREE.MathUtils.radToDeg(e.z)}`;
  }
  // fallback: only exact for common cases
  const deg = angle * 180 / Math.PI;
  return `${ax[2]*deg} 0 ${-ax[0]*deg}`;
}

// ── Dashed line (series of small spheres) ─────────────────────────────────
function makeDashedLine(from, to, color='#444', steps=20, r=0.015) {
  const wrap = document.createElement('a-entity');
  for (let i=0; i<=steps; i++) {
    if (i%2===0) continue;
    const t = i/steps;
    const s = document.createElement('a-sphere');
    s.setAttribute('radius', r);
    s.setAttribute('color', color);
    s.setAttribute('position', `${from[0]+(to[0]-from[0])*t} ${from[1]+(to[1]-from[1])*t} ${from[2]+(to[2]-from[2])*t}`);
    wrap.appendChild(s);
  }
  return wrap;
}

// ── Floating text label ───────────────────────────────────────────────────
function makeLabel(text, pos, color='#ffffff', size=0.18) {
  const el = document.createElement('a-text');
  el.setAttribute('value', text);
  el.setAttribute('position', pos.join ? pos.join(' ') : pos);
  el.setAttribute('color', color);
  el.setAttribute('width', size * 14);
  el.setAttribute('align', 'center');
  el.setAttribute('side', 'double');
  return el;
}

// ── XYZ axis cross ────────────────────────────────────────────────────────
function makeAxes(len=2.5) {
  const wrap = document.createElement('a-entity');
  const axes = [[len,0,0,'#ff5555'],[0,len,0,'#55ff55'],[0,0,len,'#5599ff']];
  const neg  = [[-len,0,0,'#ff5555'],[0,-len,0,'#55ff55'],[0,0,-len,'#5599ff']];
  [...axes,...neg].forEach(([x,y,z,c]) => {
    wrap.appendChild(makeArrow([0,0,0],[x,y,z],c,0.5,0.015,0.04,0.1));
  });
  // labels
  [['X',[len+0.15,0,0],'#ff5555'],['Y',[0,len+0.15,0],'#55ff55'],['Z',[0,0,len+0.15],'#5599ff']].forEach(([t,p,c])=>{
    wrap.appendChild(makeLabel(t,p,c,0.14));
  });
  return wrap;
}

// ── Ground grid ───────────────────────────────────────────────────────────
function makeGrid(size=5, step=1, color='#1e1e2e') {
  const grid = document.createElement('a-entity');
  for (let i=-size; i<=size; i+=step) {
    ['x','z'].forEach(axis => {
      const line = document.createElement('a-entity');
      line.setAttribute('line', axis==='x'
        ? `start: ${i} 0 ${-size}; end: ${i} 0 ${size}; color: ${color}`
        : `start: ${-size} 0 ${i}; end: ${size} 0 ${i}; color: ${color}`);
      grid.appendChild(line);
    });
  }
  return grid;
}

// ── Standard scene shell ──────────────────────────────────────────────────
// Call after DOMContentLoaded; injects camera, sky, lights, grid, axes into <a-scene>
function buildScene(sceneEl, opts={}) {
  const {
    camPos = '4 3 7',
    showAxes = true,
    showGrid = true,
    skyColor = '#0a0a0f',
    gridSize = 5,
  } = opts;

  // Sky
  const sky = document.createElement('a-sky');
  sky.setAttribute('color', skyColor);
  sceneEl.appendChild(sky);

  // Lights
  [['ambient','#303050',1],['directional','#ffffff',0.8]].forEach(([type,color,intensity])=>{
    const l = document.createElement('a-light');
    l.setAttribute('type',type);
    l.setAttribute('color',color);
    l.setAttribute('intensity',intensity);
    if (type==='directional') l.setAttribute('position','3 6 4');
    sceneEl.appendChild(l);
  });

  // Camera
  const camWrap = document.createElement('a-entity');
  camWrap.setAttribute('position', camPos);
  const cam = document.createElement('a-camera');
  cam.setAttribute('look-controls', '');
  cam.setAttribute('wasd-controls', 'fly:true; acceleration:40');
  camWrap.appendChild(cam);
  sceneEl.appendChild(camWrap);

  if (showGrid) sceneEl.appendChild(makeGrid(gridSize));
  if (showAxes) sceneEl.appendChild(makeAxes(2));
}
