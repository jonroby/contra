import type { Finding } from "../types";

const DESIGN_PRIORITY = [
  "Meta-Analysis",
  "Systematic Review",
  "Randomized Controlled Trial",
  "Clinical Trial",
  "Observational Study",
  "Review",
  "Case Reports",
];

function studyDesign(types: string[] | null): string | null {
  if (!types || types.length === 0) return null;
  for (const label of DESIGN_PRIORITY) {
    if (types.includes(label)) return label;
  }
  return null;
}

function formatCitations(n: number): string {
  if (n >= 1000) return `${(n / 1000).toFixed(1).replace(/\.0$/, "")}k`;
  return String(n);
}

const LOWERCASE_WORDS = new Set([
  "a", "an", "the",
  "and", "or", "but", "nor", "so", "yet",
  "of", "in", "on", "at", "to", "for", "by", "with", "from", "as", "vs",
]);

function titleCase(s: string): string {
  return s
    .split(/(\s+)/)
    .map((token, i) => {
      if (/^\s+$/.test(token)) return token;
      const lower = token.toLowerCase();
      if (i > 0 && LOWERCASE_WORDS.has(lower)) return lower;
      return lower.charAt(0).toUpperCase() + lower.slice(1);
    })
    .join("");
}

function shortJournal(journal: string): string {
  return titleCase(journal.split(/\s[:.]\s/)[0].trim());
}

export function FindingCard({ finding }: { finding: Finding }) {
  const pubmed = finding.pmid
    ? `https://pubmed.ncbi.nlm.nih.gov/${finding.pmid}/`
    : null;
  const year = finding.year ?? "?";
  const design = studyDesign(finding.publication_types);

  const meta: { key: string; node: React.ReactNode }[] = [];
  if (design) meta.push({ key: "design", node: <span>{design}</span> });
  if (finding.cited_by_count != null) {
    meta.push({
      key: "cited",
      node: <span>cited {formatCitations(finding.cited_by_count)}×</span>,
    });
  }
  if (finding.sample_size) {
    meta.push({ key: "n", node: <span>n={finding.sample_size}</span> });
  }
  if (finding.journal) {
    meta.push({
      key: "journal",
      node: <span className="italic">{shortJournal(finding.journal)}</span>,
    });
  }
  if (finding.oa_pdf_url) {
    meta.push({
      key: "pdf",
      node: (
        <a
          href={finding.oa_pdf_url}
          target="_blank"
          rel="noopener noreferrer"
          className="font-medium text-accent-600 hover:text-accent-700 hover:underline"
        >
          PDF
        </a>
      ),
    });
  }

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
      {pubmed ? (
        <a
          href={pubmed}
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
      {meta.length > 0 && (
        <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-slate-500">
          {meta.map((m, i) => (
            <span key={m.key} className="inline-flex items-center">
              {i > 0 && <span className="mr-3 text-slate-300">·</span>}
              {m.node}
            </span>
          ))}
        </div>
      )}
    </li>
  );
}
