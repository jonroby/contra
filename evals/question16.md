# Q16: Does aerobic exercise affect MMSE or ADAS-Cog scores in Alzheimer's disease?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=12 PMIDs.

**Current S/C/I**: 7 / 1 / 4
**Proposed S/C/I**: 7 / 1 / 4 (composition shifts)
**Net flips**: 4 (mostly direction-preserving reclassifications)

The exercise corpus is mostly accurate, but two `inconclusive` labels
miss meta-analyses with statistically significant pooled effects, and
two `supports` labels are based on uncontrolled or sub-significant
studies. The pivotal contradicting trial (Yu cycling RCT) is correctly
labeled.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `36497772` | 2022 | **inconclusive → supports** | Aerobic exercise + AD meta of 15 RCTs. Verbatim: *"There was a significant effect of aerobic exercise on increasing mini-mental state examination (MMSE) score in AD patients [WMD, 1.50 (95% CI, 0.55 to 2.45), p = 0.002]."* The note ("findings conflicting") describes the *background* of the field, not the *result* of the meta. Pooled effect is statistically significant. |
| `39800395` | 2025 | **inconclusive → supports** | 2025 aerobic + AD meta. Verbatim: *"For the Minimum Mental State Examination (MMSE) (SMD=0.95, 95% CI 0.58 to 1.32, Z=5.06, p<0.00001), Alzheimer's Disease Assessment Scale-Cognitive Section (ADAS-cog) (SMD=-0.67, 95% CI -1.15 to -0.2, Z=2.77, p=0.006)... Aerobic exercise was conducive to the improvement of cognitive function."* Both MMSE and ADAS-Cog were significantly improved. The note ("findings not entirely consistent") again references the *background*. Pooled positive. |
| `28157102` | 2017 | **supports → inconclusive** | 3-month aerobic in mild AD, **n=10, uncontrolled (open-label)**. Reports brain ketone metabolism changes (3-fold higher CMRacac) but cognitive primary not met (Stroop only trend p=0.06). Per strict bar, n=10 uncontrolled biomarker study → `inconclusive`. |
| `41790706` | 2026 | **supports → inconclusive** | Aerobic + mind-body in MCI meta. Verbatim: *"Structured aerobic exercise showed **non-significant effects on MMSE** (MD = 0.37, P = .21) and MoCA (MD = -0.49, P = .26), with modest improvement on ADAS-Cog (MD = -1.41, P = .002)."* Aerobic alone was non-significant on 2 of 3 cognitive scales; only mind-body showed consistent effects. The headline of this paper actually argues mind-body > aerobic. For the question (aerobic exercise effect on MMSE/ADAS-Cog), this paper is mixed. |

## Confirmed (no change)

- `15249848` (MoVIES, n=1146 prospective) — **supports ✓** (high exercise OR 0.39 protective, sig)
- `33523004` (Yu aerobic cycling RCT n=96, 6 mo) — **contradicts ✓** (primary not met; ADAS-Cog non-sig at 6 and 12 mo; "possibly due to lack of power")
- `27760869` (aerobic + vascular CI RCT n=70) — **supports ✓** (defensible — sig ADAS-Cog -1.71 at intervention end, though not maintained at 6-mo follow-up)
- `34601135` (2021 exercise meta in AD) — **supports ✓** (aerobic MMSE MD 2.31 sig)
- `32505710` (FIT-AD inter-individual differences methodology) — **inconclusive ✓**
- `36281092` (meta aerobic + AD) — **supports ✓** (MD 2.95 sig)
- `38669527` (urinary AD7c-NTP biomarker n=40) — **inconclusive ✓**
- `40454205` (umbrella exercise + cog dysfunction) — **supports ✓** (aerobic MD 2.95 for AD)

## Borderline (not flipped, but flagged for cross-question policy decisions)

- **`33523004`** (Yu cycling RCT) — explicitly cites *"lack of power"*
  as the reason for the null primary; primary endpoint missed is the
  CLAUDE.md-defined trigger for `contradicts`, so stance kept. Fits
  `underpowered_null` caveat — the trial was self-described as a
  "pilot" and authors attribute the null to power, not to absence of
  effect. No cross-question policy change required (CLAUDE.md is
  explicit on this).
- **`41790706`** — population mismatch (MCI not AD) and combo
  intervention (aerobic + mind-body), where aerobic-alone is non-sig
  on 2 of 3 cognitive scales. Flipped S→I above; flagging here
  because the headline of the paper itself argues mind-body > aerobic.

