import { useEffect, useState } from "react";

type Health = { status: string; papers: number };

export default function App() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/health")
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(setHealth)
      .catch((e: Error) => setError(e.message));
  }, []);

  return (
    <main className="min-h-screen bg-slate-50 text-slate-900">
      <div className="mx-auto max-w-2xl px-6 py-16">
        <h1 className="text-4xl font-semibold tracking-tight">Contra</h1>
        <p className="mt-2 text-slate-600">
          Find where the Alzheimer's research disagrees.
        </p>

        <section className="mt-12 rounded-lg border border-slate-200 bg-white p-6">
          <h2 className="text-sm font-medium uppercase tracking-wide text-slate-500">
            Stage 1 — deploy check
          </h2>
          <div className="mt-3">
            {error && (
              <p className="text-red-600">Backend unreachable: {error}</p>
            )}
            {!error && !health && <p className="text-slate-500">Loading…</p>}
            {health && (
              <p className="text-slate-800">
                Backend status: <strong>{health.status}</strong> · corpus:{" "}
                <strong>{health.papers.toLocaleString()}</strong> papers
              </p>
            )}
          </div>
        </section>
      </div>
    </main>
  );
}
