# Q15: Does Mediterranean diet adherence reduce incident Alzheimer's disease in cognitively normal adults?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=27 PMIDs.

**Current S/C/I**: 18 / 0 / 9
**Proposed S/C/I**: 15 / 0 / 12
**Net flips**: 5 (1 I→S, 4 S→I)

**Audit note (second pass):** Added one additional flip — `30682676`
(MeDi-AD biomarker meta) `supports → inconclusive`, since per the strict bar
biomarker-only studies (tau/Aβ outcomes, no clinical endpoint) belong in
`inconclusive`. All four originally proposed flips confirmed against the
strict bar. Several `supports` entries flagged for split-outcome / hedged-meta
patterns but kept (positive AD-incidence sub-outcome dominates).

The current labeling is largely sound. Most positive labels reflect
significantly-positive observational meta-analyses; most inconclusive
labels reflect narrative/biomarker/multimodal-trial papers where the
MeDi-specific signal can't be isolated. The few flips are minor
boundary corrections.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `18786971` | 2008 | **inconclusive → supports** | Sopio Tsivgoulis-style umbrella, 12 cohorts, n=1.57M. Verbatim: *"Greater adherence to a Mediterranean diet is associated with a significant improvement in health status, as seen by... incidence of or mortality from Parkinson's disease and Alzheimer's disease (0.87, 0.80 to 0.96)."* Pooled RR 0.87 (CI 0.80-0.96) for AD/PD incidence is a **statistically significant positive** finding for the question. The note rationale ("cognition not primary") is true but the AD-incidence outcome is directly the question. |
| `34153553` | 2021 | **supports → inconclusive** | MeDi-cognition meta. Verbatim findings show MeDi sig for global cognitive decline (RR 0.26 sig) **but**: *"no significant associations between MeDi and mobility, MCI, dementia were found."* The dementia/MCI outcomes — which are the relevant outcomes for this question — were **null**. Mixed signal: cognition trajectory positive, dementia incidence negative. → `inconclusive`. |
| `36529364` | 2022 | **supports → inconclusive** | MeDi neuroimaging biomarker SR. Verbatim: *"Four studies reported on hippocampal volume, with **inconclusive or no associations** seen with MedDiet adherence. Two studies found a significant association between higher MedDiet adherence and lower WMHV, while two other studies found no significant associations."* Self-described as inconclusive on hippocampal volume; mixed on WMH. The note ("favorable") doesn't match the abstract. |
| `41599807` | 2026 | **supports → inconclusive** | "MIND Pattern Nutritional Intervention" — observational case-control, n=60 (30 ALZ + 30 controls). Primary outcome was MEDAS adherence + gut microbiota changes, not cognitive incidence in cognitively-normal adults. Verbatim describes the design: *"In an observational case-control study"* — not testing whether MeDi adherence reduces AD incidence in healthy adults. The intervention even **enrolled ALZ patients** — wrong population for the question (which asks about cognitively normal adults). |
| `30682676` | 2018 | **supports → inconclusive** | [Added on second pass.] MeDi-AD biomarker meta-analysis. The pooled effect (β = 0.11, 95% CI 0.04–0.17, p = 0.002) is on **AD biomarkers (tau and beta-amyloid)**, not clinical AD incidence. Per the strict bar, biomarker-only studies with no clinical endpoint are `inconclusive`. Verbatim: *"investigated this relationship with respect to the hallmark AD biomarkers (tau and beta-amyloid) that manifest decades before clinical symptomatology."* The biomarker signal is suggestive but doesn't establish that MeDi reduces incident AD in cognitively normal adults. |

## Confirmed (no change)

- `24164735` (MeDi-MCI/AD meta — HR 0.64 sig for AD in cognitively normal) — **supports ✓**
- `25698435` (modifiable predictors of MCI→dementia review) — **inconclusive ✓** (broad mix)
- `25770254` (dietary patterns SR — MeDi protective) — **supports ✓** (defensible mixed evidence)
- `28697569` (dietary patterns review — MeDi/MIND/DASH protective) — **supports ✓**
- `30689586` (dietary patterns SR with MeDi protective) — **inconclusive ✓** (note framing)
- `26887612` (AD-diet SR — 50/64 studies show association) — **supports ✓**
- `34835984` (nutrition RCT review — heterogeneous) — **inconclusive ✓**
- `31240575` (dietary pattern-AD review) — **supports ✓**
- `39797935` (2025 MeDi-AD meta — AD HR 0.70 sig) — **supports ✓**
- `29574441` (MRI biomarker cross-sectional, n=116) — **inconclusive ✓**
- `38311314` (MIND diet SR — protective in 7/10 cohorts) — **supports ✓**
- `29728772` (implementing MeDi outside Mediterranean — feasibility/PREDIMED) — **supports ✓**
- `32427314` (umbrella prospective MeDi — SRR 0.63 for AD sig) — **supports ✓**
- `34392373` (mid-life dietary patterns — mixed) — **inconclusive ✓**
- `33336232` (GRADE rec MeDi 1B for cognitive impairment) — **supports ✓**
- `38961421` (MIND-ADmini multimodal — diet quality improved, no cognitive primary) — **inconclusive ✓**
- `39861466` (MeDi/Nordic SR — protective) — **supports ✓**
- `40744415` (multiethnic cohort, n=92,849, ADRD HR 0.91 sig) — **supports ✓**
- `41259881` (Italian guidelines MeDi prevention meta — AD OR 0.92 sig) — **supports ✓**
- `39499795` (APOE × dietary patterns umbrella — interaction-focused, mixed) — **inconclusive ✓**
- `40378769` (AgeWell.de imaging study — descriptive imaging) — **inconclusive ✓**
- `29147948` (MeDi + subjective cognitive function men, n=27,842, sig OR 0.64) — **supports ✓**

## Cross-cutting issues

