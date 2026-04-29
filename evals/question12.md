# Q12: Do GLP-1 receptor agonists (semaglutide / liraglutide) reduce dementia incidence?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=23 PMIDs.

**Current S/C/I**: 17 / 1 / 5
**Proposed S/C/I**: 9 / 3 / 11
**Net flips**: 12 (heavy demotion of mechanism/biomarker/narrative papers
labeled `supports`; ELAD primary-missed lifted to contradicts)

The current corpus is unanimously enthusiastic on GLP-1 RAs (17/23
supports). The actual primary clinical evidence (RCT cognitive endpoints
in AD/MCI) is much weaker than the corpus suggests — the dedicated AD
RCTs (ELAD liraglutide, exenatide pilot, long-acting exenatide MCI) all
**missed primary cognitive endpoints**. The positive signal in the
corpus comes mainly from observational meta-analyses of T2D
populations using dementia incidence as outcome.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `41326666` | 2025 | **inconclusive → contradicts** | ELAD phase 2b, n=204 mild-mod AD. Verbatim: *"The primary outcome showed **no significant differences** in cerebral glucose metabolism (P = 0.14) between the two groups."* Adequately-designed multicenter RCT primary endpoint missed. ADAS-Exec sig in secondary but ADCS-ADL and CDR-SoB null. **Adequately-powered RCT primary endpoint missed**. |
| `38746639` | 2024 | **supports → contradicts** | "Clinical Evidence for GLP-1 RA in AD" SR. Verbatim: *"In two RCTs with amyloid-β and tau biomarker endpoints did not observe an end of treatment difference between the placebo and treated groups. In three RCTs with cognitive endpoints, **there was no end of treatment difference between placebo and treated groups**."* The SR explicitly finds no cognitive benefit. The conclusion's hedge about "potential metabolic and neuroprotective benefits" doesn't rescue null cognitive findings. |
| `40189519` | 2025 | **supports → contradicts** | NMA of 22 RCTs, n=138,282 for prophylactic effects on neurodegenerative diseases. Verbatim: *"**Neither GLP-1 receptor agonists nor other SGLT2 inhibitors showed significant preventive effects** for any of the investigated neurodegenerative conditions."* Only dapagliflozin showed sig effect, and only for Parkinson's. GLP-1 RAs explicitly null for AD prevention in this NMA. |
| `29235507` | 2017 | **supports → inconclusive** | Liraglutide brain glucose transfer biomarker, n=38, 6 mo. Reports T_max increase but **no clinical cognitive endpoint**. The abstract's strongest claim is "consistent with the claim that GLP-1 analog treatment restores glucose transport at the BBB" — that's a biomarker claim. Per strict bar, biomarker-only → `inconclusive`. |
| `30099030` | 2018 | **supports → inconclusive** | Liraglutide neural correlates fMRI, n=at-risk cognitively normal individuals, 12 wk. Reports DMN connectivity changes. Verbatim: *"There were no detectable cognitive differences between study groups after this duration of treatment."* Imaging biomarker only, no cognitive primary signal. |
| `30938196` | 2019 | **supports → inconclusive** | "GLP-1's role in neuroprotection" SR — predominantly preclinical/animal, with a mix of clinical findings. Conclusion verbatim: *"the number of clinical studies that investigate GLP-1 as a treatment is low and further clinical trials are needed."* Mechanism-heavy review. |
| `35054924` | 2022 | **supports → inconclusive** | "GLP-1a: Going beyond Traditional Use" — broad narrative review covering Parkinson's, depression, addiction, lipotoxicity, etc. Saffron-style breadth. Not specific clinical efficacy evidence for AD. |
| `37771725` | 2023 | **supports → inconclusive** | Preclinical AD models meta — 26 animal studies. Pure animal mechanism. Per strict bar, animal-only meta → `inconclusive`. |
| `25418147` | 2014 | **supports → inconclusive** | "GLP-1 mimetics: a new treatment for AD?" review. Verbatim from abstract: clinical trials in AD patients had *"recently started"* at time of writing. Mostly preclinical with future-tense clinical outlook. |
| `39358806` | 2024 | **supports → inconclusive** | EXSCEL post-hoc inflammatory protein analysis, n=3,973. Reports proteomic changes (FCN2, PAI-1, sVCAM-1). Biomarker substudy with no cognitive primary. Per strict bar, biomarker-only → `inconclusive`. |
| `39952607` | 2025 | **supports → inconclusive** | SGLT2 vs GLP-1 head-to-head, n=221,883 pairs. SGLT2 was *better* than GLP-1 for dementia (HR 0.92 favoring SGLT2). The question is "do GLP-1 RAs reduce dementia"; this study shows GLP-1 RAs are *worse than SGLT2*, not that they fail vs no-treatment. Comparator framing — same issue as Q3 metformin comparators. |
| `40017057` | 2025 | **inconclusive → supports** | Antidiabetic-cognition meta. Verbatim: *"Glucagon-like peptide-1 receptor agonists (GLP-1 RA) versus placebo reduced dementia risk by 53% in three RCTs (n = 15,820, RR = 0.47[0.25, 0.86]) and 27% in three case-control studies."* Significantly positive on GLP-1 RAs specifically in pooled RCTs. |

## Borderline (not flipped, but flagged for cross-question policy decisions)

- `41326666` (ELAD) — **policy (c) missed_primary_sig_secondary**. Strict bar →
  `contradicts` (adequately-powered RCT primary missed). Flagged because
  secondary ADAS-Exec was significant (P=0.01 unadjusted), so this also has
  a "split outcome" character. Flip stands; flagging for cross-question
  consistency with similar mixed-outcome RCTs.
- `39952607` (SGLT2 vs GLP-1 head-to-head) — **comparator_only**. Same
  policy issue as Q3 metformin-comparator papers: a head-to-head trial that
  shows GLP-1 inferior to a different active agent doesn't directly answer
  "do GLP-1 RAs reduce dementia vs no treatment." Flipped to inconclusive
  here as the strict-bar reading; flagging for cross-question consistency.
- `31518224` (exenatide pilot, n=21, early-terminated) — **underpowered_null**.
  Reads as null ("no differences or trends compared to placebo") but the
  authors explicitly disclaim drawing firm conclusions due to early
  termination. Strict bar would point toward `contradicts` if powered;
  staying `inconclusive` because underpowered.
- `37077141` (small meta, 5 RCTs, n=184) — **pilot_positive / pooled-small**.
  MD 2.16 is statistically significant in the pool, but n=184 across 5 RCTs
  is a thin evidence base. Keeping `supports` because the pooled effect is
  significant; flagging because a single Q4 exercise–like reanalysis with
  fewer trials would land here as inconclusive.

## Confirmed (no change)

- `39780249` (evoke/evoke+ design paper, results pending) — **inconclusive ✓**
- `36821780` (2023 newer GLDs meta — GLP-1 RA RR 0.72 sig for dementia) — **supports ✓**
- `37302139` (2023 antidiabetics NMA — GLP-1 RA OR 0.34 sig) — **supports ✓**
- `33080602` (antidiabetic SR including liraglutide) — **inconclusive ✓**
- `40193122` (cardioprotective glucose-lowering meta — GLP-1 RA OR 0.55 sig for dementia among 26 RCTs) — **supports ✓**
- `37231200` (GLP-1 RA neurological diabetes complications review — exenatide/dulaglutide/liraglutide improved general cognition) — **supports ✓**
- `39302577` (TriNetX retrospective T2D + GLP-1 — sig dementia/AD reduction) — **supports ✓** (defensible despite RD magnitudes being small)
- `38565814` (long-acting exenatide MCI proof-of-concept, n=32) — **contradicts ✓** (primary endpoint missed; gender × treatment interaction with women on exenatide getting *worse*)
- `39716328` (2024 NMA antidiabetics — GLP-1 RA OR 0.58 sig observational, RCT pooled null) — **supports ✓** (defensible; observational sig)

## Cross-cutting issues

- **Mechanism/biomarker overload**: 6+ of the 17 `supports` are
  mechanism, animal-model, biomarker, or narrative reviews — not
  primary efficacy evidence for the question. After demotion, the
  primary evidence base is much smaller.
