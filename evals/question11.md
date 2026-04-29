# Q11: Does CPAP treatment for obstructive sleep apnea slow cognitive decline?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=14 PMIDs.

**Current S/C/I**: 10 / 0 / 4
**Proposed S/C/I**: 8 / 0 / 6
**Net flips**: 2

The current corpus is heavily skewed toward `supports` (10/14) with no
`contradicts`. The strict bar applied conservatively shifts only 2
labels — most studies show genuinely positive effects, though the
evidence base relies heavily on small studies and ambiguous comparator
designs (within-subject vs between-arm).

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `18795985` | 2008 | **supports → inconclusive** | Ancoli-Israel RCT, n=52, 6 wk. Verbatim: *"A comparison of subjects randomized to 3 weeks of therapeutic versus placebo CPAP **suggested no significant improvements in cognition**."* The within-group pre/post comparison was significant, but that's not the controlled signal — the randomized comparison was null. The authors describe this as exploratory: *"The study was underpowered to make definitive statements."* Genuinely mixed → `inconclusive`. |
| `19968005` | 2009 | **supports → inconclusive** | Sustained-CPAP follow-up, **n=10** (5 CPAP+ vs 5 CPAP-). Reports moderate-to-large effect sizes, but with such a small sample the effect estimates are highly imprecise. The abstract itself characterizes the study as *"preliminary"* and recommends *"prospective randomized controlled research trials evaluating these hypotheses are needed."* Per strict bar, pilot/exploratory → `inconclusive`. |

## Confirmed (no change)

- `31881487` (2019 OSA-cognition-AD SR — *"CPAP treatment may be effective in improving cognition"*) — **supports ✓** (defensible narrative SR)
- `24828897` (2014 single-blind n=23, 3-yr follow-up) — **supports ✓** (annual MMSE decline -0.7 vs -2.2, p=0.013, sig)
- `16696743` (2006 daytime sleepiness primary, no cognitive primary) — **inconclusive ✓**
- `30724333` (Memories 1 quasi-experimental, n=54, 1 yr) — **supports ✓** (sig improvement in psychomotor/cognitive processing speed)
- `19699148` (2009 sleep parameter primary, no cognition) — **inconclusive ✓**
- `35523585` (2022 PAP-cognitive disorders SR, 11 studies) — **supports ✓** (9/11 reported protective effect)
- `34546386` (2021 cognition meta of 7 RCTs) — **supports ✓** (SMD 0.49, 95% CI 0.11-0.86, sig)
- `33619666` (2021 OSAS+AD/MCI retrospective, n=24) — **supports ✓** (defensible; small but sig CDR difference)
- `37924680` (2023 CPAP adherence SR — adherence focus) — **inconclusive ✓**
- `37586145` (2023 CPAP adherence SR neurodegen — adherence focus) — **inconclusive ✓**
- `32108738` (Memories 1 mild OSA secondary) — **supports ✓** (defensible) — *substudy of `30724333`*
- `32045010` (Taiwan retrospective, 3,978 OSA) — **supports ✓** (treatment HR 0.23 sig)

## Cross-cutting issues

- **Same-cohort substudies**: `30724333` and `32108738` both report from
  the Memories 1 trial. Tagged for the planned UI paper-type filter.
- **Adherence-focused SRs**: `37924680` and `37586145` are both about
  adherence rather than efficacy. Correctly labeled `inconclusive` but
  worth noting that the question is about treatment effect, not adherence.
- **No `contradicts` in this corpus** — that's plausible because no
  large RCT has reported a null primary endpoint specifically for
  cognitive decline in CPAP-treated AD/MCI. The closest is `18795985`
  where the controlled comparison was null but the within-subject
  comparison was positive.
- After flips: 8 supports, 0 contradicts, 6 inconclusive — the
  `expected_consensus: "contested"` is debatable; "leaning positive
  with weak evidence base" might fit better.

## Highest-confidence flips for this question

- `18795985` supports → inconclusive — the controlled randomized comparison
  was *"no significant improvements"* on cognition; the current label
  ignores the study's own caveat about being underpowered.
- `19968005` supports → inconclusive — n=10 follow-up, abstract calls
  itself "preliminary."


---

## Abstracts (n=14)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 18795985 — current stance: `supports`

