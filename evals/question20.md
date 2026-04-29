# Q20: Does ginkgo biloba prevent dementia in cognitively healthy older adults?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=12 PMIDs.

**Current S/C/I**: 4 / 3 / 5
**Proposed S/C/I**: 0 / 4 / 8
**Net flips**: 4

`expected_consensus: "settled negative"` — and indeed the two pivotal
RCTs (GEM and GuidAge, both >2,800 participants) show null primary
endpoints. The current `supports` labels (4 of 12) are mainly
short-duration studies in healthy adults or comparative-pharmacology
studies — i.e., not addressing the prevention question. After
applying the strict bar, **no `supports` labels remain** and the
"settled negative" consensus is much more clearly visible.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `24871648` | 2014 | **supports → contradicts** | Natural medicines + ginkgo meta. Verbatim: *"The meta-analysis for assessing the **prevention effect** of Ginkgo against AD suggested that risk ratio (RR) is **1.06 (95% CI: 0.92 to 1.22)** between Gingko and the placebo, with no significant heterogeneity across studies."* Pooled prevention RR is null. The note's "efficacy claim" applies only to ginkgo for *existing* AD treatment, not for prevention. The conclusion verbatim: *"Ginkgo may help established AD patients with cognitive symptoms but **cannot prevent** the neurodegenerative progression of the disease."* For the question (prevention), this is `contradicts`. |
| `11466162` | 2001 | **supports → inconclusive** | 30-day ginkgo administration in **healthy young/middle-aged adults**, n=61. Reports neuropsychological improvements. **Population mismatch** — the question asks about cognitively healthy *older* adults at risk for dementia, and the duration is 30 days, far too short to address dementia prevention. Off-target study. |
| `9803773` | 1998 | **supports → inconclusive** | Ginkgo vs tacrine **CEEG/QEEG pharmacology comparison**, n=18 (mostly already with dementia, mean age 67). Pharmacodynamic/EEG study, not a prevention RCT. Doesn't address the question. |
| `15117063` | 2003 | **supports → inconclusive** | Ginkgo in healthy elderly, n=66, **4 weeks**. Endpoint is subjective emotional well-being (POMS, SDS, VAS-QoL), not cognition or dementia incidence. 4 weeks is far too short to address prevention. Off-target study. |

## Confirmed (no change)

- `19017911` (GEM trial, n=3069, 6.1-yr median follow-up) — **contradicts ✓** (HR 1.12 NS for dementia, HR 1.16 NS for AD; pivotal negative)
- `22959217` (GuidAge RCT, n=2854, 5y) — **contradicts ✓** (HR 0.84, p=0.306; primary endpoint missed)
- `26058281` (Ginkgo for prevention meta in non-demented) — **contradicts ✓** (*"no convincing evidence... can prevent the development of dementia"*)
- `29255909` (OTC supplements review — ginkgo low-strength evidence, did not reduce risk) — **inconclusive ✓** (could → `contradicts` but defensible)
- `12663701` (EPIDOS women 75+ retrospective) — **inconclusive ✓** (sig protective for combined C4A treatments OR 0.31; ginkgo alone OR 0.38 NS)
- `18690838` (GuidAge baseline/design paper) — **inconclusive ✓**
- `10641953` (herbal medications elderly review) — **inconclusive ✓** (narrative; refers to delaying dementia *progression*, not prevention)
- `18165850` (GEM vs GuidAge design comparison methodology) — **inconclusive ✓**

## Cross-cutting issues

- **Population/duration mismatches dominate the `supports` labels**:
  3 of 4 current `supports` (`11466162`, `9803773`, `15117063`) are
  studies in healthy young or short-duration (4-30 day) ginkgo
  administration. None of them address dementia *prevention* in
  cognitively healthy *older adults*. After flips, only short-term
  emotional/cognitive papers remain, correctly demoted to `inconclusive`.
- **The two pivotal RCTs alone settle this question negatively**:
  GEM (n=3,069, 6 years) and GuidAge (n=2,854, 5 years) are both
  large, well-powered, and explicitly null on dementia/AD incidence
  primary endpoints.
