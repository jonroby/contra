# Q13: Do statins prevent incident dementia in older adults?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=10 PMIDs.

**Current S/C/I**: 1 / 1 / 8
**Proposed S/C/I**: 2 / 3 / 5
**Net flips**: 4

`expected_consensus: "inconclusive"` is appropriate, but the current
labels under-weight both the negative RCT evidence (Cochrane reviews,
ASPREE) and the recent positive observational meta. Applying the strict
bar makes the inherent contradiction visible: **RCTs say no effect,
large observational metas say protective**.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `26727124` | 2016 | **inconclusive → contradicts** | Cochrane 2016 update; 2 RCTs, n=26,340 (HPS, PROSPER), follow-up 3.2-5 yr. Verbatim: *"There is **good evidence** that statins given in late life to people at risk of vascular disease **do not prevent cognitive decline or dementia**."* Adequately-powered RCT pooled OR 1.00 (CI 0.61-1.65), high-quality evidence per Cochrane. The canonical RCT-evidence-says-no-effect finding for this question. |
| `19370582` | 2009 | **inconclusive → contradicts** | Cochrane 2009; same 2 RCTs (HPS, PROSPER). Verbatim: *"There is **good evidence** from RCTs that statins given in late life to individuals at risk of vascular disease have **no effect** in preventing AD or dementia."* Predecessor of `26727124` with same conclusion. Both Cochrane reviews say "no effect" — should be `contradicts`. |
| `15699299` | 2005 | **supports → contradicts** | Cache County prospective. The study has a baseline cross-sectional component (statin use associated with lower prevalence, OR 0.44 sig) AND a prospective incidence component (HR 1.19 NS for dementia, HR 1.19 NS for AD). Verbatim: *"Statin use at baseline **did not predict incidence** of dementia or AD."* The current `supports` label is anchoring on the cross-sectional baseline finding; the prospective primary outcome is null. The conclusion: *"we found **no association** between statin use and subsequent onset of dementia or AD."* |
| `39963242` | 2025 | **inconclusive → supports** | 2025 cohort meta of 35 cohort studies, n=6.3M patients. Verbatim: *"statin use was associated with a reduced risk of dementia (HR: 0.79, 95% CI: 0.71-0.88)"* and *"a 29% decrease in the risk of AD among statin users (HR: 0.71, 95% CI: 0.60-0.85)."* Significantly positive pooled observational effect. The conclusion ("statin use is associated with a reduced incidence of dementia and AD, which might be modified by ages") is positive, not inconclusive. |

## Confirmed (no change)

- `34167639` (ASPREE n=18,846 ≥65, 4.7-yr follow-up) — **contradicts ✓** (*"statin use was not associated with dementia, MCI, or declines"* — well-powered prospective null)
- `24247674` (statins/cognition SR — narrative, mixed direction) — **inconclusive ✓**
- `23225700` (observational meta — pooled sig but explicitly addresses confounding) — **inconclusive ✓** (defensible because conclusion explicitly cautions: *"this benefit observed in both disease states should be interpreted with caution as observational studies are subject to bias"*)
- `20859546` (2010 SR — sparse RCT data) — **inconclusive ✓**
- `29914039` (2018 SR/meta — observational sig but single RCT null) — **inconclusive ✓**
- `27473843` (TOP-COG Down syndrome pilot, n=21) — **inconclusive ✓** (pilot exempt)

## Cross-cutting issues

- **The classic RCT-vs-observational divergence**: this question's data
  has the canonical pattern of well-powered RCTs (HPS, PROSPER, ASPREE)
  showing null, while observational meta-analyses (`23225700`,
  `39963242`, `29914039`) show pooled protective associations. The
  Cochrane reviews explicitly attribute the divergence to **indication
  bias** in observational studies. Under the strict bar:
  - RCTs → `contradicts` (well-powered RCT primary endpoint missed)
  - Observational meta → `supports` (pooled sig effect)
  - Mixed/narrative SRs → `inconclusive`
- **`expected_consensus: "inconclusive"`** is correct as a *summary*
  but the underlying evidence is bimodal, not uniformly null.
- After flips: 2/3/5 — the question now correctly shows both the
  negative-RCT and positive-observational signals.

## Highest-confidence flips for this question

- `26727124` and `19370582` inconclusive → contradicts — both Cochrane reviews
  explicitly state "good evidence... no effect" for the RCT pooled estimate.
