# Q6: Does intranasal insulin improve cognition in mild Alzheimer's disease?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=17 PMIDs.

**Current S/C/I**: 9 / 1 / 7
**Proposed S/C/I**: 6 / 3 / 8
**Net flips**: 5

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `41436338` | 2025 | **inconclusive → contradicts** | 2025 meta of 5 RCTs, n=540 (includes Craft 2020). Verbatim: *"no significant differences between intranasal insulin and placebo for ADAS-Cog13... CDR-SB... DSRS... or delayed recall."* Conclusion: *"Current evidence does not support its routine clinical use."* This is the canonical "evidence does not support" trigger applied to the most recent meta of the field. |
| `36172480` | 2022 | **supports → contradicts** | Meta of 16 RCTs, n=899. Verbatim: *"The pooled standard mean difference (SMD) showed no significant difference between IN insulin and placebo groups; however, statistical results suggested a difference between study groups in the effects of ADCS-ADL; AD patients with APOE4(−) also showed improved performance in verbal memory; other cognitions did not improve significantly."* Pooled cognitive SMD non-sig; only one functional and one subgroup measure sig. The headline is null. |
| `25374101` | 2015 | **supports → inconclusive** | Insulin detemir RCT, n=60, 21 days. APOE-moderated split direction: *"reflecting improvement for APOE-ε4 carriers (p<0.02), and **worsening** for non-carriers (p<0.02)."* Treatment is helping one subgroup and harming the other — that's the definition of a genuinely mixed signal, which CLAUDE.md routes to `inconclusive`. |
| `22162476` | 2011 | **supports → inconclusive** | 2011 SR of 8 studies (n=328), mostly **healthy subjects**. Only 3 studies in MCI/AD. Conclusion is hedged: *"current limited clinical experience suggests potential beneficial cognitive effects."* Mostly off-target population (healthy adults), and the SR explicitly frames as "potential" / "preliminary." |
| `34101779` | 2021 | **supports → inconclusive** | Secondary analysis of NCT01767909 — i.e., the **same trial** as Craft 2020 (`32568367`), whose primary endpoint failed. Reports WMH reduction. The study is being labeled `supports` based on a secondary biomarker outcome of a trial that overall did not meet its primary cognitive endpoint. Substudy framing applies. |

### Borderline

| PMID | Year | Status | Notes |
|------|------|--------|-------|
| `33719017` | 2021 | **inconclusive (keep)** | Glulisine phase 2, n=35. *"No significant difference in ADAS-Cog13, CDR-SOB, or FAQ scores between treatment groups."* Primary endpoint missed but small/exploratory. Could → `contradicts` under strict bar; `inconclusive` defensible because of small N + the abstract framing as "ability to detect significance was limited." |
| `23507773` | 2013 | **supports (keep, flagged)** | Sex/APOE responder re-analysis of `21911655` (Craft 2011 pilot, n=104). Subgroup-positive in a parent trial that was overall positive. Same-cohort substudy — should be tagged for the UI paper-type filter, not flipped on stance alone. |

## Confirmed (no change)

- `21911655` (Craft 2011 pilot RCT, n=104) — **supports ✓** (delayed memory primary sig at 20 IU; functional ability preserved both doses)
- `17942819` (Reger 2007 pilot, n=24) — **supports ✓** (delayed verbal recall p=0.0374)
- `32568367` (Craft 2020 phase 2/3 multisite, n=289, 12 mo) — **contradicts ✓** (primary endpoint not met in ITT; the pivotal negative trial)
- `28372335` (regular vs detemir pilot, n=36, 4 mo) — **inconclusive ✓** (regular insulin sig memory benefit, detemir null — mixed across formulations)
- `21694461` (vit D2 + insulin combo, n=32) — **inconclusive ✓** (combo intervention, abstract notes ADAS-Cog improvement may be regression to mean)
- `29392460` (2018 SR, 7 studies, n=293) — **supports ✓** (defensible — pooled story recall improved, but only APOE4-negative)
- `30958348` (EV biomarker substudy of Craft 2011) — **inconclusive ✓**
- `35079029` (CSF neuroinflammation biomarker substudy of Craft 2020) — **inconclusive ✓**
- `37379265` (2023 meta, 29 studies, n=1,726) — **supports ✓** (AD/MCI subgroup global cognition SMD=0.22, p<0.00001)
- `41057918` (factorial INI+empagliflozin phase 2A/B, 4 weeks) — **inconclusive ✓** (primary outcome was TRAEs; cognitive secondary)

## Cross-cutting issues

- **Same-cohort substudies**: `23507773`, `30958348` are substudies of
  `21911655` (Craft 2011 pilot). `34101779`, `35079029` are substudies of
  `32568367` (Craft 2020). The Craft 2020 substudies labeled `supports`
  are particularly misleading because the parent trial's primary endpoint
  failed.
- **Population mismatch in the SR/meta layer**: `22162476` pools mostly
  healthy-subject studies. The question is specifically about AD; healthy-subject
  cognitive effects shouldn't drive the stance.
- After flips: 6 supports, 3 contradicts, 8 inconclusive — the "contested"
  consensus label fits much better than the current 9/1/7.