**Golden note:** Ancoli-Israel CPAP RCT in AD — improved cognition.

**Cognitive effects of treating obstructive sleep apnea in Alzheimer's disease: a randomized controlled study.**

*Journal of the American Geriatrics Society*, 2008. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> OBJECTIVES: To examine whether treatment of obstructive sleep apnea (OSA) with continuous positive airway pressure (CPAP) in patients with Alzheimer's disease (AD) results in better cognitive function. DESIGN: Randomized double-blind placebo-controlled trial. Participants were randomized to therapeutic CPAP for 6 weeks or placebo CPAP for 3 weeks followed by therapeutic CPAP for 3 weeks. SETTING: General clinical research center. PARTICIPANTS: Fifty-two men and women with mild to moderate AD and OSA. INTERVENTION: CPAP. MEASUREMENTS: A complete neuropsychological test battery was administered before treatment and at 3 and at 6 weeks. RESULTS: A comparison of subjects randomized to 3 weeks of therapeutic versus placebo CPAP suggested no significant improvements in cognition. A comparison of pre- and posttreatment neuropsychological test scores after 3 weeks of therapeutic CPAP in both groups showed a significant improvement in cognition. The study was underpowered to make definitive statements about improvements within specific cognitive constructs, although exploratory post hoc examination of change scores for individual tests suggested improvements in episodic verbal learning and memory and some aspects of executive functioning such as cognitive flexibility and mental processing speed. CONCLUSION: OSA may aggravate cognitive dysfunction in dementia and thus may be a reversible cause of cognitive loss in patients with AD. OSA treatment seems to improve some cognitive functioning. Clinicians who care for patients with AD should consider implementing CPAP treatment when OSA is present.

---

### PMID 31881487 — current stance: `supports`

**Golden note:** OSA-cognition-AD systematic review — treatment beneficial.

**Obstructive sleep apnea, cognition and Alzheimer's disease: A systematic review integrating three decades of multidisciplinary research.**

*Sleep medicine reviews*, 2019. Types: Journal Article; Research Support, N.I.H., Extramural; Systematic Review

> Increasing evidence links cognitive-decline and Alzheimer's disease (AD) to various sleep disorders, including obstructive sleep apnea (OSA). With increasing age, there are substantial differences in OSA's prevalence, associated comorbidities and phenotypic presentation. An important question for sleep and AD researchers is whether OSA's heterogeneity results in varying cognitive-outcomes in older-adults compared to middle-aged adults. In this review, we systematically integrated research examining OSA and cognition, mild cognitive-impairment (MCI) and AD/AD biomarkers; including the effects of continuous positive airway pressure (CPAP) treatment, particularly focusing on characterizing the heterogeneity of OSA and its cognitive-outcomes. Broadly, in middle-aged adults, OSA is often associated with mild impairment in attention, memory and executive function. In older-adults, OSA is not associated with any particular pattern of cognitive-impairment at cross-section; however, OSA is associated with the development of MCI or AD with symptomatic patients who have a higher likelihood of associated disturbed sleep/cognitive-impairment driving these findings. CPAP treatment may be effective in improving cognition in OSA patients with AD. Recent trends demonstrate links between OSA and AD-biomarkers of neurodegeneration across all age-groups. These distinct patterns provide the foundation for envisioning better characterization of OSA and the need for more sensitive/novel sleep-dependent cognitive assessments to assess OSA-related cognitive-impairment.

---

### PMID 19968005 — current stance: `supports`

**Golden note:** Sustained CPAP slows cognitive decline in AD+OSA preliminary study.

**Sustained use of CPAP slows deterioration of cognition, sleep, and mood in patients with Alzheimer's disease and obstructive sleep apnea: a preliminary study.**