- `15699299` supports → contradicts — the prospective primary finding
  was null; the current label captures only the cross-sectional baseline.
- `39963242` inconclusive → supports — pooled HR 0.79 sig in 6.3M
  patients is not "inconclusive" in the technical sense; it's a
  significantly positive pooled effect with an observational caveat.


---

## Abstracts (n=10)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 26727124 — current stance: `inconclusive`

**Golden note:** Cochrane review 2016 — insufficient evidence statins prevent dementia.

**Statins for the prevention of dementia.**

*The Cochrane database of systematic reviews*, 2016. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: This is an update of a Cochrane review first published in 2001 and then updated in 2009. Vascular risk factors including high cholesterol levels increase the risk of dementia due to Alzheimer's disease and of vascular dementia. Some observational studies have suggested an association between statin use and lowered incidence of dementia. OBJECTIVES: To evaluate the efficacy and safety of statins for the prevention of dementia in people at risk of dementia due to their age and to determine whether the efficacy and safety of statins for this purpose depends on cholesterol level, apolipoprotein E (ApoE) genotype or cognitive level. SEARCH METHODS: We searched ALOIS (the Specialized Register of the Cochrane Dementia and Cognitive Improvement Group), The Cochrane Library, MEDLINE, EMBASE, PsycINFO, CINAHL, LILACS, ClinicalTrials.gov and the World Health Organization (WHO) Portal on 11 November 2015. SELECTION CRITERIA: We included double-blind, randomised, placebo-controlled trials in which statins were administered for at least 12 months to people at risk of dementia. DATA COLLECTION AND ANALYSIS: We used standard methodological procedures expected by Cochrane. MAIN RESULTS: We included two trials with 26,340 participants aged 40 to 82 years of whom 11,610 were aged 70 or older. All participants had a history of, or risk factors for, vascular disease. The studies used different statins (simvastatin and pravastatin). Mean follow-up was 3.2 years in one study and five years in one study. The risk of bias was low. Only one study reported on the incidence of dementia (20,536 participants, 31 cases in each group; odds ratio (OR) 1.00, 95% confidence interval (CI) 0.61 to 1.65, moderate quality evidence, downgraded due to imprecision). Both studies assessed cognitive function, but at different times using different scales, so we judged the results unsuitable for a meta-analysis. There were no differences between statin and placebo groups on five different cognitive tests (high quality evidence). Rates of treatment discontinuation due to non-fatal adverse events were less than 5% in both studies and there was no difference between statin and placebo groups in the risk of withdrawal due to adverse events (26,340 participants, 2 studies, OR 0.94, 95% CI 0.83 to 1.05). AUTHORS' CONCLUSIONS: There is good evidence that statins given in late life to people at risk of vascular disease do not prevent cognitive decline or dementia. Biologically, it seems feasible that statins could prevent dementia due to their role in cholesterol reduction and initial evidence from observational studies was very promising. However, indication bias may have been a factor in these studies and the evidence from subsequent RCTs has been negative. There were limitations in the included studies involving the cognitive assessments used and the inclusion of participants at moderate to high vascular risk only.

---

### PMID 15699299 — current stance: `supports`

**Golden note:** Cache County prospective — statin use associated with reduced incident AD/dementia.

**Do statins reduce risk of incident dementia and Alzheimer disease? The Cache County Study.**

*Archives of general psychiatry*, 2005. Types: Comparative Study; Journal Article; Research Support, U.S. Gov't, P.H.S.

> BACKGROUND: Prior reports suggest reduced occurrence of dementia and Alzheimer disease (AD) in statin users, but, to our knowledge, no prospective studies relate statin use and dementia incidence. OBJECTIVE: To examine the association of statin use with both prevalence and incidence of dementia and AD. DESIGN: Cross-sectional studies of prevalence and incidence and a prospective study of incidence of dementia and AD among 5092 elderly residents (aged 65 years or older) of a single county. Participants were assessed at home in 1995-1997 and again in 1998-2000. A detailed visual inventory of medicines, including statins and other lipid-lowering agents, was collected at both assessments. MAIN OUTCOME MEASURES: Diagnosis of dementia and of AD. RESULTS: From 4895 participants with data sufficient to determine cognitive status, we identified 355 cases of prevalent dementia (200 with AD) at initial assessment. Statin use was inversely associated with prevalence of dementia (adjusted odds ratio, 0.44; 95% confidence interval, 0.17-0.94). Three years later, we identified 185 cases of incident dementia (104 with AD) among 3308 survivors at risk. Statin use at baseline did not predict incidence of dementia or AD (adjusted hazard ratio for dementia, 1.19; 95% confidence interval, 0.53-2.34; adjusted hazard ratio for AD, 1.19; 95% confidence interval, 0.35-2.96), nor did statin use at follow-up (adjusted odds ratio for dementia, 1.04; 95% confidence interval, 0.56-1.81; adjusted odds ratio for AD, 0.85; 95% confidence interval, 0.32-1.88). CONCLUSIONS: Although statin use might be less frequent in those with prevalent dementia, we found no association between statin use and subsequent onset of dementia or AD. Further research is warranted before costly dementia prevention trials with statins are undertaken.

