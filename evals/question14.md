# Q14: Does lecanemab improve clinical outcomes in early or mild Alzheimer's disease?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=38 PMIDs (largest question in the corpus).

**Current S/C/I**: 19 / 1 / 18
**Proposed S/C/I**: 19 / 2 / 17
**Net flips**: 1 (the 2026 Cochrane review)

The current labeling for Q14 is largely accurate. CLARITY-AD met its
primary endpoint, multiple meta-analyses confirm a small but
statistically-significant effect, and most labeled-supports are
defensible. The single high-confidence flip is the **2026 Cochrane
review**, which explicitly characterizes the cognitive-function and
dementia-severity effects as **"trivial"** — and is currently labeled
`supports`. That's a mislabel.

The deeper question for Q14 isn't stance flips — it's **how to handle
the 7+ CLARITY-AD substudies that all count as separate `supports`
votes**, and the magnitude debate (statistically significant but below
clinical-meaningfulness threshold per several reviews).

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `41985900` | 2026 | **supports → contradicts** | 2026 Cochrane review of all amyloid-targeting mAbs (17 studies, 20,342 participants). Verbatim conclusions: *"The effect of amyloid-beta-targeting monoclonal antibodies on cognitive function and dementia severity at 18 months in people with mild cognitive impairment or mild dementia due to Alzheimer's disease is **trivial**, while on functional ability, it is **small at best**. ...**Successful removal of amyloid from the brain does not seem to be associated with clinically meaningful effects** in people with mild cognitive impairment or mild dementia due to Alzheimer's disease."* This is the canonical Cochrane "evidence does not support" finding and was sitting as `supports`. |

### Borderline — flagged for second review

| PMID | Year | Status | Notes |
|------|------|--------|-------|
| `33865446` | 2021 | **supports (keep, flagged)** | Phase 2b proof-of-concept. Verbatim: *"BAN2401-G000-201 **did not meet the 12-month primary endpoint**."* The 18-month Bayesian/frequentist secondaries were positive. Could → `inconclusive` under a strict primary-endpoint reading; defensible to keep `supports` because the 18-month data informed CLARITY-AD's design and the trial was a phase 2 dose-finder. |
| `38484213` | 2024 | **contradicts ✓** | Commentary "Lecanemab Questions" — critical opinion piece. Not RCT data. The label `contradicts` is a stretch (it's an opinion piece, not a primary contradicting finding). Could → `inconclusive` (commentary). |
| `41396015` | 2025 | **inconclusive (keep)** | Eastern China real-world n=190. Verbatim: *"Overall lecanemab exhibited a manageable short-term safety profile **with no measurable cognitive efficacy**."* Could → `contradicts` based on that direct quote, but the study is short-term and mostly safety/baseline-focused. Keep `inconclusive` but note the explicit "no measurable cognitive efficacy." |
| `36184326` | 2022 | **inconclusive ✓** | Anti-amyloid imm meta part 1. Verbatim: *"the data... confirm a **statistically significant** clinical effect on cognitive decline... However, this effect remains **below the previously established minimal clinically relevant values**."* Statistically positive, clinically borderline. Defensible as `inconclusive`. |
| `38730496` | 2024 | **inconclusive ✓** | Updated phase 3 safety report. Mostly safety/AE focus, no new efficacy claim. **inconclusive ✓** |

## Confirmed (no change)

- `36449413` (CLARITY-AD phase 3, n=1795) — **supports ✓** (primary endpoint met, sig CDR-SB difference)
- `36544184` (phase 2 OLE biomarker/cognitive) — **supports ✓** (substudy of `33865446`)
- `38253184` (NMA donanemab/lecanemab/aducanumab/lithium) — **inconclusive ✓** (defensible mixed-class NMA)
- `37874099` (CLARITY-AD QoL substudy) — **supports ✓** (defensible CLARITY substudy)
- `37902139` (lecanemab SR — efficacy in slowing decline) — **supports ✓**
- `37213538` (lecanemab safety/efficacy meta — beneficial) — **supports ✓**
- `39559868` (71-pt regional center descriptive) — **inconclusive ✓**
- `37295957` (commentary "incremental step or paradigm shift") — **inconclusive ✓**
- `36482412` (phase 2 consistency-of-results substudy) — **supports ✓**
- `38429615` (2024 NMA mAbs) — **supports ✓**
- `40189473` (CLARITY-AD Asian subgroup) — **supports ✓** (substudy)
- `39638097` (lecanemab in mild AD meta) — **supports ✓**
- `35320578` (ARIA-amyloid correlation methodology) — **inconclusive ✓**
- `37040116` (Bayesian re-analysis phase 2b) — **supports ✓** (substudy of `33865446`)
- `36336488` (anti-amyloid imm part 2 — implementation/ethics) — **inconclusive ✓**
- `40011174` (eligibility analysis descriptive) — **inconclusive ✓**
- `39432414` (anti-Aβ mAb SR — lecanemab effective) — **supports ✓**
- `38759015` (NMA early AD interventions) — **inconclusive ✓**
- `41355080` (CLARITY-AD OLE 36-month) — **supports ✓** (substudy)
- `40232258` (lecanemab safety/efficacy SR) — **supports ✓**
- `41070709` (China multicenter real-world) — **supports ✓**
- `40308765` (re-evaluation lecanemab/donanemab) — **supports ✓**
- `40386876` (rTMS vs anti-amyloid NMA) — **inconclusive ✓**
- `41322352` (symptomatic vs DMT comparative) — **inconclusive ✓**
- `39269842` (AE-as-unblinding meta) — **inconclusive ✓**
- `41160347` (US real-world utilization) — **inconclusive ✓**
- `41352683` (patient characteristics meta — subgroup) — **inconclusive ✓**
- `41428477` (effect-size comparison Souvenaid > lecanemab) — **inconclusive ✓**
- `41478817` (lecanemab safety meta RWE) — **inconclusive ✓**
- `41823189` (China multicenter real-world) — **supports ✓**
- `41581261` (regional center 2-yr safety-focused) — **inconclusive ✓**
- `41689888` (CLARITY-AD APOE non-carrier subgroup) — **supports ✓** (substudy)

## Cross-cutting issues

- **CLARITY-AD substudy proliferation**: `36449413` (parent), `37874099`
  (QoL), `40189473` (Asian subgroup), `41355080` (36-mo OLE),
  `41689888` (APOE subgroup), `38730496` (safety update). That's
  **6 PMIDs from one trial**, all counting separately as evidence
  votes. The Phase 2b parent (`33865446`) plus its substudies
  (`36544184`, `36482412`, `37040116`) adds 4 more. Together: 10/38
  PMIDs (~26%) come from 2 cohorts (Phase 2b and CLARITY-AD).
  This is the largest substudy concentration in the eval set.
- **Magnitude debate vs significance debate**: Several "inconclusive"
  labels (`36184326`, `41322352`, `41428477`, `38484213`) reflect a
  consistent critique that lecanemab's effect, while statistically
  significant, falls below standard minimal-clinically-important-difference
  thresholds. The **2026 Cochrane** (`41985900`) is the most
  authoritative version of this critique and should be `contradicts`
  under the strict bar.
- **Real-world studies stratify cleanly**: studies labeled `supports`
  (`41070709`, `41823189`) report cognitive improvement; studies labeled
  `inconclusive` (`41396015`, `41581261`) explicitly report "no
  measurable cognitive efficacy" or focus on safety. Reasonable
  stratification.

## Highest-confidence flips for this question

- `41985900` supports → contradicts — Cochrane 2026: "trivial" effect
  on cognitive function, "small at best" on functional ability, "does
  not seem to be associated with clinically meaningful effects."
  This is the only unambiguous flip in Q14.


---

## signal_types (annotation layer)

This layer annotates each pmid with one or more **signal_type tags** that
describe non-stance caveats about how the entry contributes to the
overall S/C/I tally. These are independent of the stance label — a
`supports` paper can still carry a `same_cohort_duplicate` tag that
matters for downstream weighting and UI filtering.

Q14 has the **highest concentration of same_cohort_duplicate tags in
the corpus**: 10/38 pmids (~26%) come from just 2 cohorts (CLARITY-AD
and the Phase 2b Study 201 / BAN2401-G000-201).

### Tag definitions used in Q14

- `same_cohort_duplicate` — paper reports on the same trial cohort as
  another paper in the corpus (substudy, OLE, subgroup, secondary
  outcome, safety update, regional analysis).
- `narrative_review` — review/commentary without primary data.
- `commentary` — opinion piece, not original data.
- `hedged_meta` — meta-analysis with statistically significant pooled
  effect but explicit caveat that it falls below clinical-meaningfulness
  thresholds.
- `subgroup_positive` — finding restricted to a subgroup of the parent
  trial (often without parent-trial primary failure here, since CLARITY-AD
  was positive — but the subgroup-only nature of the evidence still
  matters for weighting).
- `safety_only` — primary focus is safety/AE, no efficacy claim.
- `biomarker_only` — primary outcome is a biomarker (PET, plasma
  p-tau), not a clinical endpoint.
- `methodology_only` — methods/statistical paper, no new efficacy data.
- `uncontrolled_observational` — single-arm real-world cohort with no
  comparator group.
- `descriptive_utilization` — describes utilization patterns/eligibility,
  not efficacy.
- `comparator_only` — paper exists primarily to compare lecanemab
  against another intervention (rTMS, Souvenaid, lithium); does not
  speak to lecanemab vs placebo independently.
- `landmark_no_group_difference` — gap-period or natural-history finding
  in which the comparison of interest shows no separation (note: applied
  carefully here; CLARITY-AD core showed clear separation).
- `missed_primary_sig_secondary` — primary endpoint missed but secondaries
  positive.

### Per-pmid tags

| PMID | Year | Stance | signal_types |
|------|------|--------|--------------|
| `36449413` | 2022 | supports | (parent trial — no caveat tag; this is the canonical primary) |
| `33865446` | 2021 | supports | `missed_primary_sig_secondary` (12-mo primary missed; 18-mo Bayesian/frequentist secondaries positive) |
| `36544184` | 2022 | supports | `same_cohort_duplicate` (Phase 2b OLE, Study 201) |
| `38730496` | 2024 | inconclusive | `same_cohort_duplicate` (CLARITY-AD safety update), `safety_only` |
| `38253184` | 2024 | inconclusive | `comparator_only` (mixed-class NMA: donanemab/lecanemab/aducanumab/lithium) |
| `37874099` | 2023 | supports | `same_cohort_duplicate` (CLARITY-AD QoL substudy) |
| `36184326` | 2022 | inconclusive | `hedged_meta` ("statistically significant... below previously established minimal clinically relevant values") |
| `37902139` | 2023 | supports | `narrative_review` (SR of 3 RCTs, includes the CLARITY-AD primary) |
| `37213538` | 2023 | supports | `narrative_review` (SR/meta — pooled CLARITY-AD + Phase 2b) |
| `39559868` | 2024 | inconclusive | `uncontrolled_observational` (single-center n=71, no comparator), `safety_only` |
| `37295957` | 2023 | inconclusive | `commentary` (paradigm-shift framing piece) |
| `36482412` | 2022 | supports | `same_cohort_duplicate` (Phase 2b consistency-of-results substudy), `methodology_only` |
| `38429615` | 2024 | supports | `narrative_review` (NMA across 8 mAbs — lecanemab one of many; aducanumab ranked highest, not lecanemab) |
| `40189473` | 2025 | supports | `same_cohort_duplicate` (CLARITY-AD Asian regional subgroup), `subgroup_positive` |
| `39638097` | 2024 | supports | `narrative_review` (SR/meta — included Phase 2b + CLARITY-AD primarily) |
| `35320578` | 2022 | inconclusive | `methodology_only`, `biomarker_only` (ARIA-amyloid-clinical correlation methodology meta) |
| `37040116` | 2023 | supports | `same_cohort_duplicate` (Phase 2b Bayesian re-analysis), `methodology_only` |
| `36336488` | 2022 | inconclusive | `narrative_review` (implementation/ethics part 2), `descriptive_utilization` |
| `40011174` | 2025 | inconclusive | `descriptive_utilization` (eligibility analysis) |
| `39432414` | 2024 | supports | `narrative_review` (SR across multiple mAbs) |
| `38759015` | 2024 | inconclusive | `narrative_review` (broad NMA: 48 interventions; lecanemab one finding) |
| `41355080` | 2025 | supports | `same_cohort_duplicate` (CLARITY-AD 36-month OLE) |
| `38484213` | 2024 | contradicts | `commentary` (opinion piece raising efficacy/blinding/atrophy concerns; not primary data) |
| `40232258` | 2025 | supports | `narrative_review` (SR of 13 studies + 13 ongoing) |
| `41070709` | 2025 | supports | `uncontrolled_observational` (China multicenter n=68, no placebo), `short_duration` (7 mo) |
| `40308765` | 2025 | supports | `narrative_review` (re-evaluation meta of 5 studies, lecanemab/donanemab pooled) |
| `40386876` | 2025 | inconclusive | `comparator_only` (rTMS vs anti-amyloid NMA — lecanemab as comparator) |
| `41322352` | 2025 | inconclusive | `comparator_only` (symptomatic vs DMT NMA — lecanemab "moderate benefits") |
| `39269842` | 2024 | inconclusive | `methodology_only` (AE-as-unblinding meta) |
| `41160347` | 2025 | inconclusive | `descriptive_utilization` (US claims-based utilization), `uncontrolled_observational` |
| `41352683` | 2025 | inconclusive | `narrative_review`, `subgroup_positive` (patient-characteristics meta — best response in White/non-ApoE4) |
| `41985900` | 2026 | contradicts [FLIP] | `hedged_meta` (Cochrane: "trivial" cognitive effect, "small at best" functional, "does not seem to be associated with clinically meaningful effects") |
| `41396015` | 2025 | inconclusive | `uncontrolled_observational` (n=190 Eastern China, no comparator), `safety_only` (despite explicit "no measurable cognitive efficacy" — kept inconclusive due to short-term safety-focus design) |
| `41428477` | 2025 | inconclusive | `comparator_only` (Souvenaid effect-size comparison) |
| `41478817` | 2026 | inconclusive | `safety_only` (RCT+RWE safety meta) |
| `41823189` | 2026 | supports | `uncontrolled_observational` (China n=261; ADNI matched-comparator, not RCT), `short_duration` (6 mo) |
| `41581261` | 2026 | inconclusive | `uncontrolled_observational` (n=187 single-center), `safety_only` |
| `41689888` | 2026 | supports | `same_cohort_duplicate` (CLARITY-AD ApoE ε4 non-carrier/heterozygote subgroup), `subgroup_positive` |

### Tag distribution (Q14 totals)

- `same_cohort_duplicate`: **9** (CLARITY-AD: `38730496`, `37874099`,
  `40189473`, `41355080`, `41689888` = 5; Phase 2b Study 201:
  `36544184`, `36482412`, `37040116` = 3; plus a near-9th if you
  include the parent-trial papers themselves which are not tagged
  because they are the canonical primary). The two parents are
  `36449413` (CLARITY-AD) and `33865446` (Phase 2b).
- `narrative_review`: **9** (`37902139`, `37213538`, `38429615`,
  `39638097`, `36336488`, `39432414`, `38759015`, `40232258`,
  `40308765`, `41352683`)
- `uncontrolled_observational`: **6** (`39559868`, `41070709`,
  `41160347`, `41396015`, `41581261`, `41823189`)
- `safety_only`: **6** (`38730496`, `39559868`, `41396015`,
  `41478817`, `41581261`, plus partial `41160347`)
- `comparator_only`: **4** (`38253184`, `40386876`, `41322352`,
  `41428477`)
- `commentary`: **2** (`37295957`, `38484213`)
- `hedged_meta`: **2** (`36184326`, `41985900`)
- `methodology_only`: **4** (`36482412`, `35320578`, `37040116`,
  `39269842`)
- `descriptive_utilization`: **3** (`40011174`, `41160347`, `36336488`)
- `subgroup_positive`: **3** (`40189473`, `41352683`, `41689888`)
- `biomarker_only`: **1** (`35320578`)
- `missed_primary_sig_secondary`: **1** (`33865446`)
- `short_duration`: **2** (`41070709`, `41823189`)

### Summary

Q14 is uniquely heavy on `same_cohort_duplicate` (~26% of pmids from 2
cohorts) and `narrative_review` (~26% from secondary syntheses).
**Only 1 of 38 pmids (`36449413`) is the canonical CLARITY-AD primary;
only 1 (`33865446`) is the Phase 2b parent.** Without filtering, the
"supports" bucket reads as 19 votes when in evidence terms it's closer
to ~5 distinct supporting datasets (CLARITY-AD core, Phase 2b core,
2 Chinese real-world cohorts, comparator NMAs that ranked lecanemab
mid-tier). The single `contradicts` (now 2) carry far more weight than
the count suggests because both are GRADE-rated meta-analyses speaking
to the magnitude debate.

---

## Abstracts (n=38)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 36449413 — current stance: `supports`

**Stance justification:** > The adjusted least-squares mean change from baseline at 18 months was 1.21 with lecanemab and 1.66 with placebo (difference, -0.45; 95% confidence interval [CI], -0.67 to -0.23; P<0.001).

**Golden note:** CLARITY-AD — landmark positive phase 3 in early AD.

**Lecanemab in Early Alzheimer's Disease.**

*The New England journal of medicine*, 2022. Types: Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: The accumulation of soluble and insoluble aggregated amyloid-beta (Aβ) may initiate or potentiate pathologic processes in Alzheimer's disease. Lecanemab, a humanized IgG1 monoclonal antibody that binds with high affinity to Aβ soluble protofibrils, is being tested in persons with early Alzheimer's disease. METHODS: We conducted an 18-month, multicenter, double-blind, phase 3 trial involving persons 50 to 90 years of age with early Alzheimer's disease (mild cognitive impairment or mild dementia due to Alzheimer's disease) with evidence of amyloid on positron-emission tomography (PET) or by cerebrospinal fluid testing. Participants were randomly assigned in a 1:1 ratio to receive intravenous lecanemab (10 mg per kilogram of body weight every 2 weeks) or placebo. The primary end point was the change from baseline at 18 months in the score on the Clinical Dementia Rating-Sum of Boxes (CDR-SB; range, 0 to 18, with higher scores indicating greater impairment). Key secondary end points were the change in amyloid burden on PET, the score on the 14-item cognitive subscale of the Alzheimer's Disease Assessment Scale (ADAS-cog14; range, 0 to 90; higher scores indicate greater impairment), the Alzheimer's Disease Composite Score (ADCOMS; range, 0 to 1.97; higher scores indicate greater impairment), and the score on the Alzheimer's Disease Cooperative Study-Activities of Daily Living Scale for Mild Cognitive Impairment (ADCS-MCI-ADL; range, 0 to 53; lower scores indicate greater impairment). RESULTS: A total of 1795 participants were enrolled, with 898 assigned to receive lecanemab and 897 to receive placebo. The mean CDR-SB score at baseline was approximately 3.2 in both groups. The adjusted least-squares mean change from baseline at 18 months was 1.21 with lecanemab and 1.66 with placebo (difference, -0.45; 95% confidence interval [CI], -0.67 to -0.23; P<0.001). In a substudy involving 698 participants, there were greater reductions in brain amyloid burden with lecanemab than with placebo (difference, -59.1 centiloids; 95% CI, -62.6 to -55.6). Other mean differences between the two groups in the change from baseline favoring lecanemab were as follows: for the ADAS-cog14 score, -1.44 (95% CI, -2.27 to -0.61; P<0.001); for the ADCOMS, -0.050 (95% CI, -0.074 to -0.027; P<0.001); and for the ADCS-MCI-ADL score, 2.0 (95% CI, 1.2 to 2.8; P<0.001). Lecanemab resulted in infusion-related reactions in 26.4% of the participants and amyloid-related imaging abnormalities with edema or effusions in 12.6%. CONCLUSIONS: Lecanemab reduced markers of amyloid in early Alzheimer's disease and resulted in moderately less decline on measures of cognition and function than placebo at 18 months but was associated with adverse events. Longer trials are warranted to determine the efficacy and safety of lecanemab in early Alzheimer's disease. (Funded by Eisai and Biogen; Clarity AD ClinicalTrials.gov number, NCT03887455.).

