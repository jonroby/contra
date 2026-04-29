# Q1: Does lithium slow cognitive decline in Alzheimer's?

Reviewed against the stricter bar in `.claude/CLAUDE.md`:

- **`contradicts`** if any of: statistically significant negative finding;
  adequately-powered RCT primary endpoint missed; well-powered observational
  null; meta-analysis concluding "no efficacy" / "evidence does not support".
- **`inconclusive`** only if: pilot/feasibility/proof-of-concept; biomarker-only
  with no clinical endpoint; genuinely mixed signal; methods/design paper.
- **`supports`** if statistically significant positive primary clinical finding,
  or meta-analysis pooled effect favoring the intervention.

n=22 PMIDs.

**Current S/C/I**: 12 / 1 / 9
**Proposed S/C/I**: 10 / 4 / 8
**Net flips**: 6

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `41177743` | 2025 | **supports → contradicts** | Frequentist+Bayesian meta of 6 RCTs (n=394). Conclusion verbatim: *"current evidence does not support consistent cognitive or functional benefits in AD dementia."* MMSE MD non-sig. This is the canonical "evidence does not support" trigger. The current note ("positive efficacy framing") misreads the abstract — the framing in the abstract's *background* is positive, but the *conclusion* is null. |
| `38743015` | 2024 | **supports → contradicts** | Meta of 8 observational studies, n=377,060. Pooled OR 0.94 (CI 0.77–1.24) general population, OR 0.69 (CI 0.31–1.65) for AD, both crossing null. Conclusion verbatim: *"do not support a significant association between lithium use and the risk of MNCD."* Well-powered null. |
| `41260370` | 2025 | **supports → inconclusive** | Systematic review of mostly **animal** studies plus a small number of human studies; no pooled clinical efficacy estimate. Conclusion uses the words *"inconsistent effects... in preclinical and clinical trials"* and *"may reverse"*. Mechanism review, not efficacy evidence. |
| `38364914` | 2024 | **supports → inconclusive** | Pooled 17 **preclinical** studies in the meta; only 3 human studies, not pooled. The "evidence" is animal-dominated. Note already says "Despite fewer clinical studies." |
| `38253184` | 2024 | **inconclusive → supports** | Network meta-analysis of 8 RCTs (n=6547). Lithium *significantly* outperformed donanemab, aducanumab, and placebo on MMSE; lithium also outperformed placebo on ADAS-Cog. The note ("results 'elusive'") is a reading of the *background* line; the *results* are positive for lithium. |
| `36049127` | 2023 | **inconclusive → supports** | 13-yr follow-up of the original Lithium-MCI RCT cohort. MMSE 25.5 vs 18.3 (p=0.04, Cohen's d=0.92), Verbal Fluency 34.4 vs 11.6 (p<0.001, d=1.78). Significant cognitive advantage at long follow-up. The "observational re-evaluation" framing is true methodologically but the result is statistically significant on cognition — meets the `supports` bar. |

## Confirmed (no change)

- `41770546` (2026 pilot, none of 6 coprimaries met threshold) — **inconclusive ✓** (CLAUDE.md exempts pilot/feasibility); the CVLT-II p=0.05 is noted but borderline.
- `38657568` (2024 meta, RR 0.59 AD / 0.66 dementia) — **supports ✓**
- `35961514` (2022 NMA: lithium > aducanumab on MMSE) — **supports ✓**
- `31954065` (2020 BD meta, OR 0.51 lithium vs no-lithium for dementia) — **supports ✓**
- `30947755` (2019 long-term aMCI RCT, primary endpoints + CSF Aβ42 positive) — **supports ✓**
- `26402004` (2015 first RCT meta, SMD=-0.41, p=0.04) — **supports ✓**
- `24919696` (2014 SR of trace-dose lithium, all 4 small RCTs positive) — **supports ✓** (defensible)
- `22746245` (2013 microdose RCT, MMSE stabilized vs control) — **supports ✓**
- `21525519` (2011 long-term aMCI RCT, sig P-tau ↓, ADAS-Cog ↑) — **supports ✓**
- `17401045` (2007 BD cohort, 5% AD on lithium vs 33%, p<0.001) — **supports ✓**
- `19573486` (2009 10-week multicenter RCT, ADAS-Cog p=.11) — **contradicts ✓**
- `31156177` (2019 GSK-3i meta, overall null with positive lithium subgroup) — **inconclusive ✓**
- `21875410` (2011 GDNF substudy, no cognitive endpoint) — **inconclusive ✓**
- `19276559` (2009 BDNF substudy of the 19573486 null parent trial) — **inconclusive ✓** (mixed signal vs parent null)
- `18181229` (2008 feasibility, no efficacy claim) — **inconclusive ✓**
- `37732619` (2023 BDNF biomarker substudy in agitation trial) — **inconclusive ✓**

## Cross-cutting issues

- **Same-cohort duplicates** flagged for the planned UI paper-type filter:
  - `30947755` (2019), `21525519` (2011), `36049127` (2023) — all three are
    the same Brazilian Lithium-MCI cohort followed across multiple papers
    (24-mo, 12-mo, and 13-yr re-evaluation). Currently all three count as
    independent `supports` votes but they are one trial.
  - `19573486` (2009 parent), `19276559` (2009 BDNF substudy),
    `21875410` (2011 GDNF substudy) — same German multicenter 10-week trial.

## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

- `41770546` — `pilot_positive` (CVLT-II p=0.05; pilot n=80; coprimaries missed but trend in lithium direction)
- `41260370` — `preclinical_dominated`, `narrative_review`
- `38364914` — `preclinical_dominated`
- `38253184` — (none — clean NMA supports)
- `36049127` — `same_cohort_duplicate` (Brazilian Lithium-MCI cohort)
- `30947755` — `same_cohort_duplicate` (Brazilian Lithium-MCI cohort, 2-yr primary)
- `21525519` — `same_cohort_duplicate` (Brazilian Lithium-MCI cohort, 12-mo)
- `19573486` — (none — clean parent-trial null contradicts)
- `19276559` — `same_cohort_duplicate`, `missed_primary_sig_secondary` (BDNF substudy of 19573486 parent-null trial; sig BDNF + ADAS-Cog signal in substudy contradicts parent's overall null)
- `21875410` — `same_cohort_duplicate` (GDNF substudy of 19573486)
- `37732619` — `missed_primary_sig_secondary`-adjacent (BDNF biomarker substudy of agitation trial)
- `24919696` — `narrative_review` (SR with no pooled estimate; "all 4 small RCTs positive" but unpooled)
- `22746245` — `pilot_positive` (microdose, single-arm-design-leaning, n small)
- `17401045` — (none — clean cohort supports, but small n=66 vs 48)
- All other pmids — untagged (strong/canonical examples for their stance)

## Highest-confidence flips for this question

- `41177743` supports → contradicts (meta concludes "evidence does not support")
- `38743015` supports → contradicts (n=377k observational meta, null)

Both of these are unambiguous mislabels — the abstract's stated conclusion
directly contradicts the current stance.

---

## Abstracts (n=22)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 41770546 — current stance: `inconclusive`

**Evidence span:** > Among 80 participants (mean [SD] age, lithium: 72.93 [8.77] years; placebo: 71.22 [6.47] years; 56% female), none of the 6 coprimary outcomes met the prespecified significance threshold.

**Golden note:** Pilot RCT of low-dose lithium in MCI — feasibility/safety primary, only preliminary efficacy.

**Low-Dose Lithium for Mild Cognitive Impairment: A Pilot Randomized Clinical Trial.**

*JAMA neurology*, 2026. Types: Journal Article; Randomized Controlled Trial

> IMPORTANCE: Lithium deficiency may contribute to Alzheimer disease pathogenesis. No randomized clinical trial has examined lithium's effects on cognition, neuroimaging, and plasma biomarkers in mild cognitive impairment (MCI). OBJECTIVE: To examine the feasibility, safety, and preliminary efficacy of lithium carbonate for delaying cognitive decline in older adults with MCI. DESIGN, SETTING, AND PARTICIPANTS: This single-site, randomized, double-blind, placebo-controlled pilot feasibility clinical trial was conducted at the University of Pittsburgh School of Medicine from February 2018 to August 2024, with 2-year follow-up. Analyses used linear mixed-effects models in the intention-to-treat population. Adults aged 60 years or older with MCI who were free of major psychiatric or neurologic illness and contraindications to lithium were included. Of 170 individuals assessed, 83 were randomized (41 lithium vs 42 placebo), with 80 starting treatment (41 lithium vs 39 placebo). Data were analyzed from August 2024 to December 2025. INTERVENTION: Daily low-dose lithium carbonate or placebo for 2 years. MAIN OUTCOMES AND MEASURES: Six prespecified coprimary outcomes included cognitive performance (California Verbal Learning Test-II [CVLT-II] delayed recall, Brief Visuospatial Memory Test-Revised, preclinical Alzheimer cognitive composite), hippocampal volume, cortical gray matter volume, and brain-derived neurotrophic factor. RESULTS: Among 80 participants (mean [SD] age, lithium: 72.93 [8.77] years; placebo: 71.22 [6.47] years; 56% female), none of the 6 coprimary outcomes met the prespecified significance threshold. Mean (SD) CVLT-II baseline scores were 7.95 (3.4) for lithium and 7.90 (3.9) for placebo; scores declined 1.42 points annually in the placebo group vs 0.73 points in the lithium group (difference, 0.69 points per year; 95% CI, 0.01-1.37; P = .05). Hippocampal and cortical volumes showed a decline over time in both groups, but no significant treatment × time interactions. Serious adverse events occurred in 12 of 41 (29%) receiving lithium vs 9 of 39 (23%) receiving placebo; none were definitely treatment related. One death occurred in the placebo group. Common adverse events included increased creatinine levels (12 of 41 [29%] with lithium vs 12 of 39 [31%] with placebo), diarrhea (12 of 41 [29%] vs 6 of 39 [15%]), tiredness (12 of 41 [29%] vs 6 of 39 [15%]), and tremor occurrence (10 of 41 [24%] vs 6 of 39 [15%]). CONCLUSIONS AND RELEVANCE: This pilot randomized clinical trial established feasibility, confirmed safety and tolerability, and generated effect size estimates for future trials of low-dose lithium in MCI. None of the coprimary outcomes met the prespecified significance threshold. TRIAL REGISTRATION: ClinicalTrials.gov Identifier: NCT03185208.

---

### PMID 41177743 — current stance: `supports`

**Evidence span:** > However, current evidence does not support consistent cognitive or functional benefits in AD dementia.

**Golden note:** Meta-analysis of lithium in AD dementia, frequentist + Bayesian; positive efficacy framing.

**Efficacy and Safety of Lithium for Behavioral and Cognitive Symptoms in Alzheimer's Disease Dementia: A Systematic Review With Frequentist and Bayesian Meta-Analysis.**

*The American journal of geriatric psychiatry : official journal of the American Association for Geriatric Psychiatry*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis; Review

> BACKGROUND: Alzheimer's disease (AD) dementia is the leading cause of cognitive decline in late life, yet treatment options remain limited. Lithium, widely used in bipolar disorder, has been suggested to exert neuroprotective effects through inhibition of GSK-3β and modulation of amyloid and tau pathology. We aimed to evaluate the efficacy and safety of lithium in AD dementia. METHODS: This systematic review and meta-analysis was prospectively registered in PROSPERO and conducted following PRISMA guidelines. We searched PubMed, Embase, and Cochrane Library through April 2025 for randomized controlled trials (RCTs) comparing lithium with placebo or standard therapy in patients with AD dementia or amnestic mild cognitive impairment. Outcomes included cognition (MMSE, ADAS-Cog, memory tasks), function (CDR-SB, conversion to AD), neuropsychiatric symptoms (NPI), CSF biomarkers, and safety (adverse events [AEs], serious AEs [SAEs]). Random-effects meta-analyses were complemented by Bayesian methods and trial sequential analyses. RESULTS: Six RCTs involving 394 participants (196 lithium, 198 placebo) met inclusion criteria. Lithium did not significantly improve global cognition (MMSE: MD -1.61, 95% CI -4.11 to 0.88; ADAS-Cog: MD -1.82, -3.05 to -0.60; both with high heterogeneity). Memory outcomes were mixed, with possible benefit for figure recall but not delayed verbal recall. No consistent benefits were observed for episodic memory, functional outcomes (CDR-SB), neuropsychiatric symptoms, or CSF biomarkers. Safety analyses showed no increased risk of SAEs; drug-related AEs were more frequent but heterogeneous across trials. CONCLUSIONS: Lithium demonstrated an acceptable safety profile within the dosing regimens studied. However, current evidence does not support consistent cognitive or functional benefits in AD dementia. Larger, well-designed RCTs are warranted to clarify its potential therapeutic role.

---

### PMID 41260370 — current stance: `supports`

**Evidence span:** > Long-term low-dose lithium treatment demonstrates inconsistent effects on lowering intracerebral amyloid deposition and reversing AD-related cognitive deficits in preclinical and clinical trials.

**Golden note:** Systematic review of lithium effects on amyloid/tau/cognition; favorable.

**The effects of Lithium on Beta-amyloid deposition and tau phosphorylation: A systematic review.**

*Journal of affective disorders*, 2025. Types: Journal Article; Systematic Review

> BACKGROUND: Lithium demonstrates neuroprotective and neurotrophic effects, and preclinical studies indicate lithium reduces intracerebral amyloid deposition and tau phosphorylation. This systematic review evaluates lithium's effects on beta-amyloid, tau, and cognitive deficits in major neurocognitive disorders. METHODS: A systematic review of primary research was conducted using Embase, PsycInfo, MEDLINE, and PubMed databases from inception to September 2024, following PRISMA criteria. Animal and adult human studies evaluating lithium monotherapy's effects on Alzheimer's Disease (AD) were included. RESULTS: Long-term low-dose lithium treatment demonstrates inconsistent effects on lowering intracerebral amyloid deposition and reversing AD-related cognitive deficits in preclinical and clinical trials. Lithium was reported to slows amyloid plaque formation in pre-plaque stages through increasing heat shock proteins and suppressing protein synthesis in preclinical trials. Intracerebral lithium reduced phosphorylated tau through promoting tau ubiquitination and inhibiting CDK5 signalling in preclinical trials. LIMITATIONS: A comprehensive animal model that accurately represents human AD symptoms and progression, as well as more clinical trials are needed. Several included studies utilize peripheral lithium administration, which complicates assessment of effective intracerebral concentrations. CONCLUSIONS: Lithium potentially reduces intracerebral amyloid deposition and tau phosphorylation in AD animal models and may reverse associated cognitive deficits. Further research should seek to replicate similar findings in larger samples and explore lithium's optimal dosage range in promoting intracerebral amyloid clearance.

---

### PMID 38364914 — current stance: `supports`

**Evidence span:** > A total of 17 preclinical studies were included in the meta-analysis. Our analysis showed that lithium treatment has neuroprotective effects in diseases.

**Golden note:** Meta-analysis on AD + Parkinson's — neuroprotective effects of lithium.

**Lithium and disease modification: A systematic review and meta-analysis in Alzheimer's and Parkinson's disease.**

*Ageing research reviews*, 2024. Types: Meta-Analysis; Systematic Review; Journal Article; Research Support, Non-U.S. Gov't

> The role of lithium as a possible therapeutic strategy for neurodegenerative diseases has generated scientific interest. We systematically reviewed and meta-analyzed pre-clinical and clinical studies that evidenced the neuroprotective effects of lithium in Alzheimer's (AD) and Parkinson's disease (PD). We followed the PRISMA guidelines and performed the systematic literature search using PubMed, EMBASE, Web of Science, and Cochrane Library. A total of 32 articles were identified. Twenty-nine studies were performed in animal models and 3 studies were performed on human samples of AD. A total of 17 preclinical studies were included in the meta-analysis. Our analysis showed that lithium treatment has neuroprotective effects in diseases. Lithium treatment reduced amyloid-β and tau levels and significantly improved cognitive behavior in animal models of AD. Lithium increased the tyrosine hydroxylase levels and improved motor behavior in the PD model. Despite fewer clinical studies on these aspects, we evidenced the positive effects of lithium in AD patients. This study lends further support to the idea of lithium's therapeutic potential in neurodegenerative diseases.

---

### PMID 38743015 — current stance: `supports`

**Evidence span:** > The results of this systematic review and meta-analysis do not support a significant association between lithium use and the risk of MNCD.

**Golden note:** Meta-analysis: lithium use associated with reduced major neurocognitive disorder risk.

**Lithium Exposure and Risk of Major Neurocognitive Disorders: A Systematic Review and Meta-analysis.**

*Journal of clinical psychopharmacology*, 2024. Types: Systematic Review; Meta-Analysis; Journal Article

> BACKGROUND: Published studies on the association between lithium use and the decreased risk of major neurocognitive disorders (MNCDs) have shown disparities in their conclusions. We aimed to provide updated evidence of this association. METHODS: A comprehensive literature search was performed in PubMed, EMBASE, and Cochrane Library from inception until August 31, 2023. All the observational studies evaluating the association between lithium use and MNCD risk were eligible for inclusion. Pooled odds ratios (ORs) and 95% prediction intervals were computed using random-effects models. RESULTS: Eight studies with 377,060 subjects were included in the analysis. In the general population on the association between lithium use versus nonuse and dementia, the OR was 0.94 (95% confidence interval [CI] = 0.77-1.24). Further analysis also demonstrated that lithium use was not associated with an increased risk of Alzheimer's disease (OR = 0.69, 95% CI: 0.31-1.65). When the analysis was restricted to individuals with bipolar disorder to reduce the confounding by clinical indication, lithium exposure was also not associated with a decreased risk of MNCD (OR = 0.9, 95% CI = 0.71-1.15). CONCLUSION: The results of this systematic review and meta-analysis do not support a significant association between lithium use and the risk of MNCD.

---

### PMID 38657568 — current stance: `supports`

**Evidence span:** > The forest plot results showed that taking lithium therapy reduced the risk of AD (RR 0.59, 95% confidence interval [CI]: 0.44-0.78) and is also protective in reducing the risk of dementia (RR 0.66, 95% CI: 0.56-0.77).

**Golden note:** Meta-analysis: lithium therapy lowers dementia/AD risk.

**Lithium Therapy's Potential to Lower Dementia Risk and the Prevalence of Alzheimer's Disease: A Meta-Analysis.**

*European neurology*, 2024. Types: Journal Article; Meta-Analysis; Systematic Review

> INTRODUCTION: Dementia is a neurodegenerative disease with insidious onset and progressive progression, of which the most common type is Alzheimer's disease (AD). Lithium, a trace element in the body, has neuroprotective properties. However, whether lithium can treat dementia or AD remains a highly controversial topic. Therefore, we conducted a meta-analysis. METHODS: A systematic literature review was conducted on PubMed, Embase, and Web of Science. Comparison of the effects of lithium on AD or dementia in terms of use, duration, and dosage, and meta-analysis to test whether lithium therapy is beneficial in ameliorating the onset of dementia or AD. Sensitivity analyses were performed using a stepwise exclusion method. The Newcastle-Ottawa Scale (NOS) was used to assess the quality of included studies. We determined the relative risk (RR) between patient groups using a random-effects model. RESULTS: A total of seven studies were included. The forest plot results showed that taking lithium therapy reduced the risk of AD (RR 0.59, 95% confidence interval [CI]: 0.44-0.78) and is also protective in reducing the risk of dementia (RR 0.66, 95% CI: 0.56-0.77). The duration of lithium therapy was able to affect dementia incidence (RR 0.70, 95% CI: 0.55-0.88); however, it is unclear how this effect might manifest in AD. It is also uncertain how many prescriptions for lithium treatment lower the chance of dementia development. CONCLUSION: The duration of treatment and the usage of lithium therapy seem to lower the risk of AD and postpone the onset of dementia.

---

### PMID 38253184 — current stance: `inconclusive`

**Evidence span:** > On the Mini-Mental State Examination, lithium significantly outperformed donanemab, aducanumab and placebo. On the Alzheimer's Disease Assessment Scale-cognitive subscale, the efficacy of all active drugs was significantly higher than placebo.

**Golden note:** Network meta-analysis comparing lithium to anti-amyloids; results 'elusive'.

**Comparative efficacy, tolerability and acceptability of donanemab, lecanemab, aducanumab and lithium on cognitive function in mild cognitive impairment and Alzheimer's disease: A systematic review and network meta-analysis.**

*Ageing research reviews*, 2024. Types: Comparative Study; Journal Article; Systematic Review; Network Meta-Analysis

> BACKGROUND: The comparative clinical utility of the disease-modifying treatments for mild cognitive impairment and Alzheimer's disease that are approved or under review by the Food and Drug Administration (i.e., donanemab, lecanemab and aducanumab), and lithium, which is a potential disease-modifying agent for this condition, remains elusive. OBJECTIVE: We aimed to compare the efficacy on cognitive decline, tolerability and acceptability of these drugs in this condition. METHODS: We systematically searched in MEDLINE, CENTRAL, CINHAL and ClinicalTrials,gov for randomized controlled trials from their inception to 7 November 2023, and then performed a random-effect network meta-analysis. RESULTS: The analysis included 8 randomized placebo-controlled trials with 6547 participants. On the Mini-Mental State Examination, lithium significantly outperformed donanemab, aducanumab and placebo. On the Alzheimer's Disease Assessment Scale-cognitive subscale, the efficacy of all active drugs was significantly higher than placebo. In addition, in the Clinical Dementia Rating sum of boxes, the efficacy of donanemab and lecanemab was significantly higher than placebo. Compared to placebo, donanemab and lecanemab were significantly less acceptable and tolerable. Aducanumab was also less well tolerated compared to placebo. There were no significant differences in the other comparisons. CONCLUSION: Although it is yet to be determined which is more effective between lithium or lecanemab or donanemab, lithium may be more effective than aducanumab. Aducanumab, lecanemab and donanemab do not appear to differ in their effectiveness on cognitive function. Low-dose lithium may be safer than aducanumab, lecanemab and donanemab.

---

### PMID 36049127 — current stance: `inconclusive`

**Evidence span:** > We found statistically significant differences in current mean Mini Mental State Examination score according to previous treatment group (25.5 [SD, 5.3] vs. 18.3 [SD, 10.9], p = 0.04). The lithium group also had better performance in the phonemic Verbal Fluency Test than the control group (34.4 [SD, 14.4] vs. 11.6 [SD, 10.10], p < 0.001).

**Golden note:** 13-year follow-up of MCI lithium trial — observational re-evaluation.

**Revisiting global cognitive and functional state 13 years after a clinical trial of lithium for mild cognitive impairment.**

*Revista brasileira de psiquiatria (Sao Paulo, Brazil : 1999)*, 2023. Types: Randomized Controlled Trial; Journal Article

> OBJECTIVES: To re-evaluate a sample of older adults enrolled in a randomized controlled trial of lithium for amnestic mild cognitive impairment (MCI) after 11 to 15 years, re-assessing their current (or last available) global cognitive and functional state. METHODS: We recalled all former participants of the Lithium-MCI trial conducted by our group between 2009 and 2012 to perform a single-blinded, cross-sectional evaluation of their global clinical state to compare the long-term outcome of those who received lithium vs. those who received placebo. RESULTS: Of the original sample (n=61), we were able to reach 36 participants (59% of retention), of whom 22 had previously received lithium (61% of the recall sample) and 14 (39%) had received placebo. Since 30.5% of the recalled sample was deceased, psychometric data were collected only for 69.5% of the participants. We found statistically significant differences in current mean Mini Mental State Examination score according to previous treatment group (25.5 [SD, 5.3] vs. 18.3 [SD, 10.9], p = 0.04). The lithium group also had better performance in the phonemic Verbal Fluency Test than the control group (34.4 [SD, 14.4] vs. 11.6 [SD, 10.10], p < 0.001). Differences in these measures also had large effect sizes, as shown by Cohen's d values of 0.92 and 1.78, respectively. CONCLUSION: This data set suggests that older adults with amnestic MCI who had been treated with lithium during a previous randomized controlled trial had a better long-term global cognitive outcome than those from a matched sample who did not receive the intervention.

---

### PMID 37732619 — current stance: `inconclusive`

**Evidence span:** > BDNF levels did not change significantly and were not associated with improvement in overall neuropsychiatric symptoms or in cognitive function.

**Golden note:** BDNF biomarker effects of lithium in AD with agitation; not cognitive endpoint.

**Effects of lithium on serum Brain-Derived Neurotrophic Factor in Alzheimer's patients with agitation.**

*International journal of geriatric psychiatry*, 2023. Types: Randomized Controlled Trial; Journal Article; Research Support, N.I.H., Extramural

> BACKGROUND: There is ample evidence in animal models that lithium increases Brain-Derived Neurotrophic Factor (BDNF) with supporting evidence in human studies. Little is known, however, about the effects of lithium on BDNF in Alzheimer's Dementia (AD). In one study of patients with Mild Cognitive Impairment, serum BDNF increased after treatment with lithium. These patients also showed mild improvement in cognitive function. OBJECTIVES: To evaluate low-dose lithium treatment of agitation in Alzheimer's disease (AD). METHOD: We measured levels of BDNF in patients treated with lithium prior to and after a 12-week randomized placebo-controlled trial. RESULTS: BDNF levels did not change significantly and were not associated with improvement in overall neuropsychiatric symptoms or in cognitive function. CONCLUSIONS: More research is needed to understand the potential effects of lithium on BDNF in AD including whether its use might be dependent on the stage of cognitive decline and dementia.

---

### PMID 35961514 — current stance: `supports`

**Evidence span:** > Network meta-analysis demonstrated that lithium was significantly more effective than aducanumab in the primary outcome.

**Golden note:** Network meta-analysis lithium vs aducanumab on cognitive decline.

**Comparative efficacy of lithium and aducanumab for cognitive decline in patients with mild cognitive impairment or Alzheimer's disease: A systematic review and network meta-analysis.**

*Ageing research reviews*, 2022. Types: Journal Article; Systematic Review; Network Meta-Analysis

> BACKGROUND: In 2021, the US Food and Drug Administration granted an accelerated approval to aducanumab for patients with mild cognitive impairment (MCI) and mild dementia caused by Alzheimer's disease (AD); however, the cost of aducanumab is high, at approximately $28,000 for one year per person. On the other hand, lithium is much cheaper at $40 a year, and has been reported to be effective for the cognitive decline observed in both patients with MCI and AD. In contrast to acetylcholinesterase inhibitors and N-methyl D-aspartate receptor antagonists, aducanumab and lithium may be disease-modifying drugs. Therefore, we focused on aducanumab and lithium and compared the effects of these drugs on the cognitive decline in MCI and AD patients using a network meta-analysis. METHODS: PubMed, the Cochrane Library, CINHAL, and ClinicalTrials.gov were searched for randomized controlled trials testing lithium or aducanumab for the treatment of cognitive decline in patients with MCI or AD, up to January 31, 2022. A frequentist fixed-effect network meta-analysis was performed to estimate direct and indirect effects. The primary outcome was change scores in cognitive decline measured by Mini-Mental State Examination. This study has been registered with PROSPERO (number CRD42022304807). RESULTS: Network meta-analysis demonstrated that lithium was significantly more effective than aducanumab in the primary outcome. CONCLUSION: Although there were various limitations in this study, lithium may be a more cost-effective treatment than aducanumab for MCI and AD.

---

### PMID 31954065 — current stance: `supports`

**Evidence span:** > BD increases the risk of dementia (odds ratio (OR): 2.96 [95% CI: 2.09-4.18], P < 0.001), and treatment with lithium decreases the risk of dementia in BD (OR: 0.51 [95% CI: 0.36-0.72], P < 0.0001).

**Golden note:** Meta-analysis: lithium associated with lower dementia risk in bipolar disorder.

**Risk of dementia in bipolar disorder and the interplay of lithium: a systematic review and meta-analyses.**

*Acta psychiatrica Scandinavica*, 2020. Types: Journal Article; Meta-Analysis; Systematic Review

> OBJECTIVES: To assess whether bipolar disorder (BD) increases the rate of dementia and whether lithium is related to a lower risk of dementia in BD. METHODS: A total of 10 studies (6859 BD; 487 966 controls) were included in the meta-analysis to test whether BD is a risk factor for dementia. In addition, five studies (6483 lithium; 43 496 non-lithium) were included in the meta-analysis about the potential protective effect of lithium in BD. RESULTS: BD increases the risk of dementia (odds ratio (OR): 2.96 [95% CI: 2.09-4.18], P < 0.001), and treatment with lithium decreases the risk of dementia in BD (OR: 0.51 [95% CI: 0.36-0.72], P < 0.0001). In addition, secondary findings from our systematic review showed that the risk of progression to dementia is higher in BD than in major depressive disorder (MDD). Moreover, the number of mood episodes predicted the development of dementia in BD. CONCLUSION: Individuals with BD are at higher risk of dementia than both the general population or those with MDD. Lithium appears to reduce the risk of developing dementia in BD.

---

### PMID 31156177 — current stance: `inconclusive`

**Evidence span:** > There was no significant difference in cognitive function scores between the GSK-3 inhibitors and placebo groups [standardized mean difference (SMD) = -0.25, p = 0.11, I2 = 55% ]. A sensitivity analysis revealed that the lithium subgroup was more effective on cognitive function scores than placebo for AD and MCI (lithium subgroup: SMD = -0.41, p = 0.04; tideglusib subgroup: SMD = -0.02, p = 0.89).

**Golden note:** GSK-3 inhibitor RCT meta-analysis (lithium is GSK-3 inhibitor); efficacy 'unknown'.

**Efficacy and Safety of Glycogen Synthase Kinase 3 Inhibitors for Alzheimer's Disease: A Systematic Review and Meta-Analysis.**

*Journal of Alzheimer's disease : JAD*, 2019. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: The efficacy and safety of glycogen synthase kinase 3 (GSK-3) inhibitors in patients with Alzheimer's disease (AD) is unknown. OBJECTIVE: A systematic review and meta-analysis of randomized controlled trials (RCTs) to test GSK-3 inhibitors on AD patients. METHODS: We included RCTs of GSK-3 inhibitors in AD patients and subjects with mild cognitive impairment (MCI), using cognitive function scores as a primary measure. RESULTS: Five RCTs (three RCTs using lithium and two RCTs using tideglusib) with 568 patients were included. There was no significant difference in cognitive function scores between the GSK-3 inhibitors and placebo groups [standardized mean difference (SMD) = -0.25, p = 0.11, I2 = 55% ]. However, significant heterogeneity remained. A sensitivity analysis revealed that the lithium subgroup was more effective on cognitive function scores than placebo for AD and MCI (lithium subgroup: SMD = -0.41, p = 0.04; tideglusib subgroup: SMD = -0.02, p = 0.89). Moreover, a meta-regression analysis showed that the effect size of GSK-3 inhibitors on cognitive function scores was associated with study duration (coefficient, -0.0116). For safety outcomes, tideglusib was associated with a higher incidence of increased aspartate aminotransferase than placebo. There were no significant differences in other secondary outcomes between treatments. CONCLUSION: Our results suggested that GSK-3 inhibitors were ineffective in treating AD and MCI; however, several studies included in the present meta-analysis were small, and future studies using a larger sample size are needed.

---

### PMID 30947755 — current stance: `supports`

**Evidence span:** > Long-term lithium attenuates cognitive and functional decline in amnestic MCI, and modifies Alzheimer's disease-related CSF biomarkers.

**Golden note:** RCT of long-term lithium in amnestic MCI — clinical/biological effects positive.

**Clinical and biological effects of long-term lithium treatment in older adults with amnestic mild cognitive impairment: randomised clinical trial.**

*The British journal of psychiatry : the journal of mental science*, 2019. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Experimental studies indicate that lithium may facilitate neurotrophic/protective responses in the brain. Epidemiological and imaging studies in bipolar disorder, in addition to a few trials in Alzheimer's disease support the clinical translation of these findings. Nonetheless, there is limited controlled data about potential use of lithium to treat or prevent dementia. AIMS: To determine the benefits of lithium treatment in patients with amnestic mild cognitive impairment (MCI), a clinical condition associated with high risk for Alzheimer's disease. METHOD: A total of 61 community-dwelling, physically healthy, older adults with MCI were randomised to receive lithium or placebo (1:1) for 2 years (double-blind phase), and followed-up for an additional 24 months (single-blinded phase) (trial registration at clinicaltrials.gov: NCT01055392). Lithium carbonate was prescribed to yield subtherapeutic concentrations (0.25-0.5 mEq/L). Primary outcome variables were the cognitive (Alzheimer's Disease Assessment Scale - cognitive subscale) and functional (Clinical Dementia Rating - Sum of Boxes) parameters obtained at baseline and after 12 and 24 months. Secondary outcomes were neuropsychological test scores; cerebrospinal fluid (CSF) concentrations of Alzheimer's disease-related biomarkers determined at 0, 12 and 36 months; conversion rate from MCI to dementia (0-48 months). RESULTS: Participants in the placebo group displayed cognitive and functional decline, whereas lithium-treated patients remained stable over 2 years. Lithium treatment was associated with better performance on memory and attention tests after 24 months, and with a significant increase in CSF amyloid-beta peptide (Aβ1-42) after 36 months. CONCLUSIONS: Long-term lithium attenuates cognitive and functional decline in amnestic MCI, and modifies Alzheimer's disease-related CSF biomarkers. The present data reinforces the disease-modifying properties of lithium in the MCI-Alzheimer's disease continuum. DECLARATION OF INTEREST: None.

---

### PMID 26402004 — current stance: `supports`

**Evidence span:** > Lithium significantly decreased cognitive decline as compared to placebo (standardized mean difference = -0.41, 95% confidence interval = -0.81 to -0.02, p = 0.04, I2 = 47% , 3 studies, n = 199).

**Golden note:** First meta-analysis of RCTs of lithium in AD/MCI — positive.

**Lithium as a Treatment for Alzheimer's Disease: A Systematic Review and Meta-Analysis.**

*Journal of Alzheimer's disease : JAD*, 2015. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: This is the first meta-analysis of randomized placebo-controlled trials testing lithium as a treatment for patients with Alzheimer's disease (AD) and individuals with mild cognitive impairment (MCI). METHODS: The primary outcome measure was efficacy on cognitive performance as measured through the Alzheimer's Disease Assessment Scale cognitive subscale or the Mini-Mental State Examination. Other outcome measures were drug discontinuation rate, individual side effects, and biological markers (phosphorylated tau 181, total tau, and amyloid-β42) in cerebrospinal fluid (CSF). RESULTS: Three clinical trials including 232 participants that met the study's inclusion criteria were identified. Lithium significantly decreased cognitive decline as compared to placebo (standardized mean difference = -0.41, 95% confidence interval = -0.81 to -0.02, p = 0.04, I2 = 47% , 3 studies, n = 199). There were no significant differences in the rate of attrition, discontinuation due to all causes or adverse events, or CSF biomarkers between treatment groups. CONCLUSIONS: The results indicate that lithium treatment may have beneficial effects on cognitive performance in subjects with MCI and AD dementia.

---

### PMID 24919696 — current stance: `supports`

**Evidence span:** > All four small randomized clinical trials of lithium for Alzheimer's dementia have found at least some clinical or biological benefits versus placebo.

**Golden note:** Systematic review of trace-dose lithium for dementia prevention — positive.

**Standard and trace-dose lithium: a systematic review of dementia prevention and other behavioral benefits.**

*The Australian and New Zealand journal of psychiatry*, 2014. Types: Journal Article; Systematic Review

> OBJECTIVE: Dementia is a major public health issue, with notably high rates in persons with mood illnesses. Lithium has been shown to have considerable neuroprotective effects, even in trace or low doses. The aim of this review is to summarize the current understanding of lithium benefits in trace or low doses in dementia prevention and for other behavioral or medical benefits. METHODS: A systematic review identified 24 clinical, epidemiological, and biological reports that met inclusion criteria of assessing lithium in standard or low doses for dementia or other behavioral or medical benefits. RESULTS: Five out of seven epidemiological studies found an association between standard-dose lithium and low dementia rates. Nine out of 11 epidemiological studies, usually of drinking water sources, found an association between trace-dose lithium and low suicide/homicide/mortality and crime rates. All four small randomized clinical trials of lithium for Alzheimer's dementia have found at least some clinical or biological benefits versus placebo. Only one small randomized clinical trial (RCT) of trace lithium has been conducted, assessing mood symptoms in former substance abusers, and found benefit with lithium versus placebo. CONCLUSIONS: Lithium, in both standard and trace doses, appears to have biological benefits for dementia, suicide, and other behavioral outcomes. Further RCT research of trace lithium in dementia is warranted.

---

### PMID 22746245 — current stance: `supports`

**Evidence span:** > In the evaluation phase, the treated group showed no decreased performance in the mini-mental state examination test, in opposition to the lower scores observed for the control group during the treatment, with significant differences starting three months after the beginning of the treatment, and increasing progressively.

**Golden note:** Microdose lithium stabilized cognitive impairment in AD patients.

**Microdose lithium treatment stabilized cognitive impairment in patients with Alzheimer's disease.**

*Current Alzheimer research*, 2013. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> A lower incidence of dementia in bipolar patients treated with lithium has been described. This metal inhibits the phosphorylation of glycogen-synthase-kinase 3-α and β, which are related to amyloid precursor protein processing and tau hyperphosphorylation in pathological conditions, respectively. Following the same rationale, a group just found that lithium has disease-modifying properties in amnestic mild cognitive impairment with potential clinical implications for the prevention of Alzheimer's Disease (AD) when a dose ranging from 150 to 600 mg is used. As lithium is highly toxic in regular doses, our group evaluated the effect of a microdose of 300 μg, administered once daily on AD patients for 15 months. In the evaluation phase, the treated group showed no decreased performance in the mini-mental state examination test, in opposition to the lower scores observed for the control group during the treatment, with significant differences starting three months after the beginning of the treatment, and increasing progressively. This data suggests the efficacy of a microdose lithium treatment in preventing cognitive loss, reinforcing its therapeutic potential to treat AD using very low doses.

---

### PMID 21525519 — current stance: `supports`

**Evidence span:** > Lithium treatment was associated with a significant decrease in CSF concentrations of P-tau (P = 0.03) and better performance on the cognitive subscale of the Alzheimer's Disease Assessment Scale and in attention tasks.

**Golden note:** RCT long-term lithium in aMCI — disease-modifying focus, positive.

**Disease-modifying properties of long-term lithium treatment for amnestic mild cognitive impairment: randomised controlled trial.**

*The British journal of psychiatry : the journal of mental science*, 2011. Types: Journal Article; Randomized Controlled Trial

> BACKGROUND: Two recent clinical studies support the feasibility of trials to evaluate the disease-modifying properties of lithium in Alzheimer's disease, although no benefits were obtained from short-term treatment. AIMS: To evaluate the effect of long-term lithium treatment on cognitive and biological outcomes in people with amnestic mild cognitive impairment (aMCI). METHOD: Forty-five participants with aMCI were randomised to receive lithium (0.25-0.5 mmol/l) (n = 24) or placebo (n = 21) in a 12-month, double-blind trial. Primary outcome measures were the modification of cognitive and functional test scores, and concentrations of cerebrospinal fluid (CSF) biomarkers (amyloid-beta peptide (Aβ(42)), total tau (T-tau), phosphorylated-tau) (P-tau). TRIAL REGISTRATION: NCT01055392. RESULTS: Lithium treatment was associated with a significant decrease in CSF concentrations of P-tau (P = 0.03) and better perform-ance on the cognitive subscale of the Alzheimer's Disease Assessment Scale and in attention tasks. Overall tolerability of lithium was good and the adherence rate was 91%. CONCLUSIONS: The present data support the notion that lithium has disease-modifying properties with potential clinical implications in the prevention of Alzheimer's disease.

---

### PMID 21875410 — current stance: `inconclusive`

**Evidence span:** > However, we could not show a difference in GDNF concentrations between the patients after the treatment with lithium or placebo (serum, mean ± standard deviation: 434.3 ± 117.9 pg/ml versus 543.8 ± 250.0 pg/ml, p = 0.178; CSF, 62.3 ± 37.4 pg/ml versus 72.8 ± 43.9 pg/ml, p = 0.511).

**Golden note:** GDNF biomarker study in AD on lithium; not cognitive endpoint.

**Influence of lithium treatment on GDNF serum and CSF concentrations in patients with early Alzheimer's disease.**

*Current Alzheimer research*, 2011. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Preclinical and clinical studies gave evidence that lithium could be useful in the treatment of Alzheimer's disease (AD). One possible mechanism of action might be the induction of neurotrophins. Recently, we found a significant increase of brain-derived neurotrophic factor (BDNF) serum levels in AD patients treated with lithium and a significant decrease of ADAS Cog sum scores in comparison to placebo-treated patients. In another previous study we have shown that glial cell line-derived neurotrophic factor (GDNF) levels in CSF of patients with early AD are increased most probably due to an upregulated expression in CNS as an adaptive process of the impaired brain to enhance neurotrophic support at least in early stages of disease. Here we assessed the influence of a lithium treatment on GDNF serum and cerebrospinal fluid (CSF) concentrations in a subset of a greater sample recruited for a randomized, single-blinded, placebo-controlled, parallel-group multicenter 10-week study, investigating the efficacy of lithium treatment in AD patients. We found a significant negative correlation of lithium concentration in serum with GDNF concentration in CSF at the end of treatment (r = -0.585, p = 0.036) and with the difference of GDNF concentration in CSF before and after treatment (r = - 0.755, p = 0.003). However, we could not show a difference in GDNF concentrations between the patients after the treatment with lithium or placebo (serum, mean ± standard deviation: 434.3 ± 117.9 pg/ml versus 543.8 ± 250.0 pg/ml, p = 0.178; CSF, 62.3 ± 37.4 pg/ml versus 72.8 ± 43.9 pg/ml, p = 0.511). The findings of the present investigation indicated that beneficial effects of the lithium treatment might reduce the necessity of enhanced GDNF expression in the CNS in early AD.

---

### PMID 19573486 — current stance: `contradicts`

**Evidence span:** > Lithium treatment did not lead to change in global cognitive performance as measured by the ADAS-Cog subscale (P = .11) or in depressive symptoms.

**Golden note:** 10-week lithium AD RCT — short-term, GSK-3/tau focus, canonical null result.

**Lithium trial in Alzheimer's disease: a randomized, single-blind, placebo-controlled, multicenter 10-week study.**

*The Journal of clinical psychiatry*, 2009. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> OBJECTIVE: Lithium, a first-line drug for the treatment of bipolar depression, has recently been shown to regulate glycogen synthase kinase-3 (GSK-3), a kinase that is involved in the phosphorylation of the tau protein. Since hyperphosphorylation of tau is a core pathological feature in Alzheimer's disease, lithium-induced inhibition of GSK-3 activity may have therapeutic effects in Alzheimer's disease. In the current study, we tested the effect of short-term lithium treatment in patients with Alzheimer's disease. METHOD: A total of 71 patients with mild Alzheimer's disease (Mini-Mental State Examination score > or = 21 and < or = 26) were successfully randomly assigned to placebo (N = 38) or lithium treatment (N = 33) at 6 academic expert memory clinics. The 10-week treatment included a 6-week titration phase to reach the target serum level of lithium (0.5-0.8 mmol/L). The primary outcome measures were cerebrospinal fluid (CSF) levels of phosphorylated tau (p-tau) and GSK-3 activity in lymphocytes. Secondary outcome measures were CSF concentration of total tau and beta-amyloid(1-42) (Abeta(1-42)), plasma levels of Abeta(1-42), Alzheimer's Disease Assessment Scale (ADAS)-Cognitive summary scores, MMSE, and Neuropsychiatric Inventory (NPI). Patients were enrolled in the study from November 2004 to July 2005. RESULTS: No treatment effect on GSK-3 activity or CSF-based biomarker concentrations (P > .05) was observed. Lithium treatment did not lead to change in global cognitive performance as measured by the ADAS-Cog subscale (P = .11) or in depressive symptoms. CONCLUSIONS: The current results do not support the notion that lithium treatment may lead to reduced hyperphosphorylation of tau protein after a short 10-week treatment in the Alzheimer's disease target population. TRIAL REGISTRATION: (Controlled-Trials.com) Identifier: ISRCTN72046462.

---

### PMID 19276559 — current stance: `inconclusive`

**Evidence span:** > In AD patients treated with lithium, a significant increase of BDNF serum levels, and additionally a significant decrease of ADAS-Cog sum scores in comparison to placebo-treated patients, were found.

**Golden note:** BDNF biomarker increase in early AD on lithium; not cognitive endpoint.

**Increase of BDNF serum concentration in lithium treated patients with early Alzheimer's disease.**

*Journal of Alzheimer's disease : JAD*, 2009. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Preclinical and clinical studies gave evidence that lithium could be useful in the treatment of Alzheimer's disease (AD). In experimental investigations, lithium induces brain-derived neurotrophic factor (BDNF). Recent studies have found a decrease of BDNF in the serum and brains of AD patients with potentially consecutive lack of neurotrophic support. We assessed the influence of a lithium treatment on BDNF serum concentration in a subset of a greater sample recruited for a randomized, single-blinded, placebo-controlled, parallel-group multicenter 10-week study, investigating the efficacy of lithium treatment in AD patients. In AD patients treated with lithium, a significant increase of BDNF serum levels, and additionally a significant decrease of ADAS-Cog sum scores in comparison to placebo-treated patients, were found. Diminution of cognitive impairment was inversely correlated with lithium serum concentration. Upregulation of BDNF might be part of a neuroprotective effect of lithium in AD patients. The results of the present investigation encourage performing studies with longer treatment phases to observe potential positive long-term effects of lithium in AD patients.

---

### PMID 18181229 — current stance: `inconclusive`

**Evidence span:** > Lithium treatment in elderly people with AD has relatively few side effects and those that were apparently due to treatment were mild and reversible. Nonetheless discontinuation rates are high.

**Golden note:** Feasibility/tolerability study; no efficacy claim.

**A feasibility and tolerability study of lithium in Alzheimer's disease.**

*International journal of geriatric psychiatry*, 2008. Types: Clinical Trial; Journal Article; Research Support, Non-U.S. Gov't

> OBJECTIVE: To assess the safety and feasibility of prescribing long term lithium to elderly people with mild to moderate Alzheimer's disease (AD). METHODS: An open label treatment group with low dose lithium for up to 1 year with the Lithium Side Effects Rating Scale as the primary outcome measure. A comparison group matched for cognition and age not receiving lithium therapy. RESULTS: Twenty-two people with AD initiated lithium. Fourteen participants discontinued therapy after a mean of 16 weeks of treatment compared to the 39 weeks for those continuing to take treatment at the end of the study. Three patients discontinued treatment due to possible side effects that abated on ceasing therapy. The reports of side effects on the primary outcome scale did not differ between those discontinuing therapy and those remaining in the study. Two patients died whilst receiving lithium--in neither case was the treatment felt to be related to cause of death. There was no difference in deaths, drop outs or change in MMSE between those receiving lithium and the comparison group. CONCLUSIONS: Lithium treatment in elderly people with AD has relatively few side effects and those that were apparently due to treatment were mild and reversible. Nonetheless discontinuation rates are high. The use of lithium as a potential disease modification therapy in AD should be explored further but is not without problems.

---

### PMID 17401045 — current stance: `supports`

**Evidence span:** > Alzheimer's disease was diagnosed in 3 patients (5%) on lithium and in 16 patients (33%) who were not on lithium (P<0.001).

**Golden note:** Cohort: lower AD prevalence in BD patients on long-term lithium.

**Lithium and risk for Alzheimer's disease in elderly patients with bipolar disorder.**

*The British journal of psychiatry : the journal of mental science*, 2007. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> Bipolar disorder is associated with increased risk for dementia. We compared the prevalence of Alzheimer's disease between 66 elderly euthymic patients with bipolar disorder who were on chronic lithium therapy and 48 similar patients without recent lithium therapy. The prevalence of dementia in the whole sample was 19% v. 7% in an age-comparable population. Alzheimer's disease was diagnosed in 3 patients (5%) on lithium and in 16 patients (33%) who were not on lithium (P<0.001). Our case-control data suggest that lithium treatment reduced the prevalence of Alzheimer's disease in patients with bipolar disorder to levels in the general elderly population. This is in accordance with reports that lithium inhibits crucial processes in the pathogenesis of Alzheimer's disease.

---