---

### PMID 24247674 — current stance: `inconclusive`

**Golden note:** Statins/cognition systematic review — relationship remains unknown.

**Statins and cognitive function: a systematic review.**

*Annals of internal medicine*, 2013. Types: Journal Article; Systematic Review

> BACKGROUND: Despite the U.S. Food and Drug Administration (FDA) warning regarding cognitive impairment, the relationship between statins and cognition remains unknown. PURPOSE: To examine the effect of statins on cognition. DATA SOURCES: PubMed, Embase, and Cochrane Library from inception through October 2012; FDA databases from January 1986 through March 2012. STUDY SELECTION: Randomized, controlled trials (RCTs) and cohort, case-control, and cross-sectional studies evaluating cognition in patients receiving statins. DATA EXTRACTION: Two reviewers extracted data, 1 reviewer assessed study risk of bias, and 1 reviewer checked all assessments. DATA SYNTHESIS: Among statin users, low-quality evidence suggested no increased incidence of Alzheimer disease and no difference in cognitive performance related to procedural memory, attention, or motor speed. Moderate-quality evidence suggested no increased incidence of dementia or mild cognitive impairment or any change in cognitive performance related to global cognitive performance scores, executive function, declarative memory, processing speed, or visuoperception. Examination of the FDA postmarketing surveillance databases revealed a low reporting rate for cognitive-related adverse events with statins that was similar to the rates seen with other commonly prescribed cardiovascular medications. LIMITATIONS: The absence of many well-powered RCTs for most outcomes resulted in final strengths of evidence that were low or moderate. Imprecision, inconsistency, and risk of bias also limited the strength of findings. CONCLUSION: Larger and better-designed studies are needed to draw unequivocal conclusions about the effect of statins on cognition. Published data do not suggest an adverse effect of statins on cognition; however, the strength of available evidence is limited, particularly with regard to high-dose statins.

---

### PMID 19370582 — current stance: `inconclusive`

**Golden note:** Cochrane 2009 — insufficient evidence for prevention.

**Statins for the prevention of dementia.**

*The Cochrane database of systematic reviews*, 2009. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: This is an update of a Cochrane review first published in 2001. At that stage there was insufficient evidence to recommend statins for the prevention of Alzheimer's disease (AD). The scope of this review has been expanded to include all forms of dementia. OBJECTIVES: To assess the effects of statins in the prevention of dementia. SEARCH STRATEGY: The Specialized Register of the Cochrane Dementia and Cognitive Improvement Group, The Cochrane Library, MEDLINE, EMBASE, PsycINFO, CINAHL and LILACS were searched on 10 October 2007 using the terms statin*, lovastatin*, pravastatin*, simvastatin*, fluvastatin*, atorvastatin* and rosuvastatin*. The CDCIG Register contains records from many healthcare databases, SIGLE, LILACS as well as many trials databases and is updated regularly. SELECTION CRITERIA: Double-blind randomized placebo-controlled trials of statins in people at risk of AD and dementia. DATA COLLECTION AND ANALYSIS: Two independent reviewers extracted and assessed data independently and agreement was reached after discussion. Adverse effects were noted. MAIN RESULTS: Two trials were identified with 26,340 participants; HPS 2002 and PROSPER 2002. Age range was 40-82 years across the two studies, PROSPER 2002 included 5804 patients aged 70-82 years and HPS included 20,536 patients with 5806 at least 70 years old at study entry. Mean total cholesterol 5.9 mmol/l, LDL cholesterol 3.4 mmol/l at study entry with mean reduction in LDL cholesterol of 1.0 mmol/l in simvastatin treated patients compared to placebo in HPS 2002. Mean total cholesterol 5.7 mmol/l, LDL cholesterol 3.8 mmol/l at study entry with mean reduction in LDL cholesterol of 1.02 mmol/l in pravastatin treated patients compared to placebo in PROSPER 2002. Mean follow-up 3.2 years in PROSPER, 5 years in HPS 2002. Cognition was measured at different times and with different scales so could not be combined in a meta-analysis. There was no difference in incidence of dementia in HPS 2002 (31 cases in simvastatin group, 31 cases in placebo group) nor in performance on the modified Telephone Interview for Cognitive Status at final follow-up (23.7% simvastatin group cognitively impaired vs 24.2% in placebo group). There was no difference in cognition between groups either in relation to age at study entry or previous history of cerebrovascular disease. Cognitive function declined at the same rate in both treatment groups in PROSPER 2002, there was no significant difference between pravastatin treated and placebo groups in performance on letter digit codes, picture word learning test, Stroop and Mini Mental State Examination. There was no evidence that statins were detrimental to cognition. AUTHORS' CONCLUSIONS: There is good evidence from RCTs that statins given in late life to individuals at risk of vascular disease have no effect in preventing AD or dementia. Biologically it seems feasible that statins could prevent dementia due to their role in cholesterol reduction and initial evidence from observational studies was very promising. Indication bias may have been a factor in these studies however and the evidence from subsequent RCTs has been negative.