*Journal of clinical sleep medicine : JCSM : official publication of the American Academy of Sleep Medicine*, 2009. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> INTRODUCTION: Obstructive sleep apnea (OSA) is common among patients with Alzheimer's disease (AD). Untreated OSA exacerbates the cognitive and functional deficits. Continuous positive airway pressure (CPAP) has recently been shown to have beneficial effects on cognition in AD. Little attention has focused on the long-term benefits of CPAP in these patients. METHODS: This was an exploratory study of sustained CPAP use (mean use = 13.3 months, SD = 5.2) among a subset of participants from an initial 6-week randomized clinical trial (RCT) of CPAP in patients with mild to moderate AD. Follow-up included 5 patients who continued CPAP (CPAP+) after completion of the RCT and 5 patients who discontinued CPAP (CPAP-), matched by time of completion of the initial study. A neuropsychological test battery and sleep/mood questionnaires were administered and effect sizes were calculated. RESULTS: Even with a small sample size, sustained CPAP use resulted in moderate-to-large effect sizes. Compared to the CPAP- group, the CPAP+ group showed less cognitive decline with sustained CPAP use, stabilization of depressive symptoms and daytime somnolence, and significant improvement in subjective sleep quality. Caregivers of the CPAP+ group also reported that their own sleep was better when compared to the final RCT visit and that their patients psychopathological behavior was improved. CONCLUSION: The results of this preliminary study raise the possibility that sustained, long-term CPAP treatment for patients with AD and OSA may result in lasting improvements in sleep and mood as well as a slowing of cognitive deterioration. Prospective randomized controlled research trials evaluating these hypotheses are needed.

---

### PMID 24828897 — current stance: `supports`

**Golden note:** CPAP slows cognitive decline in mild-mod AD.

**Treatment of sleep apnoea syndrome decreases cognitive decline in patients with Alzheimer's disease.**

*Journal of neurology, neurosurgery, and psychiatry*, 2014. Types: Clinical Trial; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: It is essential to detect and then treat factors that aggravate Alzheimer's disease (AD). Here, we sought to determine whether or not continuous positive airway pressure (CPAP) therapy for sleep apnoea syndrome (SAS) slows the rate of cognitive decline in mild-to-moderate AD patients. METHODS: Between January 2003 and June 2011, we included consecutive, mild-to-moderate AD patients (a Mini Mental State Examination (MMSE) score at inclusion ≥15) with severe SAS as determined by video-polysomnography (an apnoea-hypopnoea index ≥30). In this single-blind, proof-of-concept trial, we analysed the mean decline in the annual MMSE score (the main outcome measure) according to whether or not the patients had received CPAP therapy. The decline was computed for each patient and for the first 3 years of follow-up. RESULTS: Of the 23 included patients, 14 underwent CPAP treatment. The CPAP and non-CPAP groups did not differ significantly in terms of their demographic characteristics or MMSE score at baseline. The median annual MMSE decline was significantly slower in the CPAP group (-0.7 (-1.7; +0.8)) than in the non-CPAP group (-2.2 (-3.3; -1.9); p=0.013). CONCLUSIONS: In this pilot study, CPAP treatment of severe SAS in mild-to-moderate AD patients was associated with significantly slower cognitive decline over a three-year follow-up period. Our results emphasise the importance of detecting and treating SAS in this population.

---

### PMID 16696743 — current stance: `inconclusive`

**Golden note:** CPAP reduces daytime sleepiness in mild-mod AD — sleepiness primary, not cognition.

**Continuous positive airway pressure reduces subjective daytime sleepiness in patients with mild to moderate Alzheimer's disease with sleep disordered breathing.**

*Journal of the American Geriatrics Society*, 2006. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't; Research Support, U.S. Gov't, Non-P.H.S.

> OBJECTIVES: Studies have reported that 33% to 70% of patients with Alzheimer's disease (AD) have sleep-disordered breathing (SDB). Continuous positive airway pressure (CPAP) treatment has been shown to reduce daytime sleepiness and improve health-related quality of life in nondemented older people with SDB. The effect of therapeutic CPAP treatment on daytime sleepiness in patients with mild-moderate AD with SDB was assessed. DESIGN: Randomized, double-blind, placebo-controlled trial. SETTING: Patients' home and the University of California San Diego, General Clinical Research Center, J. Christian Gillin Laboratory of Sleep and Chronobiology. PARTICIPANTS: Thirty-nine community-dwelling elderly patients with mild-moderate probable AD with SDB. INTERVENTION: Patients were randomly assigned to receive 6 weeks of therapeutic CPAP or 3 weeks of sham CPAP followed by 3 weeks of therapeutic CPAP. MEASUREMENTS: Epworth Sleepiness Scale (ESS) was administered at baseline, 3 weeks, and 6 weeks. Changes in daytime sleepiness in subjects who received optimal therapeutic CPAP were compared with changes in the sham CPAP group. RESULTS: Within the therapeutic CPAP group, ESS scores were reduced from 8.89 during baseline to 6.56 after 3 weeks of treatment (P=.04) and to 5.53 after 6 weeks of treatment (P=.004). In the sham CPAP group, there was no significant difference after 3 weeks of sham CPAP but a significant decrease from 7.68 to 6.47 (P=.01) after 3 weeks of therapeutic CPAP. CONCLUSION: These data provide evidence of the effectiveness of CPAP in reducing subjective daytime sleepiness in patients with AD with SDB.