---

### PMID 33865446 — current stance: `supports`

**Stance justification:** > BAN2401-G000-201 did not meet the 12-month primary endpoint. However, prespecified 18-month Bayesian and frequentist analyses demonstrated reduction in brain amyloid accompanied by a consistent reduction of clinical decline across several clinical and biomarker endpoints.

**Golden note:** Phase 2b proof-of-concept positive.

**A randomized, double-blind, phase 2b proof-of-concept clinical trial in early Alzheimer's disease with lecanemab, an anti-Aβ protofibril antibody.**

*Alzheimer's research & therapy*, 2021. Types: Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> BACKGROUND: Lecanemab (BAN2401), an IgG1 monoclonal antibody, preferentially targets soluble aggregated amyloid beta (Aβ), with activity across oligomers, protofibrils, and insoluble fibrils. BAN2401-G000-201, a randomized double-blind clinical trial, utilized a Bayesian design with response-adaptive randomization to assess 3 doses across 2 regimens of lecanemab versus placebo in early Alzheimer's disease, mild cognitive impairment due to Alzheimer's disease (AD) and mild AD dementia. METHODS: BAN2401-G000-201 aimed to establish the effective dose 90% (ED90), defined as the simplest dose that achieves ≥90% of the maximum treatment effect. The primary endpoint was Bayesian analysis of 12-month clinical change on the Alzheimer's Disease Composite Score (ADCOMS) for the ED90 dose, which required an 80% probability of ≥25% clinical reduction in decline versus placebo. Key secondary endpoints included 18-month Bayesian and frequentist analyses of brain amyloid reduction using positron emission tomography; clinical decline on ADCOMS, Clinical Dementia Rating-Sum-of-Boxes (CDR-SB), and Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-Cog14); changes in CSF core biomarkers; and total hippocampal volume (HV) using volumetric magnetic resonance imaging. RESULTS: A total of 854 randomized subjects were treated (lecanemab, 609; placebo, 245). At 12 months, the 10-mg/kg biweekly ED90 dose showed a 64% probability to be better than placebo by 25% on ADCOMS, which missed the 80% threshold for the primary outcome. At 18 months, 10-mg/kg biweekly lecanemab reduced brain amyloid (-0.306 SUVr units) while showing a drug-placebo difference in favor of active treatment by 27% and 30% on ADCOMS, 56% and 47% on ADAS-Cog14, and 33% and 26% on CDR-SB versus placebo according to Bayesian and frequentist analyses, respectively. CSF biomarkers were supportive of a treatment effect. Lecanemab was well-tolerated with 9.9% incidence of amyloid-related imaging abnormalities-edema/effusion at 10 mg/kg biweekly. CONCLUSIONS: BAN2401-G000-201 did not meet the 12-month primary endpoint. However, prespecified 18-month Bayesian and frequentist analyses demonstrated reduction in brain amyloid accompanied by a consistent reduction of clinical decline across several clinical and biomarker endpoints. A phase 3 study (Clarity AD) in early Alzheimer's disease is underway. TRIAL REGISTRATION: Clinical Trials.gov NCT01767311 .

---

### PMID 36544184 — current stance: `supports`

**Stance justification:** > Lecanemab treatment resulted in significant reduction in amyloid plaques and a slowing of clinical decline.

**Golden note:** Phase 2 OLE — sustained benefit on cognition + biomarkers.

**Lecanemab in patients with early Alzheimer's disease: detailed results on biomarker, cognitive, and clinical effects from the randomized and open-label extension of the phase 2 proof-of-concept study.**

*Alzheimer's research & therapy*, 2022. Types: Randomized Controlled Trial; Clinical Trial, Phase II; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: Lecanemab, a humanized IgG1 monoclonal antibody that targets soluble aggregated Aβ species (protofibrils), has demonstrated robust brain fibrillar amyloid reduction and slowing of clinical decline in early AD. The objective of this analysis is to report results from study 201 blinded period (core), the open-label extension (OLE), and gap period (between core and OLE) supporting the effectiveness of lecanemab. METHODS: The lecanemab study 201 core was a double-blind, randomized, placebo-controlled study of 856 patients randomized to one of five dose regimens or placebo. An OLE of study 201 was initiated to allow patients to receive open-label lecanemab 10mg/kg biweekly for up to 24 months, with an intervening off-treatment period (gap period) ranging from 9 to 59 months (mean 24 months). RESULTS: At 12 and 18 months of treatment in the core, lecanemab 10 mg/kg biweekly demonstrated dose-dependent reductions of brain amyloid measured PET and corresponding changes in plasma biomarkers and slowing of cognitive decline. The rates of clinical progression during the gap were similar in lecanemab and placebo subjects, with clinical treatment differences maintained after discontinued dosing over an average of 24 months in the gap period. During the gap, plasma Aβ42/40 ratio and p-tau181 levels began to return towards pre-randomization levels more quickly than amyloid PET. At OLE baseline, treatment differences vs placebo at 18 months in the randomized period were maintained across 3 clinical assessments. In the OLE, lecanemab 10 mg/kg biweekly treatment produced dose-dependent reductions in amyloid PET SUVr, improvements in plasma Aβ42/40 ratio, and reductions in plasma p-tau181. CONCLUSIONS: Lecanemab treatment resulted in significant reduction in amyloid plaques and a slowing of clinical decline. Data indicate that rapid and pronounced amyloid reduction correlates with clinical benefit and potential disease-modifying effects, as well as the potential to use plasma biomarkers to monitor for lecanemab treatment effects. TRIAL REGISTRATION: ClinicalTrials.gov NCT01767311 .

---

### PMID 38730496 — current stance: `inconclusive`

**Stance justification:** > Lecanemab was generally well-tolerated, with the most common adverse events being infusion-related reactions, ARIA-H, ARIA-E.

**Golden note:** Updated phase 3 safety report — safety focus, no new efficacy claim.

**Updated safety results from phase 3 lecanemab study in early Alzheimer's disease.**

*Alzheimer's research & therapy*, 2024. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Clinical Trial, Phase III; Research Support, Non-U.S. Gov't

> BACKGROUND: Alzheimer disease (AD) is a major health problem of aging, with tremendous burden on healthcare systems, patients, and families globally. Lecanemab, an FDA-approved amyloid beta (Aβ)-directed antibody indicated for the treatment of early AD, binds with high affinity to soluble Aβ protofibrils, which have been shown to be more toxic to neurons than monomers or insoluble fibrils. Lecanemab has been shown to be well tolerated in multiple clinical trials, although risks include an increased rate of amyloid-related imaging abnormalities (ARIA) and infusion reactions relative to placebo. METHODS: Clarity AD was an 18-month treatment (Core study), multicenter, double-blind, placebo-controlled, parallel-group study with open-label extension (OLE) in participants with early AD. Eligible participants were randomized 1:1 across 2 treatment groups (placebo and lecanemab 10 mg/kg biweekly). Safety evaluations included monitoring of vital signs, physical examinations, adverse events, clinical laboratory parameters, and 12-lead electrocardiograms. ARIA occurrence was monitored throughout the study by magnetic resonance imaging, read both locally and centrally. RESULTS: Overall, 1795 participants from Core and 1612 participants with at least one dose of lecanemab (Core + OLE) were included. Lecanemab was generally well-tolerated in Clarity AD, with no deaths related to lecanemab in the Core study. There were 9 deaths during the OLE, with 4 deemed possibly related to study treatment. Of the 24 deaths in Core + OLE, 3 were due to intracerebral hemorrhage (ICH): 1 placebo in the Core due to ICH, and 2 lecanemab in OLE with concurrent ICH (1 on tissue plasminogen activator and 1 on anticoagulant therapy). In the Core + OLE, the most common adverse events in the lecanemab group (> 10%) were infusion-related reactions (24.5%), ARIA with hemosiderin deposits (ARIA-H) microhemorrhages (16.0%), COVID-19 (14.7%), ARIA with edema (ARIA-E; 13.6%), and headache (10.3%). ARIA-E and ARIA-H were largely radiographically mild-to-moderate. ARIA-E generally occurred within 3-6 months of treatment, was more common in ApoE e4 carriers (16.8%) and most common in ApoE ε4 homozygous participants (34.5%). CONCLUSIONS: Lecanemab was generally well-tolerated, with the most common adverse events being infusion-related reactions, ARIA-H, ARIA-E. Clinicians, participants, and caregivers should understand the incidence, monitoring, and management of these events for optimal patient care. TRIAL REGISTRATION: ClinicalTrials.gov numbers: Clarity AD NCT03887455).

---

### PMID 38253184 — current stance: `inconclusive`

**Stance justification:** > Although it is yet to be determined which is more effective between lithium or lecanemab or donanemab, lithium may be more effective than aducanumab. Aducanumab, lecanemab and donanemab do not appear to differ in their effectiveness on cognitive function.

**Golden note:** Network meta donanemab/lecanemab/aducanumab/lithium — comparative, mixed.

**Comparative efficacy, tolerability and acceptability of donanemab, lecanemab, aducanumab and lithium on cognitive function in mild cognitive impairment and Alzheimer's disease: A systematic review and network meta-analysis.**

*Ageing research reviews*, 2024. Types: Comparative Study; Journal Article; Systematic Review; Network Meta-Analysis