## Cross-cutting issues

- After flips: 7/1/4 (composition shifts I→S and S→I, count unchanged).
  The "contested" expected consensus is partly justified by the
  pivotal RCT being null while pooled metas are positive — same
  pattern as Q13 statins.

## Highest-confidence flips for this question

- `36497772` and `39800395` inconclusive → supports — both meta-analyses
  report significantly positive pooled MMSE/ADAS-Cog effects. The
  current `inconclusive` labels reflect the *background* framing of
  the abstracts, not the *results*.
- `28157102` supports → inconclusive — n=10 uncontrolled biomarker
  study, cognitive primary not met (Stroop only trend p=0.06).
- `41790706` supports → inconclusive — aerobic-alone is non-sig on
  MMSE and MoCA in this combo (mind-body + aerobic) MCI meta.

## signal_types (annotation layer)

Optional pattern tags per pmid. Untagged = strong/canonical; tagged = some caveat.

- `33523004` — `underpowered_null`, `pilot_positive` (authors call this a pilot RCT and attribute null primary to "lack of power"; secondary slowing-of-decline framing)
- `27760869` — `non_durable_effect` (sig ADAS-Cog -1.71 at intervention end, not maintained at 6-mo follow-up; population is SIVCI not AD per se — wrong_population caveat too)
- `34601135` — `split_outcome` (multi-domain meta; MMSE significance reached only for aerobic subgroup, not other modalities)
- `40454205` — `broad_scope_review`, `class_positive_drug_null` (umbrella over MCI/dementia/AD/PD/stroke; aerobic+AD pooled MD 2.95 sig; Class IV evidence per authors due to small samples)
- `28157102` — `biomarker_only`, `uncontrolled_observational`, `case_series_underpowered` (n=10, open-label, cognition primary trend only; flipped S→I)
- `41790706` — `combo_intervention`, `wrong_population`, `split_outcome` (MCI not AD; aerobic-alone non-sig on MMSE/MoCA; flipped S→I)
- `38669527` — `biomarker_only`, `combo_intervention` (urinary AD7c-NTP primary, with K-MMSE secondary; aerobic vs combined RAG arms, active control)
- `32505710` — `methodology_only` (inter-individual variance secondary analysis of FIT-AD; no group-difference efficacy claim)
- `39800395` — `hedged_meta` (abstract hedges "findings not entirely consistent" and notes high heterogeneity, but pooled effect significant; flipped I→S)
- `36497772` — `hedged_meta` (abstract opens "findings conflicting" referring to background literature, but pooled MMSE effect significant; flipped I→S)
- All other pmids (`15249848`, `36281092`) — untagged

### Proposed new tags (Q16)

- `non_durable_effect` — significant effect at intervention end that does not persist at follow-up (i.e., effect dissipates after intervention stops). Distinct from `short_duration` (which is about trial length) and from missed-primary patterns.

---

## Abstracts (n=12)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 15249848 — current stance: `supports`

**Evidence span:** > In a multiple regression model, high exercise level at the baseline assessment was negatively associated with, ie, was protective against, being in the group with the greatest amount of decline at the follow-up assessment, after adjusting for likely confounders (odds ratio = 0.39; 95% confidence interval, 0.19, 0.78).

**Golden note:** MoVIES — exercise protective against cognitive decline (MMSE outcome).

**Exercise level and cognitive decline: the MoVIES project.**

*Alzheimer disease and associated disorders*, 2004. Types: Comparative Study; Journal Article; Research Support, U.S. Gov't, P.H.S.

> Growing evidence suggests that physical exercise may be protective against cognitive impairment and decline. A prospective study of a representative rural community sample (N = 1,146) aged 65+ years examined self-reported exercise habits and measured global cognitive function using the Mini-Mental State Examination (MMSE). A composite variable "exercise level" combining type, frequency, and duration of exercise was created with three levels: "high exercise" (aerobic exercise of > or = 30 minute duration > or = 3 times a week), "low exercise" (all other exercise groups), and "no exercise." Cognitive decline was defined as being in the 90 percentile of decline in this cohort, ie, declining by 3 or more MMSE points during the 2-year interval between two assessments. In a multiple regression model, high exercise level at the baseline assessment was negatively associated with, ie, was protective against, being in the group with the greatest amount of decline at the follow-up assessment, after adjusting for likely confounders (odds ratio = 0.39; 95% confidence interval, 0.19, 0.78). When high exercise was redefined using frequency as > or = 5 days per week as the threshold, as per the Surgeon General's guidelines, both low exercise and high exercise were negatively associated with cognitive decline. Exercise may have implications for prevention of cognitive decline.