---

### PMID 30724333 — current stance: `supports`

**Golden note:** CPAP adherence slows cognitive decline in MCI + apnea.

**CPAP Adherence May Slow 1-Year Cognitive Decline in Older Adults with Mild Cognitive Impairment and Apnea.**

*Journal of the American Geriatrics Society*, 2019. Types: Clinical Trial; Journal Article; Research Support, N.I.H., Extramural

> BACKGROUND/OBJECTIVES: Obstructive sleep apnea (OSA) has been linked to an increased risk for Alzheimer's disease (AD), but little prospective evidence exists on the effects of OSA treatment in preclinical AD. The objective was to determine if continuous positive airway pressure (CPAP) treatment adherence, controlling for baseline differences, predicts cognitive and everyday function after 1 year in older adults with mild cognitive impairment (MCI) and to determine effect sizes for a larger trial. DESIGN: Quasi-experimental pilot clinical trial with CPAP adherence defined as CPAP use 4 hours or more per night over 1 year. SETTING: Sleep and geriatric clinics and community. PARTICIPANTS: Older adults, aged 55 to 89 years, with an apnea-hypopnea index of 10 or higher participated: (1) MCI, OSA, and CPAP adherent (MCI +CPAP), n = 29; and (2) MCI, OSA, CPAP nonadherent (MCI -CPAP), n = 25. INTERVENTION: CPAP. MEASUREMENTS: The primary cognitive outcome was memory (Hopkins Verbal Learning Test-Revised), and the secondary cognitive outcome was psychomotor/cognitive processing speed (Digit Symbol subtest from the Wechsler Adult Intelligence Scale Substitution Test). Secondary function and progression measures were the Everyday Cognition, Alzheimer's Disease Cooperative Study-Clinical Global Impression of Change Scale, and Clinical Dementia Rating. RESULTS: Statistically significant improvements in psychomotor/cognitive processing speed in the MCI +CPAP group vs the MCI -CPAP group were observed at 1 year after adjustment for age, race, and marital status (parameter estimate = 1.68; standard error = 0.47; 95% confidence interval = 0.73-2.62), with a 6-month effect size (ES) of 0.46 and a 1-year ES of 1.25. There were small to moderate ESs for memory (ES 0.20, 6 mo), attention (ES 0.25, 1 y), daytime sleepiness (ES 0.33, 6 mo and ES 0.22, 1 y), and everyday function (ES 0.50, 6 mo) favoring the MCI +CPAP group vs the MCI -CPAP group. CONCLUSION: Controlling for baseline differences, 1 year of CPAP adherence in MCI +OSA significantly improved cognition, compared with a nonadherent control group, and may slow the trajectory of cognitive decline. TRIAL REGISTRATION NUMBER: Memories; NCT01482351; https://clinicaltrials.gov/ct2/show/NCT01482351?cond=MCI+and+OSA&rank=1 J Am Geriatr Soc 67:558-564, 2019.

---

### PMID 19699148 — current stance: `inconclusive`

**Golden note:** CPAP deepens sleep in AD+OSA — sleep parameter primary, not cognition.

**Continuous positive airway pressure deepens sleep in patients with Alzheimer's disease and obstructive sleep apnea.**

*Sleep medicine*, 2009. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, U.S. Gov't, Non-P.H.S.