- **`expected_consensus: "settled negative"`** is well-supported by
  the pivotal RCT evidence, but the current 4/3/5 mix obscures this.
  After flips: 0/4/8 — the negative consensus is much more visible.

## Highest-confidence flips for this question

- `24871648` supports → contradicts — the meta's prevention RR is
  explicitly **null** (1.06, CI 0.92-1.22). The current `supports`
  conflates ginkgo's modest treatment effect on existing AD with its
  null prevention effect.
- `11466162`, `9803773`, `15117063` supports → inconclusive — all
  three are off-target studies (healthy young adults, 4-30 day
  duration, pharmacology endpoints) that don't address the
  prevention question.

## Borderline (defensible, no flip)

- `29255909` (OTC supplements review) — verbatim states ginkgo evidence
  was "insufficient or low-strength, suggesting that these supplements
  did not reduce risk for cognitive decline." This is a hedged_meta
  null and a defensible `contradicts`, but the review's overall
  conclusion is "evidence is insufficient" rather than a definitive
  null, so `inconclusive` is also defensible. No flip.
- `12663701` (EPIDOS) — ginkgo-alone OR 0.38 (CI 0.08-1.76, p=0.22) is
  non-significant; the protective signal lives in the combined C4A
  treatment class (OR 0.31, p=0.018). Underpowered for ginkgo-alone
  effect; could lean `contradicts` under a strict bar but the authors
  hedge ("requires further examination"). No flip.

## signal_types (annotation layer)

Tag vocabulary applied below uses the standing core/established tags
from earlier passes; no new tags proposed for Q20.

| PMID | Signal types |
|------|--------------|
| `19017911` | (clean primary RCT null — no tag) |
| `22959217` | (clean primary RCT null — no tag) |
| `29255909` | `hedged_meta`, `broad_scope_review` |
| `11466162` | `wrong_population`, `short_duration` |
| `12663701` | `class_positive_drug_null`, `underpowered_null`, `observational_only` |
| `9803773` | `mechanism_only`, `biomarker_only`, `uncontrolled_observational`, `wrong_population` |
| `18690838` | `methodology_only` |
| `24871648` | `split_outcome` (treatment-positive, prevention-null in same meta) |
| `10641953` | `narrative_review`, `wrong_population` (treatment-target, not prevention) |
| `26058281` | (clean prevention meta null — no tag) |
| `15117063` | `wrong_population`, `short_duration`, `non_cognitive_primary` (subjective mood/QoL endpoint) |
| `18165850` | `methodology_only` |

**Tag distribution (Q20, n=12; 8 pmids tagged):**
- `wrong_population`: 4 (`11466162`, `9803773`, `10641953`, `15117063`)
- `short_duration`: 2 (`11466162`, `15117063`)
- `methodology_only`: 2 (`18690838`, `18165850`)
- `hedged_meta`: 1
- `broad_scope_review`: 1
- `class_positive_drug_null`: 1
- `underpowered_null`: 1
- `observational_only`: 1
- `mechanism_only`: 1
- `biomarker_only`: 1
- `uncontrolled_observational`: 1
- `split_outcome`: 1
- `narrative_review`: 1
- `non_cognitive_primary`: 1

**Policy categories observed:**
- (b) preclinical/mech-dominated review labeled supports — partial:
  `9803773` (QPEEG pharmacology study labeled supports) and `24871648`
  (treatment-positive review labeled supports despite null prevention
  pooled estimate) both fit the spirit of (b).
- (a) subgroup_positive in parent_null — no clean instance.
- (c) missed_primary_sig_secondary — no instance.

---

## Abstracts (n=12)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 19017911 — current stance: `contradicts`

**Stance justification:** > In this study, G. biloba at 120 mg twice a day was not effective in reducing either the overall incidence rate of dementia or AD incidence in elderly individuals with normal cognition or those with MCI.

**Golden note:** GEM trial — ginkgo did NOT reduce dementia incidence. Pivotal negative.

**Ginkgo biloba for prevention of dementia: a randomized controlled trial.**

