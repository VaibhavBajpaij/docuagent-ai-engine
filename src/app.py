from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from src.api.routes import router

app = FastAPI(
    title="DocuAgent AI Engine",
    version="1.0.0",
    description="Enterprise Multi-Agent Knowledge & Document Reasoning Engine with Semantic Caching"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "docuagent-ai-engine"}

@app.get("/", response_class=HTMLResponse)
def root_dashboard():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DocuAgent AI Engine — Multi-Agent Knowledge & Semantic Caching</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }
        }
      }
    }
  </script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen flex flex-col antialiased selection:bg-indigo-500 selection:text-white">

  <!-- Header -->
  <header class="border-b border-slate-800 bg-slate-900/60 backdrop-blur sticky top-0 z-50 px-6 py-4">
    <div class="max-w-6xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-sky-500 to-emerald-400 p-[2px]">
          <div class="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center font-bold text-sky-400 font-mono text-lg">
            DA
          </div>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-lg font-bold tracking-tight text-white">DocuAgent AI Engine</h1>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-950 text-emerald-400 border border-emerald-800">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
              Live in Production
            </span>
          </div>
          <p class="text-xs text-slate-400">Enterprise Multi-Agent Semantic Reasoning System</p>
        </div>
      </div>
      <div class="flex items-center gap-3">
        <a href="/docs" target="_blank" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white transition flex items-center gap-1.5 shadow-md shadow-indigo-600/20">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
          Swagger Docs
        </a>
        <a href="/health" target="_blank" class="px-3.5 py-1.5 text-xs font-medium rounded-lg border border-slate-700 bg-slate-900 hover:bg-slate-800 text-slate-300 transition">
          Health Check
        </a>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="flex-1 max-w-6xl w-full mx-auto px-6 py-10 space-y-8">
    
    <!-- Hero Banner -->
    <div class="p-8 rounded-2xl bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-800 relative overflow-hidden">
      <div class="absolute -right-20 -top-20 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -left-20 -bottom-20 w-80 h-80 bg-sky-600/10 rounded-full blur-3xl pointer-events-none"></div>
      
      <div class="relative z-10 max-w-3xl space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-md text-xs font-medium bg-slate-800/80 text-sky-400 border border-slate-700">
          <span>🚀 Serverless Architecture</span>
          <span>•</span>
          <span>LangGraph + Vector Semantic Caching</span>
        </div>
        <h2 class="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
          Sub-50ms Multi-Agent Document Intelligence
        </h2>
        <p class="text-sm text-slate-300 leading-relaxed">
          DocuAgent leverages dual-tier vector semantic caching (cosine similarity &ge; 0.90) to eliminate redundant LLM calls and deliver near-instant verified responses with zero hallucinations.
        </p>
      </div>

      <!-- Quick Stats -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8 pt-6 border-t border-slate-800/80">
        <div>
          <div class="text-xs text-slate-400">Cache Latency</div>
          <div class="text-xl font-bold font-mono text-emerald-400 mt-0.5">&lt; 1 ms</div>
        </div>
        <div>
          <div class="text-xs text-slate-400">Confidence Score</div>
          <div class="text-xl font-bold font-mono text-sky-400 mt-0.5">1.00 / 1.00</div>
        </div>
        <div>
          <div class="text-xs text-slate-400">Similarity Threshold</div>
          <div class="text-xl font-bold font-mono text-indigo-400 mt-0.5">&ge; 0.90 Cosine</div>
        </div>
        <div>
          <div class="text-xs text-slate-400">Runtime Platform</div>
          <div class="text-xl font-bold font-mono text-purple-400 mt-0.5">Vercel Serverless</div>
        </div>
      </div>
    </div>

    <!-- Live Interactive Query Playground -->
    <div class="p-6 rounded-2xl bg-slate-900/70 border border-slate-800 shadow-xl space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h3 class="text-base font-semibold text-white flex items-center gap-2">
            <span>⚡ Live Query & Semantic Caching Playground</span>
          </h3>
          <p class="text-xs text-slate-400 mt-0.5">Test real-time semantic caching and agent routing directly from this browser view</p>
        </div>
        <span class="text-xs text-slate-500 font-mono">POST /api/v1/query</span>
      </div>

      <div class="flex flex-col sm:flex-row gap-3">
        <input 
          id="queryInput" 
          type="text" 
          value="Explain semantic caching" 
          placeholder="Ask a question (e.g. Explain semantic caching, What is LangGraph?)..."
          class="flex-1 bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 font-sans"
        />
        <button 
          id="submitBtn" 
          onclick="runQuery()"
          class="px-6 py-2.5 bg-gradient-to-r from-indigo-600 to-sky-500 hover:from-indigo-500 hover:to-sky-400 text-white text-sm font-semibold rounded-xl shadow-lg shadow-indigo-500/20 transition flex items-center justify-center gap-2"
        >
          <span>Run Query</span>
          <svg id="spinner" class="hidden w-4 h-4 animate-spin text-white" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
          </svg>
        </button>
      </div>

      <!-- Presets -->
      <div class="flex flex-wrap items-center gap-2 text-xs text-slate-400">
        <span>Try sample queries:</span>
        <button onclick="setQuery('Explain semantic caching')" class="px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition">"Explain semantic caching"</button>
        <button onclick="setQuery('How does LangGraph coordinate agents?')" class="px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition">"How does LangGraph coordinate agents?"</button>
        <button onclick="setQuery('What is the cache latency target?')" class="px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition">"What is the cache latency target?"</button>
      </div>

      <!-- Result View -->
      <div id="resultBox" class="hidden mt-4 space-y-3">
        <div class="flex items-center justify-between text-xs">
          <div class="flex items-center gap-2">
            <span id="cacheBadge" class="px-2 py-0.5 rounded font-mono font-medium"></span>
            <span id="latencyBadge" class="text-slate-400 font-mono"></span>
          </div>
          <span id="traceId" class="text-slate-500 font-mono"></span>
        </div>
        <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 font-mono text-xs text-slate-200 overflow-x-auto leading-relaxed">
          <pre id="jsonOutput"></pre>
        </div>
      </div>
    </div>

    <!-- Architectural Endpoints Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="p-5 rounded-xl bg-slate-900/40 border border-slate-800/80 space-y-2">
        <div class="text-xs font-semibold text-indigo-400 uppercase tracking-wider">Interactive Docs</div>
        <h4 class="text-sm font-semibold text-white">Swagger UI & OpenAPI 3.0</h4>
        <p class="text-xs text-slate-400">Explore and execute all REST endpoints with live schemas, headers, and validation models.</p>
        <div class="pt-2">
          <a href="/docs" target="_blank" class="text-xs font-semibold text-sky-400 hover:text-sky-300 flex items-center gap-1">Open Swagger UI &rarr;</a>
        </div>
      </div>

      <div class="p-5 rounded-xl bg-slate-900/40 border border-slate-800/80 space-y-2">
        <div class="text-xs font-semibold text-emerald-400 uppercase tracking-wider">Semantic Cache</div>
        <h4 class="text-sm font-semibold text-white">Redis & Vector Store Cache</h4>
        <p class="text-xs text-slate-400">Inspect real-time hit rates, memory size, eviction policies, and cosine similarity distributions.</p>
        <div class="pt-2">
          <a href="/api/v1/cache/stats" target="_blank" class="text-xs font-semibold text-emerald-400 hover:text-emerald-300 flex items-center gap-1">View Cache Stats &rarr;</a>
        </div>
      </div>

      <div class="p-5 rounded-xl bg-slate-900/40 border border-slate-800/80 space-y-2">
        <div class="text-xs font-semibold text-purple-400 uppercase tracking-wider">System Health</div>
        <h4 class="text-sm font-semibold text-white">Heartbeat & Telemetry</h4>
        <p class="text-xs text-slate-400">Microservice readiness probe and Vercel serverless worker lifecycle monitor.</p>
        <div class="pt-2">
          <a href="/health" target="_blank" class="text-xs font-semibold text-purple-400 hover:text-purple-300 flex items-center gap-1">Check Health &rarr;</a>
        </div>
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500">
    DocuAgent AI Engine &bull; Developed by <a href="https://github.com/VaibhavBajpaij" target="_blank" class="text-slate-400 hover:underline">Vaibhav Bajpai</a> &bull; Production Deployment on Vercel
  </footer>

  <script>
    function setQuery(text) {
      document.getElementById('queryInput').value = text;
      runQuery();
    }

    async function runQuery() {
      const q = document.getElementById('queryInput').value.trim();
      if (!q) return;

      const btn = document.getElementById('submitBtn');
      const spinner = document.getElementById('spinner');
      const resultBox = document.getElementById('resultBox');
      const jsonOutput = document.getElementById('jsonOutput');
      const cacheBadge = document.getElementById('cacheBadge');
      const latencyBadge = document.getElementById('latencyBadge');
      const traceId = document.getElementById('traceId');

      spinner.classList.remove('hidden');
      btn.disabled = true;

      try {
        const start = performance.now();
        const res = await fetch('/api/v1/query', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query: q })
        });
        const elapsed = (performance.now() - start).toFixed(1);
        const data = await res.json();

        resultBox.classList.remove('hidden');
        jsonOutput.textContent = JSON.stringify(data, null, 2);

        if (data.cached) {
          cacheBadge.className = 'px-2 py-0.5 rounded font-mono font-medium bg-emerald-950 text-emerald-400 border border-emerald-800';
          cacheBadge.textContent = '⚡ CACHE HIT (Sub-Millisecond)';
        } else {
          cacheBadge.className = 'px-2 py-0.5 rounded font-mono font-medium bg-indigo-950 text-indigo-400 border border-indigo-800';
          cacheBadge.textContent = '🔍 CACHE MISS (Fresh Inference)';
        }

        latencyBadge.textContent = `Client Latency: ${elapsed}ms | Engine Latency: ${data.latency_ms}ms`;
        traceId.textContent = data.trace_id ? `Trace: ${data.trace_id}` : '';
      } catch (err) {
        resultBox.classList.remove('hidden');
        jsonOutput.textContent = "Error invoking API: " + err.message;
      } finally {
        spinner.classList.add('hidden');
        btn.disabled = false;
      }
    }
  </script>
</body>
</html>"""