- **Pivotal AD RCTs are negative**: `41326666` (ELAD liraglutide),
  `38565814` (exenatide MCI), and `31518224` (exenatide pilot) all
  failed primary cognitive endpoints. This is the dedicated-AD-trial
  signal.
- **Positive signal is observational**: The dementia-incidence positive
  pooled estimates (`36821780`, `37302139`, `40193122`, `40017057`)
  come from observational data in T2D populations, where confounding
  by indication is well-known.
- **`expected_consensus: "mostly positive"`** is partially supported
  by the observational evidence but contradicted by the pivotal AD
  RCTs. After flips: 9/3/11 — closer to "contested."

## Highest-confidence flips for this question

- `41326666` inconclusive → contradicts (ELAD primary endpoint missed)
- `38746639` supports → contradicts (SR explicitly: "no end of treatment difference")
- `40189519` supports → contradicts (NMA: "neither GLP-1 RA nor SGLT2 showed significant preventive effects")
- `29235507`, `30099030`, `39358806` supports → inconclusive (biomarker-only studies)
- `40017057` inconclusive → supports (RCT-pooled RR 0.47 sig)


---

## signal_types (annotation layer)

Optional pattern tags per pmid. Untagged = strong/canonical; tagged = some caveat.

- `41326666` — `missed_primary_sig_secondary` (ELAD: cerebral glucose primary P=0.14; ADAS-Exec secondary P=0.01)
- `38746639` — `hedged_meta` (SR cognitive null but conclusion hedges with "potential metabolic and neuroprotective benefits")
- `40189519` — none (clean NMA null on GLP-1 RAs for AD prevention)
- `29235507` — `biomarker_only` (BBB glucose transfer T_max only, no cognitive primary)
- `30099030` — `biomarker_only` (fMRI DMN connectivity; explicit no cognitive group difference)
- `30938196` — `preclinical_dominated`, `narrative_review` (SR but mostly preclinical mechanism)
- `35054924` — `narrative_review`, `broad_scope_review` (covers Parkinson's/depression/addiction/lipotoxicity, not AD-specific efficacy)
- `37771725` — `preclinical_dominated` (animal-only meta, 26 rodent studies)
- `25418147` — `preclinical_dominated`, `narrative_review` (2014; clinical trials "recently started" at writing)
- `39358806` — `biomarker_only` (EXSCEL post-hoc proteomics; no cognitive primary)
- `39952607` — `comparator_only` (SGLT2 vs GLP-1 head-to-head; no placebo arm)
- `40017057` — none (RCT-pooled RR 0.47 sig; canonical positive)
- `31518224` — `underpowered_null`, `pilot_positive` (early-terminated; null trend disclaimed by authors)
- `38565814` — `pilot_positive`, `subgroup_apoe_split` (proof-of-concept n=32; women on exenatide worsened — sex-subgroup interaction)
- `37077141` — `pilot_positive` (5 small RCTs, n=184 total; pooled sig but thin base)
- `39716328` — `split_outcome` (observational pooled sig OR 0.58; RCT pooled null — class signal differs by design)
- `33080602` — `hedged_meta` (concludes "no particular antidiabetic drug can currently be recommended")
- `39780249` — none (design paper, results pending; correctly inconclusive)
- `36821780` — none (clean observational meta, RR 0.72 sig)
- `37302139` — none (NMA, GLP-1 RA OR 0.34 sig)
- `40193122` — none (clean RCT meta on cardioprotective agents; GLP-1 OR 0.55 sig)
- `37231200` — `narrative_review` (SR but heterogeneous outcomes — stroke, MACE, cognition, neuropathy mixed)
- `39302577` — none (TriNetX retrospective; large n with sig RDs)

---

## Abstracts (n=23)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 29235507 — current stance: `supports`

**Evidence span:** > The GLP-1 analog treatment, compared to placebo, highly significantly raised the T max estimates of cerebral cortex from 0.72 to 1.1 umol/g/min, equal to T max estimates in healthy volunteers.

**Golden note:** GLP-1 analog in AD — improves blood-brain glucose transfer.

**Blood-Brain Glucose Transfer in Alzheimer's disease: Effect of GLP-1 Analog Treatment.**

*Scientific reports*, 2017. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> There are fewer than normal glucose transporters at the blood-brain barrier (BBB) in Alzheimer's disease (AD). When reduced expression of transporters aggravates the symptoms of AD, the transporters become a potential target of therapy. The incretin hormone GLP-1 prevents the decline of cerebral metabolic rate for glucose (CMRglc) in AD, and GLP-1 may serve to raise transporter numbers. We hypothesized that the GLP-1 analog liraglutide would prevent the decline of CMRglc in AD by raising blood-brain glucose transfer, depending on the duration of disease. We randomized 38 patients with AD to treatment with liraglutide (n = 18) or placebo (n = 20) for 6 months, and determined the blood-brain glucose transfer capacity (T max) in the two groups and a healthy age matched control group (n = 6). In both AD groups at baseline, T max estimates correlated inversely with the duration of AD, as did the estimates of CMRglc that in turn were positively correlated with cognition. The GLP-1 analog treatment, compared to placebo, highly significantly raised the T max estimates of cerebral cortex from 0.72 to 1.1 umol/g/min, equal to T max estimates in healthy volunteers. The result is consistent with the claim that GLP-1 analog treatment restores glucose transport at the BBB.

---

### PMID 31518224 — current stance: `inconclusive`

**Evidence span:** > Exenatide treatment produced no differences or trends compared to placebo for clinical and cognitive measures, MRI cortical thickness and volume, or biomarkers in CSF, plasma, and plasma neuronal extracellular vesicles (EV) except for a reduction of Aβ42 in EVs.

**Golden note:** Exenatide pilot in AD — no significant clinical benefit.

**A Pilot Study of Exenatide Actions in Alzheimer's Disease.**

*Current Alzheimer research*, 2019. Types: Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Intramural; Research Support, Non-U.S. Gov't

> BACKGROUND: Strong preclinical evidence suggests that exenatide, a glucagon-like peptide-1 (GLP- 1) receptor agonist used for treating type 2 diabetes, is neuroprotective and disease-modifying in Alzheimer's Disease (AD). OBJECTIVE: We performed an 18-month double-blind randomized placebo-controlled Phase II clinical trial to assess the safety and tolerability of exenatide and explore treatment responses for clinical, cognitive, and biomarker outcomes in early AD. METHOD: Eighteen participants with high probability AD based on cerebrospinal fluid (CSF) biomarkers completed the entire study prior to its early termination by the sponsor; partial outcomes were available for twentyone. RESULTS: Exenatide was safe and well-tolerated, showing an expectedly higher incidence of nausea and decreased appetite compared to placebo and decreasing glucose and GLP-1 during Oral Glucose Tolerance Tests. Exenatide treatment produced no differences or trends compared to placebo for clinical and cognitive measures, MRI cortical thickness and volume, or biomarkers in CSF, plasma, and plasma neuronal extracellular vesicles (EV) except for a reduction of Aβ42 in EVs. CONCLUSION: The positive finding of lower EV Aβ42 supports emerging evidence that plasma neuronal EVs provide an effective platform for demonstrating biomarker responses in clinical trials in AD. The study was underpowered due to early termination and therefore we cannot draw any firm conclusions. However, the analysis of secondary outcomes shows no trends in support of the hypothesis that exenatide is diseasemodifying in clinical AD, and lowering EV Aβ42 in and of itself may not improve cognitive outcomes in AD.

---

### PMID 30099030 — current stance: `supports`

**Evidence span:** > At time point 2, we observed significant improvement in intrinsic connectivity within the default mode network (DMN) in the active group relative to placebo. There were no detectable cognitive differences between study groups after this duration of treatment.

**Golden note:** Liraglutide in AD-risk persons — beneficial neural correlates.

**Neural correlates of liraglutide effects in persons at risk for Alzheimer's disease.**

*Behavioural brain research*, 2018. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> UNLABELLED: Insulin resistance (IR) is a metabolic state preceding development of type 2 diabetes (DM2), cardiovascular disease, and neurodegenerative disorders, including Alzheimer's Disease (AD). Liraglutide, a glucagon-like peptide-1 (GLP) agonist, is an insulin-sensitizing agent with neuroprotective properties, as shown in animal studies. The purpose of this double-blinded, placebo-controlled study was to examine the neural effects of administration of liraglutide in cognitively normal late middle-aged individuals with subjective cognitive complaints (half of subjects had family history of AD). Seed-based resting state connectivity using functional magnetic resonance imaging (fMRI) was conducted before and after 12 weeks of liraglutide treatment or placebo. Neuropsychological testing was conducted before and after treatment to determine whether there were any potential behavioral correlates to neural changes. RESULTS: At baseline (time point 1), higher fasting plasma glucose (FPG) was associated with decreased connectivity between bilateral hippocampal and anterior medial frontal structures. At time point 2, we observed significant improvement in intrinsic connectivity within the default mode network (DMN) in the active group relative to placebo. There were no detectable cognitive differences between study groups after this duration of treatment. To our knowledge, this is the first placebo-controlled study to report neural effects of liraglutide in a middle-aged population with subjective cognitive complaints. Larger and longer duration studies are warranted to determine whether liraglutide has neuroprotective benefits in individuals at risk for AD.

---

### PMID 30938196 — current stance: `supports`

**Evidence span:** > Based on the preclinical studies, GLP-1 modifying agents are promising targets for neuroprotection. On the other hand, the number of clinical studies that investigate GLP-1 as a treatment is low and further clinical trials are needed for a benchside to bedside translation of recent findings.

**Golden note:** GLP-1 neuroprotection systematic review.

**GLP-1's role in neuroprotection: a systematic review.**

*Brain injury*, 2019. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> Glucagon-like peptide 1 (GLP-1) is a target for treatment of diabetes; however, its function in the brain is not well studied. In this systematic review, we aimed to analyze the neuroprotective role of GLP-1 and its defined mechanisms. Methods: We searched 'Web of Science' and 'Pubmed' to identify relevant studies using GLP-1 as the keyword. Two hundred and eighty-nine clinical and preclinical studies have been included. Data have been presented by grouping neurodegenerative, neurovascular and specific cell culture models. Results: Recent literature shows that GLP-1 and its agonists, DPP-4 inhibitors and combined GLP-1/GIP molecules are effective in partially or fully reversing the effects of neurotoxic compounds, neurovascular complications of diabetes, neuropathological changes related with Alzheimer's disease, Parkinson's disease or vascular occlusion. Possible mechanisms that provide neuroprotection are enhancing the viability of the neurons and restoring neurite outgrowth by increased neurotrophic factors, increasing subventricular zone progenitor cells, decreasing apoptosis, decreasing the level of pro-inflammatory factors, and strengthening blood-brain barrier. Conclusion: Based on the preclinical studies, GLP-1 modifying agents are promising targets for neuroprotection. On the other hand, the number of clinical studies that investigate GLP-1 as a treatment is low and further clinical trials are needed for a benchside to bedside translation of recent findings.

---

### PMID 39780249 — current stance: `inconclusive`

**Evidence span:** > evoke and evoke+ are the first large-scale trials to investigate the disease-modifying potential of semaglutide in participants with early-stage symptomatic AD, including exploration of effects on AD biomarkers and neuroinflammation.

**Golden note:** evoke/evoke+ design paper — semaglutide phase 3, results pending.

**evoke and evoke+: design of two large-scale, double-blind, placebo-controlled, phase 3 studies evaluating efficacy, safety, and tolerability of semaglutide in early-stage symptomatic Alzheimer's disease.**

*Alzheimer's research & therapy*, 2025. Types: Journal Article; Randomized Controlled Trial; Clinical Trial, Phase III

> BACKGROUND: Disease-modifying therapies targeting the diverse pathophysiology of Alzheimer's disease (AD), including neuroinflammation, represent potentially important and novel approaches. The glucagon-like peptide-1 receptor agonist semaglutide is approved for the treatment of type 2 diabetes and obesity and has an established safety profile. Semaglutide may have a disease-modifying, neuroprotective effect in AD through multimodal mechanisms including neuroinflammatory, vascular, and other AD-related processes. Large randomized controlled trials are needed to assess the efficacy and safety of semaglutide in early-stage symptomatic AD. METHODS: evoke and evoke+ are randomized, double-blind, placebo-controlled phase 3 trials investigating the efficacy, safety, and tolerability of once-daily oral semaglutide versus placebo in early-stage symptomatic AD. Eligible participants were men or women aged 55-85 years with mild cognitive impairment or mild dementia due to AD with confirmed amyloid abnormalities (assessed by positron emission tomography or cerebrospinal fluid [CSF] analysis). After a maximum 12-week screening phase, an anticipated 1840 patients in each trial are randomized (1:1) to semaglutide or placebo for 156 weeks (104-week main treatment phase and 52-week extension). Randomized participants follow an 8-week dose escalation regimen (3 mg [weeks 0-4], 7 mg [weeks 4-8], and 14 mg [weeks 8-156]). The primary endpoint is the semaglutide-placebo difference on change from baseline to week 104 in the Clinical Dementia Rating - Sum of Boxes score. Analyses of plasma biomarkers, collected from all participants, and a CSF sub-study (planned n = 210) will explore semaglutide effects on AD biomarkers and neuroinflammation. RESULTS: Enrollment was undertaken between May 18, 2021, and September 8, 2023. Completion of the trials' main phase is expected in September 2025, and the 52-week extension (in which participants and investigators remain blinded to treatment assignment) will continue to October 2026. CONCLUSION: evoke and evoke+ are the first large-scale trials to investigate the disease-modifying potential of semaglutide in participants with early-stage symptomatic AD, including exploration of effects on AD biomarkers and neuroinflammation. The trials will provide data on the potential disease-modifying effects of semaglutide and will be important in evaluating its utility in the treatment of early-stage symptomatic AD. TRIAL REGISTRATION: Clinicaltrials.gov, NCT04777396 and NCT04777409. Date: 02/03/2021.

---

### PMID 35054924 — current stance: `supports`

**Evidence span:** > In Alzheimer's disease, GLP-1 analogs can improve the brain's glucose metabolism by improving glucose transport across the blood-brain barrier.

**Golden note:** GLP-1a beyond traditional use review — neuroprotective.

**GLP-1a: Going beyond Traditional Use.**

*International journal of molecular sciences*, 2022. Types: Journal Article; Systematic Review

> Glucagon-like peptide-1 (GLP-1) is a human incretin hormone derived from the proglucagon molecule. GLP-1 receptor agonists are frequently used to treat type 2 diabetes mellitus and obesity. However, the hormone affects the liver, pancreas, brain, fat cells, heart, and gastrointestinal tract. The objective of this study was to perform a systematic review on the use of GLP-1 other than in treating diabetes. PubMed, Cochrane, and Embase were searched, and the PRISMA guidelines were followed. Nineteen clinical studies were selected. The results showed that GLP-1 agonists can benefit defined off-medication motor scores in Parkinson's Disease and improve emotional well-being. In Alzheimer's disease, GLP-1 analogs can improve the brain's glucose metabolism by improving glucose transport across the blood-brain barrier. In depression, the analogs can improve quality of life and depression scales. GLP-1 analogs can also have a role in treating chemical dependency, inhibiting dopaminergic release in the brain's reward centers, decreasing withdrawal effects and relapses. These medications can also improve lipotoxicity by reducing visceral adiposity and decreasing liver fat deposition, reducing insulin resistance and the development of non-alcoholic fatty liver diseases. The adverse effects are primarily gastrointestinal. Therefore, GLP-1 analogs can benefit other conditions besides traditional diabetes and obesity uses.

---

### PMID 36821780 — current stance: `supports`

**Evidence span:** > Five studies found that users versus nonusers of GLP-1RAs were associated with a significant reduction in the risk of all-cause dementia (RR, 0.72; 95% CI, 0.54-0.97).

**Golden note:** Newer glucose-lowering drugs + dementia meta — GLP-1 RAs reduce risk.

**Newer glucose-lowering drugs and risk of dementia: A systematic review and meta-analysis of observational studies.**

*Journal of the American Geriatrics Society*, 2023. Types: Meta-Analysis; Systematic Review; Journal Article; Research Support, N.I.H., Extramural

> BACKGROUND: Preclinical studies have suggested potential beneficial effects of newer glucose-lowering drugs (GLDs) including dipeptidyl peptidase (DPP)-4 inhibitors, glucagon-like peptide-1 receptor agonists (GLP-1RAs), and sodium glucose co-transporter-2 (SGLT2) inhibitors, in protecting humans against cognitive decline and dementia. However, population studies aiming to demonstrate such cognitive benefits from newer GLDs have produced mixed findings. This meta-analysis aimed to evaluate the association between newer GLDs and risk of dementia in adults with type 2 diabetes (T2D). METHODS: Electronic databases were searched up to March 11, 2022 to include observational studies that examined the association between DPP-4 inhibitors, GLP-1RAs, and SGLT2 inhibitors and risk of dementia (including all-cause dementia, Alzheimer's disease [AD], and vascular dementia [VD]) in people with T2D. We conducted a random-effects meta-analysis to calculate the relative risk (RR) with 95% confidence interval (CI) for each class of newer GLD. RESULTS: Ten studies (from nine articles) involving 819,511 individuals with T2D were included. Three studies found that SGLT2 inhibitor users had a lower risk of all-cause dementia than non-SGLT2 inhibitor users (RR, 0.62; 95% CI, 0.39-0.97). Five studies found that users versus nonusers of GLP-1RAs were associated with a significant reduction in the risk of all-cause dementia (RR, 0.72; 95% CI, 0.54-0.97). However, a meta-analysis for AD and VD was unavailable for SGLT2 inhibitors and GLP-1RAs because only one study was included for each drug. In seven studies, users vs. nonusers of DPP-4 inhibitors were significantly associated with a decreased risk of all-cause dementia (RR, 0.84; 95% CI, 0.74-0.94) and VD (RR, 0.59; 95% CI, 0.47-0.75) but not AD (RR, 0.82; 95% CI, 0.63-1.08). CONCLUSION: Newer GLDs were associated with a decreased risk of all-cause dementia in people with T2D. Because of the observational nature and significant heterogeneity between studies, the results should be interpreted with caution. Further research is warranted to confirm our findings.

---

### PMID 37302139 — current stance: `supports`

**Evidence span:** > Compared with non-user, SGLT-2i (OR 0.41 [95% CI 0.22-0.76]), GLP-1RA (OR 0.34 [95% CI 0.14-0.85]), thiazolidinedione (OR 0.60 [95% CI 0.51-0.69]), and DPP-4i (OR 0.78 [95% CI 0.61-0.99]) users had a decreased risk of dementia, whereas sulfonylurea (OR 1.43 [95% CI 1.11-1.82]) increased dementia risk.

**Golden note:** Antidiabetics cognition meta in T2DM — GLP-1 RAs delay cognitive impairment.

**Comparison on cognitive outcomes of antidiabetic agents for type 2 diabetes: A systematic review and network meta-analysis.**

*Diabetes/metabolism research and reviews*, 2023. Types: Systematic Review; Journal Article; Research Support, Non-U.S. Gov't; Network Meta-Analysis

> We aimed to summarise current evidence on different antidiabetic drugs to delay cognitive impairment, including mild cognitive impairment, dementia, Alzheimer's disease (AD) and vascular dementia, among subjects with type 2 diabetes mellitus (T2DM). Medline, Cochrane and Embase databases were searched from inception to 31 July 2022. Two investigators independently reviewed and screened trials comparing antidiabetic drugs with no antidiabetic drugs, placebo, or other active antidiabetic drugs on cognitive outcomes in T2DM. Data were analysed using meta-analysis and network meta-analysis. Twenty-seven studies met the inclusion criteria, including 3 randomised controlled trials, 19 cohort studies and 5 case-control studies. Compared with non-user, SGLT-2i (OR 0.41 [95% CI 0.22-0.76]), GLP-1RA (OR 0.34 [95% CI 0.14-0.85]), thiazolidinedione (OR 0.60 [95% CI 0.51-0.69]), and DPP-4i (OR 0.78 [95% CI 0.61-0.99]) users had a decreased risk of dementia, whereas sulfonylurea (OR 1.43 [95% CI 1.11-1.82]) increased dementia risk. Network meta-analysis showed that SGLT-2i was most likely to rank best (SUCRA = 94.4%), GLP-1 RA second best (SUCRA = 92.7%), thiazolidinedione third best (SUCRA = 74.7%) and DPP-4i fourth best (SUCRA = 54.9%), while sulfonylurea second worst (SUCRA = 20.0%) for decreasing dementia outcomes, by synthesising evidence from direct and indirect comparisons of multiple intervention. Evidence suggests the effects of SGLT-2i ≈ GLP-1 RAs > thiazolidinedione > DPP-4i for delaying cognitive impairment, dementia and AD outcomes, whereas sulfonylurea was associated with the highest risk. These findings provide evidence for evaluating the optional treatment for clinical practice. PROSPERO REGISTRATION: Registration no. CRD42022347280.

---

### PMID 33080602 — current stance: `inconclusive`

**Evidence span:** > Intranasal insulin, pioglitazone, metformin, and liraglutide are promising drugs that could be useful in the treatment of AD. However, many questions remain to be answered in future studies, so no particular antidiabetic drug can currently be recommended to treat AD.

**Golden note:** Antidiabetic AD/MCI systematic review — modest, exploratory.

**Antidiabetic Drugs in Alzheimer's Disease and Mild Cognitive Impairment: A Systematic Review.**

*Dementia and geriatric cognitive disorders*, 2020. Types: Systematic Review; Journal Article

> INTRODUCTION: Considering that Alzheimer's disease (AD) and diabetes mellitus share pathophysiological features and AD remains with no cure, antidiabetic drugs like intranasal insulin, glitazones, metformin, and liraglutide are being tested as a potential treatment. OBJECTIVE: The aim of this systematic review was to assess the efficacy of antidiabetic drugs in patients with AD, mild cognitive impairment (MCI), or subjective cognitive complaints (SCCs). Cognition was studied as the primary outcome and modulation of AD biomarkers, and imaging was also assessed as a secondary outcome. METHODS: We conducted a search in the electronic databases PubMed/MEDLINE, EMBASE, and Scopus seeking clinical trials evaluating the effect on cognition of antidiabetic drugs in patients with AD, MCI, or SCCs. RESULTS: A total of 23 articles were found eligible. Intranasal regular insulin improved verbal memory in most studies, especially in apoE4- patients, but results in other cognitive domains were unclear. Detemir improved cognition after 2 months of treatment, but it did not after 4 months. Pioglitazone improved cognition in diabetic patients with AD or MCI in 3 clinical trials, but it is controversial as 2 other studies did not show effect. Metformin and liraglutide showed promising results, but further research is needed as just 2 clinical trials involved each of these drugs. Almost all drugs tested were shown to modulate AD biomarkers and imaging. CONCLUSIONS: Intranasal insulin, pioglitazone, metformin, and liraglutide are promising drugs that could be useful in the treatment of AD. However, many questions remain to be answered in future studies, so no particular antidiabetic drug can currently be recommended to treat AD.

---

### PMID 40193122 — current stance: `supports`

**Evidence span:** > Among drug classes, GLP-1RAs were associated with a statistically significant reduction in dementia (OR, 0.55 [95% CI, 0.35-0.86]), but not SGLT2is (OR, 1.20 [95% CI, 0.67-2.17]; P value for heterogeneity = .04).

**Golden note:** Cardioprotective glucose-lowering meta — GLP-1/SGLT2 reduce dementia.

**Cardioprotective Glucose-Lowering Agents and Dementia Risk: A Systematic Review and Meta-Analysis.**

*JAMA neurology*, 2025. Types: Journal Article; Meta-Analysis; Systematic Review

> IMPORTANCE: Although diabetes is a risk factor for dementia, the effect of glucose-lowering therapy for prevention of incident dementia is uncertain. OBJECTIVE: To determine whether cardioprotective glucose-lowering therapy (sodium-glucose cotransporter-2 inhibitors [SGLT2is], glucagon-like peptide-1 receptor agonists [GLP-1RAs], metformin, and pioglitazone), compared with controls, was associated with a reduction in risk of dementia or cognitive impairment, and among primary dementia subtypes. DATA SOURCES: The PubMed and Embase databases were searched for studies published from inception of the database to July 11, 2024. STUDY SELECTION: Randomized clinical trials comparing cardioprotective glucose-lowering therapy with controls that reported dementia or change in cognitive scores. Cardioprotective glucose-lowering therapies were defined as drug classes recommended by guidelines for reduction of cardiovascular events, based on evidence from phase III randomized clinical trials. Inclusion criteria were assessed independently and inconsistencies were resolved by consensus. DATA EXTRACTION AND SYNTHESIS: Data were screened and extracted independently by 2 authors adhering to the PRISMA guidelines in August 2024. Random-effects meta-analysis models were used to estimate a pooled treatment effect. MAIN OUTCOMES AND MEASURES: The primary outcome measure was dementia or cognitive impairment. The secondary outcomes were primary dementia subtypes, including vascular and Alzheimer dementia, and change in cognitive scores. RESULTS: Twenty-six randomized clinical trials were eligible for inclusion (N = 164 531 participants), of which 23 trials (n = 160 191 participants) reported the incidence of dementia or cognitive impairment, including 12 trials evaluating SGLT2is, 10 trials evaluating GLP-1RAs, and 1 trial evaluating pioglitazone (no trials of metformin were identified). The mean (SD) age of trial participants was 64.4 (3.5) years and 57 470 (34.9%) were women. Overall, cardioprotective glucose-lowering therapy was not significantly associated with a reduction in cognitive impairment or dementia (odds ratio [OR], 0.83 [95% CI, 0.60-1.14]). Among drug classes, GLP-1RAs were associated with a statistically significant reduction in dementia (OR, 0.55 [95% CI, 0.35-0.86]), but not SGLT2is (OR, 1.20 [95% CI, 0.67-2.17]; P value for heterogeneity = .04). CONCLUSIONS AND RELEVANCE: While cardioprotective glucose-lowering therapies were not associated with an overall reduction in all-cause dementia, this meta-analysis of randomized clinical trials found that glucose lowering with GLP-1RAs was associated with a statistically significant reduction in all-cause dementia.

---

### PMID 38746639 — current stance: `supports`

**Evidence span:** > Two RCTs with amyloid-β and tau biomarker endpoints did not observe an end of treatment difference between the placebo and treated groups. In three RCTs with cognitive endpoints, there was no end of treatment difference between placebo and treated groups.

**Golden note:** Clinical evidence GLP-1 RA in AD systematic review — favorable.

**Clinical Evidence for GLP-1 Receptor Agonists in Alzheimer's Disease: A Systematic Review.**

*Journal of Alzheimer's disease reports*, 2024. Types: Systematic Review; Journal Article

> BACKGROUND: Alzheimer's disease (AD) is the most common cause of dementia. While preclinical studies have shown benefits of glucagon-like peptide 1 receptor agonists (GLP-1 RA) in targeting core AD pathology, clinical studies are limited. OBJECTIVE: A systematic review was performed to evaluate GLP-1 RAs in AD for their potential to target core AD pathology and improve cognition. METHODS: Searches were conducted via three different databases (PubMed, Embase, and Cochrane Library). Search terms included Medical Subject Headings (MeSH) terms: 'glucagon-like peptide 1 receptor agonist' and 'Alzheimer's disease', as well as entry terms 'GLP-1 RA', 'AD', and three types of GLP-1 RA: 'liraglutide', 'exenatide', and 'lixisenatide'. RESULTS: A total of 1,444 studies were screened. Six articles that met criteria were included (four randomized control trials [RCTs] and two protocol studies). Two RCTs with amyloid-β and tau biomarker endpoints did not observe an end of treatment difference between the placebo and treated groups. In three RCTs with cognitive endpoints, there was no end of treatment difference between placebo and treated groups. GLP-1 RA showed metabolic benefits, such as lower body mass index and improved glucose levels on oral glucose tolerance tests in treated groups. GLP-1 RA may mitigate the decline in cerebral glucose metabolism and show enhanced blood-brain glucose transport capacity using 18F-FDG PET, however, more data is needed. CONCLUSIONS: GLP-1 RA therapy did not alter amyloid-β and tau biomarkers nor show improvements in cognition but showed potential metabolic and neuroprotective benefits.

---

### PMID 37771725 — current stance: `supports`

**Evidence span:** > The results showed that, in terms of behavioral tests, GLP-1 RAs could improve the learning and memory abilities of AD rodents; in terms of pathology, GLP-1 RAs could reduce Aβ deposition and phosphorylated tau levels in the brains of AD rodents.

**Golden note:** GLP-1 RAs in preclinical AD models meta — neuroprotective.

**Glucagon-like peptide 1 (GLP-1) receptor agonists in experimental Alzheimer's disease models: a systematic review and meta-analysis of preclinical studies.**

*Frontiers in pharmacology*, 2023. Types: Systematic Review; Journal Article

> Alzheimer's disease (AD) is a degenerative disease of the nervous system. Glucagon-like peptide-1 receptor agonists (GLP-1 RAs), a drug used to treat type 2 diabetes, have been shown to have neuroprotective effects. This systematic review and meta-analysis evaluated the effects and potential mechanisms of GLP-1 RAs in AD animal models. 26 studies were included by searching relevant studies from seven databases according to a predefined search strategy and inclusion criteria. Methodological quality was assessed using SYRCLE's risk of bias tool, and statistical analysis was performed using ReviewManger 5.3. The results showed that, in terms of behavioral tests, GLP-1 RAs could improve the learning and memory abilities of AD rodents; in terms of pathology, GLP-1 RAs could reduce Aβ deposition and phosphorylated tau levels in the brains of AD rodents. The therapeutic potential of GLP-1 RAs in AD involves a range of mechanisms that work synergistically to enhance the alleviation of various pathological manifestations associated with the condition. A total of five clinical trials were retrieved from ClinicalTrials.gov. More large-scale and high-quality preclinical trials should be conducted to more accurately assess the therapeutic effects of GLP-1 RAs on AD.

---

### PMID 37231200 — current stance: `supports`

**Evidence span:** > Exenatide, dulaglutide and liraglutide improved general cognition but no significant effect on diabetic peripheral neuropathy has been reported with GLP-1 RAs.

**Golden note:** GLP-1 RA + neurological complications of diabetes review — beneficial.

**Effects of GLP-1 receptor agonists on neurological complications of diabetes.**

*Reviews in endocrine & metabolic disorders*, 2023. Types: Systematic Review; Journal Article; Research Support, Non-U.S. Gov't

> Emerging evidence suggests that treatment with glucagon-like peptide-1 receptor agonists (GLP-1 RAs) could be an interesting treatment strategy to reduce neurological complications such as stroke, cognitive impairment, and peripheral neuropathy. We performed a systematic review to examine the evidence concerning the effects of GLP-1 RAs on neurological complications of diabetes. The databases used were Pubmed, Scopus and Cochrane. We selected clinical trials which analysed the effect of GLP-1 RAs on stroke, cognitive impairment, and peripheral neuropathy. We found a total of 19 studies: 8 studies include stroke or major cardiovascular events, 7 involve cognitive impairment and 4 include peripheral neuropathy. Semaglutide subcutaneous and dulaglutide reduced stroke cases. Liraglutide, albiglutide, oral semaglutide and efpeglenatide, were not shown to reduce the number of strokes but did reduce major cardiovascular events. Exenatide, dulaglutide and liraglutide improved general cognition but no significant effect on diabetic peripheral neuropathy has been reported with GLP-1 RAs. GLP-1 RAs are promising drugs that seem to be useful in the reduction of some neurological complications of diabetes. However, more studies are needed.

---

### PMID 39302577 — current stance: `supports`

**Evidence span:** > In the T2D cohorts, GLP-1RA treatment was associated with significantly lower incidences of several systemic and metabolic conditions as compared to those without GLP-1RA, specifically, dementia (Risk Difference (RD): -0.010, p < 0.001), AD (RD: -0.003, p < 0.001), PD (RD: -0.002, p < 0.001), and pancreatic cancer (RD: -0.003, p < 0.001).

**Golden note:** T2D/obesity + GLP-1 retrospective cohort — improves dementia/AD outcomes.

**Comparative outcomes of systemic diseases in people with type 2 diabetes, or obesity alone treated with and without GLP-1 receptor agonists: a retrospective cohort study from the Global Collaborative Network : Author list.**

*Journal of endocrinological investigation*, 2024. Types: Journal Article; Comparative Study

> BACKGROUND: Glucagon-like peptide-1 receptor agonists (GLP-1RAs) are increasingly used to manage type 2 diabetes (T2D) and obesity. Despite their recognized benefits in glycemic control and weight management, their impact on broader systemic has been less explored. OBJECTIVE: This study aimed to evaluate the impact of GLP-1RAs on a variety of systemic diseases in people with T2D or obesity. METHODS: We conducted a retrospective cohort study using data from the Global Collaborative Network, accessed through the TriNetX analytics platform. The study comprised two primary groups: individuals with T2D and those with obesity. Each group was further divided into subgroups based on whether they received GLP-1RA treatment or not. Data were analyzed over more than a 5-year follow-up period, comparing incidences of systemic diseases; systemic lupus erythematosus (SLE), systemic sclerosis (SS), rheumatoid arthritis (RA), ulcerative colitis (UC), crohn's disease (CD), alzheimer's disease (AD), parkinson's disease (PD), dementia, bronchial asthma (BA), osteoporosis, and several cancers. RESULTS: In the T2D cohorts, GLP-1RA treatment was associated with significantly lower incidences of several systemic and metabolic conditions as compared to those without GLP-1RA, specifically, dementia (Risk Difference (RD): -0.010, p < 0.001), AD (RD: -0.003, p < 0.001), PD (RD: -0.002, p < 0.001), and pancreatic cancer (RD: -0.003, p < 0.001). SLE and SS also saw statistically significant reductions, though the differences were minor in magnitude (RD: -0.001 and - 0.000 respectively, p < 0.001 for both). Conversely, BA a showed a slight increase in risk (RD: 0.002, p < 0.001). CONCLUSIONS: GLP-1RAs demonstrate potential benefits in reducing the risk of several systemic conditions in people with T2D or obesity. Further prospective studies are needed to confirm these effects fully and understand the mechanisms.

---

### PMID 39358806 — current stance: `supports`

**Evidence span:** > EQW affected FCN2 (Cohen's d -0.019), PAI-1 (Cohen's d -0.033), sVCAM-1 (Cohen's d 0.035) and a cytokine-cytokine cluster (Cohen's d 0.037) significantly compared with placebo.

**Golden note:** EXSCEL post-hoc — exenatide reduces AD-associated inflammation proteins.

**Inflammatory proteins associated with Alzheimer's disease reduced by a GLP1 receptor agonist: a post hoc analysis of the EXSCEL randomized placebo controlled trial.**

*Alzheimer's research & therapy*, 2024. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Glucagon-like peptide-1 receptor agonists are a viable option for the prevention of Alzheimer's disease (AD) but the mechanisms of this potential disease modifying action are unclear. We investigated the effects of once-weekly exenatide (EQW) on AD associated proteomic clusters. METHODS: The Exenatide Study of Cardiovascular Event Lowering study compared the cardiovascular effects of EQW 2 mg with placebo in 13,752 people with type 2 diabetes mellitus. 4,979 proteins were measured (Somascan V0.4) on baseline and 1-year plasma samples of 3,973 participants. C-reactive protein (CRP), ficolin-2 (FCN2), plasminogen activator inhibitor 1 (PAI-1), soluble vascular cell adhesion protein 1 (sVCAM1) and 4 protein clusters were tested in multivariable mixed models. RESULTS: EQW affected FCN2 (Cohen's d -0.019), PAI-1 (Cohen's d -0.033), sVCAM-1 (Cohen's d 0.035) and a cytokine-cytokine cluster (Cohen's d 0.037) significantly compared with placebo. These effects were sustained in individuals over the age of 65 but not in those under 65. CONCLUSIONS: EQW treatment was associated with significant change in inflammatory proteins associated with AD. TRIAL REGISTRATION: EXSCEL is registered on ClinicalTrials.gov: NCT01144338 on 10th of June 2010.

---

### PMID 38565814 — current stance: `contradicts`

**Evidence span:** > No significant between-group effects of exenatide on ADAS-Cog11 score (p = 0.17) were detected. A gender interaction with treatment was observed (p = 0.04), due to worsening of the ADAS-Cog11 score in women randomized to exenatide (p = 0.018).

**Golden note:** Long-acting exenatide in MCI proof-of-concept — did NOT prevent cognitive decline.

**Long-acting exenatide does not prevent cognitive decline in mild cognitive impairment: a proof-of-concept clinical trial.**

*Journal of endocrinological investigation*, 2024. Types: Journal Article; Randomized Controlled Trial

> PURPOSE: According to preclinical evidence, GLP-1 receptor may be an actionable target in neurodegenerative disorders, including Alzheimer's disease (AD). Previous clinical trials of GLP-1 receptor agonists were conducted in patients with early AD, yielding mixed results. The aim was to assess in a proof-of-concept study whether slow-release exenatide, a long-acting GLP-1 agonist, can benefit the cognitive performance of people with mild cognitive impairment (MCI). METHODS: Thirty-two (16 females) patients were randomized to either slow-release exenatide (n = 17; 2 mg s.c. once a week) or no treatment (n = 15) for 32 weeks. The primary endpoint was the change in ADAS-Cog11 cognitive test score at 32 weeks vs baseline. Secondary endpoints herein reported included additional cognitive tests and plasma readouts of GLP-1 receptor engagement. Statistical analysis was conducted by intention to treat. RESULTS: No significant between-group effects of exenatide on ADAS-Cog11 score (p = 0.17) were detected. A gender interaction with treatment was observed (p = 0.04), due to worsening of the ADAS-Cog11 score in women randomized to exenatide (p = 0.018), after correction for age, scholar level, dysglycemia, and ADAS-Cog score baseline value. Fasting plasma glucose (p = 0.02) and body weight (p = 0.03) decreased in patients randomized to exenatide. CONCLUSION: In patients with MCI, a 32-week trial with slow-release exenatide had no beneficial effect on cognitive performance. TRIAL REGISTRATION NUMBER: NCT03881371, registered on 21 July, 2016.

---

### PMID 39716328 — current stance: `supports`

**Evidence span:** > Compared with non-users, SGLT-2i (OR = 0.56, 95%CI, 0.45 to 0.69), glucagon-like peptide-1 receptor agonist (GLP-1RA) (OR = 0.58, 95%CI, 0.46 to 0.73), thiazolidinedione (TZD) (OR = 0.68, 95%CI, 0.57 to 0.81) and metformin (OR = 0.89, 95%CI, 0.80 to 0.99) treatments were all associated with reduced risk of dementia in patients with T2D.

**Golden note:** Antidiabetic agents + dementia network meta — GLP-1 RAs protective.

**Anti-diabetic agents and the risks of dementia in patients with type 2 diabetes: a systematic review and network meta-analysis of observational studies and randomized controlled trials.**

*Alzheimer's research & therapy*, 2024. Types: Journal Article; Systematic Review; Network Meta-Analysis; Research Support, Non-U.S. Gov't

> OBJECTIVE: To evaluate the association between anti-diabetic agents and the risks of dementia in patients with type 2 diabetes (T2D). METHODS: Literature retrieval was conducted in PubMed, Embase, the Cochrane Central Register of Controlled Trials and Clinicaltrial.gov between January 1995 and October 2024. Observational studies and randomized controlled trials (RCTs) in patients with T2D, which intercompared anti-diabetic agents or compared them with placebo, and reported the incidence of dementia were included. Conventional and network meta-analyses of these studies were implemented. Results were exhibited as the odds ratio (OR) or risk ratio (RR) with 95% confidence interval (CI). RESULTS: A total of 41 observational studies (3,307,483 participants) and 23 RCTs (155,443 participants) were included. In the network meta-analysis of observational studies, compared with non-users, sodium glucose cotransporter-2 inhibitor (SGLT-2i) (OR = 0.56, 95%CI, 0.45 to 0.69), glucagon-like peptide-1 receptor agonist (GLP-1RA) (OR = 0.58, 95%CI, 0.46 to 0.73), thiazolidinedione (TZD) (OR = 0.68, 95%CI, 0.57 to 0.81) and metformin (OR = 0.89, 95%CI, 0.80 to 0.99) treatments were all associated with reduced risk of dementia in patients with T2D. The surface under the cumulative ranking curve (SUCRA) evaluation conferred a rank order as SGLT-2i > GLP-1RA > TZD > dipeptidyl peptidase-4 inhibitor (DPP-4i) > metformin > α-glucosidase inhibitor (AGI) > glucokinase activator (GKA) > sulfonylureas > glinides > insulin in terms of the cognitive benefits. Meanwhile, compared with non-users, SGLT-2i (OR = 0.43, 95%CI, 0.30 to 0.62), GLP-1RA (OR = 0.54, 95%CI, 0.30 to 0.96) and DPP-4i (OR = 0.73, 95%CI, 0.57 to 0.93) were associated with a reduced risk of Alzheimer's disease while a lower risk of vascular dementia was observed in patients receiving SGLT-2i (OR = 0.42, 95%CI, 0.22 to 0.80) and TZD (OR = 0.52, 95%CI, 0.36 to 0.75) treatment. In the network meta-analysis of RCTs, the risks of dementia were comparable among anti-diabetic agents and placebo. CONCLUSION: Compared with non-users, SGLT-2i, GLP-1RA, TZD and metformin were associated with the reduced risk of dementia in patients with T2D. SGLT-2i, and GLP-1RA may serve as the optimal choice to improve the cognitive prognosis in patients with T2D.

---

### PMID 40189519 — current stance: `supports`

**Evidence span:** > Neither GLP-1 receptor agonists nor other SGLT2 inhibitors showed significant preventive effects for any of the investigated neurodegenerative conditions.

**Golden note:** GLP-1/SGLT2 prophylactic benefit on neurodegen network meta.

**The pharmacodynamics-based prophylactic benefits of GLP-1 receptor agonists and SGLT2 inhibitors on neurodegenerative diseases: evidence from a network meta-analysis.**

*BMC medicine*, 2025. Types: Journal Article; Systematic Review; Network Meta-Analysis

> BACKGROUND: Glucagon-like peptide-1 (GLP-1) receptor agonists and sodium-glucose cotransporter 2 (SGLT2) inhibitors represent a new generation of antihyperglycemic agents that operate through mechanisms distinct from conventional diabetes treatments. Beyond their metabolic effects, these medications have demonstrated neuroprotective properties in preclinical studies. While clinical trials have explored their therapeutic potential in established neurodegenerative conditions, their role in disease prevention remains unclear. We conducted a network meta-analysis (NMA) to comprehensively evaluate the prophylactic benefits of these agents across multiple neurodegenerative diseases and identify the most promising preventive strategies. METHODS: We systematically searched PubMed, Embase, ClinicalKey, Cochrane CENTRAL, ProQuest, ScienceDirect, Web of Science, and ClinicalTrials.gov through October 24th, 2024, for randomized controlled trials (RCTs) of GLP-1 receptor agonists or SGLT2 inhibitors. Our primary outcome was the incidence of seven major neurodegenerative diseases: Parkinson's disease, Alzheimer's disease, Lewy body dementia, multiple sclerosis, amyotrophic lateral sclerosis, frontotemporal dementia, and Huntington's disease. Secondary outcomes included safety profiles assessed through dropout rates. We performed a frequentist-based NMA and evaluated risk of bias with Risk of Bias tool. The main result of the primary outcome in the current study would be re-affirmed via sensitivity test with Bayesian-based NMA. RESULTS: Our analysis encompassed 22 RCTs involving 138,282 participants (mean age 64.8 years, 36.4% female). Among all investigated medications, only dapagliflozin demonstrated significant prophylactic benefits, specifically in preventing Parkinson's disease (odds ratio = 0.28, 95% confidence intervals = 0.09 to 0.93) compared to controls. Neither GLP-1 receptor agonists nor other SGLT2 inhibitors showed significant preventive effects for any of the investigated neurodegenerative conditions. Drop-out rates were comparable across all treatments. CONCLUSIONS: This comprehensive NMA reveals a novel and specific prophylactic effect of dapagliflozin against Parkinson's disease, representing a potential breakthrough in preventive neurology. The specificity of dapagliflozin's protective effect to Parkinson's disease might rely on its highly selective inhibition to SGLT2. These findings provide important direction for future research and could inform preventive strategies for populations at risk of Parkinson's disease. TRIAL REGISTRATION: PROSPERO CRD42021252381.

---

### PMID 40017057 — current stance: `inconclusive`

**Evidence span:** > Glucagon-like peptide-1 receptor agonists (GLP-1 RA) versus placebo reduced dementia risk by 53% in three RCTs (n = 15,820, RR = 0.47[0.25, 0.86]) and 27% in three case-control studies (n = 312,856, RR = 0.73[0.54, 0.99], I2 = 96%).

**Golden note:** Diabetes meds cognition meta — mixed by class.

**Effect of diabetes medications on the risk of developing dementia, mild cognitive impairment, or cognitive decline: A systematic review and meta-analysis.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> Background: Diabetes is a risk factor for dementia, but we do not know whether specific diabetes medications ameliorate this risk. Objective: To systematically review and meta-analyze such medication's effect on the risk of developing dementia, mild cognitive impairment (MCI), or cognitive decline. Methods: We searched three databases until 21 November 2023. We included randomized controlled trials (RCT), cohort, and case-control studies assessing association between antidiabetic medication and future dementia, MCI, or cognitive decline. We meta-analyzed studies separately for individual drug classes and their comparators (no medication, placebo, or another drug). We appraised study quality using the Newcastle-Ottawa Scale and Physiotherapy Evidence Database Scale. Results: 42 studies fulfilled inclusion criteria. Glucagon-like peptide-1 receptor agonists (GLP-1 RA) versus placebo reduced dementia risk by 53% in three RCTs (n = 15,820, RR = 0.47[0.25, 0.86]) and 27% in three case-control studies (n = 312,856, RR = 0.73[0.54, 0.99], I2 = 96%). Repaglinide was superior to glibenclamide by 0.8 points on the Mini-Mental State Examination scale in another RCT. Meta-analysis of seven longitudinal studies showed glitazones (n = 1,081,519, RR = 0.78[0.76, 0.81], I2 = 0%) were associated with reduced dementia risk. Metformin (n = 999,349, RR = 0.94[0.79, 1.13], I2 = 98.4%), sulfonylureas (RR = 0.98[0.78, 1.22], I2 = 83.3%), dipeptidyl peptidase-IV inhibitors (DPP-1V) (n = 192,802, RR = 0.86[0.65, 1.15], I2 = 92.9%) and insulin (n = 571,274, RR = 1.09[0.95, 1.25], I2 = 94.8%) were not. Most studies were observational and limited by confounding by indication. Conclusions: In people with diabetes, RCTs consistently showed GLP-RAs reduce future dementia risk. Glitazones consistently showed protective effects, without heterogeneity, suggesting potential generalizability of these results. Metformin, sulfonylureas, insulin, and DPP-1V studies had inconsistent findings. If information is available future studies should consider dosage, severity, and duration.

---

### PMID 41326666 — current stance: `inconclusive`

**Evidence span:** > The primary outcome showed no significant differences in cerebral glucose metabolism (difference = -0.17; 95% confidence interval: -0.39 to 0.06; P = 0.14) between the two groups.

**Golden note:** ELAD phase 2b liraglutide in mild-mod AD — primary endpoint missed; biomarker secondary.

**Liraglutide in mild to moderate Alzheimer's disease: a phase 2b clinical trial.**

*Nature medicine*, 2025. Types: Journal Article; Randomized Controlled Trial; Clinical Trial, Phase II; Multicenter Study

> Liraglutide, a glucagon-like peptide 1 (GLP-1) agonist and antidiabetic drug, has shown neuroprotective effects in animal models. In this study, we aimed to evaluate the safety and efficacy of liraglutide in mild to moderate Alzheimer's disease syndrome. 'Evaluating liraglutide in Alzheimer's disease' (ELAD) is a multicenter, randomized, double-blind, placebo-controlled phase 2b trial in 204 participants with mild to moderate Alzheimer's disease syndrome with no diabetes. Participants received daily injections of liraglutide or placebo for 52 weeks. They underwent fluorodeoxyglucose positron emission tomography, magnetic resonance imaging and detailed neuropsychometric evaluations. The primary outcome was a change in cerebral glucose metabolic rate. Secondary outcomes were safety and tolerability and cognitive changes. The primary outcome showed no significant differences in cerebral glucose metabolism (difference = -0.17; 95% confidence interval: -0.39 to 0.06; P = 0.14) between the two groups. The secondary outcome-score on the Alzheimer's Disease Assessment Scale-Executive domain (ADAS-Exec)-performed better in liraglutide-treated patients compared to placebo (0.15; 95% confidence interval: 0.03-0.28; unadjusted P = 0.01). No significant differences were observed in Alzheimer's Disease Cooperative Study-Activities of Daily Living (ADCS-ADL) (-0.58; 95% confidence interval: -3.13 to 1.97; unadjusted P = 0.65) or Clinical Dementia Rating-Sum of Boxes (CDR-SoB) (-0.06; 95% confidence interval: -0.57 to 0.44; unadjusted P = 0.81) scores. Liraglutide was generally safe and well tolerated in non-diabetic patients with Alzheimer's disease. ClinicalTrials.gov identifier: NCT01843075 .

---

### PMID 37077141 — current stance: `supports`

**Evidence span:** > In this review, we showed that GLP-1 receptor agonists can effectively change cognitive function, BMI and blood glucose levels in patients with AD.

**Golden note:** GLP-1 RA cognitive function in AD meta — improves cognition.

**Evaluating the effects of glucagon-like peptide-1 receptor agonists on cognitive function in Alzheimer's disease: A systematic review and meta-analysis.**

*Advances in clinical and experimental medicine : official organ Wroclaw Medical University*, 2023. Types: Meta-Analysis; Systematic Review; Journal Article

> BACKGROUND: Alzheimer's disease (AD) is the most common type of dementia. At present, some drug and non-drug therapies can be used to slow disease progression or prevent cognitive deterioration. More treatment options still need to be explored. OBJECTIVES: A meta-analysis was performed to compile the relevant evidence for the use of glucagon-like peptide-1 (GLP-1) receptor agonists in preventing AD. MATERIAL AND METHODS: We systematically searched English and Chinese databases, including Embase, PubMed, Cochrane Library, China National Knowledge Infrastructure (CNKI), Wanfang Data Knowledge Service Platform, and Weipu website (VIP), based on the PICOS (Participants, Interventions, Comparisons, Outcomes, Study design) principles. The reviewers evaluated the search results and conducted the analysis; 5 articles with a total sample size of 184 patients were included. Changes in cognitive function, body mass index (BMI), blood glucose level, and insulin content were analyzed. RESULTS: A low risk of bias and no publication bias were found in these studies. The following results were obtained: 1) cognitive function: mean difference (MD) = 2.16, 95% confidence interval (95% CI): 1.45-2.88; 2) BMI change: MD = -1.16, 95% CI: -1.71--0.61; and 3) blood glucose change: standard MD (SMD) = -0.64, 95% CI: -1.21--0.88. No statistically significant difference was found in insulin content. CONCLUSION: In this review, we showed that GLP-1 receptor agonists can effectively change cognitive function, BMI and blood glucose levels in patients with AD. This provides relevant clues for the prevention of AD. However, more studies are needed to refine these conclusions.

---

### PMID 25418147 — current stance: `supports`

**Evidence span:** > Clinical trials in patients with cognitive impairment and AD testing the effects of GLP-1 analogs have recently started.

**Golden note:** GLP-1 mimetics review for AD — neuroprotective.

**[Glucagon-like peptide-1 (GLP-1) mimetics: a new treatment for Alzheimer's disease?].**

*Revista de neurologia*, 2014. Types: Journal Article; Systematic Review

> INTRODUCTION: The glucagon-like peptide-1 (GLP-1) mimetics are an established therapeutic option for patients with type 2 diabetes. However, the properties of the GLP-1 mimetics go beyond the strict metabolic control of the patients with diabetes. The neuroprotective effects of GLP-1 have been shown in recent studies opening new areas of research in neurodegenerative diseases such as Alzheimer's disease (AD), among others. AIM. Systematic review including experimental studies and human clinical trials demonstrating the neuroprotective properties of GLP-1 mimetics in AD. DEVELOPMENT: The experimental studies that have been conducted in rodent models of AD have demonstrated the neuroprotective properties of GLP-1 in the central nervous system reducing beta-amyloid plaques, the oxidative stress and the inflammatory brain response. Clinical trials in patients with cognitive impairment and AD testing the effects of GLP-1 analogs have recently started. CONCLUSION: The GLP-1 analogs have neuroprotective properties. Considering that type 2 diabetes is a risk factor for cognitive impairment and dementia, the benefits of GLP-1 mimetics on cognition must be considered. Likewise, the GLP-1 mimetics represent a promising treatment for neurodegenerative diseases such as AD.

---

### PMID 39952607 — current stance: `supports`

**Evidence span:** > SGLT2 inhibitors were associated with a significantly lower incidence of overall dementia compared to GLP-1 receptor agonists (2.7 % vs. 3.6 %; HR, 0.92; 95 % CI, 0.89-0.95).

**Golden note:** SGLT2 vs GLP-1 in T2D — both reduce dementia.

**Comparative effectiveness of SGLT2 inhibitors and GLP-1 receptor agonists in preventing Alzheimer's disease, vascular dementia, and other dementia types among patients with type 2 diabetes.**

*Diabetes & metabolism*, 2025. Types: Journal Article; Comparative Study

> BACKGROUND: Type 2 diabetes mellitus (T2DM) is associated with an elevated risk of dementia, including Alzheimer's disease (AD) and vascular dementia (VaD). While sodium-glucose cotransporter-2 (SGLT2) inhibitors and glucagon-like peptide-1 (GLP-1) receptor agonists have shown neuroprotective potential, comparative data on their efficacy in dementia prevention remain scarce. METHODS: - We conducted a retrospective cohort study using the TriNetX database, including 307,103 SGLT2 inhibitor users and 348,686 GLP-1 receptor agonist users with T2DM. Propensity score matching yielded 221,883 pairs with balanced baseline characteristics. The primary outcome was overall dementia incidence, with secondary outcomes including AD, VaD, and all-cause mortality. Hazard ratios (HRs) were calculated using Cox proportional hazards models. RESULTS: SGLT2 inhibitors were associated with a significantly lower incidence of overall dementia compared to GLP-1 receptor agonists (2.7 % vs. 3.6 %; HR, 0.92; 95 % CI, 0.89-0.95). The risk of VaD (HR, 0.89; 95 % CI, 0.84-0.95) and AD (HR, 0.90; 95 % CI, 0.86-0.94) was also reduced with SGLT2 inhibitors. All-cause mortality was lower in the SGLT2 group (3.6 % vs. 4.6 %; HR, 0.95; 95 % CI, 0.92-0.98). No significant difference was observed in other dementia subtypes (HR, 0.96; 95 % CI, 0.91-1.01). CONCLUSIONS: In this large, real-world cohort, SGLT2 inhibitors demonstrated superior efficacy over GLP-1 receptor agonists in reducing the risks of overall dementia, VaD, and AD among patients with T2DM. These findings support the preferential use of SGLT2 inhibitors in mitigating dementia risk in this population, though randomized controlled trials are warranted for confirmation.

---