*JAMA*, 2008. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> CONTEXT: Ginkgo biloba is widely used for its potential effects on memory and cognition. To date, adequately powered clinical trials testing the effect of G. biloba on dementia incidence are lacking. OBJECTIVE: To determine effectiveness of G. biloba vs placebo in reducing the incidence of all-cause dementia and Alzheimer disease (AD) in elderly individuals with normal cognition and those with mild cognitive impairment (MCI). DESIGN, SETTING, AND PARTICIPANTS: Randomized, double-blind, placebo-controlled clinical trial conducted in 5 academic medical centers in the United States between 2000 and 2008 with a median follow-up of 6.1 years. Three thousand sixty-nine community volunteers aged 75 years or older with normal cognition (n = 2587) or MCI (n = 482) at study entry were assessed every 6 months for incident dementia. INTERVENTION: Twice-daily dose of 120-mg extract of G. biloba (n = 1545) or placebo (n = 1524). MAIN OUTCOME MEASURES: Incident dementia and AD determined by expert panel consensus. RESULTS: Five hundred twenty-three individuals developed dementia (246 receiving placebo and 277 receiving G. biloba) with 92% of the dementia cases classified as possible or probable AD, or AD with evidence of vascular disease of the brain. Rates of dropout and loss to follow-up were low (6.3%), and the adverse effect profiles were similar for both groups. The overall dementia rate was 3.3 per 100 person-years in participants assigned to G. biloba and 2.9 per 100 person-years in the placebo group. The hazard ratio (HR) for G. biloba compared with placebo for all-cause dementia was 1.12 (95% confidence interval [CI], 0.94-1.33; P = .21) and for AD, 1.16 (95% CI, 0.97-1.39; P = .11). G. biloba also had no effect on the rate of progression to dementia in participants with MCI (HR, 1.13; 95% CI, 0.85-1.50; P = .39). CONCLUSIONS: In this study, G. biloba at 120 mg twice a day was not effective in reducing either the overall incidence rate of dementia or AD incidence in elderly individuals with normal cognition or those with MCI. Trial Registration clinicaltrials.gov Identifier: NCT00010803.

---

### PMID 22959217 — current stance: `contradicts`

**Stance justification:** > Long-term use of standardised ginkgo biloba extract in this trial did not reduce the risk of progression to Alzheimer's disease compared with placebo.

**Golden note:** GuidAge RCT — ginkgo did NOT prevent AD in elderly with memory complaints. Pivotal negative.

**Long-term use of standardised Ginkgo biloba extract for the prevention of Alzheimer's disease (GuidAge): a randomised placebo-controlled trial.**

*The Lancet. Neurology*, 2012. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't; Review

> BACKGROUND: Prevention strategies are urgently needed to tackle the growing burden of Alzheimer's disease. We aimed to assess efficacy of long-term use of standardised ginkgo biloba extract for the reduction of incidence of Alzheimer's disease in elderly adults with memory complaints. METHODS: In the randomised, parallel-group, double-blind, placebo-controlled GuidAge clinical trial, we enrolled adults aged 70 years or older who spontaneously reported memory complaints to their primary-care physician in France. We randomly allocated participants in a 1:1 ratio according to a computer-generated sequence to a twice per day dose of 120 mg standardised ginkgo biloba extract (EGb761) or matched placebo. Participants and study investigators and personnel were masked to study group assignment. Participants were followed-up for 5 years by primary-care physicians and in expert memory centres. The primary outcome was conversion to probable Alzheimer's disease in participants who received at least one dose of study drug or placebo, compared by use of the log-rank test. This study is registered with ClinicalTrials.gov, number NCT00276510. FINDINGS: Between March, 2002, and November, 2004, we enrolled and randomly allocated 2854 participants, of whom 1406 received at least one dose of ginkgo biloba extract and 1414 received at least one dose of placebo. By 5 years, 61 participants in the ginkgo group had been diagnosed with probable Alzheimer's disease (1·2 cases per 100 person-years) compared with 73 participants in the placebo group (1·4 cases per 100 person-years; hazard ratio [HR] 0·84, 95% CI 0·60-1·18; p=0·306), but the risk was not proportional over time. Incidence of adverse events was much the same between groups. 76 participants in the ginkgo group died compared with 82 participants in the placebo group (0·94, 0·69-1·28; p=0·68). 65 participants in the ginkgo group had a stroke compared with 60 participants in the placebo group (risk ratio 1·12, 95% CI 0·77-1·63; p=0·57). Incidence of other haemorrhagic or cardiovascular events also did not differ between groups. INTERPRETATION: Long-term use of standardised ginkgo biloba extract in this trial did not reduce the risk of progression to Alzheimer's disease compared with placebo. FUNDING: Ipsen.