---

### PMID 33523004 — current stance: `contradicts`

**Evidence span:** > ADAS-Cog did not differ between groups at 6 (p = 0.386) and 12 months (p = 0.856). Aerobic exercise did not show superior cognitive effects to stretching in our pilot trial, possibly due to the lack of power.

**Golden note:** Yu aerobic cycling RCT in AD (n=96) — primary cognitive endpoint not met.

**Cognitive Effects of Aerobic Exercise in Alzheimer's Disease: A Pilot Randomized Controlled Trial.**

*Journal of Alzheimer's disease : JAD*, 2021. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> BACKGROUND: Aerobic exercise has shown inconsistent cognitive effects in older adults with Alzheimer's disease (AD) dementia. OBJECTIVE: To examine the immediate and longitudinal effects of 6-month cycling on cognition in older adults with AD dementia. METHODS: This randomized controlled trial randomized 96 participants (64 to cycling and 32 to stretching for six months) and followed them for another six months. The intervention was supervised, moderate-intensity cycling for 20-50 minutes, 3 times a week for six months. The control was light-intensity stretching. Cognition was assessed at baseline, 3, 6, 9, and 12 months using the AD Assessment Scale-Cognition (ADAS-Cog). Discrete cognitive domains were measured using the AD Uniform Data Set battery. RESULTS: The participants were 77.4±6.8 years old with 15.6±2.9 years of education, and 55% were male. The 6-month change in ADAS-Cog was 1.0±4.6 (cycling) and 0.1±4.1 (stretching), which were both significantly less than the natural 3.2±6.3-point increase observed naturally with disease progression. The 12-month change was 2.4±5.2 (cycling) and 2.2±5.7 (control). ADAS-Cog did not differ between groups at 6 (p = 0.386) and 12 months (p = 0.856). There were no differences in the 12-month rate of change in ADAS-Cog (0.192 versus 0.197, p = 0.967), memory (-0.012 versus -0.019, p = 0.373), executive function (-0.020 versus -0.012, p = 0.383), attention (-0.035 versus -0.033, p = 0.908), or language (-0.028 versus -0.026, p = 0.756). CONCLUSION: Exercise may reduce decline in global cognition in older adults with mild-to-moderate AD dementia. Aerobic exercise did not show superior cognitive effects to stretching in our pilot trial, possibly due to the lack of power.

---

### PMID 27760869 — current stance: `supports`

**Evidence span:** > At the end of the intervention, the aerobic exercise training group had significantly improved ADAS-Cog performance compared with the usual care plus education group (-1.71 point difference, 95% confidence interval [CI] -3.15 to -0.26, p = 0.02).

**Golden note:** Aerobic exercise + vascular CI RCT — improved everyday function.

**Aerobic exercise and vascular cognitive impairment: A randomized controlled trial.**

*Neurology*, 2016. Types: Journal Article; Randomized Controlled Trial

> OBJECTIVE: To assess the efficacy of a progressive aerobic exercise training program on cognitive and everyday function among adults with mild subcortical ischemic vascular cognitive impairment (SIVCI). METHODS: This was a proof-of-concept single-blind randomized controlled trial comparing a 6-month, thrice-weekly, progressive aerobic exercise training program (AT) with usual care plus education on cognitive and everyday function with a follow-up assessment 6 months after the formal cessation of aerobic exercise training. Primary outcomes assessed were general cognitive function (Alzheimer's Disease Assessment Scale-Cognitive subscale [ADAS-Cog]), executive functions (Executive Interview [EXIT-25]), and activities of daily living (Alzheimer's Disease Cooperative Study-Activities of Daily Living [ADCS-ADL]). RESULTS: Seventy adults randomized to aerobic exercise training or usual care were included in intention-to-treat analyses (mean age 74 years, 51% female, n = 35 per group). At the end of the intervention, the aerobic exercise training group had significantly improved ADAS-Cog performance compared with the usual care plus education group (-1.71 point difference, 95% confidence interval [CI] -3.15 to -0.26, p = 0.02); however, this difference was not significant at the 6-month follow-up (-0.63 point difference, 95% CI -2.34 to 1.07, p = 0.46). There were no significant between-group differences at intervention completion and at the 6-month follow-up in EXIT-25 or ADCS-ADL performance. Examination of secondary measures showed between-group differences at intervention completion favoring the AT group in 6-minute walk distance (30.35 meter difference, 95% CI 5.82 to 54.86, p = 0.02) and in diastolic blood pressure (-6.89 mm Hg difference, 95% CI -12.52 to -1.26, p = 0.02). CONCLUSIONS: This study provides preliminary evidence for the efficacy of 6 months of thrice-weekly progressive aerobic training in community-dwelling adults with mild SIVCI, relative to usual care plus education. CLINICALTRIALSGOV IDENTIFIER: NCT01027858. CLASSIFICATION OF EVIDENCE: This study provides Class II evidence that for adults with mild SIVCI, an aerobic exercise program for 6 months results in a small, significant improvement in ADAS-Cog performance.