> OBJECTIVE: Patients with Alzheimer's disease (AD) and obstructive sleep apnea (OSA) experience disrupted sleep. This study examined the effect of continuous positive airway pressure (CPAP) on sleep parameters in AD patients with OSA. METHODS: A randomized placebo-controlled trial of 3 weeks of therapeutic CPAP (tCPAP) vs. 3 weeks placebo CPAP (pCPAP) followed by 3 weeks tCPAP in patients with AD and OSA. Polysomnography data from screening after one night and after 3 weeks of treatment were analyzed. Records were scored for percent of each sleep stage, total sleep time (TST), sleep efficiency (SE), sleep period (SP), time in bed (TIB), sleep onset (SO), wake time after sleep onset (WASO), and arousals. A randomized design comparing one night of pCPAP to tCPAP and a paired analysis combining 3 weeks of tCPAP were performed. RESULTS: Fifty-two participants (mean age=77.8 years, SD=7.3) with AD and OSA were included. After one treatment night, the tCPAP group had significantly less % Stage 1 (p=0.04) and more % Stage 2 sleep (p=0.02) when compared to the pCPAP group. In the paired analysis, 3 weeks of tCPAP resulted in significant decreases in WASO (p=0.005), % Stage 1 (p=0.001), arousals (p=0.005), and an increase in % Stage 3 (p=0.006). CONCLUSION: In mild to moderate AD patients with OSA, the use of tCPAP resulted in deeper sleep after just one night, with improvements maintained for 3 weeks.

---

### PMID 35523585 — current stance: `supports`

**Golden note:** PAP + cognitive disorders systematic review — beneficial.

**Positive Airway Pressure and Cognitive Disorders in Adults With Obstructive Sleep Apnea: A Systematic Review of the Literature.**

*Neurology*, 2022. Types: Systematic Review; Journal Article

> BACKGROUND AND OBJECTIVES: Alzheimer disease (AD) and other forms of dementia represent a rising global public health crisis. Because effective treatments to prevent, cure, or slow progression of dementia are unavailable, identification of treatable risk factors that increase dementia risk such as obstructive sleep apnea (OSA) could offer promising means to modify dementia occurrence or severity. Here, we systematically reviewed the impact of positive airway pressure (PAP) therapy on the incidence of cognitive disorders and cognitive decline among middle-aged and older adults with OSA. METHODS: We performed a systematic search of MEDLINE, EMBASE, Scopus, and CINAHL before May 2021 to identify articles that focused on associations between PAP therapy use and cognitive disorders. We included studies that examined the effects of PAP treatment on (1) the incidence of cognitive disorders among individuals ≥40 years of age diagnosed with OSA and (2) the progression of cognitive decline among people with preexisting cognitive disorders and OSA. RESULTS: We identified 11 studies (3 clinical trials and 8 observational studies). In these studies, 96% participants had OSA (n = 60,840) and 9% had baseline cognitive impairment (mild cognitive impairment [MCI] or AD) (n=5,826). Of all study participants, 43,970 obtained PAP therapy, and 16,400 were untreated or in a placebo group. Nine out of 11 studies reported a protective effect of PAP therapy on MCI and AD incidence, e.g., delayed age at MCI onset, reduced MCI or AD incidence, slower cognitive decline, or progression to AD. DISCUSSION: These findings suggest a role for OSA as a modifiable risk factor for cognitive decline. Identification of modifiable risk factors is imperative for alleviating the impact of cognitive disorders on aging adults and their family members. Future research should build on this review and focus on PAP interventions as a potential means to alleviate the incidence of cognitive disorders and cognitive decline, particularly among ethnoracial groups who have been underrepresented and underinvestigated in the extant literature.

---

### PMID 34546386 — current stance: `supports`

**Golden note:** CPAP cognition meta in OSA + cognitive impairment — improves cognition.

**Cognition effectiveness of continuous positive airway pressure treatment in obstructive sleep apnea syndrome patients with cognitive impairment: a meta-analysis.**

*Experimental brain research*, 2021. Types: Journal Article; Meta-Analysis; Systematic Review