## Highest-confidence flips for this question

- `41436338` inconclusive → contradicts ("evidence does not support routine clinical use")
- `36172480` supports → contradicts (pooled cognitive SMD not significant; mislabel)

Both are unambiguous note-vs-conclusion mismatches; the most recent meta in
the field concludes against use and the 2022 meta finds null pooled effect.


---

## Abstracts (n=17)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 21911655 — current stance: `supports`

**Golden note:** Craft 2011 pilot RCT — intranasal insulin improved cognition/function in MCI/AD.

**Intranasal insulin therapy for Alzheimer disease and amnestic mild cognitive impairment: a pilot clinical trial.**

*Archives of neurology*, 2011. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> OBJECTIVE: To examine the effects of intranasal insulin administration on cognition, function, cerebral glucose metabolism, and cerebrospinal fluid biomarkers in adults with amnestic mild cognitive impairment or Alzheimer disease (AD). DESIGN: Randomized, double-blind, placebo-controlled trial. SETTING: Clinical research unit of a Veterans Affairs medical center. PARTICIPANTS: The intent-to-treat sample consisted of 104 adults with amnestic mild cognitive impairment (n = 64) or mild to moderate AD (n = 40). Intervention  Participants received placebo (n = 30), 20 IU of insulin (n = 36), or 40 IU of insulin (n = 38) for 4 months, administered with a nasal drug delivery device (Kurve Technology, Bothell, Washington). MAIN OUTCOME MEASURES: Primary measures consisted of delayed story recall score and the Dementia Severity Rating Scale score, and secondary measures included the Alzheimer Disease's Assessment Scale-cognitive subscale (ADAS-cog) score and the Alzheimer's Disease Cooperative Study-activities of daily living (ADCS-ADL) scale. A subset of participants underwent lumbar puncture (n = 23) and positron emission tomography with fludeoxyglucose F 18 (n = 40) before and after treatment. RESULTS: Outcome measures were analyzed using repeated-measures analysis of covariance. Treatment with 20 IU of insulin improved delayed memory (P < .05), and both doses of insulin (20 and 40 IU) preserved caregiver-rated functional ability (P < .01). Both insulin doses also preserved general cognition as assessed by the ADAS-cog score for younger participants and functional abilities as assessed by the ADCS-ADL scale for adults with AD (P < .05). Cerebrospinal fluid biomarkers did not change for insulin-treated participants as a group, but, in exploratory analyses, changes in memory and function were associated with changes in the Aβ42 level and in the tau protein-to-Aβ42 ratio in cerebrospinal fluid. Placebo-assigned participants showed decreased fludeoxyglucose F 18 uptake in the parietotemporal, frontal, precuneus, and cuneus regions and insulin-minimized progression. No treatment-related severe adverse events occurred. CONCLUSIONS: These results support longer trials of intranasal insulin therapy for patients with amnestic mild cognitive impairment and patients with AD. Trial Registration  clinicaltrials.gov Identifier: NCT00438568.

---

### PMID 17942819 — current stance: `supports`

**Golden note:** Reger 2007 — intranasal insulin improves cognition + Aβ modulation in early AD.

**Intranasal insulin improves cognition and modulates beta-amyloid in early AD.**

*Neurology*, 2007. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> BACKGROUND: Reduced brain insulin signaling and low CSF-to-plasma insulin ratios have been observed in patients with Alzheimer disease (AD). Furthermore, intracerebroventricular or IV insulin administration improve memory, alter evoked potentials, and modulate neurotransmitters, possibly by augmenting low brain levels. After intranasal administration, insulin-like peptides follow extracellular pathways to the brain within 15 minutes. OBJECTIVE: We tested the hypothesis that daily intranasal insulin treatment would facilitate cognition in patients with early AD or its prodrome, amnestic mild cognitive impairment (MCI). The proportion of verbal information retained after a delay period was the planned primary outcome measure. Secondary outcome measures included attention, caregiver rating of functional status, and plasma levels of insulin, glucose, beta-amyloid, and cortisol. METHODS: Twenty-five participants were randomly assigned to receive either placebo (n = 12) or 20 IU BID intranasal insulin treatment (n = 13) using an electronic atomizer, and 24 participants completed the study. Participants, caregivers, and all clinical evaluators were blinded to treatment assignment. Cognitive measures and blood were obtained at baseline and after 21 days of treatment. RESULTS: Fasting plasma glucose and insulin were unchanged with treatment. The insulin-treated group retained more verbal information after a delay compared with the placebo-assigned group (p = 0.0374). Insulin-treated subjects also showed improved attention (p = 0.0108) and functional status (p = 0.0410). Insulin treatment raised fasting plasma concentrations of the short form of the beta-amyloid peptide (A beta 40; p = 0.0471) without affecting the longer isoform (A beta 42), resulting in an increased A beta 40/42 ratio (p = 0.0207). CONCLUSIONS: The results of this pilot study support further investigation of the benefits of intranasal insulin for patients with Alzheimer disease, and suggest that intranasal peptide administration may be a novel approach to the treatment of neurodegenerative disorders.

---

### PMID 25374101 — current stance: `supports`