---

### PMID 23225700 — current stance: `inconclusive`

**Golden note:** Observational meta — benefit inconclusive with confounding concerns.

**Statins in the prevention of dementia and Alzheimer's disease: a meta-analysis of observational studies and an assessment of confounding.**

*Pharmacoepidemiology and drug safety*, 2012. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: Studies demonstrate the potential for statins to prevent dementia and Alzheimer's disease (AD), but the evidence is inconclusive. OBJECTIVE: Conduct a meta-analysis to estimate any benefit of statins in preventing dementia and examine the potential effect of study design and confounding on the benefit of statins in dementia. A secondary goal is to explore factors that may elucidate the mechanisms by which statins exert their potentially beneficial effect. METHODS: Performed systematic literature review to identify relevant publications. Relative risk (RR) estimates were pooled using both fixed and random effect models. Studies were stratified by study design and potential confounding factors. RESULTS: The pooled results for all-type dementia suggest that use of statins is associated with a lower RR of dementia when compared to non-statin users (random effects model: RR 0.82 (95%CI [0.69, 0.97]). The pooled results for AD also suggested a lower RR with statin user compared to non-statin users in random effects models (RR: 0.70, 95% CI [0.60, 0.83]). Study design and methods used to address biases may influence the results. CONCLUSION: These pooled results suggest that statins may provide a slight benefit in the prevention of AD and all-type dementia. This benefit observed in both disease states should be interpreted with caution as observational studies are subject to bias, and it is possible that the slight benefit observed may disappear when these biases are addressed in a well-designed randomized controlled trial.

---

### PMID 20859546 — current stance: `inconclusive`

**Golden note:** CV risk factor RCT review — sparse RCT data on prevention.

**Treatment of cardiovascular risk factors to prevent cognitive decline and dementia: a systematic review.**

*Vascular health and risk management*, 2010. Types: Journal Article; Systematic Review

> BACKGROUND: Over the last decade, evidence has accumulated that vascular risk factors increase the risk of Alzheimer disease (AD). So far, few randomized controlled trials have focused on lowering the vascular risk profile to prevent or postpone cognitive decline or dementia. OBJECTIVE: To systematically perform a review of randomized controlled trials (RCTs) evaluating drug treatment effects for cardiovascular risk factors on the incidence of dementia or cognitive decline. SELECTION CRITERIA: RCTs studying the effect of treating hypertension, dyslipidemia, hyperhomocysteinemia, obesity, or diabetes mellitus (DM) on cognitive decline or dementia, with a minimum follow-up of 1 year in elderly populations. OUTCOME MEASURE: Cognitive decline or incident dementia. MAIN RESULTS: In the identified studies, dementia was never the primary outcome. Statins (2 studies) and intensified control of type II DM (1 study) appear to have no effect on prevention of cognitive decline. Studies on treatment of obesity are lacking, and the results of lowering homocysteine (6 studies) are inconclusive. There is some evidence of a preventive effect of antihypertensive medication (6 studies), but results are inconsistent. CONCLUSION: The evidence of a preventive treatment effect aimed at vascular risk factors on cognitive decline and dementia in later life is scarce and mostly based on secondary outcome parameters. Several important sources of bias such as differential dropout may importantly affect interpretation of trial results.