> Obstructive sleep apnea (OSA) is a common respiratory disorder characterized by recurrent pharyngeal collapses during sleep leading to intermittent hypoxia and sleep disruption. Cognitive challenges and high risks of cognitive impairment, including Alzheimer's disease (AD), are closely associated with OSA. Currently, continuous positive airway pressure (CPAP) is widely used in the treatment of OSA. However, whether CPAP benefits cognitive functions in patients with OSA remains elusive. Here, we identified published studies through a systematic review of PubMed, Cochrane Library, Embase, Wanfang Data, CBM, and CNKI from January 1, 1970, to July 1, 2020. 288 patients from 7 articles (one was excluded in the meta-analysis for it was a follow-up study) were included in the present study. It revealed that cognitive functions of OSA patients with mild cognitive impairment (MCI) or AD were mildly but significantly improved after CPAP treatment (SMD 0.49, 95% CI 0.11-0.86), especially long-term CPAP treatment (SMD 0.56, 95% CI 0.10-1.02, p = 0.02), as measured by Mini-Mental State Examination (MMSE) (SMD 0.49, 95%CI 0.11-0.86). However, no significant cognition benefits were detected by the Montreal Cognitive Assessment (SMD 0.43, 95% CI 0.85-1.72). In terms of heterogeneity, cognitive improvements by CPAP were detectable on OSA patients either at a younger age or over longer periods of CPAP treatment. Therefore, our findings highlight the partial efficiency of CPAP treatment in cognition improvement of OSA patients with MCI or AD.

---

### PMID 33619666 — current stance: `supports`

**Golden note:** CPAP + OSAS + AD/MCI retrospective — slows deterioration.

**Obstructive sleep apnea syndrome and Alzheimer's disease pathology: may continuous positive airway pressure treatment delay cognitive deterioration?**

*Sleep & breathing = Schlaf & Atmung*, 2021. Types: Journal Article; Multicenter Study

> PURPOSE: The main aim of the present study was to identify the long-term effects of continuous positive airway pressure (CPAP) treatment in patients co-affected by obstructive sleep apnea syndrome (OSAS) and mild cognitive impairment (MCI) or dementia due to Alzheimer's disease (ADD). METHODS: This retrospective multicentre study included patients affected by MCI or ADD, diagnosed according to the core clinical and biomarkers criteria, and presenting comorbid OSAS. Only patients performing at least a 1-year visit during their follow-up to monitor cognitive deterioration and adherence with CPAP treatment were included. Both Mini-Mental State Examination (MMSE) and clinical dementia rating scale (CDR) were conducted during the baseline and the follow-up visits. RESULTS: Twenty-four patients were included in the study and were distributed according to the diagnosis in MCI (n = 8) or ADD (n = 16). There were no significant differences in the variables analysed at baseline between the CPAP non-adherent and CPAP adherent patients. In the whole group, a significant decrease was found in MMSE scores, and a significant increase was found in CDR scores between baseline and follow-up. No longitudinal changes in ESS scores were statistically significant from baseline to follow-up. A significant difference was found for the mean score change of the CDR since CPAP non-adherent patients showed a higher mean change of CDR compared to CPAP adherent patients. No significant differences were found for the mean change of MMSE. CONCLUSION: These findings highlight the clinical potential of treating OSAS with CPAP to delay cognitive deterioration in patients with MCI or ADD.

---

### PMID 37924680 — current stance: `inconclusive`

**Golden note:** CPAP adherence systematic review in MCI/AD — efficacy trials still needed.

**A systematic review on adherence to continuous positive airway pressure (CPAP) treatment for obstructive sleep apnoea (OSA) in individuals with mild cognitive impairment and Alzheimer's disease dementia.**

*Sleep medicine reviews*, 2023. Types: Systematic Review; Journal Article; Research Support, Non-U.S. Gov't

> Obstructive sleep apnoea (OSA) is highly prevalent in mild cognitive impairment (MCI) and Alzheimer's disease (AD). The gold standard treatment for OSA is continuous positive airway pressure (CPAP). Long-term, well-powered efficacy trials are required to understand whether CPAP could slow cognitive decline in individuals with MCI/AD, but its tolerability in this group remains uncertain. The present review investigates CPAP adherence among individuals with OSA and MCI/AD. Electronic searches were performed on 8 databases. The Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines were followed. Six independent studies and four secondary analyses included 278 unique participants (mean age = 72.1 years). In five of the retained studies, around half of participants (45% N = 85 MCI, 56% N = 22 AD) were adherent to CPAP, where ≥4 h use per night was considered adherent. Three of the retained studies also reported average CPAP use to range between 3.2 and 6.3 h/night. CPAP adherence in individuals with MCI and AD is low, albeit similar to the general elderly population. Reporting adherence in future studies as both average duration as well as using a binary cut-off would improve our understanding of the optimum CPAP use in dementia clinical trials and care.