> BACKGROUND: The comparative clinical utility of the disease-modifying treatments for mild cognitive impairment and Alzheimer's disease that are approved or under review by the Food and Drug Administration (i.e., donanemab, lecanemab and aducanumab), and lithium, which is a potential disease-modifying agent for this condition, remains elusive. OBJECTIVE: We aimed to compare the efficacy on cognitive decline, tolerability and acceptability of these drugs in this condition. METHODS: We systematically searched in MEDLINE, CENTRAL, CINHAL and ClinicalTrials,gov for randomized controlled trials from their inception to 7 November 2023, and then performed a random-effect network meta-analysis. RESULTS: The analysis included 8 randomized placebo-controlled trials with 6547 participants. On the Mini-Mental State Examination, lithium significantly outperformed donanemab, aducanumab and placebo. On the Alzheimer's Disease Assessment Scale-cognitive subscale, the efficacy of all active drugs was significantly higher than placebo. In addition, in the Clinical Dementia Rating sum of boxes, the efficacy of donanemab and lecanemab was significantly higher than placebo. Compared to placebo, donanemab and lecanemab were significantly less acceptable and tolerable. Aducanumab was also less well tolerated compared to placebo. There were no significant differences in the other comparisons. CONCLUSION: Although it is yet to be determined which is more effective between lithium or lecanemab or donanemab, lithium may be more effective than aducanumab. Aducanumab, lecanemab and donanemab do not appear to differ in their effectiveness on cognitive function. Low-dose lithium may be safer than aducanumab, lecanemab and donanemab.

---

### PMID 37874099 — current stance: `supports`

**Stance justification:** > At month 18, adjusted mean change from baseline in EQ-5D-5L and QOL-AD by subject showed 49% and 56% less decline, respectively.

**Golden note:** CLARITY-AD QoL secondary — improved health-related QoL.

**Lecanemab Clarity AD: Quality-of-Life Results from a Randomized, Double-Blind Phase 3 Trial in Early Alzheimer's Disease.**

*The journal of prevention of Alzheimer's disease*, 2023. Types: Clinical Trial, Phase III; Randomized Controlled Trial; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: Lecanemab is a humanized IgG1 monoclonal antibody binding with high affinity to amyloid-beta protein protofibrils. In phase 3 development, lecanemab has been shown to reduce markers of amyloid in early Alzheimer's disease and reduce decline on clinical endpoints of cognition and function at 18 months. OBJECTIVES: To describe the health-related quality-of-life (HRQoL) results from Clarity AD which were exploratory outcomes in this trial. DESIGN: Clarity AD was an 18-month, multi-center, double-blind, phase 3 trial. SETTING: Early Alzheimer's disease. PARTICIPANTS: Individuals 50-90 years of age with a diagnosis of mild cognitive impairment or mild dementia due to Alzheimer's disease and positron emission tomography or cerebrospinal fluid evidence of cerebral amyloid accumulation. INTERVENTION: Placebo or lecanemab 10-mg/kg IV biweekly. MEASUREMENTS: HRQoL was measured at baseline and every 6 months using the European Quality of Life-5 Dimensions (EQ-5D-5L; by subject) and Quality of Life in AD (QOL-AD; by subject and proxy). Study partner burden was measured using the Zarit Burden Interview (ZBI). RESULTS: A total of 1795 participants were enrolled (lecanemab:898; placebo:897). At month 18, adjusted mean change from baseline in EQ-5D-5L and QOL-AD by subject showed 49% and 56% less decline, respectively. QOL-AD rated by study partner as proxy resulted in 23% less decline. ZBI adjusted mean change from baseline at 18 months resulted in 38% less increase of care partner burden. Individual HRQoL test items and dimensions also showed lecanemab benefit. CONCLUSIONS: Lecanemab was associated with a relative preservation of HRQoL and less increase in caregiver burden, with consistent benefits seen across different quality of life scales and within scale subdomains. These benefits provide valuable patient reported outcomes which, together with previously reported benefits of lecanemab across multiple measures of cognition, function, disease progression, and biomarkers, demonstrate that lecanemab treatment may offer meaningful benefits to patients, care partners, and society.

---

### PMID 36184326 — current stance: `inconclusive`

**Stance justification:** > When pooled together, the data from high-clearance anti-amyloid immunotherapies trials confirm a statistically significant clinical effect of these drugs on cognitive decline after 18 months... However, this effect remains below the previously established minimal clinically relevant values.

**Golden note:** Anti-amyloid immunotherapy meta part 1 — efficacy modest, controversy.

**High-clearance anti-amyloid immunotherapies in Alzheimer's disease. Part 1: Meta-analysis and review of efficacy and safety data, and medico-economical aspects.**

*Revue neurologique*, 2022. Types: Meta-Analysis; Journal Article; Review

> In 2021, aducanumab, an immunotherapy targeting amyloid-β, was approved for Alzheimer's disease (AD) by the US Food and Drug Administration thanks to positive results on a putative biological surrogate marker. This approval has raised an unprecedented controversy. It was followed by a refusal of the European Medicine Agency, which does not allow the marketing of drugs solely on biological arguments and raised safety issues, and important US coverage limitations by the Centers for Medicare & Medicaid Services. Two other anti-amyloid immunotherapies showed significant results regarding a clinical outcome in phase 2 trials, and five drugs are being studied in phase 3 trials. Compared to those tested in previous trials of the 2010s, the common feature and novelty of these anti-amyloid immunotherapies is their ability to induce a high clearance of amyloid load, as measured with positron emission tomography, in the brain of early-stage biomarker-proven AD patients. Here, we review the available evidence regarding efficacy and safety data and medico-economical aspects for high-clearance anti-amyloid immunotherapies. We also perform frequentist and Bayesian meta-analyses of the clinical efficacy and safety of the highest dose groups from the two aducanumab phase 3 trials and the donanemab and lecanemab phase 2 trials. When pooled together, the data from high-clearance anti-amyloid immunotherapies trials confirm a statistically significant clinical effect of these drugs on cognitive decline after 18 months (difference in cognitive decline measured with CDR-SB after 18 months between the high dose immunotherapy groups vs. placebo = -0.24 points; P=0.04, frequentist random-effect model), with results on ADAS-Cog being the most statistically robust. However, this effect remains below the previously established minimal clinically relevant values. In parallel, the drugs significantly increased the occurrence of amyloid-related imaging abnormalities-edema (ARIA-E: risk ratio=13.39; P<0.0001), ARIA-hemorrhage (risk ratio=2.78; P=0.0002), and symptomatic and serious ARIA (7/1321=0.53% in the high dose groups versus 0/1446 in the placebo groups; risk ratio=6.44; P=0.04). The risk/benefit ratio of high-clearance immunotherapies in early AD is so far questionable after 18 months. Identifying subgroups of better responders, the perspective of combination therapies, and a longer follow-up may help improve their clinical relevance. Finally, the preliminary evidence from medico-economical analyses seems to indicate that the current cost of aducanumab in the US is not in reasonable alignment with its clinical benefits.

---

### PMID 37902139 — current stance: `supports`

**Stance justification:** > Lecanemab therapy led to a substantial decrease in amyloid plaques and a noticeable slowing of clinical decline.

**Golden note:** Lecanemab systematic review — efficacy in slowing decline.

**Novel anti-amyloid-beta (Aβ) monoclonal antibody lecanemab for Alzheimer's disease: A systematic review.**

*International journal of immunopathology and pharmacology*, 2023. Types: Systematic Review; Journal Article

> BACKGROUND: Lecanemab is the latest monoclonal antibody that targets beta-amyloid approved exclusively for treatment of Alzheimer's disease with mild cognitive impairment or mild dementia. This article aims to provide a systematic review of the efficacy, and safety of lecanemab in slowing clinical decline in Alzheimer's disease. METHODS: A comprehensive search of various databases, including the National Institute of Health clinical trials registry, PubMed, and the Cochrane library, was conducted until July 2023 using the keywords lecanemab, BAN2401, and Alzheimer's disease. Additionally, conference abstracts listed in the Cochrane database (including Embase) and drug information from the US Food and Drug Administration (FDA) label were examined. Only clinical trials published in the English language were considered. In total, 107 articles were retrieved, and after thorough evaluation, three randomized, double-blind, multicenter clinical trials involving 2729 participants were included in the analysis. RESULTS: The FDA approved lecanemab for Alzheimer's disease in January 2023 which acts as a novel disease-modifying anti-amyloid-beta (Aβ) human monoclonal antibody and is administered intravenously. Based on the clinical trials included in this review, lecanemab was found efficacious in reducing the accumulation of beta-amyloid and slowing down the cognitive decline and it was well tolerated. Lecanemab had a statistically significant change from baseline in Clinical Dementia Rating-Sum of Boxes (CDR-SB), Alzheimer's Disease Composite Score (ADCOMS), Alzheimer's Disease Assessment Scale (ADAScog14), Alzheimer's Disease Cooperative Study-Activities of Daily Living Scale for Mild Cognitive Impairment (ADCS-MCI-ADL), and reductions in brain amyloid burden. The most common treatment-emergent adverse events were headache, infusion-related reactions, and Amyloid related imaging abnormalities-edema. CONCLUSIONS: Lecanemab therapy led to a substantial decrease in amyloid plaques and a noticeable slowing of clinical decline. The findings suggest a meaningful connection between the reduction in amyloid and the positive impact on patients' clinical outcomes, hinting at potential disease-modifying effects.

---

### PMID 37213538 — current stance: `supports`

**Stance justification:** > It is reported that lecanemab was beneficial to stabilize or slow down the decrease in CDR-SB (WMD: -0.45; 95% CI: -0.64, -0.25; p < 0.00001), ADCOMS (WMD: -0.05; 95% CI: -0.07, -0.03; p < 0.00001), ADAS-cog (WMD: -1.11; 95% CI: -1.64, -0.57; p < 0.0001).

**Golden note:** Lecanemab safety/efficacy RCT meta — beneficial.

**Safety and efficacy of lecanemab for Alzheimer's disease: a systematic review and meta-analysis of randomized clinical trials.**

*Frontiers in aging neuroscience*, 2023. Types: Systematic Review; Journal Article

> OBJECTIVE: We performed a systematic review and meta-analysis of the cognitive effectiveness and safety of lecanemab on subjects with Alzheimer's disease (AD). METHODS: We screened the literature published before February 2023 in PubMed, Embase, Web of Science, and Cochrane that were searched for randomized controlled trials testing lecanemab for the treatment of cognitive decline in patients with MCI or AD. Outcomes measured were CDR Sum of Boxes (CDR-SB), Alzheimer's Disease Composite Score (ADCOMS), AD Assessment Scale-Cognitive Subscale (ADAS-Cog), Clinical Dementia Rating (CDR), amyloid PET Standardized Uptake Volume Ratio (SUVr), amyloid burden on PET, and risks for adverse events. RESULTS: A total of four randomized controlled trials were included, involving 3,108 AD patients (1,695 lecanemab groups and 1,413 placebo groups) to synthesize evidence. Baseline characteristics of the two groups were similar in all outcomes except that ApoE 4 status and higher MMSE score were observed in the lecanemab group. It is reported that lecanemab was beneficial to stabilize or slow down the decrease in CDR-SB (WMD: -0.45; 95% CI: -0.64, -0.25; p < 0.00001), ADCOMS (WMD: -0.05; 95% CI: -0.07, -0.03; p < 0.00001), ADAS-cog (WMD: -1.11; 95% CI: -1.64, -0.57; p < 0.0001), amyloid PET SUVr (WMD: -0.15; 95% CI: -0.48, 0.19; p = 0.38), amyloid burden on PET (WMD:-35.44; 95% CI: -65.22,-5.67; p = 0.02), adverse events (subjects with any TEAE) (OR: 0.73; 95% CI: 0.25, 2.15; p = 0.57), ARIA-E (OR:8.95; 95% CI: 5.36, 14.95; p < 0.00001), and ARIA-H (OR:2.00; 95% CI: 1.53, 2.62; p < 0.00001) in early AD patients. CONCLUSION: Our analysis found that lecanemab showed significant positive statistical efficacy with respect to cognition, function, and behavior in patients with early AD though the actual clinical significance is yet to be established. SYSTEMATIC REVIEW REGISTRATION: https://www.crd.york.ac.uk/PROSPERO/#recordDetails, identifier: CRD42023393393.

---

### PMID 39559868 — current stance: `inconclusive`

**Stance justification:** > Through our early experience with lecanemab, we have recognized several areas of improvement which have clarified and enhanced the lecanemab infusion experience.

**Golden note:** 71-patient regional center real-world experience — descriptive.

**Initial Experience with Lecanemab and Lessons Learned in 71 Patients in a Regional Medical Center.**

*The journal of prevention of Alzheimer's disease*, 2024. Types: Journal Article; Observational Study

> BACKGROUND AND OBJECTIVES: On July 6, 2023 the U.S. Food and Drug Administration approved the anti-amyloid monoclonal antibody lecanemab (Leqembi®) for treatment of patients with mild cognitive impairment or mild dementia due to Alzheimer's disease (AD). Our early experience and lessons learned with lecanemab in a regional community medical center are described. DESIGN, SETTING, AND PARTICIPANTS: This retrospective observational study highlights the first 71 patients treated with lecanemab at our multidisciplinary Norton Neuroscience Institute Memory Center. All patients had positive cerebrospinal fluid biomarkers for AD and underwent at least 1 lecanemab infusion. Two patients had additional amyloid PET scans which were positive. RESULTS: The mean age was 72 years (49-90 years), and 44 (62%) patients were female. Most were Caucasian (68 [96%]), and 54 [76%] were referred to our Memory Center by their primary care provider. Comorbidities were common, including hypertension (34 [48%]), hypercholesterolemia (51 [72%]), diabetes mellitus (17 [24%]), and cardiovascular disease excluding hypertension (22 [31%]). The mean body mass index was 27.0 (range: 17.8-45.0). A total of 36 (51%) patients were heterozygous for the ApoE4 genotype, and 9 (13%) were homozygous. A total of 61 [86%] patients had been treated with donepezil; 40 (56%) patients had received memantine. Of the 50 patients who completed 1 or more safety monitoring brain MRIs following infusion, 12 (24%) had amyloid-related imaging abnormalities (ARIA) detected: solitary ARIA-H (hemorrhage) in 5, solitary ARIA-E (edema) in 3, and both ARIA-H and ARIA-E in 4. Of the 12 patients with ARIA, 9 were asymptomatic, 4 were homozygous for the ApoE4 genotype, and 6 were heterozygous for the ApoE4 genotype. Of the 9 who were homozygous for the ApoE4 genotype in this study, 4 (44%) had evidence of ARIA. Of the 36 who were heterozygous for the ApoE4 genotype, 6 (17%) were diagnosed with ARIA. Twenty-six (37%) patients experienced infusion reactions after their first lecanemab infusion: headaches (12 patients) and shaking/chills/rigors (11 patients) were most common. Twenty-three (88%) of these 26 patients reported the side effects either at the infusion center or within the first 24 hours post-infusion. One patient died shortly after the first lecanemab infusion of a myocardial infarction. It is uncertain whether or not this death was related to lecanemab treatment. CONCLUSION: Through our early experience with lecanemab, we have recognized several areas of improvement which have clarified and enhanced the lecanemab infusion experience.

