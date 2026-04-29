# Q5: Does aducanumab specifically benefit APOE4 carriers vs non-carriers in clinical outcomes?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=7 PMIDs.

**Current S/C/I**: 0 / 2 / 5
**Proposed S/C/I**: 0 / 3 / 4
**Net flips**: 1 (inconclusive → contradicts)

The original reviewer proposed 0 flips. On second pass, one entry meets the
strict bar for `contradicts`: a well-powered meta-analysis (n=13,003) that
explicitly concludes no differential efficacy by APOE4 carrier status. The
original review noted this exact issue but argued "the explicit 'no
difference' framing is properly `inconclusive`" — that reasoning is
inconsistent with the strict bar, which treats meta-analyses concluding
"evidence does not support" as `contradicts`.

Two additional entries are flagged for policy issue (a) — subgroup analyses
where the parent trial program had mixed results (EMERGE positive, ENGAGE
negative) — but they're already labeled `inconclusive`, so no flip needed.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|---|---|---|---|
| 40316479 | 2025 | inconclusive → **contradicts** | Meta-analysis (n=13,003 across 7 mAB + 9 AChEI trials) explicitly concludes "efficacy did not differ by disease stage, concomitant AD medications, or APOE4 carrier status." A well-powered meta-analysis with explicit null on APOE4-specific benefit is the textbook strict-bar `contradicts` case. The original reviewer flagged this exact issue but kept `inconclusive` on the framing argument, which doesn't survive the strict bar. |

---

## Borderline (not flipped, but flagged for cross-question policy decisions)

### Policy issue (a) — subgroup-positive in parent-null trial

- `39350371` (2024 Japanese subgroup of EMERGE/ENGAGE) — Currently
  `inconclusive`. The abstract reports "A treatment effect was observed in
  favor of aducanumab on the primary and secondary efficacy endpoints at
  Week 78 in EMERGE, but not ENGAGE." This is the parent-trial split
  (EMERGE+ / ENGAGE−); both trials were terminated early for futility. The
  paper is also stratified by ethnicity rather than APOE specifically. The
  current `inconclusive` label is consistent with the strict bar (it would
  be wrong to call this `supports` based on EMERGE-only positivity), but
  it's an instance of the recurring policy question across the golden set
  — flag, don't flip.
- `40545559` (2025 EMERGE re-analysis) — Currently `inconclusive`. Reports
  positive findings within EMERGE only (the trial that hit), with
  randomization stratified by APOE4 status. ENGAGE is not addressed in
  this re-analysis. Conclusion: "Aducanumab meaningfully slowed disease
  progression in participants with early AD." Currently `inconclusive`
  which is consistent with the strict bar (parent program's high-dose
  primary did not consistently hit; this is a one-trial re-analysis of
  the positive arm), but flag as another instance of policy issue (a).

## Confirmed (no change)

- `34807243` (EMERGE/ENGAGE ARIA — APOE4 carriers had *higher* ARIA-E rates,
  i.e. more harm not more benefit) — **contradicts ✓**
- `36038268` (ARIA meta — directional but non-sig APOE4 differential on
  ARIA, p=0.663 / 0.398) — **contradicts ✓**.
  *Note for future review:* the original golden note frames this as "APOE4
  a predisposing factor for adverse imaging events," but the meta found
  the APOE4 vs noncarrier difference was NOT statistically significant.
  An argument exists that this is `inconclusive` (null on APOE4
  differential), but as ARIA-not-benefit it doesn't strongly bear on the
  question either way. Conservatively kept at `contradicts` since
  directionally it indicates more harm in carriers.
- `37423541` (anti-Aβ phase 3 meta; APOE4 carriers have more ARIA, mixed
  cognitive across drugs) — **inconclusive ✓**
- `41109234` (2025 aducanumab neuropath case-control, n=5+12) —
  **inconclusive ✓** (too small for clean APOE4 carrier-vs-noncarrier
  comparison; all 5 treated participants carried at least one APOE ε4)

## Observations

- The narrow question + small candidate pool (7) keeps quality high. **This
  is what good golden-set entries look like.**