---

### PMID 37586145 — current stance: `inconclusive`

**Golden note:** CPAP adherence in neurodegen — adherence focus, mixed.

**Adherence to continuous positive airway pressure for the treatment of obstructive sleep apnea in neurodegenerative diseases: A systematic review.**

*Sleep medicine reviews*, 2023. Types: Systematic Review; Journal Article; Research Support, Non-U.S. Gov't

> Obstructive sleep apnea (OSA) is prevalent in patients with neurodegenerative diseases and is associated with worse outcomes. Positive airway pressure therapy has the potential to benefit these patients but can be challenging in this population. Our primary aim was to describe positive pressure therapy adherence. Secondarily, we aimed at identifying identify predictors of adherence to treatment in adults with neurodegenerative diseases and OSA, and report the effect of PAP adherence on outcomes such as cognitive function, quality of life and patient/caregiver satisfaction. We performed a systematic review of the literature and identified seventeen studies, eight reporting on adults with obstructive sleep apnea and mild cognitive impairment (MCI) and/or Alzheimer's disease (AD), 6 with Parkinson's disease (PD), and 3 with multiple system atrophy (MSA). Meta-analyses were not performed due to lack of systematic and standardized reporting of the primary outcome. Study duration ranged from 6 weeks to an average of 3.3 years. PAP adherence definition was widely variable between studies. Attrition rates ranged from 12% to 75%. In MCI/AD, adherence rates ranged from 28% to 61% (study duration range: 3 weeks to 3.3 years). Younger age, race (white) and better CPAP confidence scores at 1 week were associated with more CPAP use while APOE4 positive and unmarried individuals were more likely to abandon CPAP. In most studies, adherent patients had improvement in excessive daytime sleepiness, depressive symptoms, sleep quality, ability to manage daily activities and certain aspects of cognition (composite score or global cognition, psychomotor speed, executive function), as well as less cognitive decline over time. Caregiver satisfaction was also better in PAP adherent patients in one study. In PD, 15-25% of individuals refused treatment with PAP upfront, and attrition ranged from 8 to 75%. Adherent patients used their device for an average of 3h27 to 5h12 per night (study duration range: 6 weeks to 12 months). Longer disease duration, worse motor symptoms or sleep quality and lower % of REM sleep were identified as predictors of lower PAP adherence in a preliminary study, while race (non-white) and sex (women) were linked to lower adherence in a large retrospective study. In the study reporting the highest attrition rate (75%), individuals had lower educational levels. PAP adherence improved daytime sleepiness, anxiety symptoms, sleep architecture and quality and global non-motor symptoms. However, in one short-term (3 weeks) study, there was no improvement in neuropsychological testing composite score. Three studies on MSA patients suffering from sleep-disordered breathing showed that most patients are accepting of PAP (69-72%) with an average nightly use of 4h42 to 6h18. Floppy epiglottis was more frequently seen in patients discontinuing PAP in one study. In one study, four adults with MSA and long-term PAP use reported better sleep and improved vigilance. Survival time was no different between treated and untreated individuals. In conclusion, PAP therapy is challenging in patients with OSA and NDD, as evidenced by the considerable attrition and low adherence rates reported in this systematic review. There is emerging evidence proposing OSA a treatable target to prevent clinical and functional deterioration in patients with neurodegenerative diseases and addressing potential barriers to PAP adherence is paramount to maximize adherence. Our systematic review outlines several of these potential barriers, underscoring the need for future studies to standardize the definition of and explore long-term adherence to PAP therapy and assess interventions that can optimize adherence in this patient population.

---

### PMID 32108738 — current stance: `supports`

**Golden note:** 1-year CPAP adherence improves cognition in mild apnea + MCI.

**One Year of Continuous Positive Airway Pressure Adherence Improves Cognition in Older Adults With Mild Apnea and Mild Cognitive Impairment.**

*Nursing research*, 2020. Types: Clinical Trial; Journal Article; Research Support, N.I.H., Extramural