---

### PMID 29255909 — current stance: `inconclusive`

**Stance justification:** > Evidence about effects of ω-3 fatty acids, soy, ginkgo biloba, folic acid alone or with other B vitamins, β-carotene, vitamin C, vitamin D plus calcium, and multivitamins or multi-ingredient supplements was either insufficient or low-strength, suggesting that these supplements did not reduce risk for cognitive decline.

**Golden note:** OTC supplements review — ginkgo insufficient evidence.

**Over-the-Counter Supplement Interventions to Prevent Cognitive Decline, Mild Cognitive Impairment, and Clinical Alzheimer-Type Dementia: A Systematic Review.**

*Annals of internal medicine*, 2017. Types: Journal Article; Research Support, U.S. Gov't, P.H.S.; Systematic Review; Video-Audio Media

> BACKGROUND: Optimal interventions to prevent or delay cognitive decline, mild cognitive impairment (MCI), or dementia are uncertain. PURPOSE: To summarize the evidence on efficacy and harms of over-the-counter (OTC) supplements to prevent or delay cognitive decline, MCI, or clinical Alzheimer-type dementia in adults with normal cognition or MCI but no dementia diagnosis. DATA SOURCES: Multiple electronic databases from 2009 to July 2017 and bibliographies of systematic reviews. STUDY SELECTION: English-language trials of at least 6 months' duration that enrolled adults without dementia and compared cognitive outcomes with an OTC supplement versus placebo or active controls. DATA EXTRACTION: Extraction performed by a single reviewer and confirmed by a second reviewer; dual-reviewer assessment of risk of bias; consensus determination of strength of evidence. DATA SYNTHESIS: Thirty-eight trials with low to medium risk of bias compared ω-3 fatty acids, soy, ginkgo biloba, B vitamins, vitamin D plus calcium, vitamin C or β-carotene, multi-ingredient supplements, or other OTC interventions with placebo or other supplements. Few studies examined effects on clinical Alzheimer-type dementia or MCI, and those that did suggested no benefit. Daily folic acid plus vitamin B12 was associated with improvements in performance on some objectively measured memory tests that were statistically significant but of questionable clinical significance. Moderate-strength evidence showed that vitamin E had no benefit on cognition. Evidence about effects of ω-3 fatty acids, soy, ginkgo biloba, folic acid alone or with other B vitamins, β-carotene, vitamin C, vitamin D plus calcium, and multivitamins or multi-ingredient supplements was either insufficient or low-strength, suggesting that these supplements did not reduce risk for cognitive decline. Adverse events were rarely reported. LIMITATION: Studies had high attrition and short follow-up and used a highly variable set of cognitive outcome measures. CONCLUSION: Evidence is insufficient to recommend any OTC supplement for cognitive protection in adults with normal cognition or MCI. PRIMARY FUNDING SOURCE: Agency for Healthcare Research and Quality.

---

### PMID 11466162 — current stance: `supports`

**Stance justification:** > Statistical analysis indicated significant improvements in speed of information processing working memory and executive processing attributable to the EGb.

**Golden note:** 30-day ginkgo in healthy participants — neuropsychological improvements.

**Neuropsychological changes after 30-day Ginkgo biloba administration in healthy participants.**

*The international journal of neuropsychopharmacology*, 2001. Types: Clinical Trial; Journal Article; Randomized Controlled Trial

> Ginkgo biloba extract (EGb) from the world's oldest living tree has been reputed to ameliorate cognitive decline in the elderly and slow cognitive deterioration in patients with dementia of the Alzheimer's type. EGb remains as one of the most popular plant extracts to alleviate symptoms associated with a range of cognitive disorders such as Alzheimer's disease, vascular dementia and age-related amnesic conditions. EGb is known to contain a range of chemically active components that have antagonistic effects on platelet-activating factor, free-radical scavenging activity and direct effects on the cholinergic neurotransmitter system. Recently there has been much speculation, that EGb may act as a 'smart drug' or nootropic agent in the healthy young to improve intelligence. We conducted a 30-d randomized, double-blind, placebo-controlled clinical trial in which 61 participants were administered a battery of validated neuropsychological tests before and after treatment. Statistical analysis indicated significant improvements in speed of information processing working memory and executive processing attributable to the EGb.