---

### PMID 34601135 — current stance: `supports`

**Evidence span:** > Benefits were also found in the MMSE test, albeit significance was only reached for aerobic exercise (n = 187, MD=2.31 points, 95% CI 0.45-4.27).

**Golden note:** Exercise meta in AD — multi-domain benefit.

**Exercise interventions in Alzheimer's disease: A systematic review and meta-analysis of randomized controlled trials.**

*Ageing research reviews*, 2021. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> AIMS: To assess the potential multi-domain benefits of exercise interventions on patients with Alzheimer's disease (AD), as well as to determine the specific effects of different exercise modalities (aerobic, strength, or combined training). METHODS: A systematic search was conducted in PubMed and Web of Science until March 2021 for randomized controlled trials assessing the effect of exercise interventions (compared with no exercise) on patients with AD. Outcomes included cognitive function (mini-mental state examination [MMSE] test), physical function (e.g., 6-minute walking test [6MWT]), functional independence (Barthel index), and neuropsychiatric symptoms (Neuropsychiatric Inventory [NPI]). A random-effects meta-analysis was conducted. RESULTS: 28 studies (total n = 1337 participants, average age 79-90 years) were included in the systematic review, of which 21 could be meta-analyzed. Although considerable heterogeneity was found, exercise interventions induced several significant benefits, including in Barthel index (n = 147 patients, mean difference [MD]=8.36 points, 95% confidence interval [CI]=0.63-16.09), 6MWT (n = 369, MD=84 m, 95% CI=44-133)), and NPI (n = 263, MD=-4.4 points, 95% CI=-8.42 to -0.38). Benefits were also found in the MMSE test, albeit significance was only reached for aerobic exercise (n = 187, MD=2.31 points, 95% CI 0.45-4.27). CONCLUSIONS: Exercise interventions appear to exert multi-domain benefits in patients with AD.

---

### PMID 36497772 — current stance: `inconclusive`

**Evidence span:** > There was a significant effect of aerobic exercise on increasing mini-mental state examination (MMSE) score in AD patients [weighted mean difference (WMD), 1.50 (95% CI, 0.55 to 2.45), p = 0.002].

**Golden note:** Aerobic exercise + AD cognition meta — findings conflicting.

**The Effect of Aerobic Exercise on Cognitive Function in People with Alzheimer's Disease: A Systematic Review and Meta-Analysis of Randomized Controlled Trials.**

*International journal of environmental research and public health*, 2022. Types: Meta-Analysis; Systematic Review; Journal Article; Research Support, Non-U.S. Gov't

> A growing body of research has examined the effect of aerobic exercise on cognitive function in people with Alzheimer's Disease (AD), but the findings of the available studies were conflicting. The aim of this study was to explore the effect of aerobic exercise on cognitive function in AD patients. Searches were performed in PubMed, Web of Science, and EBSCO databases from the inception of indexing until 12 November 2021. Cochrane risk assessment tool was used to evaluate the methodological quality of the included literature. From 1942 search records initially identified, 15 randomized controlled trials (RCTs) were considered eligible for systematic review and meta-analysis. Included studies involved 503 participants in 16 exercise groups (mean age: 69.2-84 years) and 406 participants (mean age: 68.9-84 years) in 15 control groups. There was a significant effect of aerobic exercise on increasing mini-mental state examination (MMSE) score in AD patients [weighted mean difference (WMD), 1.50 (95% CI, 0.55 to 2.45), p = 0.002]. Subgroup analyses showed that interventions conducted 30 min per session [WMD, 2.52 (95% CI, 0.84 to 4.20), p = 0.003], less than 150 min per week [WMD, 2.10 (95% CI, 0.84 to 3.37), p = 0.001], and up to three times per week [WMD, 1.68 (95% CI, 0.46 to 2.89), p = 0.007] increased MMSE score significantly. In addition, a worse basal cognitive status was associated with greater improvement in MMSE score. Our analysis indicated that aerobic exercise, especially conducted 30 min per session, less than 150 min per week, and up to three times per week, contributed to improving cognitive function in AD patients. Additionally, a worse basal cognitive status contributed to more significant improvements in cognitive function.

