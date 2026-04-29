# Q3: Does metformin lower dementia risk in type 2 diabetes patients?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=27 PMIDs.

**Current S/C/I**: 7 / 1 / 19
**Proposed S/C/I**: 7 / 3 / 17

After the second-pass review (added one additional clean flip
`32719079` inconclusive → contradicts; flagged borderline entries for
cross-question policy decisions), net flips = **6** (2 S→C, 2 I→S,
1 C→I, 1 I→C).

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `35297284` | 2022 | **supports → contradicts** | The current note ("metformin improves cognition") **does not match the abstract**. Verbatim from abstract: *"There was no significant relationship between metformin therapy and cognitive performance in none of the studies"* and *"metformin has no significant effect on improving cognitive function or protecting against any dementia... and cognitive impairment as well."* Pooled meta of 19 studies. Clear `contradicts`. |
| `35786654` | 2022 | **supports → contradicts** | Verbatim conclusion: *"The available evidence does not support the idea that metformin reduces risk of AD, and it may, in fact, increase the risk in Asians."* Pooled OR 1.17 (0.88–1.56) crossing null; significant *increased* risk in Asian subgroup. Note ("metformin reduces AD risk") is wrong. |
| `37830443` | 2023 | **inconclusive → supports** | NACC longitudinal, n=1393. Metformin associated with significant 3.2% absolute risk reduction (CI -6.2 to -0.2). Heterogeneity by subgroup but the overall effect is significant. Note "varies by subgroup" is true but obscures that the main effect is positive. |
| `38705542` | 2024 | **inconclusive → supports** | Bayesian NMA of 16 studies, n=1,565,245. *"Dementia and AD risks were significantly lower with metformin and SGLT2i. Metformin displayed the lowest risk of dementia across diverse antidiabetics."* Significantly positive on metformin specifically. |
| `40695613` | 2025 | **contradicts → inconclusive** *(borderline)* | Comparative cohort GLP-1 vs metformin, n=87,229 each. GLP-1 better than metformin (HR 0.90 for dementia). This says GLP-1 > metformin, **not** that metformin fails vs control. The `contradicts` framing of the question ("does metformin lower dementia risk") requires a metformin-vs-no-metformin comparator. This study has none. |
| `32719079` | 2020 | **inconclusive → contradicts** *(added 2nd pass)* | Well-powered observational meta-analysis (n=285,966, 23 comparisons / 19 studies). Pooled OR 1.04 (95% CI 0.92–1.17) crossing null on neurodegenerative disease incidence. Verbatim conclusion: *"Metformin has failed to demonstrate a beneficial effect on NDs. In addition, it may increase the risk of PD development."* Strict bar: well-powered observational null on the primary association ⇒ `contradicts`. The note ("Meta acknowledges inconsistent metformin findings") understates a clear-failure conclusion. |

### Withdrawn / reconsidered

| PMID | Year | Decision | Notes |
|------|------|----------|-------|
| `29790638` | 2018 | **keep `inconclusive`** (no flip) | Antidiabetic NMA; class effect positive but metformin not separately significant vs placebo. |
| `36090264` | 2022 | **keep `supports`** | Significant adjusted HR 0.92 for cognitive impairment, 0.90 for dementia, but null for AD specifically. Defensible as `supports` for the dementia question. |

## Confirmed (no change)