---

### PMID 37295957 — current stance: `inconclusive`

**Stance justification:** > The demonstration that lecanemab treatment delayed clinical progression in persons with mild symptoms due to AD is a major conceptual achievement, but a better appreciation of the magnitude and durability of benefits for individual patients will require extended observations from clinical practice settings.

**Golden note:** 'Incremental step or paradigm shift' commentary — debate framing.

**Implications of the Approval of Lecanemab for Alzheimer Disease Patient Care: Incremental Step or Paradigm Shift?**

*Neurology*, 2023. Types: Randomized Controlled Trial; Journal Article

> The amyloid cascade model of the pathogenesis of Alzheimer disease (AD) is well supported in observational studies. Its therapeutic corollary asserts that removal of amyloid-β peptide ("amyloid") would provide clinical benefits. After 2 decades of pursuing the strategy of amyloid removal without success, clinical trials of the antiamyloid monoclonal antibody (AAMA) donanemab and a phase 3 clinical trial of lecanemab have reported clinical benefits linked to amyloid removal. Lecanemab (trade name, Leqembi) is the first with published phase 3 trial results. When administered through IV every 2 weeks to patients with elevated brain amyloid and mild cognitive impairment or mild dementia, lecanemab delayed cognitive and functional worsening by approximately 5 months in an 18-month double-blind, placebo-controlled trial. The trial was well conducted, and the results favoring lecanemab were internally consistent. The demonstration that lecanemab treatment delayed clinical progression in persons with mild symptoms due to AD is a major conceptual achievement, but a better appreciation of the magnitude and durability of benefits for individual patients will require extended observations from clinical practice settings. Amyloid-related imaging abnormalities (ARIA) that were largely asymptomatic occurred in approximately 20%, slightly more than half of which were attributable to treatment and the rest to underlying AD-related amyloid angiopathy. Persons who were homozygous for the APOE ε4 allele had greater ARIA risks. Hemorrhagic complications with longer-term lecanemab use need to be better understood. Administration of lecanemab will place unprecedented pressures on dementia care personnel and infrastructure, both of which need to grow exponentially to meet the challenge.

---

### PMID 36482412 — current stance: `supports`

**Stance justification:** > The conclusion of the primary analysis of the lecanemab Study 201 is strengthened by the consistently positive conclusions across multiple statistical models, across efficacy endpoints, and over time, despite missing data.

**Golden note:** Phase 2 consistency-of-results analysis — robust to method.

**Consistency of efficacy results across various clinical measures and statistical methods in the lecanemab phase 2 trial of early Alzheimer's disease.**

*Alzheimer's research & therapy*, 2022. Types: Randomized Controlled Trial; Clinical Trial, Phase II; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: Lecanemab (BAN2401) is a humanized IgG1 monoclonal antibody that preferentially targets soluble aggregated Aβ species (protofibrils) with activity at insoluble fibrils and slowed clinical decline in an 18-month phase 2 proof-of-concept study (Study 201; ClinicalTrials.gov NCT01767311) in 856 subjects with early Alzheimer's disease (AD). In this trial, subjects were randomized to five lecanemab dose regimens or placebo. The primary efficacy endpoint was change from baseline in the Alzheimer's Disease Composite Score (ADCOMS) at 12 months with Bayesian analyses. The key secondary endpoints were ADCOMS at 18 months and Clinical Dementia Rating-Sum-of-Boxes (CDR-SB) and Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-Cog14) at 18 months. The results have been published previously. Herein, we describe the results of sensitivity analyses evaluating the consistency of the lecanemab efficacy results in Study 201 at the identified dose, the ED90, across multiple statistical methods and multiple endpoints over the duration of the study. METHODS: The protocol-specified analysis model was a mixed model for repeated measures (MMRM). Sensitivity analyses address the consistency of the conclusions using multiple statistical methods. These include a disease progression model (DPM), a natural cubic spline (NCS) model, a quadratic mixed model (QMM), and 2 MMRMs with additional covariates. RESULTS: The sensitivity analyses showed positive lecanemab treatment effects for all endpoints and all statistical models considered. The protocol-specified ADCOMS analysis showed a 29.7% slower decline than placebo for ADCOMS at 18 months. The various other analyses of 3 key endpoints showed declines ranging from 26.5 to 55.9%. The results at 12 months are also consistent with those at 18 months. CONCLUSIONS: The conclusion of the primary analysis of the lecanemab Study 201 is strengthened by the consistently positive conclusions across multiple statistical models, across efficacy endpoints, and over time, despite missing data. The 18-month data from this trial was utilized in the design of the confirmatory phase 3 trial (Clarity AD) and allowed for proper powering for multiple, robust outcomes.

---

### PMID 38429615 — current stance: `supports`

**Stance justification:** > Lecanemab (87.24%) may be the most promising way to slow down the decrease of Alzheimer's Disease Cooperative Study-Activities of Daily Living (ADCS-ADL) score.

**Golden note:** Network meta of mAbs — beneficial cognitive/clinical effects.

**Comparative Efficacy and Safety of Monoclonal Antibodies for Cognitive Decline in Patients with Alzheimer's Disease: A Systematic Review and Network Meta-Analysis.**

*CNS drugs*, 2024. Types: Systematic Review; Research Support, Non-U.S. Gov't; Journal Article; Network Meta-Analysis

> BACKGROUND: Recent clinical trials of anti-Aβ monoclonal antibodies (mAbs) in the treatment of early Alzheimer's disease (AD) have produced encouraging cognitive and clinical results. The purpose of this network meta-analysis (NMA) was to compare and rank mAb drugs according to their efficacy and safety. METHODS: PubMed, Embase, Web of Science, and the Cochrane Library were searched for randomized controlled trials testing various mAbs for the treatment of cognitive decline in patients with AD, up to March 31, 2023. R software (version 4.2.3) along with JAGS and STATA software (version 15.0) were used for statistical analysis. Odds ratio (OR) for binary variables, mean difference (MD) for continuous variables, and their 95% confidence intervals (CI) were utilized to estimate treatment effects and rank probabilities for each mAb in terms of safety and efficacy outcomes. We calculated the surface under the cumulative ranking area (SUCRA) to evaluate each mAb, with higher SUCRA values indicating better efficacy or lower likelihood of adverse events. RESULTS: Thirty-three randomized controlled trials with a total of 21,087 patients were included in the current NMA, involving eight different mAbs. SUCRA values showed that aducanumab (87.01% and 99.37%, respectively) was the most likely to achieve the best therapeutic effect based on the changes of Mini-Mental State Examination (MMSE) and Clinical Dementia Rating scale Sum of Boxes (CDR-SB) scores. Donanemab (88.50% and 99.00%, respectively) performed better than other therapies for Alzheimer's Disease Assessment Scale-cognitive subscale (ADAS-cog) and Positron Emission Tomography-Standardized Uptake Value ratio (PET-SUVr). Lecanemab (87.24%) may be the most promising way to slow down the decrease of Alzheimer's Disease Cooperative Study-Activities of Daily Living (ADCS-ADL) score. In the analysis of the incidence of adverse events (subjects with any treatment-emergent adverse event), gantenerumab (89.12%) had the least potential for adverse events, while lecanemab (0.79%) may cause more adverse events. Solanezumab (95.75% and 80.38%, respectively) had the lowest incidence of amyloid-related imaging abnormalities characterized by edema and effusion (ARIA-E) and by cerebral microhemorrhages (ARIA-H) of the included immunotherapies. While SUCRA values provided a comprehensive measure of treatment efficacy, the inherent statistical uncertainty required careful analysis in clinical application. CONCLUSION: Despite immunotherapies significantly increasing the risks of adverse events and ARIA, the data suggest that mAbs can effectively improve the cognitive function of patients with mild and moderate AD. According to the NMA, aducanumab was the most likely to achieve significant improvements in different cognitive and clinical assessments (statistically improved MMSE and CDR-SB), followed by donanemab (statistically improved ADAS-Cog, and PET-SUVr) and lecanemab (statistically improved ADCS-ADL).

---

### PMID 40189473 — current stance: `supports`

**Stance justification:** > For the primary endpoint, there was a slowing of decline with lecanemab in the CDR-SB at 18 months compared to placebo in the Asian region (adjusted mean difference: -0.349; 95 % confidence intervals: -0.773, 0.076; 24 % slowing of decline).

**Golden note:** CLARITY-AD Asian regional analysis — confirms benefit.

**Clarity AD: Asian regional analysis of a phase III trial of lecanemab in early Alzheimer's disease.**

*The journal of prevention of Alzheimer's disease*, 2025. Types: Journal Article; Clinical Trial, Phase III; Multicenter Study; Randomized Controlled Trial