---

### PMID 28157102 — current stance: `supports`

**Evidence span:** > In this uncontrolled study, ten patients with mild AD participated in a 3-month, individualized, moderate-intensity aerobic training on a treadmill (Walking). There was a tendency toward improvement in the Stroop-color naming test (-10% completion time, p = 0.06).

**Golden note:** 3-month aerobic training mild AD — improved brain energy metabolism.

**A 3-Month Aerobic Training Program Improves Brain Energy Metabolism in Mild Alzheimer's Disease: Preliminary Results from a Neuroimaging Study.**

*Journal of Alzheimer's disease : JAD*, 2017. Types: Clinical Trial; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: Aerobic training has some benefits for delaying the onset or progression of Alzheimer's disease (AD). Little is known about the implication of the brain's two main fuels, glucose and ketones (acetoacetate), associated with thesebenefits. OBJECTIVE: To determine whether aerobic exercise training modifies brain energy metabolism in mild AD. METHODS: In this uncontrolled study, ten patients with mild AD participated in a 3-month, individualized, moderate-intensity aerobic training on a treadmill (Walking). Quantitative measurement of brain uptake of glucose (CMRglu) and acetoacetate (CMRacac) using neuroimaging and cognitive testing were done before and after the Walking program. RESULTS: Four men and six women with an average global cognitive score (MMSE) of 26/30 and an average age of 73 y completed the Walking program. Average total distance and treadmill speed were 8 km/week and 4 km/h, respectively. Compared to the Baseline, after Walking, CMRacac was three-fold higher (0.6±0.4 versus 0.2±0.1 μmol/100 g/min; p = 0.01). Plasma acetoacetate concentration and the blood-to-brain acetoacetate influx rate constant were also increased by 2-3-fold (all p≤0.03). CMRglu was unchanged after Walking (28.0±0.1 μmol/100 g/min; p = 0.96). There was a tendency toward improvement in the Stroop-color naming test (-10% completion time, p = 0.06). Performance on the Trail Making A&B tests was also directly related to plasma acetoacetate and CMRacac (all p≤0.01). CONCLUSION: In mild AD, aerobic training improved brain energy metabolism by increasing ketone uptake and utilization while maintaining brain glucose uptake, and could potentially be associated with some cognitive improvement.

---

### PMID 32505710 — current stance: `inconclusive`

**Evidence span:** > There are true inter-individual differences in aerobic fitness and cognitive responses to aerobic exercise in older adults with mild-to-moderate dementia due to AD. These inter-individual differences likely underline the inconsistent cognitive benefits in human studies.

**Golden note:** FIT-AD inter-individual differences — explains inconsistency.

**Inter-individual differences in the responses to aerobic exercise in Alzheimer's disease: Findings from the FIT-AD trial.**

*Journal of sport and health science*, 2020. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural

> BACKGROUND: Despite the strong evidence of aerobic exercise as a disease-modifying treatment for Alzheimer's disease (AD) in animal models, its effects on cognition are inconsistent in human studies. A major contributor to these findings is inter-individual differences in the responses to aerobic exercise, which was well documented in the general population but not in those with AD. The purpose of this study was to examine inter-individual differences in aerobic fitness and cognitive responses to a 6-month aerobic exercise intervention in community-dwelling older adults with mild-to-moderate dementia due to AD. METHODS: This study was a secondary analysis of the Effects of Aerobic Exercise for Treating Alzheimer's Disease (FIT-AD) trial data. Aerobic fitness was measured by the shuttle walk test (SWT), the 6-min walk test (6MWT), and the maximal oxygen consumption (VO2max) test, and cognition by the AD Assessment Scale-Cognition (ADAS-Cog). Inter-individual differences were calculated as the differences in the standard deviation of 6-month change (SDR) in the SWT, 6MWT, VO2max, and ADAS-Cog between the intervention and control groups. RESULTS: Seventy-eight participants were included in this study (77.4 ± 6.3 years old, mean ± SD; 15.7 ± 2.8 years of education; 41% were female). VO2max was available for 26 participants (77.7 ± 7.1 years old; 14.8 ± 2.6 years of education; 35% were female). The SDR was 37.0, 121.1, 1.7, and 2.3 for SWT, 6MWT, VO2max, and ADAS-Cog, respectively. CONCLUSION: There are true inter-individual differences in aerobic fitness and cognitive responses to aerobic exercise in older adults with mild-to-moderate dementia due to AD. These inter-individual differences likely underline the inconsistent cognitive benefits in human studies.