- Q5 demonstrates the value of narrowing — every paper directly addresses
  the question, no scope drift, no comparator-framing issues. The one
  proposed flip (40316479) is a strict-bar interpretation question, not
  a misclassification of the underlying paper's content.
- Policy issue (a) shows up twice (39350371, 40545559) but both already
  land at `inconclusive`, so it's only a flag for cross-question
  consistency, not a flip target here.

## Highest-confidence flips for this question

1. **40316479 inconclusive → contradicts** — well-powered (n=13,003)
   meta-analysis explicitly concluding no differential efficacy by APOE4
   carrier status. Strict-bar canonical `contradicts`.

## Cross-question policy issues observed in Q5

- **(a) Subgroup-positive in parent-null trial:** 2 instances (39350371,
  40545559). Both already `inconclusive`, so flagged not flipped.
- **(b) Preclinical-dominated review labeled `supports`:** Not observed
  in Q5 (no `supports` labels at all in this question).
- **(c) Missed primary with significant secondary:** Not observed in Q5.

---

## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

### Proposed new tags (Q5)

- `directional_nonsig` — `contradicts` (or `supports`) where the underlying
  test was directional only and did NOT reach statistical significance; the
  stance rests on direction of effect rather than a significant null/positive.
- `case_series_underpowered` — autopsy/neuropath/clinical case-series with
  n too small for any inferential claim (distinct from `pilot_positive`,
  which implies a positive efficacy signal).
- `tangential_stratification` — paper stratifies on a variable adjacent to
  but distinct from the question's stratifier (e.g., ethnicity when the
  question is APOE-specific), so it speaks only indirectly to the claim.

### Per-pmid tags

- `34807243` — `same_cohort_duplicate` (EMERGE/ENGAGE parent trials; same
  cohort as 39350371 and 40545559). Note: this paper is the canonical
  ARIA-by-APOE4 result, so within Q5 it's the primary representative of
  that cohort even though it's flagged as a duplicate.
- `36038268` — `directional_nonsig` (APOE4 vs noncarrier ARIA differential
  was directional but p=0.663 / p=0.398, i.e. not significant; the
  `contradicts` label rests on direction of harm, not a significant test;
  flagged in the existing Confirmed-section note).
- `39350371` — `same_cohort_duplicate`, `subgroup_positive`,
  `tangential_stratification` (Japanese subgroup of EMERGE/ENGAGE; EMERGE
  positive / ENGAGE negative; primary stratification is ethnicity, not
  APOE; parent program terminated for futility).
- `40545559` — `same_cohort_duplicate`, `subgroup_positive` (re-analysis
  of EMERGE only — the one parent trial that hit; ENGAGE not addressed).
- `41109234` — `case_series_underpowered` (n=5 treated, n=12 untreated
  autopsy controls; all 5 treated carried APOE ε4 so no carrier-vs-noncarrier
  comparison is possible).
- `37423541` — (none — clean systematic review/meta on anti-Aβ mAbs;
  reports mixed cognitive across drugs and elevated ARIA in ε4 carriers,
  the inconclusive label is canonical).
- `40316479` — (none — clean canonical example; well-powered meta n=13,003
  with explicit null on APOE4 differential efficacy; this is the
  strict-bar `contradicts` case).

All other pmids — untagged. (No untagged remainder; all 7 listed above.)

---

## Abstracts (n=7)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 34807243 — current stance: `contradicts`

**Evidence span:** > Incidence of ARIA-E was highest in aducanumab-treated participants who were apolipoprotein E ε4 allele carriers.

**Golden note:** EMERGE/ENGAGE ARIA analysis — APOE4 carriers had ~2x higher ARIA-E rates; ε4 carriers experience more harm not more benefit.

**Amyloid-Related Imaging Abnormalities in 2 Phase 3 Studies Evaluating Aducanumab in Patients With Early Alzheimer Disease.**

