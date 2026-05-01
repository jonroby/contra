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
    <li className="border-b border-slate-200 py-5 last:border-0">
      <div className="flex items-center gap-2 text-xs text-slate-500">
        <span className="font-medium text-slate-600">{year}</span>
        {finding.pmid && (
          <>
            <span className="text-slate-300">·</span>
            <span>PMID {finding.pmid}</span>
          </>
        )}
      </div>
      {link ? (
        <a
          href={link}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-1 block text-[15px] font-semibold text-accent-700 hover:text-accent-800 hover:underline"
        >
          {finding.title}
        </a>
      ) : (
        <div className="mt-1 text-[15px] font-semibold text-slate-900">
          {finding.title}
        </div>
      )}
      <p className="mt-1.5 text-sm leading-relaxed text-slate-700">
        {finding.claim}
      </p>
      <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-slate-500">
        <span>{pop}</span>
        <span className="text-slate-300">·</span>
        <span>{n}</span>
        <span className="text-slate-300">·</span>
        <span>
          confidence{" "}
          <span className="font-medium text-slate-700">{conf}</span>
        </span>
      </div>
    </li>
  );
}