> BACKGROUND: Across Asia, Alzheimer's disease prevalence is expected to rise dramatically due to, among other factors, rapidly aging populations. Alzheimer's disease pathology is triggered by the accumulation of soluble and insoluble aggregated Aβ peptides (oligomers, protofibrils, and fibrils). Lecanemab is a recently approved humanized IgG1 monoclonal antibody that preferentially targets soluble aggregated Aβ species (oligomers, protofibrils), with activity at insoluble fibrils. In the recent 18-month phase 3 Clarity AD study, lecanemab demonstrated a consistent slowing of decline in clinical (global, cognitive, functional, and quality of life) outcomes, and reduction in brain amyloid in early Alzheimer's disease. Lecanemab was well tolerated in Clarity AD, with an increase in incidence of infusion related reactions and amyloid-related imaging abnormalities (ARIA) versus placebo. OBJECTIVES: The objective of this manuscript is to present the results for the Asian region population of Clarity AD. DESIGN: The core Clarity AD study was an 18-month, multicenter, double-blind, placebo-controlled, parallel-group study. SETTING: Academic and clinical centers in Asia PARTICIPANTS: A total of 294 individuals with early Alzheimer's disease (i.e., mild cognitive impairment or mild Alzheimer's disease). INTERVENTION: Eligible patients were randomized across 2 treatment groups (placebo and lecanemab 10 mg/kg biweekly) according to a fixed 1:1 schedule. MEASUREMENTS: The primary efficacy endpoint in the core study was change in the Clinical Dementia Rating-Sum-of-Boxes (CDR-SB) from baseline at 18 months. Key secondary endpoints included change from baseline at 18 months in amyloid PET Centiloids (in patients participating in the amyloid PET sub-study), AD COMposite Score (ADCOMS) and AD Assessment Scale-Cognitive Subscale 14 (ADAS-Cog14). Safety was monitored throughout the study in a blinded manner by the sponsor and in an unblinded manner by an independent data safety monitoring committee. RESULTS: Of the total of 1795 subjects randomized in Clarity AD, 294 subjects were in the Asian region (Japan:152; Korea:129; Singapore:13). The efficacy of lecanemab was consistent with the overall population. For the primary endpoint, there was a slowing of decline with lecanemab in the CDR-SB at 18 months compared to placebo in the Asian region (adjusted mean difference: -0.349; 95 % confidence intervals: -0.773, 0.076; 24 % slowing of decline). Results for the secondary efficacy endpoints also favored lecanemab versus placebo in Asians. Lecanemab was well tolerated in Asian subjects, with a safety profile in Asian subjects similar to the overall Clarity AD population. The most common adverse events of special interest were ARIA-H (lecanemab:14.4 %; placebo:16.2 %), ARIA-E (lecanemab:6.2 %; placebo:1.4 %), and infusion-related reactions (lecanemab:12.3 %; placebo:1.4 %). Incidence of adverse events leading to study drug dose interruption or withdrawal, infusion-related reactions, ARIA-E and ARIA-H was lower for the lecanemab treated group in the Asian region relative to the overall Clarity AD population. Results from quality of life and biomarker assessments in the Asia region were also generally similar to the overall Clarity AD population. CONCLUSION: In the Clarity AD Asian region cohort, the overall efficacy, biomarker changes and safety profile of lecanemab were consistent with the overall population, with a favorable risk-benefit profile and manageable risks. ARIA events and infusion-related reactions occurred less commonly with lecanemab in the Asian region subgroup than the overall population.

---

### PMID 39638097 — current stance: `supports`

**Stance justification:** > The meta-analysis showed that Lecanemab slowed the progression of cognitive impairment as measured by CDR-SB, ADCOMS, and ADASCog, and significantly reduced Amyloid burden on PET in centiloids.

**Golden note:** Lecanemab in mild AD systematic review/meta — efficacy.

**Monoclonal therapy with lecanemab in the treatment of mild Alzheimer's disease: A systematic review and meta-analysis.**

*Ageing research reviews*, 2024. Types: Journal Article; Systematic Review; Meta-Analysis

> Alzheimer's disease, a progressive neurodegenerative pathology, is characterized by the accumulation of Amyloid-β plaques in the brain. Lecanemab (BAN2401), a humanized IgG1 monoclonal antibody, binds with high affinity to Amyloid-β protofibrils. It is the first monoclonal antibody for Alzheimer's disease to receive full FDA approval. This systematic review, conducted meticulously, examines the current use and safety of Lecanemab in treating Alzheimer's disease. We screened literature from databases such as PubMed Central, PubMed (MedLine), ScienceDirect, Scopus, Web of Science, and Wolters Kluwer for randomized controlled trials testing Lecanemab for cognitive decline in patients with mild cognitive impairment due to Alzheimer's disease. Outcomes measured included CDR-SB, ADCOMS, ADAS-Cog, and Amyloid burden on PET in centiloids. Likewise, reports were analyzed for adverse events associated with ARIA-A and ARIA-H. Five papers were included in the systematic review and three in the meta-analysis. The meta-analysis showed that Lecanemab slowed the progression of cognitive impairment as measured by CDR-SB, ADCOMS, and ADASCog, and significantly reduced Amyloid burden on PET in centiloids. However, Lecanemab was associated with an increased risk of ARIA-E and ARIA-H. Lecanemab has demonstrated efficacy in slowing cognitive impairment progression in Alzheimer's disease as measured by ADCOMS, ADAS-Cog, and CDR-SB. However, it is associated with an increased risk of ARIA-E and ARIA-H, particularly in ApoE4 carriers.

---

### PMID 35320578 — current stance: `inconclusive`

**Stance justification:** > Aβ plaques removal in the brain due to amyloid therapy is strongly correlated with a better clinical response in patients with early Alzheimer's disease and a higher ARIA-E rate for the treatment groups and clinical trials in this meta-analysis.

**Golden note:** ARIA-amyloid-clinical correlation meta — methodology.

**Application of Meta-analysis to Evaluate Relationships Among ARIA-E Rate, Amyloid Reduction Rate, and Clinical Cognitive Response in Amyloid Therapeutic Clinical Trials for Early Alzheimer's Disease.**

*Therapeutic innovation & regulatory science*, 2022. Types: Journal Article; Meta-Analysis

> BACKGROUND: Removal of the extracellular Aβ plaques in the brain is one of the mechanisms to treat Alzheimer's disease (AD). Separate clinical trials for several therapeutic compounds that target amyloid plaque reduction have shown noteworthy correlations among plaque removal, the Amyloid-Related Imaging Abnormalities (ARIA) rate, and clinical efficacy of the treatment. The relationships among therapeutic dose levels, the rate of amyloid removal, and the clinical efficacy deserve further investigation across therapeutic agents, particularly for clinical trials to provide insights for strategies to develop amyloid therapies in Alzheimer's disease. METHODS: Published data summaries from clinical trials with amyloid therapies of aducanumab, donanemab, lecanemab, and gantenerumab are evaluated with meta-analyses. Linear mixed models for repeated measurements for visits and random study effects are applied to analyze amyloid centiloid value reduction from baseline and clinical cognition change from baseline for treatment groups according to doses and compounds for the clinical trials. Logistic regression analysis is applied to evaluate the relationship between the amyloid removal rate and the ARIA-Edema (ARIA-E) rate across different dose groups and clinical trials. RESULTS: The extent of amyloid removal varies among therapeutic agents and their dose levels. Across treatment groups and clinical trials, amyloid centiloid value reductions at Weeks 26 and 52 are strongly correlated with both ARIA-E rate over 78 weeks and the clinical efficacy response in the Clinical Dementia-Rating Scale Sum of Boxes (CDR-SB) score change from baseline at Week 78; and the Spearman rank correlations for amyloid reduction at Week 52 are stronger as - 0.79 with the ARIA-E rate over 78 weeks and 0.73 with the Week 78 CDR-SB score change from baseline. CONCLUSION: Aβ plaques removal in the brain due to amyloid therapy is strongly correlated with a better clinical response in patients with early Alzheimer's disease and a higher ARIA-E rate for the treatment groups and clinical trials in this meta-analysis. These relationships suggest that the balance between the clinical efficacy response and safety in ARIA-E rate is relevant for the choice of doses for amyloid therapies in confirmatory clinical trials.

---

### PMID 37040116 — current stance: `supports`

**Stance justification:** > The bayesian posterior probability that the ED90 was superior to placebo was 97.5% at 12 months and 97.7% at 18 months.

**Golden note:** Bayesian re-analysis of phase 2b — confirms efficacy.

**Lecanemab for Patients With Early Alzheimer Disease: Bayesian Analysis of a Phase 2b Dose-Finding Randomized Clinical Trial.**

*JAMA network open*, 2023. Types: Randomized Controlled Trial; Journal Article; Research Support, Non-U.S. Gov't

> IMPORTANCE: Bayesian clinical trial designs are increasingly common; given their promotion by the US Food and Drug Administration, the future use of the bayesian approach will only continue to increase. Innovations possible when using the bayesian approach improve the efficiency of drug development and the accuracy of clinical trials, especially in the context of substantial data missingness. OBJECTIVE: To explain the foundations, interpretations, and scientific justification of the bayesian approach in the setting of lecanemab trial 201, a bayesian-designed phase 2 dose-finding trial; to demonstrate the efficiency of using a bayesian design; and to show how it accommodates innovations in the prospective design and also treatment-dependent types of missing data. DESIGN, SETTING, AND PARTICIPANTS: This study was a bayesian analysis of a clinical trial comparing the efficacy of 5 lecanemab 201 dosages for treatment of early Alzheimer disease. The goal of the lecanemab 201 trial was to identify the effective dose 90 (ED90), the dose achieving at least 90% of the maximum effectiveness of doses considered in the trial. This study assessed the bayesian adaptive randomization used, in which patients were preferentially assigned to doses that would give more information about the ED90 and its efficacy. INTERVENTIONS: Patients in the lecanemab 201 trial were adaptively randomized to 1 of 5 dose regimens or placebo. MAIN OUTCOMES AND MEASURES: The primary end point of lecanemab 201 was the Alzheimer Disease Composite Clinical Score (ADCOMS) at 12 months with continued treatment and follow-up out to 18 months. RESULTS: A total 854 patients were included in trial treatment: 238 were in the placebo group (median age, 72 years [range, 50-89 years]; 137 female [58%]) and 587 were assigned to a lecanemab 201 treatment group (median age, 72 years [range, 50-90 years]; 272 female [46%]). The bayesian approach improved the efficiency of a clinical trial by prospectively adapting to the trial's interim results. By the trial's end more patients had been assigned to the better-performing doses: 253 (30%) and 161 (19%) patients to 10 mg/kg monthly and 10 mg/kg biweekly vs 51 (6%), 52 (6%), and 92 (11%) patients to 5 mg/kg monthly, 2.5 mg/kg biweekly, and 5 mg/kg biweekly, respectively. The trial identified 10 mg/kg biweekly as the ED90. The change in ADCOMS of the ED90 vs placebo was -0.037 at 12 months and -0.047 at 18 months. The bayesian posterior probability that the ED90 was superior to placebo was 97.5% at 12 months and 97.7% at 18 months. The respective probabilities of super-superiority were 63.8% and 76.0%. The primary analysis of the randomized bayesian lecanemab 201 trial found in the context of missing data that the most effective dose of lecanemab nearly doubles its estimated efficacy at 18 months of follow-up in comparison with restricting analysis to patients who completed the full 18 months of the trial. CONCLUSIONS AND RELEVANCE: Innovations associated with the bayesian approach can improve the efficiency of drug development and the accuracy of clinical trials, even in the context of substantial data missingness. TRIAL REGISTRATION: ClinicalTrials.gov Identifier: NCT01767311.

---

### PMID 36336488 — current stance: `inconclusive`

**Stance justification:** > In the first part of this review, we underlined through a meta-analysis that the pooled data from high-clearance anti-amyloid immunotherapies trials demonstrated a significant but slight clinical effect after 18 months.

**Golden note:** Anti-amyloid imm part 2 — implementation/ethics, not efficacy primary.

**High-clearance anti-amyloid immunotherapies in Alzheimer's disease. Part 2: putative scenarios and timeline in case of approval, recommendations for use, implementation, and ethical considerations in France.**

*Revue neurologique*, 2022. Types: Meta-Analysis; Journal Article; Review

> In 2021, aducanumab, an immunotherapy targeting amyloid-β, was approved for Alzheimer's disease (AD) by the US Food and Drug Administration thanks to positive results on a putative biological surrogate marker. This approval has raised an unprecedented controversy. It was followed by a refusal of the European Medicine Agency, which does not allow the marketing of drugs solely on biological arguments and raised safety issues, and important US coverage limitations by the Centers for Medicare & Medicaid Services. Two other anti-amyloid immunotherapies showed significant results regarding a clinical outcome in phase II trials, and five drugs are being studied in phase III trials. Lecanemab is currently under examination for an 'Accelerated Approval' in the US, with an expected decision in January 2023. The common feature and novelty of these anti-amyloid immunotherapies, compared to those tested in previous trials of the 2010s, is their ability to induce a high clearance of amyloid load, as measured with positron emission tomography, in the brain of early-stage biomarker-proven AD patients. In the first part of this review, we underlined through a meta-analysis that the pooled data from high-clearance anti-amyloid immunotherapies trials demonstrated a significant but slight clinical effect after 18 months. Still, safety remains an issue with serious and symptomatic amyloid-related imaging abnormalities, which are seldom (∼1 per 200 treated patients) but occur beyond chance. In the second part of this review, we hypothesized that there is a high probability that some phase III trials of high-clearance anti-amyloid immunotherapies in early AD will finally be unarguably positive on clinical outcomes in the next five years with acceptable safety data. This may, in turn, lead to approval by the European Medicine Agency if the risk-benefit profile is deemed favorable. Such approval would be a game-changer in managing AD patients and for the organization of memory clinics in France. We review the possible timeline and scenarios for putative approval in France and make propositions regarding putative use in clinical practice, putative implementation in a real-life setting, and ethical considerations.

---

### PMID 40011174 — current stance: `inconclusive`

**Stance justification:** > Applying the criterion of amyloid positivity (post mortem report) and the clinical trial inclusion and exclusion criteria to this sample resulted in 83 (9 %), 275 (31 %), and 172 (19 %) participants eligible for treatment with aducanumab, lecanemab, and donanemab, respectively.

**Golden note:** Patient eligibility analysis — descriptive.

**Patient eligibility for amyloid-targeting immunotherapies in Alzheimer's disease.**

*The journal of prevention of Alzheimer's disease*, 2025. Types: Journal Article; Multicenter Study

> BACKGROUND: Amyloid beta (Aβ) targeting immunotherapies have evolved as promising treatment options for patients with early symptomatic Alzheimer's disease (AD). Understanding how eligibilty criteria impact on the number of patients potentially qualifying for treatment is of high relevance for designing diagnostic workflows in clinical practice and for estimating required ressources and costs. OBJECTIVES: We aimed at estimating the number of potentially eligible patients for treatment with the Aβ targeting antibodies aducanumab, lecanemab and donanemab in a specialized center real-world sample by the applying the phase 3 clinical trial and the appropriate use recommendations (AUR) inclusion and exclusion criteria to the data set. The post-mortem report was used for defining amyloid positivity and the presence of AD pathology in this study. DESIGN: Retrospective, descriptive study. SETTING: The multicenter National Alzheimer's Coordinating Center-Uniform Data Set (NACC-UDS) and Neuropathology Data Set (NACCNP). PARTICIPANTS: We included all 3,343 participants of the NACC dataset with available post-mortem pathology reports. MEASUREMENTS/RESULTS: 887 participants were potential candidates for anti-Aβ immunotherapy as they presented with amnestic mild cognitive impairment or mild dementia and the clinical diagnosis of AD (amnestic AD syndrome). Applying the criterion of amyloid positivity (post mortem report) and the clinical trial inclusion and exclusion criteria to this sample resulted in 83 (9 %), 275 (31 %), and 172 (19 %) participants eligible for treatment with aducanumab, lecanemab, and donanemab, respectively. Applying the criteria of the AUR resulted in 242 (27 %) and 266 (30 %) participants eligible for treatment with aducanumab or lecanemab, respectively. The eligible participant groups for each antibody showed partial, but not full overlap. Co-pathologies were common. CONCLUSIONS: The number of eligible participants varies between the different antibodies and the selected groups only partly overlap, indicating partly different groups of eligible participants for each antibody. Since not all inclusion and exclusion criteria can be extracted from the NACC-UDS dataset, the real number of eligible patients will be smaller.

---

### PMID 39432414 — current stance: `supports`

**Stance justification:** > Lecanemab showed the most promise in brain amyloid reduction and decelerating cognitive decline compared to the other therapies.

**Golden note:** Anti-Aβ mAb systematic review — efficacy in AD.

**A systematic review of the efficacy and safety of anti-amyloid beta monoclonal antibodies in treatment of Alzheimer's disease.**

*Expert opinion on biological therapy*, 2024. Types: Systematic Review; Journal Article

> INTRODUCTION: Alzheimer's disease can cause dementia through brain matter degradation. This study investigates the monoclonal antibody usage for AD treatment, following PRISMA 2020 guidelines, and aims to discern the monoclonal antibody that offers the optimal balance of efficacy and safety for individuals with AD. METHODS: A systematic search was conducted across databases such as PubMed, Cochrane Library, and clinical trial registries for randomized controlled trials. The quality of studies was assessed using the Cochrane risk of bias 2 tool. Cognitive function and daily activities were evaluated using MMSE, ADAS-Cog, and CDR-SB test data. RESULTS: According to CDR-SB measurements, lecanemab showed effectiveness in reducing brain amyloid and cognitive decline, with a change from baseline of 1.21. Aducanumab resulted in a decrease of -0.39 (-22%). Bapineuzumab showed no significant benefit, with scores of 2.4 (2.8). Gantenerumab, scoring 1.69 (1.37, 2.01), reduces amyloid, particularly in early Alzheimer's stages. Crenezumab was ineffective, with a score of 3.61. CONCLUSION: The findings provide various perspectives. Lecanemab showed the most promise in brain amyloid reduction and decelerating cognitive decline compared to the other therapies. Further research is needed, highlighting the necessity of AD therapeutic research to alter AD's trajectory and provide reliable treatment. PROTOCOL REGISTRATION: www.crd.york.ac.uk/prospero identifier is CRD42024504358.

---

### PMID 38759015 — current stance: `inconclusive`

**Stance justification:** > High certainty evidence indicated that donanemab (standardized mean difference [SMD] -0.239, 95% confidence interval [CI] -0.343 to -0.134) and lecanemab (SMD -0.194, 95% CI -0.279 to -0.108) moderately slowed the clinical progression in patients with amyloid pathology.

**Golden note:** Pharm + nutritional early AD network meta — broad.

**Pharmacologic and Nutritional Interventions for Early Alzheimer's Disease: A Systematic Review and Network Meta-Analysis of Randomized Controlled Trials.**

*Journal of Alzheimer's disease : JAD*, 2024. Types: Systematic Review; Journal Article; Network Meta-Analysis

> BACKGROUND: Early intervention is essential for meaningful disease modification in Alzheimer's disease (AD). OBJECTIVE: We aimed to determine the efficacy and safety of pharmacologic and nutritional interventions for early AD. METHODS: PubMed, Embase, the Cochrane Library, and ClinicalTrials.gov were searched from database inception until 1 September 2023. We included randomized controlled trials that evaluated the efficacy of interventions in early AD. Only interventions that demonstrated efficacy compared to placebo were included in the network meta-analysis (NMA). Then we performed frequentist fixed-effects NMA to rank the interventions. GRADE criteria were used to evaluate the level of evidence. RESULTS: Fifty-eight trials including a total of 33,864 participants and 48 interventions were eligible for inclusion. Among the 48 interventions analyzed, only 6 (12.5%) treatments- ranging from low to high certainty- showed significant improvement in cognitive decline compared to placebo. High certainty evidence indicated that donanemab (standardized mean difference [SMD] -0.239, 95% confidence interval [CI] -0.343 to -0.134) and lecanemab (SMD -0.194, 95% CI -0.279 to -0.108) moderately slowed the clinical progression in patients with amyloid pathology. Additionally, methylphenidate, donepezil, LipiDiDiet, and aducanumab with low certainty showed significant improvement in cognitive decline compared to placebo. However, there was no significant difference in serious adverse events as reported between the six interventions and placebo. CONCLUSIONS: Only 12.5% of interventions studied demonstrated efficacy in reducing cognitive impairment in early AD. Donanemab and lecanemab have the potential to moderately slow the clinical progression in patients with amyloid pathology. Further evidence is required for early intervention in AD.

---

### PMID 41355080 — current stance: `supports`

**Stance justification:** > Across clinical and HRQoL endpoints, lecanemab-treated participants continued to benefit through 36 months. Separation between early and delayed start was maintained between 18 and 36 months.

**Golden note:** CLARITY-AD OLE 36-month — sustained benefit.

**Long-term safety and efficacy of lecanemab in early Alzheimer's disease: Results from the clarity AD open-label extension study.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2025. Types: Journal Article; Randomized Controlled Trial

> INTRODUCTION: In Clarity AD, lecanemab reduced markers of amyloid in early symptomatic Alzheimer's disease and slowed cognitive and functional decline at 18 months. Herein, we report 36-month data from the ongoing open-label extension (OLE). METHODS: Clarity AD is an 18-month, randomized study (Core), with an OLE where participants received open-label lecanemab. Clinical and health-related quality-of-life (HRQoL) outcomes were evaluated overall and by examining "delayed-start" and "early-start" cohorts. Low pathology (i.e., low baseline amyloid or tau) subgroups were analyzed. RESULTS: ARIA rates were low after 6 months and not associated with long-term progression. Across clinical and HRQoL endpoints, lecanemab-treated participants continued to benefit through 36 months. Separation between early and delayed start was maintained between 18 and 36 months. The low pathology subgroup showed stability or improvement over 18-36 months. DISCUSSION: Benefit continued to accrue with ongoing lecanemab treatment through 36 months. Results in the low pathology subgroup support early initiation of lecanemab treatment. HIGHLIGHTS: This research evaluated the long-term efficacy, safety, and HRQoL results from an ongoing extension of the phase 3 Clarity AD, which included open-label lecanemab treatment for up to 36 months. Overall, the results show participants continue to accrue a lecanemab treatment benefit up to 36 months and highlight the importance of continued long-term lecanemab treatment. Results presented in our paper demonstrate that lecanemab continued suppression of amyloid plaque levels and significantly slowed clinical decline on multiple measures of cognition, function, and quality of life in early AD at 18 months and continued for 36 months to date. No new safety signals were observed with continued lecanemab treatment. After the first 6 months, ARIA rates were low and similar to ARIA rates on placebo, with no association between ARIA occurrence and accelerated long-term clinical progression. Taken together with existing data, these results provide a clear rationale and a demonstration of the disease modification effects of long-term lecanemab therapy.

---

### PMID 38484213 — current stance: `contradicts`

**Stance justification:** > The value of the outcome to participants is not defined in the absolute terms necessary for clinical decision-making, and the difference attributable to lecanemab was between 18% and 46% of estimates of the minimal clinically important difference on the Clinical Dementia Rating Scale Sum of Boxes.

**Golden note:** 'Lecanemab Questions' commentary — critical, raises efficacy concerns.

**Lecanemab Questions.**

*Neurology*, 2024. Types: Comparative Study; Journal Article

> The recently published results of the 18-month randomized controlled trial of lecanemab, reporting the efficacy of the drug in slowing the progression of early Alzheimer disease, quickly led to approval by the FDA and widespread acceptance of lecanemab treatment. However, there are a number of matters that deserve further consideration. The success of blinding was not assessed, even as infusion reactions and the cerebral pathology underlying amyloid-related imaging abnormalities could have signaled to many participants that they were on drug, potentially exerting a potent placebo effect. The value of the outcome to participants is not defined in the absolute terms necessary for clinical decision-making, and the difference attributable to lecanemab was between 18% and 46% of estimates of the minimal clinically important difference on the Clinical Dementia Rating Scale Sum of Boxes. The attenuation of change on the Alzheimer's Disease Assessment Scale-Cognitive 14 achieved by lecanemab at 18 months was 50% of that achieved by donepezil at 6 months. Lecanemab treatment imposes a high treatment burden. The fact that the burden commences at the initiation of lecanemab treatment, whereas the benefit accrues years later requires us to take into account value discounting over time, which would significantly reduce the benefit/burden ratio. Finally, treatment with monoclonal antibodies to cerebral amyloid has consistently been associated with progressive cerebral atrophy. At the least, these issues should be raised in treatment discussions with patients. They also suggest a need to very seriously reconsider how we evaluate clinical trial results preparatory to translating them into clinical practice. Some suggestions are provided.

---

### PMID 40232258 — current stance: `supports`

**Stance justification:** > The Clarity AD phase 3 trial, the AHEAD study, and the DIAN-TU-001 trials have reported positive study outcomes with robust efficacy and safety outcomes with minimal side effects.

**Golden note:** Lecanemab safety/efficacy systematic review — positive.

**Exploring the efficacy and safety of lecanemab in the management of early Alzheimer's disease: A systematic review of clinical evidence.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Systematic Review

> BackgroundAlzheimer's disease (AD) is a growing neurodegenerative disorder causing cognitive decline, memory loss, and functional impairment. Lecanemab has shown safety and efficacy in clinical trials.ObjectiveThis review aims to understand the clinical evidence of lecanemab's effectiveness and safety in managing early AD.MethodsA systematic search was conducted using the Scopus database and ClinicalTrials.gov. Studies from 2014 to 2024 on lecanemab's safety, efficacy, and clinical outcomes for AD were included. Data extraction involved two independent reviewers, with synthesis using qualitative methodology.ResultsFindings from 13 studies and 13 ongoing clinical trials were reported, showing that lecanemab substantially reduces amyloid plaque load in the brains of AD patients. The therapeutic regimens vary across reported studies and trials, ranging from 2.5 mg/kg biweekly, 5 mg/kg monthly, 5 mg/kg biweekly, 10 mg/kg monthly, and 10 mg/kg intravenously biweekly. The Clarity AD phase 3 trial, the AHEAD study, and the DIAN-TU-001 trials have reported positive study outcomes with robust efficacy and safety outcomes with minimal side effects. Completed and ongoing trials report on the onset of amyloid-related imaging abnormalities (ARIA) and the continuation of care status following the onset of ARIA in these patients. The common infusion-related reactions were observed in 26.4% of the lecanemab group compared to 7% in the placebo group.ConclusionsThe management of AD has evolved over the years with the introduction of novel therapeutic agents like lecanemab. While its safety profile is generally favorable, careful monitoring is essential.

---

### PMID 41070709 — current stance: `supports`

**Stance justification:** > Alzheimer's Disease Assessment Scale-Cognitive Subscale 14-item version (ADAS-cog14) scores improved significantly at both follow-ups, and plasma p-tau181 consistently declined.

**Golden note:** China multi-center real-world — efficacy + biomarkers.

**Lecanemab treatment for Alzheimer's Disease of varying severities and associated plasma biomarkers monitoring: A multi-center real-world study in China.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2025. Types: Journal Article; Multicenter Study

> INTRODUCTION: We investigated real-world efficacy, safety, and plasma biomarker dynamics of Lecanemab in Chinese patients with Alzheimer's disease (AD). METHODS: A multi-center prospective cohort study enrolled 68 AD patients. Cognitive scales and plasma biomarkers were assessed at baseline (V0), 2.5 months (V1), and 7 months (V2). RESULTS: Alzheimer's Disease Assessment Scale-Cognitive Subscale 14-item version (ADAS-cog14) scores improved significantly at both follow-ups, and plasma p-tau181 consistently declined. Both p-tau181 and p-tau217 correlated with cognition and partially predicted treatment response (area under the curve [AUC] = 0.734 and 0.713). Mixed-effects modeling confirmed their dynamic association with ADAS-cog14 scores. Subgroup analyses indicated benefits across sex and apolipoprotein E4 status, while moderate-to-severe cases showed limited response. Lecanemab was well tolerated, with asymptomatic amyloid-related imaging abnormalities in 17.65% and mild infusion reactions in 5.88%. DISCUSSION: These findings support the short-term efficacy and safety of Lecanemab in early AD and highlight plasma biomarkers as a treatment-responsive biomarker. HIGHLIGHTS: Lecanemab improved cognitive function in Chinese patients with mild cognitive impairment due to Alzheimer's disease (AD-MCI) and mild AD over a short period. Plasma p-tau181 and p-tau217 showed significant correlation with cognitive scores, and their baseline level could partially predict the efficacy of lecanemab. Lecanemab showed a favorable safety profile with low, manageable rates of amyloid-related imaging abnormalities (ARIA) and infusion reactions.

---

### PMID 40308765 — current stance: `supports`

**Stance justification:** > Meta-analysis results showed that in terms of clinical outcomes, Lecanemab/Donanemab outperformed the control group in ADCOMS, CDR-SB, ADAS-Cog 14, and amyloid burden on PET.

**Golden note:** Re-evaluation lecanemab/donanemab — confirms benefit.

**Re-evaluation of the efficacy and safety of anti-Aβ monoclonal antibodies (lecanemab/donanemab) in the treatment of early Alzheimer's disease.**

*Frontiers in pharmacology*, 2025. Types: Journal Article; Systematic Review

> OBJECTIVE: To systematically evaluate the efficacy and safety of anti-Aβ monoclonal antibodies (Lecanemab/Donanemab) in the treatment of early Alzheimer's disease (AD) and to provide evidence for rational clinical use. METHODS: We searched databases including PubMed, Embase, Cochrane, Web of Science, CNKI, and the Chinese Biomedical Literature Database for relevant literature on the use of anti-Aβ monoclonal antibodies in treating early AD. Two reviewers independently screened the literature, extracted data, and conducted meta-analysis using RevMan 5.4. RESULTS: A total of five clinical studies were included. Meta-analysis results showed that in terms of clinical outcomes, Lecanemab/Donanemab outperformed the control group in ADCOMS, CDR-SB, ADAS-Cog 14, and amyloid burden on PET. Regarding safety, the relative risk of amyloid-related imaging abnormalities (ARIA) in patients treated with Lecanemab/Donanemab was 4.35 times higher than the control group, with significantly higher risks of ARIA-E and ARIA-H. Among other adverse events, the risk of superficial siderosis of the central nervous system was notably higher and statistically significant. CONCLUSION: Lecanemab/Donanemab can improve memory, cognitive function, and daily living abilities in patients with early AD, significantly reduce the composite score of Alzheimer's disease, and inhibit the accumulation of amyloid peptides, thereby alleviating symptoms and improving the condition.

---

### PMID 40386876 — current stance: `inconclusive`

**Stance justification:** > rTMS was significantly more effective than placebo/sham stimulation. In addition, rTMS was significantly more effective than aducanumab, lecanemab, and donanemab.

**Golden note:** Anti-amyloid + rTMS network meta — lecanemab one of many.

**Comparative efficacy, tolerability, and acceptability of aducanumab, lecanemab, and donanemab with repetitive transcranial magnetic stimulation on cognitive function in mild cognitive impairment and Alzheimer's disease: A systematic review and network meta-analysis.**

*Journal of psychopharmacology (Oxford, England)*, 2025. Types: Journal Article; Systematic Review; Comparative Study; Network Meta-Analysis

> BACKGROUND: The U.S. Food and Drug Administration approved three disease-modifying treatments for mild cognitive impairment and early Alzheimer's disease: aducanumab, lecanemab, and donanemab, which showed little efficacy, serious side effects, and are costly. Repetitive transcranial magnetic stimulation (rTMS) may overcome these difficulties by its safe, cheap, and potentially disease-modifying properties that extend beyond Aβ removal. AIMS: We aim to compare the efficacy on cognitive function, tolerability, and acceptability of rTMS with aducanumab, lecanemab, and donanemab in people with mild cognitive impairment and Alzheimer's disease. METHODS: We systematically reviewed relevant randomized placebo-controlled trials in PubMed, the CENTRAL, the CINHAL, and the ClinicalTrials.gov and performed a random-effect network meta-analysis. RESULTS: Nineteen randomized placebo-controlled trials with 6918 participants were included. rTMS was significantly more effective than placebo/sham stimulation. In addition, rTMS was significantly more effective than aducanumab, lecanemab, and donanemab. Furthermore, rTMS was not significantly inferior to placebo/sham stimulation in tolerability and acceptability, whereas aducanumab, lecanemab, and donanemab were significantly inferior to placebo/sham stimulation in tolerability and acceptability. rTMS was significantly superior to lecanemab and donanemab in acceptability. No significant differences were observed in the remaining comparisons. CONCLUSIONS: rTMS may be more effective, tolerable, and acceptable than aducanumab, lecanemab, and donanemab. Long-term direct comparison studies are needed.

---

### PMID 41322352 — current stance: `inconclusive`

**Stance justification:** > Lecanemab provides moderate benefits, while donanemab appears less effective.

**Golden note:** Symptomatic vs disease-modifying meta — comparative.

**Comparative efficacy and safety of symptomatic therapy and disease-modifying therapy for Alzheimer's disease: a systematic review and network meta-analysis.**

*Frontiers in neuroscience*, 2025. Types: Journal Article; Systematic Review

> BACKGROUND: The management of Alzheimer's disease has shifted toward disease-modifying therapies aimed at delaying disease progression rather than focusing solely on symptomatic treatment. This study summarizes the latest evidence regarding the benefits and harms of anti-Alzheimer's disease drugs. METHODS: We conducted a comprehensive review of randomized controlled trials from PubMed, Embase, Cochrane Library, Web of Science databases, and other sources up to April 2025. Two researchers independently reviewed the literature and analyzed the data. A network meta-analysis was performed using Review Manager version 5.3 and Stata version 18.0 to calculate mean differences (MDs) and 95% confidence intervals (CIs) for direct and indirect comparisons. Treatment efficacy was evaluated using the Surface Under the Cumulative Ranking Curve (SUCRA). Bias was assessed using the Revised Cochrane Risk of Bias Tool version 2.0, and publication bias was analyzed with funnel plots. RESULTS: The network meta-analysis included 23 randomized controlled trials with 16,010 participants, evaluating nine pharmacological interventions ranging from traditional symptomatic therapies to four United States Food and Drug Administration- and National Medical Products Administration-approved disease-modifying therapies, notably anti-amyloid beta monoclonal antibodies. Aducanumab significantly improved ADAS-cog scores compared with placebo (MD -5.97, 95%CI -10.33, -1.61; SUCRA: 93.0%) and demonstrated notable improvements in ADCS-ADL scores (MD 4.99, 95%CI 2.27, 7.72; SUCRA: 98.6%). Memantine ranked highest for neuropsychiatric symptoms (SUCRA: 80.8%). Aducanumab also had the highest SUCRA for CDR-SB (91.5%) and showed moderate superiority in MMSE scores (MD 3.55, 95%CI 1.35, 5.75; SUCRA: 98.2%). CONCLUSION: Symptomatic treatments, especially memantine for neuropsychiatric symptoms, remain effective. However, the network meta-analysis indicates that, for patients with mild cognitive impairment or mild Alzheimer's disease, aducanumab demonstrates the greatest potential for cognitive and clinical improvement (MMSE, ADAS-cog, ADCS-ADL), despite associated risks such as adverse events and amyloid-related imaging abnormalities linked to disease-modifying therapies. Lecanemab provides moderate benefits, while donanemab appears less effective. Thus, clinicians should apply disease-modifying therapies cautiously and individually, carefully balancing potential risks and benefits for each patient. SYSTEMATIC REVIEW REGISTRATION: PROSPERO [CRD42025637730], https://www.crd.york.ac.uk/PROSPERO/.

---

### PMID 39269842 — current stance: `inconclusive`

**Stance justification:** > The PPV for ARIA-E was high (0.915), but that for ARIA hemorrhage was low (0.630). Infusion-related reactions had a high PPV of 0.910, but with a wide confidence interval.

**Golden note:** Adverse-events-as-unblinding meta — methodology.

**Adverse Events as a Cause of Unblinding of Allocated Arms in Anti-Amyloid Therapy Trials: A Meta-Analysis of the Predictive Value.**

*Journal of Alzheimer's disease : JAD*, 2024. Types: Meta-Analysis; Journal Article

> Anti-amyloid drugs for early Alzheimer's disease, including lecanemab, are associated with adverse events (AEs), such as amyloid-related imaging abnormalities (ARIA)-edema/effusion (E), ARIA-hemorrhage, and infusion-related reactions, which can indicate allocated arms in clinical trials. Herein, we evaluated the predictive value of AEs using a meta-analysis to estimate their incidence and simulated positive predictive value (PPV). The PPV for ARIA-E was high (0.915), but that for ARIA hemorrhage was low (0.630). Infusion-related reactions had a high PPV of 0.910, but with a wide confidence interval. Our results suggest the need to ameliorate the unblinding effects of AEs, particularly ARIA-E in trials.

---

### PMID 41160347 — current stance: `inconclusive`

**Stance justification:** > Lecanemab utilization followed US FDA-approved prescribing information. Disparities for minority and rural-based populations were observed suggesting opportunities to improve access for underserved populations.

**Golden note:** US real-world descriptive — utilization patterns.

**Initial Real-World Evidence for Lecanemab in the United States.**

*Drugs & aging*, 2025. Types: Journal Article; Observational Study

> BACKGROUND: Lecanemab is the first anti-amyloid monoclonal antibody with full approval in the US for the treatment of early Alzheimer's disease (AD). This observational study aimed to provide information about patient demographics, clinical characteristics, provider specialty, and lecanemab utilization patterns. METHODS: This observational study used open administrative claims from the PurpleLab, a database encompassing medical and pharmacy claims derived from diverse sources, such as clearinghouses and Pharmacies. We included patients receiving one or more lecanemab doses between January 6, 2023 and October 31, 2024, and having continuous clinical activity ≥ 6 months prior to the first lecanemab infusion. The observation period ran from the first lecanemab infusion to the latest clinical activity or data availability. Treatment gaps were calculated as the number of gap days in lecanemab supply between consecutive infusions. RESULTS: Among the study population (n = 4261), mean age was 75.2 years, 77.8% were White, 98.4% lived in urban settings, 81.7% were treated by neurologists, 77.3% had AD, and 31.7% had mild cognitive impairment. Mean follow-up period was 171.1 days. Lecanemab infusions averaged 1.9 per patient per month (SD 1.0), 16.3 days apart (SD 11.0), and 2.8% of patients experienced a treatment interruption ≥90 days. CONCLUSIONS: Lecanemab utilization followed US FDA-approved prescribing information. Disparities for minority and rural-based populations were observed suggesting opportunities to improve access for underserved populations.

---

### PMID 41352683 — current stance: `inconclusive`

**Stance justification:** > Both lecanemab and donanemab showed the greatest slowing of cognitive decline in White/Caucasian patients and apolipoprotein E4 (ApoE4) non-carriers.

**Golden note:** Patient characteristics + efficacy meta — subgroup.

**Influence of patient characteristics on efficacy and safety of anti-amyloid monoclonal antibodies in Alzheimer's disease: A systematic review and meta-analysis.**

*Ageing research reviews*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Lecanemab and donanemab are the first anti-amyloid monoclonal antibodies (mAbs) clinically available as disease-modifying therapies for Alzheimer's disease (AD). However, it remains unclear whether their treatment effects differ across demographic, clinical, or genetic subgroups. OBJECTIVE: This systematic review aimed to explore how patient characteristics modify the efficacy, safety and humanistic outcomes of anti-amyloid mAbs lecanemab and donanemab in patients with early AD. METHODS: A systematic search of MEDLINE, Embase, Scopus, Web of Science, and Cochrane Library was conducted from database inception to July 30th, 2025, using a combination of keywords and Medical Subject Heading terms relating to lecanemab and donanemab. Meta-analyses were conducted for safety outcomes where sufficient data was available. RESULTS: Sixteen studies representing six randomised clinical trials (total N = 5633) were included. Both lecanemab and donanemab showed the greatest slowing of cognitive decline in White/Caucasian patients and apolipoprotein E4 (ApoE4) non-carriers. Amyloid-related imaging abnormalities with edema/effusion (ARIA-E) and microhemorrhages (ARIA-H) were more prevalent in ApoE4 carriers. The risk of ARIA-E was 2.19 times higher (95 %CI:1.91-2.50) and ARIA-H was 3.45 times higher (95 %CI:1.35-8.72) in ApoE4 carriers versus non-carriers. Statistically significant improvements in health-related quality of life were observed with lecanemab in ApoE4 heterozygous participants and in those aged 65-74 years. CONCLUSIONS: The efficacy and safety of anti-amyloid mAbs in AD may differ based on patients' demographic and genetic factors. These findings highlight the potential for personalised treatment strategies and inform national drug policies. Further research is needed to evaluate long-term outcomes and address under-studied patient populations. SUMMARY: The efficacy and safety of lecanemab and donanemab varied across patient subgroups, including age, sex, race/ethnicity and genetic factors such as ApoE4 genotype status. The risk of ARIA was higher in ApoE4 carriers, particularly the homozygous.

---

### PMID 41985900 — current stance: `supports` [FLIP from supports → contradicts]

**Stance justification:** > The effect of amyloid-beta-targeting monoclonal antibodies on cognitive function and dementia severity at 18 months in people with mild cognitive impairment or mild dementia due to Alzheimer's disease is trivial, while on functional ability, it is small at best. Successful removal of amyloid from the brain does not seem to be associated with clinically meaningful effects in people with mild cognitive impairment or mild dementia due to Alzheimer's disease.

**Golden note:** Aβ-mAbs Cochrane-style review — disease-modifying potential.

**Amyloid-beta-targeting monoclonal antibodies for people with mild cognitive impairment or mild dementia due to Alzheimer's disease.**

*The Cochrane database of systematic reviews*, 2026. Types: Journal Article; Systematic Review; Meta-Analysis; Review

> RATIONALE: Alzheimer's disease is a neurodegenerative disorder and the most common cause of dementia. Aggregated amyloid-beta protein deposits are implicated in its pathogenesis. Amyloid-beta-targeting monoclonal antibodies (sometimes represented as Aβ-mAbs) are potentially disease-modifying for Alzheimer's disease: through the clearance of amyloid in the brain, they may slow cognitive and functional decline. OBJECTIVES: To assess the clinical benefits and harms of amyloid-beta-targeting monoclonal antibodies aducanumab, bapineuzumab, crenezumab, donanemab, gantenerumab, lecanemab, ponezumab, remternetug, and solanezumab in people with mild cognitive impairment or mild dementia due to Alzheimer's disease. SEARCH METHODS: We searched CENTRAL, MEDLINE (PubMed), Embase, and two clinical trials registries (Clinicaltrials.gov and WHO International Clinical Trials Registry Platform), and we undertook reference checking and citation research. The most recent search date was 7 August 2025. ELIGIBILITY CRITERIA: We included randomised controlled trials (RCTs) that lasted at least 12 months and compared amyloid-beta-targeting monoclonal antibodies with placebo or no treatment in people with mild cognitive impairment or mild dementia due to Alzheimer's disease. We included both parallel-group and cluster designs. OUTCOMES: Our outcomes of critical importance were: cognitive function; dementia severity; functional ability; any amyloid-related imaging abnormality (ARIA), which includes oedema (E) and haemorrhage (H); any symptomatic ARIA E and H; symptomatic brain haemorrhage; serious adverse events; and any-cause mortality. We analysed data at 12, 18, 24, and over 24 months of treatment. RISK OF BIAS: We used the Cochrane risk of bias tool RoB 2 to assess the risk of bias in outcomes of critical importance. SYNTHESIS METHODS: We meta-analysed results for each outcome within each comparison using the inverse variance method and the random-effects model. We used GRADE to assess the certainty of evidence for each outcome as very low, low, moderate, or high. INCLUDED STUDIES: Overall, we included 17 studies with 20,342 participants. The mean age of participants in the studies ranged from 70 to 74 years. Seven studies enroled only participants with mild dementia, and one study enroled only participants with mild cognitive impairment. The remaining studies included a mixed population. The mean duration of participants' cognitive impairment ranged from 17 to 52 months. The 17 studies assessed seven different amyloid-beta-targeting monoclonal antibodies: aducanumab (n = 3), bapineuzumab (n = 4), crenezumab (n = 2), donanemab (n = 1), gantenerumab (n = 4), lecanemab (n = 1), and solanezumab (n = 2). All used placebo as a comparison. Eleven studies lasted 18 months, four lasted 24 months, and two lasted more than 24 months. All studies were funded by the pharmaceutical industry. SYNTHESIS OF RESULTS: Below, we report the results of the studies at 18 months. Cognitive function Compared to placebo, amyloid-beta-targeting monoclonal antibodies probably result in little to no difference in cognitive function as measured by the ADAS-Cog (Alzheimer's Disease Assessment Scale-Cognitive) scale (standardised mean difference (SMD) -0.11, 95% confidence interval (CI) -0.16 to -0.06; 13 studies, 9895 participants; moderate certainty). Dementia severity Amyloid-beta-targeting monoclonal antibodies may result in little to no difference in dementia severity as measured by the CDR-SB (Clincal Dementia Rating Sum of Boxes) scale (SMD -0.12, 95% CI -0.24 to -0.00; 9 studies, 8053 participants; low certainty). Functional ability Amyloid-beta-targeting monoclonal antibodies probably result in little to no difference in functional ability as measured on the ADCS-ADL (Alzheimer's Disease Cooperative Study - Activities of Daily Living) scale (SMD 0.09, 95% CI 0.03 to 0.16; 3 studies, 3478 participants; moderate certainty) and may result in a small increase in functional ability if measured with the ADCS-iADL (Alzheimer's Disease Cooperative Study-Instrumental Activities of Daily Living) scale (SMD 0.21, 95% CI 0.10 to 0.32; 1 study, 1252 participants; low certainty) or ADCS-ADL-MCI (Alzheimer's Disease Cooperative Study - Activities of Daily Living for Mild Cognitive Impairment) scale (SMD 0.23, 95% CI 0.12 to 0.33; 4 studies, 2802 participants; low certainty). Adverse events Amyloid-beta-targeting monoclonal antibodies probably result in a small increase in the occurrence of any ARIA E (ARD (absolute risk difference) 107 more per 1000, 95% CI 77 more to 148 more; 11 studies, 13,595 participants; moderate certainty) and probably little to no difference in symptomatic ARIA E (ARD 29 more per 1000, 95% CI 22 more to 38 more; 2 studies, 3522 participants; moderate certainty) or symptomatic ARIA H (ARD 4 more per 1000, 95% CI 1 fewer to 31 more; 1 study, 1795 participants; moderate certainty). Three studies assessing any ARIA H showed heterogeneous results (I2 = 81%), which prevented pooled analysis. At 18 months, amyloid-beta-targeting monoclonal antibodies do not increase serious adverse events (ARD 6 more events per 1000, 95% CI 10 fewer to 26 more; 9 studies, 11,904 participants; high certainty) or overall mortality (ARD 2 more events per 1000, 95% CI 3 fewer to 11 more; 7 studies, 9733 participants; high certainty). We judged the overall risk of bias as low for the outcomes of serious adverse events and mortality. We had some concerns about the overall risk of bias for efficacy outcomes, mainly due to the risk of functional unblinding (i.e. participants and investigators correctly guessing whether a participant is receiving the active drug or placebo because of noticeable side effects). AUTHORS' CONCLUSIONS: The effect of amyloid-beta-targeting monoclonal antibodies on cognitive function and dementia severity at 18 months in people with mild cognitive impairment or mild dementia due to Alzheimer's disease is trivial, while on functional ability, it is small at best. Amyloid-beta-targeting monoclonal antibodies increase the risk of amyloid-related imaging abnormalities. Both desirable outcomes and adverse events were inconsistently reported in the studies included in the review. Successful removal of amyloid from the brain does not seem to be associated with clinically meaningful effects in people with mild cognitive impairment or mild dementia due to Alzheimer's disease. Future research on disease-modifying treatments for Alzheimer's disease should focus on other mechanisms of action. FUNDING: This Cochrane review was funded in part by the Drug and Medical Devices Governance Area, Regione Emilia-Romagna, Bologna, Italy. The publication of this article was supported by "Ricerca Corrente" funding from the Italian Ministry of Health. REGISTRATION: Protocol (2025): PROSPERO registration number CRD420251114325.

---

### PMID 41396015 — current stance: `inconclusive`

**Stance justification:** > Overall lecanemab exhibited a manageable short-term safety profile with no measurable cognitive efficacy.

**Golden note:** Real-world Eastern China — baseline + safety.

**Real-world experience with baseline characteristics and safety of lecanemab for Alzheimer's disease in Eastern China.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Multicenter Study

> BackgroundLecanemab reduces amyloid levels and modestly slows cognitive decline in a large cohort of early Alzheimer's disease (AD) but lacks real-world safety data in Chinese population.ObjectiveThe real-world study aims to analyze baseline characteristics and preliminary safety of lecanemab for AD in Zhejiang Province, and to evaluate the efficacy of plasma biomarkers for patient screening.MethodsThis multi-center study included 190 patients with AD in Zhejiang Province, who completed baseline assessments and received lecanemab treatment with follow-up.ResultsThe study included 176 participants with early AD and 14 moderate. In the early AD (mean age 68.04 years, Mini-Mental State Examination 20.03 and Montreal Cognitive Assessment 14.93), 124 (70.5%) participants were female, and 127 (72.1%) were junior high school education level or less. APOE4 heterozygote was predominant (48.9%). Logistic regression for distinguishing early AD from the Aβ negative cognitively unimpaired populations showed that p-Tau 217 independently provided better classification efficacy (area under the curve = 0.9983, p < 0.0001). In the early AD, 29 (16.5%) participants experienced infusion-related reactions (IRR) after the first-dose lecanemab, and amyloid-related imaging abnormalities (ARIA) were identified in 17 patients (9.7%), while 3 (21.4%) with IRR and none ARIA observed in the moderate AD.ConclusionsThe real-world lecanemab cohort had more females, lower educational level, and higher disease burden compared with the clinical trial cohort. Overall lecanemab exhibited a manageable short-term safety profile with no measurable cognitive efficacy. Extensive monitoring and management are required for ARIA of clinically importance. The plasma p-Tau 217 showed high accuracy for early AD screening.

---

### PMID 41428477 — current stance: `inconclusive`

**Stance justification:** > Point estimates of Cohen's d effect sizes on CDR-SB were -0.34, -0.33, and -0.52 for lecanemab, donanemab, and Souvenaid™, respectively, with no statistically significant differences between drugs.

**Golden note:** Effect-size comparison lecanemab/donanemab/Souvenaid.

**Comparing clinical effect sizes of SouvenaidTM, lecanemab, and donanemab in early Alzheimer's disease.**

*Journal of Alzheimer's disease : JAD*, 2025. Types: Journal Article; Comparative Study

> BackgroundLecanemab and donanemab are anti-amyloid-β monoclonal antibodies recently approved in the United States and Europe for the treatment of early Alzheimer's disease (AD). Their modest clinical benefit, safety profile, and cost raise debate about real-world applicability. Fortasyn Connect (SouvenaidTM), a multi-nutrient intervention, has shown potential clinical benefits in prodromal AD.ObjectiveTo compare the clinical effect sizes (Cohen's d) and estimated months of preserved independence in instrumental activities of daily living (IADLs) for lecanemab, donanemab, and Souvenaid™, based on published pivotal clinical trial data.MethodsCohen's d on the Clinical Dementia Rating-Sum of Boxes (CDR-SB) was computed using standardized mean differences and 95% confidence intervals (CIs) derived from published trials. Times of functional independence were estimated using the Hartz approach.ResultsPoint estimates of Cohen's d effect sizes on CDR-SB were -0.34, -0.33, and -0.52 for lecanemab, donanemab, and Souvenaid™, respectively, with no statistically significant differences between drugs. Estimated gains in IADL independence were 10 months for lecanemab, 8 months for donanemab, and 27 months for Souvenaid™.ConclusionsDespite differences in study designs, SouvenaidTM demonstrated comparable clinical efficacy with superior safety, accessibility, and cost profile. These findings support further evaluation of SouvenaidTM as a non-invasive, scalable option in early AD management.