*JAMA neurology*, 2022. Types: Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> IMPORTANCE: The EMERGE and ENGAGE phase 3 randomized clinical trials of aducanumab provide a robust data set to characterize amyloid-related imaging abnormalities (ARIA) that occur with treatment with aducanumab, an amyloid-β (Aβ)-targeting monoclonal antibody, in patients with mild cognitive impairment due to Alzheimer disease or mild Alzheimer disease dementia. OBJECTIVE: To describe the radiographic and clinical characteristics of ARIA that occurred in EMERGE and ENGAGE. DESIGN, SETTING, AND PARTICIPANTS: Secondary analysis of data from the EMERGE and ENGAGE trials, which were 2 double-blind, placebo-controlled, parallel-group, phase 3 randomized clinical trials that compared low-dose and high-dose aducanumab treatment with placebo among participants at 348 sites across 20 countries. Enrollment occurred from August 2015 to July 2018, and the trials were terminated early (March 21, 2019) based on a futility analysis. The combined studies consisted of a total of 3285 participants with Alzheimer disease who received 1 or more doses of placebo (n = 1087) or aducanumab (n = 2198; 2752 total person-years of exposure) during the placebo-controlled period. Primary data analyses were performed from November 2019 to July 2020, with additional analyses performed through July 2021. INTERVENTIONS: Participants were randomly assigned 1:1:1 to high-dose or low-dose intravenous aducanumab or placebo once every 4 weeks. Dose titration was used as a risk-minimization strategy. MAIN OUTCOMES AND MEASURES: Brain magnetic resonance imaging was used to monitor patients for ARIA; associated symptoms were reported as adverse events. RESULTS: Of 3285 included participants, the mean (SD) age was 70.4 (7.45) years; 1706 participants (52%) were female, 2661 (81%) had mild cognitive impairment due to Alzheimer disease, and 1777 (54%) used symptomatic medications for Alzheimer disease. A total of 764 participants from EMERGE and 709 participants from ENGAGE were categorized as withdrawn before study completion, most often owing to early termination of the study by the sponsor. Unless otherwise specified, all results represent analyses from the 10-mg/kg group. During the placebo-controlled period, 425 of 1029 patients (41.3%) experienced ARIA, with serious cases occurring in 14 patients (1.4%). ARIA-edema (ARIA-E) was the most common adverse event (362 of 1029 [35.2%]), and 263 initial events (72.7%) occurred within the first 8 doses of aducanumab; 94 participants (26.0%) with an event exhibited symptoms. Common associated symptoms among 103 patients with symptomatic ARIA-E or ARIA-H were headache (48 [46.6%]), confusion (15 [14.6%]), dizziness (11 [10.7%]), and nausea (8 [7.8%]). Incidence of ARIA-E was highest in aducanumab-treated participants who were apolipoprotein E ε4 allele carriers. Most events (479 of 488 [98.2%]) among those with ARIA-E resolved radiographically; 404 of 488 (82.8%) resolved within 16 weeks. In the placebo group, 29 of 1076 participants (2.7%) had ARIA-E (apolipoprotein E ε4 carriers: 16 of 742 [2.2%]; noncarriers, 13 of 334 [3.9%]). ARIA-microhemorrhage and ARIA-superficial siderosis occurred in 197 participants (19.1%) and 151 participants (14.7%), respectively. CONCLUSIONS AND RELEVANCE: In this integrated safety data set from EMERGE and ENGAGE, the most common adverse event in the 10-mg/kg group was ARIA-E, which occurred in 362 of the 1029 patients (35.2%) in the 10-mg/kg group with at least 1 postbaseline MRI scan, with 94 patients (26.0%) experiencing associated symptoms. The most common associated symptom was headache. TRIAL REGISTRATIONS: ClinicalTrials.gov Identifiers: NCT02484547, NCT02477800.

---

### PMID 37423541 — current stance: `inconclusive`

**Evidence span:** > However, while cognitive effects were of small effect sizes, these drugs considerably increased risk of side effects such as Amyloid Related Imaging Abnormalities (ARIA), especially in APOE-ε4 carriers.

**Golden note:** Anti-Aβ phase 3 meta — discusses APOE genotype effects, mixed across drugs.

**Efficacy and safety of anti-amyloid-β monoclonal antibodies in current Alzheimer's disease phase III clinical trials: A systematic review and interactive web app-based meta-analysis.**

*Ageing research reviews*, 2023. Types: Systematic Review; Meta-Analysis; Journal Article; Research Support, Non-U.S. Gov't