- `30149446` (2018 meta, HR 0.76 for dementia incidence sig) — **supports ✓**
- `26890736` (2016 pilot RCT in non-diabetic aMCI) — **inconclusive ✓** (pilot exempt)
- `33080602`, `40017057`, `33935082`, `38160357`, `38279266`, `37968954`, `39871536`, `40268162`, `40023730`, `37869901`, `28538088`, `33609776`, `41223766` — all **inconclusive ✓** (genuinely mixed, comparator framing, biomarker-only, or umbrella reviews that explicitly note inconsistency)
- `36220195` (2022 VA cohort comparing SU/TZD/MET) — **inconclusive ✓** (uses MET as the *reference*; doesn't tell us MET vs no-MET)
- `39716328` (2024 NMA, metformin OR 0.89 sig in observational arm but null in RCT arm) — could → `supports` if we count the observational signal; **keep `inconclusive`** because the RCT arm is null and the conclusion explicitly downgrades metformin to behind SGLT2i and GLP-1.

## Borderline (not flipped, but flagged for cross-question policy decisions)

These entries surface recurring policy issues identified across the golden
set. Not flipped here pending a global policy decision.

- `27250528` (2016, insulin-sensitizers meta) — **currently `supports`**.
  Class-level RR 0.78 (0.64–0.95, p=0.015) is significant, but **metformin
  alone is RR 0.79 (0.62–1.01, p=0.064), explicitly marginal/non-significant**.
  Conclusion uses hedged language ("might provide protection"). Strict bar
  for metformin specifically would say `inconclusive`. **Falls under policy
  (a)/(c)** — class-positive but the metformin-specific endpoint did not
  reach significance; question is "does metformin lower dementia risk", not
  "do insulin sensitizers". Decision pending: count class-level results as
  metformin evidence, or hold each drug to its own significance test?

- `36090264` (2022, observational meta in DM) — **currently `supports`**.
  Significant for cognitive impairment (aHR 0.92) and dementia (aHR 0.90),
  **but null for AD specifically (aHR 1.10, 95% CI 0.95–1.28)**. Authors'
  conclusion: "the use of metformin... for the prevention of dementia, but
  not AD, is supported by the available evidence." **Falls under policy
  (c)** — split outcome, hits one endpoint, misses another. For the Q3
  framing ("dementia risk"), `supports` is defensible; if Q3 were "AD
  risk", this would flip to `contradicts`. Flagged because the split is
  not represented in the single-stance label.

- `35445359` (2022, ADNI observational subgroup) — **currently `supports`**.
  The "T2D + metformin vs T2D no-metformin" arm comes from an observational
  cohort (ADNI), not a randomized parent. Within ADNI's MCI population,
  authors compute T2D-positive subgroups and find metformin-treated patients
  do better. **Falls under policy (a)-adjacent** — non-randomized subgroup
  positive within a broader observational study; the parent ADNI cohort is
  not a trial with a primary endpoint, so policy (a) doesn't apply cleanly,
  but the comparator-subgroup nature is similar in flavor. Defensible as
  `supports` under the dementia question; flagged for cross-question
  consistency.

## Cross-cutting issues

- **Mostly comparator/network meta-analyses.** Many of the "metformin"
  studies are really "antidiabetic class comparison" studies where metformin
  is the *reference*, not the treatment. The question framing should be
  tightened, or the eval should distinguish metformin-vs-no-treatment from
  metformin-vs-other-class.
- **Recommendation:** rephrase question as *"Among antidiabetics, does
  metformin reduce dementia risk?"* and treat comparator studies
  appropriately, OR move comparator-only papers to `excluded`.

## Cross-question policy questions raised by Q3

The borderline entries above all touch one of three recurring policy
questions across the golden set:

1. **(a) Subgroup-positive in parent-null context** — `35445359`
   (ADNI observational subgroup) is comparator-subgroup-positive within a
   non-randomized parent. Closest Q3 fit to policy (a). `27250528` is the
   inverse flavor — a class-level positive where the metformin-specific
   subset is non-significant.
2. **(c) Split-outcome / mixed-endpoint** — `36090264` hits dementia
   (aHR 0.90) but misses AD (aHR 1.10, NS). One paper, two stances depending
   on which endpoint the question pins down.
3. **(b) preclinical-dominated review** — does **not** appear as a
   mislabel in Q3. `41223766` is preclinical-dominated but already labeled
   `inconclusive` (correct), and `33609776` likewise. No Q3 paper labeled
   `supports` rests on preclinical evidence.

## Highest-confidence flips for this question

- `35297284` supports → contradicts ("no significant effect on improving cognitive function")
- `35786654` supports → contradicts ("does not support... may increase the risk in Asians")
- `32719079` inconclusive → contradicts ("Metformin has failed to demonstrate a beneficial effect on NDs"; n=285,966)

All three are unambiguous note-vs-conclusion mismatches against well-powered
designs.

## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

### Proposed new tags (Q3)

- `metformin_as_reference` — observational study uses metformin as the
  comparator/reference arm rather than as the intervention being evaluated;
  cannot speak to metformin-vs-no-metformin.
- `class_positive_drug_null` — pooled "drug class" estimate is significant
  but the metformin-specific subset/branch is not (or only marginally) sig.
- `split_outcome` — same study reports significant benefit on one endpoint
  (e.g., dementia) but null on a related endpoint (e.g., AD specifically).
- `regional_heterogeneity` — pooled effect is driven by one geographic
  region/population subgroup; null in others.
- `rct_obs_disagreement` — within a single NMA/review, the observational arm
  shows benefit but the RCT arm is null (or vice versa).
- `biomarker_only` — outcome is a fluid/imaging biomarker, not a clinical
  cognitive endpoint.

### Tagged pmids

- `26890736` (2016 pilot aMCI RCT) — `pilot_positive`, `wrong_population`
  (non-diabetic, but Q3 is about T2D). Co-primary clinical outcome partly
  hit (SRT total recall, p=0.02); ADAS-cog null. Small n=80.
- `27250528` (2016 insulin-sensitizers meta) — `class_positive_drug_null`,
  `hedged_meta`. Class RR 0.78 sig but metformin RR 0.79 (p=0.064) marginal;
  authors hedge "might provide protection."
- `28538088` (2017 pilot AD crossover RCT) — `pilot_positive`,
  `wrong_population` (non-diabetic AD/MCI). n=20, "trends" only, no sig
  changes in CSF/imaging primary biomarkers.
- `29790638` (2018 antidiabetic NMA) — `class_positive_drug_null`. Class
  effect positive but metformin not separately sig vs placebo; pioglitazone
  is the driver.
- `33609776` (2021 nutrient-sensing review) — `preclinical_dominated`,
  `narrative_review`. Authors explicitly note "clear lack of translation
  from animal models to human populations."
- `33935082` (2021 Korean dual-therapy cohort) — `comparator_only`,
  `metformin_as_reference`. Compares Met+DPP4i, Met+TZD vs Met+SU; doesn't
  isolate metformin effect.
- `35445359` (2022 ADNI subgroup) — `subgroup_positive`. Metformin-treated
  T2D subgroup within ADNI MCI population shows better cognitive performance;
  parent ADNI is observational, not a trial with primary endpoint.
- `36090264` (2022 obs meta in DM) — `split_outcome`. Sig for dementia
  (aHR 0.90) and cognitive impairment (aHR 0.92), but null for AD specifically
  (aHR 1.10, 95% CI 0.95-1.28).
- `36220195` (2022 VA cohort) — `comparator_only`, `metformin_as_reference`.
  Compares SU and TZD vs MET as reference; tells us about SU/TZD relative to
  MET, not MET vs no-MET.
- `37869901` (2023 umbrella review) — `regional_heterogeneity`. Metformin
  effect significant only in US / Western populations; null in Eastern.
- `38160357` (2024 metformin proteomics RCT) — `biomarker_only`,
  `pilot_positive`, `wrong_population` (non-diabetic MCI). n=20, 8-week
  proteomics-only readout, no clinical efficacy endpoint.
- `38279266` (2024 autophagy review) — `narrative_review`. n=10 records,
  heterogeneous interventions (metformin, resveratrol, masitinib, TPI-287);
  explicitly notes "differences in sample power, intervention, patients
  enrolled, assessment, and measure of outcomes prevents generalization."
- `39716328` (2024 antidiabetic NMA) — `rct_obs_disagreement`,
  `class_positive_drug_null`. Metformin OR 0.89 sig in observational arm
  but RCT arm shows risks "comparable among anti-diabetic agents and
  placebo"; conclusion downgrades metformin behind SGLT2i and GLP-1RA.
- `40268162` (2025 SGLT2 vs metformin) — `comparator_only`,
  `metformin_as_reference`. No placebo arm; SGLT2 better than metformin
  doesn't establish metformin vs no-metformin.
- `40695613` (2025 GLP-1 vs metformin, currently contradicts → flagged
  inconclusive) — `comparator_only`, `metformin_as_reference`. No placebo;
  GLP-1 > metformin head-to-head doesn't establish metformin null vs control.
- `41223766` (2025 metformin CNS review) — `preclinical_dominated`,
  `narrative_review`. Authors explicitly state "majority of available data
  are preclinical."

All other pmids — untagged (clean canonical examples within their stance):
`30149446`, `32719079`, `35297284`, `35786654`, `37830443`, `38705542`,
`37968954`, `39871536`, `33080602`, `40017057`, `40023730`.

---

## Abstracts (n=27)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 30149446 — current stance: `supports`

**Stance justification:** > Meta-analysis of three studies showed that cognitive impairment was significantly less prevalent in diabetic metformin (Odds ratio = 0.55, 95% CI 0.38 to 0.78), while six studies showed that dementia incidence was also significantly reduced (Hazard ratio = 0.76, 95% CI 0.39 to 0.88).

**Golden note:** Meta-analysis — metformin reduced dementia risk in diabetes patients.

**Metformin Use Associated with Reduced Risk of Dementia in Patients with Diabetes: A Systematic Review and Meta-Analysis.**

*Journal of Alzheimer's disease : JAD*, 2018. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: Metformin, a first line antihyperglycemic medication, is an AMPK activator and has been hypothesized to act as a geroprotective agent. Studies on its association with various classifications of age-related cognitive decline have shown mixed results with positive and negative findings. OBJECTIVE: To synthesize the best available evidence on the association of metformin-use with risk, progression, and severity of dementia. METHOD: Eligible research investigated the effect of metformin on dementia, Alzheimer's disease, or any measure of cognitive impairment compared to any control group who were not receiving metformin. The initial search resulted in 862 citations from which 14 studies (seven cohort, four cross-sectional, two RCTs, and one case control) were included. RESULTS: Meta-analysis of three studies showed that cognitive impairment was significantly less prevalent in diabetic metformin (Odds ratio = 0.55, 95% CI 0.38 to 0.78), while six studies showed that dementia incidence was also significantly reduced (Hazard ratio = 0.76, 95% CI 0.39 to 0.88). Mini-Mental State Examination scores were not significantly affected by metformin-use, although both RCTs showed that metformin had a neuroprotective effect compared to placebo. Some studies found negative or neutral effects for metformin use by people with diabetes; the potential mechanism of metformin-induced vitamin B12 deficiency is discussed. CONCLUSIONS: Metformin should continue to be used as a first line therapy for diabetes in patients at risk of developing dementia or Alzheimer's disease. The use of metformin by individuals without diabetes for the prevention of dementia is not supported by the available evidence.

---

### PMID 26890736 — current stance: `inconclusive`

**Stance justification:** > After adjusting for baseline ADAS-cog, changes in total recall of the SRT favored the metformin group (9.7±8.5 versus 5.3±8.5; p = 0.02). Differences for other outcomes were not significant.

**Golden note:** Pilot RCT in amnestic MCI — small, exploratory.

**Metformin in Amnestic Mild Cognitive Impairment: Results of a Pilot Randomized Placebo Controlled Clinical Trial.**

*Journal of Alzheimer's disease : JAD*, 2016. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> Diabetes and hyperinsulinemia may be risk factors for Alzheimer's disease (AD). We conducted a pilot study of metformin, a medication efficacious in treating and preventing diabetes while reducing hyperinsulinemia, among persons with amnestic mild cognitive impairment (aMCI) with the goal of collecting preliminary data on feasibility, safety, and efficacy. Participants were 80 men and women aged 55 to 90 years with aMCI, overweight or obese, without treated diabetes. We randomized participants to metformin 1000 mg twice a day or matching placebo for 12 months. The co-primary clinical outcomes were changes from baseline to 12 months in total recall of the Selective Reminding Test (SRT) and the score of the Alzheimer's Disease Assessment Scale-cognitive subscale (ADAS-cog). The secondary outcome was change in relative glucose uptake in the posterior cingulate-precuneus in brain fluorodeoxyglucose positron emission tomography. Change in plasma Aβ42 was an exploratory outcome. The mean age of participants was 65 years. Fifty percent of participants were women. The only baseline variable that was different between the arms was the ADAS-Cog. Metformin could not be tolerated by 7.5% of participants; 15% tolerated 500 mg/day, 35% tolerated 1000 mg/day, 32.5% tolerated 1500 mg/day, and only 10% tolerated the maximum dose. There were no serious adverse events related to metformin. The 7.5% of persons who did not tolerate metformin reported gastrointestinal symptoms. After adjusting for baseline ADAS-cog, changes in total recall of the SRT favored the metformin group (9.7±8.5 versus 5.3±8.5; p = 0.02). Differences for other outcomes were not significant. A larger trial seems warranted to evaluate the efficacy and cognitive safety of metformin in prodromal AD.

---

### PMID 29790638 — current stance: `inconclusive`

**Stance justification:** > Pioglitazone 15 to 30 mg demonstrated the greatest efficacy compared to placebo in network meta-analysis. No significant differences in acceptability were identified when comparing agents with each other and with placebo.

**Golden note:** Network meta antidiabetic agents — mixed by drug class.

**Comparative efficacy and acceptability of antidiabetic agents for Alzheimer's disease and mild cognitive impairment: A systematic review and network meta-analysis.**

*Diabetes, obesity & metabolism*, 2018. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review; Network Meta-Analysis

> This study (registered with PROSPERO, CRD42018085967) compares the efficacy (i.e. pro-cognitive effects) and acceptability of antidiabetic agents for Alzheimer's disease (AD) and mild cognitive impairment (MCI). Cochrane Library (CENTRAL), PubMed/MEDLINE, EMBASE and PsycINFO were searched from inception to January 15, 2018 for randomized controlled trials comparing antidiabetic agents with placebo and/or another active antidiabetic agent for the treatment of AD or MCI. Nineteen eligible studies (n = 4855) evaluating the effects of 6 different antidiabetic drugs (i.e. intranasal insulin, pioglitazone, rosiglitazone, metformin, sitagliptin and liraglutide) were included. The results of 29 pairwise comparisons indicated that cognition was significantly improved in subjects treated with antidiabetic agents compared with placebo. Pioglitazone 15 to 30 mg demonstrated the greatest efficacy compared to placebo in network meta-analysis. No significant differences in acceptability were identified when comparing agents with each other and with placebo. The current findings indicate a pro-cognitive class effect of antidiabetic agents in AD/MCI. Other antidiabetic agents should also be investigated in future studies.

---

### PMID 33080602 — current stance: `inconclusive`

**Stance justification:** > Metformin and liraglutide showed promising results, but further research is needed as just 2 clinical trials involved each of these drugs.

**Golden note:** Antidiabetic systematic review including metformin — modest evidence.

**Antidiabetic Drugs in Alzheimer's Disease and Mild Cognitive Impairment: A Systematic Review.**

*Dementia and geriatric cognitive disorders*, 2020. Types: Systematic Review; Journal Article

> INTRODUCTION: Considering that Alzheimer's disease (AD) and diabetes mellitus share pathophysiological features and AD remains with no cure, antidiabetic drugs like intranasal insulin, glitazones, metformin, and liraglutide are being tested as a potential treatment. OBJECTIVE: The aim of this systematic review was to assess the efficacy of antidiabetic drugs in patients with AD, mild cognitive impairment (MCI), or subjective cognitive complaints (SCCs). Cognition was studied as the primary outcome and modulation of AD biomarkers, and imaging was also assessed as a secondary outcome. METHODS: We conducted a search in the electronic databases PubMed/MEDLINE, EMBASE, and Scopus seeking clinical trials evaluating the effect on cognition of antidiabetic drugs in patients with AD, MCI, or SCCs. RESULTS: A total of 23 articles were found eligible. Intranasal regular insulin improved verbal memory in most studies, especially in apoE4- patients, but results in other cognitive domains were unclear. Detemir improved cognition after 2 months of treatment, but it did not after 4 months. Pioglitazone improved cognition in diabetic patients with AD or MCI in 3 clinical trials, but it is controversial as 2 other studies did not show effect. Metformin and liraglutide showed promising results, but further research is needed as just 2 clinical trials involved each of these drugs. Almost all drugs tested were shown to modulate AD biomarkers and imaging. CONCLUSIONS: Intranasal insulin, pioglitazone, metformin, and liraglutide are promising drugs that could be useful in the treatment of AD. However, many questions remain to be answered in future studies, so no particular antidiabetic drug can currently be recommended to treat AD.

---

### PMID 27250528 — current stance: `supports`

**Stance justification:** > The incidence rate of dementia was reduced with either metformin (RR 0.79, 95% CI 0.62-1.01, p = 0.064) or thiazolidinediones (RR 0.75, 95% CI 0.56-1.00, p = 0.050), both with a marginal trend toward significance.

**Golden note:** Insulin-sensitizers meta — reduced dementia incidence (metformin a key contributor).

**Impact of Insulin Sensitizers on the Incidence of Dementia: A Meta-Analysis.**

*Dementia and geriatric cognitive disorders*, 2016. Types: Journal Article; Meta-Analysis

> BACKGROUND: Abundant evidence from epidemiological and clinical studies has proven that diabetes mellitus (DM) is correlated with an increased incidence of dementia and Alzheimer's disease (AD). Insulin resistance is considered to play an important role in the associations between DM and dementia. However, whether insulin sensitizer drugs are effective in preventing dementia still remains unclear. METHODS: Electronic searches of PubMed, EMBASE, Google Scholar, and the ISI Web of Science were conducted to identify studies that reported about the associations between insulin sensitizers and the incidence of dementia. The included studies were reviewed, and a meta-analysis was performed using STATA to determine the combined relative risk (RR) for the incidence of dementia when using insulin sensitizers. Subgroup analysis and meta regression were also conducted. RESULTS: In total, nine comparisons out of six studies were qualified for inclusion, and data from 544,093 participants were evaluated. The results of the meta-analysis revealed a combined RR of 0.78 (95% CI 0.64-0.95, p = 0.015) for the incidence of dementia when using insulin sensitizers. The incidence rate of dementia was reduced with either metformin (RR 0.79, 95% CI 0.62-1.01, p = 0.064) or thiazolidinediones (RR 0.75, 95% CI 0.56-1.00, p = 0.050), both with a marginal trend toward significance. CONCLUSIONS: The results indicate that insulin sensitizer drugs might provide protection against incident dementia. Controlled studies with large samples should be conducted to further confirm these conclusions and provide information for clinical strategies.

---

### PMID 35297284 — current stance: `supports`

**Stance justification:** > Results show that metformin has no significant effect on improving cognitive function or protecting against any dementia including vascular dementia and Alzheimer's disease, and cognitive impairment as well.

**Golden note:** Meta-analysis — metformin improves cognition in T2D.

**The effect of metformin on cognitive function: A systematic review and meta-analysis.**

*Journal of psychopharmacology (Oxford, England)*, 2022. Types: Journal Article; Meta-Analysis; Systematic Review

> Most people are familiar with metformin as a diabetic treatment option. Different positive benefits have been found for it, in addition to its anti-diabetes properties. Cognitive function enhancement is the most recent characteristic that has been studied. This study aimed to look at the evidence on the effects of metformin on cognitive performance. Web of Science, PubMed, Scopus, the Cochrane Library, EMBASE, and PsycINFO databases were searched systematically. After eliminating duplicates and irrelevant documents, the findings were screened. The documents that remained were scanned and data were extracted. Nineteen studies were qualified for meta-analysis after evaluating 3827 identified records. There was no significant relationship between metformin therapy and cognitive performance in none of the studies including cross-sectionals, cohorts, and clinical trials (p > 0.05). Results show that metformin has no significant effect on improving cognitive function or protecting against any dementia including vascular dementia and Alzheimer's disease, and cognitive impairment as well.

---

### PMID 36220195 — current stance: `inconclusive`

**Stance justification:** > After at least 1 year of treatment, TZD monotherapy was associated with a 22% lower risk of all-cause dementia onset (HR 0.78, 95% CI 0.75 to 0.81), compared with MET monotherapy, and 11% lower for MET and TZD dual therapy (HR 0.89, 95% CI 0.86 to 0.93).

**Golden note:** US veterans cohort — comparing SU/TZD/metformin, mixed.

**Use of oral diabetes medications and the risk of incident dementia in US veterans aged ≥60 years with type 2 diabetes.**

*BMJ open diabetes research & care*, 2022. Types: Journal Article; Observational Study; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> INTRODUCTION: Studies have reported that antidiabetic medications (ADMs) were associated with lower risk of dementia, but current findings are inconsistent. This study compared the risk of dementia onset in patients with type 2 diabetes (T2D) treated with sulfonylurea (SU) or thiazolidinedione (TZD) to patients with T2D treated with metformin (MET). RESEARCH DESIGN AND METHODS: This is a prospective observational study within a T2D population using electronic medical records from all sites of the Veterans Affairs Healthcare System. Patients with T2D who initiated ADM from January 1, 2001, to December 31, 2017, were aged ≥60 years at the initiation, and were dementia-free were identified. A SU monotherapy group, a TZD monotherapy group, and a control group (MET monotherapy) were assembled based on prescription records. Participants were required to take the assigned treatment for at least 1 year. The primary outcome was all-cause dementia, and the two secondary outcomes were Alzheimer's disease and vascular dementia, defined by International Classification of Diseases (ICD), 9th Revision, or ICD, 10th Revision, codes. The risks of developing outcomes were compared using propensity score weighted Cox proportional hazard models. RESULTS: Among 559 106 eligible veterans (mean age 65.7 (SD 8.7) years), the all-cause dementia rate was 8.2 cases per 1000 person-years (95% CI 6.0 to 13.7). After at least 1 year of treatment, TZD monotherapy was associated with a 22% lower risk of all-cause dementia onset (HR 0.78, 95% CI 0.75 to 0.81), compared with MET monotherapy, and 11% lower for MET and TZD dual therapy (HR 0.89, 95% CI 0.86 to 0.93), whereas the risk was 12% higher for SU monotherapy (HR 1.12 95% CI 1.09 to 1.15). CONCLUSIONS: Among patients with T2D, TZD use was associated with a lower risk of dementia, and SU use was associated with a higher risk compared with MET use. Supplementing SU with either MET or TZD may partially offset its prodementia effects. These findings may help inform medication selection for elderly patients with T2D at high risk of dementia.

---

### PMID 35786654 — current stance: `supports`

**Stance justification:** > The available evidence does not support the idea that metformin reduces risk of AD, and it may, in fact, increase the risk in Asians.

**Golden note:** Observational meta — metformin reduces AD risk in T2DM.

**Association Between Metformin and Alzheimer's Disease: A Systematic Review and Meta-Analysis of Clinical Observational Studies.**

*Journal of Alzheimer's disease : JAD*, 2022. Types: Meta-Analysis; Systematic Review; Research Support, Non-U.S. Gov't; Journal Article

> BACKGROUND: As one of the widely used drugs for the management of type 2 diabetes mellites (T2DM), metformin is increasingly believed to delay cognitive deterioration and therapeutically for Alzheimer's disease (AD) patients especially those with T2DM. However, studies of the potential neuroprotective effects of metformin in AD patients have reported contradictory results. OBJECTIVE: This study aimed to evaluate the association between metformin and the risk of developing AD. METHODS: We systematically searched the PubMed, EMBASE, Web of Science, Cochrane Central Register of Controlled Trials, and ClinicalTrials.gov databases to identify clinical observational studies on the relationship between AD risk and metformin use published before December 20, 2021. Two investigators independently screened records, extracted data, and assessed the quality of the studies. Pooled odds ratios (ORs) and corresponding 95% confidence intervals (CIs) were calculated using random-effect models. RESULTS: After screening a total of 1,670 records, we included 10 studies involving 229,110 participants. The meta-analysis showed no significant association between AD incidence and metformin exposure (OR 1.17, 95% CI 0.88-1.56, p = 0.291). However, subgroup analysis showed that among Asians, the risk of AD was significantly higher among metformin users than those who did not (OR 1.71, 95% CI 1.24-2.37, p = 0.001). CONCLUSION: The available evidence does not support the idea that metformin reduces risk of AD, and it may, in fact, increase the risk in Asians. Further well-designed randomized controlled trials are required to understand the role played by metformin and other antidiabetic drugs in the prevention of AD and other neurodegenerative diseases.

---

### PMID 36090264 — current stance: `supports`

**Stance justification:** > Moreover, the use of metformin by adults with diabetes for the prevention of dementia, but not AD, is supported by the available evidence.

**Golden note:** Meta — metformin associated with reduced cognitive impairment in DM.

**Metformin use is associated with a reduced risk of cognitive impairment in adults with diabetes mellitus: A systematic review and meta-analysis.**

*Frontiers in neuroscience*, 2022. Types: Systematic Review; Journal Article

> OBJECTIVE: Controversy exists regarding the impact of metformin and whether it prevents or promotes the incidence of cognitive dysfunction. This systematic review and meta-analysis were conducted to identify the effect of metformin therapy on cognitive function in patients with diabetes. METHODS: Electronic databases (PubMed, EMBASE, PsycINFO, the Cochrane Library, and Web of Science) were systematically searched by two investigators from the date of inception until March 1, 2022. The study followed PRISMA guidelines. Inclusion criteria were defined according to the PECOS model. Eligible studies investigated cognitive dysfunction in metformin users compared with non-users in adults with diabetes. Only observational study designs (such as cohort, cross-section, and case-control) were included. RESULTS: A systematic search identified 1,839 articles, of which 28 (17 cohort, 8 case-control, and 3 cross-sectional studies) were included in the meta-analysis. Metformin reduced the occurrence of cognitive impairment in patients with diabetes [unadjusted hazard ratio (HR) = 0.67, 95% CI: 0.62-0.73; adjusted hazard ratio (aHR) = 0.92, 95% CI: 0.85-0.99]. In addition, the use of metformin was associated with a decreased risk of dementia (HR = 0.64, 95% CI: 0.59-0.69; aHR = 0.90, 95% CI: 0.84-0.96), while a random-effects meta-analysis indicated no significant effect of metformin on the risk of Alzheimer's disease (AD) (HR = 0.85, 95% CI: 0.60-1.22; aHR = 1.10, 95% CI: 0.95-1.28). CONCLUSION: Metformin therapy decreased the occurrence risk of cognitive decline in patients with diabetes mellitus. Moreover, the use of metformin by adults with diabetes for the prevention of dementia, but not AD, is supported by the available evidence.

---

### PMID 35445359 — current stance: `supports`

**Stance justification:** > Our study-employing different strategies for data analysis from the global study ADNI-shows a beneficial effect of metformin treatment on cognitive performance, CSF biomarkers profile, and neuroanatomical measures in MCI due to AD patients.

**Golden note:** ADNI subgroup — diabetic AD patients on metformin perform better.

**Diabetic patients treated with metformin during early stages of Alzheimer's disease show a better integral performance: data from ADNI study.**

*GeroScience*, 2022. Types: Journal Article; Observational Study

> We evaluated the effect of the antidiabetic drug metformin on patients enrolled in the ADNI study considering patients with mild cognitive impairment (MCI) due to Alzheimer's disease (AD). Employing data from this observational study, we performed a principal component analysis focusing on the cognitive sphere by evaluating data from neuropsychological tests included in a modified version of the Alzheimer's Disease Cooperative Study-Preclinical Alzheimer Cognitive Composite (ADCS-PACC). Second, we included the levels of amyloid-β, tau, and phosphorylated tau in CSF. We found that MCI metformin-treated patients were globally characterized as subjects with a better cognitive performance and CSF biomarkers profile than the mean population of MCI patients. On the other hand, control subjects and type 2 diabetes patients (T2D) were paired by age, gender, ApoE allele, and years of education, defining three groups: MCI, MCI + T2D, and MCI + T2D + metformin. We evaluated the effect of T2D and metformin treatment employing the PACC score and composites defined from standardized ADNI variables to evaluate the memory and learning function. We found that MCI + T2D patients had a worse cognitive performance than MCI patients, but this deleterious effect was not observed in MCI + T2D + metformin patients. These cognitive variations were associated with changes in cortical thickness and hippocampal volume. Finally, no differences were found in metabolic plasmatic parameters (glycemia, cholesterol, triglycerides). Our study-employing different strategies for data analysis from the global study ADNI-shows a beneficial effect of metformin treatment on cognitive performance, CSF biomarkers profile, and neuroanatomical measures in MCI due to AD patients.

---

### PMID 39716328 — current stance: `inconclusive`

**Stance justification:** > Compared with non-users, SGLT-2i, GLP-1RA, TZD and metformin were associated with the reduced risk of dementia in patients with T2D. SGLT-2i, and GLP-1RA may serve as the optimal choice to improve the cognitive prognosis in patients with T2D.

**Golden note:** Network meta antidiabetics — broad, mixed.

**Anti-diabetic agents and the risks of dementia in patients with type 2 diabetes: a systematic review and network meta-analysis of observational studies and randomized controlled trials.**

*Alzheimer's research & therapy*, 2024. Types: Journal Article; Systematic Review; Network Meta-Analysis; Research Support, Non-U.S. Gov't

> OBJECTIVE: To evaluate the association between anti-diabetic agents and the risks of dementia in patients with type 2 diabetes (T2D). METHODS: Literature retrieval was conducted in PubMed, Embase, the Cochrane Central Register of Controlled Trials and Clinicaltrial.gov between January 1995 and October 2024. Observational studies and randomized controlled trials (RCTs) in patients with T2D, which intercompared anti-diabetic agents or compared them with placebo, and reported the incidence of dementia were included. Conventional and network meta-analyses of these studies were implemented. Results were exhibited as the odds ratio (OR) or risk ratio (RR) with 95% confidence interval (CI). RESULTS: A total of 41 observational studies (3,307,483 participants) and 23 RCTs (155,443 participants) were included. In the network meta-analysis of observational studies, compared with non-users, sodium glucose cotransporter-2 inhibitor (SGLT-2i) (OR = 0.56, 95%CI, 0.45 to 0.69), glucagon-like peptide-1 receptor agonist (GLP-1RA) (OR = 0.58, 95%CI, 0.46 to 0.73), thiazolidinedione (TZD) (OR = 0.68, 95%CI, 0.57 to 0.81) and metformin (OR = 0.89, 95%CI, 0.80 to 0.99) treatments were all associated with reduced risk of dementia in patients with T2D. The surface under the cumulative ranking curve (SUCRA) evaluation conferred a rank order as SGLT-2i > GLP-1RA > TZD > dipeptidyl peptidase-4 inhibitor (DPP-4i) > metformin > α-glucosidase inhibitor (AGI) > glucokinase activator (GKA) > sulfonylureas > glinides > insulin in terms of the cognitive benefits. Meanwhile, compared with non-users, SGLT-2i (OR = 0.43, 95%CI, 0.30 to 0.62), GLP-1RA (OR = 0.54, 95%CI, 0.30 to 0.96) and DPP-4i (OR = 0.73, 95%CI, 0.57 to 0.93) were associated with a reduced risk of Alzheimer's disease while a lower risk of vascular dementia was observed in patients receiving SGLT-2i (OR = 0.42, 95%CI, 0.22 to 0.80) and TZD (OR = 0.52, 95%CI, 0.36 to 0.75) treatment. In the network meta-analysis of RCTs, the risks of dementia were comparable among anti-diabetic agents and placebo. CONCLUSION: Compared with non-users, SGLT-2i, GLP-1RA, TZD and metformin were associated with the reduced risk of dementia in patients with T2D. SGLT-2i, and GLP-1RA may serve as the optimal choice to improve the cognitive prognosis in patients with T2D.

---

### PMID 37830443 — current stance: `inconclusive`

**Stance justification:** > Metformin was significantly associated with a lower risk of dementia in the overall population (RD, -3.2%; 95% CI, -6.2% to -0.2%).

**Golden note:** Heterogeneous treatment effects — varies by subgroup.

**Heterogeneous treatment effects of metformin on risk of dementia in patients with type 2 diabetes: A longitudinal observational study.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2023. Types: Observational Study; Journal Article; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> INTRODUCTION: Little is known about the heterogeneous treatment effects of metformin on dementia risk in people with type 2 diabetes (T2D). METHODS: Participants (≥ 50 years) with T2D and normal cognition at baseline were identified from the National Alzheimer's Coordinating Center database (2005-2021). We applied a doubly robust learning approach to estimate risk differences (RD) with a 95% confidence interval (CI) for dementia risk between metformin use and no use in the overall population and subgroups identified through a decision tree model. RESULTS: Among 1393 participants, 104 developed dementia over a 4-year median follow-up. Metformin was significantly associated with a lower risk of dementia in the overall population (RD, -3.2%; 95% CI, -6.2% to -0.2%). We identified four subgroups with varied risks for dementia, defined by neuropsychiatric disorders, non-steroidal anti-inflammatory drugs, and antidepressant use. DISCUSSION: Metformin use was significantly associated with a lower risk of dementia in individuals with T2D, with significant variability among subgroups.

---

### PMID 40017057 — current stance: `inconclusive`

**Stance justification:** > Metformin (n = 999,349, RR = 0.94[0.79, 1.13], I2 = 98.4%), sulfonylureas (RR = 0.98[0.78, 1.22], I2 = 83.3%), dipeptidyl peptidase-IV inhibitors (DPP-1V) (n = 192,802, RR = 0.86[0.65, 1.15], I2 = 92.9%) and insulin (n = 571,274, RR = 1.09[0.95, 1.25], I2 = 94.8%) were not.

**Golden note:** Meta diabetes meds vs cognition — mixed by drug.

**Effect of diabetes medications on the risk of developing dementia, mild cognitive impairment, or cognitive decline: A systematic review and meta-analysis.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> Background: Diabetes is a risk factor for dementia, but we do not know whether specific diabetes medications ameliorate this risk. Objective: To systematically review and meta-analyze such medication's effect on the risk of developing dementia, mild cognitive impairment (MCI), or cognitive decline. Methods: We searched three databases until 21 November 2023. We included randomized controlled trials (RCT), cohort, and case-control studies assessing association between antidiabetic medication and future dementia, MCI, or cognitive decline. We meta-analyzed studies separately for individual drug classes and their comparators (no medication, placebo, or another drug). We appraised study quality using the Newcastle-Ottawa Scale and Physiotherapy Evidence Database Scale. Results: 42 studies fulfilled inclusion criteria. Glucagon-like peptide-1 receptor agonists (GLP-1 RA) versus placebo reduced dementia risk by 53% in three RCTs (n = 15,820, RR = 0.47[0.25, 0.86]) and 27% in three case-control studies (n = 312,856, RR = 0.73[0.54, 0.99], I2 = 96%). Repaglinide was superior to glibenclamide by 0.8 points on the Mini-Mental State Examination scale in another RCT. Meta-analysis of seven longitudinal studies showed glitazones (n = 1,081,519, RR = 0.78[0.76, 0.81], I2 = 0%) were associated with reduced dementia risk. Metformin (n = 999,349, RR = 0.94[0.79, 1.13], I2 = 98.4%), sulfonylureas (RR = 0.98[0.78, 1.22], I2 = 83.3%), dipeptidyl peptidase-IV inhibitors (DPP-1V) (n = 192,802, RR = 0.86[0.65, 1.15], I2 = 92.9%) and insulin (n = 571,274, RR = 1.09[0.95, 1.25], I2 = 94.8%) were not. Most studies were observational and limited by confounding by indication. Conclusions: In people with diabetes, RCTs consistently showed GLP-RAs reduce future dementia risk. Glitazones consistently showed protective effects, without heterogeneity, suggesting potential generalizability of these results. Metformin, sulfonylureas, insulin, and DPP-1V studies had inconsistent findings. If information is available future studies should consider dosage, severity, and duration.

---

### PMID 33935082 — current stance: `inconclusive`

**Stance justification:** > Dual therapy with metformin (Met) + dipeptidyl peptidase-4 inhibitor (DPP-4i), Met + thiazolidinedione (TZD), and sulfonylurea (SU) + thiazolidinediones (TZD) were significantly associated with all-cause dementia (HR = 0.904, 0.804, and 0.962, respectively) and VaD (HR = 0.865, 0.725, and 0.911, respectively), compared with Met + SU.

**Golden note:** Real-world second-line meds — drug-class differences.

**The Association Between Second-Line Oral Antihyperglycemic Medication on Types of Dementia in Type 2 Diabetes: A Nationwide Real-World Longitudinal Study.**

*Journal of Alzheimer's disease : JAD*, 2021. Types: Journal Article; Observational Study

> BACKGROUND: There are few reports that evaluated the association between various types of dementia and dual oral therapy with antihyperglycemic medication. OBJECTIVE: The goal of this study was to investigate the association between treatment of dual antihyperglycemic medication and dementia subclass in type 2 diabetes mellitus using the Korean National Health Insurance System. METHODS: This study included 701,193 individuals with diabetes prescribed dual oral therapy between 2009 and 2012 from the Korean National Health Insurance Service Database, which were tracked until 2017. All-cause, Alzheimer's (AD) and vascular dementia (VaD) were investigated by dual oral therapy. Adjustments were made for age, sex, income, diabetes duration, hypertension, dyslipidemia, smoking, drinking, exercise, body mass index, glucose level, and estimated glomerular filtration rate. RESULTS: Dual therapy with metformin (Met) + dipeptidyl peptidase-4 inhibitor (DPP-4i), Met + thiazolidinedione (TZD), and sulfonylurea (SU) + thiazolidinediones (TZD) were significantly associated with all-cause dementia (HR = 0.904, 0.804, and 0.962, respectively) and VaD (HR = 0.865, 0.725, and 0.911, respectively), compared with Met + SU. Met + DPP-4i and Met + TZD were associated with significantly lower risk of AD (HR = 0.922 and 0.812), compared with Met + SU. Dual therapy with TZD was associated with a significantly lower risk of all-cause dementia, AD, and VaD than nonusers of TZD (HR = 0.918, 0.925 and 0.859, respectively). CONCLUSION: Adding TZD or DPP-4i instead of SU as second-line anti-diabetic treatment may be considered for delaying or preventing dementia. Also, TZD users relative to TZD non-users on dual oral therapy were significantly associated with lower risk of various types of dementia.

---

### PMID 38160357 — current stance: `inconclusive`

**Stance justification:** > Our pilot study is the first to investigate the effect of metformin on plasma and CSF proteins in non-diabetic patients with MCI and positive AD biomarkers and identifies several candidate plasma biomarkers for future clinical trials after confirmatory studies.

**Golden note:** Metformin in non-diabetic MCI — biomarker study, no clinical primary.

**Effect of Metformin on Plasma and Cerebrospinal Fluid Biomarkers in Non-Diabetic Older Adults with Mild Cognitive Impairment Related to Alzheimer's Disease.**

*Journal of Alzheimer's disease : JAD*, 2024. Types: Journal Article; Research Support, Non-U.S. Gov't; Randomized Controlled Trial; Research Support, N.I.H., Extramural

> BACKGROUND: Alzheimer's disease (AD) is a complicated condition involving multiple metabolic and immunologic pathophysiological processes that can occur with the hallmark pathologies of amyloid-β, tau, and neurodegeneration. Metformin, an anti-diabetes drug, targets several of these disease processes in in vitro and animal studies. However, the effects of metformin on human cerebrospinal fluid (CSF) and plasma proteins as potential biomarkers of treatment remain unexplored. OBJECTIVE: Using proteomics data from a metformin clinical trial, identify the impact of metformin on plasma and CSF proteins. METHODS: We analyzed plasma and CSF proteomics data collected previously (ClinicalTrials.gov identifier: NCT01965756, conducted between 2013 and 2015), and conduced bioinformatics analyses to compare the plasma and CSF protein levels after 8 weeks of metformin or placebo use to their baseline levels in 20 non-diabetic patients with mild cognitive impairment (MCI) and positive AD biomarkers participants. RESULTS: 50 proteins were significantly (unadjusted p < 0.05) altered in plasma and 26 in CSF after 8 weeks of metformin use, with 7 proteins in common (AZU1, CASP-3, CCL11, CCL20, IL32, PRTN3, and REG1A). The correlation between changes in plasma and CSF levels of these 7 proteins after metformin use relative to baseline levels was high (r = 0.98). The proteins also demonstrated temporal stability. CONCLUSIONS: Our pilot study is the first to investigate the effect of metformin on plasma and CSF proteins in non-diabetic patients with MCI and positive AD biomarkers and identifies several candidate plasma biomarkers for future clinical trials after confirmatory studies.

---

### PMID 38705542 — current stance: `inconclusive`

**Stance justification:** > Dementia and AD risks were significantly lower with metformin and sodium glucose co-transporter-2 inhibitors (SGLT2i). Metformin displayed the lowest risk of dementia across diverse antidiabetics, whereas α-glucosidase inhibitors demonstrated the highest risk.

**Golden note:** Bayesian network meta — different antidiabetic classes, mixed.

**Risk of Dementia and Alzheimer's Disease Associated With Antidiabetics: A Bayesian Network Meta-Analysis.**

*American journal of preventive medicine*, 2024. Types: Journal Article; Systematic Review; Research Support, Non-U.S. Gov't; Network Meta-Analysis

> INTRODUCTION: Dementia risk is substantially elevated in patients with diabetes. However, evidence on dementia risk associated with various antidiabetic regimens is still limited. This study aims to comprehensively investigate the risk of dementia and Alzheimer's disease (AD) associated with various antidiabetic classes. METHODS: Cochrane Central Register of Controlled Trials, Embase, MEDLINE (PubMed), and Scopus were searched from inception to March 2024 (PROSPERO CRD 42022365927). Observational studies investigating dementia and AD incidences after antidiabetic initiation were identified. Bayesian network meta-analysis was performed to determine dementia and AD risks associated with antidiabetics. Preferred Reporting Items for Systematic Reviews-Network Meta-Analyses (PRISMA-NMA) guidelines were followed. Statistical analysis was performed and updated in November 2023 and March 2024, respectively. RESULTS: A total of 1,565,245 patients from 16 studies were included. Dementia and AD risks were significantly lower with metformin and sodium glucose co-transporter-2 inhibitors (SGLT2i). Metformin displayed the lowest risk of dementia across diverse antidiabetics, whereas α-glucosidase inhibitors demonstrated the highest risk. SGLT2i exhibited the lowest dementia risk across second-line antidiabetics. Dementia risk was significantly higher with dipeptidyl peptidase-4 inhibitor (DPP4i), metformin, sulfonylureas, and thiazolidinediones (TZD) compared to SGLT2i in the elderly (≥75 years). Dementia risk associated with metformin was substantially lower, regardless of diabetic complication status or baseline A1C. DISCUSSION: Metformin and SGLT2i demonstrated lower dementia risk than other antidiabetic classes. Patient-specific factors may affect this relationship and cautious interpretation is warranted as metformin is typically initiated at an earlier stage with fewer complications. Hence, further large-scaled clinical trials are required.

---

### PMID 38279266 — current stance: `inconclusive`

**Stance justification:** > Differences in sample power, intervention, patients enrolled, assessment, and measure of outcomes prevents generalization of results.

**Golden note:** Autophagy inducers including metformin — broad, indirect.

**Exploitation of Autophagy Inducers in the Management of Dementia: A Systematic Review.**

*International journal of molecular sciences*, 2024. Types: Systematic Review; Journal Article

> The social burden of dementia is remarkable since it affects some 57.4 million people all over the world. Impairment of autophagy in age-related diseases, such as dementia, deserves deep investigation for the detection of novel disease-modifying approaches. Several drugs belonging to different classes were suggested to be effective in managing Alzheimer's disease (AD) by means of autophagy induction. Useful autophagy inducers in AD should be endowed with a direct, measurable effect on autophagy, have a safe tolerability profile, and have the capability to cross the blood-brain barrier, at least with poor penetration. According to the PRISMA 2020 recommendations, we propose here a systematic review to appraise the measurable effectiveness of autophagy inducers in the improvement of cognitive decline and neuropsychiatric symptoms in clinical trials and retrospective studies. The systematic search retrieved 3067 records, 10 of which met the eligibility criteria. The outcomes most influenced by the treatment were cognition and executive functioning, pointing at a role for metformin, resveratrol, masitinib and TPI-287, with an overall tolerable safety profile. Differences in sample power, intervention, patients enrolled, assessment, and measure of outcomes prevents generalization of results. Moreover, the domain of behavioral symptoms was found to be less investigated, thus prompting new prospective studies with homogeneous design. PROSPERO registration: CRD42023393456.

---

### PMID 37968954 — current stance: `inconclusive`

**Stance justification:** > The results of clinical studies on the use of metformin in AD are limited and contradictory.

**Golden note:** Antidiabetic-AD systematic review (Russian).

**[The role of antidiabetic drugs in the treatment of Alzheimer's disease: systematic review].**

*Problemy endokrinologii*, 2023. Types: Systematic Review; English Abstract; Journal Article

> Recent studies show that Alzheimer's disease (AD) has many common links with conditions associated with insulin resistance, including neuroinflammation, impaired insulin signaling, oxidative stress, mitochondrial dysfunction and metabolic syndrome. The authors conducted an electronic search for publications in the PubMed/MEDLINE and Google Scholar databases using the keywords "amyloid beta", "Alzheimer type-3-diabetes", "intranasal insulin", "metformin", "type 2 diabetes mellitus", "incretins" and "PPARy agonists». A systematic literature search was conducted among studies published between 2005 and 2022. The authors used the following inclusion criteria: 1) Subjects who received therapy for AD and/or DM2, if the expected result concerned the risk of cognitive decline or the development of dementia; 2) The age of the study participants is &gt; 50 years; 3) The type of studies included in this review were randomized clinical trials, population-based observational studies or case-control studies, prospective cohort studies, as well as reviews and meta-analyses; 4) The included articles were written in English. In recent years, there has been considerable interest in identifying the mechanisms of action of antidiabetic drugs and their potential use in AD. Human studies involving patients with mild cognitive impairment and Alzheimer's disease have shown that the administration of certain antidiabetic drugs, such as intranasal insulin, metformin, incretins and thiazolidinediones, can improve cognitive function and memory. The purpose of this study is to evaluate the effectiveness of antidiabetic drugs in the treatment of AD. According to the results of the study, metformin, intranasal insulin, thiazolidinediones and incretins showed a positive effect both in humans and in animal models. Recent studies show that thiazolidinediones can activate pathways in the brain that are regulated by IGF-1; however, rosiglitazone may pose a significant risk of side effects. The results of clinical studies on the use of metformin in AD are limited and contradictory.

---

### PMID 39871536 — current stance: `inconclusive`

**Stance justification:** > However, the inconsistency and low quality of current evidence point toward the need for accurate research to elucidate whether metformin's cognitive effects are protective, neutral, or context-dependent based on patient profiles.

**Golden note:** Umbrella review — explicitly notes contradictory results.

**Metformin and Cognitive Performance in Patients With Type 2 Diabetes: An Umbrella Review.**

*Neuropsychopharmacology reports*, 2025. Types: Journal Article; Systematic Review

> Contradictory results for the association between metformin intake and changes in cognitive function have been reported. We attempted to overview systematic reviews and meta-analyses showing the role of metformin, as mono or combination therapy, in cognitive performance alterations among patients with type 2 diabetes mellitus (T2DM) and to determine the quality of the evidence as well. To find the English-written reviews, a literature search was conducted on PubMed, Web of Science, Scopus, Cochrane Library, Trip, and Google Scholar by May 1, 2023. The literature search unearthed 2672 records, 10 of which were included in the study. Metformin may provide cognitive benefits for patients with type 2 diabetes, as evidence suggests potential improvements in memory and a reduced risk of neurodegenerative diseases. Even though the Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-Cog) score alterations correspond to raising concerns about cognitive decline, Mini-Mental State Examination (MMSE) and selective reminding test (SRT) score improvements support metformin's role in improving specific cognitive domains. As such, metformin may exert differential impacts on various aspects of cognitive performance in these patients. However, the inconsistency and low quality of current evidence point toward the need for accurate research to elucidate whether metformin's cognitive effects are protective, neutral, or context-dependent based on patient profiles.

---

### PMID 40695613 — current stance: `contradicts`

**Stance justification:** > GLP-1 RAs were more effective than metformin in reducing the risk of dementia-especially AD and non-vascular types-highlighting their potential as a preferred first-line treatment in T2DM.

**Golden note:** GLP-1 vs metformin — GLP-1 better; implies metformin not optimal head-to-head.

**Evaluating GLP-1 receptor agonists versus metformin as first-line therapy for reducing dementia risk in type 2 diabetes.**

*BMJ open diabetes research & care*, 2025. Types: Journal Article; Comparative Study

> INTRODUCTION: No direct comparisons have evaluated glucagon-like peptide-1 receptor agonists (GLP-1 RAs) versus metformin as first-line antidiabetic therapy for preventing dementia in patients with type 2 diabetes mellitus (T2DM). This study aimed to assess the comparative effectiveness of GLP-1 RAs and metformin in reducing dementia risk. RESEARCH DESIGN AND METHODS: This retrospective cohort study used data from a global health research network between 2004 and 2024. Patients with T2DM initiating GLP-1 RAs or metformin as first-line monotherapy were included. Propensity score matching was employed to balance baseline characteristics. Dementia incidence was analyzed using Cox proportional hazards models, with sensitivity analyses to confirm robustness. RESULTS: Among 87,229 matched patients per cohort, GLP-1 RA use was associated with a significantly lower risk of overall dementia (adjusted HR (AHR) 0.90; 95% CI 0.85 to 0.95), Alzheimer's disease (AD) (AHR 0.88; 95% CI 0.83 to 0.94), and non-vascular dementias (non-VaDs) (AHR 0.75; 95% CI 0.70 to 0.81) compared with metformin. No significant difference was observed for VaD. Subgroup analyses showed consistent benefit across age and sex, with the strongest effect among older adults and females. CONCLUSIONS: GLP-1 RAs were more effective than metformin in reducing the risk of dementia-especially AD and non-vascular types-highlighting their potential as a preferred first-line treatment in T2DM. Further randomized trials are warranted to validate these findings.

---

### PMID 40268162 — current stance: `inconclusive`

**Stance justification:** > SGLT2is significantly reduced dementia risk and mortality compared to metformin in T2D patients.

**Golden note:** SGLT2 vs metformin comparison — both effective, no clear winner.

**Comparative study of SGLT2 inhibitors and metformin: Evaluating first-line therapies for dementia prevention in type 2 diabetes.**

*Diabetes & metabolism*, 2025. Types: Journal Article; Comparative Study

> BACKGROUND: - Type 2 diabetes (T2D) increases the risk of dementia by 1.5 to 2.5 times. Sodium-glucose cotransporter 2 inhibitors (SGLT2is) and metformin, widely used antidiabetic therapies, have demonstrated potential neuroprotective effects. Their comparative effectiveness in dementia prevention remains unknown. METHODS: - This retrospective cohort study used the TriNetX global federated network, analyzing de-identified records from over 98 healthcare organizations. Adults with T2D initiating SGLT2i or metformin as first-line therapy were propensity score-matched (1:1). The primary outcome was overall dementia incidence, including vascular dementia, Alzheimer's disease, and other subtypes. Secondary outcomes included all-cause mortality. Time-to-event outcomes were assessed using Kaplan-Meier curves and Cox models. RESULTS: - Among 74,975 matched patients in each cohort, SGLT2i use was associated with a lower incidence of overall dementia: 2.7 % vs. 6.9 %: adjusted hazard ratio (aHR) 0.80 [95 % CI 0.76;0.84]. Reductions were observed in vascular dementia (0.8 % vs. 2.0 %; aHR 0.87), Alzheimer's dementia (1.1 % vs. 3.2 %; aHR, 0.76), and all-cause mortality (6.8 % vs. 15.4 %; aHR, 0.92). Benefits were pronounced in older adults, particularly those aged ≥80 years. CONCLUSIONS: - SGLT2is significantly reduced dementia risk and mortality compared to metformin in T2D patients. These findings suggest SGLT2is may offer superior neuroprotective benefits, underscoring their potential as a first-line therapy for T2D. Further randomized trials are needed to confirm these results.

---

### PMID 40023730 — current stance: `inconclusive`

**Stance justification:** > In terms of reducing Aβ deposition, metformin ranked highest in effectiveness, with the highest SUCRA score (84.6), followed by high-dose insulin detemir (SUCRA: 54.1).

**Golden note:** Network meta of antidiabetics in AD — mixed.

**Comparative efficacy and safety of antidiabetic agents in Alzheimer's disease: A network meta-analysis of randomized controlled trials.**

*The journal of prevention of Alzheimer's disease*, 2025. Types: Comparative Study; Journal Article; Network Meta-Analysis

> BACKGROUND: Alzheimer's disease (AD) is a progressive neurodegenerative disorder with limited treatment options. Emerging evidence suggests that antidiabetic agents may offer neuroprotective effects by targeting shared pathophysiological mechanisms such as insulin resistance and neuroinflammation. However, the comparative efficacy, and safety of these agents in the treatment of AD remain unclear. OBJECTIVES: This study aimed to systematically evaluate and compare the efficacy and safety of antidiabetic agents for improving cognitive outcomes, reducing amyloid-β (Aβ) deposition, and managing adverse effects in patients with AD, using a network meta-analysis of randomized controlled trials (RCTs). METHODS: A comprehensive literature search was conducted across multiple databases to identify RCTs examining the effects of antidiabetic agents in patients with AD. The primary outcomes included cognitive performance (e.g., MMSE scores), Aβ deposition (measured via CSF biomarkers), and safety/adverse effects. A network meta-analysis was performed to integrate direct and indirect evidence, ranking interventions using Surface Under the Cumulative Ranking (SUCRA) probabilities. Risk of bias was assessed using the Cochrane risk-of-bias tool. RESULTS: A total of 26 studies, involving 7,361 participants, were included in the analysis. The interventions evaluated included insulin detemir (both low-dose and high-dose), liraglutide, exenatide, metformin, and pioglitazone. Both low-dose insulin detemir (mean difference: 2.10, 95 % CI: 1.04 to 3.15), high-dose insulin detemir (mean difference: 1.40, 95 % CI: -0.07 to 2.88), exenatide (mean difference: 1.19, 95 % CI: 0.06 to 2.32), and metformin combined with exenatide (mean difference: 1.06, 95 % CI: -1.68 to 3.80) showed cognitive improvements compared to placebo. Among these, low-dose insulin detemir demonstrated the most significant improvement. In terms of reducing Aβ deposition, metformin ranked highest in effectiveness, with the highest SUCRA score (84.6), followed by high-dose insulin detemir (SUCRA: 54.1). Low-dose insulin detemir (SUCRA: 51.1) also demonstrated moderate efficacy. Low-dose insulin detemir showed some reduction in Aβ deposition (mean difference: -0.31, 95 % CI: -2.82 to 2.20), although statistical significance was limited. Liraglutide exhibited the highest rate of study treatment withdrawal (mean difference: 1.97, 95 % CI: -0.07 to 4.00), while pioglitazone demonstrated the lowest withdrawal rates (mean difference: 0.07, 95 % CI: -0.03 to 0.17). CONCLUSIONS: This network meta-analysis provides valuable insights into the comparative efficacy and safety of antidiabetic agents in AD. Low-dose insulin detemir demonstrated the most significant cognitive improvement and a moderate effect on reducing Aβ deposition. Metformin emerged as the most effective agent for reducing Aβ levels, though its effects on cognitive function were less pronounced. Safety profiles varied, with liraglutide associated with the highest rate of treatment withdrawals, while pioglitazone demonstrated the lowest incidence of treatment-related discontinuations. These findings support the potential use of antidiabetic agents, particularly insulin detemir, as a therapeutic option for AD, although further studies are needed to confirm their long-term benefits and safety.

---

### PMID 32719079 — current stance: `inconclusive`

**Stance justification:** > Metformin has failed to demonstrate a beneficial effect on NDs. In addition, it may increase the risk of PD development.

**Golden note:** Meta acknowledges inconsistent metformin findings.

**Association between metformin and neurodegenerative diseases of observational studies: systematic review and meta-analysis.**

*BMJ open diabetes research & care*, 2020. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND AND AIMS: Aging becomes a growing global concern with an increased risk of neurodegenerative diseases (NDs) that mainly consist of cognitive decline and Parkinson disease (PD). As the most commonly prescribed antidiabetic drug, metformin has been shown to have inconsistent roles in the incidence of NDs. We performed a systematic review and meta-analysis of observational studies to evaluate the effect of metformin exposure on onset of NDs. METHODS: The observational studies that investigated the associations between metformin and the incidence of NDs were searched in MEDLINE, Embase and Cochrane Library databases. A random-effect model was performed using STATA to calculate the combined ORs. RESULTS: In total, 23 comparisons out of 19 studies with 285 966 participants were included. Meta-analysis found there was no significant effect on incidence of all the subtypes of NDs with metformin exposure (OR 1.04, 95% CI 0.92 to 1.17). However, metformin monotherapy was associated with a significantly increased risk of PD incidence compared with non-metformin users or glitazone users (OR 1.66, 95% CI 1.14 to 2.42). CONCLUSION: Metformin has failed to demonstrate a beneficial effect on NDs. In addition, it may increase the risk of PD development. In light of current results, how metformin would impact NDs, especially the potential risk of PD, needs to be scrutinized. The underlying mechanisms are vital to achieve some more profound understanding on the regimen. TRIAL REGISTRATION NUMBER: CRD 42019133285.

---

### PMID 37869901 — current stance: `inconclusive`

**Stance justification:** > When studies examining metformin were divided by country, the only significant effect was for the United States. Moreover, the effect of metformin was significant in Western but not Eastern populations.

**Golden note:** Umbrella review on antidiabetic dementia risk — mixed.

**Diabetes, antidiabetic medications and risk of dementia: A systematic umbrella review and meta-analysis.**

*Diabetes, obesity & metabolism*, 2023. Types: Journal Article; Meta-Analysis; Systematic Review

> AIMS: The objective of this umbrella review and meta-analysis was to evaluate the effect of diabetes on risk of dementia, as well as the mitigating effect of antidiabetic treatments. MATERIALS AND METHODS: We conducted a systematic umbrella review on diabetes and its treatment, and a meta-analysis focusing on treatment. We searched MEDLINE/PubMed, Embase, PsycINFO, CINAHL and the Cochrane Library for systematic reviews and meta-analyses assessing the risk of cognitive decline/dementia in individuals with diabetes until 2 July 2023. We conducted random-effects meta-analyses to obtain risk ratios and 95% confidence intervals estimating the association of metformin, thiazolidinediones, pioglitazone, dipeptidyl peptidase-4 inhibitors, α-glucosidase inhibitors, meglitinides, insulin, sulphonylureas, glucagon-like peptide-1 receptor agonists (GLP1RAs) and sodium-glucose cotransporter-2 inhibitors (SGLT2is) with risk of dementia from cohort/case-control studies. The subgroups analysed included country and world region. Risk of bias was assessed with the AMSTAR tool and Newcastle-Ottawa Scale. RESULTS: We included 100 reviews and 27 cohort/case-control studies (N = 3 046 661). Metformin, thiazolidinediones, pioglitazone, GLP1RAs and SGLT2is were associated with significant reduction in risk of dementia. When studies examining metformin were divided by country, the only significant effect was for the United States. Moreover, the effect of metformin was significant in Western but not Eastern populations. No significant effect was observed for dipeptidyl peptidase-4 inhibitors, α-glucosidase inhibitors, or insulin, while meglitinides and sulphonylureas were associated with increased risk. CONCLUSIONS: Metformin, thiazolidinediones, pioglitazone, GLP1RAs and SGLT2is were associated with reduced risk of dementia. More longitudinal studies aimed at determining their relative benefit in different populations should be conducted.

---

### PMID 28538088 — current stance: `inconclusive`

**Stance justification:** > Metformin was associated with improved executive functioning, and trends suggested improvement in learning/memory and attention.

**Golden note:** Pilot RCT crossover in AD — exploratory.

**Effects of the Insulin Sensitizer Metformin in Alzheimer Disease: Pilot Data From a Randomized Placebo-controlled Crossover Study.**

*Alzheimer disease and associated disorders*, 2017. Types: Journal Article; Randomized Controlled Trial

> Epidemiological studies have identified a robust association between type II diabetes mellitus and Alzheimer disease (AD), and neurobiological studies have suggested the presence of central nervous system insulin resistance in individuals with AD. Given this association, we hypothesized that the central nervous system-penetrant insulin-sensitizing medication metformin would be beneficial as a disease-modifying and/or symptomatic therapy for AD, and conducted a placebo-controlled crossover study of its effects on cerebrospinal fluid (CSF), neuroimaging, and cognitive biomarkers. Twenty nondiabetic subjects with mild cognitive impairment or mild dementia due to AD were randomized to receive metformin then placebo for 8 weeks each or vice versa. CSF and neuroimaging (Arterial Spin Label MRI) data were collected for biomarker analyses, and cognitive testing was performed. Metformin was found to be safe, well-tolerated, and measureable in CSF at an average steady-state concentration of 95.6 ng/mL. Metformin was associated with improved executive functioning, and trends suggested improvement in learning/memory and attention. No significant changes in cerebral blood flow were observed, though post hoc completer analyses suggested an increase in orbitofrontal cerebral blood flow with metformin exposure. Further study of these findings is warranted.

---

### PMID 33609776 — current stance: `inconclusive`

**Stance justification:** > While the risk of bias was relatively low in human studies, this risk in animal studies was largely unclear. Overall, there is a clear lack of translation from animal models to human populations.

**Golden note:** Nutrient-sensing repurposed therapeutics review — broad, indirect.

**Targeting impaired nutrient sensing with repurposed therapeutics to prevent or treat age-related cognitive decline and dementia: A systematic review.**

*Ageing research reviews*, 2021. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: Dementia is a debilitating syndrome that significantly impacts individuals over the age of 65 years. There are currently no disease-modifying treatments for dementia. Impairment of nutrient sensing pathways has been implicated in the pathogenesis of dementia, and may offer a novel treatment approach for dementia. AIMS: This systematic review collates all available evidence for Food and Drug Administration (FDA)-approved therapeutics that modify nutrient sensing in the context of preventing cognitive decline or improving cognition in ageing, mild cognitive impairment (MCI), and dementia populations. METHODS: PubMed, Embase and Web of Science databases were searched using key search terms focusing on available therapeutics such as 'metformin', 'GLP1', 'insulin' and the dementias including 'Alzheimer's disease' and 'Parkinson's disease'. Articles were screened using Covidence systematic review software (Veritas Health Innovation, Melbourne, Australia). The risk of bias was assessed using the Cochrane Risk of Bias tool v 2.0 for human studies and SYRCLE's risk of bias tool for animal studies. RESULTS: Out of 2619 articles, 114 were included describing 31 different 'modulation of nutrient sensing pathway' therapeutics, 13 of which specifically were utilized in human interventional trials for normal ageing or dementia. Growth hormone secretagogues improved cognitive outcomes in human mild cognitive impairment, and potentially normal ageing populations. In animals, all investigated therapeutic classes exhibited some cognitive benefits in dementia models. While the risk of bias was relatively low in human studies, this risk in animal studies was largely unclear. CONCLUSIONS: Modulation of nutrient sensing pathway therapeutics, particularly growth hormone secretagogues, have the potential to improve cognitive outcomes. Overall, there is a clear lack of translation from animal models to human populations.

---

### PMID 41223766 — current stance: `inconclusive`

**Stance justification:** > Clinical data, while promising, remain limited and heterogeneous, mainly suggesting potential cognitive benefits.

**Golden note:** Metformin neurotransmission review — mechanistic, not clinical efficacy.

**Exploring the impact of metformin on the central nervous system and neurotransmission: A systematic review.**

*Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*, 2025. Types: Journal Article; Systematic Review

> BACKGROUND: Metformin, a well-established antidiabetic agent, has emerging neuroactive properties extending beyond glycemic control. Evidence suggests effects on neurotransmission, neuroprotection, and neuroinflammatory pathways, offering potential in neurodegenerative disorders. METHODS: Following PRISMA 2020 guidelines and PROSPERO registration (CRD420251105355), we systematically searched PubMed, Scopus, Web of Science, and Google Scholar (November 2024-July 2025) for in vivo and clinical studies in humans or animals reporting CNS-related outcomes. Two reviewers independently screened and extracted data; risk of bias was assessed with validated tools appropriate to study design. RESULTS: A total of 166 studies met inclusion criteria, including animal models, mechanistic experiments, and clinical observations. Metformin crosses the blood-brain barrier and modulates CNS pathways through anti-inflammatory and mitochondrial-supportive actions. Crucially, it regulates major neurotransmitter systems - serotonin, dopamine, glutamate, GABA, acetylcholine, and norepinephrine - restoring excitatory/inhibitory balance and enhancing synaptic plasticity. Most of the current evidence arises from preclinical studies, which consistently demonstrate neuroprotective and neuromodulatory effects of metformin in models of Alzheimer's disease, Parkinson's disease, stroke, and fragile X syndrome. Clinical data, while promising, remain limited and heterogeneous, mainly suggesting potential cognitive benefits. CONCLUSIONS: Metformin shows promise for repurposing in CNS disorders via direct neurotransmitter regulation alongside mitochondrial and anti-inflammatory effects. Given that the majority of available data are preclinical, translational studies and well-designed clinical trials are essential to establish efficacy, dosing, and target populations. These findings underscore the metabolic-neurological interface and suggest a shift from viewing metformin solely as a metabolic therapy to recognizing its neurotherapeutic potential. Long-term use warrants vitamin B12 monitoring.

---

