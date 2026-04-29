# Q17: Does estrogen replacement therapy initiated near menopause reduce later Alzheimer's risk?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=22 PMIDs.

**Current S/C/I**: 7 / 1 / 14
**Proposed S/C/I**: 5 / 0 / 17
**Net flips**: 5 (4 original + 1 added by reviewer)

Q17 is one of the most genuinely contested questions in the corpus
because the evidence really *is* split: observational data and the
"timing window" hypothesis support early-initiation benefit, while
RCTs in late-life initiation show null or harm. Most current labels
reflect this complexity correctly. A few flips bring borderline papers
into stricter alignment.

**Reviewer note (second pass):** All 4 originally proposed flips
confirmed. One additional flip added: `20840280` (narrative
"critical-period" review with no new clinical data) → `inconclusive`.
Borderline cases (`32057896`, `19160224`) flagged but kept as
`inconclusive` since each has a defensible mixed/out-of-scope reason.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `27163830` | 2016 | **contradicts → inconclusive** | KEEPS-AD PiB amyloid substudy, n=68. Verbatim: *"Women (age = 52-65) randomized to transdermal 17β-estradiol (n = 21) had **lower PiB SUVR** compared to placebo (n = 30) after adjusting for age [odds ratio (95% CI) = 0.31(0.11-0.83)]."* The substudy actually reports a **statistically significant amyloid reduction** with transdermal estradiol — that's a positive biomarker finding, not a contradicting one. The current `contradicts` label and note ("primary missed") don't match the abstract's actual finding. Per strict bar, this is biomarker-only (not a clinical-cognitive primary endpoint), so `inconclusive` fits best. |
| `10997480` | 2000 | **supports → inconclusive** | Estrogen + cerebral blood flow mechanism, n=12 women, 6-week pilot. Mechanism/biomarker (CBF) only, no cognitive primary, very small sample. Per strict bar, mechanism + small/pilot → `inconclusive`. |
| `39422947` | 2024 | **supports → inconclusive** | Phytoestrogen + AD meta. The findings are direction-mixed: *"Combination MHT should probably be prescribed for less than 5 years after menopause to reduce risk for AD, while estrogen alone should not be prescribed to women over 60."* The pooled findings show **increased AD risk** with combination MHT in some groups and no association with estrogen alone for younger women. Direction-mixed result; current `supports` overstates. → `inconclusive`. |
| `41618732` | 2026 | **inconclusive ✓** (keep, but note explicit null) | Long-term KEEPS amyloid PET/MRI 10 years post-trial, n=266. Verbatim: *"Aβ and structural MRI biomarkers were **not different** in the oCEE and tE2 groups compared to placebo. Apolipoprotein E ε4 status did not modify the findings."* Well-powered biomarker-null. Keep `inconclusive` (biomarker-only) but flag as a strong null for the timing-window hypothesis. |
| `20840280` | 2010 | **supports → inconclusive** (added by reviewer) | Narrative review proposing the "critical period" hypothesis. No new clinical data; reviews mechanistic/in-vivo studies suggesting "positive effects of estrogen are most robust in young women and in older women who had initiated ET around the time of menopause." Per strict bar, narrative review without primary clinical efficacy data → `inconclusive` rather than `supports`. The hypothesis is supported elsewhere by `40220453` (timing-window meta, RR 0.70 sig); this paper itself is a hypothesis-framing review. |

## Confirmed (no change)