**Golden note:** Insulin detemir intranasal — improved cognition in MCI/early AD.

**Long-acting intranasal insulin detemir improves cognition for adults with mild cognitive impairment or early-stage Alzheimer's disease dementia.**

*Journal of Alzheimer's disease : JAD*, 2015. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> Previous trials have shown promising effects of intranasally administered insulin for adults with Alzheimer's disease dementia (AD) or amnestic mild cognitive impairment (MCI). These trials used regular insulin, which has a shorter half-life compared to long-lasting insulin analogues such as insulin detemir. The current trial examined whether intranasal insulin detemir improves cognition or daily functioning for adults with MCI or AD. Sixty adults diagnosed with MCI or mild to moderate AD received placebo (n = 20), 20 IU of insulin detemir (n = 21), or 40 IU of insulin detemir (n = 19) for 21 days, administered with a nasal drug delivery device. Results revealed a treatment effect for the memory composite for the 40 IU group compared with placebo (p < 0.05). This effect was moderated by APOE status (p < 0.05), reflecting improvement for APOE-ε4 carriers (p < 0.02), and worsening for non-carriers (p < 0.02). Higher insulin resistance at baseline predicted greater improvement with the 40 IU dose (r = 0.54, p < 0.02). Significant treatment effects were also apparent for verbal working memory (p < 0.03) and visuospatial working memory (p < 0.04), reflecting improvement for subjects who received the high dose of intranasal insulin detemir. No significant differences were found for daily functioning or executive functioning. In conclusion, daily treatment with 40 IU insulin detemir modulated cognition for adults with AD or MCI, with APOE-related differences in treatment response for the primary memory composite. Future research is needed to examine the mechanistic basis of APOE-related treatment differences, and to further assess the efficacy and safety of intranasal insulin detemir.

---

### PMID 32568367 — current stance: `contradicts`

**Golden note:** Craft 2020 multi-site RCT — primary endpoint NOT met. The pivotal negative trial.

**Safety, Efficacy, and Feasibility of Intranasal Insulin for the Treatment of Mild Cognitive Impairment and Alzheimer Disease Dementia: A Randomized Clinical Trial.**

*JAMA neurology*, 2020. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural

> IMPORTANCE: Insulin modulates aspects of brain function relevant to Alzheimer disease and can be delivered to the brain using intranasal devices. To date, the use of intranasal insulin to treat persons with mild cognitive impairment and Alzheimer's disease dementia remains to be examined in a multi-site trial. OBJECTIVE: To examine the feasibility, safety, and efficacy of intranasal insulin for the treatment of persons with mild cognitive impairment and Alzheimer disease dementia in a phase 2/3 multisite clinical trial. DESIGN, SETTING, AND PARTICIPANTS: A randomized (1:1) double-blind clinical trial was conducted between 2014 and 2018. Participants received 40 IU of insulin or placebo for 12 months during the blinded phase, which was followed by a 6-month open-label extension phase. The clinical trial was conducted at 27 sites of the Alzheimer's Therapeutic Research Institute. A total of 432 adults were screened, and 144 adults were excluded. Inclusion criteria included adults aged 55 to 85 years with a diagnosis of amnestic mild cognitive impairment or Alzheimer disease (based on National Institute on Aging-Alzheimer Association criteria), a score of 20 or higher on the Mini-Mental State Examination, a clinical dementia rating of 0.5 or 1.0, and a delayed logical memory score within a specified range. A total of 289 participants were randomized. Among the first 49 participants, the first device (device 1) used to administer intranasal insulin treatment had inconsistent reliability. A new device (device 2) was used for the remaining 240 participants, who were designated the primary intention-to-treat population. Data were analyzed from August 2018 to March 2019. INTERVENTIONS: Participants received 40 IU of insulin (Humulin-RU-100; Lilly) or placebo (diluent) daily for 12 months (blinded phase) followed by a 6-month open-label extension phase. Insulin was administered with 2 intranasal delivery devices. MAIN OUTCOMES AND MEASURES: The primary outcome (mean score change on the Alzheimer Disease Assessment Scale-cognitive subscale 12) was evaluated at 3-month intervals. Secondary clinical outcomes were assessed at 6-month intervals. Cerebrospinal fluid collection and magnetic resonance imaging scans occurred at baseline and 12 months. RESULTS: A total of 289 participants (155 men [54.6%]; mean [SD] age, 70.9 [7.1] years) were randomized. Of those, 260 participants completed the blinded phase, and 240 participants completed the open-label extension phase. For the first 49 participants, the first device used to administer treatment had inconsistent reliability. A second device was used for the remaining 240 participants (123 men [51.3%]; mean [SD] age, 70.8 [7.1] years), who were designated the primary intention-to-treat population. No differences were observed between treatment arms for the primary outcome (mean score change on ADAS-cog-12 from baseline to month 12) in the device 2 ITT cohort (0.0258 points; 95% CI, -1.771 to 1.822 points; P = .98) or for the other clinical or cerebrospinal fluid outcomes in the primary (second device) intention-to-treat analysis. No clinically important adverse events were associated with treatment. CONCLUSIONS AND RELEVANCE: In this study, no cognitive or functional benefits were observed with intranasal insulin treatment over a 12-month period among the primary intention-to-treat cohort. TRIAL REGISTRATION: ClinicalTrials.gov Identifier: NCT01767909.