---

### PMID 41478817 — current stance: `inconclusive`

**Stance justification:** > The pooled ARIA incidence was 19% (95% CI: 16%-23%), which was significantly modulated by ApoE4 status (RR 1.45 for heterozygotes, 3.54 for homozygotes vs noncarriers) and the pooled symptomatic ARIA incidence was 3% (95% CI: 2%-4%).

**Golden note:** Lecanemab safety meta — RCT vs RWE comparison.

**Safety profiles of lecanemab: A systematic review and meta-analysis of randomized controlled trials and real-world evidence.**

*The journal of prevention of Alzheimer's disease*, 2026. Types: Journal Article; Systematic Review; Meta-Analysis; Review

> BACKGROUND: Safety profiles of lecanemab, an anti-amyloid-β antibody for the treatment of early Alzheimer's disease (AD), remain uncertain and may vary between randomized controlled trials (RCTs) and real-world evidence (RWE) studies. OBJECTIVES: This systematic review and meta-analysis aimed to evaluate the safety, tolerability, and acceptability of lecanemab based on findings from both RCTs and emerging RWE studies. METHODS: We systematically searched major databases and clinical trial registries from their inception to June 2025. Random-effects meta-analyses were performed to estimate the pooled incidence of key safety outcomes, including amyloid-related imaging abnormalities (ARIA), infusion-related reactions (IRRs), and treatment discontinuation (due to ARIA, adverse events [AEs], or any cause). The risk of ARIA according to the ApoE4 genotype was assessed via relative risk (RR). This study was registered with PROSPERO (No. CRD420251110679). RESULTS: A total of two RCTs and five RWE studies encompassing 1576 patients were included. The pooled ARIA incidence was 19% (95% CI: 16%-23%), which was significantly modulated by ApoE4 status (RR 1.45 for heterozygotes, 3.54 for homozygotes vs noncarriers) and the pooled symptomatic ARIA incidence was 3% (95% CI: 2%-4%). IRRs occurred in 26% (95% CI: 19%-34%), with heterogeneity reduced in patients receiving specific pre-infusion prophylaxis. The pooled rate of discontinuation due to AEs was 8% (95% CI: 5%-11%), with discontinuation due to ARIA occurring in 5% (95% CI: 3%-7%) of patients in RWE studies. CONCLUSIONS: Lecanemab-related ARIA demonstrates a clear ApoE4 gene-dose effect, supporting routine ApoE4 genotyping before treatment. Standardizing pre-infusion prophylaxis may reduce variability in IRRs incidence, while prompt recognition and management of ARIA are critical for improving treatment tolerability. These findings provide important evidence to support the safe clinical use of lecanemab.