- `9496988` (Yaffe 1998 — observational supports, controlled trials don't) — **inconclusive ✓**
- `34339416` (MHT umbrella — mixed across outcomes) — **inconclusive ✓**
- `19160224` (Cochrane HRT for cognition in dementia — explicitly says "not indicated for women with AD"; out of scope for prevention question) — **inconclusive ✓**
- `19468050` (HT and cognition SR — mixed by formulation/age) — **inconclusive ✓**
- `36834617` (HRT risk factor or therapeutic? — debate framing) — **inconclusive ✓**
- `32910516` (estrogen + brain structure SR — descriptive imaging) — **inconclusive ✓**
- `38501109` (MHT cognition meta — timing-near-menopause sig improves verbal memory; late-life null/worsens) — **inconclusive ✓**
- `32057896` (MHT-AD time-response meta — pooled OR 1.08 sig increase but timing-window subgroup) — **inconclusive ✓**
- `15511602` (Reproductive events RCT, n=10wk small) — **inconclusive ✓**
- `14520653` (DS earlier menopause → earlier AD) — **supports ✓** (estrogen-loss hypothesis)
- `16926067` (DS bioavailable estradiol delays AD) — **supports ✓**
- `23418430` (APOE-ε4 + cell aging mid-life HT users) — **inconclusive ✓**
- `33110037` (cognitive complaints + GM volume cross-sectional) — **inconclusive ✓**
- `34342862` (HT in postmenop AD SR — conflicting) — **inconclusive ✓**
- `40220453` (MHT timing meta, n=7.7M — initiation within 5y of menopause RR 0.70 sig) — **supports ✓** (sig protective in timing-window subgroup)
- `37393661` (early menopause/POI → increased dementia meta) — **supports ✓**
- `17368974` (WHI risks commentary) — **inconclusive ✓**

## Borderline (kept as-is, flagged)

- **`32057896`** (time-response meta, 2020) — **policy (c) candidate**.
  Pooled OR 1.08 (95% CI 1.03–1.14) sig *increase* in AD risk overall
  with MHT; combined estrogen+progestogen drives this. Could be argued
  as `contradicts` for the broad question. Kept as `inconclusive`
  because the same paper identifies a non-linear time-response with
  the timing-window hypothesis preserved (direction shifts after 5
  years), making this genuinely mixed within one paper.
- **`19160224`** (Cochrane HRT for cognition in dementia, 2009) —
  Concludes "HRT or ERT for cognitive improvement or maintenance is
  not indicated for women with AD." This is a meta concluding "no
  efficacy" — meets `contradicts` bar — BUT scope is treatment of
  established AD, not prevention near menopause. Kept as
  `inconclusive` (out-of-scope for the prevention question), with
  note that it would be `contradicts` for a treatment-focused query.
- **`34339416`** (umbrella review, 2021) — "ET and EPT had opposite
  effects for ... Alzheimer disease." Single sentence, formulation-
  dependent direction; defensible as `inconclusive`.

## Cross-cutting issues

- **The timing-window hypothesis is the central tension**: observational
  data and timing-stratified meta-analyses (`40220453`, `38501109`,
  `32057896`) suggest early-initiation MHT is protective, while
  late-life initiation RCTs (KEEPS biomarker substudies `27163830`
  and `41618732`) show null effects. The question specifically asks
  about "near menopause" — i.e., the timing-window subgroup — so
  papers like `40220453` (timing-window RR 0.70 sig) directly support
  it, while WHI-era late-initiation evidence is less directly relevant.
- **KEEPS substudies appear twice**: `27163830` (2016 amyloid PET) and
  `41618732` (2026 long-term PET/MRI follow-up) both report on the
  same KEEPS cohort. Same-cohort substudies should be tagged.
- **Down syndrome cohort appears twice**: `14520653` (2003) and
  `16926067` (2006) both from the New York State DD service system
  cohort, same first authors. Same-cohort findings.
- **Recurring policy issues touched by Q17:**
  - **(b) preclinical/mech-dominated review labeled `supports`** —
    `20840280` (critical-period review) was a `supports` based on
    in-vivo neurobiology mechanism evidence, not clinical efficacy.
    Flipped to `inconclusive`.
  - **(c) missed primary with significant secondary** — `27163830`
    KEEPS-AD: parent KEEPS missed cognitive primary, but this
    biomarker substudy reports significant amyloid reduction.
    Currently `contradicts` is wrong (substudy result is positive,
    not negative); flipped to `inconclusive` since it's biomarker-
    only and labeled a pilot.
- After flips: 5/0/17 — slight shift toward more `inconclusive`, but
  the genuinely contested nature of this question is preserved.

## Highest-confidence flips for this question

- `27163830` contradicts → inconclusive — the abstract reports
  *significant* amyloid reduction with transdermal estradiol; the
  current label and note both misread this as a contradicting finding.
- `10997480` supports → inconclusive — n=12 mechanism/CBF pilot,
  no cognitive primary.
- `20840280` supports → inconclusive — narrative review proposing
  the critical-period hypothesis; no new clinical efficacy data,
  argues from mechanistic in-vivo studies.

## signal_types (annotation layer)

Tags reflect *paper-level caveats* that affect how each pmid should
be weighted in a strict-bar reading of the literature. Tags do not
change stance labels — they document why a label is what it is, or
flag papers that should be down-weighted in headline counts.

### Proposed new tags (Q17)

- **`timing_window_subgroup`** — paper's primary finding is in a
  pre-defined timing-window subgroup (e.g., MHT initiation within
  5 years of menopause), distinct from a general MHT effect. Used
  when the timing-window subgroup is the answer to the question
  but the parent finding may differ. Q17 specifically asks about
  near-menopause initiation, so timing-window subgroup positives
  here are the *primary* relevant finding, not a `subgroup_positive`
  caveat. (Distinct from generic `subgroup_positive` because the
  subgroup matches the question's scope.)
- **`indirect_endogenous_estrogen`** — paper studies *endogenous*
  estrogen variation (age at menopause, bioavailable estradiol,
  POI) rather than *exogenous* hormone replacement. Supports the
  estrogen-loss hypothesis but does not directly answer whether
  HRT reduces AD risk. Useful caveat for Q17 specifically.
- **`down_syndrome_cohort`** — finding is in Down syndrome
  population (early menopause, early AD onset). Mechanistically
  informative but population is not "women initiating HRT near
  menopause" in the typical sense.
- **`out_of_scope_treatment_not_prevention`** — paper addresses
  treatment of established AD, not primary prevention near
  menopause. Relevant for Q17 because some retrieved papers are
  treatment trials in AD patients.

### Tag assignments

- `9496988` (Yaffe 1998 meta) — `hedged_meta`, `narrative_review`
  (mechanism + meta blend; conclusion: "we do not recommend estrogen
  for the prevention or treatment ... until adequate trials have
  been completed").
- `34339416` (umbrella review 2021) — `hedged_meta`,
  `broad_scope_review`, `split_outcome` (ET vs EPT have opposite
  effects on AD).
- `19160224` (Cochrane HRT in dementia 2009) — `hedged_meta`,
  `out_of_scope_treatment_not_prevention`, `wrong_population`
  (women with established AD, not near-menopause).
- `27163830` (KEEPS-AD amyloid 2016) — `pilot_positive`,
  `biomarker_only`, `same_cohort_duplicate` (KEEPS), `subgroup_apoe_split`,
  `missed_primary_sig_secondary` (parent KEEPS cognitive primary
  null; this substudy reports sig amyloid reduction).
- `19468050` (HT and cognition SR 2009) — `hedged_meta`,
  `split_outcome` (ET helpful, CEE+MPA harmful).
- `20840280` (critical-period review 2010) — `narrative_review`,
  `mechanism_only`, `preclinical_dominated`.
- `10997480` (CBF mechanism 2000) — `pilot_positive`,
  `biomarker_only`, `mechanism_only`, `short_duration` (6 weeks),
  `case_series_underpowered` (n=12).
- `36834617` (HRT debate review 2023) — `narrative_review`,
  `hedged_meta`, `broad_scope_review`.
- `32910516` (estrogen + brain structure 2020) — `biomarker_only`,
  `observational_only`, `uncontrolled_observational` (cross-sectional
  voxelwise on self-reported HT use).
- `38501109` (MHT cognition meta 2024) — `hedged_meta`,
  `split_outcome`, `timing_window_subgroup` (midlife verbal memory
  improved; late-life null/worse).
- `32057896` (time-response meta 2020) — `hedged_meta`,
  `split_outcome`, `timing_window_subgroup`,
  `directionally_opposite_finding` (overall pooled OR 1.08 *increase*,
  but timing-window protective).
- `15511602` (n=10wk RCT 2005) — `pilot_positive`, `short_duration`,
  `case_series_underpowered`, `subgroup_positive` (only "years since
  menopause" stratification reaches sig).
- `14520653` (DS menopause→AD 2003) — `down_syndrome_cohort`,
  `indirect_endogenous_estrogen`, `same_cohort_duplicate` (NY State
  DD cohort), `observational_only`.
- `16926067` (DS bioavailable E2 2006) — `down_syndrome_cohort`,
  `indirect_endogenous_estrogen`, `same_cohort_duplicate` (NY State
  DD cohort), `observational_only`.
- `23418430` (APOE-ε4 telomere mid-life 2013) — `biomarker_only`,
  `mechanism_only`, `subgroup_apoe_split`, `case_series_underpowered`
  (n=63).
- `33110037` (cognitive complaints + GM volume 2020) — `biomarker_only`,
  `uncontrolled_observational`, `case_series_underpowered` (n=44),
  `tangential_stratification`.
- `34342862` (HT in postmenop AD SR 2021) — `hedged_meta`,
  `split_outcome`, `out_of_scope_treatment_not_prevention` (mixes
  observational on prevention with trials in AD patients).
- `40220453` (MHT timing meta 2025, n=7.7M) — `timing_window_subgroup`,
  `split_outcome` (estrogen alone protective in subgroup;
  combination/progestogen-only increases risk).
- `39422947` (phytoestrogen meta 2024) — `hedged_meta`,
  `split_outcome`, `timing_window_subgroup`,
  `directionally_opposite_finding` (combination MHT *increases* AD
  risk; estrogen alone neutral for younger, harmful for older).
- `41618732` (KEEPS long-term 2026) — `biomarker_only`,
  `same_cohort_duplicate` (KEEPS), `landmark_no_group_difference`.
- `37393661` (POI/early menopause meta 2023) — `hedged_meta`,
  `indirect_endogenous_estrogen`, `observational_only` (sensitivity
  analysis loses sig after one cohort excluded — flagged as fragile).
- `17368974` (WHI risks commentary 2007) — `commentary`,
  `narrative_review`.

### Tag distribution (22 pmids, multi-tag)

- `hedged_meta`: 9
- `split_outcome`: 7
- `biomarker_only`: 6
- `narrative_review`: 5
- `same_cohort_duplicate`: 4
- `timing_window_subgroup`: 4 (new tag)
- `observational_only`: 4
- `case_series_underpowered`: 4
- `mechanism_only`: 3
- `indirect_endogenous_estrogen`: 3 (new tag)
- `pilot_positive`: 3
- `out_of_scope_treatment_not_prevention`: 3 (new tag)
- `subgroup_apoe_split`: 2
- `directionally_opposite_finding`: 2
- `down_syndrome_cohort`: 2 (new tag)
- `uncontrolled_observational`: 2
- `short_duration`: 2
- `broad_scope_review`: 2
- `wrong_population`: 1
- `missed_primary_sig_secondary`: 1
- `preclinical_dominated`: 1
- `subgroup_positive`: 1
- `tangential_stratification`: 1
- `landmark_no_group_difference`: 1
- `commentary`: 1

All 22 pmids tagged (≥1 tag each).

---

## Abstracts (n=22)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 9496988 — current stance: `inconclusive`

**Evidence span:** > Studies conducted in women, however, have substantial methodologic problems and have produced conflicting results. Given the known risks of estrogen therapy, we do not recommend estrogen for the prevention or treatment of Alzheimer disease or other dementias until adequate trials have been completed.

**Golden note:** Yaffe 1998 review — observational supports, controlled trials don't.

**Estrogen therapy in postmenopausal women: effects on cognitive function and dementia.**

*JAMA*, 1998. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't

> CONTEXT: Several studies have suggested that estrogen replacement therapy in postmenopausal women improves cognition, prevents development of dementia, and improves the severity of dementia, while other studies have not found a benefit of estrogen use. OBJECTIVE: To determine whether postmenopausal estrogen therapy improves cognition, prevents development of dementia, or improves dementia severity. DATA SOURCES: We performed a literature search of studies published from January 1966 through June 1997, using MEDLINE, manually searched bibliographies of articles identified, and consulted experts. STUDY SELECTION: Studies that evaluated biological mechanisms of estrogen's effect on the central nervous system and studies that addressed the effect of estrogen on cognitive function or on dementia. DATA EXTRACTION: We reviewed studies for methods, sources of bias, and outcomes and performed a meta-analysis of the 10 studies of postmenopausal estrogen use and risk of dementia using standard meta-analytic methods. DATA SYNTHESIS: Biochemical and neurophysiologic studies suggest several mechanisms by which estrogen may affect cognition: promotion of cholinergic and serotonergic activity in specific brain regions, maintenance of neural circuitry, favorable lipoprotein alterations, and prevention of cerebral ischemia. Five observational studies and 8 trials have addressed the effect of estrogen on cognitive function in nondemented postmenopausal women. Cognition seems to improve in perimenopausal women, possibly because menopausal symptoms improve, but there is no clear benefit in asymptomatic women. Ten observational studies have measured the effect of postmenopausal estrogen use on risk of developing dementia. Meta-analysis of these studies suggests a 29% decreased risk of developing dementia among estrogen users, but the findings of the studies are heterogeneous. Four trials of estrogen therapy in women with Alzheimer disease have been conducted and have had primarily positive results, but most have been small, of short duration, non-randomized, and uncontrolled. CONCLUSIONS: There are plausible biological mechanisms by which estrogen might lead to improved cognition, reduced risk for dementia, or improvement in the severity of dementia. Studies conducted in women, however, have substantial methodologic problems and have produced conflicting results. Large placebo-controlled trials are required to address estrogen's role in prevention and treatment of Alzheimer disease and other dementias. Given the known risks of estrogen therapy, we do not recommend estrogen for the prevention or treatment of Alzheimer disease or other dementias until adequate trials have been completed.

---

### PMID 34339416 — current stance: `inconclusive`

**Evidence span:** > ET and EPT had opposite effects for endometrial cancer, endometrial hyperplasia, and Alzheimer disease.

**Golden note:** MHT umbrella review — mixed across outcomes.

**Menopausal hormone therapy and women's health: An umbrella review.**

*PLoS medicine*, 2021. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND: There remains uncertainty about the impact of menopausal hormone therapy (MHT) on women's health. A systematic, comprehensive assessment of the effects on multiple outcomes is lacking. We conducted an umbrella review to comprehensively summarize evidence on the benefits and harms of MHT across diverse health outcomes. METHODS AND FINDINGS: We searched MEDLINE, EMBASE, and 10 other databases from inception to November 26, 2017, updated on December 17, 2020, to identify systematic reviews or meta-analyses of randomized controlled trials (RCTs) and observational studies investigating effects of MHT, including estrogen-alone therapy (ET) and estrogen plus progestin therapy (EPT), in perimenopausal or postmenopausal women in all countries and settings. All health outcomes in previous systematic reviews were included, including menopausal symptoms, surrogate endpoints, biomarkers, various morbidity outcomes, and mortality. Two investigators independently extracted data and assessed methodological quality of systematic reviews using the updated 16-item AMSTAR 2 instrument. Random-effects robust variance estimation was used to combine effect estimates, and 95% prediction intervals (PIs) were calculated whenever possible. We used the term MHT to encompass ET and EPT, and results are presented for MHT for each outcome, unless otherwise indicated. Sixty systematic reviews were included, involving 102 meta-analyses of RCTs and 38 of observational studies, with 102 unique outcomes. The overall quality of included systematic reviews was moderate to poor. In meta-analyses of RCTs, MHT was beneficial for vasomotor symptoms (frequency: 9 trials, 1,104 women, risk ratio [RR] 0.43, 95% CI 0.33 to 0.57, p < 0.001; severity: 7 trials, 503 women, RR 0.29, 95% CI 0.17 to 0.50, p = 0.002) and all fracture (30 trials, 43,188 women, RR 0.72, 95% CI 0.62 to 0.84, p = 0.002, 95% PI 0.58 to 0.87), as well as vaginal atrophy (intravaginal ET), sexual function, vertebral and nonvertebral fracture, diabetes mellitus, cardiovascular mortality (ET), and colorectal cancer (EPT), but harmful for stroke (17 trials, 37,272 women, RR 1.17, 95% CI 1.05 to 1.29, p = 0.027) and venous thromboembolism (23 trials, 42,292 women, RR 1.60, 95% CI 0.99 to 2.58, p = 0.052, 95% PI 1.03 to 2.99), as well as cardiovascular disease incidence and recurrence, cerebrovascular disease, nonfatal stroke, deep vein thrombosis, gallbladder disease requiring surgery, and lung cancer mortality (EPT). In meta-analyses of observational studies, MHT was associated with decreased risks of cataract, glioma, and esophageal, gastric, and colorectal cancer, but increased risks of pulmonary embolism, cholelithiasis, asthma, meningioma, and thyroid, breast, and ovarian cancer. ET and EPT had opposite effects for endometrial cancer, endometrial hyperplasia, and Alzheimer disease. The major limitations include the inability to address the varying effects of MHT by type, dose, formulation, duration of use, route of administration, and age of initiation and to take into account the quality of individual studies included in the systematic reviews. The study protocol is publicly available on PROSPERO (CRD42017083412). CONCLUSIONS: MHT has a complex balance of benefits and harms on multiple health outcomes. Some effects differ qualitatively between ET and EPT. The quality of available evidence is only moderate to poor.

---

### PMID 19160224 — current stance: `inconclusive`

**Evidence span:** > Currently, HRT or ERT for cognitive improvement or maintenance is not indicated for women with AD.

**Golden note:** Cochrane HRT for cognition in dementia — insufficient evidence.

**Hormone replacement therapy to maintain cognitive function in women with dementia.**

*The Cochrane database of systematic reviews*, 2009. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: As estrogens have been shown to have several potentially beneficial effects on the central nervous system, it is biologically plausible that maintaining high levels of estrogens in postmenopausal women by means of estrogen replacement therapy (ERT) could be protective against cognitive decline in women with Alzheimer's disease (AD) or other dementia syndromes. OBJECTIVES: To investigate the effects of ERT (estrogens only) or HRT (estrogens combined with a progestagen) compared with placebo in randomized controlled trials (RCTs) on cognitive function of postmenopausal women with dementia. SEARCH STRATEGY: The Cochrane Dementia and Cognitive Improvement Group Specialized Register, which contains records from many medical databases, The Cochrane Library, EMBASE, MEDLINE, CINAHL, PsycINFO and LILACS were searched on 7 November 2007 using the terms ORT, PORT, ERT, HRT, estrogen*, oestrogen* and progesterone*. SELECTION CRITERIA: All double-blind randomized controlled trials (RCTs) into the effect of ERT or HRT for cognitive function with a treatment period of at least two weeks in postmenopausal women with AD or other types of dementia. DATA COLLECTION AND ANALYSIS: Abstracts of the references retrieved by the searches were read by two reviewers (EH and KY) independently in order to discard those that were clearly not eligible for inclusion. The two reviewers studied the full text of the remaining references and independently selected studies for inclusion. Any disparity in the ensuing lists was resolved by discussion with all reviewers in order to arrive at the final list of included studies. The selection criteria ensured that the blinding and randomization of the included studies was adequate. The two reviewers also assessed the quality of other aspects of the included trials. One reviewer (EH) extracted the data from the studies, but was aided and checked by JB from Cochrane. MAIN RESULTS: A total of seven trials including 351 women with AD were analysed. Because different drugs were used at different studies it was not possible to combine more than two studies in any analysis.On a clinical global rating, clinicians scored patients taking CEE as significantly worse compared with the placebo group on the Clinical Dementia Rating scale after 12 months (overall WMD = 0.35, 95% CI = 0.01 to 0.69, z = 1.99, P < 0.05).Patients taking CEE had a worse performance on the delayed recall of the Paragraph Test (overall WMD = -0.45, 95% CI = -0.79 to -0.11, z = 2.60, P < 0.01) after one month than those taking placebo. They had a worse performance on Finger Tapping after 12 months (WMD = -3.90, 95% CI = -7.85 to 0.05, z = 1.93, P < 0.05).Limited positive effects were found for the lower dosage of CEE (0.625 mg/day) which showed a significant improvement in MMSE score only when assessed at two months, and disappeared after correction for multiple testing. No significant effects for MMSE were found at longer end points (3, 6 and 12 months of treatment). With a dosage of 1.25 mg/d CEE, short-term significant effects were found for Trial-Making test B at one month and Digit Span backward at four months. After two months of transdermal diestradiol (E2) treatment, a highly significant effect was observed for the word recall test (WMD = 6.50, 95% CI = 4.04 to 8.96, z = 5.19, P < 0.0001). No other significant effects were found for other outcomes measured. AUTHORS' CONCLUSIONS: Currently, HRT or ERT for cognitive improvement or maintenance is not indicated for women with AD.

---

### PMID 27163830 — current stance: `contradicts`

**Evidence span:** > Women (age = 52-65) randomized to transdermal 17β-estradiol (n = 21) had lower PiB SUVR compared to placebo (n = 30) after adjusting for age [odds ratio (95% CI) = 0.31(0.11-0.83)].

**Golden note:** KEEPS-AD RCT — recently postmenopausal women on transdermal estradiol; no effect on amyloid deposition. Pivotal test of timing-window hypothesis, primary missed.

**Early Postmenopausal Transdermal 17β-Estradiol Therapy and Amyloid-β Deposition.**

*Journal of Alzheimer's disease : JAD*, 2016. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't; Research Support, N.I.H., Extramural

> BACKGROUND: It remains controversial whether hormone therapy in recently postmenopausal women modifies the risk of Alzheimer's disease (AD). OBJECTIVE: To investigate the effects of hormone therapy on amyloid-β deposition in recently postmenopausal women. METHODS: Participants within 5-36 months past menopause in the Kronos Early Estrogen Prevention Study, a randomized, double blinded placebo-controlled clinical trial, were randomized to: 1) 0.45 mg/day oral conjugated equine estrogens (CEE); 2) 50μg/day transdermal 17β-estradiol; or 3) placebo pills and patch for four years. Oral progesterone (200 mg/day) was given to active treatment groups for 12 days each month. 11C Pittsburgh compound B (PiB) PET imaging was performed in 68 of the 118 participants at Mayo Clinic approximately seven years post randomization and three years after stopping randomized treatment. PiB Standard unit value ratio (SUVR) was calculated. RESULTS: Women (age = 52-65) randomized to transdermal 17β-estradiol (n = 21) had lower PiB SUVR compared to placebo (n = 30) after adjusting for age [odds ratio (95% CI) = 0.31(0.11-0.83)]. In the APOEɛ4 carriers, transdermal 17β-estradiol treated women (n = 10) had lower PiB SUVR compared to either placebo (n = 5) [odds ratio (95% CI) = 0.04(0.004-0.44)], or the oral CEE treated group (n = 3) [odds ratio (95% CI) = 0.01(0.0006-0.23)] after adjusting for age. Hormone therapy was not associated with PiB SUVR in the APOEɛ4 non-carriers. CONCLUSION: In this pilot study, transdermal 17β-estradiol therapy in recently postmenopausal women was associated with a reduced amyloid-β deposition, particularly in APOEɛ4 carriers. This finding may have important implications for the prevention of AD in postmenopausal women, and needs to be confirmed in a larger sample.

---

### PMID 19468050 — current stance: `inconclusive`

**Evidence span:** > There is some evidence for a beneficial effect of estrogen alone on verbal memory in younger naturally post-menopausal women... There is stronger evidence of a detrimental effect of conjugated equine estrogen plus medroxyprogesterone acetate on verbal memory in younger and older post-menopausal women.

**Golden note:** HT and cognition — discrepant trial information.

**Hormone therapy and cognitive function.**

*Human reproduction update*, 2009. Types: Journal Article; Research Support, N.I.H., Extramural; Systematic Review

> BACKGROUND: Clinical trials yield discrepant information about the impact of hormone therapy on verbal memory and executive function. This issue is clinically relevant because declines in verbal memory are the earliest predictor of Alzheimer's disease and declines in executive function are central to some theories of normal, age-related changes in cognition. METHODS: We conducted a systematic review of randomized clinical trials of hormone therapy (i.e. oral, transdermal, i.m.) and verbal memory, distinguishing studies in younger (i.e. <or=65 years of age; n = 9) versus older (i.e. >65 years; n = 7) women and studies involving estrogen alone versus estrogen plus progestogen. Out of 32 placebo-controlled trials, 17 were included (13 had no verbal memory measures and 2 involved cholinergic manipulations). We also provide a narrative review of 25 studies of executive function (two trials), since there are insufficient clinical trial data for systematic review. RESULTS: There is some evidence for a beneficial effect of estrogen alone on verbal memory in younger naturally post-menopausal women and more consistent evidence from small-n studies of surgically post-menopausal women. There is stronger evidence of a detrimental effect of conjugated equine estrogen plus medroxyprogesterone acetate on verbal memory in younger and older post-menopausal women. Observational studies and pharmacological models of menopause provide initial evidence of improvements in executive function with hormone therapy. CONCLUSIONS: Future studies should include measures of executive function and should address pressing clinical questions; including what formulation of combination hormone therapy is cognitively neutral/beneficial, yet effective in treating hot flashes in the early post-menopause.

---

### PMID 20840280 — current stance: `supports`

**Evidence span:** > Consistent with the "critical period" hypothesis, these studies suggest that the positive effects of estrogen are most robust in young women and in older women who had initiated ET around the time of menopause.

**Golden note:** Critical-period hypothesis — early initiation may reduce AD risk.

**Estrogen therapy and Alzheimer's dementia.**

*Annals of the New York Academy of Sciences*, 2010. Types: Evaluation Study; Journal Article; Review

> Previous studies in postmenopausal women have reported that estrogen treatment (ET) modulates the risk for developing Alzheimer's disease (AD). It has recently been hypothesized that there may be a "critical period" around the time of menopause during which the prescription of ET may reduce the risk of developing AD in later life. This effect may be most significant in women under 49 years old. Furthermore, prescription of ET after this point may have a neutral or negative effect, particularly when initiated in women over 60-65 years old. In this paper, we review recent studies that use in vivo techniques to analyze the neurobiological mechanisms that might underpin estrogen's effects on the brain postmenopause. Consistent with the "critical period" hypothesis, these studies suggest that the positive effects of estrogen are most robust in young women and in older women who had initiated ET around the time of menopause.

---

### PMID 10997480 — current stance: `supports`

**Evidence span:** > Twelve healthy menopausal women experiencing daily hot flushes and not on ERT were recruited to participate in a clinical study. There was a global improvement in CBF associated with ERT, an average gain of 22% over baseline.

**Golden note:** Estrogen + CBF mechanism review — proposes protective mechanism.

**Estrogen and cerebral blood flow: a mechanism to explain the impact of estrogen on the incidence and treatment of Alzheimer's disease.**

*International journal of fertility and women's medicine*, 2000. Types: Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> OBJECTIVE: Women are three times as likely to develop late-onset Alzheimer's Disease (AD) as are age-matched men. In the perimenopausal period, women typically have profound hypoestrogenism associated with vasomotor episodes. The pattern of AD development in women resembles the hormonal changes that occur in the perimenopausal period; the risk of AD is lower in menopausal women taking estrogen replacement therapy (ERT), and ERT is associated with clinical improvement in AD patients. Further, ERT has been shown to augment the therapeutic benefits of medications designed to treat AD. To understand better the relationship between ERT, hot flushes and AD, a pilot study was conducted at UCLA-Harbor Medical Center. PATIENTS AND METHODS: Twelve healthy menopausal women experiencing daily hot flushes and not on ERT were recruited to participate in a clinical study. Each patient underwent regional cerebral blood flow (CBF) measurement using single-photon emission computed tomography (SPECT) at baseline and during a hot flush episode. Patients were then randomized to receive either 0.625 mg or 1.25 mg conjugated equine estrogens (CEE) daily. During the sixth week of ERT, each patient had a repeat SPECT study. Baseline SPECT data were compared with ERT data. RESULTS: Baseline examinations demonstrated CBF patterns commonly seen in patients with Alzheimer's disease. There was a global improvement in CBF associated with ERT, an average gain of 22% over baseline. Improvements were most dramatic in the temporal and parietal regions of the brain. The cortical CBF demonstrated a mean increase of 9.2 mL/100 g/min (P < .01). CONCLUSIONS: CBF is diminished in hypoestrogenic women, with regional patterns resembling those of patients with mild to moderate AD. Cerebral circulation tends to be further compromised during hot flush episodes. This mechanism could be the initiating event in the metabolic process that results in dementia of the Alzheimer's type, and thus serve as the link between hypoestrogenism and neurodegenerative diseases. In this study, ERT reversed these detrimental blood flow changes back to a normal pattern after only 6 weeks of CEE therapy. With improved blood flow, the brain is protected from the metabolic injury associated with hypoxia. The study is currently being repeated with a larger population.

---

### PMID 36834617 — current stance: `inconclusive`

**Evidence span:** > The literature suggests that estrogens have a clear role in modulating dementia risk, with reliable evidence showing that HRT can have both a beneficial and a deleterious effect.

**Golden note:** 'HRT risk factor or therapeutic option?' — debate framing.

**Is Hormone Replacement Therapy a Risk Factor or a Therapeutic Option for Alzheimer's Disease?**

*International journal of molecular sciences*, 2023. Types: Systematic Review; Journal Article

> Alzheimer's disease (AD) is a progressive neurodegenerative disorder that accounts for more than half of all dementia cases in the elderly. Interestingly, the clinical manifestations of AD disproportionately affect women, comprising two thirds of all AD cases. Although the underlying mechanisms for these sex differences are not fully elucidated, evidence suggests a link between menopause and a higher risk of developing AD, highlighting the critical role of decreased estrogen levels in AD pathogenesis. The focus of this review is to evaluate clinical and observational studies in women, which have investigated the impact of estrogens on cognition or attempted to answer the prevailing question regarding the use of hormone replacement therapy (HRT) as a preventive or therapeutic option for AD. The articles were retrieved through a systematic review of the databases: OVID, SCOPUS, and PubMed (keywords "memory", "dementia," "cognition," "Alzheimer's disease", "estrogen", "estradiol", "hormone therapy" and "hormone replacement therapy" and by searching reference sections from identified studies and review articles). This review presents the relevant literature available on the topic and discusses the mechanisms, effects, and hypotheses that contribute to the conflicting findings of HRT in the prevention and treatment of age-related cognitive deficits and AD. The literature suggests that estrogens have a clear role in modulating dementia risk, with reliable evidence showing that HRT can have both a beneficial and a deleterious effect. Importantly, recommendation for the use of HRT should consider the age of initiation and baseline characteristics, such as genotype and cardiovascular health, as well as the dosage, formulation, and duration of treatment until the risk factors that modulate the effects of HRT can be more thoroughly investigated or progress in the development of alternative treatments can be made.

---

### PMID 32910516 — current stance: `inconclusive`

**Evidence span:** > Undesirable side effects of hormone variations emphasize a role for hormone therapy (HT) where possible benefits include a delay in the onset of dementia-yet findings are inconsistent.

**Golden note:** Estrogen + brain structure review — findings inconsistent.

**Estrogen, brain structure, and cognition in postmenopausal women.**

*Human brain mapping*, 2020. Types: Journal Article; Multicenter Study; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> Declining estrogen levels before, during, and after menopause can affect memory and risk for Alzheimer's disease. Undesirable side effects of hormone variations emphasize a role for hormone therapy (HT) where possible benefits include a delay in the onset of dementia-yet findings are inconsistent. Effects of HT may be mediated by estrogen receptors found throughout the brain. Effects may also depend on lifestyle factors, timing of use, and genetic risk. We studied the impact of self-reported HT use on brain volume in 562 elderly women (71-94 years) with mixed cognitive status while adjusting for aforementioned factors. Covariate-adjusted voxelwise linear regression analyses using a model with 16 predictors showed HT use as positively associated with regional brain volumes, regardless of cognitive status. Examinations of other factors related to menopause, oophorectomy and hysterectomy status independently yielded positive effects on brain volume when added to our model. One interaction term, HTxBMI, out of several examined, revealed significant negative association with overall brain volume, suggesting a greater reduction in brain volume than BMI alone. Our main findings relating HT to regional brain volume were as hypothesized, but some exploratory analyses were not in line with existing hypotheses. Studies suggest lower levels of estrogen resulting from oophorectomy and hysterectomy affect brain volume negatively, and the addition of HT modifies the relation between BMI and brain volume positively. Effects of HT may depend on the age range assessed, motivating studies with a wider age range as well as a randomized design.

---

### PMID 38501109 — current stance: `inconclusive`

**Evidence span:** > When initiated specifically in midlife or close to menopause onset, estrogen therapy was associated with improved verbal memory (SMD=0.394, 95% CI 0.014, 0.774; P=0.046), while late-life initiation had no effects.

**Golden note:** MHT cognition meta — controversial.

**Systematic review and meta-analysis of the effects of menopause hormone therapy on cognition.**

*Frontiers in endocrinology*, 2024. Types: Journal Article; Meta-Analysis; Systematic Review

> INTRODUCTION: Despite evidence from preclinical studies suggesting estrogen's neuroprotective effects, the use of menopausal hormone therapy (MHT) to support cognitive function remains controversial. METHODS: We used random-effect meta-analysis and multi-level meta-regression to derive pooled standardized mean difference (SMD) and 95% confidence intervals (C.I.) from 34 randomized controlled trials, including 14,914 treated and 12,679 placebo participants. RESULTS: Associations between MHT and cognitive function in some domains and tests of interest varied by formulation and treatment timing. While MHT had no overall effects on cognitive domain scores, treatment for surgical menopause, mostly estrogen-only therapy, improved global cognition (SMD=1.575, 95% CI 0.228, 2.921; P=0.043) compared to placebo. When initiated specifically in midlife or close to menopause onset, estrogen therapy was associated with improved verbal memory (SMD=0.394, 95% CI 0.014, 0.774; P=0.046), while late-life initiation had no effects. Overall, estrogen-progestogen therapy for spontaneous menopause was associated with a decline in Mini Mental State Exam (MMSE) scores as compared to placebo, with most studies administering treatment in a late-life population (SMD=-1.853, 95% CI -2.974, -0.733; P = 0.030). In analysis of timing of initiation, estrogen-progestogen therapy had no significant effects in midlife but was associated with improved verbal memory in late-life (P = 0.049). Duration of treatment >1 year was associated with worsening in visual memory as compared to shorter duration. Analysis of individual cognitive tests yielded more variable results of positive and negative effects associated with MHT. DISCUSSION: These findings suggest time-dependent effects of MHT on certain aspects of cognition, with variations based on formulation and timing of initiation, underscoring the need for further research with larger samples and more homogeneous study designs.

---

### PMID 32057896 — current stance: `inconclusive`

**Evidence span:** > Pooled results with random effect model showed a significant association between hormone therapy and Alzheimer's disease (OR 1.08, 95 % CI 1.03-1.14, I2: 69 %). However, the association appears to shift in direct after five years in the context of Alzheimer's disease, adding further weight to the critical window or timing hypothesis.

**Golden note:** MHT-AD/dementia/PD time-response meta — controversial.

**Postmenopausal hormone therapy and Alzheimer's disease, dementia, and Parkinson's disease: A systematic review and time-response meta-analysis.**

*Pharmacological research*, 2020. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> Hormone therapy continues to be a favourable option in the management of menopausal symptomatology, but the associated risk-benefit ratios with respect to neurodegenerative diseases remain controversial. The study aim was to determine the relation between menopausal hormone therapy and Alzheimer's disease, dementia, and Parkinson's disease in human subjects. A literature search was performed in PubMed/Medline, Cochrane collaboration, and Scopus databases from onset of the database to September 2019. Random-effects model was used to estimate pooled odd ratio (OR) and 95 % confidence intervals (CI). Subgroup analysis was performed based on the type and formulation of hormone. In addition, the time-response effect of this relationship was also assessed based on duration of hormone therapy. Associations between hormone therapy and Alzheimer's disease, dementia, and Parkinson's disease in menopausal women were reported in 28 studies. Pooled results with random effect model showed a significant association between hormone therapy and Alzheimer's disease (OR 1.08, 95 % CI 1.03-1.14, I2: 69 %). This relationship was more pronounced in patients receiving the combined estrogen-progestogen formulation. Moreover, a significant non-linear time-response association between hormone therapy and Alzheimer's disease was also identified (Coef1 = 0.0477, p1<0.001; Coef2 = -0.0932, p2<0.001). Similarly, pooled analysis revealed a significant association between hormone therapy and all-cause dementia (OR 1.16, 95 % CI 1.02-1.31, I2: 19 %). Interestingly, no comparable relationship was uncovered between hormone therapy as a whole and Parkinson's disease (OR 1.14, 95 % CI 0.95-1.38, I2: 65 %); however, sub-group analysis revealed a significant relationship between the disease and progestogen (OR 3.41, 95 % CI 1.23-9.46) or combined estrogen-progestogen formulation use (OR 1.49, 95 % CI 1.34-1.65). Indeed, this association was also found to be driven by duration of exposure (Coef1 = 0.0626, p1 = 0.04). This study reveals a significant direct relationship between the use of certain hormonal therapies and Alzheimer's disease, all-cause dementia, and Parkinson's disease in menopausal women. However, the association appears to shift in direct after five years in the context of Alzheimer's disease, adding further weight to the critical window or timing hypothesis of neurodegeneration and neuroprotection.

---

### PMID 15511602 — current stance: `inconclusive`

**Evidence span:** > Results indicate that while little overall beneficial effect of estrogen was found, years since menopause was significantly related to change in executive functioning in the estrogen but not the placebo group, such that more recently postmenopausal women demonstrated greater positive change than older women.

**Golden note:** Reproductive events modify ERT cognitive effects — moderator framing.

**Reproductive events modify the effects of estrogen replacement therapy on cognition in healthy postmenopausal women.**

*Psychoneuroendocrinology*, 2005. Types: Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.

> The question of whether estrogen replacement therapy (ERT) is beneficial to cognitive functioning in postmenopausal women has become controversial in the past several years. Early studies suggested that ERT improved cognitive functioning and decreased the risk of Alzheimer's disease, but recent studies have failed to find any benefit. However, studies have varied in terms of the age of participants, the estrogen preparation used, whether progesterone is administered concurrently, and the study design. The present study used a randomized, placebo-controlled design and a transdermal estrogen preparation composed of 17-beta estradiol. A neuropsychological battery was administered at baseline and after completion of the 10-week trial, and test scores were grouped into four composite scores using psychometric techniques. Baseline to follow-up change was analyzed using multiple regression techniques. Results indicate that while little overall beneficial effect of estrogen was found, years since menopause was significantly related to change in executive functioning in the estrogen but not the placebo group, such that more recently postmenopausal women demonstrated greater positive change than older women. Body mass index, a gross estimate of circulating estrogen, was significantly positively related to change in attentional and psychomotor processes regardless of treatment group, and to a weaker extent, verbal memory, but only in the estrogen-treated group. These results suggest that reproductive events and levels of endogenous estrogen are related to the clinical response to ERT, but larger studies with longer follow-up periods are needed to determine the strength of these effects.

---

### PMID 14520653 — current stance: `supports`

**Evidence span:** > Women with early onset of menopause (46 years or younger) had earlier onset and increased risk of Alzheimer's disease (AD) compared with women with onset of menopause after 46 years (rate ratio, 2.7; 95% confidence interval [CI], 1.2-5.9).

**Golden note:** Earlier menopause → earlier AD onset in Down syndrome — supports estrogen-loss hypothesis.

**Onset of dementia is associated with age at menopause in women with Down's syndrome.**

*Annals of neurology*, 2003. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't; Research Support, U.S. Gov't, P.H.S.

> Women with Down's syndrome experience early onset of both menopause and Alzheimer's disease. This timing provides an opportunity to examine the influence of endogenous estrogen deficiency, indicated by age at menopause, on risk of Alzheimer's disease. A community-based sample of 163 postmenopausal women with Down's syndrome, 40 to 60 years of age, was ascertained through the New York State Developmental Disability service system. Information from cognitive assessments, medical record review, neurological evaluation, and caregiver interviews was used to establish ages for onset of menopause and dementia. We used survival and multivariate regression analyses to determine the relation of age at menopause to age at onset of Alzheimer's disease, adjusting for age, level of mental retardation, body mass index, and history of hypothyroidism or depression. Women with early onset of menopause (46 years or younger) had earlier onset and increased risk of Alzheimer's disease (AD) compared with women with onset of menopause after 46 years (rate ratio, 2.7; 95% confidence interval [CI], 1.2-5.9). Demented women had higher mean serum sex hormone binding globulin levels than nondemented women (86.4 vs 56.6 nmol/L, p = 0.02), but similar levels of total estradiol, suggesting that bioavailable estradiol, rather than total estradiol, is associated with dementia. Our findings support the hypothesis that reductions in estrogens after menopause contribute to the cascade of pathological processes leading to AD.

---

### PMID 16926067 — current stance: `supports`

**Evidence span:** > Women who had low levels of bioavailable E2 at baseline were four times as likely to develop AD (HR=4.1, 95% CI: 1.2-13.9) and developed AD, on average, 3 years earlier, than those with high levels of bioavailable E2.

**Golden note:** Bioavailable estradiol delays AD onset in DS — supports timing.

**Bioavailable estradiol and age at onset of Alzheimer's disease in postmenopausal women with Down syndrome.**

*Neuroscience letters*, 2006. Types: Comparative Study; Journal Article; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> Several lines of evidence suggest that loss of estrogen after menopause may play a role in the cognitive declines associated with Alzheimer's disease (AD). Women with Down syndrome (DS) experience early onset of both menopause and AD. This timing provides a model to examine the influence of endogenous estrogen deficiency on risk of AD. We hypothesized that low serum levels of bioavailable estradiol (E2) would be associated with increased risk of AD. One hundred and nineteen postmenopausal women with DS, 42-59 years of age, were ascertained through the New York State developmental disability service system and followed at 18-month intervals. Information from cognitive assessments, caregiver interviews, medical record review and neurological examination was used to establish the diagnosis of dementia. Women with DS who developed AD had lower levels of bioavailable E2, lower levels of total estradiol, higher levels of sex-hormone binding globulin, and lower levels of dehydroepiandrosterone sulfate at baseline than women who remained dementia free over the course of follow-up. Women who had low levels of bioavailable E2 at baseline were four times as likely to develop AD (HR=4.1, 95% CI: 1.2-13.9) and developed AD, on average, 3 years earlier, than those with high levels of bioavailable E2, after adjustment for age, level of mental retardation, ethnicity, body mass index, history of hypothyroidism or depression and the presence of the apolipoprotein varepsilon4 allele. Our findings support the hypothesis that reductions in estrogen following menopause can contribute to the cascade of pathological processes leading to AD.

---

### PMID 23418430 — current stance: `inconclusive`

**Evidence span:** > APOE-ε4 carriers who went off their HT regimen exhibited TL shortening, as predicted for the at-risk population. APOE-ε4 carriers who remained on HT, however, did not exhibit comparable signs of cell aging.

**Golden note:** APOE-ε4 + accelerated cell aging in mid-life women — implication for HT.

**Accelerated cell aging in female APOE-ε4 carriers: implications for hormone therapy use.**

*PloS one*, 2013. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> Apolipoprotein-ε4 (APOE-ε4) is a major genetic risk factor for cognitive decline, Alzheimer's disease (AD) and early mortality. An accelerated rate of biological aging could contribute to this increased risk. Here, we determined whether APOE-ε4 status impacts leukocyte telomere length (TL) and the rate of cellular senescence in healthy mid-life women and, further, whether hormone replacement therapy (HT) modifies this association. Post-menopausal women (N = 63, Mean age = 57.7), all HT users for at least one year, were enrolled in a randomized longitudinal study. Half of the participants (N = 32) remained on their HT regimen and half (N = 31) went off HT for approximately two years (Mean  = 1.93 years). Participants included 24 APOE-ε4 carriers and 39 non-carrier controls. Leukocyte TL was measured at baseline and the end of year 2 using quantitative polymerase chain reaction. Logistic regression analysis indicated that the odds of an APOE-ε4 carrier exhibiting telomere shortening (versus maintenance/growth) over the 2-year study were more than 6 (OR  = 6.26, 95% CI  = 1.02, 38.49) times higher than a non-carrier, adjusting for established risk factors and potential confounds. Despite the high-functioning, healthy mid-life status of study participants, APOE-ε4 carriers had marked telomere attrition during the 2-year study window, the equivalent of approximately one decade of additional aging compared to non-carriers. Further analyses revealed a modulatory effect of hormone therapy on the association between APOE status and telomere attrition. APOE-ε4 carriers who went off their HT regimen exhibited TL shortening, as predicted for the at-risk population. APOE-ε4 carriers who remained on HT, however, did not exhibit comparable signs of cell aging. The opposite pattern was found in non-carriers. The results suggest that hormone use might buffer against accelerated cell aging in mid-life women at risk for dementia. Importantly, for non-carrier women there was no evidence that HT conferred protective effects on telomere dynamics.

---

### PMID 33110037 — current stance: `inconclusive`

**Evidence span:** > Increased levels of cognitive complaints were associated with lower gray-matter volume in the right medial temporal lobe (r = -0.445, P < 0.002, R = 0.2).

**Golden note:** Cognitive complaints + GM volume in younger postmenop — descriptive.

**Cognitive complaints are associated with smaller right medial temporal gray-matter volume in younger postmenopausal women.**

*Menopause (New York, N.Y.)*, 2020. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural

> OBJECTIVE: Menopause is associated with increasing cognitive complaints and older women are at increased risk of developing Alzheimer disease compared to men. However, there is difficulty in early markers of risk using objective performance measures. We investigated the impact of subjective cognitive complaints on the cortical structure in a sample of younger postmenopausal women. METHODS: Data for this cross-sectional study were drawn from the baseline visit of a longer double-blind study examining estrogen-cholinergic interactions in normal postmenopausal women. Structural Magnetic Resonance Imaging was acquired on 44 women, aged 50-60 years and gray-matter volume was defined by voxel-based morphometry. Subjective measures of cognitive complaints and postmenopausal symptoms were obtained as well as tests of verbal episodic and working memory performance. RESULTS: Increased levels of cognitive complaints were associated with lower gray-matter volume in the right medial temporal lobe (r = -0.445, P < 0.002, R = 0.2). Increased depressive symptoms and somatic complaints were also related to increased cognitive complaints and smaller medial temporal volumes but did not mediate the effect of cognitive complaints. In contrast, there was no association between performance on the memory tasks and subjective cognitive ratings, or medial temporal lobe volume. CONCLUSIONS: The findings of the present study indicate that the level of reported cognitive complaints in postmenopausal women may be associated with reduced gray-matter volume which may be associated with cortical changes that may increase risk of future cognitive decline. : Video Summary:http://links.lww.com/MENO/A626.

---

### PMID 34342862 — current stance: `inconclusive`

**Evidence span:** > Both observational and controlled clinical trials had methodological issues and discrepancies in inclusion criteria and HT protocols. These inconsistencies made it difficult to establish an association between HT and AD.

**Golden note:** HT in postmenop AD systematic review — conflicting.

**Use of Hormone Therapy in Postmenopausal Women with Alzheimer's Disease: A Systematic Review.**

*Drugs & aging*, 2021. Types: Research Support, Non-U.S. Gov't; Systematic Review; Journal Article

> BACKGROUND: Around two-thirds of patients with Alzheimer's disease (AD) are women, which could be related to the depletion of female sexual hormones at menopause. The replacement of these hormones with hormone therapy (HT) to possibly decrease AD risk or treat AD patients has generated conflicting results in the literature. OBJECTIVE: Our aim was to systematically review the relationship between HT use in postmenopausal women with AD and the risk of developing or treating AD symptoms. DATA SOURCES: The PubMed, LILACS, Scopus, Scielo, and Web of Science databases were searched from January 1994 to December 2020 using the descriptors 'Alzheimer Disease OR Alzheimer's Disease' and 'Hormone Replacement Therapy OR Estrogen Replacement Therapy'. STUDY SELECTION: Observational and controlled clinical trials including postmenopausal women diagnosed with AD and evaluating HT efficacy were eligible for inclusion. DATA EXTRACTION: Extracted data comprise study design, covariates, inclusion criteria for sample selection, AD diagnosis criteria, biases, HT regimen, and cognitive measurement tools used. RESULTS: Overall, 25 studies were selected. Among the 14 observational studies, 8 reported an improvement in cognitive function and a decrease in AD risk, especially in younger postmenopausal women. Five observational studies did not demonstrate any association between HT and AD, and one study reported an increase in AD risk, regardless of time of HT initiation. Of the 11 controlled clinical trials included, 7 showed an amelioration in cognitive function after HT. The remaining 4 trials saw no difference between HT and control. CONCLUSION: Both observational and controlled clinical trials had methodological issues and discrepancies in inclusion criteria and HT protocols. These inconsistencies made it difficult to establish an association between HT and AD.

---

### PMID 40220453 — current stance: `supports`

**Evidence span:** > Pooled estimates showed that MHT use for 3-5 years (cohort, RR = 0.56, 95% CI: 0.34-0.93) or initiation within 5 years of menopause (cohort, RR = 0.70, 95% CI: 0.49-0.99) reduced the risk of AD.

**Golden note:** MHT duration/timing/route/formulation meta — protective association overall.

**Association between duration, initiation time, routes, and formulations of menopausal hormone therapy use and Alzheimer disease in women: A systematic review and meta-analysis.**

*The Journal of pharmacology and experimental therapeutics*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> The purpose of this study was to investigate the effect of menopausal hormone therapy (MHT) on the risk of Alzheimer disease (AD) by examining its duration, initiation time, routes of administration, and formulations through systematic review and meta-analysis. PubMed, Embase, Cochrane Library, Web of Science, and Scopus were searched on March 15, 2023. We selected cohort studies, case-control studies, and randomized controlled trials on the effect of MHT on AD in women. Odds ratio, relative risk, and hazard ratio were extracted. Random-effect models were used to estimate the polled estimates (relative risk [RR] or odds ratio [OR]) and their 95% confidence interval (95% CI). We included 3 randomized controlled trials, 12 cohort studies, and 16 case-control studies. A total of 7,710,379 women were included. Pooled estimates showed that MHT use for 3-5 years (cohort, RR = 0.56, 95% CI: 0.34-0.93) or initiation within 5 years of menopause (cohort, RR = 0.70, 95% CI: 0.49-0.99) reduced the risk of AD. Oral administration reduced AD risk (cohort, RR = 0.42, 95% CI: 0.40-0.44). Combining estrogen and progesterone (case-control, OR = 1.13, 95% CI: 1.05-1.21) or progesterone only (case-control, OR = 1.13, 95% CI: 1.10-1.17) increases AD risk. Tibolone increased AD risk (cohort, RR = 1.04, 95% CI: 1.01-1.07; case-control, OR = 1.07, 95% CI: 1.01-1.14). MHT-protected apolipoprotein E genotype 4 carriers (cohort, RR = 0.13, 95% CI: 0.02-0.90), depressed populations (cohort, RR = 0.85, 95% CI: 0.80-0.90), and Americas (cohort, RR = 0.54, 95% CI: 0.37-0.80; case-control, OR = 0.68, 95% CI: 0.47-0.99) from AD. Using MHT early (within 5 years after menopause) for about 5 years may protect against AD. However, combining estrogen with progesterone, or using progesterone only, could increase AD risk. Oral MHT methods are more effective than transdermal ones in reducing this risk. SIGNIFICANCE STATEMENT: Menopausal hormone therapy (MHT) use within 5 years after menopause could offer protective benefits against Alzheimer disease (AD). A combination of estrogen and progesterone, using progesterone only or tibolone usage was connected with an elevated risk of AD. Oral MHT was more effective than transdermal methods in lowering AD risk. MHT lowered AD risk in apolipoprotein E genotype 4 allele carriers, individuals with depression, and Americans. MHT regimens should be highly personalized.

---

### PMID 39422947 — current stance: `supports`

**Evidence span:** > Combination MHT should probably be prescribed for less than 5 years after menopause to reduce risk for AD, while estrogen alone should not be prescribed to women over 60.

**Golden note:** (Phyto)estrogen + AD — modified by age + duration; supports timing window.

**Alzheimer's Disease and (Phyto) Estrogen Treatment: Modification of Effects by Age, Type of Treatment, and Duration of Use.**

*Journal of Alzheimer's disease : JAD*, 2024. Types: Journal Article; Meta-Analysis

> BACKGROUND: There is a continued debate on whether menopausal hormone therapy (MHT) protects women against Alzheimer's disease (AD). It is also unclear whether phytoestrogen could be an alternative treatment for AD. OBJECTIVE: To investigate whether mixed study findings may be due to differences in age at initiation of MHT and duration of prescription of different types of MHT using meta-analyses. METHODS: After a systematic literature search, meta-analyses were carried out using Cochrane Revman 5.4.1.software including data from large nationwide studies of registered medically diagnosed AD and prescribed MHT. These analyses were stratified for duration and type of treatment, by age at start of prescription of therapy. Insufficient quality data were available for phytoestrogen treatment and AD meta-analyses. RESULTS: A total of 912,157 women were included from five registries, of whom 278,495 had developed AD during follow-up. Meta-analyses suggested a small increased AD risk after 5-10 years prescription of combination MHT regardless of age, and over 10 years only in women younger than 60 years of age. No association was seen for estrogen alone for women younger than 60 years of age, but AD risk did increase for women over 60 years of age for up to 5 years of MHT prescriptions. CONCLUSIONS: Combination MHT should probably be prescribed for less than 5 years after menopause to reduce risk for AD, while estrogen alone should not be prescribed to women over 60. For phytoestrogen, small treatment trials suggested some benefit of tempeh (fermented soy), which should be investigated further.

---

### PMID 41618732 — current stance: `inconclusive`

**Evidence span:** > Aβ and structural MRI biomarkers were not different in the oCEE and tE2 groups compared to placebo. Apolipoprotein E ε4 status did not modify the findings.

**Golden note:** Long-term amyloid PET/MRI HT trial — biomarker-only.

**Long-term amyloid PET and MRI outcomes in a menopausal hormone therapy trial.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2026. Types: Journal Article; Randomized Controlled Trial

> INTRODUCTION: Associations of short-term use of menopausal hormone therapy (mHT) with Alzheimer's disease (AD) and structural magnetic resonance imaging (MRI) biomarkers were investigated 10 years after an mHT trial. METHODS: Recently menopausal women with good cardiovascular health were randomized to oral conjugated equine estrogens (oCEE) or transdermal 17β-estradiol (tE2) and micronized progesterone, or placebo for 4 years. Amyloid beta (Aβ) on positron emission tomography, hippocampal atrophy, and dorsolateral prefrontal cortex thickness on MRI were assessed 10 years after completion of the mHT trial (n = 266). RESULTS: Aβ and structural MRI biomarkers were not different in the oCEE and tE2 groups compared to placebo. Apolipoprotein E ε4 status did not modify the findings. DISCUSSION: There was no evidence of adverse effects or benefits associated with 4 years of use of oral or transdermal mHT on Aβ and structural MRI biomarkers in relatively healthy women, 10 years after mHT. Findings support the long-term safety of short-term use of mHT on brain health. CLINICAL TRIALS REGISTRATION: NCT00154180 Kronos Early Estrogen Prevention Study (KEEPS) HIGHLIGHTS: There were no menopausal hormone therapy-related adverse effects or benefits on amyloid beta and magnetic resonance imaging biomarkers in the long term. Apolipoprotein E ε4 carrier status did not modify these findings. Findings align with neutral cognitive and cerebrovascular outcomes in this cohort.

---

### PMID 37393661 — current stance: `supports`

**Evidence span:** > Women with EM demonstrated a greater risk of dementia of any type than women of normal age at menopause (OR 1.37, 95 % CI 1.22-1.54; I2 93%). Increased risk of dementia was also found in women with POI (OR 1.18, 95 % CI 1.15-1.21; I2 0%).

**Golden note:** Early menopause / POI → increased dementia risk meta — supports estrogen-loss hypothesis.

**Early menopause and premature ovarian insufficiency are associated with increased risk of dementia: A systematic review and meta-analysis of observational studies.**

*Maturitas*, 2023. Types: Meta-Analysis; Systematic Review; Journal Article

> BACKGROUND/AIMS: Among other risk factors, the decline in estrogen concentrations during menopause may compromise cognitive function. Whether early menopause (EM) is associated with an increased risk of dementia remains unclear. The purpose of this study was to systematically review and meta-analyze current evidence regarding the association between EM or premature ovarian insufficiency (POI) and the risk of dementia of any type. MATERIALS AND METHODS: A comprehensive literature search was conducted through the PubMed, Scopus and CENTRAL databases up to August 2022. Study quality was assessed using the Newcastle-Ottawa scale. Associations were calculated as odds ratio (OR) with 95 % confidence interval (CI). The I2 index was employed for heterogeneity. RESULTS: Eleven studies (nine assessed as of good and two as of fair quality) were included in the meta-analysis (n = 4,716,862). Women with EM demonstrated a greater risk of dementia of any type than women of normal age at menopause (OR 1.37, 95 % CI 1.22-1.54; I2 93%). However, after excluding a large retrospective cohort study, the results were altered (OR 1.07, 95 % CI 0.78-1.48; I2 94%). Increased risk of dementia was also found in women with POI (OR 1.18, 95 % CI 1.15-1.21; I2 0%). Subgroup analysis showed that this risk was mostly evident in cohort studies, and those which included women with natural menopause. CONCLUSIONS: Women with EM or POI may be at increased risk of dementia compared with women of normal age at menopause, but further research investigating that hypothesis is warranted.

---

### PMID 17368974 — current stance: `inconclusive`

**Evidence span:** > Therefore the reported overall cardiovascular risks in WHI, in both treatment arms, should be regarded as irrelevant to menopause management.

**Golden note:** WHI risks / menopause management commentary.

**WHI risks: any relevance to menopause management?**

*Maturitas*, 2007. Types: Journal Article; Randomized Controlled Trial

> Two randomised controlled trials of hormone therapy (HT) were conducted within the US Women's Health Initiative. Both were chronic disease prevention trials, undertaken to determine whether HT reduced cardiovascular risk and increased breast cancer risk. Because the majority of subjects in both trials were asymptomatic and many years postmenopausal, and because substantial numbers had received HT prior to recruitment to the trials, care must be taken in drawing conclusions that the observed risks are applicable to women for whom HT is conventionally prescribed. Each of the reported risks must be examined critically to determine its likely applicability to symptomatic women treated for two to three years to relieve symptoms, but sometimes for substantially longer periods. Further, the risks reported in each of the two trials must be considered separately. Concerning cardiovascular disease, many subjects in the trials were at increased baseline risk because of their age, body mass index, smoking status, blood pressure and years since menopause, in contrast to the usual situation for symptomatic perimenopausal women. Therefore the reported overall cardiovascular risks in WHI, in both treatment arms, should be regarded as irrelevant to menopause management. In contrast, breast cancer risk is relevant, providing that proper note is taken of the fact that there was no increased risk after five years of combined hormone therapy in non-prior HT users and there was a tendency to a decreased risk in oestrogen only treated individuals. Other risks are analysed similarly.

---