---

### PMID 36281092 — current stance: `supports`

**Evidence span:** > Meta analysis of all articles: I2 = 91%, P ≤ .00001, (MD = 2.95, 95%CI [2.49, 3.40], P ≤ .00001).

**Golden note:** Meta aerobic exercise + AD — improves cognition.

**Meta analysis of aerobic exercise improving intelligence and cognitive function in patients with Alzheimer's disease.**

*Medicine*, 2022. Types: Meta-Analysis; Journal Article

> OBJECTIVE: Alzheimer's disease (AD) is a neurodegenerative disease. This study aims to explore the intervention and treatment effects of aerobic exercise and different exercise modes on AD through meta-analysis. METHODS: Using the set inclusion and exclusion criteria, retrieve the China national knowledge infrastructure (CNKI), Wanfang Data Knowledge Service Platform, China Science and Technology Journal Database, Cochrane Library, and PubMed were searched from January 1, 2012, to December 31, 2021. Cochrane risk bias assessment tool was used to evaluate the quality of the included articles, and ReMan5.4.1 was used for forest plot analysis of mini-mental state exam (MMSE) score indicators included in the included articles. RESULTS: Twelve randomized controlled trials and 795 samples were included. Meta analysis of all articles: I2 = 91%, P ≤ .00001, (MD = 2.95, 95%CI [2.49, 3.40], P ≤ .00001). Meta analysis of 5 fit aerobics groups: I2 = 4%, P = .38, (MD = 1.53, 95%CI [0.72, 2.33], P = .0002); meta-analysis of three spinning groups: I2 = 3%, P = .36, (MD = 1.79, 95%CI [0.29, 3.29], P = .02). CONCLUSION: Aerobic exercise can effectively improve intellectual and cognitive impairment in AD patients, and for different forms of aerobic exercise, the therapeutic effect of spinning aerobic exercise is better than that of fit aerobics.

---

### PMID 39800395 — current stance: `inconclusive`

**Evidence span:** > For the Minimum Mental State Examination (MMSE) (SMD=0.95, 95% CI 0.58 to 1.32, Z=5.06, p<0.00001), Alzheimer's Disease Assessment Scale-Cognitive Section (ADAS-cog) (SMD=-0.67, 95% CI -1.15 to -0.2, Z=2.77, p=0.006).

**Golden note:** Aerobic exercise + AD meta — findings not entirely consistent.

**Effects of aerobic exercise on cognitive function and quality of life in patients with Alzheimer's disease: a systematic review and meta-analysis.**