---

### PMID 12663701 — current stance: `inconclusive`

**Stance justification:** > Figures for EGb 761 alone were similar but did not reach statistical significance (odds ratio = 0.38, 95% confidence interval = 0.08-1.76, p =.22).

**Golden note:** EPIDOS women elderly — ginkgo + AD onset, no clear protective association.

**Association of Alzheimer's disease onset with ginkgo biloba and other symptomatic cognitive treatments in a population of women aged 75 years and older from the EPIDOS study.**

*The journals of gerontology. Series A, Biological sciences and medical sciences*, 2003. Types: Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't

> BACKGROUND: Peripheral C4A treatment (cerebral and peripheral vasotherapeutics) and especially Ginkgo biloba extracts are prescribed for a number of symptoms, particularly memory impairment, in elderly patients. It is postulated that because of its pharmacological actions, this treatment could prevent the decline of cognitive function, but no studies have been published to date to test its efficacy in prevention of Alzheimer's disease. The potential association between use of C4A treatments, in particular EGb 761 (standardized Ginkgo biloba extracts), and dementia of the Alzheimer type was investigated. METHODS: A case-control study was nested in a cohort of 1462 community-dwelling elderly women aged over 75 years. Sixty-nine women with Alzheimer-type dementia were compared with 345 paired women whose cognitive function remained normal. This study involved women whose cognitive function was evaluated at baseline by use of Pfeiffer's test and whose medication history was taken. The onset of cognitive impairment was investigated over a 7-year follow-up period. In order to study the factors associated with the onset of dementia, the data concerning women with a score of > or = 8 on Pfeiffer's test at inclusion, indicating normal cognitive function, were analyzed. RESULTS: A multivariate analysis including potential confounding factors showed that fewer women who developed Alzheimer's dementia had been prescribed C4A treatment (including EGb 761) for at least 2 years (odds ratio = 0.31, 95% confidence interval = 0.12-0.82, p =.018). Figures for EGb 761 alone were similar but did not reach statistical significance (odds ratio = 0.38, 95% confidence interval = 0.08-1.76, p =.22). CONCLUSION: These results suggest that C4A treatment may reduce the risk of developing Alzheimer's dementia in elderly women. The potential preventive effect of C4A treatments, including EGb 761, requires further examination. To establish a causal relationship, these findings have to be confirmed with prospective studies.

---

### PMID 9803773 — current stance: `supports`

**Stance justification:** > The results also showed that 240 mg of EGb has typical cognitive activator CEEG profiles (responders) in more subjects (8 of 18) than 40 mg tacrine (3 of 18 subjects).

**Golden note:** Ginkgo vs tacrine pharmacology comparison — efficacy claim.

**The pharmacological effects of ginkgo biloba, a plant extract, on the brain of dementia patients in comparison with tacrine.**

