<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tamper-Proof Chat Logging System</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #070b0f;
    --surface: #0d1117;
    --surface2: #111820;
    --border: #1e2d3d;
    --accent: #00e5ff;
    --accent2: #00ff88;
    --accent3: #ff4757;
    --warn: #ffd32a;
    --text: #cdd9e5;
    --text-muted: #546e7a;
    --mono: 'Share Tech Mono', monospace;
    --sans: 'Syne', sans-serif;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--sans);
    font-size: 15px;
    line-height: 1.7;
    overflow-x: hidden;
  }

  /* Scanline overlay */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,0,0,0.08) 2px,
      rgba(0,0,0,0.08) 4px
    );
    pointer-events: none;
    z-index: 9999;
  }

  /* Grid background */
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,229,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,229,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 24px 80px;
    position: relative;
    z-index: 1;
  }

  /* ── HERO ── */
  .hero {
    padding: 72px 0 48px;
    border-bottom: 1px solid var(--border);
    position: relative;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    border: 1px solid rgba(0,229,255,0.3);
    padding: 4px 12px;
    margin-bottom: 24px;
    letter-spacing: 2px;
    text-transform: uppercase;
    animation: fadeSlideIn 0.6s ease forwards;
  }

  .hero-badge::before {
    content: '';
    width: 6px; height: 6px;
    background: var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--accent);
    animation: pulse 1.5s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
  }

  h1 {
    font-family: var(--sans);
    font-size: clamp(28px, 5vw, 48px);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1px;
    color: #fff;
    margin-bottom: 16px;
    animation: fadeSlideIn 0.7s ease forwards;
  }

  h1 .accent { color: var(--accent); }

  .hero-desc {
    font-size: 16px;
    color: var(--text-muted);
    max-width: 620px;
    margin-bottom: 28px;
    animation: fadeSlideIn 0.8s ease forwards;
  }

  .tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    animation: fadeSlideIn 0.9s ease forwards;
  }

  .tag {
    font-family: var(--mono);
    font-size: 11px;
    padding: 4px 12px;
    border: 1px solid var(--border);
    color: var(--text-muted);
    letter-spacing: 1px;
    transition: all 0.2s;
  }

  .tag:hover {
    border-color: var(--accent);
    color: var(--accent);
  }

  /* ── SECTION ── */
  section {
    padding: 52px 0 0;
    animation: fadeSlideIn 0.6s ease forwards;
    opacity: 0;
  }

  section.visible { opacity: 1; }

  .section-label {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
  }

  h2 {
    font-size: 22px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }

  h2 .num {
    font-family: var(--mono);
    color: var(--accent);
    margin-right: 8px;
    font-size: 14px;
  }

  p { color: var(--text); margin-bottom: 14px; }

  /* ── CODE BLOCK ── */
  .code-block {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    padding: 20px 24px;
    font-family: var(--mono);
    font-size: 13px;
    color: #a8d8ea;
    overflow-x: auto;
    margin: 16px 0;
    line-height: 1.8;
    position: relative;
  }

  .code-block .label {
    position: absolute;
    top: 8px; right: 12px;
    font-size: 10px;
    color: var(--text-muted);
    letter-spacing: 1px;
  }

  .code-block .c-green { color: var(--accent2); }
  .code-block .c-red { color: var(--accent3); }
  .code-block .c-blue { color: var(--accent); }
  .code-block .c-yellow { color: var(--warn); }
  .code-block .c-muted { color: var(--text-muted); }

  /* ── TABLE ── */
  .table-wrap { overflow-x: auto; margin: 16px 0; }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
  }

  thead tr {
    background: var(--surface2);
    border-bottom: 2px solid var(--accent);
  }

  th {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--accent);
    padding: 12px 16px;
    text-align: left;
  }

  td {
    padding: 11px 16px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  td:first-child {
    font-family: var(--mono);
    color: var(--accent2);
    font-size: 13px;
  }

  tr:hover td { background: rgba(0,229,255,0.03); }

  /* ── ALERT BOXES ── */
  .alert {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 16px 20px;
    border: 1px solid;
    margin: 16px 0;
    font-size: 14px;
  }

  .alert-success { border-color: var(--accent2); background: rgba(0,255,136,0.05); }
  .alert-danger  { border-color: var(--accent3); background: rgba(255,71,87,0.05); }
  .alert-warn    { border-color: var(--warn);    background: rgba(255,211,42,0.05); }

  .alert-icon { font-size: 18px; line-height: 1; margin-top: 1px; }
  .alert-success .alert-icon { color: var(--accent2); }
  .alert-danger  .alert-icon { color: var(--accent3); }
  .alert-warn    .alert-icon { color: var(--warn); }

  /* ── ARCHITECTURE ── */
  .arch {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0;
    margin: 20px 0;
    padding-left: 8px;
  }

  .arch-node {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .arch-box {
    border: 1px solid var(--border);
    padding: 10px 20px;
    font-family: var(--mono);
    font-size: 13px;
    color: var(--text);
    background: var(--surface);
    transition: all 0.2s;
    white-space: nowrap;
  }

  .arch-box:hover {
    border-color: var(--accent);
    color: var(--accent);
    box-shadow: 0 0 16px rgba(0,229,255,0.1);
  }

  .arch-box.highlight { border-color: var(--accent2); color: var(--accent2); }

  .arch-arrow {
    font-family: var(--mono);
    color: var(--text-muted);
    font-size: 12px;
    margin-left: 24px;
    padding: 2px 0;
  }

  .arch-note {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text-muted);
    margin-left: 14px;
  }

  /* ── CHAIN VIZ ── */
  .chain {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 0;
    margin: 20px 0;
    overflow-x: auto;
    padding: 16px 0;
  }

  .chain-block {
    border: 1px solid var(--border);
    padding: 12px 16px;
    background: var(--surface);
    font-family: var(--mono);
    font-size: 12px;
    line-height: 1.6;
    min-width: 130px;
    transition: all 0.2s;
  }

  .chain-block:hover {
    border-color: var(--accent);
    box-shadow: 0 0 20px rgba(0,229,255,0.12);
  }

  .chain-block .cb-label {
    font-size: 10px;
    color: var(--accent);
    letter-spacing: 2px;
    margin-bottom: 4px;
  }

  .chain-block .cb-msg { color: #fff; font-size: 11px; }
  .chain-block .cb-hash { color: var(--text-muted); font-size: 10px; margin-top: 4px; }

  .chain-arrow {
    font-size: 18px;
    color: var(--accent);
    padding: 0 8px;
    flex-shrink: 0;
  }

  /* ── WORKFLOW STEPS ── */
  .steps { margin: 20px 0; }

  .step {
    display: flex;
    gap: 20px;
    padding: 16px 0;
    border-bottom: 1px solid var(--border);
    align-items: flex-start;
  }

  .step:last-child { border-bottom: none; }

  .step-num {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    border: 1px solid rgba(0,229,255,0.3);
    padding: 4px 10px;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .step-content { flex: 1; }
  .step-title { font-weight: 600; color: #fff; margin-bottom: 4px; }
  .step-desc { font-size: 13px; color: var(--text-muted); font-family: var(--mono); }

  /* ── APPS GRID ── */
  .apps-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
    margin: 20px 0;
  }

  .app-card {
    border: 1px solid var(--border);
    padding: 16px;
    background: var(--surface);
    transition: all 0.25s;
  }

  .app-card:hover {
    border-color: var(--accent2);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }

  .app-card .app-icon { font-size: 22px; margin-bottom: 10px; }
  .app-card .app-name { font-weight: 700; color: #fff; font-size: 14px; margin-bottom: 4px; }
  .app-card .app-desc { font-size: 12px; color: var(--text-muted); }

  /* ── FUTURE LIST ── */
  .future-list { list-style: none; margin: 16px 0; }

  .future-list li {
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 14px;
  }

  .future-list li::before {
    content: '→';
    font-family: var(--mono);
    color: var(--accent);
    flex-shrink: 0;
  }

  /* ── INSTALL COMMANDS ── */
  .cmd {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 14px 20px;
    font-family: var(--mono);
    font-size: 13px;
    color: var(--accent2);
    margin: 10px 0;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .cmd::before {
    content: '$';
    color: var(--text-muted);
    flex-shrink: 0;
  }

  /* ── TOC ── */
  .toc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    padding: 24px 28px;
    margin: 32px 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 32px;
  }

  .toc a {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--text-muted);
    text-decoration: none;
    padding: 4px 0;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: color 0.2s;
  }

  .toc a::before { content: '//'; color: var(--accent); font-size: 10px; }
  .toc a:hover { color: var(--accent); }

  /* ── FOOTER ── */
  footer {
    margin-top: 72px;
    padding-top: 24px;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }

  footer .f-left { font-family: var(--mono); font-size: 11px; color: var(--text-muted); }
  footer .f-right { font-family: var(--mono); font-size: 11px; color: var(--text-muted); }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, var(--accent), transparent);
    margin: 8px 0 0;
    opacity: 0.3;
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(16px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .d1 { animation-delay: 0.1s; }
  .d2 { animation-delay: 0.2s; }
  .d3 { animation-delay: 0.3s; }

  /* ── SCROLLBAR ── */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border); }
  ::-webkit-scrollbar-thumb:hover { background: var(--accent); }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HERO -->
  <header class="hero">
    <div class="hero-badge">🔐 &nbsp; Security Project</div>
    <h1>Tamper-Proof<br><span class="accent">Chat Logging</span> System</h1>
    <p class="hero-desc">
      A secure chat logging system demonstrating tamper-proof audit logs using cryptographic hash chaining.
      Any unauthorized modification is automatically detected.
    </p>
    <div class="tech-stack">
      <span class="tag">Python</span>
      <span class="tag">Streamlit</span>
      <span class="tag">SHA-256</span>
      <span class="tag">JSON Storage</span>
      <span class="tag">Hash Chaining</span>
    </div>
  </header>

  <!-- TOC -->
  <nav class="toc">
    <a href="#intro">Introduction</a>
    <a href="#workflow">Application Workflow</a>
    <a href="#problem">Problem Statement</a>
    <a href="#install">Installation & Setup</a>
    <a href="#objectives">Security Objectives</a>
    <a href="#demo">Demonstration</a>
    <a href="#arch">System Architecture</a>
    <a href="#realworld">Real-World Applications</a>
    <a href="#crypto">Cryptographic Background</a>
    <a href="#future">Future Improvements</a>
    <a href="#math">Mathematical Model</a>
    <a href="#license">License</a>
    <a href="#tamper">Tampering Detection</a>
  </nav>

  <!-- 1. INTRODUCTION -->
  <section id="intro">
    <div class="section-label">01 — Overview</div>
    <h2><span class="num">#</span>Introduction</h2>
    <p>
      Modern information systems rely heavily on log files to record critical activities — user logins, financial
      transactions, system events, and security alerts. However, attackers who gain system access may attempt
      to modify these logs to conceal their actions.
    </p>
    <p>
      This project demonstrates a <strong style="color:#fff">tamper-proof logging mechanism</strong> using
      cryptographic hash chaining, similar to techniques used in:
    </p>
    <div class="apps-grid" style="grid-template-columns: repeat(auto-fill, minmax(160px,1fr))">
      <div class="app-card"><div class="app-icon">⛓️</div><div class="app-name">Blockchain</div><div class="app-desc">Immutable ledgers</div></div>
      <div class="app-card"><div class="app-icon">📋</div><div class="app-name">Audit Trails</div><div class="app-desc">Secure record-keeping</div></div>
      <div class="app-card"><div class="app-icon">🏦</div><div class="app-name">Financial</div><div class="app-desc">Transaction integrity</div></div>
      <div class="app-card"><div class="app-icon">🛡️</div><div class="app-name">CyberSec</div><div class="app-desc">Monitoring platforms</div></div>
    </div>
  </section>

  <!-- 2. PROBLEM -->
  <section id="problem">
    <div class="section-label">02 — The Problem</div>
    <h2><span class="num">#</span>Problem Statement</h2>
    <p>Traditional logging systems store records sequentially with no built-in integrity protection:</p>
    <div class="code-block">
      <span class="c-muted">// Sequential log — no protection</span><br>
      Log1 → Log2 → Log3 → Log4
    </div>
    <p>An attacker can silently modify any record without leaving a trace:</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:16px 0;">
      <div class="alert alert-success">
        <span class="alert-icon">✓</span>
        <div><strong>Original</strong><br><code style="font-family:var(--mono); font-size:13px">UserA: Login successful</code></div>
      </div>
      <div class="alert alert-danger">
        <span class="alert-icon">✗</span>
        <div><strong>Tampered</strong><br><code style="font-family:var(--mono); font-size:13px">UserA: No activity</code></div>
      </div>
    </div>
    <p style="color:var(--text-muted)">There is no mechanism to detect such changes in a conventional logging system.</p>
  </section>

  <!-- 3. OBJECTIVES -->
  <section id="objectives">
    <div class="section-label">03 — Goals</div>
    <h2><span class="num">#</span>Security Objectives</h2>
    <p>This system is designed to achieve three core security properties:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Property</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td>Integrity</td><td>Log entries cannot be modified without detection</td></tr>
          <tr><td>Traceability</td><td>Every log entry is cryptographically linked to the previous one</td></tr>
          <tr><td>Tamper Detection</td><td>Any modification invalidates the entire hash chain</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- 4. ARCHITECTURE -->
  <section id="arch">
    <div class="section-label">04 — Design</div>
    <h2><span class="num">#</span>System Architecture</h2>
    <div class="arch">
      <div class="arch-node"><div class="arch-box highlight">👥 Users</div><div class="arch-note">// Chat messages</div></div>
      <div class="arch-arrow">│<br>▼</div>
      <div class="arch-node"><div class="arch-box">🌐 Streamlit Web Application</div></div>
      <div class="arch-arrow">│<br>▼</div>
      <div class="arch-node"><div class="arch-box">🔗 Hash Chain Logging System</div></div>
      <div class="arch-arrow">│<br>▼</div>
      <div class="arch-node"><div class="arch-box">💾 logs.json</div><div class="arch-note">// Persistent storage</div></div>
      <div class="arch-arrow">│<br>▼</div>
      <div class="arch-node"><div class="arch-box highlight">🔍 Admin Verification Panel</div></div>
    </div>
    <p style="font-size:13px; color:var(--text-muted)">The admin panel allows verification of the full log chain's integrity at any time.</p>
  </section>

  <!-- 5. CRYPTO -->
  <section id="crypto">
    <div class="section-label">05 — Cryptography</div>
    <h2><span class="num">#</span>Cryptographic Background</h2>
    <p>This project uses the <strong style="color:var(--accent)">SHA-256</strong> cryptographic hash function:</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Property</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td>Deterministic</td><td>Same input always produces the same output</td></tr>
          <tr><td>Collision Resistant</td><td>Extremely difficult to produce the same hash from different inputs</td></tr>
          <tr><td>Preimage Resistant</td><td>Cannot reconstruct the original input from its hash</td></tr>
          <tr><td>Avalanche Effect</td><td>A small change in input produces a completely different hash</td></tr>
        </tbody>
      </table>
    </div>
    <p>Even a tiny change in input produces a completely different hash:</p>
    <div class="code-block">
      <span class="label">SHA-256 EXAMPLE</span>
      <span class="c-muted">Input: </span><span class="c-yellow">"Hello"</span><br>
      <span class="c-muted">SHA256: </span><span class="c-green">185f8db32271fe25f561a6fc938b2e264306ec304eda518007d176...</span><br><br>
      <span class="c-muted">Input: </span><span class="c-yellow">"Hello!"</span>  <span class="c-muted">← one character added</span><br>
      <span class="c-muted">SHA256: </span><span class="c-red">334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5...</span>
    </div>
  </section>

  <!-- 6. MATH -->
  <section id="math">
    <div class="section-label">06 — Model</div>
    <h2><span class="num">#</span>Mathematical Model</h2>
    <p>Let <code style="color:var(--accent)">Mᵢ</code> = message, <code style="color:var(--accent)">Tᵢ</code> = timestamp, <code style="color:var(--accent)">Hᵢ₋₁</code> = previous hash. Each entry is defined as:</p>
    <div class="code-block">
      <span class="label">HASH FORMULA</span>
      <span class="c-blue">Hᵢ</span> = <span class="c-green">SHA256</span>(<span class="c-yellow">Mᵢ</span> <span class="c-muted">||</span> <span class="c-yellow">Tᵢ</span> <span class="c-muted">||</span> <span class="c-yellow">Hᵢ₋₁</span>)<br><br>
      <span class="c-muted">// Genesis entry (no previous hash)</span><br>
      <span class="c-blue">H₀</span> = <span class="c-green">SHA256</span>(<span class="c-yellow">M₀ || T₀ ||</span> <span class="c-red">0</span>)<br>
      <span class="c-blue">H₁</span> = <span class="c-green">SHA256</span>(<span class="c-yellow">M₁ || T₁ ||</span> <span class="c-blue">H₀</span>)<br>
      <span class="c-blue">H₂</span> = <span class="c-green">SHA256</span>(<span class="c-yellow">M₂ || T₂ ||</span> <span class="c-blue">H₁</span>)
    </div>
    <p>This creates a chain where each entry depends on all previous entries:</p>
    <div class="chain">
      <div class="chain-block">
        <div class="cb-label">LOG 0</div>
        <div class="cb-msg">UserA: Hello</div>
        <div class="cb-hash">H₀: 185f8d...</div>
      </div>
      <div class="chain-arrow">──▶</div>
      <div class="chain-block">
        <div class="cb-label">LOG 1</div>
        <div class="cb-msg">UserB: Hi</div>
        <div class="cb-hash">H₁: a3f92c...</div>
      </div>
      <div class="chain-arrow">──▶</div>
      <div class="chain-block">
        <div class="cb-label">LOG 2</div>
        <div class="cb-msg">UserA: Thanks</div>
        <div class="cb-hash">H₂: 7d1e40...</div>
      </div>
      <div class="chain-arrow">──▶</div>
      <div class="chain-block">
        <div class="cb-label">LOG 3</div>
        <div class="cb-msg">UserB: Sure</div>
        <div class="cb-hash">H₃: 2b98fc...</div>
      </div>
    </div>
  </section>

  <!-- 7. TAMPERING -->
  <section id="tamper">
    <div class="section-label">07 — Detection</div>
    <h2><span class="num">#</span>Tampering Detection</h2>
    <p>If an attacker modifies any message in the chain:</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin:16px 0;">
      <div class="alert alert-success"><span class="alert-icon">✓</span><div><strong>Original</strong><br><code style="font-family:var(--mono); font-size:13px">"UserB: Hi"</code></div></div>
      <div class="alert alert-danger"><span class="alert-icon">✗</span><div><strong>Tampered</strong><br><code style="font-family:var(--mono); font-size:13px">"UserB: Send OTP"</code></div></div>
    </div>
    <p>The recalculated hash will not match the stored hash, causing a chain break:</p>
    <div class="code-block">
      <span class="c-red">Hᵢ'</span> ≠ <span class="c-green">Hᵢ</span>  <span class="c-muted">// Hash mismatch — chain is broken</span>
    </div>
    <div class="alert alert-warn">
      <span class="alert-icon">⚠</span>
      <div><strong>Tampering Detected</strong> — Because every subsequent hash depends on the modified entry, the entire downstream chain is invalidated, making silent tampering impossible.</div>
    </div>
  </section>

  <!-- 8. WORKFLOW -->
  <section id="workflow">
    <div class="section-label">08 — Flow</div>
    <h2><span class="num">#</span>Application Workflow</h2>
    <div class="steps">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-content">
          <div class="step-title">User Sends a Message</div>
          <div class="step-desc">e.g. "UserA: Hello"</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-content">
          <div class="step-title">Log Entry Created</div>
          <div class="step-desc">{ message, timestamp, prevHash, hash }</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-content">
          <div class="step-title">Log Appended to Chain</div>
          <div class="step-desc">New entry linked to previous hash</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">04</div>
        <div class="step-content">
          <div class="step-title">Admin Triggers Verification</div>
          <div class="step-desc">All hashes recomputed and compared</div>
        </div>
      </div>
    </div>
    <div class="alert alert-success" style="margin-top:12px">
      <span class="alert-icon">✅</span>
      <div>Stored Hash == Recomputed Hash → <strong>Logs are VALID</strong></div>
    </div>
    <div class="alert alert-danger">
      <span class="alert-icon">❌</span>
      <div>Mismatch detected → <strong>Tampering Detected</strong></div>
    </div>
  </section>

  <!-- 9. INSTALL -->
  <section id="install">
    <div class="section-label">09 — Setup</div>
    <h2><span class="num">#</span>Installation &amp; Setup</h2>
    <p><strong style="color:#fff">Step 1 — Clone the repository:</strong></p>
    <div class="cmd">git clone https://github.com/Priyanshu-rajsingh/tamper-proof-chat-streamlit.git</div>
    <div class="cmd">cd tamper-proof-chat-streamlit</div>
    <p style="margin-top:16px"><strong style="color:#fff">Step 2 — Install dependencies:</strong></p>
    <div class="cmd">pip install -r requirements.txt</div>
    <p style="margin-top:12px; font-size:13px; color:var(--text-muted)">Or install manually:</p>
    <div class="cmd">pip install streamlit</div>
    <p style="margin-top:20px"><strong style="color:#fff">Run the application:</strong></p>
    <div class="cmd">streamlit run app.py</div>
    <div class="alert alert-success" style="margin-top:12px">
      <span class="alert-icon">🌐</span>
      <div>Open your browser and navigate to <code style="font-family:var(--mono)">http://localhost:8501</code></div>
    </div>
  </section>

  <!-- 10. DEMO -->
  <section id="demo">
    <div class="section-label">10 — Demo</div>
    <h2><span class="num">#</span>Demonstration Scenario</h2>
    <div class="steps">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-content">
          <div class="step-title">Users Send Messages</div>
          <div class="step-desc">UserA: Hello &nbsp;|&nbsp; UserB: Hi</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-content">
          <div class="step-title">Admin Opens Log Panel</div>
          <div class="step-desc" style="color:var(--accent2)">✅ Logs are VALID</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-content">
          <div class="step-title">Admin Simulates Tampering</div>
          <div class="step-desc">Changes "Hi" → "Send OTP" in logs.json</div>
        </div>
      </div>
      <div class="step">
        <div class="step-num">04</div>
        <div class="step-content">
          <div class="step-title">System Re-verifies the Chain</div>
          <div class="step-desc" style="color:var(--accent3)">❌ Tampering Detected</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 11. REAL WORLD -->
  <section id="realworld">
    <div class="section-label">11 — Applications</div>
    <h2><span class="num">#</span>Real-World Applications</h2>
    <div class="apps-grid">
      <div class="app-card"><div class="app-icon">⛓️</div><div class="app-name">Blockchain</div><div class="app-desc">Ensures immutability of transaction records</div></div>
      <div class="app-card"><div class="app-icon">🏦</div><div class="app-name">Financial Systems</div><div class="app-desc">Protects banking and transaction audit logs</div></div>
      <div class="app-card"><div class="app-icon">🛡️</div><div class="app-name">Security Monitoring</div><div class="app-desc">Prevents attackers from hiding their traces</div></div>
      <div class="app-card"><div class="app-icon">🔬</div><div class="app-name">Digital Forensics</div><div class="app-desc">Maintains trustworthy evidence records</div></div>
      <div class="app-card"><div class="app-icon">📋</div><div class="app-name">Audit & Compliance</div><div class="app-desc">Ensures regulatory compliance through verifiable logs</div></div>
    </div>
  </section>

  <!-- 12. FUTURE -->
  <section id="future">
    <div class="section-label">12 — Roadmap</div>
    <h2><span class="num">#</span>Future Improvements</h2>
    <ul class="future-list">
      <li>Real-time multi-user chat using WebSockets</li>
      <li>Digital signatures for stronger log authentication</li>
      <li>Distributed logging using blockchain</li>
      <li>Database storage to replace JSON files</li>
      <li>Automated intrusion alerts on tampering detection</li>
      <li>Visual hash chain graph for intuitive exploration</li>
    </ul>
  </section>

  <!-- FOOTER -->
  <footer id="license">
    <div class="f-left">© 2024 tamper-proof-chat · Educational & Research Use</div>
    <div class="f-right">SHA-256 · Python · Streamlit</div>
  </footer>

</div>

<script>
  // Scroll-triggered fade-in for sections
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.animation = 'fadeSlideIn 0.6s ease forwards';
        e.target.style.opacity = '1';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('section').forEach(s => {
    s.style.opacity = '0';
    observer.observe(s);
  });
</script>
</body>
</html>