---

### PMID 41823189 — current stance: `supports`

**Stance justification:** > Lecanemab significantly attenuated cognitive decline versus ADNI.

**Golden note:** China multicenter real-world — effectiveness confirmed.

**Effectiveness, safety, and biomarker dynamics of lecanemab in Chinese Alzheimer's disease population: a multicenter real-world study.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2026. Types: Journal Article; Multicenter Study

> BACKGROUND: Lecanemab, an anti-amyloid beta (Aβ) protofibril antibody, was introduced in China in 2024, but its real-world performance remains unknown. METHODS: In this prospective, multicenter study across 21 sites, 261 Alzheimer's disease patients (mild cognitive impairment to moderate dementia) received biweekly lecanemab (10 mg/kg). A matched Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort served as comparator. Cognitive tests, plasma biomarkers, and optional amyloid/tau positron emission tomography (PET) were assessed over 6 months. RESULTS: Lecanemab significantly attenuated cognitive decline versus ADNI. Plasma Aβ42, Aβ40, phosphorylated tau 217 (p‑tau217), glial fibrillary acidic protein (GFAP), and ratios showed robust changes; a p‑tau217 reduction correlated with amyloid PET clearance (mean -22.1 Centiloid; 29.2% turned amyloid-negative). Apolipoprotein E (APOE) ε4 non-carriers showed greater improvements. Infusion reactions occurred in 11.1% and amyloid-related imaging abnormalities in 9.2% (1.6% symptomatic), with no stage-related safety differences. CONCLUSION: Lecanemab was effective and well tolerated in real-world Chinese patients. Plasma p‑tau217 may serve as a sensitive, minimally invasive treatment-response biomarker.