> The risk-benefit profile of anti-Aβ monoclonal antibodies (mAbs) in Alzheimer's disease (AD) remains unclear, especially concerning their safety and overall effects on AD progression and cognitive function. Here, we investigated cognitive, biomarker and side effects of anti-Aβ mAbs in large phase III randomized placebo-controlled clinical trials (RCTs) in sporadic AD. The search was performed on Google Scholar, PubMed and ClinicalTrials.gov by applying Jadad score to evaluate the methodological quality of the reports. Studies were excluded if they scored < 3 on Jadad scale or if they analyzed less than 200 sporadic AD patients. We followed PRISMA guidelines and DerSimonian-Laird random-effects model in R. Primary outcomes were cognitive: AD Assessment Scale-Cognitive Subscale (ADAS-Cog), Mini Mental State Examination (MMSE) and Clinical Dementia Rating Scale-sum of Boxes (CDR-SB). Secondary and tertiary outcomes included biomarkers of Aβ and tau pathology, adverse events, and performance on Alzheimer's Disease Cooperative Study - Activities of Daily Living Scale. The meta-analysis included 14,980 patients in 14 studies and four mAbs: Bapineuzumab, Aducanumab, Solanezumab and Lecanemab. The results of this study suggest that anti-Aβ mAbs statistically improved cognitive and biomarker outcomes, particularly Aducanumab and Lecanemab. However, while cognitive effects were of small effect sizes, these drugs considerably increased risk of side effects such as Amyloid Related Imaging Abnormalities (ARIA), especially in APOE-ε4 carriers. Meta-regression revealed that higher (better) baseline MMSE score was associated with improved ADAS Cog and CDR-SB. In order to improve reproducibility and update the analysis in the future, we developed AlzMeta.app, web-based application freely available at https://alzmetaapp.shinyapps.io/alzmeta/.

---

### PMID 36038268 — current stance: `contradicts`

**Evidence span:** > In subgroup analysis according to ApoE-4 carrier status, the incidences of ARIA-E and ARIA-H were higher in the ApoE-4 carrier group than those in the ApoE-4 noncarrier group, but there was no statistical significance (ApoE-4 carrier vs noncarrier, ARIA-E: 8.6% vs 6.9%, p = 0.663, and ARIA-H: 10.5% vs 6.6%, p = 0.398).

**Golden note:** ARIA meta — APOE4 a predisposing factor for adverse imaging events, not a benefit modifier.

**Incidence of Amyloid-Related Imaging Abnormalities in Patients With Alzheimer Disease Treated With Anti-β-Amyloid Immunotherapy: A Meta-analysis.**

*Neurology*, 2022. Types: Meta-Analysis; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND AND OBJECTIVES: To assess the incidence of amyloid-related imaging abnormalities (ARIA) in clinical trials of anti-β-amyloid (Aβ) immunotherapy and compare the incidence among different agents and clinical characteristics to identify possible predisposing factors for ARIA. METHODS: The PubMed and Embase databases were searched for clinical trials of anti-Aβ immunotherapy published on or before January 12, 2022. Phase 2 or 3 randomized controlled trials reporting detailed data sufficient to assess the incidence of ARIA were selected. The pooled incidences of ARIA and subgroup analyses according to agent and ApoE-4 carrier status were calculated using the DerSimonian-Liard random-effects model. The proportion of symptomatic ARIA cases was also calculated. RESULTS: In total, 19 eligible studies, including 24 cohorts, were identified and 9,429 patients were analyzed. The overall pooled incidence of ARIA-effusion (E) and ARIA-hemorrhage (H) was 6.5% and 7.8%, respectively. In the subgroup analysis, the incidence of ARIA was different according to the anti-Aβ immunotherapy agent. The cohorts treated with aducanumab had a significantly higher incidence of ARIA-E and ARIA-H (30.7% and 30.0%, respectively; both p < 0.001) compared with cohorts from other drugs. In subgroup analysis according to ApoE-4 carrier status, the incidences of ARIA-E and ARIA-H were higher in the ApoE-4 carrier group than those in the ApoE-4 noncarrier group, but there was no statistical significance (ApoE-4 carrier vs noncarrier, ARIA-E: 8.6% vs 6.9%, p = 0.663, and ARIA-H: 10.5% vs 6.6%, p = 0.398). The pooled proportion of asymptomatic ARIA, detected by routine scheduled MRI surveillances, was 80.4%. DISCUSSION: The overall incidences of ARIA-E and ARIA-H were 6.5% and 7.8%, respectively, and the pooled proportion of asymptomatic ARIA was 80.4%. The cohorts treated with aducanumab showed a significantly higher incidence of ARIA-E and ARIA-H (30.7% and 30.0%) compared with other drugs.

