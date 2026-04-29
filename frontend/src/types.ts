export interface Finding {
  pmid: string | null;
  title: string;
  year: number | null;
  claim: string;
  direction: "supports" | "contradicts" | "inconclusive";
  intervention: string | null;
  population: string | null;
  sample_size: number | null;
  duration: string | null;
  confidence: "high" | "medium" | "low" | null;
}

export interface Timings {
  retriever_init_s?: number;
  retrieval_s?: number;
  extraction_s?: number;
  synthesis_s?: number;
}

export interface Metadata {
  target: string;
  top_k: number;
  n_retrieved: number;
  n_findings: number;
  timings: Timings;
}

export interface QueryResult {
  query: string;
  summary: string;
  supports: Finding[];
  contradicts: Finding[];
  inconclusive: Finding[];
  metadata: Metadata;
}

export type Tab = "supports" | "contradicts" | "inconclusive";
