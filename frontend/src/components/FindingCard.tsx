import type { Finding } from "../types";

export function FindingCard({ finding }: { finding: Finding }) {
  const link = finding.pmid
    ? `https://pubmed.ncbi.nlm.nih.gov/${finding.pmid}/`
    : null;
  const year = finding.year ?? "?";
  const n = finding.sample_size ? `n=${finding.sample_size}` : "n=?";
  const pop = finding.population ?? "—";
  const conf = finding.confidence ?? "?";

  return (
    <li className="border-b border-slate-200 py-4 last:border-0">
      <div className="text-sm text-slate-500">[{year}]</div>
      {link ? (
        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="text-base font-medium text-indigo-700 hover:underline"
        >
          {finding.title}
        </a>
      ) : (
        <div className="text-base font-medium text-slate-900">
          {finding.title}
        </div>
      )}
      <p className="mt-1 italic text-slate-700">{finding.claim}</p>
      <div className="mt-1 text-xs text-slate-500">
        {pop} · {n} · confidence: {conf}
      </div>
    </li>
  );
}