---

### PMID 28372335 — current stance: `inconclusive`

**Golden note:** Pilot trial regular vs detemir — mixed effects across formulations.

**Effects of Regular and Long-Acting Insulin on Cognition and Alzheimer's Disease Biomarkers: A Pilot Clinical Trial.**

*Journal of Alzheimer's disease : JAD*, 2017. Types: Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, Non-P.H.S.; Research Support, Non-U.S. Gov't

> BACKGROUND: Long acting insulin detemir administered intranasally for three weeks enhanced memory for adults with Alzheimer's disease dementia (AD) or amnestic mild cognitive impairment (MCI). The investigation of longer-term administration is necessary to determine whether benefits persist, whether they are similar to benefits provided by regular insulin, and whether either form of insulin therapy affects AD biomarkers. OBJECTIVE: The present study aimed to determine whether four months of treatment with intranasal insulin detemir or regular insulin improves cognition, daily functioning, and AD biomarkers for adults with MCI or AD. METHODS: This randomized, double-blind, placebo-controlled trial included an intent-to-treat sample consisting of 36 adults diagnosed with MCI or mild to moderate AD. Participants received placebo (n = 12), 40 IU of insulin detemir (n = 12), or 40 IU of regular insulin (n = 12) daily for four months, administered with a nasal delivery device. A cognitive battery was administered at baseline and after two and four months of treatment. MRI was administered for all participants and lumbar puncture for a subset (n = 20) at baseline and four months. The primary outcome was change from baseline to four months on a memory composite (sum of Z scores for delayed list and story recall). Secondary outcomes included: global cognition (Alzheimer's Disease Assessment Scale-Cognition), daily functioning (Dementia Severity Rating Scale), MRI volume changes in AD-related regions of interest, and cerebrospinal fluid AD markers. RESULTS: The regular insulin treated group had better memory after two and four months compared with placebo (p < 0.03). No significant effects were observed for the detemir-assigned group compared with the placebo group, or for daily functioning for either group. Regular insulin treatment was associated with preserved volume on MRI. Regular insulin treatment was also associated with reduction in the tau-P181/Aβ42 ratio. CONCLUSION: Future research is warranted to examine the mechanistic basis of treatment differences, and to further assess the efficacy and safety of intranasal insulin.

---

### PMID 23507773 — current stance: `supports`

**Golden note:** Sex/APOE responder analysis — specific subgroups benefited.

**Sex and ApoE genotype differences in treatment response to two doses of intranasal insulin in adults with mild cognitive impairment or Alzheimer's disease.**

*Journal of Alzheimer's disease : JAD*, 2013. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't; Research Support, U.S. Gov't, Non-P.H.S.

> A previous clinical trial demonstrated that four months of treatment with intranasal insulin improves cognition and function for patients with Alzheimer's disease (AD) or mild cognitive impairment (MCI), but prior studies suggest that response to insulin treatment may differ by sex and ApoE ε4 carriage. Thus, responder analyses using repeated measures analysis of covariance were completed on the trial's 104 participants with MCI or AD who received either placebo or 20 or 40 IU of insulin for 4 months, administered by a nasal delivery device. Results indicate that men and women with memory impairment responded differently to intranasal insulin treatment. On delayed story memory, men and women showed cognitive improvement when taking 20 IU of intranasal insulin, but only men showed cognitive improvement for the 40 IU dose. The sex difference was most apparent for ApoE ε4 negative individuals. For the 40 IU dose, ApoE ε4 negative men improved while ApoE ε4 negative women worsened. Their ApoE ε4 positive counterparts remained cognitively stable. This sex effect was not detected in functional measures. However, functional abilities were relatively preserved for women on either dose of intranasal insulin compared with men. Unlike previous studies with young adults, neither men nor women taking intranasal insulin exhibited a significant change in weight over 4 months of treatment.

---

### PMID 22162476 — current stance: `supports`

**Golden note:** Systematic review — intranasal insulin improves cognition.

**Effect of intranasal insulin on cognitive function: a systematic review.**

*The Journal of clinical endocrinology and metabolism*, 2011. Types: Evaluation Study; Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> AIM: Epidemiological and mechanistic studies raised the possibility that cognitive function may be affected by brain responses to insulin. We systematically reviewed and analyzed existing clinical trials that assessed the potential beneficial effects of intranasal insulin administration on cognitive functions. METHODS: Interventional studies measuring changes in cognitive functions in response to intranasal insulin were retrieved and included if they were in English and assessed cognitive functions before and after treatment. Cohen's effect size was calculated to allow comparison between studies. RESULTS: Eight studies (328 participants) were analyzed. No significant side effects of intranasal insulin administration were reported. Seven studies included healthy subjects' response to intranasal insulin, and three evaluated the cognitive effect among patients with minimal cognitive impairment or overt Alzheimer's disease. In healthy people, Cohen's effect size calculations suggest that only 160 IU/d intranasal insulin induced potential beneficial effects. Although females, when compared head-to-head, exhibited greater improvements in cognitive tests than men, the composite analysis of all included studies did not support this trend. Among cognitively impaired patients, only lower doses of insulin were assessed, and 20 IU revealed potential beneficial effects on cognitive functions. This was significant in a single study assessing long-term intranasal insulin administration, whereas acute administration of 20 IU intranasal insulin tended to show a beneficial effect on immediate recall in Apo ε4(-), but not Apo ε4(+), patients. CONCLUSIONS: The current limited clinical experience suggests potential beneficial cognitive effects of intranasal insulin. Analyses provide clinical considerations for future research aimed at elucidating whether intranasal insulin may be used to improve cognitive functions.