*BMJ open*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> OBJECTIVES: Numerous studies have examined the effects of physical activity on cognitive performance and executive function in people with Alzheimer's disease (AD), although the findings are not entirely consistent. There are also insufficient study reviews for specific workout and assessment tool types. Therefore, the purpose of this study was to systematically investigate the effects of aerobic exercise on the quality of life, cognitive performance and depressive symptoms in people with AD. DESIGN: Risk of bias was assessed using the Cochrane risk of bias tool, systematic reviews and meta-analyses using random-effects modelling, and certainty of evidence using the Grading of Recommendations Assessment, Development and Evaluation tool. DATA SOURCES: PubMed, Web of Science, Cochrane Library, EMBASE, Scopus, CINAHL and CNKI through 12 March 2024. ELIGIBILITY CRITERIA: The analysis includes all randomised controlled trials (RCTs) that used aerobic exercise as an intervention for individuals with AD. DATA EXTRACTION AND SYNTHESIS: Two writers selected and searched for data using defined techniques. To investigate possible sources of heterogeneity between studies, meta-regression was carried out using Stata MP V.18.0 and V.14.0 software, standardised mean differences (SMDs) and 95% CIs were computed, and data were reviewed using Review Manager V.5.4 software, which was made available by the Cochrane Collaboration. Sensitivity analyses were employed to ascertain the stability and reliability of the results, and funnel plots and Egger's test were employed to check for publication bias. Correction and assessment of publication bias was done using Duval and Tweedie clipping methods. RESULTS: Aerobic exercise enhanced cognitive function. For the Minimum Mental State Examination (MMSE) (SMD=0.95, 95% CI 0.58 to 1.32, Z=5.06, p<0.00001), Alzheimer's Disease Assessment Scale-Cognitive Section (ADAS-cog) (SMD=-0.67, 95% CI -1.15 to -0.2, Z=2.77, p=0.006) and quality of life (SMD=0.36, 95% CI 0.08 to 0.64, Z=2.51, p=0.01), but not statistically significant for depressive symptoms (SMD=-0.25, 95% CI -0.63 to 0.13, Z=1.27, p=0.21). Subgroup analysis showed that duration greater than 16 weeks and less than 50 min per intervention improved MMSE Scores. Duration greater than 16 weeks and more than 30 min per intervention improved ADAS-cog Scores in patients with AD. Aerobic exercise greater than 16 weeks, with more than three interventions per week and 30-50 min per intervention improves quality of life in patients with AD. CONCLUSION: The study revealed that aerobic exercise was conducive to the improvement of cognitive function and quality of life among patients with AD, yet it did not exert a significant impact on the amelioration of depressive symptoms. Nevertheless, given the high level of heterogeneity and the variations in the quality of the included studies, the conclusions require further verification through more scientifically objective RCTs. PROSPERO REGISTRATION NUMBER: CRD42024526067.

---

### PMID 38669527 — current stance: `inconclusive`

**Evidence span:** > This is the first study to investigate urine biomarker through exercise intervention. In future stuides, participants who have low cognitive function and low activity levels need to be recruited to observe more significant 'Exercise' effect.

**Golden note:** Exercise + urinary AD7c-NTP biomarker — biomarker-focused.

**Effects of Exercise on Urinary AD7c-NTP (Alzheimer-Associated Neuronal Thread Protein) Levels and Cognitive Function Among Active Korean Elderly: A Randomized Controlled Trial.**

*Journal of Alzheimer's disease : JAD*, 2024. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Alzheimer-associated neuronal thread protein (AD7c-NTP) has been demonstrated to have high diagnostic accuracy in differentiating Alzheimer's disease (AD) patients from healthy individuals. However, it is yet unclear whether exercise can lower the level of AD7c-NTP in urine among active Korean elderly. OBJECTIVE: To assess the effect of exercise on AD7c-ntp levels in urine and cognitive function among active Korean elderly. METHODS: In total, 40 Korean elderly (≥65 years) were divided into Active Control group (CG, n = 10), Aerobic exercise group (AG, n = 18), and combined Resistance/Aerobic exercise group (RAG, n = 12). A total of 12 weeks of exercise intervention was implemented. At week 0 and 12, cognitive performance (Korean Mini-Mental State Examination, Korean-Color Word Stroop test), grip strength, and body composition (muscle mass and body fat percentage) were measured. Also, a morning urine sample was obtained from each subject. The level of AD7c-NTP was measured using competitive enzyme-linked immunosorbent assay (ELISA). RESULTS: After 12 weeks of exercise intervention, there was a significant difference of AD7c-NTP levels between RAG and CG (p = 0.026), AG and CG (p = 0.032), respectively. Furthermore, the AD7c-NTP levels in urine showed negative correlation with K-MMSE scores (r = -0.390, p = 0.013) and grip strength (r = -0.376, p = 0.017), among all participants after exercise intervention. CONCLUSIONS: This is the first study to investigate urine biomarker through exercise intervention. In future stuides, participants who have low cognitive function and low activity levels need to be recruited to observe more significant 'Exercise' effect.

---

### PMID 40454205 — current stance: `supports`

**Evidence span:** > Aerobic exercise (MD 2.95) was more effective for AD, while mind-body exercises (MD 1.68) benefitted PD patients.

**Golden note:** Umbrella review exercise in cognitive dysfunction — beneficial.

**Effects of exercise interventions on cognitive function in patients with cognitive dysfunction: an umbrella review of meta-analyses.**

*Frontiers in aging neuroscience*, 2025. Types: Journal Article; Systematic Review

