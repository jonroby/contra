import { useState } from "react";
import type { QueryResult, Tab } from "../types";
import { FindingCard } from "./FindingCard";

const TABS: { id: Tab; label: string }[] = [
  { id: "supports", label: "Supporting" },
  { id: "contradicts", label: "Contradicting" },
  { id: "inconclusive", label: "Inconclusive" },
];

export function Results({ result }: { result: QueryResult }) {
  const [tab, setTab] = useState<Tab>("supports");

  const counts = {
    supports: result.supports.length,
    contradicts: result.contradicts.length,
    inconclusive: result.inconclusive.length,
  };
  const findings = result[tab];
  const t = result.metadata.timings;

  return (
    <section className="mt-10">
      <h2 className="text-xl font-semibold text-slate-900">Summary</h2>
      <p className="mt-2 text-slate-700 leading-relaxed">{result.summary}</p>

      <div className="mt-4 text-sm text-slate-600">
        <span className="font-medium">Supports:</span> {counts.supports} ·{" "}
        <span className="font-medium">Contradicts:</span> {counts.contradicts} ·{" "}
        <span className="font-medium">Inconclusive:</span> {counts.inconclusive}
      </div>
      <div className="mt-1 text-xs text-slate-500">
        retrieval {t.retrieval_s ?? "?"}s · extraction {t.extraction_s ?? "?"}s
        · synthesis {t.synthesis_s ?? "?"}s
      </div>

      <div className="mt-6 flex gap-1 border-b border-slate-200">
        {TABS.map(({ id, label }) => (
          <button
            key={id}
            onClick={() => setTab(id)}
            className={`px-4 py-2 text-sm font-medium transition-colors ${
              tab === id
                ? "border-b-2 border-orange-500 text-orange-600"
                : "text-slate-500 hover:text-slate-700"
            }`}
          >
            {label} ({counts[id]})
          </button>
        ))}
      </div>

      <ul className="mt-2">
        {findings.length === 0 ? (
          <li className="py-6 text-slate-400 italic">No studies in this group.</li>
        ) : (
          findings.map((f, i) => (
            <FindingCard key={f.pmid ?? `${tab}-${i}`} finding={f} />
          ))
        )}
      </ul>
    </section>
  );
}