- **Population scope**: The question specifically asks about
  "cognitively normal adults." Several papers in `relevant_pmids`
  include populations with MCI or AD (e.g., `41599807`, parts of
  `34153553`'s analysis). These should ideally be tagged as off-target
  or moved to a separate "MeDi in MCI/AD" question.
- **Outcome scope**: The question asks about "incident Alzheimer's
  disease" specifically, but many positive labels rest on broader
  cognitive-decline endpoints. `34153553` is the cleanest example:
  cognitive-decline trajectory was positive, AD/dementia incidence was
  null — and currently labeled `supports`.
- **No `contradicts`**: Plausible. The MeDi corpus is genuinely
  consistent across observational meta-analyses (effect sizes ~0.7-0.9
  HR for AD), and there are no large RCT primary failures because no
  large RCT has been adequately powered for AD-incidence as a primary
  endpoint. PREDIMED and FINGER-style trials use cognitive scores not
  incident AD.
- After flips: 15/0/12 — minor net change, the "mostly positive"
  expected consensus holds well.

### Recurring policy patterns observed in Q15

- **(a) Subgroup-positive in parent-null trial:** Not strongly present.
  Closest is `39499795` (APOE × diet umbrella) — MeDi works only in subset
  (APOE ε4 subgroup question with mixed-by-status results); kept as
  inconclusive.
- **(b) Preclinical/mech-dominated review labeled `supports`:** `30682676`
  (biomarker-only meta) flipped to inconclusive on second pass. `36529364`
  (neuroimaging biomarker review) already flipped in first pass.
- **(c) Missed primary with significant secondary:** `34153553` is the
  cleanest case for the question scope: cognition trajectory (secondary)
  positive, but MCI/dementia/AD incidence (primary for this question) null.
  Flipped to inconclusive. `41259881` exhibits the inverse pattern: AD
  outcome (which IS the primary question outcome) sig, but dementia/MCI
  outcomes null — kept as supports because the AD-incidence outcome is
  the on-target endpoint.

## Highest-confidence flips for this question

- `34153553` supports → inconclusive — the **dementia-incidence outcome
  was null** in this meta. The current label generalizes from the
  cognition trajectory result.
- `36529364` supports → inconclusive — abstract says "inconclusive or
  no associations" for hippocampal volume.
- `30682676` supports → inconclusive — biomarker-only meta (tau/Aβ),
  no clinical endpoint. Strict-bar rule: biomarker-only studies do not
  count as `supports` for incidence questions.

These are stance corrections rather than direction reversals — the
question's overall consensus picture is unchanged.


---

## signal_types (annotation layer)

Pattern tags applied to each pmid. Tags identify caveats that make a paper
weaker evidence than its stance label suggests. Tags are NOT direct stance
overrides — they're metadata for stratified eval scoring and UI filtering.

### Tag vocabulary (Q15)

Existing tags used:
- `biomarker_only` — outcome is a biomarker (imaging, microbiome, fluid
  biomarker), not a clinical AD/dementia diagnosis or cognitive score
- `hedged_meta` — meta or SR with mixed primary studies; pooled or
  vote-counted result + a "but evidence is heterogeneous/limited" caveat
- `narrative_review` — non-meta SR or review that integrates findings
  qualitatively
- `broad_scope_review` — review covers many diseases/factors with AD as
  one of several outcomes; AD-specific signal not the main focus
- `split_outcome` — multi-outcome study where some outcomes are
  significant and others null; stance depends on which outcome you read
- `missed_primary_sig_secondary` — primary endpoint null/missed but
  secondary endpoint significant
- `regional_heterogeneity` — effect varies by geographic / ethnic
  population
- `subgroup_apoe_split` — effect varies by APOE genotype
- `wrong_population` — population is not "cognitively normal adults"
  (e.g., MCI, AD, prodromal AD)
- `combo_intervention` — multimodal intervention (diet + exercise +
  cognitive training etc.) where the MeDi-specific contribution can't
  be isolated
- `case_series_underpowered` — sample size too small to detect realistic
  effect (n < ~100)
- `comparator_only` — paper's main contribution is comparing/citing
  other studies, not an independent finding
- `uncontrolled_observational` — observational with no control group
  comparison appropriate to the question
- `pilot_positive` — pilot/feasibility study with positive but
  exploratory result

New tag proposed (Q15-specific):
- `subjective_endpoint` — clinical outcome is self-reported / subjective
  (e.g., subjective cognitive function questionnaire) rather than a
  clinician-adjudicated AD/dementia diagnosis or validated cognitive test
  battery. Distinct from `biomarker_only` (which is imaging/lab) and
  from `split_outcome` (which is multi-endpoint mixed). Rationale: a
  paper can be statistically rigorous on a subjective endpoint and still
  not directly answer an incident-AD question.

### Per-pmid tags

| PMID | Year | Stance (proposed) | Tags |
|------|------|-------------------|------|
| `18786971` | 2008 | supports | `broad_scope_review` |
| `24164735` | 2014 | supports | (clean meta — no caveats) |
| `25698435` | 2015 | inconclusive | `broad_scope_review`, `narrative_review` |
| `25770254` | 2015 | supports | `narrative_review`, `hedged_meta` |
| `28697569` | 2017 | supports | `narrative_review` |
| `30689586` | 2019 | inconclusive | `narrative_review`, `hedged_meta` |
| `34153553` | 2021 | inconclusive [FLIP] | `split_outcome`, `missed_primary_sig_secondary` |
| `26887612` | 2016 | supports | `narrative_review`, `wrong_population` (partial — mean age >65 at-risk, not all cog-normal) |
| `30682676` | 2018 | inconclusive [FLIP] | `biomarker_only` |
| `34835984` | 2021 | inconclusive | `hedged_meta`, `narrative_review` |
| `31240575` | 2019 | supports | `narrative_review` |
| `39797935` | 2025 | supports | (clean meta — no caveats) |
| `29574441` | 2018 | inconclusive | `biomarker_only`, `case_series_underpowered` |
| `38311314` | 2024 | supports | `regional_heterogeneity`, `hedged_meta` |
| `29728772` | 2018 | supports | `narrative_review`, `comparator_only` |
| `32427314` | 2020 | supports | `hedged_meta` |
| `34392373` | 2022 | inconclusive | `narrative_review`, `hedged_meta` |
| `33336232` | 2021 | supports | `narrative_review` |
| `36529364` | 2022 | inconclusive [FLIP] | `biomarker_only`, `hedged_meta` |
| `38961421` | 2024 | inconclusive | `combo_intervention`, `wrong_population`, `pilot_positive` |
| `39861466` | 2025 | supports | `narrative_review`, `hedged_meta` |
| `40744415` | 2025 | supports | `regional_heterogeneity` |
| `41259881` | 2025 | supports | `split_outcome` |
| `39499795` | 2025 | inconclusive | `subgroup_apoe_split`, `hedged_meta` |
| `40378769` | 2025 | inconclusive | `combo_intervention`, `biomarker_only`, `case_series_underpowered` |
| `41599807` | 2026 | inconclusive [FLIP] | `wrong_population`, `biomarker_only`, `case_series_underpowered`, `uncontrolled_observational` |
| `29147948` | 2017 | supports | `subjective_endpoint` |

### Tag distribution (count of pmids with each tag)

- `narrative_review`: 11
- `hedged_meta`: 9
- `biomarker_only`: 5
- `case_series_underpowered`: 3
- `combo_intervention`: 2
- `regional_heterogeneity`: 2
- `split_outcome`: 2
- `wrong_population`: 3 (1 partial, 2 full)
- `broad_scope_review`: 2
- `subgroup_apoe_split`: 1
- `missed_primary_sig_secondary`: 1
- `comparator_only`: 1
- `uncontrolled_observational`: 1
- `pilot_positive`: 1
- `subjective_endpoint`: 1 (new tag)

### Coverage

- 27 / 27 pmids tagged (100%).
- 2 pmids carry no caveat tags (`24164735`, `39797935` — both clean
  AD-incidence metas with sig HR).
- The high concentration of `narrative_review` and `hedged_meta` reflects
  the structure of the MeDi-AD literature: many overlapping SRs and
  umbrella reviews citing the same underlying primary cohorts. UI-side
  paper-type filtering (per CLAUDE.md TODO #2) would substantially
  collapse these.

---

## Abstracts (n=27)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 18786971 — current stance: `supports` [FLIP from inconclusive → supports]

**Evidence span:** > Greater adherence to a Mediterranean diet is associated with a significant improvement in health status, as seen by a significant reduction in overall mortality (9%), mortality from cardiovascular diseases (9%), incidence of or mortality from cancer (6%), and incidence of Parkinson's disease and Alzheimer's disease (13%).

**Golden note:** Broad mortality/chronic disease meta — cognition not primary.

**Adherence to Mediterranean diet and health status: meta-analysis.**

*BMJ (Clinical research ed.)*, 2008. Types: Journal Article; Meta-Analysis; Review

> OBJECTIVE: To systematically review all the prospective cohort studies that have analysed the relation between adherence to a Mediterranean diet, mortality, and incidence of chronic diseases in a primary prevention setting. DESIGN: Meta-analysis of prospective cohort studies. DATA SOURCES: English and non-English publications in PubMed, Embase, Web of Science, and the Cochrane Central Register of Controlled Trials from 1966 to 30 June 2008. Studies reviewed Studies that analysed prospectively the association between adherence to a Mediterranean diet, mortality, and incidence of diseases; 12 studies, with a total of 1 574,299 subjects followed for a time ranging from three to 18 years were included. RESULTS: The cumulative analysis among eight cohorts (514,816 subjects and 33,576 deaths) evaluating overall mortality in relation to adherence to a Mediterranean diet showed that a two point increase in the adherence score was significantly associated with a reduced risk of mortality (pooled relative risk 0.91, 95% confidence interval 0.89 to 0.94). Likewise, the analyses showed a beneficial role for greater adherence to a Mediterranean diet on cardiovascular mortality (pooled relative risk 0.91, 0.87 to 0.95), incidence of or mortality from cancer (0.94, 0.92 to 0.96), and incidence of Parkinson's disease and Alzheimer's disease (0.87, 0.80 to 0.96). CONCLUSIONS: Greater adherence to a Mediterranean diet is associated with a significant improvement in health status, as seen by a significant reduction in overall mortality (9%), mortality from cardiovascular diseases (9%), incidence of or mortality from cancer (6%), and incidence of Parkinson's disease and Alzheimer's disease (13%). These results seem to be clinically relevant for public health, in particular for encouraging a Mediterranean-like dietary pattern for primary prevention of major chronic diseases.

---

### PMID 24164735 — current stance: `supports`

**Evidence span:** > Among cognitively normal individuals, higher adherence to the MeDi was associated with a reduced risk of MCI (HR = 0.73; 95% CI, 0.56-0.96; p = 0.02) and AD (HR = 0.64; 95% CI, 0.46-0.89; p = 0.007).

**Golden note:** MeDi-MCI/AD meta — protective association.

**Association of mediterranean diet with mild cognitive impairment and Alzheimer's disease: a systematic review and meta-analysis.**

*Journal of Alzheimer's disease : JAD*, 2014. Types: Journal Article; Meta-Analysis; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't; Systematic Review

> BACKGROUND/OBJECTIVE: To conduct a systematic review of all studies to determine whether there is an association between the Mediterranean diet (MeDi) and cognitive impairment. METHODS: We conducted a comprehensive search of the major databases and hand-searched proceedings of major neurology, psychiatry, and dementia conferences through November 2012. Prospective cohort studies examining the MeDi with longitudinal follow-up of at least 1 year and reporting cognitive outcomes (mild cognitive impairment [MCI] or Alzheimer's disease [AD]) were included. The effect size was estimated as hazard-ratio (HR) with 95% confidence intervals (CIs) using the random-effects model. Heterogeneity was assessed using Cochran's Q-test and I2-statistic. RESULTS: Out of the 664 studies screened, five studies met eligibility criteria. Higher adherence to the MeDi was associated with reduced risk of MCI and AD. The subjects in the highest MeDi tertile had 33% less risk (adjusted HR = 0.67; 95% CI, 0.55-0.81; p < 0.0001) of cognitive impairment (MCI or AD) as compared to the lowest MeDi score tertile. Among cognitively normal individuals, higher adherence to the MeDi was associated with a reduced risk of MCI (HR = 0.73; 95% CI, 0.56-0.96; p = 0.02) and AD (HR = 0.64; 95% CI, 0.46-0.89; p = 0.007). There was no significant heterogeneity in the analyses. CONCLUSIONS: While the overall number of studies is small, pooled results suggest that a higher adherence to the MeDi is associated with a reduced risk of developing MCI and AD, and a reduced risk of progressing from MCI to AD. Further prospective-cohort studies with longer follow-up and randomized controlled trials are warranted to consolidate the evidence. Systematic review registration number: PROSPERO 2013: CRD42013003868.

---

### PMID 25698435 — current stance: `inconclusive`

**Evidence span:** > Mediterranean diet decreased the risk of conversion to Alzheimer's dementia.

**Golden note:** Modifiable predictors of MCI→dementia — broad mixed factors.

**Modifiable predictors of dementia in mild cognitive impairment: a systematic review and meta-analysis.**

*The American journal of psychiatry*, 2015. Types: Journal Article; Meta-Analysis; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't; Systematic Review

> OBJECTIVE: Public health campaigns encouraging early help seeking have increased rates of mild cognitive impairment (MCI) diagnosis in Western countries, but we know little about how to treat or predict dementia outcomes in persons with the condition. METHOD: The authors searched electronic databases and references for longitudinal studies reporting potentially modifiable risk factors for incident dementia after MCI. Two authors independently evaluated study quality using a checklist. Meta-analyses were conducted of three or more studies. RESULTS: There were 76 eligible articles. Diabetes and prediabetes increased risk of conversion from amnestic MCI to Alzheimer's dementia; risk in treated versus untreated diabetes was lower in one study. Diabetes was also associated with increased risk of conversion from any-type or nonamnestic MCI to all-cause dementia. Metabolic syndrome and prediabetes predicted all-cause dementia in people with amnestic and any-type MCI, respectively. Mediterranean diet decreased the risk of conversion to Alzheimer's dementia. The presence of neuropsychiatric symptoms or lower serum folate levels predicted conversion from any-type MCI to all-cause dementia, but less formal education did not. Depressive symptoms predicted conversion from any-type MCI to all-cause dementia in epidemiological but not clinical studies. CONCLUSIONS: Diabetes increased the risk of conversion to dementia. Other prognostic factors that are potentially manageable are prediabetes and the metabolic syndrome, neuropsychiatric symptoms, and low dietary folate. Dietary interventions and interventions to reduce neuropsychiatric symptoms, including depression, that increase risk of conversion to dementia may decrease new incidence of dementia.

---

### PMID 25770254 — current stance: `supports`

**Evidence span:** > The results suggest that better adherence to a Mediterranean diet is associated with less cognitive decline, dementia, or Alzheimer disease, as shown by 4 of 6 cross-sectional studies, 6 of 12 longitudinal studies, 1 trial, and 3 meta-analyses.

**Golden note:** Dietary patterns review — MeDi protective.

**Dietary patterns, cognitive decline, and dementia: a systematic review.**

*Advances in nutrition (Bethesda, Md.)*, 2015. Types: Journal Article; Systematic Review

> Nutrition is an important modifiable risk factor that plays a role in the strategy to prevent or delay the onset of dementia. Research on nutritional effects has until now mainly focused on the role of individual nutrients and bioactive components. However, the evidence for combined effects, such as multinutrient approaches, or a healthy dietary pattern, such as the Mediterranean diet, is growing. These approaches incorporate the complexity of the diet and possible interaction and synergy between nutrients. Over the past few years, dietary patterns have increasingly been investigated to better understand the link between diet, cognitive decline, and dementia. In this systematic review we provide an overview of the literature on human studies up to May 2014 that examined the role of dietary patterns (derived both a priori as well as a posteriori) in relation to cognitive decline or dementia. The results suggest that better adherence to a Mediterranean diet is associated with less cognitive decline, dementia, or Alzheimer disease, as shown by 4 of 6 cross-sectional studies, 6 of 12 longitudinal studies, 1 trial, and 3 meta-analyses. Other healthy dietary patterns, derived both a priori (e.g., Healthy Diet Indicator, Healthy Eating Index, and Program National Nutrition Santé guideline score) and a posteriori (e.g., factor analysis, cluster analysis, and reduced rank regression), were shown to be associated with reduced cognitive decline and/or a reduced risk of dementia as shown by all 6 cross-sectional studies and 6 of 8 longitudinal studies. More conclusive evidence is needed to reach more targeted and detailed guidelines to prevent or postpone cognitive decline.

---

### PMID 28697569 — current stance: `supports`

**Evidence span:** > In particular, higher adherence to a Mediterranean-type diet was associated with decreased cognitive decline.

**Golden note:** Dietary patterns review — protective for late-life cognitive disorders.

**Relationships of Dietary Patterns, Foods, and Micro- and Macronutrients with Alzheimer's Disease and Late-Life Cognitive Disorders: A Systematic Review.**

*Journal of Alzheimer's disease : JAD*, 2017. Types: Journal Article; Systematic Review

> In the last decade, the association between diet and cognitive function or dementia has been largely investigated. In the present article, we systematically reviewed observational studies published in the last three years (2014-2016) on the relationship among dietary factors and late-life cognitive disorders at different levels of investigation (i.e., dietary patterns, foods and food-groups, and dietary micro- and macronutrients), and possible underlying mechanisms of the proposed associations. From the reviewed evidence, the National Institute on Aging-Alzheimer's Association guidelines for Alzheimer's disease (AD) and cognitive decline due to AD pathology introduced some evidence suggesting a direct relation between diet and changes in the brain structure and activity. There was also accumulating evidence that combinations of foods and nutrients into certain patterns may act synergistically to provide stronger health effects than those conferred by their individual dietary components. In particular, higher adherence to a Mediterranean-type diet was associated with decreased cognitive decline. Moreover, also other emerging healthy dietary patterns such as the Dietary Approach to Stop Hypertension (DASH) and the Mediterranean-DASH diet Intervention for Neurodegenerative Delay (MIND) diets were associated with slower rates of cognitive decline and significant reduction of AD rate. Furthermore, some foods or food groups traditionally considered harmful such as eggs and red meat have been partially rehabilitated, while there is still a negative correlation of cognitive functions with saturated fatty acids and a protective effect against cognitive decline of elevated fish consumption, high intake of monounsaturated fatty acids and polyunsaturated fatty acids (PUFA), particularly n-3 PUFA.

---

### PMID 30689586 — current stance: `inconclusive`

**Evidence span:** > Of 38 studies, the Mediterranean diet was the most investigated with evidence supporting protection against cognitive decline among older adults.

**Golden note:** Dietary patterns review — efficacy uncertain framing.

**Dietary Patterns and Cognitive Health in Older Adults: A Systematic Review.**

*Journal of Alzheimer's disease : JAD*, 2019. Types: Journal Article; Systematic Review

> While the role of diet and nutrition in cognitive health and prevention of dementia in older adults has attracted much attention, the efficacy of different dietary patterns remains uncertain. Previous reviews have mainly focused on the Mediterranean diet, but either omitted other dietary patterns, lacked more recent studies, were based on cross-sectional studies, or combined older and younger populations. We followed PRISMA guidelines, and examined the efficacy of current research from randomized controlled trials and cohort studies on the effects of different dietary patterns. We reviewed the Mediterranean diet, Dietary Approach to Stop Hypertension (DASH) diet, the Mediterranean-DASH diet Intervention for Neurodegenerative Delay (MIND) diet, Anti-inflammatory diet, Healthy diet recommended by guidelines via dietary index, or Prudent healthy diets generated via statistical approaches, and their impact on cognitive health among older adults. Of 38 studies, the Mediterranean diet was the most investigated with evidence supporting protection against cognitive decline among older adults. Evidence from other dietary patterns such as the MIND, DASH, Anti-inflammatory, and Prudent healthy diets was more limited but showed promising results, especially for those at risk of cardiovascular disease. Overall, this review found positive effects of dietary patterns including the Mediterranean, DASH, MIND, and Anti-inflammatory diets on cognitive health outcomes in older adults. These dietary patterns are plant-based, rich in poly- and mono-unsaturated fatty acids with lower consumption of processed foods. Better understanding of the underlying mechanisms and effectiveness is needed to develop comprehensive and practical dietary recommendations against age-related cognitive decline among older adult.

---

### PMID 34153553 — current stance: `inconclusive` [FLIP from supports → inconclusive]

**Evidence span:** > Results of the pooled analysis of longitudinal studies revealed that high adherence to MeDi reduced the risk of global cognitive decline in non-demented older adults. However, no significant associations between MeDi adherence and the incidence of mobility problems, MCI, and dementia were found.

**Golden note:** MeDi adherence-cognition meta — positive.

**Cross-sectional and longitudinal associations between adherence to Mediterranean diet with physical performance and cognitive function in older adults: A systematic review and meta-analysis.**

*Ageing research reviews*, 2021. Types: Journal Article; Meta-Analysis; Systematic Review

> OBJECTIVES: The present study investigated the association between adherence to Mediterranean diet (MeDi) and physical performance and cognitive function in older adults. METHODS: We conducted a systematic review and meta-analysis of cross-sectional and longitudinal studies that investigated older adults aged 60+ years and assessed adherence to MeDi diet using validated composite scores. Observational studies, including cross-sectional, case-control, and longitudinal cohort studies, if crude baseline data was available, which investigated as a primary or secondary outcome the association of MeDi diet adherence with physical performance and/or cognitive function in non-demented older adults were included in the cross-sectional analysis. For the longitudinal analysis, case-control and longitudinal cohort studies that investigated the longitudinal associations between adherence to MeDi diet with the incidence of mild cognitive impairment (MCI), dementia, and/or Alzheimer's disease (AD), and/or changes in physical performance and cognition in non-demented older adults were included. Studies published in other languages than English were excluded. Studies were retrieved from MEDLINE, SCOPUS, CINAHL, and AgeLine databases until May 19, 2021. The risk of bias was evaluated using the Newcastle - Ottawa Quality Assessment Scale (NOS). A pooled effect size was calculated based on standard mean differences (SMD), log odds ratio (OR) and log risk ratio (RR). This study is registered on PROSPERO (CRD42021250254). RESULTS: Nineteen cross-sectional studies that investigated 19.734 community-dwelling and institutionalized older adults free of disability and dementia were included. A high adherence to MeDi was cross-sectionally associated with better walking speed (SMD = 0.42; 95 % Confidence Interval (CI) = 0.12-0.72, P = 0.006; I² = 65 %, P = 0.06), knee muscle strength speed (SMD = 0.26; 95 % CI = 0.17-0.36, P < 0.00001; I² = 0 %, P = 0.69), global cognition (SMD = 0.24; 95 % CI = 0.15-0.33, P < 0.00001; I² = 85 %, P < 0.00001), and memory (SMD = 0.18; 95 % CI = 0.13-0.25, P < 0.00001; I² = 100 %, P < 0.00001). The association between MeDi adherence and global cognition remained significant after stratifying the analysis by the region where the study was conducted, MeDi diet adherence composite score, and Mini Mental State Examination (MMSE). Studies had a moderate to low risk of bias. In relation to longitudinal analysis, thirty-four prospective studies with an average follow-up period that varied from 3.0 to 12.6 years and investigated 98.315 community-dwellers were included. Results indicated that older adults with high MeDi scores had a lower decline in global cognition RR = 0.26; 95 % CI = 0.23-0.29, P < 0.00001; I² = 100 %, P < 0.00001). In contrast, no significant associations between MeDi and mobility, MCI, dementia were found. A low risk of bias was found in the longitudinal studies. DISCUSSION: Findings of the present study indicated that high adherence to MeDi was cross-sectionally associated with physical performance and cognitive function. Results of the pooled analysis of longitudinal studies revealed that high adherence to MeDi reduced the risk of global cognitive decline in non-demented older adults. However, no significant associations between MeDi adherence and the incidence of mobility problems, MCI, and dementia were found. Although important, our findings should be carefully interpreted due to the presence of heterogeneity and publication bias.

---

### PMID 26887612 — current stance: `supports`

**Evidence span:** > Despite the methodological limitations, the finding that 50 of the 64 reviewed studies revealed an association between diet and AD incidence offers promising implications for diet as a modifiable risk factor for AD.

**Golden note:** AD-diet review — MeDi protective overall.

**Alzheimer's disease and diet: a systematic review.**

*The International journal of neuroscience*, 2016. Types: Journal Article; Systematic Review

> UNLABELLED: Purpose/Aim: Approximately 44 million people worldwide have Alzheimer's disease (AD). Numerous claims have been made regarding the influence of diet on AD development. The aims of this systematic review were to summarize the evidence considering diet as a protective or risk factor for AD, identify methodological challenges and limitations, and provide future research directions. METHODS: Medline, PsycINFO and PsycARTICLES were searched for articles that examined the relationship between diet and AD. RESULTS: On the basis of the inclusion and exclusion criteria, 64 studies were included, generating a total of 141 dietary patterns or "models". All studies were published between 1997 and 2015, with a total of 132 491 participants. Twelve studies examined the relationship between a Mediterranean (MeDi) diet and AD development, 10 of which revealed a significant association. Findings were inconsistent with respect to sample size, AD diagnosis and food measures. Further, the majority of studies (81.3%) included samples with mean baseline ages that were at risk for AD based on age (>65 years), ranging from 52.0 to 85.4 years. The range of follow-up periods was 1.5-32.0 years. CONCLUSIONS: The mean age of the samples poses a limitation in determining the influence of diet on AD; given that AD has a long prodromal phase prior to the manifestation of symptoms and decline. Further studies are necessary to determine whether diet is a risk or protective factor for AD, foster translation of research into clinical practice and elucidate dietary recommendations. Despite the methodological limitations, the finding that 50 of the 64 reviewed studies revealed an association between diet and AD incidence offers promising implications for diet as a modifiable risk factor for AD.

---

### PMID 30682676 — current stance: `inconclusive` [FLIP from supports → inconclusive]

**Evidence span:** > Meta-analysis revealed a small but significant effect of diet on AD biomarkers (β = 0.11 [95% CI 0.04-0.17], p = 0.002).

**Golden note:** MeDi-AD biomarker meta — favorable biomarkers.

**Diet and biomarkers of Alzheimer's disease: a systematic review and meta-analysis.**

*Neurobiology of aging*, 2018. Types: Journal Article; Meta-Analysis; Research Support, Non-U.S. Gov't; Systematic Review

> Alzheimer's disease (AD) risk increases with age and lacks efficacious pharmacological options. Summaries of the existing evidence reveal an association between Mediterranean-style diet adherence and reduced AD incidence; however, no review has investigated this relationship with respect to the hallmark AD biomarkers (tau and beta-amyloid) that manifest decades before clinical symptomatology. MEDLINE, PubMed, PsycINFO, Google Scholar, and SCOPUS databases were systematically searched to identify peer-reviewed articles investigating diet and AD biomarkers in the last 2 decades. Two thousand seven hundred twenty-six records were extracted, quality assessed, and double-blind screened by 2 authors. Fifteen studies met the inclusion criteria and 13 studies found a significant relationship. Of these, 4 studies found a high-glycemic load was related to an increase in AD biomarker burden; 6 found adherence to a Mediterranean or "AD-protective" dietary pattern conferred a reduction in AD biomarker burden. Meta-analysis revealed a small but significant effect of diet on AD biomarkers (β = 0.11 [95% CI 0.04-0.17], p = 0.002). This systematic review supports the notion that diet and nutrition display potential for nonpharmacological AD prevention.

---

### PMID 34835984 — current stance: `inconclusive`

**Evidence span:** > The Mediterranean diet showed promising results, whereas the role of the DASH diet was not clear.

**Golden note:** Nutrition RCT review — heterogeneous, inconsistent.

**Effects of Nutrition on Cognitive Function in Adults with or without Cognitive Impairment: A Systematic Review of Randomized Controlled Clinical Trials.**

*Nutrients*, 2021. Types: Journal Article; Systematic Review

> New dietary approaches for the prevention of cognitive impairment are being investigated. However, evidence from dietary interventions is mainly from food and nutrient supplement interventions, with inconsistent results and high heterogeneity between trials. We conducted a comprehensive systematic search of randomized controlled trials (RCTs) published in MEDLINE-PubMed, from January 2018 to July 2021, investigating the impact of dietary counseling, as well as food-based and dietary supplement interventions on cognitive function in adults with or without cognitive impairment. Based on the search strategy, 197 eligible publications were used for data abstraction. Finally, 61 articles were included in the analysis. There was reasonable evidence that dietary patterns, as well as food and dietary supplements improved cognitive domains or measures of brain integrity. The Mediterranean diet showed promising results, whereas the role of the DASH diet was not clear. Healthy food consumption improved cognitive function, although the quality of these studies was relatively low. The role of dietary supplements was mixed, with strong evidence of the benefits of polyphenols and combinations of nutrients, but with low evidence for PUFAs, vitamin D, specific protein, amino acids, and other types of supplements. Further well-designed RCTs are needed to guide the development of dietary approaches for the prevention of cognitive impairment.

---

### PMID 31240575 — current stance: `supports`

**Evidence span:** > This literature review indicated that adherence to a healthy dietary pattern has neuroprotective effects on AD prevention, while unhealthy diet can cause neurodegenerative effects in AD etiology.

**Golden note:** Dietary pattern-AD review — MeDi protective.

**Dietary pattern in relation to the risk of Alzheimer's disease: a systematic review.**

*Neurological sciences : official journal of the Italian Neurological Society and of the Italian Society of Clinical Neurophysiology*, 2019. Types: Journal Article; Systematic Review

> Alzheimer's disease (AD) is a progressive neurodegenerative disease leading to a gradual and irreversible loss of memory, linguistic skills, and perception of time and space, thinking, and behavior. Dietary pattern has been presented as a contributor to the incidence of Alzheimer's. This study aimed at reviewing the evidence on the relation between dietary pattern and AD. This systematic search was performed on the articles available in PubMed, Scopus, and Web of Sciences databases until May 2019 using keywords, including (diet, food, dietary pattern, food pattern) and (Alzheimer's disease) among observational studies. After excluding duplicated, and irrelevant studies, 26 studies were eligible for this review study. We categorized the studied dietary patterns into two groups: healthy and unhealthy diet. This study reviewed two case-control, five cross-sectional, and 19 prospective studies. Eight studies assessed unhealthy diet (high-fat diet, high-glycemic diet, sweetened sugary beverage, etc.) and the risk of AD. In addition, the other studies considered the effect of healthy diet such as Mediterranean diet, dietary approaches to stop hypertension (DASH), Mediterranean-DASH intervention for neurodegenerative delay, and seafood-rich diet on AD. This literature review indicated that adherence to a healthy dietary pattern has neuroprotective effects on AD prevention, while unhealthy diet can cause neurodegenerative effects in AD etiology. In conclusion, our findings showed that adherence to healthy diet can decrease oxidative stress and inflammation and accumulation of amyloid-β and consequently can decrease the risk of AD.

---

### PMID 39797935 — current stance: `supports`

**Evidence span:** > The combined HR for cognitive impairment among those adhering to the Mediterranean diet was 0.82 (95% CI 0.75-0.89); for dementia, the HR was 0.89 (95% CI 0.83-0.95); and for AD, the HR was 0.70 (95% CI 0.60-0.82), indicating substantial protective effects.

**Golden note:** MeDi-cognitive impairment/dementia/AD meta — reduces risk.

**The role of the Mediterranean diet in reducing the risk of cognitive impairement, dementia, and Alzheimer's disease: a meta-analysis.**

*GeroScience*, 2025. Types: Journal Article; Meta-Analysis; Systematic Review

> Age-related cognitive impairment and dementia pose a significant global health, social, and economic challenge. While Alzheimer's disease (AD) has historically been viewed as the leading cause of dementia, recent evidence reveals the considerable impact of vascular cognitive impairment and dementia (VCID), which now accounts for nearly half of all dementia cases. The Mediterranean diet-characterized by high consumption of fruits, vegetables, whole grains, fish, and olive oil-has been widely recognized for its cardiovascular benefits and may also reduce the risk of cognitive decline and dementia. To investigate the protective effects of the Mediterranean diet on cognitive health, we conducted a systematic literature review using PubMed, Web of Science, and Google Scholar, focusing on studies published between 2000 and 2024. The studies included in the meta-nalysis examined the adherence to the Mediterranean diet and the incidence of dementia and AD. We applied a random-effects model to calculate pooled hazard ratios (HRs) with 95% confidence intervals (CIs) and assessed heterogeneity through I-square statistics. Forest plots, funnel plots, and Z-score plots were used to visualize study outcomes. Of the 324 full-text records reviewed, 23 studies met the inclusion criteria. The combined HR for cognitive impairment among those adhering to the Mediterranean diet was 0.82 (95% CI 0.75-0.89); for dementia, the HR was 0.89 (95% CI 0.83-0.95); and for AD, the HR was 0.70 (95% CI 0.60-0.82), indicating substantial protective effects. Significant heterogeneity was observed across studies, though Z-score plots suggested sufficient sample sizes to support reliable conclusions for each condition. In conclusion, this meta-analysis confirms that adherence to the Mediterranean diet is associated with an 11-30% reduction in the risk of age-related cognitive disorders, including cognitive impairment, dementia, and AD. These findings underscore the Mediterranean diet's potential as a central element in neuroprotective public health strategies to mitigate the global impact of cognitive decline and dementia and to promote healthier cognitive aging.

---

### PMID 29574441 — current stance: `inconclusive`

**Evidence span:** > Adherence to a Mediterranean-style diet (MeDi) and insulin sensitivity were both positively associated with MRI-based cortical thickness (diet: βs≥0.26, insulin sensitivity βs≥0.58, P≤0.008).

**Golden note:** MRI biomarker cross-sectional — descriptive, lifestyle/vascular.

**Lifestyle and vascular risk effects on MRI-based biomarkers of Alzheimer's disease: a cross-sectional study of middle-aged adults from the broader New York City area.**

*BMJ open*, 2018. Types: Journal Article; Multicenter Study; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> OBJECTIVE: To investigate the effects of lifestyle and vascular-related risk factors for Alzheimer's disease (AD) on in vivo MRI-based brain atrophy in asymptomatic young to middle-aged adults. DESIGN: Cross-sectional, observational. SETTING: Broader New York City area. Two research centres affiliated with the Alzheimer's disease Core Center at New York University School of Medicine. PARTICIPANTS: We studied 116 cognitively normal healthy research participants aged 30-60 years, who completed a three-dimensional T1-weighted volumetric MRI and had lifestyle (diet, physical activity and intellectual enrichment), vascular risk (overweight, hypertension, insulin resistance, elevated cholesterol and homocysteine) and cognition (memory, executive function, language) data. Estimates of cortical thickness for entorhinal (EC), posterior cingulate, orbitofrontal, inferior and middle temporal cortex were obtained by use of automated segmentation tools. We applied confirmatory factor analysis and structural equation modelling to evaluate the associations between lifestyle, vascular risk, brain and cognition. RESULTS: Adherence to a Mediterranean-style diet (MeDi) and insulin sensitivity were both positively associated with MRI-based cortical thickness (diet: βs≥0.26, insulin sensitivity βs≥0.58, P≤0.008). After accounting for vascular risk, EC in turn explained variance in memory (P≤0.001). None of the other lifestyle and vascular risk variables were associated with brain thickness. In addition, the path associations between intellectual enrichment and better cognition were significant (βs≥0.25 P≤0.001), as were those between overweight and lower cognition (βs≥-0.22, P≤0.01). CONCLUSIONS: In cognitively normal middle-aged adults, MeDi and insulin sensitivity explained cortical thickness in key brain regions for AD, and EC thickness predicted memory performance in turn. Intellectual activity and overweight were associated with cognitive performance through different pathways. Our findings support further investigation of lifestyle and vascular risk factor modification against brain ageing and AD. More studies with larger samples are needed to replicate these research findings in more diverse, community-based settings.

---

### PMID 38311314 — current stance: `supports`

**Evidence span:** > Higher MIND diet adherence was protective of dementia in 7 of 10 cohorts.

**Golden note:** MIND diet review — positive (MeDi-derived).

**The Mediterranean-Dietary Approaches to Stop Hypertension Intervention for Neurodegenerative Delay (MIND) Diet for the Aging Brain: A Systematic Review.**

*Advances in nutrition (Bethesda, Md.)*, 2024. Types: Journal Article; Systematic Review

> The Mediterranean-Dietary Approaches to Stop Hypertension Intervention for Neurodegenerative Delay (MIND) diet seems a promising approach to preserve brain function during aging. Previous systematic reviews have demonstrated benefits of the MIND diet for cognition and dementia, though an update is needed. Additionally, other outcomes relevant to brain aging have not been summarized. Therefore, this systematic review aims to give an up-to-date and complete overview on human studies that examined the MIND diet in relation to brain aging outcomes in adults aged ≥40 y. Ovid Medline, Web of Science core collection, and Scopus were searched up to July 25, 2023. Study quality was assessed using the Newcastle-Ottawa Scale and the Cochrane Risk-of-Bias tool. We included 40 articles, of which 32 were unique cohorts. Higher MIND diet adherence was protective of dementia in 7 of 10 cohorts. Additionally, positive associations were demonstrated in 3 of 4 cohorts for global cognition and 4 of 6 cohorts for episodic memory. The protective effects of the MIND diet on cognitive decline are less apparent, with only 2 of 7 longitudinal cohorts demonstrating positive associations for global decline and 1 of 6 for episodic memory decline. For other brain outcomes (domain-specific cognition, cognitive impairments, Parkinson's disease, brain volume, and pathology), results were mixed or only few studies had been performed. Many of the cohorts demonstrating protective associations were of North American origin, raising the question if the most favorable diet for healthy brain aging is population-dependent. In conclusion, this systematic review provides observational evidence for protective associations between the MIND diet and global cognition and dementia risk, but evidence for other brain outcomes remains mixed and/or limited. The MIND diet may be the preferred diet for healthy brain aging in North American populations, though evidence for other populations seems less conclusive. This review was registered at PROSPERO as CRD42022254625.

---

### PMID 29728772 — current stance: `supports`

**Evidence span:** > The PREDIMED study confirmed reductions in CVD-related mortality with a MedDiet; a meta-analysis in over 4.7 million people showed reduced mortality, CVD-related mortality, and reduced risk of Parkinson's and Alzheimer's disease.

**Golden note:** Implementing MeDi outside Mediterranean — positive RCT review.

**Implementing a Mediterranean-Style Diet Outside the Mediterranean Region.**

*Current atherosclerosis reports*, 2018. Types: Journal Article; Meta-Analysis; Review

> PURPOSE OF REVIEW: Populations surrounding the Mediterranean basin have traditionally reaped health benefits from a Mediterranean diet (MedDiet), which may benefit Westernized countries plagued by chronic disease. But is it feasible to implement beyond the Mediterranean? To answer this question, we present evidence from randomized controlled trials that achieved high dietary compliance rates with subsequent physical and mental health benefits. RECENT FINDINGS: In the 1960s, the Seven Countries Study identified dietary qualities of Mediterranean populations associated with healthy aging and longevity. The PREDIMED study confirmed reductions in CVD-related mortality with a MedDiet; a meta-analysis in over 4.7 million people showed reduced mortality, CVD-related mortality, and reduced risk of Parkinson's and Alzheimer's disease. Continually emerging research supports the MedDiet's benefits for chronic diseases including metabolic syndrome, cancers, liver disease, type 2 diabetes, depression, and anxiety. We summarize components of studies outside the Mediterranean that achieved high compliance to a Med-style diet: dietitian led, dietary education, goal setting, mindfulness; recipe books, meal plans, and food checklists; food hampers; regular contact between volunteers and staff through regular cooking classes; clinic visits; and recipes that are simple, palatable, and affordable. The next step is testing the MedDiet's feasibility in the community. Potential obstacles include access to dietetic/health care professionals, high meat intake, pervasive processed foods, and fast food outlets. For Western countries to promote a Med-style diet, collective support from government, key stakeholders and policy makers, food industry, retailers, and health professionals is needed to ensure the healthiest choice is the easiest choice.

---

### PMID 32427314 — current stance: `supports`

**Evidence span:** > For the recalculated meta-analyses, quality of evidence was moderate for inverse associations between higher adherence to the Mediterranean diet (SRR: 0.63; 95% CI: 0.48, 0.82; n = 4 primary studies) and higher fish intake (SRR: 0.72; 95% CI: 0.59, 0.89; n = 6) and Alzheimer disease.

**Golden note:** Umbrella prospective — MeDi reduces neurodegen incidence.

**Dietary Factors and Neurodegenerative Disorders: An Umbrella Review of Meta-Analyses of Prospective Studies.**

*Advances in nutrition (Bethesda, Md.)*, 2020. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> Diet has been hypothesized to be associated with neurodegenerative disorders. The aim was to conduct an umbrella review to summarize and evaluate the current evidence of prospective associations between any dietary factors and the incidence of neurodegenerative disorders. We conducted a systematic search in PubMed, Embase, and the Cochrane library up to November 2019 to identify systematic reviews with meta-analyses of prospective studies investigating the association between dietary factors (dietary patterns, foods and beverages, nutrients, and phytochemicals) and neurodegenerative disorders (cognitive decline, cognitive impairment, Alzheimer disease, all-cause dementia, and Parkinson disease). Summary risk ratios (SRRs) and 95% CIs were recalculated using a random effects model. We evaluated the risk of bias of identified meta-analyses and the quality of evidence for all associations. In total, 20 meta-analyses including 98 SRRs were identified. All original meta-analyses were rated as being at high risk of bias. Methodological concerns related mainly to the inappropriate synthesis, assessment, and discussion of the risk of bias of primary studies. For the recalculated meta-analyses, quality of evidence was moderate for inverse associations between higher adherence to the Mediterranean diet (SRR: 0.63; 95% CI: 0.48, 0.82; n = 4 primary studies) and higher fish intake (SRR: 0.72; 95% CI: 0.59, 0.89; n = 6) and Alzheimer disease, as well as for tea consumption and all-cause dementia (SRR: 0.74; 95% CI: 0.63, 0.88; n = 2) and Parkinson disease (SRR per 2 cups/d: 0.69; 95% CI: 0.54, 0.87; n = 5). This umbrella review provides a comprehensive overview of the available evidence on dietary factors and neurodegenerative disorders. The results indicate that the Mediterranean diet, fish, and tea could be inversely associated with neurodegenerative disorders. However, the quality of evidence was generally low, suggesting that further studies are likely to change the overall estimates. Thus, more well-conducted research, also investigating other dietary factors in association with neurodegenerative disorders, is warranted.

---

### PMID 34392373 — current stance: `inconclusive`

**Evidence span:** > Findings were mixed, with some studies reporting a significant positive relationship between adherence to various "healthy" dietary patterns and neurocognition, but others reporting no such relationship.

**Golden note:** Mid-life dietary patterns — concurrent neurocognition mixed.

**Dietary patterns in middle age: effects on concurrent neurocognition and risk of age-related cognitive decline.**

*Nutrition reviews*, 2022. Types: Journal Article; Systematic Review; Research Support, Non-U.S. Gov't

> CONTEXT: Diet plays a critical role in cognitive integrity and decline in older adults. However, little is known about the relationship between diet and cognitive integrity in middle age. OBJECTIVE: To investigate the relationship between dietary patterns in healthy middle-aged adults and neurocognition both in middle age and later in life. DATA SOURCES: Using the Preferred Reporting Items for Systematic Reviews and Meta-Analysis (PRISMA) guidelines, the following electronic databases were searched: Web of Science, Scopus, PubMed, and PsychInfo. DATA EXTRACTION: Data from eligible articles was extracted by 2 reviewers. DATA ANALYSIS: Articles included in the systematic review were synthesized (based on the synthesis without meta-analysis reporting guidelines) and assessed for quality (using the Joanna Briggs Institute checklist for randomized controlled trials, cohort studies, and cross-sectional studies) by 2 reviewers. RESULTS: Of 1558 studies identified, 34 met the eligibility criteria for inclusion. These comprised 9 cross-sectional studies, 23 longitudinal or prospective cohort studies, and 2 randomized controlled trials. Findings were mixed, with some studies reporting a significant positive relationship between adherence to various "healthy" dietary patterns and neurocognition, but others reporting no such relationship. CONCLUSION: This systematic review demonstrated that adherence to the Mediterranean diet and other healthy dietary patterns in middle age can protect neurocognition later in life. SYSTEMATIC REVIEW REGISTRATION: PROSPERO registration no. CRD42020153179.

---

### PMID 33336232 — current stance: `supports`

**Evidence span:** > Thus, 1) adherence to a Mediterranean diet (GRADE 1B); 2) high-level of consumption of mono- or poly- unsaturated fatty acids combined to a low consumption of saturated fatty acids (GRADE 1B); 3) high consumption of fruits and vegetables (GRADE 1B); 4) higher vitamin D intake (GRADE 1C) than the recommended daily allowance.

**Golden note:** GRADE recommendation — MeDi recommended.

**Nutrition to Prevent or Treat Cognitive Impairment in Older Adults: A GRADE Recommendation.**

*The journal of prevention of Alzheimer's disease*, 2021. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> Aging is associated with cognitive declines leading to mild cognitive impairments or Alzheimer disease. Nutrition appear to protect from aging. Some dietary factors could either increase or protect against cognitive declines. This article aimed to provide GRADE recommendations related to nutrition aspects able to prevent or to treat cognitive impairments. A comprehensive literature review was performed using Medline database. The GRADE approach was used to classify quality of the existing evidence (systematic review or meta-analysis).The GRADE process led us to formulate seven key nutritional recommendations to manage cognitive declines, but did not allow us to do it for protein, vitamin B or antioxidants. Thus, 1) adherence to a Mediterranean diet (GRADE 1B); 2) high-level of consumption of mono- or poly- unsaturated fatty acids combined to a low consumption of saturated fatty acids (GRADE 1B); 3) high consumption of fruits and vegetables (GRADE 1B); 4) higher vitamin D intake (GRADE 1C) than the recommended daily allowance. In addition, a ketogenic diet, a low consumption of whole-fat dairy products or a caloric restriction are promising nutritional habits although the evidence does not yet support widespread uptake (GRADE 2C). In conclusion, nutrition is an important modifiable factor to prevent or protect against cognitive decline. Nevertheless, more studies are required to determine specific guidelines such as duration and amounts of nutrients to help older adult to maintain a healthy cognitive life.

---

### PMID 36529364 — current stance: `inconclusive` [FLIP from supports → inconclusive]

**Evidence span:** > Four studies reported on hippocampal volume, with inconclusive or no associations seen with MedDiet adherence. Two studies found a significant association between higher MedDiet adherence and lower WMHV, while two other studies found no significant associations.

**Golden note:** MeDi neuroimaging biomarker review — favorable.

**Mediterranean diet and structural neuroimaging biomarkers of Alzheimer's and cerebrovascular disease: A systematic review.**

*Experimental gerontology*, 2022. Types: Systematic Review; Journal Article

> Previous studies have demonstrated an association between adherence to the Mediterranean diet (MedDiet) and better cognitive performance, lower incidence of dementia and lower Alzheimer's disease biomarker burden. The aim of this systematic review was to evaluate the evidence base for MedDiet associations with hippocampal volume and white matter hyperintensity volume (WMHV). We searched systematically for studies reporting on MedDiet and hippocampal volume or WMHV in MedLine, EMBASE, CINAHL and PsycInfo. Searches were initially carried out on 21st July 2021 with final searches run on 23rd November 2022. Risk of bias was assessed using the NIH Quality Assessment Tool for Observational Cohort and Cross-Sectional Studies. Of an initial 112 papers identified, seven papers were eligible for inclusion in the review reporting on 21,933 participants. Four studies reported on hippocampal volume, with inconclusive or no associations seen with MedDiet adherence. Two studies found a significant association between higher MedDiet adherence and lower WMHV, while two other studies found no significant associations. Overall these results highlight a gap in our knowledge about the associations between the MedDiet and AD and cerebrovascular related structural neuroimaging findings.

---

### PMID 38961421 — current stance: `inconclusive`

**Evidence span:** > These results suggest that dietary intervention as part of multimodal lifestyle interventions is feasible and results in improved dietary quality in a population with prodromal AD.

**Golden note:** MIND-ADmini multimodal — diet quality improved, no cognitive primary.

**Nutrition guidance within a multimodal intervention improves diet quality in prodromal Alzheimer's disease: Multimodal Preventive Trial for Alzheimer's Disease (MIND-ADmini).**

*Alzheimer's research & therapy*, 2024. Types: Journal Article; Randomized Controlled Trial; Multicenter Study; Research Support, Non-U.S. Gov't

> BACKGROUND: Multimodal lifestyle interventions can benefit overall health, including cognition, in populations at-risk for dementia. However, little is known about the effect of lifestyle interventions in patients with prodromal Alzheimer's disease (AD). Even less is known about dietary intake and adherence to dietary recommendations within this population making it difficult to design tailored interventions for them. METHOD: A 6-month MIND-ADmini pilot randomized controlled trial (RCT) was conducted among 93 participants with prodromal AD in Sweden, Finland, Germany, and France. Three arms were included in the RCT: 1) multimodal lifestyle intervention (nutritional guidance, exercise, cognitive training, vascular/metabolic risk management, and social stimulation); 2) multimodal lifestyle intervention + medical food product; and 3) regular health advice (control group). Adherence to dietary advice was assessed with a brief food intake questionnaire by using the Healthy Diet Index (HDI) and Mediterranean Diet Adherence Screener (MEDAS). The intake of macro- and micronutrients were analyzed on a subsample using 3-day food records. RESULTS: The dietary quality in the intervention groups, pooled together, improved compared to that of the control group at the end of the study, as measured with by HDI (p = 0.026) and MEDAS (p = 0.008). The lifestyle-only group improved significantly more in MEDAS (p = 0.046) and almost significantly in HDI (p = 0.052) compared to the control group, while the lifestyle + medical food group improved in both HDI (p = 0.042) and MEDAS (p = 0.007) during the study. There were no changes in macro- or micronutrient intake for the intervention groups at follow-up; however, the intakes in the control group declined in several vitamins and minerals when adjusted for energy intake. CONCLUSION: These results suggest that dietary intervention as part of multimodal lifestyle interventions is feasible and results in improved dietary quality in a population with prodromal AD. Nutrient intakes remained unchanged in the intervention groups while the control group showed a decreasing nutrient density. TRIAL REGISTRATION: ClinicalTrials.gov NCT03249688, 2017-07-08.

---

### PMID 39861466 — current stance: `supports`

**Evidence span:** > The findings suggest that adherence to the Mediterranean and Nordic diets is generally associated with improved cognitive function and delayed cognitive decline and that adherence to both these diets can improve cognitive function.

**Golden note:** MeDi/Nordic diet adherence systematic review — protective.

**Dietary Intake, Mediterranean and Nordic Diet Adherence in Alzheimer's Disease and Dementia: A Systematic Review.**

*Nutrients*, 2025. Types: Systematic Review; Journal Article

> BACKGROUND/OBJECTIVES: Dementia is not a single disease but an umbrella term that encompasses a range of symptoms, such as memory loss and cognitive impairments, which are severe enough to disrupt daily life. One of the most common forms of dementia is Alzheimer's Disease (AD), a complex neurodegenerative condition influenced by both genetic and environmental factors. Recent research has highlighted diet as a potential modifiable risk factor for AD. Decades of research have explored the role of dietary patterns, including the Mediterranean Diet (MD) and its components, in neuroprotection and cognitive health. Systematic review examines studies investigating the impact of the Mediterranean Diet, Mediterranean-like diets, the Nordic Diet (ND), dietary intake patterns, and specific components such as extra virgin olive oil and rapeseed oil on cognitive function, disease onset, and progression in AD and dementia. METHODS: A comprehensive search of PubMed, the Directory of Open Access Journals, and the Social Science Research Network was conducted independently by two reviewers using predefined search terms. The search period included studies from 2006 to 2024. Eligible studies meeting the inclusion criteria were systematically reviewed, yielding 88 studies: 85 focused on the MD and its relationship to AD and dementia, while only 3 investigated the ND. RESULTS: The findings suggest that adherence to the Mediterranean and Nordic diets is generally associated with improved cognitive function and delayed cognitive decline and that adherence to both these diets can improve cognitive function. Some studies identified that higher legume consumption decreased dementia incidence, while fruits and vegetables, carbohydrates, and eggs lowered dementia prevalence. Most studies demonstrated that high MD or ND adherence was associated with better cognitive function and a lower risk of poor cognition in comparison to individuals with lower MD or ND adherence. However, some studies reported no significant benefits of the MD on cognitive outcomes, while two studies indicated that higher red meat consumption was linked to better cognitive function. CONCLUSION: Despite promising trends, the evidence remains varying across studies, underscoring the need for further research to establish definitive associations between diet and cognitive function. These findings highlight the essential role of dietary interventions in the prevention and management of dementia and AD, therefore offering critical insights into the underlying mechanisms by which the diet may impact brain health.

---

### PMID 40744415 — current stance: `supports`

**Evidence span:** > Among 92,849 participants with 21,478 cases, higher baseline scores of the 4 dietary patterns were associated with 4%‒9% lower ADRD risk (for aMED, HR 0.91, 95% CI: 0.87, 0.95; for DASH, HR 0.96, 95% CI: 0.92, 1.01; for HEI-2015, HR 0.94, 95% CI: 0.90, 0.98; for MIND, HR 0.91, 95% CI: 0.87, 0.96) over the follow-up.

**Golden note:** Multiethnic cohort — diet patterns lower ADRD risk across groups.

**Dietary patterns and risk of Alzheimer's disease and related dementias across 5 racial and ethnic groups in the Multiethnic Cohort Study.**

*The American journal of clinical nutrition*, 2025. Types: Journal Article; Observational Study

> BACKGROUND: Healthier dietary patterns have been linked to a lower risk of dementia, but data from diverse racial and ethnic populations are limited, particularly to support dietary improvement in older adults. OBJECTIVES: We examined dietary patterns in relation to late-onset Alzheimer's disease and related dementia (ADRD) risk across 5 racial and ethnic groups in the Multiethnic Cohort Study. METHODS: Participants were scored for 4 predefined dietary pattern indices based on their food frequency questionnaire responses at baseline (45-75 y) and at a 10-y follow-up: the alternate Mediterranean diet (aMED), the Dietary Approaches to Stop Hypertension (DASH), the Healthy Eating Index-2015 (HEI-2015), and the Mediterranean-DASH Intervention for Neurodegenerative Delay (MIND) diet. Associations between dietary patterns and ADRD were examined using Cox proportional hazards models to estimate hazard ratios (HRs) and 95% confidence intervals (CIs). RESULTS: Among 92,849 participants with 21,478 cases, higher baseline scores of the 4 dietary patterns were associated with 4%‒9% lower ADRD risk (for aMED, HR 0.91, 95% CI: 0.87, 0.95; for DASH, HR 0.96, 95% CI: 0.92, 1.01; for HEI-2015, HR 0.94, 95% CI: 0.90, 0.98; for MIND, HR 0.91, 95% CI: 0.87, 0.96) over the follow-up, with stronger associations observed in African American, Latino, and White participants than in Japanese American and Native Hawaiian participants. Dietary improvement over 10 y was associated with 11%‒25% lower risk across the 4 indices in a subset of 45,065 participants with 8360 cases, with similar racial and ethnic differences as observed for baseline diet, but consistently for younger (<60 y at baseline) and older age groups. CONCLUSIONS: Healthy dietary patterns in mid- to late-life and improvement in older age were associated with a reduced risk of ADRD in a diverse population. The racial and ethnic heterogeneity in the relationships observed warrants further study.

---

### PMID 41259881 — current stance: `supports`

**Evidence span:** > Higher MD adherence was associated with reduced risk or prevalence of Alzheimer's disease (odds ratios = 0.92), mild cognitive impairment (RR = 0.93), depression (RR = 0.96), and Parkinson's disease (RR = 0.90), with moderate certainty of evidence.

**Golden note:** Italian guidelines MeDi neurological prevention meta — positive.

**Efficacy of Mediterranean diet for the prevention of neurological diseases: A systematic review and meta-analysis featured in the Italian National Guidelines "La Dieta Mediterranea".**

*Nutrition (Burbank, Los Angeles County, Calif.)*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Neurological diseases, including Alzheimer's disease, depression, and Parkinson's disease, pose a growing public health challenge. Dietary patterns, particularly the Mediterranean diet (MD), have been proposed as modifiable factors for prevention. The aim of this systematic review and meta-analysis was to evaluate the association between adherence to the MD and the risk or progression of neurological conditions. METHODS: This review was conducted in accordance with PRISMA 2020 and MOOSE guidelines. A comprehensive search of PubMed/MEDLINE, Scopus, Embase, and Cochrane Library was performed up to February 28, 2024. Study quality was assessed using the Newcastle-Ottawa Scale, and the certainty of evidence was evaluated with the NUTRIGRADE approach. Pooled effect sizes were computed using a random-effects model and expressed as risk ratios (RR), hazard ratios, or odds ratios, as appropriate. RESULTS: Forty-five studies involving over 730 000 participants were included. Higher MD adherence was associated with reduced risk or prevalence of Alzheimer's disease (odds ratios = 0.92), mild cognitive impairment (RR = 0.93), depression (RR = 0.96), and Parkinson's disease (RR = 0.90), with moderate certainty of evidence. Limited evidence suggested reduced anxiety and lower mortality among patients with Alzheimer's disease. No significant associations were observed for dementia prevalence or progression from mild cognitive impairment to dementia. CONCLUSIONS: Greater adherence to the MD is consistently associated with a lower risk of several neurological and mental health conditions. These findings support the promotion of MD-based dietary patterns in clinical and public health strategies to prevent cognitive decline and enhance healthy aging.

---

### PMID 39499795 — current stance: `inconclusive`

**Evidence span:** > Both observational studies and clinical trials yielded inconclusive results attributed to both practical limitations associated with longitudinal follow-up and issues of methodological quality.

**Golden note:** APOE × dietary patterns umbrella — interaction-focused, mixed.

**APOE ε4 and Dietary Patterns in Relation to Cognitive Function: An Umbrella Review of Systematic Reviews.**

*Nutrition reviews*, 2025. Types: Journal Article; Systematic Review

> CONTEXT: Carrying the apolipoprotein ε4 allele (APOE ε4) is the strongest genetic risk factor for late-onset Alzheimer's disease. There is some evidence suggesting that APOE ε4 may modulate the influence of diet on cognitive function. OBJECTIVE: This umbrella review of systematic reviews evaluates the existing literature on the effect of dietary interventions on cognitive and brain-imaging outcomes by APOE status. DATA SOURCES: PubMed, EMBASE, Web of Science, and Scopus were searched using terms appropriate to each area of research, from their respective starting dates of coverage until March 2023. DATA EXTRACTION: Two independent reviewers conducted data extraction and performed a quality appraisal using the Measurement Tool to Assess Systematic Reviews (AMSTAR) 2. DATA ANALYSIS: Six total reviews were included in the final analysis. Four reviews evaluated randomized controlled trials on individuals aged 50-93 years ranging the entire cognitive continuum. One review combined observational studies and clinical trials conducted on both cognitively healthy and cognitively impaired individuals (age range: 50-90), and 1 review included observational studies of both cognitively healthy and cognitively impaired adults (age range: 50-75). RESULTS: Both observational studies and clinical trials yielded inconclusive results attributed to both practical limitations associated with longitudinal follow-up and issues of methodological quality. Except for the Mediterranean diet, dietary interventions, such as the ketogenic diet, nutraceuticals, and supplements, were generally not effective in older APOE ε4 carriers. This review considers plausible biological mechanisms that might explain why older and cognitively impaired APOE ε4 carriers were less likely to benefit. CONCLUSION: This review identifies notable gaps in the literature, such as a shortage of studies conducted in middle-aged and cognitively healthy APOE ε4 carriers assessing the impact of dietary interventions and provides suggestions for novel trial designs.

---

### PMID 40378769 — current stance: `inconclusive`

**Evidence span:** > In this group of older adults at risk for dementia, we find no conclusive evidence whether a multi-modal lifestyle intervention improves brain imaging markers of neurodegeneration and small vessel disease.

**Golden note:** AgeWell.de multi-modal MRI — descriptive imaging.

**Exploring the effect of multi-modal intervention against cognitive decline on atrophy and small vessel disease imaging markers in the AgeWell.de imaging study.**

*NeuroImage. Clinical*, 2025. Types: Journal Article; Randomized Controlled Trial; Multicenter Study

> BACKGROUND: Multimodal lifestyle interventions might help to maintain healthy cognition in older age and to delay onset of dementia. Here, we studied the effects of a multi-modal lifestyle-based intervention, based on the FINGER trial, on magnetic resonance imaging (MRI) markers of hippocampal-limbic atrophy and cerebral small vessel disease in older adults at increased risk for dementia in Germany. METHODS: Leipzig participants of the multicenter AgeWell.de randomized controlled trial underwent neuroimaging before and after a two year intervention at 3 Tesla MRI. We extracted hippocampal volume and entorhinal cortex thickness (ECT), free water fraction (FW), peak width of skeletonized mean diffusivity (PSMD), white matter hyperintensity volume and mean gray matter cerebral blood flow and assessed the effect of the intervention on these imaging markers using linear mixed models. We also tested the effect of the intervention on the hippocampus-dependent Mnemonic Similarity Test and fixel-based white matter microstructure. RESULTS: 56 individuals (mean (sd) age: 68.8 (4.2) years, 26 females, 24/32 intervention/control group) were included at baseline and 41 returned after an average of 28 months for the second assessment. ECT and FW exhibited stronger decline in the intervention compared to the control group in preregistered models but not when adjusted for baseline differences. All other markers progressed similarly across groups, however sample size was smaller than expected. In exploratory analyses, cerebral blood flow increased more in the intervention group and this change was associated with decreases in systolic blood pressure. CONCLUSIONS: In this group of older adults at risk for dementia, we find no conclusive evidence whether a multi-modal lifestyle intervention improves brain imaging markers of neurodegeneration and small vessel disease. Preliminary evidence suggested an association of the intervention, increased cerebral blood flow and systolic blood pressure reductions. ABBREVIATIONS: ECT, entorhinal cortex thickness; FW, free water fraction; WHO, world health organization; AD, Alzheimer's disease; VCI, vascular cognitive impairment; FINGER, Finnish Geriatric Intervention Study to Prevent Cognitive Impairment and Disability; MTL, medial temporal lobe; MIND, Mediterranean-DASH Intervention for Neurodegenerative Delay diet; cSVD, cerebral small vessel disease; WMH, white matter hyperintensities of presumed vascular origin; PSMD, peak width of the mean diffusivity distribution; WW-FINGERS, world wide FINGER studies; CAIDE, Cardiovascular Risk Factors, Aging, and Incidence of Dementia; GPP, general practitioner praxis; MRI, magnetic resonance imaging; MST, Mnemonic Similarity Test; TE, echo time; TR, repetition time; FA, flip angle; FOV, field of view; GRAPPA, GeneRalized Autocalibrating Partial Parallel Acquisition; CMRR, Center for Magnetic Resonance Research; BOLD, blood oxygenation level dependent; pcASL: pseudo-continuous arterial spin labeling; EPI, echo-planar imaging; FLAIR, fluid attenuated inversion recovery; CBF, cerebral blood flow; QA, quality assessment; GM, gray matter; HCV, hippocampal volume; eICV, estimated intracranial volume; DWI, diffusion-weighted imaging; MD, mean diffusivity; FA, fractional anisotropy TBSS: tract-based spatial statistics; CSF, cerebral spinal fluid; ISI, inter-stimulus interval; LDI, lure discrimination index; REC, recognition score; CG, control group; IG, intervention group; MoCA, Montreal Cognitive Assessment; CASMIN, Comparative Analysis of Social Mobility in Industrial Nations; BMI, body mass index; SBP/DBP, systolic/diastolic blood pressure; OSF, open science framework; LMM, linear mixed model; ANOVA, analysis of covariance.

---

### PMID 41599807 — current stance: `inconclusive` [FLIP from supports → inconclusive]

**Evidence span:** > A structured, non-restrictive MIND intervention was feasible, improved dietary adherence, and accompanied higher diversity and compositional remodeling of the GM in ALZ's disease.

**Golden note:** MIND pattern + MeDi adherence in AD — positive.

**MIND Pattern Nutritional Intervention Modulates Mediterranean Diet Adherence and Gut Microbiota in Alzheimer's Disease: An Observational Case-Control Study.**

*Nutrients*, 2026. Types: Journal Article; Observational Study

> Background: Evidence on non-restrictive MIND pattern interventions in Alzheimer's (ALZ) disease remains limited. Methods: In an observational case-control study, 60 participants (ALZ, n = 30; cognitively healthy controls, n = 30) completed baseline (T0) and follow-up (T1) after structured MIND counseling. Adherence was assessed via the MEDAS questionnaire. Stool samples (16S rRNA profiling) were taken and anthropometry and cognitive/functional measures were recorded at T0/T1. Results: In the ALZ group, MEDAS improved as adherence to the Mediterranean diet increased (increasing the use of vegetables ≥ 2/day, p < 0.01; and lowering butter adoption ≤ 1/day, p = 0.02), with a shift from low to moderate/high adherence; in controls, baseline Mediterranean diet adherence was already high, and changes in MEDAS categories were modest (low adherence from 13.8% to 3.6%, high adherence from 37.9% to 50.0%), with no statistically significant overall change (p = 0.39). Regarding gut microbiota (GM), in the ALZ group, alpha diversity increased significantly and Bray-Curtis PCoA separated T0 from T1. Species-level analysis showed increases in SCFA-linked taxa (e.g., Anaerobutyricum hallii, Blautia luti, Eubacterium coprostanoligenes) and reductions in dysbiosis/mucin-degrading taxa (e.g., Mediterraneibacter torques, M. gnavus, Agathobacter rectalis). Between-group Δ(T1 - T0) comparisons at the genus level indicated larger positive shifts in ALZ for Anaerobutyricum, Oscillibacter, Faecalicatena, Romboutsia, Mediterraneibacter, and Blautia, and more negative Δ for Gemmiger, Subdoligranulum, Bifidobacterium, Clostridium, and Collinsella. sPLS-DA showed partial separation (first two components ≈ 9% variance). Conclusions: A structured, non-restrictive MIND intervention was feasible, improved dietary adherence, and accompanied higher diversity and compositional remodeling of the GM in ALZ's disease. Larger randomized mechanistic studies are warranted.

---

### PMID 29147948 — current stance: `supports`

**Evidence span:** > In a multivariate model, compared with men having a MD score in the lowest quintile, those in the highest quintile had a 36% lower odds of a poor SCF score (odds ratio 0.64, 95% CI 0.55-0.75; P, trend < 0.001) and a 24% lower odds of a moderate SCF score (OR 0.76, 95% CI 0.70-0.83; P, trend < 0.001).

**Golden note:** MeDi + subjective cognitive function in men prospective — positive.

**Adherence to Mediterranean diet and subjective cognitive function in men.**

*European journal of epidemiology*, 2017. Types: Journal Article; Observational Study; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> Benefits of a Mediterranean diet for cognition have been suggested, but epidemiologic studies have been relatively small and of limited duration. To prospectively assess the association between long-term adherence to a Mediterranean dietary pattern and self-reported subjective cognitive function (SCF). Prospective observational study. The Health Professionals' Follow-up Study, a prospective cohort of 51,529 men, 40-75 years of age when enrolled in 1986, of whom 27,842 were included in the primary analysis. Mediterranean diet (MD) score, computed from the mean of five food frequency questionnaires, assessed every 4 years from 1986 to 2002. Self-reported SCF assessed by a 6-item questionnaire in 2008 and 2012, and validated by association with genetic variants in apolipoprotein-4. Using the average of 2008 and 2012 SCF scores, 38.0% of men were considered to have moderate memory scores and 7.3% were considered to have poor scores. In a multivariate model, compared with men having a MD score in the lowest quintile, those in the highest quintile had a 36% lower odds of a poor SCF score (odds ratio 0.64, 95% CI 0.55-0.75; P, trend < 0.001) and a 24% lower odds of a moderate SCF score (OR 0.76, 95% CI 0.70-0.83; P, trend < 0.001). Both remote and more recent diet contributed to this relation. Associations were only slightly weaker using baseline dietary data and a lag of 22 years. Long-term adherence to the Mediterranean diet pattern was strongly related to lower subjective cognitive function. These findings provide further evidence that a healthy dietary pattern may prevent or delay cognitive decline.

---

