# Q4: Is there a causal link between herpes simplex virus and Alzheimer's?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=28 PMIDs.

**Current S/C/I**: 22 / 1 / 5
**Proposed S/C/I**: 13 / 2 / 13
**Net flips**: 14 (mostly S→I scope/mechanism, plus the VALAD I→C flip; +3 added on second pass: `1328575`, `40898264`, `11848687`)

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `41405855` | 2026 | **inconclusive → contradicts** | VALAD valacyclovir RCT. Primary endpoint (ADAS-Cog at 78 weeks): **valacyclovir group had MORE cognitive worsening** than placebo (between-group difference 3.93, p=.01). Conclusion: *"valacyclovir was not efficacious with cognitive worsening for the primary outcome and it is not recommended."* This is a **statistically significant negative finding** in the only large dedicated antiviral RCT — the canonical `contradicts` for the antiviral arm of this question. |
| `37904465` | 2023 | **supports → inconclusive** | Herpes Zoster meta. Verbatim: *"the pooled analysis showed **no statistically significant difference** between the dementia group and the No dementia group"* (RR 1.04, p=.70) for HZV-dementia incidence. Only the HZ-ophthalmicus subgroup was significant. The headline is null. This is a **mislabel**. |
| `25376108` | 2014 | **supports → inconclusive** | Cell-line in-vitro study of Aβ peptide antiviral activity vs HSV-1 — purely mechanistic. No clinical/epidemiological data. Mechanism papers should be `inconclusive` per the bar (or arguably excluded). |
| `2172499` | 1990 | **supports → inconclusive** | Sera study, n=19+21. Verbatim: *"Antiviral antibody titers showed no significant differences except for antibodies to herpes simplex virus-1, which were **increased in control group**"* — i.e., AD patients had *fewer* anti-HSV-1 antibodies. The conclusion emphasizes autoimmunity, not viral. The current `supports` is wrong. (`contradicts` would be defensible too — it's pointing in the *opposite* direction from the question.) |
| `16595160` | 2006 | **supports → inconclusive** | TAP2 SNP genotype study — *"consistent with the hypothesis that human genetic variants facilitating the access of HSV-1 to the brain might result in susceptibility to AD."* Indirect/mechanistic; doesn't directly test the HSV→AD link. |
| `29676229` | 2019 | **supports → inconclusive** | Systems-biology / data-mining review of viral-host gene interactions. No primary epidemiology. Mechanism + drug-discovery framing. |
| `38549138` | 2024 | **supports → inconclusive** | CMV-neurological SR. Verbatim: *"the direct cause-effect relationship is not fully understood and several gaps in knowledge persist."* Plus this is **CMV not HSV** — only tangentially relevant to the question. Should arguably be excluded from `relevant_pmids`. |
| `40442743` | 2025 | **supports → inconclusive** | HSV-1/CMV oxidative stress mechanism paper. Mechanism only — no cognitive/clinical efficacy outcome. |
| `41073371` | 2025 | **inconclusive → supports** | Pooled estimates significant: HHV OR 1.24 (CI 1.02–1.51) for AD risk. Note "inconclusive" was reading from the abstract's *background*, not the result. |
| `41275158` | 2025 | **inconclusive → supports** | HHV-6 meta — pooled OR 1.81 (CI 1.16–2.84, p=0.009) for AD risk. Sensitivity analysis OR 2.78. Significant positive. |
| `41953111` | 2026 | **supports → inconclusive** | HSV-2 dementia meta. Conclusion: *"no clear association between HSV-2 and Alzheimer's disease."* Pooled ORs cross null across multiple methods; only one HR analysis borderline (1.37, CI 1.00–1.89). Headline is null. |
| `1328575` | 1992 | **supports → inconclusive** | Itzhaki landmark, but the abstract itself reports HSV-1 thymidine kinase gene in **14/21 SDAT cases AND 9/15 elderly normals** — no significant AD-specific elevation stated. Conclusion: *"the presence of Herpes simplex virus type 1 DNA is a region-dependent feature of the aged brain"* — i.e., it's in aged brains generally, not AD-specifically. This is a foundational mechanism/pathology paper, not an epidemiological supports. |
| `40898264` | 2025 | **supports → inconclusive** | Herpesviruses+antiviral meta. Conclusion verbatim: *"the present review of the scientific literature **generally shows little evidence of an association between herpesviruses and risk of dementia**. However, the review shows evidence of an association between antiviral treatment and a decreased risk of dementia."* The herpesvirus-dementia arm (the question's main hypothesis) is explicitly downplayed by the authors; HSV1/2 HR 1.36 (CI 1.01–1.83) and VZV HR 1.12 (CI 1.00–1.25) are borderline at the null. Mixed signal between herpesvirus arm (~null) and antiviral arm (sig protective). |
| `11848687` | 2002 | **supports → inconclusive** | Itzhaki/CMV-in-VaD paper. The paper is **about CMV in vascular dementia, not HSV in AD** (title: "Cytomegalovirus is present in a very high proportion of brains from vascular dementia patients"). HSV-1+APOE4 is mentioned only as a prior finding in the intro. Conclusion: *"Further studies are needed to reveal whether or not the association of CMV with VaD is causal."* This does not support HSV→AD. Scope drift + tentative conclusion. |

## Confirmed (no change)

- `26401558` (2015 herpesviridae meta, OR 1.38 sig) — **supports ✓**
- `33657269` (2021 multi-country, antiherpetic ≠ reduced dementia) — **contradicts ✓**
- `32280095` (2020 meta, HSV-1 OR 1.34 sig) — **supports ✓**
- `15207442` (2004 small DEBATE study, viral burden ↔ MMSE) — **inconclusive ✓**
- `33317741` (2020 meta, OR 1.40 sig) — **supports ✓**
- `30427305` (2018 HHV-6 autophagy mechanism) — **inconclusive ✓**
- `37639023` (2023 VZV meta, HR 1.11 sig) — **supports ✓**
- `37801540` (2023 SR — substantiates HSV-1↔AD relationship) — **supports ✓**
- `41269248` (2025 vaccinations meta, HZ vaccine RR 0.53 sig for AD) — **supports ✓**
- `40551502` (2025 HZ vaccine meta, HR 0.71 sig) — **supports ✓**
- `40140230` (2025 HSV-1 meta, OR 1.39 sig) — **supports ✓**
- `41490027` (2026 VZV meta, RR 1.12 sig) — **supports ✓**
- `41467972` (2025 anti-herpetic meta, aHR 0.77 sig) — **supports ✓**
- `40934136` (2025 HSV meta, OR 1.32 sig) — **supports ✓**

## Borderline (not flipped, but flagged for cross-question policy decisions)

- **`2172499`** (1990 sera, n=19+21) — already proposed S→I, but per the strict bar the abstract reports anti-HSV-1 antibodies were **higher in controls** than in AD patients (statistically significant difference in the *opposite* direction from the question). Could push to `contradicts` as a "statistically significant negative finding pointing the wrong way." Defensible either way; flagging as **policy issue (b)-adjacent / (c)-adjacent** — small-n biomarker study with a directionally contradicting signal that the authors framed as autoimmune rather than viral. Cross-question question: should small-n studies whose primary finding contradicts the question's hypothesis be `contradicts` regardless of N, or should N gate the bar?

- **`37904465`** (HZ-dementia meta) — the proposed flip S→I is a clean instance of **policy issue (a): subgroup-positive in parent-null meta**. Pooled HZV-dementia RR 1.04 (p=.70) is null; only the HZ-ophthalmicus subgroup is significant (RR 6.26). Currently `supports` riding entirely on the subgroup. The flip to `inconclusive` is correct, but flagging the pattern: when a meta-analysis's headline pooled result is null and only a pre-specified subgroup is positive, the strict-bar default should be `inconclusive`, not `supports`.

- **`16595160`** (TAP2 SNP), **`29676229`** (systems-biology gene-mining), **`25376108`** (cell-line antiviral activity), **`30427305`** (HHV-6 autophagy mechanism), **`40442743`** (oxidative stress mechanism), **`38549138`** (CMV-neuro SR with no pooled estimate, conclusion explicitly hedges) — all flagged as **policy issue (b): preclinical/mech-dominated papers labeled `supports`**. Of these, `25376108`, `16595160`, `29676229`, `40442743`, `38549138` are already in the proposed-flips table (S→I). `30427305` is already `inconclusive`. The pattern is widespread on this question because herpesvirus-AD has a large mechanism literature; cross-question policy: should the corpus filter exclude `Comparative Study` / non-RCT non-observational papers from the candidate pool entirely, or should the stance bar treat any mechanism-only paper as `inconclusive` by default?

## Cross-cutting issues

- **Heavy meta-analysis stack.** ~14 of 28 are SR/meta. With paper-type
  filtering, primary epidemiology drops dramatically.
- **Scope drift** — papers about CMV (`38549138`, `11848687`), HZV
  (`37904465`, `37639023`, `40551502`, `41269248`, `41490027`), HHV-6
  (`41275158`, `30427305`), and HSV-2 (`41953111`) are tangential to the
  HSV-and-Alzheimer's question. The question should either be broadened to
  "herpesviruses and AD" or these should move to `excluded`.
- **Mechanism-paper stance inflation.** Six of the original `supports`
  labels were on papers with no clinical efficacy data (mechanism, in vitro,
  bioinformatics, gene-association, oxidative-stress markers). After this
  pass, all six are flipped or already non-supports. The corpus filter or
  stance prompt should treat mechanism-only papers as `inconclusive` by
  default rather than reading "supports the viral hypothesis" as `supports`
  for the clinical question.

## Highest-confidence flips for this question

- `41405855` (VALAD) inconclusive → contradicts — primary endpoint
  significant *worsening* on valacyclovir; this is the canonical
  contradicting RCT in the antiviral arm and was sitting as `inconclusive`.
- `37904465` supports → inconclusive — pooled HZV-dementia RR 1.04 (p=.70)
  was labeled `supports`.
- `40898264` supports → inconclusive — meta conclusion verbatim says
  *"generally shows little evidence of an association between herpesviruses
  and risk of dementia"* yet was labeled `supports`. The antiviral arm hits,
  but the herpesvirus arm (the question's primary hypothesis) is null.
- `1328575` supports → inconclusive — Itzhaki landmark, but the abstract
  shows HSV-1 DNA in 14/21 AD AND 9/15 normal aged brains (no AD-specific
  elevation reported); conclusion explicitly says it's a feature of aged
  brains generally.
- `11848687` supports → inconclusive — paper is about CMV in vascular
  dementia, not HSV in AD; conclusion is tentative ("further studies needed").

These five are unambiguous mislabels. Plus `2172499` is at minimum I, and
arguably `contradicts`.

## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

### Proposed new tags (Q4)

- `mechanism_only` — paper has no clinical/epidemiological endpoint (in vitro,
  cell line, gene-association/SNP, bioinformatics, oxidative-stress markers).
  Distinct from `preclinical_dominated` (which is for reviews/metas pooling
  preclinical evidence); `mechanism_only` tags primary mechanism studies
  themselves. Q4 is mechanism-heavy because of the antimicrobial-protection
  hypothesis literature.
- `scope_drift_virus` — paper studies a herpesvirus other than the question's
  primary target (HSV-1). Q4's question is HSV↔AD; tag covers HSV-2, HZV/VZV,
  HHV-6, CMV, EBV. Distinct from `wrong_population` (which is about human
  cohort mismatch — wrong age, wrong disease); `scope_drift_virus` is about
  the pathogen being adjacent rather than on-target. Useful because this
  question has heavy scope drift across the herpesviridae family and a UI
  filter or cross-question policy may want to separate them.
- `landmark_no_group_difference` — historically influential paper (cited as
  supportive in downstream literature) whose own abstract reports no
  AD-specific elevation versus controls. The "supports" label rides on
  citation reputation, not the paper's own numbers. Applies to `1328575`
  (Itzhaki 1992, HSV-1 DNA in 14/21 SDAT AND 9/15 normal aged brains).
- `directionally_opposite_finding` — small-n primary study whose statistically
  significant signal points *opposite* to the question's hypothesis (e.g.,
  marker higher in controls than cases). Currently labeled `supports` or
  `inconclusive` by reputation/framing, but the data are arguably `contradicts`.
  Applies to `2172499` (anti-HSV-1 antibodies higher in controls than AD).

### Tag assignments

- `25376108` — `mechanism_only` (Aβ-vs-HSV-1 cell-line antiviral assay, no clinical data)
- `1328575` — `landmark_no_group_difference`, `mechanism_only` (HSV-1 DNA
  PCR in postmortem brain; reports presence in both AD and aged-normal,
  no AD-specific elevation in abstract)
- `11848687` — `scope_drift_virus`, `wrong_population` (paper is about CMV
  in vascular dementia, not HSV in AD; HSV/APOE4 is mentioned only as prior
  finding in intro)
- `2172499` — `directionally_opposite_finding`, `mechanism_only` (small
  sera study n=19+21; anti-HSV-1 antibodies higher in controls than AD)
- `15207442` — (none — small-n DEBATE substudy but already correctly
  labeled `inconclusive`; mixed across pathogens flagged in golden note)
- `30427305` — `mechanism_only`, `scope_drift_virus` (HHV-6, not HSV;
  autophagy/ER-stress in cell lines)
- `37904465` — `subgroup_positive`, `scope_drift_virus` (HZV; pooled
  HZV-dementia RR 1.04 p=.70 null, only HZ-ophthalmicus subgroup RR 6.26 sig)
- `38549138` — `narrative_review`, `scope_drift_virus` (CMV-neurological SR,
  no pooled estimate, conclusion explicitly hedges "direct cause-effect
  relationship is not fully understood")
- `37639023` — `scope_drift_virus` (VZV-dementia meta; clean within its
  scope but tangential to HSV→AD question)
- `40898264` — `hedged_meta` (authors verbatim: "generally shows little
  evidence of an association between herpesviruses and risk of dementia";
  borderline CIs touching null on herpesvirus arm; antiviral arm carries the
  signal)
- `41269248` — `scope_drift_virus` (HZ vaccine + influenza + pneumococcal +
  Tdap meta; HSV not assessed)
- `40442743` — `mechanism_only` (oxidative-stress / inflammation / apoptosis
  serum markers; no cognitive endpoint despite "RCT" type label)
- `40551502` — `scope_drift_virus` (HZ vaccine cohort meta; HSV not assessed)
- `41073371` — `scope_drift_virus` (HHV result is the "supports" signal for
  AD; HHV is a broad family — not a clean HSV-1 read)
- `41490027` — `scope_drift_virus` (VZV; clean meta within its scope)
- `41275158` — `scope_drift_virus` (HHV-6, not HSV; clean meta within scope)
- `41953111` — `scope_drift_virus`, `hedged_meta` (HSV-2; pooled ORs cross
  null across multiple methods, conclusion: "no clear association between
  HSV-2 and Alzheimer's disease")
- `16595160` — `mechanism_only` (TAP2 SNP genotype association; indirect
  genetic-susceptibility framing, no direct HSV→AD epidemiology)
- `29676229` — `mechanism_only`, `narrative_review` (systems-biology gene
  mining + drug-discovery; no primary epidemiology)
- All other pmids — untagged (strong/canonical examples within their stance bucket)

Untagged: `26401558`, `33657269`, `32280095`, `33317741`, `37801540`,
`41405855`, `40140230`, `41467972`, `40934136`.

---

## Abstracts (n=28)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 25376108 — current stance: `supports`

**Evidence span:** > Our data suggest that Aβ peptides represent a novel class of antimicrobial peptides that protect against neurotropic enveloped virus infections such as HSV-1.

**Golden note:** Aβ peptides display antiviral activity against HSV-1 — supports antimicrobial-protection hypothesis.

**β-Amyloid peptides display protective activity against the human Alzheimer's disease-associated herpes simplex virus-1.**

*Biogerontology*, 2014. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> Amyloid plaques, the hallmark of Alzheimer's disease (AD), contain fibrillar β-amyloid (Aβ) 1-40 and 1-42 peptides. Herpes simplex virus 1 (HSV-1) has been implicated as a risk factor for AD and found to co-localize within amyloid plaques. Aβ 1-40 and Aβ 1-42 display anti-bacterial, anti-yeast and anti-viral activities. Here, fibroblast, epithelial and neuronal cell lines were exposed to Aβ 1-40 or Aβ 1-42 and challenged with HSV-1. Quantitative analysis revealed that Aβ 1-40 and Aβ 1-42 inhibited HSV-1 replication when added 2 h prior to or concomitantly with virus challenge, but not when added 2 or 6 h after virus addition. In contrast, Aβ 1-40 and Aβ 1-42 did not prevent replication of the non-enveloped human adenovirus. In comparison, antimicrobial peptide LL-37 prevented HSV-1 infection independently of its sequence of addition. Our findings showed also that Aβ 1-40 and Aβ 1-42 acted directly on HSV-1 in a cell-free system and prevented viral entry into cells. The sequence homology between Aβ and a proximal transmembrane region of HSV-1 glycoprotein B suggested that Aβ interference with HSV-1 replication could involve its insertion into the HSV-1 envelope. Our data suggest that Aβ peptides represent a novel class of antimicrobial peptides that protect against neurotropic enveloped virus infections such as HSV-1. Overproduction of Aβ peptide to protect against latent herpes viruses and eventually against other infections, may contribute to amyloid plaque formation, and partially explain why brain infections play a pathogenic role in the progression of the sporadic form of AD.

---

### PMID 1328575 — current stance: `supports`

**Evidence span:** > Using the highly sensitive polymerase chain reaction, we have detected the viral thymidine kinase gene in post-mortem brain from 14/21 cases of senile dementia of the Alzheimer type and 9/15 elderly normals... Thus, the presence of Herpes simplex virus type 1 DNA is a region-dependent feature of the aged brain.

**Golden note:** Itzhaki 1992 — HSV-1 DNA in AD brains. Landmark observation.

**Herpes simplex virus type 1 DNA is present in specific regions of brain from aged people with and without senile dementia of the Alzheimer type.**

*The Journal of pathology*, 1992. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> We have investigated the possible involvement of viruses, specifically Herpes simplex virus type 1, in senile dementia of the Alzheimer type (SDAT). Using the highly sensitive polymerase chain reaction, we have detected the viral thymidine kinase gene in post-mortem brain from 14/21 cases of senile dementia of the Alzheimer type and 9/15 elderly normals. The temporal cortex and hippocampus were usually virus-positive; in contrast, the occipital cortex was virus-negative in 9/9 SDAT cases and 5/5 elderly normals. Temporal and frontal cortex from younger normals (five infants and five middle-aged) were negative. Thus, the presence of Herpes simplex virus type 1 DNA is a region-dependent feature of the aged brain.

---

### PMID 26401558 — current stance: `supports`

**Evidence span:** > There was an increased risk for AD when herpesviridae is present in the brain compared to controls [OR 1.38; 95% CI 1.14-1.66].

**Golden note:** Meta-analysis — herpesviruses increase AD risk.

**Herpes Viruses Increase the Risk of Alzheimer's Disease: A Meta-Analysis.**

*Journal of Alzheimer's disease : JAD*, 2015. Types: Journal Article; Meta-Analysis

> The role of infectious agents in the development of AD has long been debated, in particular, the herpesviridae family. We therefore conducted a meta-analysis to quantitatively assess all published data to establish whether there is an association. We identified studies that looked for the presence of viral DNA in the brain and/or antibody seropositivity in people with AD from four electronic databases. 35 studies met our inclusion criteria (AD cases = 1294; controls = 3059). There was an increased risk for AD when herpesviridae is present in the brain compared to controls [OR 1.38; 95% CI 1.14-1.66]. Sub-analysis showed that APOE ɛ4 and HSV1 together increased the risk of AD development [OR 2.71; 95% CI 1.08-6.80]. HSV1 together with the presence of the APOE ɛ4 allele increases the risk of developing AD.

---

### PMID 11848687 — current stance: `supports`

**Evidence span:** > We have found that a very high proportion of the VaD patients, 93% (14/15), but not of age-matched normals, 34% (10/29), harbor CMV DNA (P = 0.0002); the proportions of the patients harboring the other viruses in brain do not differ significantly from those of the normals.

**Golden note:** Itzhaki — HSV-1 + APOE4 strong AD risk factor; CMV in vascular dementia.

**Cytomegalovirus is present in a very high proportion of brains from vascular dementia patients.**

*Neurobiology of disease*, 2002. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> We previously found that herpes simplex type 1 virus (HSV1), when present in brain of carriers of the apolipoprotein E type 4 allele is a strong risk factor for Alzheimer's disease. To find if HSV1 or certain other herpesviruses are involved in vascular dementia (VaD), we searched post mortem brain specimens from patients suffering from VaD for the presence of HSV1, cytomegalovirus (CMV), and human herpesvirus type 6 DNA, using polymerase chain reaction. We have found that a very high proportion of the VaD patients, 93% (14/15), but not of age-matched normals, 34% (10/29), harbor CMV DNA (P = 0.0002); the proportions of the patients harboring the other viruses in brain do not differ significantly from those of the normals. Further studies are needed to reveal whether or not the association of CMV with VaD is causal.

---

### PMID 2172499 — current stance: `supports`

**Evidence span:** > Antiviral antibody titers showed no significant differences except for antibodies to herpes simplex virus-1, which were increased in control group.

**Golden note:** Antibodies to viruses elevated in AD — early supportive observation.

**Antibodies to viral antigens, xenoantigens, and autoantigens in Alzheimer's disease.**

*Journal of clinical laboratory analysis*, 1990. Types: Comparative Study; Journal Article

> Sera from 19 patients with Alzheimer's disease (AD) and 21 control subjects were studied by immunofluorescence and enzyme immunoassay for antibody activity against various viruses and 12 self- and non-self-antigens. Total IgG mean level was significantly higher in the AD group; the IgG level was above 15 g/L in 52.8% of AD patients versus 14.3% of control subjects. Antiviral antibody titers showed no significant differences except for antibodies to herpes simplex virus-1, which were increased in control group. In contrast, autoantibodies were more frequently found in AD patients, and the prevalence of antibodies to spectrin, peroxidase, and thyroglobulin was significantly increased. Thus, in our series, autoimmune but not antiviral responses were heightened in at least 42% of AD patients (versus 9% of the control group) suggesting the existence of two subpopulations in the AD group.

---

### PMID 33657269 — current stance: `contradicts`

**Evidence span:** > Short-term antiherpetic medication is not markedly associated with incident dementia. Because neither dementia subtype nor herpes subtype modified the association, the small but significant decrease in dementia incidence with antiherpetic administration may reflect confounding and misclassification.

**Golden note:** Multi-country cohort — antiherpetic medication NOT associated with reduced dementia.

**Antiherpetic medication and incident dementia: Observational cohort studies in four countries.**

*European journal of neurology*, 2021. Types: Journal Article; Multicenter Study; Observational Study; Research Support, Non-U.S. Gov't

> BACKGROUND AND PURPOSE: Several epidemiological studies from Taiwan, all using the same data resource, found significant associations between herpes virus infection, antiherpetic medication, and subsequent dementia. We conducted a multicenter observational cohort study using health registry data from Wales, Germany, Scotland, and Denmark to investigate potential associations between antiherpetic medication and incident dementia, and also to comprehensively investigate such associations broken down according to medication type and dose, type of herpes virus, and dementia subtype. METHODS: A total of 2.5 million individuals aged 65 years or more were followed up using linked electronic health records in four national observational cohort studies. Exposure and outcome were classified using coded data from primary and secondary care. Data were analyzed using survival analysis with time-dependent covariates. RESULTS: Results were heterogeneous, with a tendency toward decreased dementia risk in individuals exposed to antiherpetic medication. Associations were not affected by treatment number, herpes subtype, dementia subtype, or specific medication. In one cohort, individuals diagnosed with herpes but not exposed to antiherpetic medication were at higher dementia risk. CONCLUSIONS: Short-term antiherpetic medication is not markedly associated with incident dementia. Because neither dementia subtype nor herpes subtype modified the association, the small but significant decrease in dementia incidence with antiherpetic administration may reflect confounding and misclassification.

---

### PMID 32280095 — current stance: `supports`

**Evidence span:** > Herpes simplex virus-1 (OR:1.34, 95% CI = 1.02-1.75; I2 = 0%), and the Herpesviridae family (OR:1.41, 95% CI = 1.15-1.74; I2 = 12%) infection were associated with a higher risk of AD.

**Golden note:** Infectious agents-AD meta — significant association including HSV.

**Associations of Infectious Agents with Alzheimer's Disease: A Systematic Review and Meta-Analysis.**

*Journal of Alzheimer's disease : JAD*, 2020. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: The role of infectious agents in the development of Alzheimer's disease (AD) has long been debated, however, uncertainties still persist. OBJECTIVE: We aimed to illuminate the associations between infectious agents and risk of AD comprehensively. METHODS: Studies examining the associations between AD and infectious agents were identified through a systematic search of PubMed, Embase, and Cochrane library. A random-effects meta-analysis was conducted. Publication bias was explored using funnel plot. RESULTS: Fifty-one studies were included in the systematic review, of which forty-seven studies with 108,723 participants and 4,039 AD cases were eligible for meta-analysis. Evidence based on case control studies demonstrated that Chlamydia pneumoniae [odds ratio (OR): 4.39, 95% CI = 1.81-10.67; I2 = 68%)], Human herpes virus-6 (OR: 3.97, 95% CI = 2.04-7.75; I2 = 0%, Epstein-Barr virus (OR:1.45, 95% CI = 1.00-2.08; I2 = 0%), Herpes simplex virus-1 (OR:1.34, 95% CI = 1.02-1.75; I2 = 0%), and the Herpesviridae family (OR:1.41, 95% CI = 1.15-1.74; I2 = 12%) infection were associated with a higher risk of AD. No significant evidence of publication bias was found. CONCLUSION: These findings strengthened the evidence that infection may play an important role in AD. Additional research is required to determine whether treatment strategies targeting infectious diseases to prevent AD are viable in the future.

---

### PMID 15207442 — current stance: `inconclusive`

**Evidence span:** > Viral burden of herpes virus and cytomegalovirus was associated with cognitive impairment in home-dwelling elderly.

**Golden note:** Infectious burden + cognition in elderly — mixed across pathogens.

**Cognitive impairment and infectious burden in the elderly.**

*Archives of gerontology and geriatrics. Supplement*, 2004. Types: Clinical Trial; Journal Article; Randomized Controlled Trial

> Infectious agents have been suspected as contributing factors to dementia, especially in Alzheimer disease. We intended to test whether viral or bacterial seropositivity is associated with cognitive impairment among home-dwelling elderly. Viral burden (seropositivity for herpes simplex type 1 (HSVI), type 2 (HSV2), or cytomegalovirus (CMV), and bacterial burden (Chlamydia pneumoniae and Mycoplasma pneumoniae) were tested among 383 home-dwelling individuals with vascular disease (mainly coronary heart disease) in the ongoing DEBATE study (mean age 80 years). Mini-mental state examination (MMSE) and its changes were used to define cognitive impairment. At baseline, 0-1, 2, and 3 positive titers toward viruses were found in 48 (12.5 %), 229 (59.8 %), and 106 (27.7 %) individuals,respectively. MMSE points decreased with increasing viral burden (p = 0.03). At baseline,58 individuals (15.1 %) had cognitive impairment (MMSE < 24 points) which after adjustments was significantly associated with seropositivity for 3 viruses (risk ratio 2.5, 95%confidence interval 1.3 to 4.7). MMSE score decreased in 150 cases (43%) during 12-month follow-up. After adjustment for MMSE score at baseline and with 0-1 seropositivities as reference (1.0), the risk ratios were 1.8 (95 % confidence interval 0.9 to 3.6) and 2.3 (95% confidence interval 1.1 to 5.0) for 2 and 3 seropositivities, respectively. No significant associations were observed between bacterial burden and cognition. Viral burden of herpes virus and cytomegalovirus was associated with cognitive impairment in home-dwelling elderly. The association may offer a preventable cause of cognitive decline.

---

### PMID 33317741 — current stance: `supports`

**Evidence span:** > The pooled OR suggested that HSV-1 infection is a risk factor of AD: pooled OR 1.40 (95% CI: 1.13-1.75; I2 = 3%, P = 0.42).

**Golden note:** HSV-1/AD systematic review meta — significant association.

**The association between herpes simplex virus type 1 infection and Alzheimer's disease.**

*Journal of clinical neuroscience : official journal of the Neurosurgical Society of Australasia*, 2020. Types: Journal Article; Meta-Analysis; Systematic Review

> There is growing evidence demonstrating the relationship between herpes simplex virus type 1 (HSV-1) infection and Alzheimer's disease (AD). We searched PubMed, Embase, and Cochrane databases for relevant articles. The Newcastle-Ottawa Scale (NOS) was used to evaluate the qualities of these studies. Pooled odds ratios (ORs) with 95% confidence intervals (CIs) were calculated using random-effects models. We also performed subgroup analyses stratified by apolipoprotein ε4 (APOE ε4), NOS score, and the method of confirming AD. A total of 21 studies between 1990 and 2020 were identified. The pooled OR suggested that HSV-1 infection is a risk factor of AD: pooled OR 1.40 (95% CI: 1.13-1.75; I2 = 3%, P = 0.42). In the subgroup analyses, the pooled ORs of HSV-1 infection associated with AD were 0.75 (95% CI: 0.24-2.37) among the APOE ε4-positive individuals; 0.85 (95% CI: 0.61-1.17) among the APOE ε4-negative individuals; 1.51 (95% CI: 1.10-2.06) in the high NOS score studies; 1.23 (95% CI: 0.85-1.76) in the moderate NOS score studies; 1.47 (95% CI: 1.16-1.87) in the clinical diagnosis group, and 1.20 (95% CI: 0.77-1.87) in the autopsy group. Our up-to-date systematic review and meta-analysis suggest that HSV-1 infection is a risk factor of AD.

---

### PMID 30427305 — current stance: `inconclusive`

**Evidence span:** > Understanding how HHV-6A/B infection regulates autophagy could be of particular interest, as it has been recently shown that this virus may be involved in Alzheimer's disease in which a dysregulation of autophagy may also play a role.

**Golden note:** HHV-6 lytic infection autophagy mechanism — mechanistic only.

**Impact of HHV-6A and HHV-6B lytic infection on autophagy and endoplasmic reticulum stress.**

*The Journal of general virology*, 2018. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> Herpesviruses are known to manipulate autophagy to optimize their replication, counteract immune response and probably to promote tumourigenesis. This study explored, for the first time, the impact of human herpesvirus (HHV)-6 lytic infection on autophagy and demonstrated that HHV-6A and B (viruses sharing more than 80 % homology) differently affected this cellular process. Indeed, while HHV-6A (GS) infection of HSB2 cells promoted autophagy, HHV-6B (Z29) or the virus isolated from the serum of roseola infantum-affected patient-inhibited autophagy in Molt-3 cells or in PBMCs, respectively. Interestingly, the different behaviour of HHV-6A and B on the autophagic process was accompanied by different effects on endoplasmic reticulum stress, unfolded protein response and cell survival that was more strongly reduced by HHV-6B infection. We hypothesize that the ability to inhibit autophagy displayed by HHV-6B could be due to the fact that it contains gene homologues of those encoding for TRS1; the protein responsible for the block of autophagy by human cytomegalovirus. Understanding how HHV-6A/B infection regulates autophagy could be of particular interest, as it has been recently shown that this virus may be involved in Alzheimer's disease in which a dysregulation of autophagy may also play a role.

---

### PMID 37904465 — current stance: `supports`

**Evidence span:** > In the outcome of the incidence of HZV, the pooled analysis showed no statistically significant difference between the dementia group and the No dementia group (RR = 1.04% CI = 0.86-1.25, P = .70).

**Golden note:** Herpes Zoster meta — increased dementia risk.

**Herpes Zoster virus infection and the risk of developing dementia: A systematic review and meta-analysis.**

*Medicine*, 2023. Types: Meta-Analysis; Systematic Review; Journal Article

> BACKGROUND: Herpes Zoster, commonly known as shingles, is a viral infection that affects a significant portion of the adult population; however, its potential role in the onset or progression of neurodegenerative disorders like dementia remains unclear. METHODS: We searched the following databases: PubMed, Scopus, Cochrane library, and Web of Science. We included any randomized control trials and controlled observational studies as Cross-sectional, prospective, or retrospective cohort and case-control studies that investigated the prevalence of dementia in Herpes Zoster Virus (HZV)-infected patients and HZV-free control group or if the study investigated the prevalence of HZV in demented patients. Also, if the studies measured the levels of dementia biomarkers in patients with HZV compared with a healthy control group. RESULTS: After the complete screening, 9 studies were included in the meta-analysis. In the outcome of the incidence of HZV, the pooled analysis showed no statistically significant difference between the dementia group and the No dementia group (RR = 1.04% CI = 0.86-1.25, P = .70). In the outcome of incidences of dementia and Alzheimer's disease, the pooled analysis showed no statistically significant difference between the HZV group and the incidence of dementia (RR = 0.99, 95% CI = 0.92-1.08, P = .89), (RR = 3.74, 95% CI = 0.22-62.70, P = .36) respectively. In the outcome of incidences of Herpes Zoster ophthalmicus (HZO), the generic inverse variance showed a statistically significant association between patients who have HZO and increased incidence of dementia (RR = 6.26, 95% CI = 1.30-30.19, P = .02). CONCLUSION: Our study showed no significant association between HZV and the incidence of dementia or Alzheimer's disease, but it shows a significant association between HZO and the incidence of dementia. More multicenter studies are needed to establish the actual association between the HZV and dementia.

---

### PMID 38549138 — current stance: `supports`

**Evidence span:** > Despite significant research into the potential links between CMV infection and various neurological disorders, the direct cause-effect relationship is not fully understood and several gaps in knowledge persist.

**Golden note:** CMV-neurological systematic review — implicated.

**Association between cytomegalovirus infection and neurological disorders: A systematic review.**

*Reviews in medical virology*, 2024. Types: Meta-Analysis; Systematic Review; Journal Article

> Cytomegalovirus (CMV) belongs to the Herpesviridae family and is also known as human herpesvirus type 5. It is a common virus that usually doesn't cause any symptoms in healthy individuals. However, once infected, the virus remains in the host's body for life and can reactivate when the host's immune system weakens. This virus has been linked to several neurological disorders, including Alzheimer's disease, Parkinson's disease, Autism spectrum disorder, Huntington's disease (HD), ataxia, Bell's palsy (BP), and brain tumours, which can cause a wide range of symptoms and challenges for those affected. CMV may influence inflammation, contribute to brain tissue damage, and elevate the risk of moderate-to-severe dementia. Multiple studies suggest a potential association between CMV and ataxia in various conditions, including Guillain-Barré syndrome, chronic inflammatory demyelinating polyneuropathy, acute cerebellitis, etc. On the other hand, the evidence regarding CMV involvement in BP is conflicting, and also early indications of a link between CMV and HD were challenged by subsequent research disproving CMV's presence. This systematic review aims to comprehensively investigate any link between the pathogenesis of CMV and its potential role in neurological disorders and follows the preferred reporting items for systematic review and meta-analysis checklist. Despite significant research into the potential links between CMV infection and various neurological disorders, the direct cause-effect relationship is not fully understood and several gaps in knowledge persist. Therefore, continued research is necessary to gain a better understanding of the role of CMV in neurological disorders and potential treatment avenues.

---

### PMID 37639023 — current stance: `supports`

**Evidence span:** > VZV infection was associated with an increased risk of dementia (HR = 1.11, 95% CI: 1.02-1.21).

**Golden note:** VZV-dementia meta — positive association.

**The association between varicella zoster virus and dementia: a systematic review and meta-analysis of observational studies.**

*Neurological sciences : official journal of the Italian Neurological Society and of the Italian Society of Clinical Neurophysiology*, 2023. Types: Journal Article; Meta-Analysis; Systematic Review

> PURPOSE: The relationship between varicella zoster virus (VZV) infection and the risk of dementia has not been previously studied specifically. Therefore, this study sought to determine the relationship between studying VZV infection and dementia occurring in the general population by conducting an extensive meta-analysis of published cases. METHOD: A systematic literature search was conducted in seven online databases by October 31, 2022. Heterogeneity was tested by the I2 index. Pooled HR and 95% CI were used to estimate the effect of VZV infection on dementia. Sensitivity analyses and publication bias were also performed. RESULT: Nine studies involving 3,326,673 subjects were included. VZV infection was associated with an increased risk of dementia (HR = 1.11, 95% CI: 1.02-1.21). The risk of dementia was reduced in those who received antiviral therapy compared to those who did not (HR = 0.84, 95% CI: 0.71-0.99). In addition, VZV infection was found to be associated with an increased risk of developing dementia in the pooled results of the moderate quality study (HR = 1.81,95% CI: 1.27-2.59), and this association persisted when subgroup analyses were performed based on region (Asia: HR = 1.18,95% CI: 1.04-1.33). CONCLUSIONS: Our results suggest that VZV infection might increase the risk of developing dementia, but there is no clear mechanism about the true relationship, and since there is no effective treatment for dementia, and our results suggest that some populations can benefit from antiviral therapy, it is at least arguable that patients who develop VZV infection should be treated with appropriate antiviral medications.

---

### PMID 37801540 — current stance: `supports`

**Evidence span:** > The quantitative data derived from the studies in this report substantiate a relationship between infection with HSV-1 and AD.

**Golden note:** HSV-AD systematic review — positive associations.

**The Association Between Herpes Simplex Virus and Alzheimer's Disease: A Systematic Review.**

*Journal of drugs in dermatology : JDD*, 2023. Types: Systematic Review; Journal Article

> Alzheimer's disease (AD) is a significant public health concern, affecting more than 6 million Americans; and currently, there are no cure or effective treatment options. The underlying etiology and pathogenesis are not fully understood, presenting a barrier to therapy. A substantial amount of data exists associating infection with Herpes simplex virus 1 (HSV-1) and AD. This review of published studies highlights the epidemiological associations between HSV-1 and AD. A systematic search of PubMed, Embase, and Web of Science was conducted on January 6, 2022, using PRISMA guidelines. Articles that presented epidemiological data correlating HSV-1 with AD were included. Bibliographies were screened for additional relevant articles as well. After review, 21 studies were included: 2 review articles and 19 population-based studies including case control, cohort, and cross-sectional studies.&nbsp; The quantitative data derived from the studies in this report substantiate a relationship between infection with HSV-1 and AD. Based on these results, it may be of reasonable benefit to more consistently treat latent or active HSV-1 infection with anti-viral medications to potentially reduce the risk of AD. Furthermore, a prospective randomized controlled clinical trial could elucidate the benefit of anti-viral therapy to prevent or limit AD.J Drugs Dermatol. 2023;22(10):1046-1052&nbsp; &nbsp;&nbsp; doi:10.36849/JDD.6785.

---

### PMID 40898264 — current stance: `supports`

**Evidence span:** > The present review of the scientific literature generally shows little evidence of an association between herpesviruses and risk of dementia. However, the review shows evidence of an association between antiviral treatment and a decreased risk of dementia.

**Golden note:** Herpesviruses + antiviral treatment meta — antiviral protective.

**Herpesviruses, antiviral treatment, and the risk of dementia - systematic review and meta-analysis.**

*Alzheimer's research & therapy*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> INTRODUCTION: The aim of this systematic review and meta-analysis was to synthesize the evidence on the association between herpesviruses, antiviral treatment, and the risk of dementia. We also aimed to explore the impact of time between herpesviruses and dementia on the reported associations. METHODS: PubMed and Web of Science were searched along with reference lists of the included studies. We included studies that looked at clinical episodes or serology (IgG/IgM) of herpes simplex virus type 1/2 (HSV1/2) and/or varicella zoster virus (VZV), antiviral treatment and incident dementia (all-cause dementia, Alzheimer's disease, and vascular dementia). Study results were pooled with random effect meta-analyses. RESULTS: We included 32 studies. The pooled hazard ratio for all-cause dementia was 1.36 [95% CI: 1.01, 1.83] following a clinical episode of HSV1/2, and 1.12 [95% CI: 1.00, 1.25] following a clinical episode of VZV. The pooled estimate for all-cause dementia following antiviral treatment and VZV was 0.88 [95% CI: 0.81, 0.96]. CONCLUSIONS: The present review of the scientific literature generally shows little evidence of an association between herpesviruses and risk of dementia. However, the review shows evidence of an association between antiviral treatment and a decreased risk of dementia. Because of considerable heterogeneity, future investigations could advantageously target certain subgroups.

---

### PMID 41269248 — current stance: `supports`

**Evidence span:** > Vaccination against herpes zoster was associated with a reduced risk of any dementia (RR 0.76, 95% CI 0.69-0.83) and Alzheimer's disease (RR 0.53, 95% CI 0.44-0.64).

**Golden note:** Vaccinations + dementia meta — protective (HZ vaccine signal).

**Association between vaccinations and risk of dementia: a systematic review and meta-analysis.**

*Age and ageing*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> IMPORTANCE: Dementia is a highly prevalent issue in older people. Whilst the prevention of dementia is a public health priority, the role of vaccinations is still largely unexplored. OBJECTIVE: The aim of this systematic review is to evaluate whether common adult vaccinations are associated with a reduced risk of dementia. DATA SOURCES: PubMed, Embase and Web of Science were searched from inception to 1 January 2025. STUDY SELECTION: Observational studies comparing dementia and mild cognitive impairment incidence between vaccinated and unvaccinated adults aged ≥50 years. DATA EXTRACTION AND SYNTHESIS: Four reviewers independently extracted data and assessed study quality using the Newcastle-Ottawa Scale. Risk ratios (RRs) and 95% confidence intervals (CIs) were pooled using a random-effects model. MAIN OUTCOMES AND MEASURES: Incidence of dementia, including its subtypes. RESULTS: Twenty-one studies (n = 104 031 186 participants) were included. Vaccination against herpes zoster was associated with a reduced risk of any dementia (RR 0.76, 95% CI 0.69-0.83) and Alzheimer's disease (RR 0.53, 95% CI 0.44-0.64). Influenza vaccination was linked to a reduction in dementia risk (RR 0.87, 95% CI 0.77-0.99), as was pneumococcal vaccination (RR 0.64, 95% CI 0.47-0.87) for Alzheimer's disease. Tetanus, diphtheria, pertussis (Tdap) vaccination was also associated with a significant reduction for any dementia (RR 0.67, 95% CI 0.54-0.83). CONCLUSIONS AND RELEVANCE: Adult vaccinations, particularly against herpes zoster, influenza, pneumococcus and Tdap, are associated with a lower risk of dementia. Vaccination strategies should be incorporated into public health initiatives for dementia prevention. REGISTRATION: https://osf.io/x3d4f/.

---

### PMID 41405855 — current stance: `inconclusive`

**Evidence span:** > At 78 weeks, the LSM change in the 11-item ADAS-Cognitive Subscale score was 10.86 (95% CI, 8.80 to 12.91) in the valacyclovir group vs 6.92 (95% CI, 4.88 to 8.97) in the placebo group, indicating greater cognitive worsening with valacyclovir than placebo (between-group difference, 3.93 [95% CI, 1.03 to 6.83]; P = .01).

**Golden note:** VALAD valacyclovir RCT — early report, outcomes mixed.

**Valacyclovir Treatment of Early Symptomatic Alzheimer Disease: The VALAD Randomized Clinical Trial.**

*JAMA*, 2026. Types: Clinical Trial, Phase II; Journal Article; Multicenter Study; Randomized Controlled Trial

> IMPORTANCE: Neuroscientific, epidemiological, and electronic health record studies implicate herpes simplex virus (HSV) as potentially etiological for Alzheimer disease (AD). OBJECTIVE: To compare the efficacy and adverse effects of valacyclovir vs placebo in participants with early symptomatic AD and HSV seropositivity (HSV-1 or HSV-2). DESIGN, SETTING, AND PARTICIPANTS: This randomized clinical trial included adults with a clinical diagnosis of probable AD or a clinical diagnosis of mild cognitive impairment with positive biomarkers for AD, a positive serum antibody test (IgG or IgM) for HSV-1 or HSV-2, and a Mini-Mental State Examination score of 18 to 28. The trial was conducted at 3 US outpatient clinics specializing in memory disorders. Recruitment occurred from January 2018 to May 2022; the last follow-up occurred in September 2024. INTERVENTION: Either 4 g/d of valacyclovir (n = 60) or matching placebo (n = 60). MAIN OUTCOMES AND MEASURES: The primary outcome was least-squares mean (LSM) change at 78 weeks in the 11-item Alzheimer's Disease Assessment Scale Cognitive (ADAS-Cognitive) Subscale score (range, 0-70; higher scores indicate greater impairment). The secondary outcomes were LSM change in the Alzheimer's Disease Cooperative Study-Activities of Daily Living (ADCS-ADL) Scale score; LSM change in the 18F-florbetapir amyloid positron emission tomography (PET) standardized uptake value ratio (SUVR; higher scores indicate higher amyloid levels) for 6 brain regions (medial orbitofrontal, anterior cingulate, parietal lobe, posterior cingulate, temporal lobe, and precuneus); and LSM change in 18F-MK-6240 tau PET medial temporal SUVR (higher scores indicate higher tau levels) for 4 brain regions (amygdala, hippocampus, entorhinal, and parahippocampus). The frequency of adverse events was the safety outcome. RESULTS: Of the 120 participants (mean age, 71.4 [SD, 8.6] years; 55% were female), 93 (77.5%) completed the trial. At 78 weeks, the LSM change in the 11-item ADAS-Cognitive Subscale score was 10.86 (95% CI, 8.80 to 12.91) in the valacyclovir group vs 6.92 (95% CI, 4.88 to 8.97) in the placebo group, indicating greater cognitive worsening with valacyclovir than placebo (between-group difference, 3.93 [95% CI, 1.03 to 6.83]; P = .01). The LSM change in the ADCS-ADL Scale score at 78 weeks was -13.78 (95% CI, -17.00 to -10.56) in the valacyclovir group vs -10.16 (95% CI, -13.37 to -6.96) in the placebo group (between-group difference, -3.62 [95% CI, -8.16 to 0.93]). At 78 weeks, the LSM change in the 18F-florbetapir amyloid PET SUVR was 0.03 (95% CI, -0.04 to 0.10) in the valacyclovir group vs 0.01 (95% CI, -0.06 to 0.08) in the placebo group (between-group difference, 0.02 [95% CI, -0.08 to 0.12]). The LSM change in the 18F-MK-6240 tau PET medial temporal SUVR at 78 weeks was 0.07 (95% CI, -0.06 to 0.19) in the valacyclovir group vs -0.04 (95% CI, -0.15 to 0.07) in the placebo group (between-group difference, 0.11 [95% CI, -0.06 to 0.28]). The most common adverse events were elevated serum creatinine level (5 participants [8.3%] in the valacyclovir group vs 2 participants [3.3%] in the placebo group) and COVID-19 infection (3 [5%] vs 2 [3.3%], respectively). CONCLUSIONS AND RELEVANCE: Valacyclovir was not efficacious with cognitive worsening for the primary outcome and it is not recommended to treat individuals with early symptomatic AD and HSV seropositivity. TRIAL REGISTRATION: ClinicalTrials.gov Identifier: NCT03282916.

---

### PMID 40442743 — current stance: `supports`

**Evidence span:** > AD patients infected with HSV-1 or CMV demonstrated distinct alterations in inflammatory, oxidative stress, antioxidant profiles, and apoptosis markers, which may have beneficial implications for circulatory biomarkers and potentially cognitive outcomes in AD.

**Golden note:** HSV-1/CMV coinfection — oxidative stress mechanisms in AD.

**Oxidative stress, inflammation, and apoptosis in Alzheimer's disease associated with HSV-1 and CMV coinfection.**

*Virology journal*, 2025. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Oxidative stress, inflammation, and apoptosis have been reported to influence cognitive function in patients with Alzheimer's disease (AD), particularly those infected with herpes simplex virus type 1 (HSV-1) or cytomegalovirus (CMV). This study aimed to evaluate the effects of viral infection on oxidative stress markers associated with these pathways in AD patients. A total of 100 adults with mild-to-moderate AD were randomly assigned to a double-blind, placebo-controlled clinical trial and categorized into three groups: AD (uninfected), AD with HSV-1, and AD with CMV. The primary outcomes included changes in serum inflammatory markers (IL-1β and TNF-α), blood antioxidant and oxidative stress markers-glutathione peroxidase (GPx), superoxide dismutase (SOD), malondialdehyde (MDA), reactive oxygen species (ROS), and total antioxidant capacity (TAC), as well as the expression levels of apoptosis-related proteins (BAX and BCL-2). Results showed that, compared to the control group, the AD group exhibited significant alterations in inflammatory and oxidative stress markers. CMV infection led to increased antioxidant enzyme activity and decreased serum inflammatory markers relative to the uninfected AD group. However, there were significant differences in ratio BAX/BCL-2 protein expression between the CMV and HSV-1 groups when compared to the AD group. In conclusion, AD patients infected with HSV-1 or CMV demonstrated distinct alterations in inflammatory, oxidative stress, antioxidant profiles, and apoptosis markers, which may have beneficial implications for circulatory biomarkers and potentially cognitive outcomes in AD.

---

### PMID 40551502 — current stance: `supports`

**Evidence span:** > Pooled analysis of adjusted HRs indicated that HZ vaccination could reduce dementia risk by 29% (HR = 0.71, 95% CI: 0.66-0.76, I2 = 97.15%).

**Golden note:** HZ vaccination meta — reduced dementia risk.

**The association between herpes zoster vaccination and the decreased risk of dementia: A systematic review and meta-analysis of cohort studies.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> BackgroundHerpes zoster (HZ) infection may increase the risk of dementia, that causes a heavy socioeconomic burden. However, the epidemiological evidence between HZ vaccination and the risk of dementia remains inconclusive.ObjectiveThis meta-analysis was conducted to investigate the effect of HZ vaccination on the onset of dementia.MethodsWe searched PubMed, EMBASE, Web of Science, Science Direct, and Scopus for cohort studies assessing the association between HZ vaccination and dementia risk up to 20th January 2025. Hazard ratios (HRs) with 95% confidence intervals (CIs) were pooled adopting a random-effect model.ResultsFour eligible studies were included in the systematic review and five retrospective cohort studies in the meta-analysis. Among 14,493,383 dementia-free participants at baseline, 427,309 dementia cases occurred during 36-95 months of follow-up. All studies were of high quality. Pooled analysis of adjusted HRs indicated that HZ vaccination could reduce dementia risk by 29% (HR = 0.71, 95% CI: 0.66-0.76, I2 = 97.15%). Subgroup analyses revealed heterogeneity linked to definitions of dementia, exposure measurements, vaccination doses, deprivation index, and region. The results were stable in the sensitivity analyses, and no publication bias was found.ConclusionsHZ vaccination was notably related to a reduced risk of dementia. More mechanistic studies and epidemiological studies are warranted.

---

### PMID 41073371 — current stance: `inconclusive`

**Evidence span:** > The analysis demonstrated that infections with cytomegalovirus (CMV) (odds ratio [OR] = 1.41; 95% confidence interval [CI]: 1.03, 1.93), severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) (OR = 1.88; 95% CI: 1.53, 2.32), hepatitis C virus (HCV) (OR = 1.39; 95% CI: 1.14, 1.69), and human herpesvirus (HHV) (OR = 1.24; 95% CI: 1.02, 1.51) were associated with an increased risk of AD.

**Golden note:** Viral infections-neurodegenerative meta — 'inconclusive'.

**Viral infections and the risk of neurodegenerative diseases: a comprehensive meta-analysis and systematic review.**

*Translational psychiatry*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Viral infections have been implicated in the pathogenesis of neurodegenerative diseases (NDs); however, evidence linking specific viruses to Alzheimer's disease (AD), Parkinson's disease (PD), and amyotrophic lateral sclerosis (ALS) remains inconclusive. This study conducted a meta-analysis and systematic review to investigate these associations. METHODS: Thorough searches were conducted across Embase, PubMed, Cochrane Library, Web of Science and Scopus until May 18, 2025, to identify observational studies investigating the relationship between viral infections and the risk of NDs, including AD, PD, and ALS. Meta-analyses were executed using a random-effects model with Stata MP18.0. RESULTS: A total of 34,417 articles were identified, of which 73 met the eligibility criteria for inclusion in the meta-analysis, and 48 were included in the systematic review. The analysis demonstrated that infections with cytomegalovirus (CMV) (odds ratio [OR] = 1.41; 95% confidence interval [CI]: 1.03, 1.93), severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) (OR = 1.88; 95% CI: 1.53, 2.32), hepatitis C virus (HCV) (OR = 1.39; 95% CI: 1.14, 1.69), and human herpesvirus (HHV) (OR = 1.24; 95% CI: 1.02, 1.51) were associated with an increased risk of AD. Regarding PD, infections with hepatitis B virus (HBV) (OR = 1.18; 95% CI: 1.04, 1.35) and HCV (OR = 1.29; 95% CI: 1.18, 1.41) were identified as risk factors. Conversely, no significant correlation was found between any viral infection and the risk of ALS. CONCLUSION: This meta-analysis supports the role of select viral infections in AD and PD pathogenesis. However, no association was found between viral infections and ALS, warranting further large, multicenter, and longitudinal studies to elucidate mechanisms and confirm causality.

---

### PMID 40140230 — current stance: `supports`

**Evidence span:** > The results of the meta-analysis indicated that HSV-1 infection is a risk factor for AD (OR = 1.39, 95% CI = (1.14-1.69), P < 0.05)).

**Golden note:** Herpesviruses-AD case-control meta — positive association.

**Association between herpesviruses and alzheimer's disease: a meta-analysis based on case-control studies.**

*Molecular and cellular biochemistry*, 2025. Types: Journal Article; Meta-Analysis

> Herpesviruses infection has been found to be implicated in the etiology of Alzheimer's disease (AD). However, the results remain controversial. This systematic meta-analysis was aimed to evaluate the relationship between Herpesviruses infection and the risk of developing AD. Relevant literature was searched from five databases, including CNKI, PubMed, Web of Science, Embase, and Cochrane Library, to obtain case-control studies (published between the date of database establishment and February 2025; no language restrictions) that compared the Herpesviruses positivity in AD patients and healthy controls. Among all existing studies, there are more abundant published case-control studies on the relationship between HSV-1, HCMV and Alzheimer's disease. Therefore, we chose these two viruses to further explore their association with Alzheimer's disease. The quality of the included studies was evaluated by the NOS scale. The Review Manager 5.3 software was used to calculate the odds ratio (OR) and 95% confidence interval (95% CI) for meta-analysis. Publication bias was investigated using the funnel plots, Begg's and Egger's publication bias plots. Twenty-one eligible studies were included to investigate the association between HSV-1 and AD. The results of the meta-analysis indicated that HSV-1 infection is a risk factor for AD (OR = 1.39, 95% CI = (1.14-1.69), P < 0.05)). In the subgroup analysis, the pooled ORs of HSV-1 infection associated with AD were 1.28 (95% CI: 0.74-2.22) in literature prior to 2010;1.44 (95% CI: 1.14-1.82) in literature after 2010; 1.27(95% CI: 1.01-1.60) in studies from Europe; 1.22(95% CI: 0.66-2.27) in studies from North America;1.89 (95% CI: 1.19-3.02) in studies from Asia; 1.38 (95% CI: 1.10-1.74) in the clinical diagnosis group; 1.52 (95% CI: 0.84-2.74) in the autopsy group. The pooled OR of APOE4 positivity and AD risk was 5.51 (95% CI: 4.33-7.01). The association between HCMV and AD was analyzed in seven studies. The pooled result showed that HCMV infection is not a risk factor for AD (OR = 0.83, 95% CI = 0.63-1.09). Our latest meta-analysis suggests that HSV-1 infection is a risk factor for the risk of AD. Therefore, anti-HSV-1 infection can serve as a potential therapeutic strategy for control of AD incidence. There is insufficient evidence to support association between HCMV and AD.

---

### PMID 41490027 — current stance: `supports`

**Evidence span:** > Meta-analysis showed: (1) herpes zoster patients had significantly higher AD risk (RR = 1.12, 95% CI: 1.01-1.24, p = 0.04); (2) patients receiving antiviral treatment had lower AD risk (RR = 0.55, 95% CI: 0.37-0.82, p = 0.003); (3) vaccinated individuals had lower AD risk (RR = 0.72, 95% CI: 0.68-0.78, p < 0.0001).

**Golden note:** VZV-AD comprehensive meta — implicates VZV.

**Association between varicella-zoster virus and Alzheimer's disease: A systematic review and meta-analysis of comprehensive evidence from infection, treatment to prevention.**

*Journal of Alzheimer's disease : JAD*, 2026. Types: Journal Article; Systematic Review; Meta-Analysis; Review

> BackgroundThe association between varicella-zoster virus (VZV) infection and Alzheimer's disease (AD) risk has shown inconsistent results. Given difficulties in early diagnosis and limited therapeutic options for AD, identifying modifiable risk factors is significant for prevention.ObjectiveTo systematically evaluate the impact of VZV infection on AD risk and explore protective effects of antiviral treatment and vaccination.MethodsWe searched PubMed and Web of Science databases up to April 2025. The Newcastle-Ottawa Scale assessed study quality. Random-effects models were used for meta-analysis using risk ratios (RR) as the primary effect measure, with sensitivity and subgroup analyses conducted.ResultsTwenty-one studies were included. Meta-analysis showed: (1) herpes zoster patients had significantly higher AD risk (RR = 1.12, 95% CI: 1.01-1.24, p = 0.04); (2) patients receiving antiviral treatment had lower AD risk (RR = 0.55, 95% CI: 0.37-0.82, p = 0.003); (3) vaccinated individuals had lower AD risk (RR = 0.72, 95% CI: 0.68-0.78, p < 0.0001). The strongest association occurred in the >70 years age group, demonstrating age as an important effect modifier.ConclusionsThis meta-analysis provides systematic evidence supporting that VZV infection increases AD risk while confirming protective effects of antiviral treatment and vaccination. These findings support including herpes zoster vaccination in preventive healthcare for elderly populations.

---

### PMID 41467972 — current stance: `supports`

**Evidence span:** > To demonstrate the effects of anti-herpetic medications in various clinical scenarios, the meta-analysis compared: diagnosed and treated versus diagnosed but untreated (aHR=0.77, 95% CI: 0.67-0.89); treated versus untreated regardless of diagnosis (aHR=0.90, 95% CI: 0.87-0.94); and diagnosed and treated versus neither diagnosed nor treated (aHR=0.87, 95% CI: 0.78-0.97).

**Golden note:** Anti-herpetic treatment meta — reduces dementia risk.

**Anti-herpetic treatment reduces dementia risk: A systematic review and meta-analysis.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis; Review

> BackgroundHuman herpesvirus (HHV) infections, particularly for herpes simplex virus (HSV) and varicella-zoster virus (VZV), may increase dementia risk, yet the protective effects of anti-herpetic medications remained unclear.ObjectiveThis systematic review and meta-analysis of observational studies aimed to examine the association between anti-herpetic medications and dementia, focusing on HSV or VZV-related infections.MethodsThis study followed PRISMA guidelines (CRD42022368318). Cohort or nested case-control studies published from databases' inception to December 2024 were systematically searched in PubMed, MEDLINE, Embase, Cochrane Library, PsycINFO, and Web of Science. Eligible studies evaluated anti-herpetic medications (e.g., acyclovir, famciclovir, ganciclovir, valacyclovir, valganciclovir) and dementia risk in non-demented adults aged ≥50. Pooled adjusted hazard ratios (aHR) and 95% confidence intervals (CIs) were analyzed using random-effects models. Subgroup and meta-regression analyses were performed to explore potential sources of heterogeneity and effect modifiers.ResultsFourteen cohort studies involving more than 10 million older adults were included. To demonstrate the effects of anti-herpetic medications in various clinical scenarios, the meta-analysis compared: diagnosed and treated versus diagnosed but untreated (aHR=0.77, 95% CI: 0.67-0.89); treated versus untreated regardless of diagnosis (aHR=0.90, 95% CI: 0.87-0.94); and diagnosed and treated versus neither diagnosed nor treated (aHR=0.87, 95% CI: 0.78-0.97). Subgroup analysis and meta-regression identified infection severity as a significant modifier (p < 0.0001), explaining 89.01% of heterogeneity.ConclusionsThis systematic review and meta-analysis reveals notable protective effect of anti-herpetic medication usage on dementia, and the effect is especially pronounced in patients with severe alpha herpesvirus infections.

---

### PMID 41275158 — current stance: `inconclusive`

**Evidence span:** > The pooled analysis revealed a significant association between HHV-6 infection and increased risk of Alzheimer's [OR = 1.81, 95% CI: 1.16-2.84, p = 0.009], with moderate heterogeneity (I² = 60%).

**Golden note:** HHV-6/AD meta — inconsistent reports.

**Human herpesvirus 6 (HHV-6) infection and risk of Alzheimer's disease: a systematic review and meta-analysis.**

*BMC neurology*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Alzheimer's disease (AD) is the most common form of dementia worldwide. Human Herpesvirus 6 (HHV-6), a neurotropic virus capable of establishing lifelong latency in the CNS, has been suggested as a potential risk factor in the pathogenesis of AD. However, studies investigating this association have reported inconsistent findings. This systematic review and meta-analysis aimed to explore this association further and shed light on the matter. OBJECTIVE: This study aimed to systematically review and meta-analyze existing literature to assess the association between HHV-6 infection and the risk of Alzheimer's disease. METHODS: A comprehensive search of MEDLINE, Web of Science, EMBASE, and grey literature was conducted following PRISMA guidelines. Case-control studies that assessed the presence of HHV-6 in patients with Alzheimer's disease were included. The quality of studies was assessed using the Newcastle-Ottawa Scale (NOS), and meta-analysis was performed using RevMan 5.3 and STATA 17.0. Subgroup and sensitivity analyses were conducted to assess heterogeneity and robustness of the results. Publication bias was evaluated using funnel plots, trim-and-fill analysis, and Begg's test. RESULTS: Eight case-control studies comprising 1,507 participants were included. The pooled analysis revealed a significant association between HHV-6 infection and increased risk of Alzheimer's [OR = 1.81, 95% CI: 1.16-2.84, p = 0.009], with moderate heterogeneity (I² = 60%). Sensitivity analysis excluding one outlier strengthened the association [OR = 2.78, 95% CI: 1.65-4.70] and eliminated heterogeneity (I² = 0%). Subgroup analyses demonstrated stronger associations in studies using PCR detection [OR = 2.20, 95% CI: 1.22-3.98] and brain tissue samples [OR = 2.49, 95% CI: 1.22-5.11], whereas serological and blood-based studies yielded weaker, non-significant associations. Publication bias was not detected. CONCLUSIONS: This meta-analysis suggests that HHV-6 infection is significantly associated with an increased risk of Alzheimer's disease. Nevertheless, the exact causal mechanisms remain unclear. Further longitudinal and mechanistic studies are needed to better understand the role of HHV-6 in Alzheimer's pathogenesis and to evaluate potential antiviral options for preventive or therapeutic strategies.

---

### PMID 41953111 — current stance: `supports`

**Evidence span:** > Overall, the available evidence indicates no clear association between HSV-2 and Alzheimer's disease and only one of the two meta-analytic methods shows evidence of a potential relationship with all-cause dementia.

**Golden note:** HSV-2/dementia meta — positive association.

**Herpes simplex virus 2 and dementia risk: a systematic review and meta-analysis.**

*Frontiers in dementia*, 2026. Types: Journal Article; Systematic Review

> INTRODUCTION: Several potentially modifiable risk factors for dementia have been identified, including infectious diseases. Among the infectious diseases potentially associated with dementia is herpes simplex virus type-2 (HSV-2). METHODS: To better characterize the association between HSV-2 and dementia, we conducted a meta-analysis of published peer-reviewed studies reporting HSV-2 exposure and dementia outcomes. RESULTS: Of 626 identified primary studies, eight met our inclusion criteria, with one of these excluded due to overlapping data with another study, yielding seven independent studies (total N = 751,156). Meta-analyses found no significant association between HSV-2 infection and Alzheimer's disease (pooled odds ratios ≈ 1.1, 95% confidence intervals included the null across all methods). Similarly, when pooling odds ratios across studies examining all-cause dementia, results were non-significant (pooled odds ratios ≈ 1.2, 95% confidence intervals included 1). In contrast, pooled hazard ratios from three studies for all-cause dementia suggested a possible increased risk among individuals with HSV-2 (DerSimonian and Laird pooled hazard ratio = 1.37, 95% CI: 1.00-1.89; Hartung-Knapp-Sidik-Jonkman pooled hazard ratio = 1.35, 95% CI: 0.58-3.14), driven primarily by two significant studies. DISCUSSION: Overall, the available evidence indicates no clear association between HSV-2 and Alzheimer's disease and only one of the two meta-analytic methods shows evidence of a potential relationship with all-cause dementia. These findings support continued investigation into the association between HSV-2 and dementia.

---

### PMID 40934136 — current stance: `supports`

**Evidence span:** > The findings indicated a 32% higher likelihood of AD in individuals with HSV infection in case-control studies (OR = 1.32; 95% CI: 1.12, 1.55; I2 = 22.7%) and a 20% increased risk in cohort studies (HR = 1.20; 95% CI: 1.10, 1.31; I2 = 11.0%).

**Golden note:** HSV-AD systematic review meta — relationship implicated.

**Herpes Simplex Virus Infection and Risk of Alzheimer's Disease: A Systematic Review and Meta-Analysis.**

*Neuroepidemiology*, 2025. Types: Journal Article; Systematic Review

> INTRODUCTION: The relationship between herpes simplex virus (HSV) infection and the risk of Alzheimer's disease (AD) remains unclear. METHODS: A systematic review and meta-analysis were conducted to investigate this potential association. Observational studies were sourced from PubMed, Embase, Web of Science, and the Cochrane Library up to July 31, 2024. The analysis utilized the generic inverse variance method with a random-effects model. Effect sizes were calculated as odds ratios (ORs) or hazard ratios (HRs) with corresponding 95% confidence intervals. RESULTS: A total of 26 original studies, encompassing 1,213,193 participants, were included in the meta-analysis. The findings indicated a 32% higher likelihood of AD in individuals with HSV infection in case-control studies (OR = 1.32; 95% CI: 1.12, 1.55; I2 = 22.7%) and a 20% increased risk in cohort studies (HR = 1.20; 95% CI: 1.10, 1.31; I2 = 11.0%). Specifically, HSV-1 infection was associated with 46% higher odds of AD (OR = 1.46; 95% CI: 1.14, 1.86; I2 = 3.1%). CONCLUSION: This meta-analysis demonstrates an association between HSV infection and increased risk of AD, particularly for HSV-1. Given the high global prevalence of HSV-1 and the heterogeneity of existing evidence, these findings should be regarded as hypothesis-generating, underscoring the need for rigorous, biomarker-informed studies to clarify causality, and identify susceptible subgroups.

---

### PMID 16595160 — current stance: `supports`

**Evidence span:** > These findings are consistent with the hypothesis that human genetic variants facilitating the access of HSV-1 to the brain might result in susceptibility to AD.

**Golden note:** TAP2 genotype + HSV-1 + APOE4 in AD — supports mechanistic hypothesis.

**A TAP2 genotype associated with Alzheimer's disease in APOE4 carriers.**

*Neurobiology of aging*, 2006. Types: Comparative Study; Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't

> Sporadic Alzheimer's disease (AD) appears to be the consequence of the interaction between combinations of genes and environmental factors. Binding with the transporter associated with antigen processing (TAP) is thought to be the main way in which herpes simplex virus type 1 (HSV-1) evades immune surveillance. Several TAP gene polymorphisms were examined and a TAP2 SNP (rs241448) associated with AD found in two independent case-control samples, especially in carriers of the APOE4 allele. These findings are consistent with the hypothesis that human genetic variants facilitating the access of HSV-1 to the brain might result in susceptibility to AD.

---

### PMID 29676229 — current stance: `supports`

**Evidence span:** > Our study demonstrated the role of viral etiology in AD pathogenesis by elucidating interaction of oxidative stress and inflammation causing candidate genes with common viruses along with the identification of potential AD drug candidates.

**Golden note:** Viral-induced oxidative/inflammatory response in AD pathogenesis — supports viral hypothesis.

**Viral Induced Oxidative and Inflammatory Response in Alzheimer's Disease Pathogenesis with Identification of Potential Drug Candidates: A Systematic Review using Systems Biology Approach.**

*Current neuropharmacology*, 2019. Types: Journal Article; Systematic Review

> Alzheimer's disease (AD) is genetically complex with multifactorial etiology. Here, we aim to identify the potential viral pathogens leading to aberrant inflammatory and oxidative stress response in AD along with potential drug candidates using systems biology approach. We retrieved protein interactions of amyloid precursor protein (APP) and tau protein (MAPT) from NCBI and genes for oxidative stress from NetAge, for inflammation from NetAge and InnateDB databases. Genes implicated in aging were retrieved from GenAge database and two GEO expression datasets. These genes were individually used to create protein-protein interaction network using STRING database (score≥0.7). The interactions of candidate genes with known viruses were mapped using virhostnet v2.0 database. Drug molecules targeting candidate genes were retrieved using the Drug- Gene Interaction Database (DGIdb). Data mining resulted in 2095 APP, 116 MAPT, 214 oxidative stress, 1269 inflammatory genes. After STRING PPIN analysis, 404 APP, 109 MAPT, 204 oxidative stress and 1014 inflammation related high confidence proteins were identified. The overlap among all datasets yielded eight common markers (AKT1, GSK3B, APP, APOE, EGFR, PIN1, CASP8 and SNCA). These genes showed association with hepatitis C virus (HCV), Epstein- Barr virus (EBV), human herpes virus 8 and Human papillomavirus (HPV). Further, screening of drugs targeting candidate genes, and possessing anti-inflammatory property, antiviral activity along with a suggested role in AD pathophysiology yielded 12 potential drug candidates. Our study demonstrated the role of viral etiology in AD pathogenesis by elucidating interaction of oxidative stress and inflammation causing candidate genes with common viruses along with the identification of potential AD drug candidates.

---