---

### PMID 41581261 — current stance: `inconclusive`

**Stance justification:** > Our findings suggest that ARIA is a significant concern especially in patients who are ε4 homozygous.

**Golden note:** Regional center 2-year — mostly safety/AE.

**Lecanemab over a two-year duration: Key insights from a regional specialty medical center.**

*The journal of prevention of Alzheimer's disease*, 2026. Types: Journal Article; Observational Study

> BACKGROUND AND OBJECTIVES: The anti-amyloid monoclonal antibody lecanemab (Leqembi®) treats patients with mild cognitive impairment (MCI) or mild dementia due to Alzheimer's disease (AD). We sought to evaluate the incidence of amyloid-related imaging abnormalities) ARIA and other adverse events associated with lecanemab. DESIGN, SETTING, AND PARTICIPANTS: This retrospective and observational study features 187 patients who received at least one lecanemab infusion at our multidisciplinary Norton Neuroscience Institute Memory Center over a two-year duration (August 25, 2023-August 24, 2025). RESULTS: A total of 109 (58.3 %) patients were diagnosed with MCI, and 78 (41.7 %) had mild dementia prior to starting lecanemab. The mean age at the initial infusion was 73 years (Range: 49-90 years). Most (127 [67.9 %]) patients were female, and the majority (181 [96.8 %]) were Caucasian. Of the 175 patients who underwent at least one surveillance brain MRI following lecanemab initiation, 39 (22.3 %) had evidence of ARIA (both ARIA-H and ARIA-E: 13 [33.3 %]; solitary ARIA-H: 17 [43.6 %]; and solitary ARIA-E: 9 [23.1 %]). Of these 39 patients, 20 (51.3 %) were ε4 heterozygous, 12 (30.8 %) were ε4 homozygous, and 7 (17.9 %) were ε4 non-carriers. Patients who were ε4 homozygous more frequently had evidence of any ARIA (p-value = 0.002), ARIA-E (p = 0.041), and ARIA-H (p = 0.004). Of the 25 patients who underwent at least one surveillance brain MRI and were ε4 homozygous, 12 (48.0 %) had ARIA detected. Five (12.8 %) patients with ARIA were symptomatic, requiring lecanemab suspension. Three of these symptomatic patients were ε4 homozygous, and two were ε4 heterozygous. The ARIA was most frequently detected on the surveillance brain MRI performed before the 5th infusion (29 [74.4 %] patients). All 39 cases of ARIA occurred before the 14th lecanemab infusion. Patients with more baseline microbleeds more frequently developed any ARIA (ARIA-H and ARIA-E) (p = 0.041) and solitary ARIA-H (p = 0.022). The presence of baseline microbleeds was associated with a higher frequency of solitary ARIA-H, though was only marginally statistically significant (p = 0.051). Sixty (32.1 %) patients experienced infusion-related adverse effects, with 54 (90.0 %) occurring after the first lecanemab infusion. Mild and transient headaches were most common, affecting 26 (48.1 %) of these patients after the first infusion. After initiating a pre-infusion oral cocktail of acetaminophen 650 mg, loratadine 10 mg, and famotidine 20 mg, the number of patients who experienced an infusion-related adverse event decreased from 45.2 % to 28.3 %. Thirty-two (17.1 %) patients discontinued lecanemab, primarily due to cognitive decline associated with progressive AD (10 [31.2 %]) and ARIA progression (9 [28.1 %]). Of the 73 patients who had MMSE scores performed at baseline and after 1 year post-lecanemab, 13 (17.8 %) had increased scores, 51 (69.9 %) had decreased scores, and the scores remained the same in 9 (12.3 %) patients. CONCLUSIONS: Our findings suggest that ARIA is a significant concern especially in patients who are ε4 homozygous. Close monitoring of patients who are ε4 carriers is recommended to recognize any complications that may ensue.

---

### PMID 41689888 — current stance: `supports`

**Stance justification:** > Lecanemab significantly reduced clinical decline on CDR-SB at 18 months compared to placebo in the ApoEε4 heterozygotes or non-carriers subgroup.

**Golden note:** CLARITY-AD APOE non-carrier/heterozygote subgroup — meaningful delay.

**Lecanemab for treatment of individuals with early Alzheimer's Disease (AD) who are apolipoprotein E ε4 (ApoE ε4) non-carriers or heterozygotes.**

*The journal of prevention of Alzheimer's disease*, 2026. Types: Journal Article; Randomized Controlled Trial; Multicenter Study

> BACKGROUND: Lecanemab, an antibody directed at Aβ-protofibrils and plaque, showed meaningful delay in disease progression and biological effects consistent with disease modification in the phase 3 Clarity AD trial. OBJECTIVE: The objective of this paper is to present efficacy and safety results in ApoE ε4 non-carriers or heterozygotes population of Clarity AD. DESIGN: Clarity AD is an 18-month, randomized study (core) in participants with early AD, with an open-label extension phase (OLE) phase. SETTING: Academic and clinical centers. PARTICIPANTS: All eligible ApoE ε4 participants were randomized 1:1 across 2 treatment groups (placebo and lecanemab 10 mg/kg biweekly); the results presented herein are for the ApoE4 heterozygote or non-carrier participants. MEASUREMENTS: Endpoints included change from baseline at 18 months in the global cognitive and functional scale, CDR-SB, amyloid positron emission tomography (PET), Alzheimer's Disease Assessment Scale-Cognitive Subscale 14 (ADAS-Cog14), Alzheimer's Disease Cooperative Study-Activities of Daily Living Scale for Mild Cognitive Impairment (ADCS-MCI-ADL), and health-related quality-of-life (HRQoL) assessments. Amyloid imaging related abnormalities (ARIA) occurrence was monitored throughout the study by central reading of magnetic resonance imaging. Following 18 months treatment in the Core, eligible participants transitioned to the OLE where they received open-label lecanemab. Clinical outcomes (CDR-SB, ADAS-Cog14, and ADCS-MCI-ADL) were evaluated by examining 'delayed start' (core:placebo followed by OLE:lecanemab) and 'early start' (core:lecanemab followed by OLE:lecanemab) cohorts as well as natural history cohorts. Time to progression to next stage of AD was also evaluated through 36 months. RESULTS: 1795 participants with early AD were enrolled in Clarity AD, of which 1521 were ApoE ε4 heterozygotes or non-carriers (85 %). Lecanemab significantly reduced clinical decline on CDR-SB at 18 months compared to placebo in the ApoEε4 heterozygotes or non-carriers subgroup. Amyloid PET, ADAS-Cog14, ADCS-MCI-ADL, and HRQoL results were consistent with the CDR-SB findings. In the analysis subgroup, the most common adverse reactions for lecanemab were infusion-related reactions (26 %), ARIA-H (13 %), fall (11 %), headache (11 %), and ARIA-E (9 %). In the OLE, lecanemab-treated participants continued to accrue benefit in CDR-SB through 36 months, with continued separation through 36 months relative to the ADNI natural history cohort. Delayed start results follow a parallel trajectory relative to early start results, but do not catch up, confirming a disease modifying effect and reflecting importance of early treatment initiation. Results were similar for ADAS-Cog14 and ADCS-MCI-ADL. Lecanemab reduced the risk of progression to next stage of AD by 28 % on lecanemab as compared to the ADNI natural history cohort. CONCLUSION: In the ApoE ε4 heterozygotes or non-carrier subgroup of Clarity AD, lecanemab slowed decline in disease progression and reduced markers of amyloid, with expanding benefit over time. GOV IDENTIFIER: Clarity AD NCT03887455.

---