> BACKGROUND: Mild cognitive impairment frequently represents a predementia stage of Alzheimer's disease. Although obstructive sleep apnea is increasingly recognized as a common comorbidity of mild cognitive impairment, most apnea research has focused on middle-aged adults with moderate-to-severe obstructive sleep apnea. Mild obstructive sleep apnea, defined as 5-14 apneas or hypopneas per hour slept, is common in older adults. Little is known about the effect on cognition of adherence to continuous positive airway pressure (CPAP) treatment of obstructive sleep apnea in older adults with mild obstructive sleep apnea and mild cognitive impairment. OBJECTIVE: The objective of this study was to explore the effect of CPAP adherence on cognition in older adults with mild obstructive sleep apnea and mild cognitive impairment. METHODS: We conducted a secondary analysis of data from Memories 1, a 1-year quasiexperimental clinical trial on the effect of CPAP adherence in older adults with mild cognitive impairment and obstructive sleep apnea. Those with mild obstructive sleep apnea were divided into two groups based on their CPAP adherence over 1 year: (a) CPAP adherent group (mild cognitive impairment + CPAP) with an average CPAP use of ≥4 hours per night and (b) CPAP nonadherent group (mild cognitive impairment - CPAP) with an average CPAP use of <4 hours per night. Individuals currently using CPAP were not eligible. A CPAP adherence intervention was provided for all participants, and an attention control intervention was provided for participants who chose to discontinue CPAP use during the 1-year follow-up. Descriptive baseline analyses, paired t tests for within-group changes, and general linear and logistic regression models for between-group changes were conducted. RESULTS: Those in the mild cognitive impairment + CPAP group compared to the mild cognitive impairment - CPAP group demonstrated a significant improvement in psychomotor/cognitive processing speed, measured by the Digit Symbol Coding Test. Eight participants improved on the Clinical Dementia Rating Scale, whereas six worsened or were unchanged. Twelve participants rated themselves as improved on the Alzheimer's Disease Cooperative Study-Clinical Global Impression of Change Scale, whereas three reported their status as worsened or unchanged. The mild cognitive impairment + CPAP group had greater than an eightfold increased odds of improving on the Clinical Dementia Rating and greater than a ninefold increased odds of improving on the Alzheimer's Disease Cooperative Study-Clinical Global Impression of Change Scale, compared to the mild cognitive impairment - CPAP group. DISCUSSION: CPAP adherence may be a promising intervention for slowing cognitive decline in older adults with mild obstructive sleep apnea and mild cognitive impairment. A larger, adequately powered study is needed.

---

### PMID 32045010 — current stance: `supports`

**Golden note:** OSA AD risk real-world — treated patients had lower AD risk.

**Risk of Alzheimer's Disease in Obstructive Sleep Apnea Patients With or Without Treatment: Real-World Evidence.**

*The Laryngoscope*, 2020. Types: Evaluation Study; Journal Article; Research Support, Non-U.S. Gov't

> OBJECTIVE: To assess the risk of Alzheimer's disease (AD) in patients with obstructive sleep apnea (OSA) with or without treatment based on real-world evidence. STUDY DESIGN: Retrospective cohort study. METHODS: Patients newly diagnosed with OSA during 1997-2012 were identified using the National Health Insurance Research Database of Taiwan. Patients without OSA were randomly selected and matched in a 1:4 ratio by age, sex, urbanization level, and income. All patients were followed up until death or the end of 2013. The primary outcome was AD occurrence. RESULTS: This study included 3,978 OSA patients and 15,912 non-OSA patients. OSA was independently and significantly associated with a higher incidence of AD in an adjusted Cox proportional hazard model (adjusted hazard ratio: 2.12; 95% confidence interval [CI], 1.27-3.56). The average period of AD detection from the time of OSA occurrence was 5.44 years (standard deviation: 2.96). Subgroup analyses revealed that the effect of OSA remained significant in patients aged ≥60 years, male subgroups, patients without CPAP or surgical treatment, and patients without pharmacological therapies. Patients with OSA who received treatment (continuous positive airway pressure or surgery) exhibited a significantly reduced risk of AD compared with those without treatment (incidence rate ratio 0.23, 95% CI, 0.06-0.98). CONCLUSION: OSA is independently associated with an increased risk of AD. Treatment for OSA reduces the AD risk in OSA patients. AD irreversibility renders OSA as a potential modifiable target for slowing or preventing the process of AD development. LEVEL OF EVIDENCE: IV Laryngoscope, 130:2292-2298, 2020.

---