---

### PMID 21694461 — current stance: `inconclusive`

**Golden note:** Vit D2 + intranasal insulin RCT in AD — combo intervention, small.

**A randomized controlled trial of high-dose vitamin D2 followed by intranasal insulin in Alzheimer's disease.**

*Journal of Alzheimer's disease : JAD*, 2011. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Poor vitamin D nutrition is linked with dementia, but vitamin D has not been tested in a randomized controlled trial (RCT) in Alzheimer's disease (AD). Nasal insulin acutely improves cognition and vitamin D upregulates insulin receptor expression and enhances insulin action. In an RCT we examined the effect of high-dose vitamin D followed by nasal insulin on memory and disability in mild-moderate AD. 63 community-dwelling individuals aged > 60 were recruited; 32 with mild-moderate disease (Folstein Mini-Mental State Examination [MMSE] score 12-24) met entry criteria and were randomized. All took low-dose vitamin D (1000 IU/day) throughout. After run-in (8 weeks), they were randomized to additional high-dose D/placebo for 8 weeks, followed immediately by randomization to nasal insulin (60 IU qid)/placebo for 48 h. Primary outcome measures were Alzheimer's disease assessment scale-cognitive subscale (ADAS-cog) and Disability Assessment in Dementia (after high-dose D) and ADAS-cog and Wechsler Memory Scale-Revised Logical memory (WMS-R LM) for immediate and delayed recall (after nasal insulin). Baseline median (interquartile range, IR) age, MMSE, and ADAS-cog were 77.5 (69-80), 19.5 (17-22), and 25.5 (20-31), respectively. Median 25OHD increased from 49 to 60 nM (p < 0.01) after run-in and was 187 nM after high-dose vitamin D and 72 nM after placebo (p < 0.001). Neither cognition nor disability changed significantly after high-dose D. ADAS-cog improved by a median (IR) of 9 (1-11) with nasal insulin after placebo high-dose vitamin D (p = 0.02), but may represent regression to the mean as WLS-R LM did not change. We conclude that high-dose vitamin D provides no benefit for cognition or disability over low-dose vitamin D in mild-moderate AD.

---

### PMID 29392460 — current stance: `supports`

**Golden note:** Systematic review intranasal insulin AD/MCI — beneficial.

**Intranasal insulin in Alzheimer's dementia or mild cognitive impairment: a systematic review.**

*Journal of neurology*, 2018. Types: Journal Article; Systematic Review

> BACKGROUND AND AIMS: Due to common pathophysiological findings of Alzheimer's disease (AD) with diabetes mellitus (DM), insulin has been suggested as a possible treatment of AD or mild cognitive impairment (MCI). A safe alternative of IV insulin is intranasal (IN) insulin. The aim of this systematic review is to investigate the effects of IN insulin on cognitive function of patients with either AD or MCI. METHODS: A literature search of the electronic databases Medline, Scopus and CENTRAL was performed to identify RCTs investigating the effect of IN insulin administration on cognitive tasks, in patients with AD or MCI. RESULTS: Seven studies (293 patients) met our inclusion criteria. Most studies showed that verbal memory and especially story recall was improved after IN insulin administration. Sometimes the effect was restricted for apoe4 (-) patients. Intranasal insulin did not affect other cognitive functions. However, there were some positive results in functional status and daily activity. Data suggested that different insulin types and doses may have different effects on different apoe4 groups. In addition, the effects of treatment on Αβ levels differed from study to study. Finally, IN insulin resulted in minor adverse effects. CONCLUSIONS: Intranasal insulin improved story recall performance of apoe4 (-) patients with AD or MCI. Other cognitive functions were not affected, but there were some positive results in functional status and daily activity. Since IN insulin is a safe intervention, future studies should be conducted with larger doses and after proper selection of patients and insulin types.

---

### PMID 34101779 — current stance: `supports`

**Golden note:** Intranasal insulin reduces WMH progression with cognitive improvement.

**Intranasal Insulin Reduces White Matter Hyperintensity Progression in Association with Improvements in Cognition and CSF Biomarker Profiles in Mild Cognitive Impairment and Alzheimer's Disease.**

*The journal of prevention of Alzheimer's disease*, 2021. Types: Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial

> BACKGROUND: Intranasally administered insulin has shown promise in both rodent and human studies in Alzheimer's disease; however, both effects and mechanisms require elucidation. OBJECTIVE: We assessed the effects of intranasally administered insulin on white matter health and its association with cognition and cerebral spinal fluid biomarker profiles in adults with mild cognitive impairment or Alzheimer's disease in secondary analyses from a prior phase 2 clinical trial (NCT01767909). DESIGN: A randomized (1:1) double-blind clinical trial. SETTING: Twelve sites across the United States. PARTICIPANTS: Adults with mild cognitive impairment or Alzheimer's disease. INTERVENTION: Participants received either twice daily placebo or insulin (20 IU Humulin R U-100 b.i.d.) intranasally for 12 months. Seventy-eight participants were screened, of whom 49 (32 men) were enrolled. MEASUREMENTS: Changes from baseline in global and regional white matter hyperintensity volume and gray matter volume were analyzed and related to changes in cerebral spinal fluid biomarkers, Alzheimer's Disease Assessment Scale-Cognition, Clinical Disease Rating-Sum of Boxes, Alzheimer's Disease Cooperative Study-Activities of Daily Living Scale, and a memory composite. RESULTS: The insulin-treated group demonstrated significantly reduced changes in white matter hyperintensity volume in deep and frontal regions after 12 months, with a similar trend for global volume. White matter hyperintensity volume progression correlated with worsened Alzheimer's disease cerebral spinal fluid biomarker profile and cognitive function; however, patterns of correlations differed by treatment group. CONCLUSION: Intranasal insulin treatment for 12 months reduced white matter hyperintensity volume progression and supports insulin's potential as a therapeutic option for Alzheimer's disease.

---

### PMID 30958348 — current stance: `inconclusive`

**Golden note:** EV biomarkers track cognitive change post-intranasal insulin — exploratory.

**Extracellular Vesicle Biomarkers Track Cognitive Changes Following Intranasal Insulin in Alzheimer's Disease.**

*Journal of Alzheimer's disease : JAD*, 2019. Types: Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, N.I.H., Intramural

> BACKGROUND: Insulin resistance is implicated in Alzheimer's disease (AD), whereas intranasal insulin is an experimental treatment in clinical trials. We previously proposed insulin signaling mediators in plasma neuronal-enriched extracellular vesicles (EVs) as biomarkers of brain insulin resistance. OBJECTIVE: We sought to demonstrate the capacity of neuronal-enriched EV biomarkers to demonstrate target engagement in response to intranasal insulin and their ability to track treatment-associated cognitive changes in AD. METHODS: We isolated neuronal-enriched EVs from plasma samples of participants with amnestic mild cognitive impairment or probable AD involved in a 4-month duration placebo-controlled clinical trial of 20 or 40 IU intranasal insulin. We measured insulin signaling mediators as biomarkers and examined treatment-associated changes and their relationship with cognitive performance (ADAS-Cog). RESULTS: There were no EV biomarker changes from baseline in any of the treatment groups. In participants treated with 20 IU insulin, EV biomarkers of insulin resistance (pS312-IRS-1, pY-IRS-1) showed strong positive correlations with ADAS-Cog changes, especially in ApoE ɛ4 non-carriers. CONCLUSION: Neuronal EV biomarkers of insulin resistance (pS312-IRS-1, pY-IRS-1) were associated with cognitive changes in response to low dose intranasal insulin suggesting engagement of the insulin cascade in neurons of origin.

---

### PMID 35079029 — current stance: `inconclusive`

**Golden note:** Intranasal insulin modulates CSF neuroinflammation — biomarker, not cognitive primary.

**Intranasal insulin modulates cerebrospinal fluid markers of neuroinflammation in mild cognitive impairment and Alzheimer's disease: a randomized trial.**

*Scientific reports*, 2022. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> Intranasal insulin (INI) has shown promise as a treatment for Alzheimer's disease (AD) in pilot clinical trials. In a recent phase 2 trial, participants with mild cognitive impairment (MCI) or AD who were treated with INI with one of two delivery devices showed improved cerebral spinal fluid (CSF) biomarker profiles and slower symptom progression compared with placebo. In the cohort which showed benefit, we measured changes in CSF markers of inflammation, immune function and vascular integrity and assessed their relationship with changes in cognition, brain volume, and CSF amyloid and tau concentrations. The insulin-treated group had increased CSF interferon-γ (p = 0.032) and eotaxin (p = 0.049), and reduced interleukin-6 (p = 0.048) over the 12 month trial compared to placebo. Trends were observed for increased CSF macrophage-derived chemokine for the placebo group (p = 0.083), and increased interleukin-2 in the insulin-treated group (p = 0.093). Insulin-treated and placebo groups showed strikingly different patterns of associations between changes in CSF immune/inflammatory/vascular markers and changes in cognition, brain volume, and amyloid and tau concentrations. In summary, INI treatment altered the typical progression of markers of inflammation and immune function seen in AD, suggesting that INI may promote a compensatory immune response associated with therapeutic benefit.

---

### PMID 33719017 — current stance: `inconclusive`

**Golden note:** Glulisine phase 2 — small, exploratory.

**A Phase II, Single-Center, Randomized, Double-Blind, Placebo-Controlled Study of the Safety and Therapeutic Efficacy of Intranasal Glulisine in Amnestic Mild Cognitive Impairment and Probable Mild Alzheimer's Disease.**