> OBJECTIVE: This umbrella review assessed the quality, potential biases, and effects of exercise interventions on cognitive function in individuals with cognitive impairments. METHODS: A comprehensive umbrella review of meta-analyses of randomized controlled trials (RCTs) was performed to evaluate the effects of exercise on cognitive function in individuals with cognitive impairments. Databases including Web of Science, PubMed, Embase, and the Cochrane Database of Systematic Reviews were searched. Outcomes were evaluated using the Grading of Recommendations, Assessment, Development and Evaluation (GRADE) system, classified as "high," "moderate," "low," or "very low" quality. RESULTS: A total of 55 meta-analyses were included, covering dementia, cognitive impairment, MCI, Alzheimer's disease (AD), Parkinson's disease (PD), and stroke. Cognitive outcomes were assessed using scales like MMSE and MoCA. High-quality evidence supports Exergaming (SMD 0.69), Tai Chi (SMD 0.36), and traditional Chinese mind-body exercises (SMD 0.32) for improving MMSE and MoCA Score in MCI patients. For dementia, moderate-quality evidence shows resistance training (SMD 0.60) and Tai Chi (SMD 0.27) have positive effects. Aerobic exercise (MD 2.95) was more effective for AD, while mind-body exercises (MD 1.68) benefitted PD patients. Multi-component exercises (SMD 0.67) improved MMSE and MoCA scores in post-stroke cognitive impairment. For unspecified cognitive impairments, combining exercise with cognitive training and traditional Chinese exercises showed higher effectiveness. Due to small sample sizes, all findings were Class IV evidence, requiring further research. CONCLUSION: Moderate to high-quality evidence supports Exergaming, Tai Chi, and traditional Chinese exercises in improving cognitive function in MCI. For dementia, resistance training and Tai Chi are effective; for AD, aerobic exercise; for PD, mind-body exercises; and for post-stroke cognitive impairment, multi-component exercises are beneficial. SYSTEMATIC REVIEW REGISTRATION: https://www.crd.york.ac.uk/PROSPERO/view/CRD42024587635, identifier [CRD42024587635].

---

### PMID 41790706 — current stance: `supports`

**Evidence span:** > Structured aerobic exercise showed non-significant effects on MMSE (MD = 0.37, P = .21) and MoCA (MD = -0.49, P = .26), with modest improvement on ADAS-Cog (MD = -1.41, P = .002).

**Golden note:** Aerobic + mind-body in MCI meta — exercise improves cognition.

**The effects of structured aerobic exercise and mind-body exercise on cognitive function in older adults with MCI: Systematic review and meta-analysis.**

*Medicine*, 2026. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Global aging has increased the prevalence of dementia, with mild cognitive impairment (MCI) representing a critical window for intervention. While exercise is recognized for mitigating cognitive decline, the comparative effectiveness of mind-body versus structured aerobic exercise remains unclear. METHODS: Search sources included PubMed, Web of Science, and the Cochrane Library. Randomized controlled trials (RCTs) assessing mind-body exercise (tai chi, yoga, and dance) or structured aerobic exercise (walking and cycling) in patients with MCI aged over 50 years were included. The Mini-Mental State Examination (MMSE), Montreal Cognitive Assessment (MoCA), and Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-Cog) were used as outcome measures. Random- or fixed-effects meta-analyses were conducted using RevMan 5.4.1. Heterogeneity was assessed using the I2 statistic. Subgroup analyses examined intervention parameters. RESULTS: Twenty-six randomized controlled trials (n = 2,555) were included. Mind-body exercise significantly improved MMSE (mean difference [MD] = 1.27, 95% confidence interval [CI]: 0.99-1.55, P < .01), MoCA (MD = 1.89, 95% CI: 0.78-3.00, P = .0008), and ADAS-Cog (MD = -2.09, 95% CI: -2.94 to -1.25, P < .00001) versus controls. Structured aerobic exercise showed non-significant effects on MMSE (MD = 0.37, P = .21) and MoCA (MD = -0.49, P = .26), with modest improvement on ADAS-Cog (MD = -1.41, P = .002). Optimal mind-body parameters include ≥20 weeks' duration, ≥60 minutes per session, and ≥3 times per week. CONCLUSIONS: Mind-body exercise demonstrates superior cognitive benefits compared with structured aerobic exercise in older adults with MCI. It is advised to prioritize mind-body exercise interventions at least 3 times per week, for 60 minutes per session, for at least 20 weeks. Limitations include heterogeneity and geographic bias; these findings warrant confirmation through multicenter trials.

---

