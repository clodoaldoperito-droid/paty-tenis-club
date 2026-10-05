import os

css_code = """/* ==========================================================================
   PATY TÊNIS CLUB - COMPACT LUXURY DARK DESIGN SYSTEM
   ========================================================================== */

:root {
  --bg-primary: #07080b;
  --bg-secondary: #0e1017;
  --bg-tertiary: #141722;
  --bg-glass-card: rgba(18, 22, 33, 0.75);
  
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-glow: rgba(0, 240, 255, 0.35);
  --border-gold: rgba(212, 175, 55, 0.35);

  --text-main: #f0f4f8;
  --text-muted: #95a3b8;
  --text-dim: #64748b;

  --accent-cyan: #00f0ff;
  --accent-gold: #ffd000;
  --accent-green: #00ff9d;

  --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-display: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;

  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-full: 9999px;

  --shadow-sm: 0 4px 12px rgba(0,0,0,0.3);
  --shadow-glow: 0 0 25px rgba(0, 240, 255, 0.25);
  --shadow-gold: 0 0 25px rgba(212, 175, 55, 0.2);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-main);
  background-color: var(--bg-primary);
  color: var(--text-main);
  line-height: 1.5;
  overflow-x: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}

/* Ambient glow orbs */
.glow-sphere {
  position: fixed;
  border-radius: 50%;
  filter: blur(140px);
  pointer-events: none;
  z-index: 0;
  opacity: 0.12;
}

.glow-cyan {
  top: -10%;
  left: -5%;
  width: 500px;
  height: 500px;
  background: var(--accent-cyan);
}

.glow-gold {
  bottom: 10%;
  right: -5%;
  width: 450px;
  height: 450px;
  background: var(--accent-gold);
}

.container {
  width: 100%;
  max-width: 1180px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 1;
}

.flex-center-between {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.text-center {
  text-align: center;
}

.text-gradient-cyan {
  background: linear-gradient(135deg, #00f0ff 0%, #8000ff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.text-gradient-gold {
  background: linear-gradient(135deg, #ffe066 0%, #d4af37 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.text-gold {
  color: var(--accent-gold);
}

/* Announcement Bar - Mais fino */
.announcement-bar {
  background: linear-gradient(90deg, rgba(0, 240, 255, 0.08) 0%, rgba(112, 0, 255, 0.1) 100%);
  border-bottom: 1px solid rgba(0, 240, 255, 0.15);
  font-size: 12px;
  padding: 6px 0;
  font-weight: 600;
}

.badge-live {
  color: var(--accent-green);
  font-size: 11px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.announcement-text {
  color: var(--text-muted);
}

.announcement-link {
  color: var(--accent-cyan);
  text-decoration: none;
  font-weight: 700;
}

/* Header - Mais compacto */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  background: rgba(7, 8, 11, 0.85);
  border-bottom: 1px solid var(--border-subtle);
  padding: 10px 0;
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-display);
}

.logo-brand {
  font-size: 18px;
  font-weight: 800;
  color: #fff;
}

.logo-club {
  font-size: 18px;
  font-weight: 800;
  color: var(--accent-cyan);
}

.tag-vip {
  font-size: 9px;
  background: rgba(212, 175, 55, 0.15);
  color: var(--accent-gold);
  border: 1px solid var(--border-gold);
  padding: 2px 6px;
  border-radius: var(--radius-sm);
  font-weight: 800;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 24px;
}

.nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  transition: color 0.2s;
}

.nav-links a:hover {
  color: var(--accent-cyan);
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: var(--font-main);
  font-size: 13px;
  font-weight: 700;
  padding: 10px 20px;
  border-radius: var(--radius-full);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.25s ease;
  border: 1px solid transparent;
}

.btn-lg {
  padding: 13px 26px;
  font-size: 15px;
}

.btn-block {
  width: 100%;
}

.btn-primary {
  background: linear-gradient(135deg, #00f0ff 0%, #0088ff 100%);
  color: #07080b;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-glow);
  filter: brightness(1.1);
}

.btn-gold {
  background: linear-gradient(135deg, #ffe066 0%, #d4af37 100%);
  color: #07080b;
}

.btn-gold:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-gold);
}

.btn-outline {
  background: rgba(255, 255, 255, 0.03);
  color: var(--text-main);
  border: 1px solid var(--border-subtle);
}

.btn-outline:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
}

.btn-glow {
  box-shadow: 0 0 16px rgba(0, 240, 255, 0.25);
}

/* Glass panel */
.glass-panel {
  background: var(--bg-glass-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
}

/* Section Spacing Controls (Drasticamente reduzidos) */
section {
  padding: 48px 0;
  position: relative;
}

.section-header {
  margin-bottom: 28px;
}

.section-tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: var(--accent-cyan);
  text-transform: uppercase;
  margin-bottom: 8px;
}

.section-title {
  font-family: var(--font-display);
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.15;
  margin-bottom: 10px;
}

.section-description {
  font-size: 15px;
  color: var(--text-muted);
  max-width: 620px;
  margin: 0 auto;
  line-height: 1.5;
}

/* Hero Section */
.hero-section {
  padding: 36px 0 44px;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 36px;
  align-items: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(0, 240, 255, 0.08);
  border: 1px solid rgba(0, 240, 255, 0.2);
  padding: 4px 14px;
  border-radius: var(--radius-full);
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  color: var(--accent-cyan);
  margin-bottom: 16px;
}

.pill-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent-cyan);
  box-shadow: 0 0 8px var(--accent-cyan);
  animation: pulse 1.8s infinite;
}

@keyframes pulse {
  0% { transform: scale(0.9); opacity: 0.7; }
  50% { transform: scale(1.4); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.7; }
}

.hero-title {
  font-family: var(--font-display);
  font-size: 44px;
  line-height: 1.1;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 16px;
}

.hero-subtitle {
  font-size: 16px;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 24px;
  max-width: 560px;
}

.hero-cta-group {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
}

.hero-stats-row {
  display: flex;
  align-items: center;
  gap: 24px;
  padding-top: 16px;
  border-top: 1px solid var(--border-subtle);
}

.stat-box {
  display: flex;
  flex-direction: column;
}

.stat-num {
  font-family: var(--font-display);
  font-size: 26px;
  font-weight: 800;
  color: #fff;
  line-height: 1;
}

.stat-label {
  font-size: 11px;
  color: var(--text-dim);
  text-transform: uppercase;
  font-weight: 700;
  margin-top: 4px;
}

.stat-separator {
  width: 1px;
  height: 28px;
  background: var(--border-subtle);
}

/* Hero Visual / 3D Card */
.hero-card-3d {
  position: relative;
  border-radius: 24px;
  background: linear-gradient(145deg, rgba(22, 27, 40, 0.8), rgba(11, 14, 20, 0.95));
  border: 1px solid rgba(0, 240, 255, 0.2);
  padding: 12px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.6), 0 0 30px rgba(0, 240, 255, 0.12);
  transition: transform 0.2s cubic-bezier(0.1, 0.9, 0.2, 1);
  transform-style: preserve-3d;
}

.hero-img-render {
  width: 100%;
  height: auto;
  border-radius: 16px;
  display: block;
}

.floating-badge {
  position: absolute;
  background: rgba(11, 14, 20, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid var(--border-subtle);
  padding: 6px 12px;
  border-radius: var(--radius-full);
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.05em;
  box-shadow: var(--shadow-sm);
}

.badge-top-right {
  top: 20px;
  right: 20px;
  color: var(--text-main);
}

.dot-green {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent-green);
  margin-right: 4px;
}

.floating-hud {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background: rgba(7, 9, 14, 0.9);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(0, 240, 255, 0.25);
  padding: 10px 14px;
  border-radius: var(--radius-md);
  font-size: 10px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.5);
}

.hud-header {
  font-size: 8px;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: var(--accent-cyan);
  margin-bottom: 4px;
}

.hud-row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 2px;
}

.hud-row span {
  color: var(--text-muted);
}

.hud-row strong {
  color: #fff;
}

/* Timeline / Como Funciona */
.timeline-section {
  background: rgba(14, 16, 23, 0.4);
}

.timeline-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.timeline-card {
  padding: 22px 18px;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--border-subtle);
  transition: transform 0.25s, border-color 0.25s;
}

.timeline-card:hover {
  transform: translateY(-4px);
  border-color: rgba(0, 240, 255, 0.35);
}

.timeline-step {
  font-family: var(--font-display);
  font-size: 11px;
  font-weight: 800;
  color: var(--accent-cyan);
  letter-spacing: 0.08em;
  margin-bottom: 6px;
}

.timeline-card h4 {
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 8px;
}

.timeline-card p {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 14px;
  flex-grow: 1;
}

.timeline-tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  background: rgba(0, 255, 157, 0.1);
  color: var(--accent-green);
  border: 1px solid rgba(0, 255, 157, 0.25);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  align-self: flex-start;
}

/* 3D Exploded View */
.exploded-section {
  background: radial-gradient(circle at 50% 50%, rgba(16, 22, 34, 0.35) 0%, rgba(7, 8, 11, 0) 70%);
}

.exploded-showcase-container {
  display: grid;
  grid-template-columns: 1.35fr 0.85fr;
  gap: 28px;
  align-items: center;
}

.exploded-image-wrapper {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  background: #0b0d13;
  border: 1px solid var(--border-subtle);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7);
}

.exploded-img {
  width: 100%;
  height: auto;
  display: block;
}

/* Hotspot Pins */
.hotspot-pin {
  position: absolute;
  width: 22px;
  height: 22px;
  border: none;
  background: transparent;
  cursor: pointer;
  z-index: 10;
  transform: translate(-50%, -50%);
}

.pin-core {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--accent-cyan);
  box-shadow: 0 0 10px var(--accent-cyan);
  transition: transform 0.2s, background 0.2s;
}

.pin-wave {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid var(--accent-cyan);
  animation: ripple 2s infinite ease-out;
}

@keyframes ripple {
  0% { transform: translate(-50%, -50%) scale(0.6); opacity: 1; }
  100% { transform: translate(-50%, -50%) scale(2.0); opacity: 0; }
}

.pin-label {
  position: absolute;
  left: 24px;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(11, 14, 20, 0.92);
  backdrop-filter: blur(8px);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-glow);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0.85;
}

.hotspot-pin:hover .pin-core,
.hotspot-pin.active .pin-core {
  background: #fff;
  transform: translate(-50%, -50%) scale(1.3);
  box-shadow: 0 0 16px #fff, 0 0 20px var(--accent-cyan);
}

.hotspot-pin:hover .pin-label,
.hotspot-pin.active .pin-label {
  opacity: 1;
  border-color: #fff;
}

/* Inspector Card */
.exploded-inspector-card {
  padding: 26px 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 360px;
  border: 1px solid rgba(0, 240, 255, 0.25);
}

.inspector-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 16px;
}

.tech-id {
  font-size: 10px;
  font-family: var(--font-display);
  color: var(--accent-cyan);
  font-weight: 700;
  letter-spacing: 0.05em;
}

.tech-dots span {
  display: inline-block;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--border-subtle);
  margin-left: 3px;
}

.spec-title {
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 800;
  margin-bottom: 6px;
  color: #fff;
}

.spec-badge {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  color: var(--accent-green);
  background: rgba(0, 255, 157, 0.1);
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  margin-bottom: 12px;
}

.spec-text {
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 18px;
}

.spec-metrics {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-top: 10px;
}

.metric-box {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-subtle);
  padding: 12px;
  border-radius: var(--radius-md);
}

.metric-value {
  display: block;
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 800;
  color: var(--accent-cyan);
}

.metric-label {
  font-size: 10px;
  color: var(--text-dim);
  text-transform: uppercase;
  font-weight: 700;
}

.inspector-footer {
  font-size: 10px;
  color: var(--text-dim);
  font-weight: 700;
  letter-spacing: 0.08em;
  padding-top: 14px;
  border-top: 1px solid var(--border-subtle);
}

/* Unboxing Section */
.unboxing-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 36px;
  align-items: center;
}

.unboxing-glow-box {
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid var(--border-gold);
  box-shadow: 0 15px 35px rgba(0,0,0,0.7), 0 0 35px rgba(212, 175, 55, 0.12);
}

.unboxing-img {
  width: 100%;
  height: auto;
  display: block;
}

.unboxing-p {
  font-size: 15px;
  color: var(--text-muted);
  margin-bottom: 20px;
}

.box-perks-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 24px;
}

.box-perk-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.perk-icon-gold {
  font-size: 20px;
  width: 38px;
  height: 38px;
  border-radius: var(--radius-md);
  background: rgba(212, 175, 55, 0.1);
  border: 1px solid var(--border-gold);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.box-perk-item h4 {
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 2px;
}

.box-perk-item p {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.4;
}

/* Catalog Section */
.catalog-filter-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin-top: 20px;
}

.filter-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  padding: 8px 16px;
  border-radius: var(--radius-full);
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover,
.filter-btn.active {
  background: var(--accent-cyan);
  color: #07080b;
  border-color: var(--accent-cyan);
  box-shadow: 0 0 12px rgba(0, 240, 255, 0.3);
}

.catalog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 18px;
  margin-top: 28px;
}

.sneaker-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 18px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s, border-color 0.2s;
}

.sneaker-card:hover {
  transform: translateY(-4px);
  border-color: rgba(0, 240, 255, 0.35);
  box-shadow: 0 10px 25px rgba(0,0,0,0.5);
}

.card-brand-badge {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--accent-cyan);
  text-transform: uppercase;
  margin-bottom: 4px;
}

.card-title {
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 4px;
}

.card-category {
  font-size: 11px;
  color: var(--text-dim);
  margin-bottom: 12px;
}

.card-sizes {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
  margin-bottom: 14px;
}

.size-pill {
  font-size: 10px;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-subtle);
  color: var(--text-muted);
  padding: 2px 6px;
  border-radius: var(--radius-sm);
}

.size-pill.available {
  border-color: rgba(0, 255, 157, 0.3);
  color: var(--accent-green);
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 12px;
  border-top: 1px solid var(--border-subtle);
}

.card-price-ref {
  font-size: 10px;
  color: var(--text-dim);
}

.card-price-val {
  font-size: 14px;
  font-weight: 700;
  color: #fff;
}

.btn-card-select {
  font-size: 11px;
  padding: 6px 12px;
  border-radius: var(--radius-full);
  background: rgba(0, 240, 255, 0.1);
  color: var(--accent-cyan);
  border: 1px solid rgba(0, 240, 255, 0.3);
  text-decoration: none;
  font-weight: 700;
  transition: all 0.2s;
}

.btn-card-select:hover {
  background: var(--accent-cyan);
  color: #07080b;
}

.catalog-footer-note {
  text-align: center;
  margin-top: 24px;
  font-size: 13px;
  color: var(--text-muted);
}

/* Centered Pricing Wrapper */
.pricing-wrapper-centered {
  max-width: 680px;
  margin: 0 auto;
}

.pricing-card {
  padding: 36px 32px;
  position: relative;
  display: flex;
  flex-direction: column;
}

.featured-tier {
  border: 2px solid var(--accent-cyan);
  background: linear-gradient(160deg, rgba(20, 26, 40, 0.85) 0%, rgba(9, 12, 18, 0.95) 100%);
  box-shadow: 0 20px 45px rgba(0,0,0,0.6), 0 0 35px rgba(0, 240, 255, 0.18);
}

.featured-ribbon {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(90deg, #00f0ff, #7000ff);
  color: #07080b;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 3px 14px;
  border-radius: var(--radius-full);
}

.card-tier-badge {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: var(--accent-cyan);
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tier-name {
  font-family: var(--font-display);
  font-size: 26px;
  font-weight: 800;
  margin-bottom: 8px;
  color: #fff;
}

.tier-desc {
  font-size: 14px;
  color: var(--text-muted);
  margin-bottom: 18px;
}

.price-block {
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-bottom: 4px;
}

.price-block .currency {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-muted);
}

.price-block .amount {
  font-family: var(--font-display);
  font-size: 46px;
  font-weight: 800;
  color: #fff;
}

.price-block .period {
  font-size: 14px;
  color: var(--text-muted);
}

.price-sub {
  font-size: 13px;
  color: var(--accent-green);
  font-weight: 600;
  margin-bottom: 18px;
  display: block;
}

.shipping-notice {
  background: rgba(255, 193, 7, 0.08);
  border: 1px solid rgba(255, 193, 7, 0.25);
  padding: 10px 14px;
  border-radius: var(--radius-md);
  margin-bottom: 22px;
  font-size: 12px;
  line-height: 1.5;
  color: #f1f5f9;
}

.tier-features {
  list-style: none;
  margin-bottom: 26px;
}

.tier-features li {
  font-size: 13px;
  color: var(--text-muted);
  margin-bottom: 10px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.security-banner {
  text-align: center;
  margin-top: 14px;
  font-size: 11px;
  color: var(--text-dim);
}

/* FAQ Section */
.faq-container {
  max-width: 760px;
}

.faq-accordion {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.faq-item {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: border-color 0.2s;
}

.faq-item.active {
  border-color: rgba(0, 240, 255, 0.35);
}

.faq-question {
  width: 100%;
  padding: 16px 20px;
  background: transparent;
  border: none;
  color: #fff;
  font-family: var(--font-main);
  font-size: 15px;
  font-weight: 700;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  text-align: left;
}

.faq-icon {
  font-size: 18px;
  color: var(--accent-cyan);
  transition: transform 0.2s;
}

.faq-item.active .faq-icon {
  transform: rotate(45deg);
}

.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease, padding 0.3s ease;
  padding: 0 20px;
}

.faq-item.active .faq-answer {
  max-height: 200px;
  padding: 0 20px 16px;
}

.faq-answer p {
  color: var(--text-muted);
  font-size: 14px;
  line-height: 1.5;
}

/* CTA Banner - Compacto */
.cta-banner-section {
  padding: 40px 0;
}

.cta-banner-box {
  padding: 36px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid rgba(0, 240, 255, 0.25);
  background: linear-gradient(135deg, rgba(16, 22, 34, 0.9) 0%, rgba(7, 9, 14, 0.95) 100%);
  border-radius: var(--radius-lg);
}

.cta-banner-content h2 {
  font-family: var(--font-display);
  font-size: 24px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 6px;
}

.cta-banner-content p {
  color: var(--text-muted);
  font-size: 14px;
}

/* Footer - Compacto */
.site-footer {
  border-top: 1px solid var(--border-subtle);
  background: #050608;
  padding: 44px 0 24px;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1fr;
  gap: 32px;
  margin-bottom: 32px;
}

.footer-brand-col .logo {
  margin-bottom: 12px;
}

.footer-text {
  font-size: 13px;
  color: var(--text-dim);
  line-height: 1.5;
  margin-bottom: 16px;
  max-width: 300px;
}

.footer-copy {
  font-size: 11px;
  color: var(--text-dim);
}

.footer-col h4 {
  font-family: var(--font-display);
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 14px;
}

.footer-col ul {
  list-style: none;
}

.footer-col ul li {
  margin-bottom: 8px;
}

.footer-col ul li a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 13px;
}

.footer-col ul li a:hover {
  color: var(--accent-cyan);
}

.security-badges {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sec-badge {
  font-size: 11px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-subtle);
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-weight: 600;
}

/* Responsive */
@media (max-width: 1024px) {
  .hero-grid { grid-template-columns: 1fr; }
  .timeline-grid { grid-template-columns: 1fr 1fr; }
  .exploded-showcase-container { grid-template-columns: 1fr; }
  .unboxing-grid { grid-template-columns: 1fr; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .cta-banner-box { flex-direction: column; text-align: center; gap: 20px; }
}

@media (max-width: 768px) {
  .announcement-bar { display: none; }
  .nav-links { display: none; }
  .hero-title { font-size: 32px; }
  .timeline-grid { grid-template-columns: 1fr; }
  .footer-grid { grid-template-columns: 1fr; }
}
"""

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_code)

print("Generated compact style.css successfully!")