---

### PMID 40316479 — current stance: `inconclusive` [FLIP from inconclusive → contradicts]

**Evidence span:** > Further analysis of mABs indicated that their efficacy did not differ by disease stage, concomitant AD medications, or APOE4 carrier status.

**Golden note:** Anti-amyloid vs AChEI by genotype/stage — mixed across agents.

**Flip rationale:** Conclusion explicitly states "efficacy did not differ
by disease stage, concomitant AD medications, or APOE4 carrier status"
across n=13,003 in the meta. A well-powered meta-analysis with explicit
null on APOE4-specific differential benefit is the strict-bar
`contradicts` case. The fact that lecanemab/donanemab/aducanumab as a
class showed *some* slowing of decline vs. placebo is a different
question — the question here is whether ε4 carriers benefit *more*, and
the answer in this paper is explicitly no.

**The efficacy and safety of anti-amyloid monoclonal antibody versus acetylcholinesterase inhibitor with an in-depth analysis across genotypes and disease stages: a systematic review and meta-analysis.**

*The journal of prevention of Alzheimer's disease*, 2025. Types: Comparative Study; Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: To date, studies have not compared the efficacy and safety of monoclonal antibodies (mABs) with acetylcholinesterase inhibitors (AChEIs). METHODS: Five electronic databases were systemic searched from inception to 10 November 2024 for double-blinded randomized controlled trial (RCT) of patients diagnosed with MCI or mild AD treated with mABs or AChEIs for at least 6 months. The primary outcome was change in cognitive function, measured by the Alzheimer's Disease Assessment Scale-cognitive subscale 14-item (ADAS-Cog) and Clinical Dementia Rating Scale-Sum of Boxes (CDR-SOB). The secondary outcomes were acceptability, tolerability, serious adverse events (SAE), and all -cause mortality. For mABs, amyloid-related imaging abnormalities-edema (ARIA-E), and amyloid-related imaging abnormalities-hemorrhage (ARIA-H) were also assessed. Subgroup analyses included (i) MCI versus mild AD; (ii) with versus without concomitant AD medications; and (iii) Apolipoprotein E (ApoE4) carriers versus non-carriers. Data were pooled using a random effects model within a Bayesian framework. RESULTS: There were 8010 participants (mean age: 71.5 years) across seven mAB trials, and 4993 participants (mean age:70.7 years) in nine AChEI trials. When compared to placebo, only mABs, not AChEIs, were associated with a slower progression of cognitive decline on CDR-SOB (mean difference -0.41 (95 % credible interval -0.61 to -0.22); minimally important difference (MID) -1) and ADAS-Cog (-1.35 (-2.36 to -0.36), MID -2); however, these benefits of mABs did not reach MID across the two cognitive measurements. Besides, mABs were associated with a slower progression of cognitive decline on CDR-SOB (-0.30 (-0.60 to -0.001)) than AChEIs, although mABs and AChEIs did not differ across safety outcomes, including acceptability, tolerability, SAE, and all-cause mortality. Further analysis of mABs indicated that their efficacy did not differ by disease stage, concomitant AD medications, or APOE4 carrier status. However, APOE4 homozygotes carriers were associated with a 5.53-fold (2.48 to 13.07) increased odds of developing ARIA-E compared to non-carriers. Finally, lecanemab demonstrated relatively better efficacy and a more favorable profile on ARIA-E compared to aducanumab and donanemab. CONCLUSIONS: mABs were associated with a slower progression of cognitive decline than AChEIs; however, this effect did not reach the MID. The incidence of ARIA-E with mABs was associated with APOE4 carrier status and was not indicative of treatment efficacy.

---

