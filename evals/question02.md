# Q2: Is donepezil effective for mild cognitive impairment (not yet AD)?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`
for the bar definitions).

n=17 PMIDs.

**Current S/C/I**: 1 / 3 / 13
**Proposed S/C/I**: 1 / 7 / 9
**Net flips**: 4 (all I → C)

`expected_consensus: "mostly negative"` is well-supported by the data — with
the proposed flips the count becomes 7 contradicts vs 1 supports.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `18044984` | 2007 | **inconclusive → contradicts** | SR of 8 RCTs; conclusion verbatim: *"The use of ChEIs in MCI was not associated with any delay in the onset of AD or dementia."* All point estimates non-sig. Meets "evidence does not support" bar. |
| `15326237` | 2004 | **inconclusive → contradicts** | 24-week donepezil RCT in MCI, n=270. *"Primary efficacy measures... did not show significant treatment effects in the ITT population."* Adequately-powered RCT primary endpoint missed. |
| `19176895` | 2009 | **inconclusive → contradicts** | 48-week donepezil RCT in MCI, n=821 (large multicenter). *"The dual primary efficacy endpoint was not reached."* Adequately-powered RCT primary endpoint missed. One of two co-primaries (modified ADAS-Cog) hit; CDR-SB (functional co-primary) was null. A dual endpoint is not "rescued" by hitting just one half. |
| `16856114` | 2006 | **inconclusive → contradicts** | Cochrane review of donepezil in MCI. Conclusion verbatim: *"There is no evidence to support the use of donepezil for patients with MCI. The putative benefits are minor, short lived and associated with significant side effects."* Plus the second included study reported HR 0.84 (CI 0.57–1.25, p=0.4) for AD onset at 3 years — primary missed. The "evidence does not support" trigger language is as clean here as in `18044984`. |

### Borderline (not flipped, but flagged for cross-question policy decisions)

| PMID | Year | Status | Notes |
|------|------|--------|-------|
| `15829527` | 2005 | **inconclusive (keep)** | Petersen/NEJM, n=769, 3-year. Primary endpoint (HR 0.80, p=0.42) **missed at 36mo** but transient benefit at 12mo + APOE4 subgroup signal throughout the 3 years. Strict-bar reading favors `contradicts` (adequately-powered RCT, primary endpoint missed at the named timepoint). `inconclusive` is defensible because of the pre-specified 12mo signal and APOE4 subgroup. Decision depends on **policy**: do regression-to-null patterns where an early significant signal does not hold at the primary timepoint count as `contradicts` or `inconclusive`? Apply uniformly across all 20 questions. |
| `19528519` | 2009 | **supports (keep)** | Depression-positive subgroup of the Petersen ADCS trial. The bar's `supports` slot requires a *significant positive primary clinical finding* or a *meta-analysis pooled effect favoring the intervention* — a pre-specified subgroup analysis of a parent trial whose overall primary missed at 36mo does not cleanly meet either. Strict-bar reading favors `inconclusive` ("subgroup-dependent" mixed signal). `supports` is defensible only if the policy is to honor pre-specified-ish subgroup signals as supports. Decide once, apply uniformly. |
| `30565793` | 2018 | **contradicts (keep, second-review flagged)** | Gait/falls RCT in MCI, n=60. Primary (gait speed) non-sig; two of three dual-task gait cost (DTC) secondaries hit (p=0.048, p=0.037). Conclusion: *"Donepezil treatment improved dual-task gait speed and DTC."* Strict-bar reading: missed primary + significant functional secondaries = `inconclusive` (genuinely mixed signal), not `contradicts`. The current `contradicts` understates the DTC results. Recommend re-evaluation; the call here depends on whether motor-cognitive interaction is a meaningful "functional" outcome under this question's frame. |

## Confirmed (no change)

- `32096857` (2020 USPSTF) — **contradicts ✓**
- `24043661` (2013 meta, MMSE/ADAS-Cog/ADL all null) — **contradicts ✓**
- `27567841`, `26876309`, `37353809` (subtype/predictor analyses) —
  **inconclusive ✓**
- `19001543` (fMRI pilot) — **inconclusive ✓**
- `17330176` (2007 meta; small risk reduction with high adverse events) —
  **inconclusive ✓** (borderline; "questionable efficacy:risk ratio" hedge
  could read as `contradicts`, but the 24% RR reduction is real)
- `26091818`, `39939901` (atrophy outcome only) — **inconclusive ✓**
- `19949165` (open-label safety extension) — **inconclusive ✓**

(`15829527`, `19528519`, `30565793` moved to the Borderline section above.)

## Cross-cutting issues

- **`15829527` is the parent Petersen trial; `27567841`, `26876309`,
  `19528519` are all secondary analyses of this one cohort.** Should be
  tagged as substudies for the planned UI filter. Note: this means the
  one remaining `supports` vote (`19528519`) is itself a substudy of a
  parent trial whose primary endpoint missed.
- After flips: 7 contradicts vs 1 supports — the "mostly negative" expected
  consensus is now properly reflected.
- **Cross-question policy questions raised here** (need to be settled
  uniformly across all 20 questions):
  1. Does a pre-specified subgroup signal in a parent-null trial qualify as
     `supports`, or is it `inconclusive`? (`19528519` hinges on this.)
  2. Does an adequately-powered RCT with a significant early-timepoint
     signal that does not hold at the named primary timepoint count as
     `contradicts` or `inconclusive`? (`15829527` hinges on this.)
  3. Does a missed primary with significant secondary functional outcomes
     count as `contradicts` or `inconclusive`? (`30565793` hinges on this.)

## Highest-confidence flips for this question

All four proposed flips are high-confidence — two large RCTs with primary
endpoints explicitly missed (`15326237`, `19176895`), plus two systematic
reviews with "evidence does not support" / "not associated with any delay"
language (`18044984`, `16856114`). No interpretive ambiguity in any of the
four conclusion statements.

## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

