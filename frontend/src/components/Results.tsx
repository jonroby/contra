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
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-card">
        <div className="text-xs font-semibold uppercase tracking-wider text-slate-500">
          Summary
        </div>
        <p className="mt-2 text-[15px] leading-relaxed text-slate-800">
          {result.summary}
        </p>

        <div className="mt-5 flex flex-wrap items-center gap-2">
          <CountChip label="Supports" value={counts.supports} tone="accent" />
          <CountChip label="Contradicts" value={counts.contradicts} tone="rose" />
          <CountChip
            label="Inconclusive"
            value={counts.inconclusive}
            tone="slate"
          />
        </div>

        <div className="mt-3 text-xs text-slate-500">
          retrieval {t.retrieval_s ?? "?"}s · extraction {t.extraction_s ?? "?"}s
          · synthesis {t.synthesis_s ?? "?"}s
        </div>
      </div>

      <div className="mt-6 flex gap-1 border-b border-slate-200">
        {TABS.map(({ id, label }) => (
          <button
            key={id}
            onClick={() => setTab(id)}
            className={`relative px-4 py-2.5 text-sm font-medium transition-colors ${
              tab === id
                ? "text-accent-600"
                : "text-slate-500 hover:text-slate-800"
            }`}
          >
            {label}{" "}
            <span
              className={`ml-1 rounded-md px-1.5 py-0.5 text-xs ${
                tab === id
                  ? "bg-accent-50 text-accent-700"
                  : "bg-slate-100 text-slate-500"
              }`}
            >
              {counts[id]}
            </span>
            {tab === id && (
              <span className="absolute inset-x-0 -bottom-px h-0.5 rounded-full bg-accent-500" />
            )}
          </button>
        ))}
      </div>

      <ul className="mt-2">
        {findings.length === 0 ? (
          <li className="py-10 text-center text-sm text-slate-400 italic">
            No studies in this group.
          </li>
        ) : (
          findings.map((f, i) => (
            <FindingCard key={f.pmid ?? `${tab}-${i}`} finding={f} />
          ))
        )}
      </ul>
    </section>
  );
}

function CountChip({
  label,
  value,
  tone,
}: {
  label: string;
  value: number;
  tone: "accent" | "rose" | "slate";
}) {
  const tones = {
    accent: "bg-accent-50 text-accent-700 ring-accent-100",
    rose: "bg-rose-50 text-rose-700 ring-rose-100",
    slate: "bg-slate-100 text-slate-700 ring-slate-200",
  } as const;
  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-md px-2.5 py-1 text-xs font-medium ring-1 ring-inset ${tones[tone]}`}
    >
      <span className="opacity-80">{label}</span>
      <span className="font-semibold">{value}</span>
    </span>
  );
}