### PMID 41109234 — current stance: `inconclusive`

**Evidence span:** > Aducanumab-treated participants comprised four males and one female, all carrying at least one APOE ∊4 allele, with two harbouring a PSEN1 mutation.

**Golden note:** Aducanumab neuropath case-control retrospective — small, no clean APOE4 benefit comparison.

**Neuropathological changes and amyloid-related imaging abnormalities in Alzheimer's disease treated with aducanumab versus untreated: a retrospective case-control study.**

*The Lancet. Neurology*, 2025. Types: Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial

> BACKGROUND: Understanding the neuropathological effects of amyloid β (Aβ)-targeting therapies and amyloid-related imaging abnormalities (ARIA) in Alzheimer's disease is critical for optimising treatment efficacy and patient outcomes. Comparing Aβ PET imaging with neuropathological assessments provides context for evaluating the extent of Aβ clearance and interpreting in-vivo biomarkers. We aimed to assess clinicopathological changes and ARIA-related effects in aducanumab-treated versus untreated Alzheimer's disease. METHODS: This retrospective case-control study included five aducanumab-treated participants from clinical trials conducted at the Mayo Clinic (2016-21) who underwent autopsy (2020-23). Treated participants were matched by autosomal dominant Alzheimer's disease mutation or APOE genotype, age at cognitive symptom onset, and sex to 12 untreated participants from the Mayo Clinic Alzheimer's Disease Research Center and Mayo Clinic Study of Aging cohorts in the Mayo Clinic brain bank (Jacksonville, FL, USA). Cognitive, imaging, and neuropathological outcomes were compared using descriptive analyses and Mann-Whitney U tests. FINDINGS: Aducanumab-treated participants comprised four males and one female, all carrying at least one APOE ∊4 allele, with two harbouring a PSEN1 mutation. Cumulative dosages of aducanumab ranged from 5 mg/kg to 241 mg/kg; all participants cognitively declined during treatment, and two exhibited ARIA. Reductions in [18F]florbetapir PET Centiloid values ranged from -6% to -81% compared with baseline. Treatment-to-death intervals ranged from 5 months to 41 months. Neuropathological analyses revealed clearance of Aβaa1-8 and Aβ42 localised to cortical layer I in treated participants, with no significant clearance in deeper cortical layers. Regions corresponding to ARIA on MRI showed microinfarcts with haemosiderin, complement activation, and CD68-positive vessel walls originating from Aβ-laden leptomeningeal and penetrating vessels. INTERPRETATION: Disproportionate Aβ clearance and ARIA-associated neuropathology localised to superficial cortical layers suggest a distinctive pattern of target engagement by aducanumab. These findings inform understanding and monitoring of similar Aβ-targeting therapies. FUNDING: Alzheimer Nederland, National Institute on Aging, and Alzheimer's Association.

---

### PMID 39350371 — current stance: `inconclusive`

**Evidence span:** > A treatment effect was observed in favor of aducanumab on the primary and secondary efficacy endpoints at Week 78 in EMERGE, but not ENGAGE.

**Golden note:** Japanese subgroup of EMERGE/ENGAGE — by ethnicity not specifically APOE-stratified.

**Japanese Subgroup Analyses from EMERGE and ENGAGE, Phase 3 Clinical Trials of Aducanumab in Patients with Early Alzheimer's Disease.**

*The journal of prevention of Alzheimer's disease*, 2024. Types: Journal Article; Randomized Controlled Trial; Clinical Trial, Phase III

