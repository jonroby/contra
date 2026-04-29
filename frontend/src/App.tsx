import { useEffect, useState } from "react";
import type { QueryResult } from "./types";
import { Results } from "./components/Results";

export default function App() {
  const [examples, setExamples] = useState<string[]>([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<QueryResult | null>(null);

  useEffect(() => {
    fetch("/api/examples")
      .then((r) => r.json())
      .then((d: { examples: string[] }) => setExamples(d.examples))
      .catch(() => {
        /* examples are non-essential */
      });
  }, []);

  async function submit(q?: string) {
    const text = (q ?? question).trim();
    if (!text) return;
    setQuestion(text);
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch("/api/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: text }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail ?? `HTTP ${res.status}`);
      }
      const data: QueryResult = await res.json();
      setResult(data);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-50 text-slate-900">
      <div className="mx-auto max-w-4xl px-6 py-12">
        <header>
          <h1 className="text-4xl font-semibold tracking-tight">Contra</h1>
          <p className="mt-2 text-lg font-medium text-slate-800">
            Find where the Alzheimer's research disagrees.
          </p>
          <p className="mt-1 text-slate-600">
            Ask a research question. Contra retrieves relevant clinical
            studies, classifies each as supporting or contradicting your
            question, and summarizes where the evidence conflicts.
          </p>
        </header>

        <form
          className="mt-8 flex gap-3"
          onSubmit={(e) => {
            e.preventDefault();
            void submit();
          }}
        >
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                void submit();
              }
            }}
            placeholder="e.g., Does lithium slow cognitive decline in Alzheimer's?"
            rows={2}
            disabled={loading}
            className="flex-1 resize-none rounded-md border border-slate-300 bg-white px-4 py-3 text-slate-900 shadow-sm focus:border-orange-500 focus:outline-none focus:ring-2 focus:ring-orange-200 disabled:bg-slate-100"
          />
          <button
            type="submit"
            disabled={loading || !question.trim()}
            className="rounded-md bg-orange-500 px-6 py-3 font-medium text-white shadow-sm hover:bg-orange-600 disabled:bg-slate-300"
          >
            {loading ? "Searching…" : "Search"}
          </button>
        </form>

        {examples.length > 0 && !result && !loading && (
          <div className="mt-4">
            <div className="mb-2 text-sm font-medium text-slate-500">
              Examples
            </div>
            <div className="flex flex-wrap gap-2">
              {examples.map((ex) => (
                <button
                  key={ex}
                  onClick={() => void submit(ex)}
                  className="rounded-md border border-slate-300 bg-white px-3 py-1.5 text-sm text-slate-700 hover:border-orange-400 hover:text-orange-700"
                >
                  {ex}
                </button>
              ))}
            </div>
          </div>
        )}

        {loading && (
          <div className="mt-10 flex items-center gap-3 text-slate-600">
            <span className="h-3 w-3 animate-pulse rounded-full bg-orange-500" />
            <span>
              Retrieving and classifying studies… (~5–10 seconds)
            </span>
          </div>
        )}

        {error && (
          <div className="mt-10 rounded-md border border-red-200 bg-red-50 px-4 py-3 text-red-800">
            <strong>Error:</strong> {error}
          </div>
        )}

        {result && <Results result={result} />}
      </div>
    </main>
  );
}