*Psychopharmacology bulletin*, 1998. Types: Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> In 1994, a standardized dry extract of Ginkgo biloba leaves (SeGb), has been approved by German health authorities for the treatment of primary degenerative dementia and vascular dementia. More than 24 different brands of Ginkgo biloba extract are sold in the United States. Tacrine, also known as tetrahydroaminoacrine (THA), and donepezil are currently the only drugs approved in the United States for the treatment of Alzheimer's disease. Previous studies demonstrated that SeGb and tacrine induce significant pharmacological effects on the brains of young, healthy human males, as determined by bioelectrical activity measurements obtained using the quantitative pharmaco-electroencephalogram (QPEEG) method. The type of central nervous system (CNS) effects we have seen on computer-analyzed EEGs (CEEGs) after administration of tacrine or EGb suggests both are "cognitive activators" which are, as a class of products, characterized by a (prepost) relative increase of 7.5 to 13 Hz ("alpha") and decrease of 1.3 to 7.5 Hz ("delta" and "theta") activity. To determine whether EGb or tacrine had noticeable pharmacological effects on elderly subjects diagnosed with possible or probable Alzheimer's, the present open, uncontrolled trial was conducted. Data from 18 subjects (11 males, 7 females) at an average age of 67.4 years with light to moderate dementia (Mini Mental mean score = 23.7, ranges: 15-29 [Geriatric Depression Scale mean scores = 3.7; range: 3.2-5.4]) were analyzed for this presentation. Each subject was randomly administered a single oral "Test-Dose" of either 40 mg of tacrine or 240 mg of EGb2 in two separate sessions within 3- to 7-day intervals. Before drug administration and at 1- and 3-hour intervals after drug administration, CEEGs were recorded for a minimum of 10 minutes. The CEEGs were analyzed using Period Analysis programs we developed for QPEEG. The results indicated that both EGb and, to a lesser degree, tacrine induced pharmacological effects, as established by QPEEG measurements, in the CNS similar to those previously established in healthy, young subjects. The type of CNS effects produced by EGb (as established by HZI's CEEG psychotropic drug database) in elderly dementia patients were similar to those induced by tacrine responders as well as those seen after the administration of other "cognitive activators" (pramiracetam, vinpocetine, BMY-21502, suloctidil, and lisuride) and anti-dementia drugs approved in the United States or Europe (tacrine, donepezil, nimodipine, piracetam, and oxiracetam) from our database. The results also showed that 240 mg of EGb has typical cognitive activator CEEG profiles (responders) in more subjects (8 of 18) than 40 mg tacrine (3 of 18 subjects). Because of the small sample size, we could not test the hypothesis that subjects who showed cognitive activator-type pharmacological response to the first Test-Dose of EGb or tacrine also exhibit more therapeutic effects (compared to nonresponders) when drugs are administered chronically.

---

### PMID 18690838 — current stance: `inconclusive`

**Stance justification:** > This study will enable us to evaluate the efficacy of EGb761 in the prevention of AD, and to assess the usefulness of various baseline characteristics as predictors of conversion to AD in this population.

**Golden note:** GuidAge baseline/design paper — no efficacy data yet.

**GuidAge study: a 5-year double blind, randomised trial of EGb 761 for the prevention of Alzheimer's disease in elderly subjects with memory complaints. i. rationale, design and baseline data.**

*Current Alzheimer research*, 2008. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Primary and secondary prevention strategies for Alzheimer's disease (AD) are urgently needed. We have initiated a five-year prospective prevention study involving patients spontaneously reporting memory complaints. The primary objective is to determine the effect of treatment with EGb 76 on the rate of conversion from memory complaints to AD using survival analysis. Ambulatory patients aged at least 70 years who spontaneously reported a memory complaint during a GP or memory centre consultation were eligible for inclusion. Patients with major objective memory impairment or clinically relevant symptoms of anxiety and depression were excluded. Subjects were randomised to receive either EGb 761 120mg bid or matching placebo. Participants undergo an annual visit at a memory centre, where a series of neuropsychological tests are administered to assess cognitive function (Grober and Buschke, Trail-Making and controlled oral word association tests) and cognitive status (MMS and CDR). Functional status is evaluated with the Instrumental Activities of Daily Living questionnaire. The primary outcome is the transition to a diagnosis of AD (DSM-IV and NINCDS-ADRDA criteria), determined at the annual memory centre visit. A total of 4066 patients were screened for participation, of whom 2854 fulfilled the eligibility criteria and were entered into the study. Their mean age was 76.8+/-4.4 years and 66.7% were female. The mean MMSE score was 27.8+/-1.7 and 55.5% presented a CDR score of 0.5. This study will enable us to evaluate the efficacy of EGb761 in the prevention of AD, and to assess the usefulness of various baseline characteristics as predictors of conversion to AD in this population.

---

### PMID 24871648 — current stance: `supports`

**Stance justification:** > The meta-analysis for assessing the prevention effect of Ginkgo against AD suggested that risk ratio (RR) is 1.06 (95% CI: 0.92 to 1.22) between Gingko and the placebo, with no significant heterogeneity across studies. Ginkgo may help established AD patients with cognitive symptoms but cannot prevent the neurodegenerative progression of the disease.

**Golden note:** Natural medicines + ginkgo meta — efficacy claim.

**A systematic review on natural medicines for the prevention and treatment of Alzheimer's disease with meta-analyses of intervention effect of ginkgo.**

*The American journal of Chinese medicine*, 2014. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> We performed a systematic review to evaluate the efficacy of natural medicines for the treatment of Alzheimer's disease (AD) in randomized controlled trials (RCTs). Disease-specific and intervention terms were searched in MEDLINE, EMBASE, the Cochrane Library and PsycINFO to identify RCTs for the AD intervention of natural medicines, and searched for literatures in English language. The RCTs compared natural medicines and either placebo or orthodox medication in AD patients. The quality of literature was evaluated by Jadad's score and the Cochrane assessing tool to reduce the risk of bias. Meta-analysis and the heterogeneity of results across the trials were performed. Out of the literatures, 21 clinical reports were included in this review that satisfied the particular selection criteria. Apart from Ginkgo, other treatments we came across had minimal benefits and/or the methodological quality of the available trials was poor. The meta-analyses showed that Ginkgo had better outcomes than the placebo, with the standardized mean difference (SMD) between Ginkgo and the placebo on cognition being -1.62 (95% CI: -2.69 to -0.56) and on activities of daily living being -1.55 (95% CI: -2.55 to -0.55), with the existence of significant heterogeneity across studies. The meta-analysis for assessing the prevention effect of Ginkgo against AD suggested that risk ratio (RR) is 1.06 (95% CI: 0.92 to 1.22) between Gingko and the placebo, with no significant heterogeneity across studies (test for heterogeneity, p = 0.49). Our results suggest that Ginkgo may help established AD patients with cognitive symptoms but cannot prevent the neurodegenerative progression of the disease.

---

### PMID 10641953 — current stance: `inconclusive`

**Stance justification:** > There is relatively compelling evidence that Ginkgo biloba (ginkgo) is effective in delaying the clinical course of dementias.

**Golden note:** Herbal medications elderly review — ginkgo broadly discussed.

**Herbal medications for common ailments in the elderly.**

*Drugs & aging*, 1999. Types: Journal Article; Meta-Analysis

> The popularity of herbal medicine is at an all time peak. This article provides an overview of systematic reviews of herbal treatments for conditions common in elderly individuals. According to this evidence, there is little doubt that Hypericum perforatum (St John's Wort) is well tolerated and effective for mild to moderate depression. Although widely used, Valeriana officinalis (valerian) has not been shown beyond reasonable doubt to be effective for insomnia. There is relatively compelling evidence that Ginkgo biloba (ginkgo) is effective in delaying the clinical course of dementias. It has been well documented that Aesculus hippocastanum (horse chestnut) seed extracts alleviate the subjective symptoms and reduce the objective signs of chronic venous insufficiency. Serenoa repens (saw palmetto) is effective in improving the symptoms of benign prostatic hyperplasia. Finally, yohimbine has been shown to be effective forerectile dysfunction. It is concluded that several plant-based medicines can be useful additions to our therapeutic repertoire for treating common conditions in the elderly. However, several uncertainties remain and, at present, prevent unreserved recommendations.

---

### PMID 26058281 — current stance: `contradicts`

**Stance justification:** > Meta-analysis of the two trials involving 5,889 participants indicated no significant difference in dementia rate between Ginkgo biloba and the placebo (347/2,951 vs. 330/2,938, odds ratio = 1.05, 95% CI 0.89-1.23). There is no convincing evidence from this review that demonstrated Ginkgo biloba in late-life can prevent the development of dementia.

**Golden note:** Ginkgo for dementia prevention meta in non-demented — no efficacy.

**Ginkgo biloba for prevention of dementia: a systematic review and meta-analysis.**

*Journal of the Medical Association of Thailand = Chotmaihet thangphaet*, 2015. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> OBJECTIVE: To determine the efficacy of Ginkgo biloba for the prevention of dementia in individuals without dementia. MATERIAL AND METHOD: English databases including Medline, Embase, Cochrane Library and PsycINFO, were searched, and randomized double-blind controlled studies comparing Ginkgo biloba with placebo in prevention of dementia were considered. Two trials met inclusion criteria. Methodological quality was assessed using the Jadad criteria. RESULTS: Meta-analysis of the two trials involving 5,889 participants indicated no significant difference in dementia rate between Ginkgo biloba and the placebo (347/2,951 vs. 330/2,938, odds ratio = 1.05, 95% CI 0.89-1.23) and there was no considerable heterogeneity between the trials. The two studies revealed no statistically significant differences in the rate of serious adverse effect between Ginko biloba and the placebo. CONCLUSION: There is no convincing evidence from this review that demonstrated Ginkgo biloba in late-life can prevent the development of dementia. Using it for this indication is not suggested at present.

---

### PMID 15117063 — current stance: `supports`

**Stance justification:** > The final examination revealed a statistically significant difference between the two groups for the VAS mental health and quality of life, as also for SIS Mood at the telephone interview in week 2.

**Golden note:** Ginkgo in healthy elderly — positive short-term effect.

**[The effect of ginkgo biloba on healthy elderly subjects].**

*Fortschritte der Medizin. Originalien*, 2003. Types: Clinical Trial; Journal Article; Randomized Controlled Trial

> BACKGROUND AND AIM: Over the past 25 years, numerous studies have confirmed the positive effect of the special ginkgo extract EGb 761 on the mental ability and emotional well-being of patients with cognitive disorders of vascular genesis, and Alzheimer-type dementia. The following study investigated the short-term effect of the special ginkgo extract EGb 761 on the subjective emotional well-being of healthy elderly subjects. STUDY POPULATION AND METHOD: The study was designed as a randomized double-blind, monocenter study with parallel groups. It included 66 healthy subjects of both sexes aged between 50 and 65 with no age-related cognitive impairments. For a period of 4 weeks, 34 subjects received a daily dose of 240 mg EGb 761, and 32 a placebo. Prior to starting medication and after 28 days of treatment, subjects completed the following scales and questionnaires to establish subjective emotional well-being: the Profile of Mood States (POMS), the Self Rating Depression Scale (SDS), three Visual Analog Scales to assess the quality of life (VAS-QoL), general health (VAS-GH) and mental health (VAS-MH), and a new instrument for assessing changes in general subjective well-being, the Subjective Intensity Score Mood (SIS Mood). Depending on the underlying distribution of the variables analyzed, parametric (t-tests) or nonparametric tests (U-tests) were performed to compare mean values and distributions both within and between the treatment groups. RESULTS: The final examination revealed a statistically significant difference between the two groups for the VAS mental health and quality of life, as also for SIS Mood at the telephone interview in week 2. A comparison of baseline with the final examination within the groups showed a statistically significant improvement in the EGb 761 group for the variables: depression, fatigue, anger and SDS. For none of the variables investigated was a worsening observed in the EGb 761 group. CONCLUSIONS: The results suggest a positive effect of EGb 761 on the subjective emotional well-being of healthy elderly persons.

---

### PMID 18165850 — current stance: `inconclusive`

**Stance justification:** > We present here the first comparative design and baseline data from GEM and Guidage, two of the largest dementia primary prevention trials to date.

**Golden note:** GEM vs GuidAge design comparison — methodology paper.

**Comparison of the design differences between the Ginkgo Evaluation of Memory study and the GuidAge study.**

*The journal of nutrition, health & aging*, 2008. Types: Comparative Study; Journal Article; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> The epidemic of late life dementia, prominence of use of alternative medications and supplements, and initiation of efforts to determine how to prevent dementia have led to efforts to conduct studies aimed at prevention of dementia. The GEM (Ginkgo Evaluation of Memory) and GuidAge studies are ongoing randomized double-blind, placebo-controlled trials of Ginkgo biloba, administered in a dose of 120 mg twice per day as EGb761, to test whether Ginkgo biloba is effective in the prevention of dementia (and especially Alzheimer's disease) in normal elderly or those early cognitive impairment. Both GEM and GuidAge will also add substantial knowledge to the growing need for expertise in designing and implementing clinical trials to test the efficacy of putative disease-modifying agents for the dementias. While there are many similarities between GEM and Guidage, there are also significant differences. We present here the first comparative design and baseline data fromGEM and Guidage, two of the largest dementia primary prevention trials to date.

---