> BACKGROUND: Global prevalence and incidence of dementia continue to rise at a rapid rate. There is a need for new Alzheimer's disease (AD) treatments globally. Aducanumab is a human monoclonal antibody that selectively targets aggregated soluble amyloid beta oligomers and insoluble amyloid beta fibrils. In June 2021, aducanumab was approved by the US Food and Drug Administration for the treatment of AD under the accelerated approval pathway. OBJECTIVES: We evaluated the efficacy, safety, biomarker and pharmacokinetics (PK) of aducanumab in Japanese subgroups in EMERGE and ENGAGE studies. DESIGN: EMERGE and ENGAGE were two randomized, double-blind, placebo-controlled, global, phase 3 studies of aducanumab in patients with early AD (mild cognitive impairment due to AD or mild AD dementia). SETTING: These studies involved 348 sites in 20 countries. PARTICIPANTS: Participants enrolled in Japan included 121 (7.4% of total 1638 in EMERGE) and 100 (6.1% of total 1647 in ENGAGE) patients (aged 50-85 years with confirmed amyloid pathology) who met clinical criteria for mild cognitive impairment due to AD or mild AD dementia. INTERVENTION: Participants were randomly assigned 1:1:1 to receive aducanumab low dose (3 or 6 mg/kg target dose), high dose (6 or 10 mg/kg target dose) or placebo via IV infusion once every 4 weeks over 76 weeks. MEASUREMENTS: The primary outcome measure was change from baseline to Week 78 on the Clinical Dementia Rating Sum of Boxes (CDR-SB), an integrated scale that assesses both function and cognition. Other measures included safety assessments; secondary and tertiary clinical outcomes that assessed cognition, function, and behavior; biomarker endpoints (amyloid PET and plasma p-tau181); serum PK profiles and immunogenicity. RESULTS: Results from the Japanese subgroup analyses were generally consistent with those of the overall study population across endpoints, while a lower mean body weight (kg) and a smaller proportion of ApoE ε4 carriers were observed in the Japanese subgroup population. A treatment effect was observed in favor of aducanumab on the primary and secondary efficacy endpoints at Week 78 in EMERGE, but not ENGAGE. The incidence and type of adverse events in the Japanese subgroups were generally comparable to those observed in the overall study population; amyloid related imaging abnormalities (ARIA) were common treatment-related adverse events that appeared to be related to the aducanumab dose. ARIA incidence was generally lower in the Japanese subgroup compared with the overall population. Consistent with the overall data set, a robust dose-dependent decrease in amyloid beta levels as assessed with amyloid-PET and plasma p-tau181 was observed. Serum PK profiles and immunogenicity of aducanumab in Japanese population were consistent with the non-Japanese population. CONCLUSION: Efficacy, safety, biomarker, and PK profiles of aducanumab were consistent between the Japanese subgroup and the overall population. A positive treatment effect of aducanumab on efficacy endpoints was observed in EMERGE, but not in ENGAGE.

---

### PMID 40545559 — current stance: `inconclusive`

**Evidence span:** > Across multiple analyses aducanumab slowed cognitive decline, prolonged functional independence, and attenuated behavioral symptoms in participants with early AD.

**Golden note:** EMERGE clinical-meaningfulness re-analysis — APOE-stratification not the focus.

**Evaluation of cognitive, functional, and behavioral effects observed in EMERGE, a phase 3 trial of aducanumab in people with early Alzheimer's disease.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2025. Types: Journal Article; Randomized Controlled Trial; Clinical Trial, Phase III

> INTRODUCTION: In EMERGE (NCT02484547), participants receiving aducanumab had significantly less progression versus placebo on all prespecified clinical endpoints at week 78. Here, we explicate the clinical meaningfulness of these treatment effects by analyzing item-level data and the persistence of treatment benefit. METHODS: Participants with early Alzheimer's disease (AD) were stratified by apolipoprotein E (APOE) ε4 status and randomized (1:1:1) to receive low- or high-dose aducanumab, or placebo. Prespecified principal component analyses (PCAs) per the Statistical Analysis Plan were followed by post hoc examination of individual domains/items across all five clinical endpoints. Progression analysis assessed reduction in clinical decline. RESULTS: High-dose aducanumab demonstrated clinically meaningful slowing of progression across clinical endpoints measuring cognition, daily function, and behavioral symptoms. Delay of progression over 18 months was consistent across measures; treatment effects increased over time. DISCUSSION: Across multiple analyses aducanumab slowed cognitive decline, prolonged functional independence, and attenuated behavioral symptoms in participants with early AD. These outcomes comprise the elements of a clinically meaningful response to treatment. HIGHLIGHTS: Endpoints in EMERGE assessed different aspects of cognition, daily function, and behavioral symptoms. Treatment benefits were observed across subdomains on all five clinical endpoints. Aducanumab meaningfully slowed disease progression in participants with early AD.

---