---

### PMID 29914039 — current stance: `inconclusive`

**Golden note:** Vascular risk factor treatment meta — uncertain on AD/dementia incidence.

**Does Treating Vascular Risk Factors Prevent Dementia and Alzheimer's Disease? A Systematic Review and Meta-Analysis.**

*Journal of Alzheimer's disease : JAD*, 2018. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: Epidemiological evidence has associated Alzheimer's disease (AD) with vascular risk factors (VRFs), but whether treatment of VRFs reduces the incidence of dementia and AD is uncertain. OBJECTIVE: To conduct a systematic review and meta-analysis to summarize available data on the impact of treatment of VRFs on dementia and AD incidence. METHODS: Pertinent studies published until 1 January 2018 were identified from PubMed. Both randomized controlled trials (RCT) and prospective studies that investigated the impact of treatment of VRFs on dementia or AD incidence were included. RESULTS: Eight RCTs and 52 prospective studies were identified. Antihypertensive treatment was associated with a non-significant reduced risk of dementia in RCTs (n = 5; relative risk [RR], 0.84; 95% confidence interval [CI], 0.69-1.02) and prospective studies (n = 3; RR, 0.77; 95% CI, 0.58-1.01) and with reduced AD risk in prospective studies (n = 5; RR = 0.78; 95% CI, 0.66-0.91). In prospective studies, treatment of hyperlipidemia with statins, but not nonstatin lipid-lowering agents, was associated with reduced risk of dementia (n = 17; RR, 0.77; 95% CI, 0.63-0.95) and AD (n = 13; RR, 0.86; 95% CI, 0.80-0.92). The single RCT on statins and dementia incidence showed no association. Data from one RCT and six prospective studies did not support a beneficial impact of antidiabetic drugs or insulin therapy on dementia risk. CONCLUSION: Current evidence indicates that antihypertensives and statins might reduce the incidence of dementia and AD. Further trials to determine the effect of VRF on AD are needed.

---

### PMID 27473843 — current stance: `inconclusive`

**Golden note:** TOP-COG Down syndrome statin pilot RCT — small, exploratory.

**Towards onset prevention of cognition decline in adults with Down syndrome (The TOP-COG study): A pilot randomised controlled trial.**

*Trials*, 2016. Types: Journal Article; Randomized Controlled Trial

> BACKGROUND: Dementia is very common in Down syndrome (trisomy 21) adults. Statins may slow brain amyloid β (Aβ, coded on chromosome 21) deposition and, therefore, delay Alzheimer disease onset. One prospective cohort study with Down syndrome adults found participants on statins had reduced risk of incident dementia, but there are no randomised controlled trials (RCTs) on this issue. Evidence is sparse on the best instruments to detect longitudinal cognitive decline in older Down syndrome adults. METHODS: TOP-COG was a feasibility/pilot, double-blind RCT of 12 months simvastatin 40 mg versus placebo for the primary prevention of dementia in Alzheimer disease in Down syndrome adults aged 50 years or older. Group allocation was stratified by age, apolipoprotein E (APOE) ε4 allele status, and cholesterol level. Recruitment was from multiple general community sources over 12 months. Adults with dementia, or simvastatin contraindications, were excluded. Main outcomes were recruitment and retention rates. Cognitive decline was measured with a battery of tests; secondary measures were adaptive behaviour skills, general health, and quality of life. Assessments were conducted pre randomisation and at 12 months post randomisation. Blood Aβ40/Aβ42 levels were investigated as a putative biomarker. Results were analysed on an intention-to-treat basis. A qualitative sub-study was conducted and analysed using the Framework Approach to determine recruitment motivators/barriers, and participation experience. RESULTS: We identified 181 (78 %) of the likely eligible Down syndrome population, and recruited 21 (11.6 %), from an area with a general population size of 3,135,974. Recruitment was highly labour-intensive. Thirteen (62 %) participants completed the full year. Results favoured the simvastatin group. The most appropriate cognitive instrument (regarding ease of completion and detecting change over time) was the Memory for Objects test from the Neuropsychological Assessment of Dementia in Individuals with Intellectual Disabilities battery. Cognitive testing appeared more sensitive than proxy-rated adaptive behaviour, quality of life, or general health scores. Aβ40 levels changed less for the simvastatin group (not statistically significant). People mostly declined to participate because of not wanting to take medication, and not knowing if they would receive simvastatin or placebo. Participants reported enjoying taking part. CONCLUSION: A full-scale RCT is feasible. It will need 37 % UK population coverage to recruit the required 160 participants. Information/education about the importance of RCT participation is needed for this population. TRIAL REGISTRATION: ISRCTN67338640 .