*Drugs & aging*, 2021. Types: Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Intranasal insulin is a potential treatment for neurodegenerative disease shown to increase cerebral glucose uptake, reduce amyloid plaques, and improve verbal memory in cognitively impaired as well as healthy adults. Investigations have suggested rapid-acting insulins such as glulisine may result in superior cognitive benefits compared with regular insulin. OBJECTIVE: The aim of this study was to evaluate the safety and efficacy of rapid-acting intranasal glulisine in subjects with amnestic mild cognitive impairment (MCI) or mild probable Alzheimer's disease (AD). METHODS: We performed a single-center, randomized, double-blind, placebo-controlled study to evaluate the efficacy of intranasal glulisine 20 IU twice daily versus saline placebo in 35 memory-impaired (MCI/AD) subjects using the Impel NeuroPharma I109 Precision Olfactory Delivery (POD®) device. The 13-item Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-Cog13), Clinical Dementia Rating (CDR) global score, and Functional Assessment Questionnaire (FAQ) were measured at baseline and 3 and 6 months. Secondary outcome measures included digit span forward/backwards, Trail Making Test Parts A/B, Controlled Oral Word Association Test (COWAT), and Weschler Memory Scale (WMS)-IV logical memory. Adverse effects (AEs) and serious adverse effects (SAEs) were measured along with blood glucose/insulin levels. RESULTS: No significant difference in ADAS-Cog13, CDR Sum of Boxes (CDR-SOB), or FAQ scores were found between treatment groups at 3 and 6 months. Subjects in the saline group were significantly older than those in the glulisine group (p = 0.022). No significant differences in sex, education, apolipoprotein E4 (ApoE4) status, and Montreal Cognitive Assessment (MoCA) score existed between treatment groups. Overall, the number of adverse events per person was similar between groups (2.32 vs. 2.24; p = 0.824), although subjects receiving intranasal glulisine had higher rates of nasal irritation (25.0% vs. 13.9%) and respiratory symptoms (15.9% vs. 8.3%) compared with placebo. There were no differences in blood sugar or rate of hypoglycemia between the treatment and placebo groups. CONCLUSIONS: Intranasal glulisine was relatively safe and well-tolerated and did not consistently impact peripheral glucose or insulin levels. There were no enhancing effects of intranasal glulisine on cognition, function, or mood, but the ability to detect significance was limited by the number of subjects successfully enrolled and the study duration. CLINICALTRIALS. GOV REGISTRATION: NCT02503501.

---

### PMID 36172480 — current stance: `supports`

**Golden note:** Meta-analysis intranasal insulin MCI/dementia — improves cognition.

**Efficacy of intranasal insulin in improving cognition in mild cognitive impairment or dementia: a systematic review and meta-analysis.**

*Frontiers in aging neuroscience*, 2022. Types: Systematic Review; Journal Article

> BACKGROUND: Insulin regulates many aspects of brain function related to mild cognitive impairment (MCI) or dementia, which can be delivered to the brain center via intranasal (IN) devices. Some small, single-site studies indicated that intranasal insulin can enhance memory in patients with MCI or dementia. The pathophysiology of Alzheimer's disease (AD) and diabetes mellitus (DM) overlap, making insulin an attractive therapy for people suffering from MCI or dementia. OBJECTIVE: The goal of the study is to evaluate the effectiveness of IN insulin on cognition in patients with MCI or dementia. METHODS: We searched the electronic database for randomized controlled trials (RCTs) that verified the effects of insulin on patients with MCI or dementia.16 studies (899 patients) were identified. RESULTS: The pooled standard mean difference (SMD) showed no significant difference between IN insulin and placebo groups; however, statistical results suggested a difference between study groups in the effects of ADCS-ADL; AD patients with APOE4 (-) also showed improved performance in verbal memory; other cognitions did not improve significantly. CONCLUSION: In view of IN insulin's promising potential, more researches should be conducted at a larger dose after proper selection of insulin types and patients. SYSTEMATIC REVIEW REGISTRATION: http://www.crd.york.ac.uk/PROSPERO/, identifier CRD42022353546.

---

### PMID 37379265 — current stance: `supports`

**Golden note:** Systematic review/meta intranasal insulin in humans — overall positive.

**Outcomes and clinical implications of intranasal insulin on cognition in humans: A systematic review and meta-analysis.**

*PloS one*, 2023. Types: Meta-Analysis; Systematic Review; Journal Article

> BACKGROUND: Aberrant brain insulin signaling has been posited to lie at the crossroads of several metabolic and cognitive disorders. Intranasal insulin (INI) is a non-invasive approach that allows investigation and modulation of insulin signaling in the brain while limiting peripheral side effects. OBJECTIVES: The objective of this systematic review and meta-analysis is to evaluate the effects of INI on cognition in diverse patient populations and healthy individuals. METHODS: MEDLINE, EMBASE, PsycINFO, and Cochrane CENTRAL were systematically searched from 2000 to July 2021. Eligible studies were randomized controlled trials that studied the effects of INI on cognition. Two independent reviewers determined study eligibility and extracted relevant descriptive and outcome data. RESULTS: Twenty-nine studies (pooled N = 1,726) in healthy individuals as well as those with Alzheimer's disease (AD)/mild cognitive impairment (MCI), mental health disorders, metabolic disorders, among others, were included in the quantitative meta-analysis. Patients with AD/MCI treated with INI were more likely to show an improvement in global cognition (SMD = 0.22, 95% CI: 0.05-0.38 p = <0.00001, N = 12 studies). Among studies with healthy individuals and other patient populations, no significant effects of INI were found for global cognition. CONCLUSIONS: This review demonstrates that INI may be associated with pro-cognitive benefits for global cognition, specifically for individuals with AD/MCI. Further studies are required to better understand the neurobiological mechanisms and differences in etiology to dissect the intrinsic and extrinsic factors contributing to the treatment response of INI.

