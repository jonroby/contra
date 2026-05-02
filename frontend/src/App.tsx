import { useEffect, useState } from "react";
import type { QueryResult } from "./types";
import { Results } from "./components/Results";

const FALLBACK_EXAMPLES = [
  "Does lithium slow cognitive decline in Alzheimer's?",
  "Is the Mediterranean diet protective against Alzheimer's?",
  "Do statins reduce Alzheimer's risk?",
];

export default function App() {
  const [examples, setExamples] = useState<string[]>([]);
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<QueryResult | null>(null);
  const [placeholder, setPlaceholder] = useState("");

  useEffect(() => {
    fetch("/api/examples")
      .then((r) => r.json())
      .then((d: { examples: string[] }) => setExamples(d.examples))
      .catch(() => {
        /* examples are non-essential */
      });
  }, []);

  useEffect(() => {
    const list = examples.length > 0 ? examples : FALLBACK_EXAMPLES;
    if (list.length === 0) return;

    let cancelled = false;
    let idx = 0;
    let charIdx = 0;
    let phase: "typing" | "pausing" | "deleting" = "typing";
    let timer: ReturnType<typeof setTimeout>;

    const STEP_MS = 25;

    const tick = () => {
      if (cancelled) return;
      const current = list[idx];
      if (phase === "typing") {
        charIdx += 1;
        setPlaceholder(current.slice(0, charIdx));
        if (charIdx >= current.length) {
          phase = "pausing";
          timer = setTimeout(tick, 1800);
          return;
        }
        timer = setTimeout(tick, STEP_MS);
      } else if (phase === "pausing") {
        phase = "deleting";
        timer = setTimeout(tick, STEP_MS);
      } else {
        charIdx -= 1;
        setPlaceholder(current.slice(0, Math.max(0, charIdx)));
        if (charIdx <= 0) {
          phase = "typing";
          idx = (idx + 1) % list.length;
          timer = setTimeout(tick, 400);
          return;
        }
        timer = setTimeout(tick, STEP_MS);
      }
    };

    timer = setTimeout(tick, 600);
    return () => {
      cancelled = true;
      clearTimeout(timer);
    };
  }, [examples]);

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
    <main className="min-h-screen bg-slate-50 font-sans text-slate-900">
      <div className="sticky top-0 z-10 px-8 pt-6 pb-3">
        <div className="inline-flex items-center gap-2.5">
          <svg
            viewBox="0 0 24 24"
            fill="none"
            className="h-8 w-8"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <g
              stroke="#26489d"
              transform="rotate(-45 12 12) translate(0.5 0)"
            >
              <path d="M9 2v17.5a2.5 2.5 0 0 0 5 0V2" fill="white" />
              <path d="M8 2h7" />
              <path d="M9.5 12h4" />
            </g>
            <g
              stroke="#be123c"
              transform="rotate(45 12 12) translate(0.5 0)"
            >
              <path d="M9 2v17.5a2.5 2.5 0 0 0 5 0V2" fill="white" />
              <path d="M8 2h7" />
              <path d="M9.5 12h4" />
            </g>
          </svg>
          <span className="text-base font-bold uppercase tracking-wide text-accent-600">
            Contra
          </span>
        </div>
      </div>
      <div className="mx-auto max-w-4xl px-6 pb-16 pt-8">
        <header className="text-center">
          <h1 className="text-3xl font-semibold tracking-tight text-slate-900">
            Surfacing disagreement in research
          </h1>
          <p className="mx-auto mt-4 max-w-2xl text-base leading-relaxed text-slate-600">
            A research tool exploring how AI can reliably detect disagreement
            in the scientific literature, with a focus on Alzheimer's research
          </p>
        </header>

        <form
          className="mt-8"
          onSubmit={(e) => {
            e.preventDefault();
            void submit();
          }}
        >
          <div className="rounded-2xl border border-slate-200 bg-white shadow-prompt transition focus-within:border-accent-400 focus-within:shadow-[0_0_0_4px_rgba(58,111,224,0.12),0_8px_28px_rgba(58,111,224,0.10)]">
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  void submit();
                }
              }}
              placeholder={placeholder}
              rows={3}
              disabled={loading}
              className="w-full resize-none rounded-2xl bg-transparent px-5 pt-4 pb-2 text-[15px] leading-relaxed text-slate-900 placeholder:text-slate-400 focus:outline-none disabled:opacity-60"
            />
            <div className="flex items-center justify-between px-3 pb-3">
              <div className="flex items-center gap-2 px-2 text-xs text-slate-500">
                <span className="inline-flex items-center gap-1.5 rounded-md border border-slate-200 bg-slate-50 px-2 py-1 font-medium text-slate-600">
                  <span className="h-1.5 w-1.5 rounded-full bg-accent-500" />
                  Research agent
                </span>
              </div>
              <button
                type="submit"
                disabled={loading || !question.trim()}
                className="inline-flex h-9 w-9 items-center justify-center rounded-lg bg-accent-500 text-white shadow-sm transition hover:bg-accent-600 disabled:bg-slate-200 disabled:text-slate-400"
                aria-label="Search"
              >
                {loading ? (
                  <svg
                    className="h-4 w-4 animate-spin"
                    viewBox="0 0 24 24"
                    fill="none"
                  >
                    <circle
                      cx="12"
                      cy="12"
                      r="9"
                      stroke="currentColor"
                      strokeOpacity="0.3"
                      strokeWidth="3"
                    />
                    <path
                      d="M21 12a9 9 0 0 0-9-9"
                      stroke="currentColor"
                      strokeWidth="3"
                      strokeLinecap="round"
                    />
                  </svg>
                ) : (
                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    className="h-4 w-4"
                    stroke="currentColor"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M5 12h14M13 5l7 7-7 7" />
                  </svg>
                )}
              </button>
            </div>
          </div>
        </form>

        {examples.length > 0 && !result && !loading && (
          <div className="mt-8">
            <div className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-500">
              Try an example
            </div>
            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {examples.map((ex) => (
                <button
                  key={ex}
                  onClick={() => void submit(ex)}
                  className="group rounded-xl border border-slate-200 bg-white p-4 text-left shadow-card transition hover:border-accent-300 hover:shadow-md"
                >
                  <div className="mb-2 inline-flex items-center gap-1.5 rounded-md bg-slate-100 px-2 py-0.5 text-[11px] font-medium text-slate-600">
                    <span className="h-1.5 w-1.5 rounded-full bg-accent-500" />
                    Research agent
                  </div>
                  <div className="text-sm leading-snug text-slate-800 group-hover:text-slate-900">
                    {ex}
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}

        {loading && (
          <div className="mt-10 flex items-center gap-3 rounded-xl border border-slate-200 bg-white px-5 py-4 text-sm text-slate-600 shadow-card">
            <span className="relative flex h-2.5 w-2.5">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-accent-400 opacity-60" />
              <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-accent-500" />
            </span>
            <span>Retrieving and classifying studies… (~5–10 seconds)</span>
          </div>
        )}

        {error && (
          <div className="mt-10 rounded-xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-800">
            <strong className="font-semibold">Error:</strong> {error}
          </div>
        )}

        {result && <Results result={result} />}
      </div>
    </main>
  );
}