---

### PMID 39963242 — current stance: `inconclusive`

**Golden note:** 2025 cohort meta — effect unclear.

**The role of statins in dementia or Alzheimer's disease incidence: a systematic review and meta-analysis of cohort studies.**

*Frontiers in pharmacology*, 2025. Types: Journal Article; Systematic Review

> BACKGROUND: The effect of statins on the risk of dementia and Alzheimer's disease (AD) is unclear. METHODS: We systematically searched EMBASE, Web of Science, PubMed, CENTRAL and ClinicalTrail.gov for cohort studies comparing incidence of new-onset dementia and AD between statin users and non-users. We applied the DerSimonian-Laird random effects method to pool hazard ratio (HR) with 95% confidence intervals (CI). RESULTS: We included forty-two studies comprising 6,325,740 patients. Thirty-five cohort studies involving 6,306,043 participants were pooled and indicated that statin use was associated with a reduced risk of dementia (HR: 0.79, 95% CI: 0.71-0.88). Similarly, an analysis of 19 studies comprising 1,237,341 participants demonstrated a 29% decrease in the risk of AD among statin users (HR: 0.71, 95% CI: 0.60-0.85). In sensitivity analyses, diagnostic criteria for dementia/AD significantly affected the combined risk estimates. In subgroup analyses, compared to studies enrolling participants with a mean/median age over 70 years, those younger than 70 years exhibited greater efficacy of statins in preventing dementia (HR: 0.67, 95% CI: 0.56-0.81 vs HR: 0.86, 95% CI: 0.78-0.95; P = 0.02) and AD (HR: 0.47, 95% CI: 0.44-0.50 vs. HR: 0.81, 95% CI: 0.71-0.92; P < 0.01). Due to significant heterogeneity in the definitions of statin dosage and exposure duration, pooling the results was abandoned and most studies suggested that higher dosages and longer exposure duration of statins further reduce the risk of dementia and AD. CONCLUSION: Statin use is associated with a reduced incidence of dementia and AD, which might be modified by ages.

---

### PMID 34167639 — current stance: `contradicts`

**Golden note:** ASPREE secondary analysis (n=18,846 ≥65, well-powered) — statin/cognition association uncertain, primary suggests null.

**Effect of Statin Therapy on Cognitive Decline and Incident Dementia in Older Adults.**

*Journal of the American College of Cardiology*, 2021. Types: Journal Article; Observational Study; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> BACKGROUND: The neurocognitive effect of statins in older adults remain uncertain. OBJECTIVES: The aim of this study was to investigate the associations of statin use with cognitive decline and incident dementia among older adults. METHODS: This analysis included 18,846 participants ≥65 years of age in a randomized trial of aspirin, who had no prior cardiovascular events, major physical disability, or dementia initially and were followed for 4.7 years. Outcome measures included incident dementia and its subclassifications (probable Alzheimer's disease, mixed presentations); mild cognitive impairment (MCI) and its subclassifications (MCI consistent with Alzheimer's disease, other MCI); and changes in domain-specific cognition, including global cognition, memory, language and executive function, psychomotor speed, and the composite of these domains. Associations of baseline statin use versus nonuse with dementia and MCI outcomes were examined using Cox proportional hazards models and with cognitive change using linear mixed-effects models, adjusting for potential confounders. The impact of statin lipophilicity on these associations was further examined, and effect modifiers were identified. RESULTS: Statin use versus nonuse was not associated with dementia, MCI, or their subclassifications or with changes in cognitive function scores over time (p > 0.05 for all). No differences were found in any outcomes between hydrophilic and lipophilic statin users. Baseline neurocognitive ability was an effect modifier for the associations of statins with dementia (p for interaction < 0.001) and memory change (p for interaction = 0.02). CONCLUSIONS: In adults ≥65 years of age, statin therapy was not associated with incident dementia, MCI, or declines in individual cognition domains. These findings await confirmation from ongoing randomized trials.

---