- `15829527` — `same_cohort_duplicate` (Petersen ADCS parent), `missed_primary_sig_secondary` (12-mo signal didn't hold at 36-mo named primary)
- `27567841` — `same_cohort_duplicate` (Petersen ADCS substudy), `subgroup_positive` (APOE4/BCHE-K pharmacogenomic subgroup of parent-null)
- `26876309` — `same_cohort_duplicate` (Petersen-adjacent, NCT00403520), `subgroup_positive`
- `19528519` — `same_cohort_duplicate` (Petersen ADCS substudy), `subgroup_positive` (depression-positive subgroup of parent-null trial)
- `30565793` — `missed_primary_sig_secondary` (gait-speed primary missed; DTC secondaries hit p=0.048, p=0.037)
- `19176895` — `missed_primary_sig_secondary` (dual co-primary not reached; modified ADAS-Cog hit but CDR-SB null)
- `19001543` — `pilot_positive`-adjacent (fMRI pilot, biomarker-only, no cognitive primary)
- `19949165` — (none — open-label safety extension, correctly inconclusive)
- `26091818`, `39939901` — (atrophy-only outcomes; correctly inconclusive)
- `37353809` — `subgroup_positive` (MRI-subtype-restricted treatment response)
- `17330176` — `hedged_meta` (24% RR reduction but authors call efficacy:risk ratio "questionable")
- `16856114` — (none — Cochrane "no evidence to support" is clean contradicts)
- All other pmids — untagged

---

## Abstracts (n=17)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 18044984 — current stance: `inconclusive`

**Evidence span:** > The use of ChEIs in MCI was not associated with any delay in the onset of AD or dementia.

**Golden note:** Systematic review of ChEIs in MCI — small effects, marginal.

**Cholinesterase inhibitors in mild cognitive impairment: a systematic review of randomised trials.**

*PLoS medicine*, 2007. Types: Journal Article; Systematic Review

> BACKGROUND: Mild cognitive impairment (MCI) refers to a transitional zone between normal ageing and dementia. Despite the uncertainty regarding the definition of MCI as a clinical entity, clinical trials have been conducted in the attempt to study the role of cholinesterase inhibitors (ChEIs) currently approved for symptomatic treatment of mild to moderate Alzheimer disease (AD), in preventing progression from MCI to AD. The objective of this review is to assess the effects of ChEIs (donepezil, rivastigmine, and galantamine) in delaying the conversion from MCI to Alzheimer disease or dementia. METHODS AND FINDINGS: The terms "donepezil", "rivastigmine", "galantamine", and "mild cognitive impairment" and their variants, synonyms, and acronyms were used as search terms in four electronic databases (MEDLINE, EMBASE, Cochrane, PsycINFO) and three registers: the Cochrane Collaboration Trial Register, Current Controlled Trials, and ClinicalTrials.gov. Published and unpublished studies were included if they were randomized clinical trials published (or described) in English and conducted among persons who had received a diagnosis of MCI and/or abnormal memory function documented by a neuropsychological assessment. A standardized data extraction form was used. The reporting quality was assessed using the Jadad scale. Three published and five unpublished trials met the inclusion criteria (three on donepezil, two on rivastigmine, and three on galantamine). Enrolment criteria differed among the trials, so the study populations were not homogeneous. The duration of the trials ranged from 24 wk to 3 y. No significant differences emerged in the probability of conversion from MCI to AD or dementia between the treated groups and the placebo groups. The rate of conversion ranged from 13% (over 2 y) to 25% (over 3 y) among treated patients, and from 18% (over 2 y) to 28% (over 3 y) among those in the placebo groups. Only for two studies was it possible to derive point estimates of the relative risk of conversion: 0.85 (95% confidence interval 0.64-1.12), and 0.84 (0.57-1.25). Statistically significant differences emerged for three secondary end points. However, when adjusting for multiple comparisons, only one difference remained significant (i.e., the rate of atrophy in the whole brain). CONCLUSIONS: The use of ChEIs in MCI was not associated with any delay in the onset of AD or dementia. Moreover, the safety profile showed that the risks associated with ChEIs are not negligible. The uncertainty regarding MCI as a clinical entity raises the question as to the scientific validity of these trials.

---

### PMID 15326237 — current stance: `inconclusive`

**Evidence span:** > Primary efficacy measures of the NYU Paragraph Recall test and the ADCS CGIC-MCI did not show significant treatment effects in the ITT population.

**Golden note:** 24-week donepezil RCT in MCI — limited efficacy on primary, mixed.

**Efficacy of donepezil in mild cognitive impairment: a randomized placebo-controlled trial.**

*Neurology*, 2004. Types: Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> OBJECTIVE: To evaluate the efficacy and safety of the acetylcholinesterase inhibitor donepezil in a placebo-controlled trial in patients with mild cognitive impairment (MCI). METHODS: A total of 270 patients with MCI were enrolled in a 24-week, multicenter, randomized, double-blind, placebo-controlled study. Patients were randomized to receive donepezil (n = 133; 5 mg/day for 42 days, followed by forced dose escalation to 10 mg/day) or placebo (n = 137). Primary efficacy measures were the New York University (NYU) Paragraph Delayed Recall test and the Alzheimer disease (AD) Cooperative Study Clinician's Global Impression of Change for MCI (ADCS CGIC-MCI). Secondary efficacy measures included the modified AD Assessment Scale-cognitive subscale (ADAS-cog), the Patient Global Assessment (PGA), and additional neuropsychologic measures. Efficacy analyses were performed on intent-to-treat (ITT) and fully evaluable (FE) populations. RESULTS: Primary efficacy measures of the NYU Paragraph Recall test and the ADCS CGIC-MCI did not show significant treatment effects in the ITT population. Some secondary measures showed effects favoring donepezil. More donepezil-treated patients showed improvements in ADAS-cog total scores, in tests of attention and psychomotor speed, and in PGA scores. More donepezil-treated than placebo-treated patients experienced adverse events, most of which were mild to moderate and transient. CONCLUSION: Although significant treatment effects were not seen in the primary efficacy measures, outcomes on secondary measures suggest promising directions for further evaluation of donepezil treatment in patients with MCI.

---

### PMID 32096857 — current stance: `contradicts`

**Evidence span:** > There is no empirical evidence, however, that screening for cognitive impairment improves patient or caregiver outcomes or causes harm. It remains unclear whether interventions for patients or caregivers provide clinically important benefits for older adults with earlier detected cognitive impairment or their caregivers.

**Golden note:** USPSTF review — insufficient/no benefit of pharmacologic treatment for MCI.

**Screening for Cognitive Impairment in Older Adults: Updated Evidence Report and Systematic Review for the US Preventive Services Task Force.**

*JAMA*, 2020. Types: Journal Article; Research Support, U.S. Gov't, P.H.S.; Systematic Review

> IMPORTANCE: Early identification of cognitive impairment may improve patient and caregiver health outcomes. OBJECTIVE: To systematically review the test accuracy of cognitive screening instruments and benefits and harms of interventions to treat cognitive impairment in older adults (≥65 years) to inform the US Preventive Services Task Force. DATA SOURCES: MEDLINE, PubMed, PsycINFO, and Cochrane Central Register of Controlled Trials through January 2019, with literature surveillance through November 22, 2019. STUDY SELECTION: Fair- to good-quality English-language studies of cognitive impairment screening instruments, and pharmacologic and nonpharmacologic treatments aimed at persons with mild cognitive impairment (MCI), mild to moderate dementia, or their caregivers. DATA EXTRACTION AND SYNTHESIS: Independent critical appraisal and data abstraction; random-effects meta-analyses and qualitative synthesis. MAIN OUTCOMES AND MEASURES: Sensitivity, specificity; patient, caregiver, and clinician decision-making; patient function, quality of life, and neuropsychiatric symptoms; caregiver burden and well-being. RESULTS: The review included 287 studies with more than 280 000 older adults. One randomized clinical trial (RCT) (n = 4005) examined the direct effect of screening for cognitive impairment on patient outcomes, including potential harms, finding no significant differences in health-related quality of life at 12 months (effect size, 0.009 [95% CI, -0.063 to 0.080]). Fifty-nine studies (n = 38 531) addressed the accuracy of 49 screening instruments to detect cognitive impairment. The Mini-Mental State Examination was the most-studied instrument, with a pooled sensitivity of 0.89 (95% CI, 0.85 to 0.92) and specificity of 0.89 (95% CI, 0.85 to 0.93) to detect dementia using a cutoff of 23 or less or 24 or less (15 studies, n = 12 796). Two hundred twenty-four RCTs and 3 observational studies including more than 240 000 patients or caregivers addressed the treatment of MCI or mild to moderate dementia. None of the treatment trials were linked with a screening program; in all cases, participants were persons with known cognitive impairment. Medications approved to treat Alzheimer disease (donepezil, galantamine, rivastigmine, and memantine) improved scores on the ADAS-Cog 11 by 1 to 2.5 points over 3 months to 3 years. Psychoeducation interventions for caregivers resulted in a small benefit for caregiver burden (standardized mean difference, -0.24 [95% CI, -0.36 to -0.13) over 3 to 12 months. Intervention benefits were small and of uncertain clinical importance. CONCLUSIONS AND RELEVANCE: Screening instruments can adequately detect cognitive impairment. There is no empirical evidence, however, that screening for cognitive impairment improves patient or caregiver outcomes or causes harm. It remains unclear whether interventions for patients or caregivers provide clinically important benefits for older adults with earlier detected cognitive impairment or their caregivers.

---

### PMID 19176895 — current stance: `inconclusive`

**Evidence span:** > The dual primary efficacy endpoint was not reached. We noted a small, but significant, decrease in modified ADAS-Cog scores in favor of donepezil at study endpoint.

**Golden note:** 48-week donepezil RCT in MCI — modest benefit, not definitive.

**Donepezil treatment of patients with MCI: a 48-week randomized, placebo-controlled trial.**

*Neurology*, 2009. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Treatment of mild cognitive impairment (MCI) with cholinesterase inhibitors may improve symptoms. METHODS: In this multicenter, randomized, placebo-controlled trial, subjects with MCI entered a 3-week placebo run-in period followed by 48 weeks of double-blind donepezil (5 mg/day for 6 weeks, then 10 mg/day for 42 weeks) or placebo treatment. Primary efficacy variables included change from baseline in the modified Alzheimer Disease Assessment Scale-cognitive subscale (ADAS-Cog) and Clinical Dementia Rating Scale-sum of boxes (CDR-SB) after 48 weeks of treatment (modified intention-to-treat analysis). Secondary efficacy measures evaluated cognition, behavior, and function. RESULTS: The dual primary efficacy endpoint was not reached. We noted a small, but significant, decrease in modified ADAS-Cog scores in favor of donepezil at study endpoint. Little change from baseline in CDR-SB and secondary variables was observed for either group. Patient Global Assessment scores favored donepezil at all time points except week 12 (p < or = 0.05). Perceived Deficits Questionnaire scores favored donepezil at week 24 (p = 0.05). Clinical Global Impression of Change-MCI scores favored donepezil only at week 6 (p = 0.04). Adverse events were generally mild or moderate. More donepezil-treated subjects (18.4%) discontinued treatment due to adverse events than placebo-treated subjects (8.3%). CONCLUSIONS: Donepezil demonstrated small but significant improvement on the primary measure of cognition but there was no change on the primary measure of global function. Most other measures of global impairment, cognition, and function were not improved, possibly because these measures are insensitive to change in MCI. Responses on subjective measures suggest subjects perceived benefits with donepezil treatment.

---

### PMID 24043661 — current stance: `contradicts`

**Evidence span:** > Cognitive enhancers did not improve cognition or function among patients with mild cognitive impairment and were associated with a greater risk of gastrointestinal harms. Our findings do not support the use of cognitive enhancers for mild cognitive impairment.

**Golden note:** Meta-analysis: cognitive enhancers in MCI lack efficacy.

**Efficacy and safety of cognitive enhancers for patients with mild cognitive impairment: a systematic review and meta-analysis.**

*CMAJ : Canadian Medical Association journal = journal de l'Association medicale canadienne*, 2013. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: Cognitive enhancers, including cholinesterase inhibitors and memantine, are used to treat dementia, but their effectiveness for mild cognitive impairment is unclear. We conducted a systematic review to examine the efficacy and safety of cognitive enhancers for mild cognitive impairment. METHODS: Our eligibility criteria were studies of the effects of donepezil, rivastigmine, galantamine or memantine on mild cognitive impairment reporting cognition, function, behaviour, global status, and mortality or harms. We identified relevant material by searching electronic databases (e.g., MEDLINE, Embase), the references of included studies, trial registries and conference proceedings, and by contacting experts. Two reviewers independently screened the results of the literature search, abstracted data and appraised risk of bias using the Cochrane risk-of-bias tool. RESULTS: We screened 15,554 titles and abstracts and 1384 full-text articles. Eight randomized clinical trials and 3 companion reports met our inclusion criteria. We found no significant effects of cognitive enhancers on cognition (Mini-Mental State Examination: 3 randomized clinical trials [RCTs], mean difference [MD] 0.14, 95% confidence interval [CI] -0.22 to 0.50; Alzheimer's Disease Assessment Scale - cognition subscale: 3 RCTs, standardized MD -0.07, 95% CI-0.16 to 0.01]) or function (Alzheimer's Disease Cooperative Study activities of daily living inventory: 2 RCTs, MD 0.30, 95% CI -0.26 to 0.86). Cognitive enhancers were associated with higher risks of nausea, diarrhea and vomiting than placebo. INTERPRETATION: Cognitive enhancers did not improve cognition or function among patients with mild cognitive impairment and were associated with a greater risk of gastrointestinal harms. Our findings do not support the use of cognitive enhancers for mild cognitive impairment.

---

### PMID 16856114 — current stance: `inconclusive`

**Evidence span:** > There is no evidence to support the use of donepezil for patients with MCI. The putative benefits are minor, short lived and associated with significant side effects.

**Golden note:** Cochrane review of donepezil for MCI — uncertain benefit.

**Donepezil for mild cognitive impairment.**

*The Cochrane database of systematic reviews*, 2006. Types: Journal Article; Systematic Review

> BACKGROUND: Problems with memory which do not meet the diagnostic criteria for dementia, usually called mild cognitive impairment (MCI), can be the first sign of an impending dementia, particularly Alzheimer's disease (AD). There is no consensus on a definition or diagnostic criteria for MCI, and MCI remains a vague term and those so described are a heterogeneous population, consisting of people who may rapidly progress to dementia but also of people with stable cognitive deficits and some who may actually improve. Treatment in the very earliest stages of AD may delay progression to AD. Donepezil (Aricept, E2020), a cholinesterase inhibitor, has been shown to benefit all severities of AD including mild and it would be reasonable to investigate its efficacy for those with MCI. OBJECTIVES: To assess the effects of donepezil in people with mild cognitive impairment but no diagnosis of dementia. SEARCH STRATEGY: The trials were identified from a search of the Specialized Register of the Cochrane Dementia and Cognitive Improvement Group on 6 January 2006. This register contains records from major health care databases like CENTRAL, MEDLINE, EMBASE, CINAHL and PsycINFO and many ongoing trial databases and is updated regularly. SELECTION CRITERIA: All double blind, randomized trials in which treatment with donepezil was compared with placebo for patients with mild cognitive impairment. DATA COLLECTION AND ANALYSIS: Data were extracted from the published reports of the included studies, pooled where appropriate and the treatment effects or the risks and benefits estimated. MAIN RESULTS: The two included studies, with a total of 782 patients, all with a MMSE greater than 23 points, identified similar patients for inclusion, but were quite different with respect to design and objective. Pooling results in a meta-analysis was not possible. In the first study the 13-item ADAS-Cog showed benefit associated with 10 mg/day donepezil compared with placebo at 24 weeks (MD 1.90, 95% CI 0.51 to 3.29, p=0.007), but four other measures of cognitive function did not. The analysis of withdrawals before the end of treatment at 24 weeks, withdrawals due to an adverse event, and numbers experiencing an adverse event, showed a significant difference between the donepezil group and the placebo group in favour of placebo, (43/133 donepezil 23/137 placebo, OR 2.37, 95% CI 1.33 to 4.22, p=0.003), (29/133 donepezil 10/137 placebo, OR 3.54, 95% CI 1.65 to 7.60, p=0.001), (116/133 donepezil, 100/137 placebo, OR 2.52 95% CI 1.34 to 4.76, p=0.004). Various adverse effects were recorded, and several types of event, diarrhoea, nausea, vomiting, leg cramps and abnormal dreams, were reported more frequently in the donepezil group compared with the placebo. In the second study there was a significant difference between the number of patients diagnosed with AD or another dementia between the donepezil group and the placebo group in favour of donepezil after one year of treatment (16/253 donepezil 38/259 placebo) (OR 0.39, 95% CI 0.21 to 0.72, p=0.003), but no difference after 3 years of treatment (63/253 donepezil 73/259 placebo) (OR 0.84, 95% CI 0.57 to 1.25, p=0.4). AUTHORS' CONCLUSIONS: There are two included studies. One study demonstrated a modest treatment effect in cognitive function as assessed by ADAS-Cog13 but not for other outcomes assessing different domains of cognitive function. Donepezil was associated with significantly more adverse effects compared with placebo, mostly gastrointestinal. From the second study, there is no evidence that donepezil delays the onset of AD. There is no evidence to support the use of donepezil for patients with MCI. The putative benefits are minor, short lived and associated with significant side effects.

---

### PMID 19528519 — current stance: `supports`

**Evidence span:** > Kaplan-Meier analysis showed that among the depressed subjects, the proportion progressing to AD was lower for the donepezil group than the combined vitamin E and placebo groups at 1.7 years (p = 0.023), at 2.2 years (p = 0.025), and remained marginally lower at 2.7 years (p = 0.070).

**Golden note:** Donepezil delays progression to AD in MCI subjects with depression — subgroup positive.

**Donepezil delays progression to AD in MCI subjects with depressive symptoms.**

*Neurology*, 2009. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> OBJECTIVE: To determine whether the presence of depression predicts higher rate of progression to Alzheimer disease (AD) in patients with amnestic mild cognitive impairment (aMCI) and whether donepezil treatment beneficially affect this relationship. METHODS: The study sample was composed of 756 participants with aMCI from the 3-year, double-blind, placebo-controlled Alzheimer's Disease Cooperative Study drug trial of donepezil and vitamin E. Beck Depression Inventory (BDI) was used to assess depressive symptoms at baseline and participants were followed either to the end of study or to the primary endpoint of progression to probable or possible AD. RESULTS: Cox proportional hazards regression, adjusted for age at baseline, gender, apolipoprotein genotype, and NYU paragraph delayed recall score, showed that higher BDI scores were associated with progression to AD (p = 0.03). The sample was stratified into depressed (BDI score > or =10; n = 208) and nondepressed (BDI <10; n = 548) groups. Kaplan-Meier analysis showed that among the depressed subjects, the proportion progressing to AD was lower for the donepezil group than the combined vitamin E and placebo groups at 1.7 years (p = 0.023), at 2.2 years (p = 0.025), and remained marginally lower at 2.7 years (p = 0.070). The survival curves among the three treatment groups did not differ within the nondepressed participants. CONCLUSIONS: Results suggest that depression is predictive of progression from amnestic mild cognitive impairment (aMCI) to Alzheimer disease (AD) and treatment with donepezil delayed progression to AD among depressed subjects with aMCI. Donepezil appears to modulate the increased risk of AD conferred by the presence of depressive symptoms.

---

### PMID 30565793 — current stance: `contradicts`

**Evidence span:** > After 6 months, the donepezil group experienced an improvement in dual-task gait speed (range 4-11 cm/s), although this was not statistically significant.

**Golden note:** Donepezil for gait/falls in MCI RCT — no functional benefit.

**Donepezil for gait and falls in mild cognitive impairment: a randomized controlled trial.**

*European journal of neurology*, 2018. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND AND PURPOSE: Cognitive enhancers are commonly prescribed to people with Alzheimer's disease and related dementias to improve cognition and function. However, their effectiveness for individuals in the pre-stages of dementia, particularly in functional motor outcomes, remains unknown. We aimed to determine the efficacy of donepezil, a cognitive enhancer that improves cholinergic neurotransmission, on gait performance in mild cognitive impairment (MCI). METHODS: This was a double-blind, placebo-controlled trial including 60 older adults with MCI, randomized to receive donepezil (10 mg/daily, maximal dose) or placebo. Primary outcome was gait speed (cm/s) under single and three dual-task conditions (counting backwards by 1 or 7 and naming animals) measured using an electronic walkway. Dual-task gait cost (DTC), a valid measure of motor-cognitive interaction, was calculated as the percentage change between single (S) and dual-task (D) gait speeds: [(S - D)/S] × 100. Secondary outcomes included attention, executive function, balance and falls. RESULTS: After 6 months, the donepezil group experienced an improvement in dual-task gait speed (range 4-11 cm/s), although this was not statistically significant. The donepezil group showed a significant reduction in DTC (improvement) by counting backwards by 1 and 7 compared with placebo (10.25% vs. 1.75%, P = 0.048; 21.38% vs. 14.64%, P = 0.037, intention-to-treat analysis). Per-protocol analyses showed that all three DTCs improved in the donepezil group, along with a non-significant reduction of rate of falls. CONCLUSIONS: Donepezil treatment improved dual-task gait speed and DTC in elderly patients with MCI. Our results support the concept of reducing falls in MCI by targeting the motor-cognitive interface.

---

### PMID 19001543 — current stance: `inconclusive`

**Evidence span:** > Despite the limitations inherent to a pilot study of a small sample, our results point to specific cortical substrates underlying the actions of donepezil, which can be tested in future studies.

**Golden note:** fMRI pilot — donepezil affects cortical activation in MCI; no clinical primary.

**Effects of donepezil on cortical activation in mild cognitive impairment: a pilot double-blind placebo-controlled trial using functional MR imaging.**

*AJNR. American journal of neuroradiology*, 2008. Types: Controlled Clinical Trial; Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't

> BACKGROUND AND PURPOSE: Cholinesterase-inhibitor therapy is approved for treatment of Alzheimer disease; however, application in patients with mild cognitive impairment (MCI) is still under active investigation. The purpose of this study was to determine the effect of such therapy on the neural substrates underlying memory processing in subjects with MCI by using functional MR imaging (fMRI). MATERIALS AND METHODS: Thirteen subjects with MCI (mean age, 68 +/- 6.9 years) enrolled in a multicenter double-blind placebo-controlled trial testing the clinical efficacy of the cholinesterase-inhibitor, donepezil, were studied with fMRI at baseline and following 12 or 24 weeks of therapy (single-site pilot study). The cognitive paradigm was delayed-response visual memory for novel faces. Within-group 1-sample t tests were performed on the donepezil and placebo groups at baseline and at follow-up. A repeated-measures analysis of variance design was used to look for a Treatment Group x Time interaction showing a significant donepezil- but not placebo-related change in blood oxygen level-dependent response during the course of the study. RESULTS: At baseline, both groups showed multiple areas of activation, including the bilateral dorsolateral prefrontal cortex, fusiform gyrus, and anterior cingulate cortex. On follow-up, the placebo group demonstrated a decreased extent of dorsolateral prefrontal activation, whereas the donepezil group demonstrated an increased extent of activation in the ventrolateral prefrontal cortex. Interaction demonstrated significant donepezil- but not placebo-related change in the left inferior frontal gyrus. CONCLUSIONS: Despite the limitations inherent to a pilot study of a small sample, our results point to specific cortical substrates underlying the actions of donepezil, which can be tested in future studies.

---

### PMID 27567841 — current stance: `inconclusive`

**Evidence span:** > Among the carriers of APOE-ɛ4 and BCHE-K*, the benefit of donepezil was evident at the end of the three-year follow-up.

**Golden note:** BCHE/APOE genotype modulates donepezil response in MCI — pharmacogenetic, mixed.

**Butyrylcholinesterase K and Apolipoprotein E-ɛ4 Reduce the Age of Onset of Alzheimer's Disease, Accelerate Cognitive Decline, and Modulate Donepezil Response in Mild Cognitively Impaired Subjects.**

*Journal of Alzheimer's disease : JAD*, 2016. Types: Journal Article; Randomized Controlled Trial

> BACKGROUND: Genetic heterogeneity in amnestic mild cognitively impaired (aMCI) subjects could lead to variations in progression rates and response to cholinomimetic agents. Together with the apolipoprotein E4 (APOE-ɛ4) gene, butyrylcholinesterase (BCHE) has become recently one of the few Alzheimer's disease (AD) susceptibility genes with distinct pharmacogenomic properties. OBJECTIVE: To validate candidate genes (APOE/BCHE) which display associations with age of onset of AD and donepezil efficacy in aMCI subjects. METHODS: Using the Petersen et al. (2005) study on vitamin E and donepezil efficacy in aMCI, we contrasted the effects of BCHE and APOE variants on donepezil drug response using the Alzheimer's Disease Assessment Score-Cognition (ADAS-Cog) scale. Independently, we assessed the effects of APOE/BCHE genotypes on age of onset and cortical choline acetyltransferase activity in autopsy-confirmed AD and age-matched control subjects. RESULTS: Statistical analyses revealed a significant earlier age of onset in AD for APOE-ɛ4, BCHE-K*, and APOE-ɛ4/BCHE-K* carriers. Among the carriers of APOE-ɛ4 and BCHE-K*, the benefit of donepezil was evident at the end of the three-year follow-up. The responder's pharmacogenomic profile is consistent with reduced brain cholinergic activity measured in APOE-ɛ4 and BCHE-K* positive subjects. CONCLUSIONS: APOE-ɛ4 and BCHE-K* positive subjects display an earlier age of onset of AD, an accelerated cognitive decline and a greater cognitive benefits to donepezil therapy. These results clearly emphasize the necessity of monitoring potential pharmacogenomic effects in this population of subjects, and suggest enrichment strategies for secondary prevention trials involving prodromal AD subjects.

---

### PMID 26876309 — current stance: `inconclusive`

**Evidence span:** > Only Hp, but not BF volume was a useful predictor of cognitive decline in suspected prodromal AD patients. Both Hp and BF volumes were poor predictors of treatment response, questioning previous approaches on predicting treatment response without placebo control.

**Golden note:** Hippocampal/BF volume predictors of donepezil response in prodromal AD.

**Predictors of cognitive decline and treatment response in a clinical trial on suspected prodromal Alzheimer's disease.**

*Neuropharmacology*, 2016. Types: Clinical Trial; Journal Article

> UNLABELLED: We determined the value of hippocampus (Hp) and basal forebrain (BF) volumes for predicting cognitive decline and treatment response in a double-blind, randomized, placebo-controlled phase 4 trial at 28 academic centers (France) in patients with amnestic mild cognitive impairment (MCI) receiving Donepezil 10 mg daily or placebo over 12 months, and 6 months open label follow-up. Outcome measures were the rates of global and domain specific cognitive decline as non-primary efficacy endpoint. The intention-to-treat (ITT) sample analyzed comprised 215 cases. Baseline Hp volume was a significant predictor of rates of change in global cognitive function in linear mixed effects models. This effect was independent of treatment. BF volume was not associated with rates of global or domain specific cognitive decline. Rates of delayed free recall decline were higher in MCI cases treated with donepezil compared to placebo. Only Hp, but not BF volume was a useful predictor of cognitive decline in suspected prodromal AD patients. Both Hp and BF volumes were poor predictors of treatment response, questioning previous approaches on predicting treatment response without placebo control. TRIAL REGISTRATION: clinicalTrials.gov Identifier NCT00403520.

---

### PMID 37353809 — current stance: `inconclusive`

**Evidence span:** > Donepezil-treated MCI individuals showed slower atrophy rates compared to the placebo group, but only if they belonged to the minimal atrophy or hippocampal-sparing subtypes.

**Golden note:** Differential donepezil response by MRI subtypes in MCI — heterogeneity finding.

**Differential response to donepezil in MRI subtypes of mild cognitive impairment.**

*Alzheimer's research & therapy*, 2023. Types: Randomized Controlled Trial; Journal Article

> BACKGROUND: Donepezil is an approved therapy for the treatment of Alzheimer's disease (AD). Results across clinical trials have been inconsistent, which may be explained by design-methodological issues, the pathophysiological heterogeneity of AD, and diversity of included study participants. We investigated whether response to donepezil differs in mild cognitive impaired (MCI) individuals demonstrating different magnetic resonance imaging (MRI) subtypes. METHODS: From the Hippocampus Study double-blind, randomized clinical trial, we included 173 MCI individuals (donepezil = 83; placebo = 90) with structural MRI data, at baseline and at clinical follow-up assessments (6-12-month). Efficacy outcomes were the annualized percentage change (APC) in hippocampal, ventricular, and total grey matter volumes, as well as in the AD cortical thickness signature. Participants were classified into MRI subtypes as typical AD, limbic-predominant, hippocampal-sparing, or minimal atrophy at baseline. We primarily applied a subtyping approach based on continuous scale of two subtyping dimensions. We also used the conventional categorical subtyping approach for comparison. RESULTS: Donepezil-treated MCI individuals showed slower atrophy rates compared to the placebo group, but only if they belonged to the minimal atrophy or hippocampal-sparing subtypes. Importantly, only the continuous subtyping approach, but not the conventional categorical approach, captured this differential response. CONCLUSIONS: Our data suggest that individuals with MCI, with hippocampal-sparing or minimal atrophy subtype, may have improved benefit from donepezil, as compared with MCI individuals with typical or limbic-predominant patterns of atrophy. The newly proposed continuous subtyping approach may have advantages compared to the conventional categorical approach. Future research is warranted to demonstrate the potential of subtype stratification for disease prognosis and response to treatment. TRIAL REGISTRATION: ClinicalTrial.gov NCT00403520. Submission Date: November 21, 2006.

---

### PMID 17330176 — current stance: `inconclusive`

**Evidence span:** > The use of ChEI resulted in approximately 24% reduction of risk of conversion from MCI to dementia at the cost of more than 50% increase of adverse events and more than 130% increase of adverse events leading to drug discontinuation, as compared to placebo.

**Golden note:** Meta-analysis ChEIs in MCI — modest, uncertain.

**Cholinesterase inhibitors in mild cognitive impairment: a meta-analysis of randomized controlled trials.**

*Neurologia i neurochirurgia polska*, 2007. Types: Journal Article; Meta-Analysis

> BACKGROUND AND PURPOSE: Despite being commonly regarded as an initial stage of dementia (particularly of Alzheimer's type, AD), mild cognitive impairment (MCI) is usually not treated and no recommendations for management have been established. Cholinesterase inhibitors have been proposed to halt the progression of MCI to AD and several randomized controlled studies (RCT) have been undertaken to prove this hypothesis. Here we have analyzed the results of RCT of ChEI in MCI. MATERIAL AND METHODS: Four long-term RCT of ChEI in MCI were identified. A meta-analysis was conducted with the Mantel-Haenszel method using a fixed model. We compared a major parameter of efficacy (the proportion of those who progressed to dementia within two years) and two parameters of safety, i.e. the total number of adverse events and the number of adverse events leading to drug discontinuation. RESULTS: The use of ChEI resulted in approximately 24% reduction of risk of conversion from MCI to dementia at the cost of more than 50% increase of adverse events and more than 130% increase of adverse events leading to drug discontinuation, as compared to placebo. Moreover, in the case of galantamine a considerable increase in deaths was observed in the active treatment group; whether this outcome is a class effect of all ChEI or is limited to galantamine cannot be established due to the lack of data from donepezil and rivastigmine trials. CONCLUSIONS: Because of the questionable efficacy : risk ratio, we believe that it is too early to recommend ChEI in MCI. The sine qua non condition is to establish the factors that predict the risk of conversion from MCI to AD.

---

### PMID 26091818 — current stance: `inconclusive`

**Evidence span:** > Pooled anti-dementia drugs showed superior protective outcomes compared with placebo regarding %TBV/y (SMD=-0.21, 95%CI=-0.37 to -0.04, P=.01, N=4, n=624) and %VV/y (SMD=-0.79, 95%CI=-1.40 to -0.19, P=.01, N=3, n=851). However, %HV/y failed to show difference between both groups.

**Golden note:** Anti-dementia meds vs brain atrophy meta in MCI/AD — atrophy outcome only.

**Protection against Brain Atrophy by Anti-dementia Medication in Mild Cognitive Impairment and Alzheimer's Disease: Meta-Analysis of Longitudinal Randomized Placebo-Controlled Trials.**

*The international journal of neuropsychopharmacology*, 2015. Types: Journal Article; Meta-Analysis

> BACKGROUND: There has not been conclusive evidence for prevention of brain atrophy by anti-dementia drugs in mild cognitive impairment and Alzheimer's Disease. METHODS: Relevant studies were identified through searches of PubMed, databases of the Cochrane Library, and PsycINFO citations up to 16 May, 2015. Only double-blind, randomized, placebo-controlled clinical trials of anti-dementia drugs in patients with mild cognitive impairment or Alzheimer's Disease were included. Primary outcomes were annualized percent change of total brain volume (%TBV/y), annualized percent change of hippocampal volume (%HV/y), and annualized percent change of ventricular volume (%VV/y) measured by magnetic resonance imaging. Standardized mean difference (SMD) and 95% confidence intervals (CI) were calculated for relevant outcomes. RESULTS: Seven randomized, placebo-controlled clinical trials (n=1708) were found to meet the inclusion criteria, including 4 mild cognitive impairment studies (n=1327) and 3 Alzheimer's Disease studies (n=381) [3 donepezil studies (2 mild cognitive impairment studies and 1 Alzheimer's Disease study), 1 galantaime study for mild cognitive impairment, 2 mementine studies for Alzheimer's Disease, and 1 rivastigmine study for mild cognitive impairment]. Pooled anti-dementia drugs showed superior protective outcomes compared with placebo regarding %TBV/y (SMD=-0.21, 95%CI=-0.37 to -0.04, P=.01, N=4, n=624) and %VV/y (SMD=-0.79, 95%CI=-1.40 to -0.19, P=.01, N=3, n=851). However, %HV/y failed to show difference between both groups. Among anti-dementia drugs, donepezil showed significantly greater protective effects than placebo regarding %TBV/y (SMD=-0.43, 95%CI=-0.74 to -0.12, P=.007, N=1, n=164) and %VV/y (SMD=-0.51, 95%CI=-0.73 to -0.29, P<.00001, N=2, n=338). Rivastigmine was also superior to placebo regarding %VV/y (SMD=-1.33, 95%CI=-1.52 to -1.14, P<.00001). CONCLUSIONS: The results favored the hypothesis that anti-dementia drugs may prevent brain atrophy in patients with mild cognitive impairment and Alzheimer's Disease.

---

### PMID 19949165 — current stance: `inconclusive`

**Evidence span:** > These findings support the safety of donepezil in patients with aMCI. When compared with other studies, however, the data suggest that patients with Alzheimer's tolerate donepezil better than patients with MCI.

**Golden note:** Open-label extension safety — no efficacy claim.

**Safety and tolerability of donepezil in mild cognitive impairment: open-label extension study.**

*American journal of Alzheimer's disease and other dementias*, 2009. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Following a 48-week, double-blind, randomized, placebo-controlled trial of donepezil in 821 patients with amnestic mild cognitive impairment (aMCI), safety and tolerability of donepezil (10 mg) were further evaluated in a 28-week extension study. Of 499 participants who completed the double-blind phase, 145 enrolled in the open-label study. Adverse events (AEs) were recorded throughout. Overall, 57.4% of participants in the donepezil/donepezil group and 62.3% in the placebo/donepezil group experienced an AE, with the most frequent treatment-emergent AEs being diarrhea, muscle spasms, insomnia, and nausea. Most were mild to moderate in severity and were more common in the first several weeks after treatment initiation. More participants in the placebo/donepezil group (22.1%) discontinued donepezil due to an AE compared with the donepezil/donepezil group (10.3%). These findings support the safety of donepezil in patients with aMCI. When compared with other studies, however, the data suggest that patients with Alzheimer's tolerate donepezil better than patients with MCI.

---

### PMID 39939901 — current stance: `inconclusive`

**Evidence span:** > Higher doses of donepezil (10 mg) significantly reduce hippocampal atrophy in Alzheimer's disease and mild cognitive impairment, suggesting potential neuroprotective effects.

**Golden note:** AChEI hippocampal atrophy meta — atrophy outcome, mixed populations.

**Efficacy of acetylcholinesterase inhibitors on reducing hippocampal atrophy rate: a systematic review and meta-analysis.**

*BMC neurology*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Neurodegenerative diseases (NDs) are conditions characterized by irreversible progressive degeneration to the nervous tissue and are usually associated with cognitive decline and functional deficits, especially in elderly. Acetylcholinesterase inhibitors (AChEIs) like donepezil, rivastigmine, and galantamine are commonly prescribed to alleviate cognitive symptoms associated with NDs. However, their long-term impact on slowing structural brain degeneration, particularly hippocampal atrophy, remains unclear. OBJECTIVE: This systematic review and meta-analysis assess the efficacy of AChEIs in reducing hippocampal atrophy in patients with NDs or clinical syndromes that lead to cognitive decline. METHODS: A systematic search of PubMed, Scopus, Web of Science, and Cochrane databases, since inception till 20th August 2024, identified randomized controlled trials (RCTs) and comparative studies that measured hippocampal volume changes in elderly patients with NDs and other clinical syndromes. Random effect model was employed to estimate the pooled atrophy rates. Subgroup analysis was conducted by disease, dosage, and side of the measurement. RESULTS: From 5,943 initially screened studies, nine were included in the review, and six were analyzed in the meta-analysis, encompassing a total of 2,179 participants. The meta-analysis showed that donepezil at a 10 mg dose significantly reduced hippocampal atrophy compared to placebo (SMD = 0.44, 95% CI [0.08 to 0.81], p = 0.01), whereas the 5 mg dose showed no significant effect on hippocampal volume. Overall, pooled results favored donepezil in reducing hippocampal atrophy (SMD = 0.33, p = 0.04), indicating that higher doses are more effective. Among patients with mild cognitive impairment (MCI), both donepezil and vitamin E were associated with a significant reduction in hippocampal atrophy compared to placebo (SMD = 0.27, p = 0.01). In contrast, galantamine did not significantly reduce hippocampal atrophy in the overall analysis, but it was associated with reduced whole brain atrophy in APOE ε4 carriers. Further analysis revealed no significant difference in the reduction of right or left hippocampal atrophy in donepezil-treated patients. These findings suggest that donepezil, particularly at higher doses, may have a protective effect against hippocampal atrophy in patients with AD and MCI, while galantamine's effect may be more limited, especially in certain genetic subgroups. CONCLUSION: Higher doses of donepezil (10 mg) significantly reduce hippocampal atrophy in Alzheimer's disease and mild cognitive impairment, suggesting potential neuroprotective effects. In contrast, lower doses (5 mg) and galantamine showed no significant impact on hippocampal volume, though galantamine reduced whole brain atrophy in APOE ε4 carriers. Dosage and genetic factors are crucial in determining the efficacy of acetylcholinesterase inhibitors in slowing neurodegeneration.

---

### PMID 15829527 — current stance: `inconclusive`

**Evidence span:** > Although donepezil therapy was associated with a lower rate of progression to Alzheimer's disease during the first 12 months of treatment, the rate of progression to Alzheimer's disease after three years was not lower among patients treated with donepezil than among those given placebo.

**Golden note:** Petersen 2005 NEJM vit-E + donepezil for MCI — donepezil reduced progression to AD at 12mo but not 36mo. Classic mixed.

**Vitamin E and donepezil for the treatment of mild cognitive impairment.**

*The New England journal of medicine*, 2005. Types: Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't; Research Support, U.S. Gov't, P.H.S.

> BACKGROUND: Mild cognitive impairment is a transitional state between the cognitive changes of normal aging and early Alzheimer's disease. METHODS: In a double-blind study, we evaluated subjects with the amnestic subtype of mild cognitive impairment. Subjects were randomly assigned to receive 2000 IU of vitamin E daily, 10 mg of donepezil daily, or placebo for three years. The primary outcome was clinically possible or probable Alzheimer's disease; secondary outcomes were cognition and function. RESULTS: A total of 769 subjects were enrolled, and possible or probable Alzheimer's disease developed in 212. The overall rate of progression from mild cognitive impairment to Alzheimer's disease was 16 percent per year. As compared with the placebo group, there were no significant differences in the probability of progression to Alzheimer's disease in the vitamin E group (hazard ratio, 1.02; 95 percent confidence interval, 0.74 to 1.41; P=0.91) or the donepezil group (hazard ratio, 0.80; 95 percent confidence interval, 0.57 to 1.13; P=0.42) during the three years of treatment. Prespecified analyses of the treatment effects at 6-month intervals showed that as compared with the placebo group, the donepezil group had a reduced likelihood of progression to Alzheimer's disease during the first 12 months of the study (P=0.04), a finding supported by the secondary outcome measures. Among carriers of one or more apolipoprotein E epsilon4 alleles, the benefit of donepezil was evident throughout the three-year follow-up. There were no significant differences in the rate of progression to Alzheimer's disease between the vitamin E and placebo groups at any point, either among all patients or among apolipoprotein E epsilon4 carriers. CONCLUSIONS: Vitamin E had no benefit in patients with mild cognitive impairment. Although donepezil therapy was associated with a lower rate of progression to Alzheimer's disease during the first 12 months of treatment, the rate of progression to Alzheimer's disease after three years was not lower among patients treated with donepezil than among those given placebo.

---