---

### PMID 41057918 — current stance: `inconclusive`

**Golden note:** Phase 2A/B intranasal insulin + empagliflozin factorial — mixed.

**A phase 2A/B randomized trial of metabolic modulators intranasal insulin and empagliflozin for MCI and early AD.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2025. Types: Journal Article; Randomized Controlled Trial; Clinical Trial, Phase II

> INTRODUCTION: Agents targeting metabolic/vascular disorders are promising candidates to treat Alzheimer's disease (AD) and enhance safety and efficacy of other therapies. METHODS: In a 2×2 factorial double-blinded randomized trial, participants with mild cognitive impairment (MCI), early AD, or who were amyloid positive received intranasal insulin (INI; 40 IU q.i.d.), the sodium-glucose cotransporter-2 inhibitor empagliflozin (10 mg q.d. oral tablet), both, or placebo for 4 weeks. The primary outcome was treatment-related adverse events (TRAEs). Secondary outcomes included the modified Preclinical Alzheimer's Cognitive Composite-5 (mPACC5), fluid biomarkers, cerebral blood flow (CBF), and fractional anisotropy (FA). RESULTS: TRAEs were mild and similar for all groups. INI increased mPACC5, modulated FA and CBF, and reduced plasma glial fibrillary acidic protein. Empagliflozin lowered cerebrospinal fluid tau and modulated CBF. Both agents moderated immune/inflammatory/neurovascular markers. DISCUSSION: INI and empagliflozin treatment was safe with promising effects on cognition, fluid, and imaging biomarkers. A longer and larger trial is needed to confirm these results. CLINICAL TRIAL REGISTRATION: NCT05081219 HIGHLIGHTS: Agents targeting metabolic or vascular disorders are promising candidates to prevent or treat Alzheimer's disease (AD). Intranasal insulin and empagliflozin were safe alone or in combination for mild cognitive impairment/AD. Insulin improved cognition and markers of inflammation and immune function. Empagliflozin reduced markers of vascular injury and neurodegeneration. A longer, larger trial is needed to validate these results.

---

### PMID 41436338 — current stance: `inconclusive`

**Golden note:** 2025 meta of RCTs — net mixed, includes Craft 2020 negative.

**Intranasal insulin for mild cognitive impairment and Alzheimer's disease: A systematic review and meta-analysis of randomized controlled trials.**

*Revue neurologique*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis; Review

> BACKGROUND: Central insulin resistance has been implicated in the pathophysiology of Alzheimer's disease (AD), supporting the hypothesis that, in some individuals, AD may represent "type 3 diabetes." Intranasal insulin has been proposed as a non-invasive approach to enhance brain insulin signaling while minimizing peripheral metabolic effects, but clinical evidence remains inconsistent. METHODS: We conducted a systematic review and meta-analysis of randomized controlled trials (RCTs) comparing intranasal insulin with placebo in patients with mild cognitive impairment (MCI) or mild-to-moderate AD. Primary outcomes included changes in cognitive performance (ADAS-Cog13, CDR-SB, DSRS, delayed recall) and functional ability (ADCS-ADL). Secondary outcomes included cerebrospinal fluid (CSF) biomarkers (Aβ42, total tau, phosphorylated tau) and safety endpoints. Literature searches were performed in PubMed, Embase, and Cochrane Central up to April 2025. Random-effects models were used to pool effect estimates, and risk of bias was assessed using the Cochrane RoB 2 tool. RESULTS: Five RCTs enrolling 540 participants met the inclusion criteria. Pooled analyses showed no significant differences between intranasal insulin and placebo for ADAS-Cog13 (mean difference: -1.09 [95% CI: -4.89; 2.71]), ADCS-ADL (mean difference 0.06 [-0.33; 0.45]), CDR-SB, DSRS, or delayed recall. No significant effects were observed on CSF Aβ42, total tau, or p-tau181. Gastrointestinal adverse events were more frequent with insulin (risk ratio: 1.57; [95% CI: 1.15; 2.14]), whereas cardiovascular events were less frequent (risk ratio: 0.30 [0.12; 0.79]). No differences were found for other safety outcomes, and discontinuation rates were comparable between groups. CONCLUSION: Intranasal insulin was generally well tolerated but did not produce meaningful improvements in cognitive, functional, or biomarker outcomes in patients with MCI or mild-to-moderate AD. Current evidence does not support its routine clinical use, and further trials with standardized dosing, longer follow-up, and biomarker-stratified designs are warranted to clarify its therapeutic potential.

---

