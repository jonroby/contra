# Q9: Does coconut oil / MCT supplementation improve cognition in Alzheimer's?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=22 PMIDs.

**Current S/C/I**: 9 / 2 / 11
**Proposed S/C/I**: 6 / 4 / 12
**Net flips**: 8 (4 S→I, 1 S→C, 1 I→C, 2 I→S)

`expected_consensus: "mostly negative"` is partly correct — the two
pivotal RCTs (NOURISH AD and VCO-AD) are properly flagged as
`contradicts`, but the corpus has scope drift (frail-elderly studies, KD
broad reviews) that confuses the picture.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `26811674` | 2016 | **supports → contradicts** | Axona Japanese pilot, n=22, open-label. Verbatim conclusion: *"**Axona did not improve cognitive function in our sample of AD patients**, even in those patients without the ApoE4 allele."* Only a small APOE4-negative subgroup with MMSE ≥14 showed improvement. Headline is null. The current `supports` label is wrong. |
| `33622392` | 2021 | **supports → inconclusive** | Modified ketogenic diet AD crossover, n=26, 12 wk. ADCS-ADL +3.13 (p=0.0067) and QOL-AD +3.37 (p=0.023) sig, but **the cognitive primary (ACE-III) was not significant** (+2.12, p=0.24). Mixed: cognitive primary missed, daily-function/QOL secondary sig. Genuinely mixed → `inconclusive`. |
| `30056419` | 2018 | **supports → inconclusive** | Coconut oil + Mediterranean diet pilot, n=44, **21 days**. Qualitative descriptive study, no formal cognitive primary, very short duration. The combo intervention also confounds cocoanut-oil-specific effect. Pilot exempt to inconclusive. |
| `28552878` | 2017 | **supports → inconclusive** | MCT + leucine + vitamin D3 in **frail elderly** (n=38, mean age 86.6, MMSE ~17 at nursing homes). Population is elderly with cognitive impairment, but **not specifically AD**. Combo intervention (3 actives) confounds MCT effect. Off-target population for the AD question. |
| `32652024` | 2020 | **supports → inconclusive** | MCT alone in **frail elderly** (n=64, mean age 85.5, BMI 18.6, secondary outcome cognition). Same population concern as above — frail nursing home elderly, not AD. Off-target. |
| `32597927` | 2020 | **inconclusive → supports** | KD-AD systematic review, 10 RCTs. Verbatim: *"The use of ketoneurotherapeutics proved effective in improving general cognition using the Alzheimer's Disease Assessment Scale-Cognitive, in interventions of either duration. In addition, long-term ketogenic therapy improved episodic and secondary memory."* Pooled positive on cognition. The note "modest, inconsistent" undersells the conclusion. |
| `38943982` | 2024 | **inconclusive → supports** | KD-AD meta of 10 RCTs, n=691. MMSE +1.25 (p=0.002) and ADAS-Cog -3.43 (p=0.008), both significant. Verbatim: *"the KD can enhance the mental state and cognitive function of those with AD."* Significantly positive pooled effect. |
| `28807434` | 2017 | **inconclusive → contradicts** | Network meta of nutrition strategies in AD, including MCT. Verbatim: *"Isolated nutrient supplementations show no convincing evidence of providing a significant benefit on clinical manifestations or neuropathology of AD."* And: *"The other nutrients supplementation did not show any significant effect on any outcome measures"* (with MCT explicitly among "other nutrients"). Strict bar criterion met: meta-analysis concluding "evidence does not support." |

### Borderline (not flipped, but flagged for cross-question policy decisions)

| PMID | Year | Current | Policy issue | Notes |
|------|------|---------|--------------|-------|
| `15123336` | 2004 | `supports` | (a) subgroup-positive in exploratory/null parent | Reger 2004 β-OHB acute, n=20, single-dose crossover, explicitly exploratory ("Additional research is warranted"). Headline acute ADAS-Cog benefit was driven by APOE4-negative subgroup only ("MCT treatment facilitated performance on the ADAS-cog for 4- subjects, but not for 4+ subjects"). Whole-sample primary not separately reported as significant. Under strict bar this is canonically `inconclusive` (small N, exploratory pilot), but it's a foundational pilot for the MCT-AD literature so is currently `supports` by tradition. Flag, don't flip — depends on cross-question rule for "subgroup positive in exploratory parent." |
| `33622392` | 2021 | `supports` (proposed → `inconclusive`) | (c) missed primary, significant secondary | Cognitive primary ACE-III not significant (p=0.24); secondary ADCS-ADL (p=0.0067) and QOL-AD (p=0.023) hit. Already proposed for S→I flip on the strict bar. Listed here too so cross-question policy on "primary missed, secondary hit" can be applied uniformly. |
| `26811674` | 2016 | `supports` (proposed → `contradicts`) | Borderline pilot vs null-conclusion | Open-label pilot, n=22, headline conclusion is "Axona did not improve cognitive function." Under strict bar, pilot/feasibility studies are canonically `inconclusive`; but the verbatim conclusion is starkly null. Reviewer's S→C is defensible because the null-conclusion language is direct, but a defensible alternative target is `inconclusive` (pilot, n=22). Flagged as a cross-question policy choice: when a small pilot's verbatim conclusion is null, do we route to `contradicts` (privileging the conclusion) or `inconclusive` (privileging the design tier)? |
| `32290868` | 2020 | `inconclusive` | (b) preclinical/mech-dominated review | KD translational review. Half the included studies are animal (11 preclinical, 11 human). Conclusion is hedged ("might be promising"). Stays `inconclusive` either way; flagged because under strict bar (b), preclinical-dominated reviews labeled `supports` should drop to `inconclusive` — here the label already is `inconclusive` so no flip needed, but useful as an exemplar of the policy. |

## Confirmed (no change)

- `33103819` (BENEFIC kMCT MCI 6 mo, n=83) — **supports ✓** (multiple cognitive measures sig improved)
- `31694759` (MCT crossover in mild-mod AD APOE4-negative, n=53, 30 d) — **supports ✓** (ADAS-Cog-C sig improvement; population is pre-specified APOE4-/-, not a post-hoc subgroup of a null parent)
- `31870908` (2019 MCT meta, 12 records, n=422) — **supports ✓** (ADAS-Cog significant, combined ADAS+MMSE SMD=-0.289 sig)
- `32310169` (AC-1204/NOURISH AD RCT, n=413, 26 wk) — **contradicts ✓** (pivotal negative trial; primary endpoint not met)
- `37980665` (VCO-AD Sri Lanka RCT, n=120, 24 wk) — **contradicts ✓** (no significant difference vs canola oil control; APOE4 carriers showed MMSE benefit)
- `30006299` (caprylidene rCBF pilot, biomarker) — **inconclusive ✓**
- `33354711` (KD-cognition SR, qualitative) — **inconclusive ✓**
- `32757903` (KD CNS broad SR) — **inconclusive ✓**
- `36846143` (ketogenic critical appraisal — Class B for APOE4-negative) — **inconclusive ✓** (defensible; explicitly stratifies by APOE4)
- `33906081` (kMCT cardiometabolic markers, biomarker substudy) — **inconclusive ✓**
- `33621313` (KD-NDD SR, narrative) — **inconclusive ✓**
- `39584279` (lifestyle interventions broad review) — **inconclusive ✓**

## Cross-cutting issues

- **Population drift**: `28552878` and `32652024` are MCT studies in
  frail nursing-home elderly, not AD specifically. Two of the most
  decisively positive RCTs in the corpus are off-target population.
- **Same-cohort substudy**: `33906081` is a secondary analysis of the
  BENEFIC trial (`33103819`), reporting biomarkers rather than cognition.
- **Intervention conflation**: ~half the corpus is "ketogenic diet" rather
  than MCT/coconut oil specifically. The question is about MCT/coconut
  oil; broad KD reviews should arguably be excluded or tagged.
- After flips: 6 supports, 4 contradicts, 12 inconclusive — the
  "mostly negative" expected consensus is partly justified by the two
  pivotal phase 3 / large RCTs (NOURISH AD and VCO-AD) plus the
  network meta `28807434`, but the MCT-focused meta layer
  (`32597927`, `38943982`, `31870908`) does show signal in the
  positive direction. The picture is genuinely contested.

## Cross-question policy questions surfaced here

- **(a) Subgroup-positive in exploratory/null parent.** `15123336` (Reger
  2004) and arguably the Axona pilot `26811674`: APOE4-negative subgroups
  show benefit while whole-sample primary is null or absent. Decision
  needed: do exploratory pilots that report only subgroup-positive results
  get `supports` or `inconclusive`?
- **(b) Preclinical-dominated review.** `32290868` is half-animal,
  half-human studies. Already `inconclusive`, so flagged only as an
  exemplar — no flip required for this question.
- **(c) Missed primary, significant secondary.** `33622392` (modified KD
  AD crossover): cognitive primary ACE-III missed (p=0.24); ADCS-ADL and
  QOL-AD secondaries hit. Already proposed for S→I flip; flagged as
  policy exemplar.
- **Pilot vs null-conclusion (novel-ish).** `26811674` (Axona pilot) is
  n=22 open-label, but its verbatim conclusion is "did not improve
  cognitive function." Does the verbatim null-conclusion language
  override the pilot/feasibility design tier? The reviewer routed S→C;
  defensible alternative is S→I.

## Highest-confidence flips for this question

- `26811674` supports → contradicts (Axona "did not improve cognitive function" — direct mislabel; alternative target `inconclusive` if pilot tier is privileged)
- `33622392` supports → inconclusive (cognitive primary ACE-III not sig; current label overstates)
- `38943982` inconclusive → supports (pooled MMSE and ADAS-Cog both sig)
- `28807434` inconclusive → contradicts (network meta: "no convincing evidence of significant benefit")
- `28552878` and `32652024` supports → inconclusive (frail elderly, not AD population)


## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

### Proposed new tags (Q9)

- `combined_intervention` — active intervention bundles MCT/coconut oil with one or more co-actives (e.g., leucine + vitamin D, Mediterranean diet), confounding the MCT-specific effect
- `biomarker_only` — primary endpoint is a biomarker (rCBF, plasma markers) rather than a clinical cognitive endpoint
- `broad_scope_review` — systematic review covers multiple diseases/interventions where MCT/coconut-oil-in-AD is one slice; pooled estimate not specific to the question
- `subgroup_positive_prespecified` — population restricted by pre-specified stratifier (e.g., APOE4-negative as inclusion criterion, not post-hoc subgroup); weaker than parent-trial-positive but stronger than post-hoc subgroup_positive

### Annotations

- `15123336` — `subgroup_positive`, `pilot_positive` (Reger 2004 acute crossover, n=20, exploratory; ADAS-Cog benefit driven by APOE4-negative subgroup only)
- `33622392` — `missed_primary_sig_secondary`, `pilot_positive` (n=26 crossover; ACE-III primary p=0.24, ADCS-ADL/QOL secondaries hit)
- `33103819` — (none — clean canonical example; BENEFIC kMCT MCI 6mo, n=83, multiple cognitive measures sig)
- `31694759` — `subgroup_positive_prespecified` (population pre-specified APOE4-/-, not post-hoc; primary ADAS-Cog-C significant in the restricted population)
- `30056419` — `pilot_positive`, `combined_intervention` (n=44, 21 days only, qualitative; coconut oil bundled with Mediterranean diet)
- `31870908` — `hedged_meta` (authors: "risk of bias of existing studies necessitates future trials"; SMD significant but trend on ADAS-Cog alone)
- `26811674` — `pilot_positive` (n=22 open-label pilot; verbatim "did not improve cognitive function" — see borderline section for pilot-vs-null-conclusion policy issue)
- `32597927` — (none — clean canonical example; KD-AD SR of 10 RCTs, ADAS-Cog improvement noted)
- `32290868` — `preclinical_dominated`, `narrative_review` (11 animal + 11 human studies; conclusion hedged "might be promising")
- `30006299` — `biomarker_only`, `pilot_positive`, `subgroup_positive` (n=16 caprylidene rCBF pilot; rCBF endpoint only; APOE4-negative subgroup)
- `33354711` — `narrative_review` (63 entries; "no statistical analysis was carried out"; broad neurological scope)
- `32310169` — (none — clean canonical example; NOURISH AD RCT, n=413, primary endpoint not met, p=0.25)
- `32757903` — `broad_scope_review`, `narrative_review` (24 RCTs across CNS diseases; only 2 AD studies; primary topic is epilepsy)
- `38943982` — (none — clean canonical example; KD-AD meta of 10 RCTs, n=691, MMSE p=0.002 and ADAS-Cog p=0.008)
- `28807434` — (none — clean canonical example; network meta concluding "no convincing evidence" for isolated nutrient supplementation)
- `36846143` — `narrative_review` (qualitative AAN-tier critical appraisal; mixed evidence stratified by APOE4 status — Class B for APOE4-, Class U for APOE4+)
- `28552878` — `wrong_population`, `combined_intervention` (n=38 frail nursing-home elderly, mean age 86.6, MMSE ~17 — not AD specifically; MCT bundled with leucine + vitamin D3)
- `32652024` — `wrong_population` (n=64 frail nursing-home elderly, mean age 85.5, BMI 18.6 — not AD specifically; cognition was secondary outcome to muscle function)
- `33906081` — `same_cohort_duplicate`, `biomarker_only` (secondary analysis of BENEFIC `33103819` cohort; cardiometabolic/inflammatory markers, not cognition)
- `33621313` — `narrative_review`, `broad_scope_review` (17 studies across MCI/MS/AD/PD; only 5 AD studies; qualitative recommendations)
- `37980665` — `subgroup_positive` (VCO-AD primary null overall; APOE4+ MMSE benefit p=0.021 reported as subgroup signal — note: stance is `contradicts` per primary, subgroup tag flags the secondary supports signal)
- `39584279` — `narrative_review`, `broad_scope_review` (lifestyle interventions broadly; MCT/KD one of many interventions; "inconsistent effects on cognitive function")
- All other pmids — untagged

---

## Abstracts (n=22)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 15123336 — current stance: `supports`

**Evidence span:** > On cognitive testing, MCT treatment facilitated performance on the Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-cog) for 4- subjects, but not for 4+ subjects (P=0.04).

**Golden note:** Reger β-hydroxybutyrate acute study — cognitive improvement in memory-impaired adults.

**Effects of beta-hydroxybutyrate on cognition in memory-impaired adults.**

*Neurobiology of aging*, 2004. Types: Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't; Research Support, U.S. Gov't, Non-P.H.S.

> Glucose is the brain's principal energy substrate. In Alzheimer's disease (AD), there appears to be a pathological decrease in the brain's ability to use glucose. Neurobiological evidence suggests that ketone bodies are an effective alternative energy substrate for the brain. Elevation of plasma ketone body levels through an oral dose of medium chain triglycerides (MCTs) may improve cognitive functioning in older adults with memory disorders. On separate days, 20 subjects with AD or mild cognitive impairment consumed a drink containing emulsified MCTs or placebo. Significant increases in levels of the ketone body beta-hydroxybutyrate (beta-OHB) were observed 90 min after treatment (P=0.007) when cognitive tests were administered. beta-OHB elevations were moderated by apolipoprotein E (APOE) genotype (P=0.036). For 4+ subjects, beta-OHB levels continued to rise between the 90 and 120 min blood draws in the treatment condition, while the beta-OHB levels of 4- subjects held constant (P<0.009). On cognitive testing, MCT treatment facilitated performance on the Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-cog) for 4- subjects, but not for 4+ subjects (P=0.04). Higher ketone values were associated with greater improvement in paragraph recall with MCT treatment relative to placebo across all subjects (P=0.02). Additional research is warranted to determine the therapeutic benefits of MCTs for patients with AD and how APOE-4 status may mediate beta-OHB efficacy.

---

### PMID 33622392 — current stance: `supports`

**Evidence span:** > Compared with usual diet, patients on the ketogenic diet increased their mean within-individual ADCS-ADL (+ 3.13 ± 5.01 points, P = 0.0067) and QOL-AD (+ 3.37 ± 6.86 points, P = 0.023) scores; the ACE-III also increased, but not significantly (+ 2.12 ± 8.70 points, P = 0.24).

**Golden note:** Modified ketogenic diet RCT in AD — improved daily function/QoL.

**Randomized crossover trial of a modified ketogenic diet in Alzheimer's disease.**

*Alzheimer's research & therapy*, 2021. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Brain energy metabolism is impaired in Alzheimer's disease (AD), which may be mitigated by a ketogenic diet. We conducted a randomized crossover trial to determine whether a 12-week modified ketogenic diet improved cognition, daily function, or quality of life in a hospital clinic of AD patients. METHODS: We randomly assigned patients with clinically confirmed diagnoses of AD to a modified ketogenic diet or usual diet supplemented with low-fat healthy-eating guidelines and enrolled them in a single-phase, assessor-blinded, two-period crossover trial (two 12-week treatment periods, separated by a 10-week washout period). Primary outcomes were mean within-individual changes in the Addenbrookes Cognitive Examination - III (ACE-III) scale, AD Cooperative Study - Activities of Daily Living (ADCS-ADL) inventory, and Quality of Life in AD (QOL-AD) questionnaire over 12 weeks. Secondary outcomes considered changes in cardiovascular risk factors and adverse effects. RESULTS: We randomized 26 patients, of whom 21 (81%) completed the ketogenic diet; only one withdrawal was attributed to the ketogenic diet. While on the ketogenic diet, patients achieved sustained physiological ketosis (12-week mean beta-hydroxybutyrate level: 0.95 ± 0.34 mmol/L). Compared with usual diet, patients on the ketogenic diet increased their mean within-individual ADCS-ADL (+ 3.13 ± 5.01 points, P = 0.0067) and QOL-AD (+ 3.37 ± 6.86 points, P = 0.023) scores; the ACE-III also increased, but not significantly (+ 2.12 ± 8.70 points, P = 0.24). Changes in cardiovascular risk factors were mostly favourable, and adverse effects were mild. CONCLUSIONS: This is the first randomized trial to investigate the impact of a ketogenic diet in patients with uniform diagnoses of AD. High rates of retention, adherence, and safety appear to be achievable in applying a 12-week modified ketogenic diet to AD patients. Compared with a usual diet supplemented with low-fat healthy-eating guidelines, patients on the ketogenic diet improved in daily function and quality of life, two factors of great importance to people living with dementia. TRIAL REGISTRATION: This trial is registered on the Australia New Zealand Clinical Trials Registry, number ACTRN12618001450202 . The trial was registered on August 28, 2018.

---

### PMID 33103819 — current stance: `supports`

**Evidence span:** > Free and cued recall (Trial 1; P = .047), verbal fluency (categories; P = .024), Boston Naming Test (total correct answers; P = .033), and the Trail-Making Test (total errors; P = .017) improved significantly in the kMCT group compared to placebo.

**Golden note:** BENEFIC ketogenic drink in MCI — improved cognition over 6 months.

**A ketogenic drink improves cognition in mild cognitive impairment: Results of a 6-month RCT.**

*Alzheimer's & dementia : the journal of the Alzheimer's Association*, 2020. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> INTRODUCTION: Counteracting impaired brain glucose metabolism with ketones may improve cognition in mild cognitive impairment (MCI). METHODS: Cognition, plasma ketone response, and metabolic profile were assessed before and 6 months after supplementation with a ketogenic drink containing medium chain triglyceride (ketogenic medium chain triglyceride [kMCT]; 15 g twice/day; n = 39) or placebo (n = 44). RESULTS: Free and cued recall (Trial 1; P = .047), verbal fluency (categories; P = .024), Boston Naming Test (total correct answers; P = .033), and the Trail-Making Test (total errors; P = .017) improved significantly in the kMCT group compared to placebo (analysis of covariance; pre-intervention score, sex, age, education, and apolipoprotein E4 as covariates). Some cognitive outcomes also correlated positively with plasma ketones. Plasma metabolic profile and ketone response were unchanged. CONCLUSIONS: This kMCT drink improved cognitive outcomes in MCI, at least in part by increasing blood ketone level. These data support further assessment of MCI progression to Alzheimer's disease.

---

### PMID 31694759 — current stance: `supports`

**Evidence span:** > This study showed a significant (p < 0.01) reduction in ADAS-Cog-C scores between the MCT (2.62 points below baseline) and placebo interventions (2.57 points above baseline).

**Golden note:** MCT RCT in mild-mod AD APOE4-negative — improved cognition (subgroup).

**Medium-chain triglycerides improved cognition and lipid metabolomics in mild to moderate Alzheimer's disease patients with APOE4-/-: A double-blind, randomized, placebo-controlled crossover trial.**

*Clinical nutrition (Edinburgh, Scotland)*, 2019. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Previous clinical and animal studies suggested that medium-chain triglycerides (MCT) might be an alternative energy substrate for the brain and might benefit patients with Alzheimer's disease (AD), but the clinical evidence is not substantial or totally convincing. OBJECTIVE: To investigate the effects of MCT on cognitive ability in patients with mild to moderate AD and explore the changes in peripheral blood metabolomics. METHODS: A double-blind, randomized, placebo-controlled crossover study was undertaken in 53 mild to moderate AD patients. Participants were randomized between two sequences (placebo followed by MCT or MCT followed by placebo) and took MCT jelly or placebo jelly (canola oil) by mouth three times daily (total daily fat dose: 17.3 g MCT, or 19.7 g canola oil) for 30 days per phase. The primary outcome was cognition as measured by the Alzheimer's Disease Assessment Scale-Cognitive Subscale, Chinese version (ADAS-Cog-C). The secondary outcome was self-care as measured by the activities of daily living scale (ADL) and changes in plasma metabolites. RESULTS: This study showed a significant (p < 0.01) reduction in ADAS-Cog-C scores between the MCT (2.62 points below baseline) and placebo interventions (2.57 points above baseline). Data from 46 (86.8%) APOE4-/- subjects who completed the entire study were analyzed. Changes in ADL scores were not significantly different between the MCT and placebo interventions (p > 0.05). The concentrations of TC, HDL-C, β-hydroxybutyrate and acetoacetate were significantly higher in the MCT group than in the placebo group (p < 0.05). Lysophosphatidylcholine 16:0 (LysoPC (16:0)), LysoPC (P-18:0), LysoPC (P-18:1(9Z)), LysoPC (20:2(11Z,14Z)), and LysoPC (22:5(4Z,7Z,10Z,13Z,16Z)) were significantly increased after MCT intervention, and the concentrations of LysoPC (18:0), palmitic acid, linoleic acid, oleic acid, and 7,12-dimethylbenz[a]anthracene were significantly decreased (p < 0.05), whereas no significant changes appeared after the placebo intervention. Androstenedione concentration increased after placebo intervention. Furthermore, a significant negative correlation was observed between changes in LysoPC (P-18:1(9Z)) and ADAS-Cog-C scores after MCT intervention (r = -0.1472, p < 0.05). CONCLUSIONS: MCT had positive effects on cognitive ability in mild to moderate AD patients with APOE4-/-. These effects of MCT might be related to the metabolism of LysoPC, oleic acid, linoleic acid and palmitic acid, in addition to the ketogenic effect. STUDY ID NUMBER: ChiCTR-IOR-16009737. REGISTRY WEBSITE: WHO ICTRP Search Portal - http://apps.who.int/trialsearch/Default.aspx.

---

### PMID 30056419 — current stance: `supports`

**Evidence span:** > After intervention with coconut oil, improvements in episodic, temporal orientation, and semantic memory were observed, and it seems that the positive effect is more evident in women with mild-moderate state, although other improvements in males and severe state were also shown.

**Golden note:** Coconut oil + Mediterranean diet pilot in AD — cognitive improvement.

**Improvement of Main Cognitive Functions in Patients with Alzheimer's Disease after Treatment with Coconut Oil Enriched Mediterranean Diet: A Pilot Study.**

*Journal of Alzheimer's disease : JAD*, 2018. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Alzheimer's disease (AD) is the most prevalent neurodegenerative disorder (mainly in women), and new therapies are needed. In this way, ketone bodies are a direct source of cellular energy and can be obtained from coconut oil, postulating that coconut oil could be a new non-pharmacological alternative in AD patients. OBJECTIVE: The aim of this study is to detect changes in the main cognitive functions of patients with AD after following a coconut oil enriched Mediterranean diet, and to determine whether there are differences in function of stage or sex. METHODS: A prospective, longitudinal, qualitative, analytic, experimental study was carried out in 44 patients with AD, who were randomly divided into two homogenous groups of 22 patients each: an experimental group of patients who followed a coconut oil enriched Mediterranean diet for 21 days and a control group. In order to determine the cognitive changes after the intervention, we carried out the 7 Minute Screen, which analyses temporal orientation, visuospatial and visuoconstructive abilities, and semantic and episodic memory. RESULTS: After intervention with coconut oil, improvements in episodic, temporal orientation, and semantic memory were observed, and it seems that the positive effect is more evident in women with mild-moderate state, although other improvements in males and severe state were also shown. CONCLUSIONS: The isocaloric coconut oil enriched Mediterranean diet seems to improve cognitive functions in patients with AD, with differences according to patient sex and degree of severity of the disease, although more studies in this line are needed.

---

### PMID 31870908 — current stance: `supports`

**Evidence span:** > showed a trend towards cognitive improvement on ADAS-Cog [MD = -0.539; 95% CI (-1.239, -0.161), I2 = 0 %], and significantly improved cognition on a combined measure (ADAS-Cog with MMSE) [SMD = -0.289; 95 % CI (-0.551, -0.027), I2 = 0 %].

**Golden note:** MCT meta in AD — may improve cognition, modest effect.

**Medium Chain Triglycerides induce mild ketosis and may improve cognition in Alzheimer's disease. A systematic review and meta-analysis of human studies.**

*Ageing research reviews*, 2019. Types: Journal Article; Meta-Analysis; Research Support, N.I.H., Intramural; Systematic Review

> INTRODUCTION/AIM: The brain in Alzheimer's disease shows glucose hypometabolism but may utilize ketones for energy production. Ketone levels can potentially be boosted through oral intake of Medium Chain Triglycerides (MCTs). The aim of this meta-analysis is to investigate the effect of MCTs on peripheral ketone levels and cognitive performance in patients with mild cognitive impairment and Alzheimer's disease. METHODS: Medline, Scopus and Web of Science were searched for literature up to March 1, 2019. Meta-analyses were performed by implementing continuous random-effects models and outcomes were reported as weighted Mean Differences (MDs) or Standardized Mean Differences (SMDs). RESULTS: Twelve records (422 participants) were included. Meta-analysis of RCTs showed that, compared with placebo, MCTs elevated beta-hydroxybutyrate [MD = 0.355; 95 % CI (0.286, 0.424), I2 = 0 %], showed a trend towards cognitive improvement on ADAS-Cog [MD = -0.539; 95% CI (-1.239, -0.161), I2 = 0 %], and significantly improved cognition on a combined measure (ADAS-Cog with MMSE) [SMD = -0.289; 95 % CI (-0.551, -0.027), I2 = 0 %]. CONCLUSIONS: In this meta-analysis, we demonstrated that MCTs can induce mild ketosis and may improve cognition in patients with mild cognitive impairment and Alzheimer's disease. However, risk of bias of existing studies necessitates future trials.

---

### PMID 26811674 — current stance: `supports`

**Evidence span:** > Axona did not improve cognitive function in our sample of AD patients, even in those patients without the ApoE4 allele.

**Golden note:** MCT (Axona) Japanese AD pilot — benefits, tolerable.

**Benefits of use, and tolerance of, medium-chain triglyceride medical food in the management of Japanese patients with Alzheimer's disease: a prospective, open-label pilot study.**

*Clinical interventions in aging*, 2016. Types: Journal Article; Observational Study; Research Support, Non-U.S. Gov't

> OBJECTIVES: This is the first clinical trial of this type in Japan, designed to analyze two important aspects of Alzheimer's disease (AD) management using medium-chain triglycerides. Axona was administered for 3 months (40 g of powder containing 20 g of caprylic triglycerides). We used an indurating, four-step dose-titration method (from 10 to 40 g per day) for 7 days before the trial, and examined the tolerance and adverse effects of this intervention. We also investigated its effect on cognitive function in mild-to-moderate AD patients. PATIENTS AND METHODS: This was a clinical intervention in 22 Japanese patients with sporadic AD at a mild-to-moderate stage (ten females, 12 males), mean age (± standard deviation) 63.9 (±8.5) years, Mini-Mental State Examination (MMSE) score, 10-25, seven patients were ApoE4-positive. During Axona administration, we examined changes in cognitive function by obtaining MMSE and AD assessment-scale scores. Intolerance and serum ketone concentrations were also examined. RESULTS: The tolerance of Axona was good, without severe gastrointestinal adverse effects. Axona did not improve cognitive function in our sample of AD patients, even in those patients without the ApoE4 allele. However, some ApoE4-negative patients with baseline MMSE score ≥14 showed improvement in their cognitive functions. CONCLUSION: The modified dose-titration method, starting with a low dose of Axona, decreased gastrointestinal adverse effects in Japanese patients. Axona might be effective for some relatively mildly affected patients with AD (with cognitive function MMSE score of ≥14 and lacking the ApoE4 allele).

---

### PMID 32597927 — current stance: `inconclusive`

**Evidence span:** > The use of ketoneurotherapeutics proved effective in improving general cognition using the Alzheimer's Disease Assessment Scale-Cognitive, in interventions of either duration. In addition, long-term ketogenic therapy improved episodic and secondary memory.

**Golden note:** Ketogenic RCT systematic review — modest, inconsistent.

**To Keto or Not to Keto? A Systematic Review of Randomized Controlled Trials Assessing the Effects of Ketogenic Therapy on Alzheimer Disease.**

*Advances in nutrition (Bethesda, Md.)*, 2020. Types: Journal Article; Systematic Review

> Alzheimer disease (AD) is a global health concern with the majority of pharmacotherapy choices consisting of symptomatic treatment. Recently, ketogenic therapies have been tested in randomized controlled trials (RCTs), focusing on delaying disease progression and ameliorating cognitive function. The present systematic review aimed to aggregate the results of trials examining the effects of ketogenic therapy on patients with AD/mild cognitive impairment (MCI). A systematic search was conducted on PubMed, CENTRAL, clinicaltrials.gov, and gray literature for RCTs performed on adults, published in English until 1 April, 2019, assessing the effects of ketogenic therapy on MCI and/or AD compared against placebo, usual diet, or meals lacking ketogenic agents. Two researchers independently extracted data and assessed risk of bias with the Cochrane tool. A total of 10 RCTs were identified, fulfilling the inclusion criteria. Interventions were heterogeneous, acute or long term (45-180 d), including adherence to a ketogenic diet, intake of ready-to-consume drinks, medium-chain triglyceride (MCT) powder for drinks preparation, yoghurt enriched with MCTs, MCT capsules, and ketogenic formulas/meals. The use of ketoneurotherapeutics proved effective in improving general cognition using the Alzheimer's Disease Assessment Scale-Cognitive, in interventions of either duration. In addition, long-term ketogenic therapy improved episodic and secondary memory. Psychological health, executive ability, and attention were not improved. Increases in blood ketone concentrations were unanimous and correlated to the neurocognitive battery based on various tests. Cerebral ketone uptake and utilization were improved, as indicated by the global brain cerebral metabolic rate for ketones and [11C] acetoacetate. Ketone concentrations and cognitive performance differed between APOE ε4(+) and APOE ε4(-) participants, indicating a delayed response among the former and an improved response among the latter. Although research on the subject is still in the early stages and highly heterogeneous in terms of study design, interventions, and outcome measures, ketogenic therapy appears promising in improving both acute and long-term cognition among patients with AD/MCI. This systematic review was registered at www.crd.york.ac.uk/prospero as CRD42019128311.

---

### PMID 32290868 — current stance: `inconclusive`

**Evidence span:** > The KD or MCT intake might be promising ways to alter cognitive symptoms in AD, especially at the prodromal stage of the disease.

**Golden note:** Ketogenic-AD translational review — promising but unproven.

**Are ketogenic diets promising for Alzheimer's disease? A translational review.**

*Alzheimer's research & therapy*, 2020. Types: Journal Article; Systematic Review

> BACKGROUND: Brain amyloid deposition and neurofibrillary tangles in Alzheimer's disease (AD) are associated with complex neuroinflammatory reactions such as microglial activation and cytokine production. Glucose metabolism is closely related to neuroinflammation. Ketogenic diets (KDs) include a high amount of fat, low carbohydrate and medium-chain triglyceride (MCT) intake. KDs lead to the production of ketone bodies to fuel the brain, in the absence of glucose. These nutritional interventions are validated treatments of pharmacoresistant epilepsy, consequently leading to a better intellectual development in epileptic children. In neurodegenerative diseases and cognitive decline, potential benefits of KD were previously pointed out, but the published evidence remains scarce. The main objective of this review was to critically examine the evidence regarding KD or MCT intake effects both in AD and ageing animal models and in humans. MAIN BODY: We conducted a review based on a systematic search of interventional trials published from January 2000 to March 2019 found on MEDLINE and Cochrane databases. Overall, 11 animal and 11 human studies were included in the present review. In preclinical studies, this review revealed an improvement of cognition and motor function in AD mouse model and ageing animals. However, the KD and ketone supplementation were also associated with significant weight loss. In human studies, most of the published articles showed a significant improvement of cognitive outcomes (global cognition, memory and executive functions) with ketone supplementation or KD, regardless of the severity of cognitive impairments previously detected. Both interventions seemed acceptable and efficient to achieve ketosis. CONCLUSION: The KD or MCT intake might be promising ways to alter cognitive symptoms in AD, especially at the prodromal stage of the disease. The need for efficient disease-modifying strategies suggests to pursue further KD interventional studies to assess the efficacy, the adherence to this diet and the potential adverse effects of these nutritional approaches.

---

### PMID 30006299 — current stance: `inconclusive`

**Evidence span:** > Daily ingestion of caprylidene over 45 days was associated with increased blood flow in specific brain regions in patients lacking an apolipoprotein ɛ4 allele.

**Golden note:** Caprylidene + cerebral blood flow pilot — biomarker secondary.

**Changes in regional cerebral blood flow associated with a 45 day course of the ketogenic agent, caprylidene, in patients with mild to moderate Alzheimer's disease: Results of a randomized, double-blinded, pilot study.**

*Experimental gerontology*, 2018. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Caprylidene is a ketogen that, when metabolized, produces the ketones beta-hydroxybutyrate and acetoacetate, which can cross the blood brain barrier. It has been hypothesized that ketone bodies can be used as an alternate energy source by neurons with impaired glucose utilization. Caprylidene has been shown to improve cognition in patients with mild-to-moderate Alzheimer's disease (AD) who lacked an AD-predisposing allele (ɛ4) of the gene for apolipoprotein E. In this pilot study, we examined the effects of caprylidene on regional cerebral blood flow (rCBF) in patients with mild to moderate AD. METHODS: Sixteen subjects with mild-to-moderate AD, based on NINCDS-ADRDA criteria, were enrolled in a double-blinded, placebo-controlled, randomized clinical trial. Fourteen subjects received treatment with caprylidene, and 2 subjects were given placebo. Subjects received 4 15O-water PET scans over the course of the study to assess rCBF: once before receiving a standard caprylidene or placebo dose and 90 min after the dose, on the first day and after 45 days of daily caprylidene or placebo consumption. The scans were examined by standardized volumes of interest (sVOI) and voxel-based statistical parametric mapping (spm) methods of analysis. RESULTS: Subjects lacking an ɛ4 allele had significantly elevated rCBF in the left superior lateral temporal cortex by sVOI analysis after adopting a caprylidene diet for 45 days (p = 0.04), which was further corroborated by spm. The anterior cerebellum, left inferior temporal cortex, and hypothalamus were also found by spm to be regions of long-term increase in rCBF in these subjects. In contrast, patients who possessed the ɛ4 allele did not display these changes in rCBF. CONCLUSION: Daily ingestion of caprylidene over 45 days was associated with increased blood flow in specific brain regions in patients lacking an apolipoprotein ɛ4 allele.

---

### PMID 33354711 — current stance: `inconclusive`

**Evidence span:** > Although scientific literature on the subject is scarce and there has tended to be a lack of scientific rigor, the studies reviewed confirmed the effectiveness of this diet in improving the cognitive symptomatology of the aforementioned diseases.

**Golden note:** KD-cognition systematic review — mixed for AD.

**Ketogenic diet and cognition in neurological diseases: a systematic review.**

*Nutrition reviews*, 2021. Types: Journal Article; Systematic Review

> CONTEXT: In recent years, the ketogenic diet has gained special relevance as a possible therapeutic alternative to some neurological and chronic diseases. OBJECTIVE: The aim of this systematic review was to answer the following question: Does a ketogenic diet improve cognitive skills in patients with Alzheimer's disease, Parkinson's disease, refractory epilepsy, and type 1 glucose deficiency syndrome? To define the research question, the PICOS criteria were used, following the guidelines of the PRISMA method. DATA SOURCES: Medline/PubMed, Elsevier Science Direct, Dialnet, EBSCOhost, Mediagraphic, Sage Journals, ProQuest, and Wiley Online Library databases were used. DATA EXTRACTION: After applying inclusion and exclusion criteria in accordance with the PRISMA method, a total of 63 entries published between 2004 and 2019 were used. DATA ANALYSIS: The records extracted were analyzed from a qualitative approach, so no statistical analysis was carried out. CONCLUSION: Although scientific literature on the subject is scarce and there has tended to be a lack of scientific rigor, the studies reviewed confirmed the effectiveness of this diet in improving the cognitive symptomatology of the aforementioned diseases.

---

### PMID 32310169 — current stance: `contradicts`

**Evidence span:** > The AC-1204 formulation of caprylic triglyceride failed to improve cognition or functional ability in subjects with mild-to-moderate AD.

**Golden note:** AC-1204 (Axona reformulation) RCT in mild-mod AD — primary endpoint NOT met.

**A Placebo-Controlled, Parallel-Group, Randomized Clinical Trial of AC-1204 in Mild-to-Moderate Alzheimer's Disease.**

*Journal of Alzheimer's disease : JAD*, 2020. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Alzheimer's disease (AD) is characterized by amyloid-β plaques, neurofibrillary tangles, and regional cerebral glucose hypometabolism. Providing an alternative metabolic substrate, such as ketone bodies, may be a viable therapeutic option. OBJECTIVE: The objective was to determine the efficacy and safety of the AC-1204 formulation of caprylic triglyceride administered daily for 26 weeks in APOE4 non-carrier participants with mild-to-moderate AD. METHODS: In a double-blind, placebo-controlled, randomized study (AC-12-010, NOURISH AD, NCT01741194), 413 patients with mild-to-moderate probable AD were stratified by APOE genotype and randomized (1 : 1) to receive either placebo or AC-1204 for 26 weeks. The primary outcome was the change from baseline to week 26 on the 11-item Alzheimer's Disease Assessment Scale - Cognitive subscale (ADAS-Cog11) among APOE4 non-carriers. The key secondary outcome was the change from baseline to week 26 in the Alzheimer's Disease Cooperative Study - Clinician's Global Impression of Change scale. RESULTS: Administration of AC-1204 was safe and well-tolerated. Mean changes from baseline in the primary outcome at 26 weeks in ADAS-Cog11 for placebo (n = 138) was 0.0 and for AC-1204 (n = 137) was 0.6 (LS differences of mean - 0.761, p = 0.2458) and secondary outcome measures failed to detect any drug effects. CONCLUSION: The AC-1204 formulation of caprylic triglyceride failed to improve cognition or functional ability in subjects with mild-to-moderate AD. The lack of efficacy observed in this study may have several contributing factors including a lower ketone body formation from AC-1204 than expected and a lack of decline in the patients receiving placebo.

---

### PMID 32757903 — current stance: `inconclusive`

**Evidence span:** > MCT did not significantly change regional cerebral blood flow (rCBF) in patients with AD, but MAD significantly improved memory at 6 weeks (p = .03).

**Golden note:** KD in CNS diseases systematic review — broad, mixed.

**Use of ketogenic diets in the treatment of central nervous system diseases: a systematic review.**

*Nordic journal of psychiatry*, 2020. Types: Journal Article; Systematic Review

> BACKGROUND: Studies have consistently shown that patients with epilepsy could benefit from ketogenic diets (KDs). Recent evidence suggests that KD could be used in the treatment of central nervous system (CNS) diseases. The aim of this systematic review was to investigate the use and efficacy of KD, modified Atkins diet (MAD) and medium-chain triglyceride (MCT) diet in infants, children, adolescents, and adults with CNS diseases. METHODS: This systematic review was performed according to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines. Main databases, i.e. EMBASE, PubMed and PsycINFO, were searched on 4 December 2019. Only randomized clinical trials (RCTs) were included and only if they reported KD, MCT or MAD interventions on patients with CNS diseases. RESULTS: Twenty-four publications were eligible for inclusion (n = 1221). Twenty-one publications concerned epilepsy, two concerned Alzheimer's disease (AD), and one concerned Parkinson's disease (PD). All studies regarding epilepsy reported of seizure reduction compared to baseline. MCT did not significantly change regional cerebral blood flow (rCBF) in patients with AD, but MAD significantly improved memory at 6 weeks (p = .03). KD significantly improved motor and nonmotor functions in patients with PD at 8 weeks (p < .001). There was a trend towards fewer adverse effects in MAD compared to KD. CONCLUSION: In conclusion, various forms of KDs seem tolerable and effective as part of the treatment for epilepsy, AD and PD, although more investigation concerning the mechanism, efficacy and adverse events is necessary.

---

### PMID 38943982 — current stance: `inconclusive`

**Evidence span:** > Meta-analysis results showed that KD could effectively improve the mental state of the elderly (NM scale) [MD = 7.56, 95%CI (3.02, 12.10), P = 0.001], MMSE [MD = 1.25, 95%CI (0.46, 2.04), P = 0.002], and ADAS-Cog [MD = -3.43, 95%CI (-5.98, -0.88), P = 0.008].

**Golden note:** KD-AD cognition meta — clinical effect 'uncertain'.

**Effects of ketogenic diet on cognitive function of patients with Alzheimer's disease: a systematic review and meta-analysis.**

*The journal of nutrition, health & aging*, 2024. Types: Journal Article; Systematic Review; Meta-Analysis

> BACKGROUND: Ketogenic diets (KD) have shown remarkable effects in many disease areas. It has been demonstrated in numerous animal experiments that KD is effective in the treatment of Alzheimer's disease (AD). But the clinical effect of treating AD is uncertain. OBJECTIVE: To systematically review the impact of KD on cognitive function in AD. METHODS: We conducted a search of three international databases-PubMed, Cochrane Library, and Embase-to retrieve RCTs on the KD intervention for AD from the inception of the databases through October 2023. Two reviewers searched and screened the literature, extracted and checked relevant data independently, and assessed the risk of bias of the included studies. The meta-analysis was carried out utilizing RevMan 5.3 software. RESULTS: A total of 10 RCTS involving 691 patients with AD were included. There were 357 participants in the intervention group and 334 participants in the control group. The duration of the KD intervention ranged from a minimum of 3 months to a maximum of 15 months. Meta-analysis results showed that KD could effectively improve the mental state of the elderly (NM scale) [MD = 7.56, 95%CI (3.02, 12.10), P = 0.001], MMSE [MD = 1.25, 95%CI (0.46, 2.04), P = 0.002], and ADAS-Cog [MD = -3.43, 95%CI (-5.98, -0.88), P = 0.008]. The elevation of ketone body (β-hydroxybutyric) [MD = 118.84, 95%CI (15.20, 222.48), P = 0.02] may also lead to the elevation of triglyceride [MD = 0.19, 95%CI (0.03, 0.35), P = 0.02] and low density lipoprotein [MD = 0.31, 95%CI (0.04, 0.58), P = 0.02]. CONCLUSION: Research conducted has indicated that the KD can enhance the mental state and cognitive function of those with AD, albeit potentially leading to an elevation in blood lipid levels. In summary, the good intervention effect and safety of KD are worthy of promotion and application in clinical treatment of AD.

---

### PMID 28807434 — current stance: `inconclusive`

**Evidence span:** > Isolated nutrient supplementations show no convincing evidence of providing a significant benefit on clinical manifestations or neuropathology of AD.

**Golden note:** Network meta nutrition AD — MCT/ketogenic among many interventions.

**Nutritional Strategies in the Management of Alzheimer Disease: Systematic Review With Network Meta-Analysis.**

*Journal of the American Medical Directors Association*, 2017. Types: Journal Article; Systematic Review; Network Meta-Analysis

> BACKGROUND: Alzheimer disease (AD) is the major cause of dependency and disability in the elderly. Numerous studies have sought to achieve its prevention and/or management examining a role for modifiable risk factors, such as nutrition. This work aims to investigate the effects of food and/or nutrients in the management of AD at different stages. METHODS: Electronic databases were searched for clinical trials examining the effect of nutrient intervention in individuals with AD, compared with placebo, published up to 2014. The outcomes investigated were neuropsychological assessment scales, neuroimaging, and biomarkers. The Cochrane tool was employed to assess risk of bias. Pairwise meta-analyses were performed in a random-effect model by estimating the weighted mean differences with 95% confidence interval (CI) for each outcome measure. The Network meta-analysis was undertaken on cognitive outcome. RESULTS: Selected studies used antioxidants, B-vitamins, inositol, medium-chain triglyceride, omega-3, polymeric formulas, polypeptide, and vitamin D. AD outcome measurements were mainly restricted to cognitive state and functional abilities. Estimate treatment effects from pairwise meta-analyses showed large but nonsignificant effect in the supplementation with proline-rich polypeptide [weighted mean difference 6.93 (95% CI -3.04, 16.89); P = .17] and B-vitamins [weighted mean difference 0.52 (95% CI -0.05, 1.09); P = .07) on cognitive function measured by the Mini-Mental State Examination. The other nutrients supplementation did not show any significant effect on any outcome measures. CONCLUSIONS: Isolated nutrient supplementations show no convincing evidence of providing a significant benefit on clinical manifestations or neuropathology of AD. During the initial stages of AD, nutrient supplementation did not show any effect when delivered individually, probably because of their synergistic function on brain, at different domains.

---

### PMID 36846143 — current stance: `inconclusive`

**Evidence span:** > We found class "B" evidence (probably effective) for cognitive improvement in subjects with mild cognitive impairment and subjects with mild-to-moderate Alzheimer's disease negative for the apolipoprotein ε4 allele (APOε4-). We found class "U" evidence (unproven) for cognitive stabilization in individuals with mild-to-moderate Alzheimer's disease positive for the apolipoprotein ε4 allele (APOε4+).

**Golden note:** Ketogenic interventions critical appraisal in MCI/AD/PD — mostly small studies.

**Ketogenic interventions in mild cognitive impairment, Alzheimer's disease, and Parkinson's disease: A systematic review and critical appraisal.**

*Frontiers in neurology*, 2023. Types: Systematic Review; Journal Article

> BACKGROUND: There is increasing interest in therapeutic ketosis as a potential therapy for neurodegenerative disorders-in particular, mild cognitive impairment (MCI), Alzheimer's disease (AD), and Parkinson's disease (PD)-following a proof-of-concept study in Parkinson's disease published in 2005. METHODS: To provide an objective assessment of emerging clinical evidence and targeted recommendations for future research, we reviewed clinical trials involving ketogenic interventions in mild cognitive impairment, Alzheimer's disease, and Parkinson's disease reported since 2005. Levels of clinical evidence were systematically reviewed using the American Academy of Neurology criteria for rating therapeutic trials. RESULTS: 10 AD, 3 MCI, and 5 PD therapeutic ketogenic trials were identified. Respective grades of clinical evidence were objectively assessed using the American Academy of Neurology criteria for rating therapeutic trials. We found class "B" evidence (probably effective) for cognitive improvement in subjects with mild cognitive impairment and subjects with mild-to-moderate Alzheimer's disease negative for the apolipoprotein ε4 allele (APOε4-). We found class "U" evidence (unproven) for cognitive stabilization in individuals with mild-to-moderate Alzheimer's disease positive for the apolipoprotein ε4 allele (APOε4+). We found class "C" evidence (possibly effective) for improvement of non-motor features and class "U" evidence (unproven) for motor features in individuals with Parkinson's disease. The number of trials in Parkinson's disease is very small with best evidence that acute supplementation holds promise for improving exercise endurance. CONCLUSIONS: Limitations of the literature to date include the range of ketogenic interventions currently assessed in the literature (i.e., primarily diet or medium-chain triglyceride interventions), with fewer studies using more potent formulations (e.g., exogenous ketone esters). Collectively, the strongest evidence to date exists for cognitive improvement in individuals with mild cognitive impairment and in individuals with mild-to-moderate Alzheimer's disease negative for the apolipoprotein ε4 allele. Larger-scale, pivotal trials are justified in these populations. Further research is required to optimize the utilization of ketogenic interventions in differing clinical contexts and to better characterize the response to therapeutic ketosis in patients who are positive for the apolipoprotein ε4 allele, as modified interventions may be necessary.

---

### PMID 28552878 — current stance: `supports`

**Evidence span:** > The combined supplementation of MCTs (6 g), L-leucine-rich amino acids, and cholecalciferol may improve cognitive function in frail elderly individuals.

**Golden note:** MCT + leucine + vit D3 RCT in frail elderly — cognitive benefit.

**Medium-Chain Triglycerides in Combination with Leucine and Vitamin D Benefit Cognition in Frail Elderly Adults: A Randomized Controlled Trial.**

*Journal of nutritional science and vitaminology*, 2017. Types: Journal Article; Randomized Controlled Trial

> The combined supplementation of medium-chain triglycerides (MCTs), L-leucine-rich amino acids, and cholecalciferol (vitamin D3) increase muscle strength and function in frail elderly individuals. However, their effects on cognition are unknown. We enrolled 38 elderly nursing home residents (mean age±SD, 86.6±4.8 y) in a 3-mo randomized, controlled, parallel group trial. The participants were randomly allocated to 3 groups: the first group received a L-leucine (1.2 g)- and cholecalciferol (20 μg)-enriched supplement with 6 g of MCT (LD+MCT); the second group received the same supplement with 6 g of long-chain triglycerides (LD+LCT); and the third group did not receive any supplements (control). Cognition was assessed at baseline and after the 3-mo intervention. The difference in changes among the groups was assessed with ANCOVA, adjusting for age and the baseline value as covariates. After 3 mo, the Mini-Mental State Examination (MMSE) score in the LD+MCT group increased by 10.6% (from 16.6 to 18.4 points, p<0.05). After 3 mo, the Nishimura geriatric rating scale for mental status (NM scale) score in the LD+MCT group increased by 30.6% (from 24.6 to 32.2 points, p<0.001), whereas that in the LD+LCT and control groups decreased by 11.2% (from 31.2 to 27.7 points, p<0.05) and 26.1% (from 27.2 to 20.1 points, p<0.001), respectively. The combined supplementation of MCTs (6 g), L-leucine-rich amino acids, and cholecalciferol may improve cognitive function in frail elderly individuals.

---

### PMID 32652024 — current stance: `supports`

**Evidence span:** > Supplementation with 6 g MCTs/d may improve the cognition of frail elderly individuals.

**Golden note:** MCT (C8/C10) RCT in frail elderly — improved MMSE.

**Medium-Chain Triglycerides (8:0 and 10:0) Increase Mini-Mental State Examination (MMSE) Score in Frail Elderly Adults in a Randomized Controlled Trial.**

*The Journal of nutrition*, 2020. Types: Journal Article; Randomized Controlled Trial

> BACKGROUND: Supplementation with medium-chain triglycerides (MCTs) was previously shown to increase muscle function in frail elderly individuals. OBJECTIVE: We aimed to assess effects of MCTs on cognition in such individuals. METHODS: We enrolled 64 elderly nursing home residents (85.5 ± 6.8 y; 13 men, 51 women; BMI 18.6 ± 2.5 kg/m2) in a 3-mo randomized, controlled, single-blinded, intervention trial. Participants were randomly allocated to 3 groups: the first group received supplemental L-leucine (1.2 g) and cholecalciferol (20 μg) enriched with 6 g/d of MCTs (LD + MCT group) as a positive control, the second group received 6 g/d of MCTs (MCT group) as the test nutrient, and the third group received 6 g/d of long-chain triglycerides (LCT group) as a negative control. Cognition (secondary outcome) was monitored 4 times: baseline, 1.5 and 3 mo after initiation of the intervention (intervention), and 1.5 mo after termination of the intervention (postintervention follow-up). Cognition scores were assessed by a linear mixed model (intention-to-treat analysis). RESULTS: MCT supplementation increased the Mini-Mental State Examination (MMSE) score by 3.5 points at the 3-mo intervention from baseline (P < 0.001) [intention-to-treat adjusted means: baseline 17.5 points (95% CI: 14.9, 20.2), 3-mo intervention 21.0 points (18.3, 23.7)], whereas LCT supplementation decreased the MMSE score by -0.7 points [baseline 17.0 points (95% CI: 14.4, 19.6), 3-mo intervention 16.3 points (13.6, 18.9)]. At the 3-mo intervention, the difference in MMSE score between the MCT (21.0 points) and LCT (16.3 points) groups became significant (P < 0.05). The increase in MMSE score in response to MCTs was 2.1-fold greater at 3 mo than at 1.5 mo and had returned to baseline value at the 4.5-mo postintervention follow-up visit. CONCLUSION: Supplementation with 6 g MCTs/d may improve the cognition of frail elderly individuals. This trial was registered at umin.ac.jp as UMIN000023302.

---

### PMID 33906081 — current stance: `inconclusive`

**Evidence span:** > Under these study conditions, 30 g/d of kMCT taken for six months and up to 2-hour before post-intervention testing had minimal effect on an extensive profile of circulating cardiometabolic and inflammatory markers as compared to a placebo calorie-matched drink.

**Golden note:** kMCT 6-month MCI — cardiometabolic/inflammatory markers, not cognitive primary.

**The effect of a 6-month ketogenic medium-chain triglyceride supplement on plasma cardiometabolic and inflammatory markers in mild cognitive impairment.**

*Prostaglandins, leukotrienes, and essential fatty acids*, 2020. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> INTRODUCTION: Mild cognitive impairment (MCI) is often accompanied by metabolic abnormalities and inflammation that might play a role in the development of cognitive impairment. The use of ketogenic medium-chain triglycerides (kMCT) to improve cognition in this population has shown promising results but remains controversial because of the potentially detrimental effect of elevated intake of saturated fatty acids on cardiovascular (CV) health and perhaps inflammatory processes. The primary aim of this secondary data analysis report is to describe changes in cardiometabolic markers and peripheral inflammation during a 6-month kMCT intervention in MCI. METHODS: Thirty-nine participants with MCI completed the intervention of 30 g/day of either a kMCT drink or calorie-matched placebo (high-oleic acid) for 6 months. Plasma concentrations of cardiometabolic and inflammatory markers were collected before (fasting state) and after the intervention (2 h following the last drink). RESULTS: A mixed model ANOVA analysis revealed a time by group interaction for ketones (P < 0.001), plasma 8:0 and 10:0 acids (both P < 0.001) and IL-8 (P = 0.002) with follow up comparison revealing a significant increase in the kMCT group (+48%, P = 0.005), (+3,800 and +4,900%, both P < 0.001) and (+147%, P < 0.001) respectively. A main effect of time was observed for insulin (P = 0.004), triglycerides (P = 0.011) and non-esterified fatty acids (P = 0.036). CONCLUSION: Under these study conditions, 30 g/d of kMCT taken for six months and up to 2-hour before post-intervention testing had minimal effect on an extensive profile of circulating cardiometabolic and inflammatory markers as compared to a placebo calorie-matched drink. Our results support the safety kMCT supplementation in individuals with MCI. The clinical significance of the observed increase in circulating IL-8 levels is presently unknown and awaits future studies.

---

### PMID 33621313 — current stance: `inconclusive`

**Evidence span:** > Based on available evidence, exogenous ketogenic agents may be more feasible than dietary interventions in NDD from a compliance and adherence perspective; more research is required to confirm this.

**Golden note:** Ketogenic neurodegen review — limited evidence quality.

**The Efficacy of Ketogenic Therapies in the Clinical Management of People with Neurodegenerative Disease: A Systematic Review.**

*Advances in nutrition (Bethesda, Md.)*, 2021. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> Ketone bodies have potential disease-modifying activity that represent a novel therapeutic approach for neurodegenerative diseases (NDD). The aim of this systematic review was to summarize and evaluate the evidence for the application of ketogenic therapies (dietary or exogenous ketogenic agents) for NDD and provide recommendations for future research. Eight databases were electronically searched for articles reporting on controlled trials (≥4 wk duration) that induced ketosis or elevated serum ketone concentrations in people with NDD. Of 4498 records identified, 17 articles met the inclusion criteria with a total of 979 participants including studies on mild cognitive impairment (MCI; n = 6), multiple sclerosis (n = 4), Alzheimer's disease (n = 5), Parkinson's disease (n = 1), and MCI secondary to Parkinson's disease (n = 1). Of 17 studies, 7 were randomized double-blind placebo-controlled trials. Most studies used dietary interventions (n = 9), followed by medium-chain triglycerides (n = 7) and a fasting protocol (n = 1). Generally, trials were 6 wk in duration and assessed cognition as the primary outcome. Studies were heterogeneous in type and severity of NDD, interventions used, and outcomes assessed. Overall, 3/17 studies carried a low risk of bias. Based on available evidence, exogenous ketogenic agents may be more feasible than dietary interventions in NDD from a compliance and adherence perspective; more research is required to confirm this. Recommendations for future research include improving exogenous formulations to reduce adverse effects, exploring interindividual factors affecting response-to-treatment, and establishing a "minimum required dose" for clinically meaningful improvements in disease-specific symptoms, such as cognition or motor function.

---

### PMID 37980665 — current stance: `contradicts`

**Evidence span:** > Overall, VCO did not improve cognition in individuals with mild-to-moderate AD following a 24-week intervention, compared to canola oil.

**Golden note:** VCO-AD Sri Lanka RCT — virgin coconut oil did NOT improve cognition vs placebo.

**Effect of Virgin Coconut Oil Supplementation on Cognition of Individuals with Mild-to-Moderate Alzheimer's Disease in Sri Lanka (VCO-AD Study): A Randomized Placebo-Controlled Trial.**

*Journal of Alzheimer's disease : JAD*, 2023. Types: Randomized Controlled Trial; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: Virgin coconut oil (VCO) is a potential therapeutic approach to improve cognition in Alzheimer's disease (AD) due to its properties as a ketogenic agent and antioxidative characteristics. OBJECTIVE: This study aimed to investigate the effect of VCO on cognition in people with AD and to determine the impact of apolipoprotein E (APOE) ɛ4 genotype on cognitive outcomes. METHODS: Participants of this double-blind placebo-controlled trial (SLCTR/2015/018, 15.09.2015) were 120 Sri Lankan individuals with mild-to-moderate AD (MMSE = 15-25), aged > 65 years, and they were randomly allocated to treatment or control groups. The treatment group was given 30 mL/day of VCO orally and the control group, received similar amount of canola oil, for 24 weeks. The Mini-Mental Sate Examination (MMSE) and Clock drawing test were performed to assess cognition at baseline and at the end of the intervention. Blood samples were collected and analyzed for lipid profile and glycated hemoglobin (HbA1 C) levels.∥Results:There were no significant difference in cognitive scores, lipid profile, and HbA1 C levels between VCO and control groups post-intervention. The MMSE scores, however, improved among APOE ɛ4 carriers who had VCO, compared to non-carriers (2.37, p = 0.021). APOE ɛ4 status did not influence the cognitive scores in the control group. The attrition rate was 30%.∥Conclusion:Overall, VCO did not improve cognition in individuals with mild-to-moderate AD following a 24-week intervention, compared to canola oil. However, it improved the MMSE scores in APOE ɛ4 carriers. Besides, VCO did not compromise lipid profile and HbA1 C levels and is thus safe to consume.

---

### PMID 39584279 — current stance: `inconclusive`

**Evidence span:** > Modified diets, such as Atkins and ketogenic, displayed inconsistent effects on cognitive function but influenced other health-related parameters.

**Golden note:** Lifestyle interventions AD systematic review — broad, MCT one of many.

**A systematic review of lifestyle-based interventions for managing Alzheimer's disease: Insights from randomized controlled trials.**

*Journal of Alzheimer's disease : JAD*, 2024. Types: Systematic Review; Journal Article

> BACKGROUND: Alzheimer's disease (AD) presents a significant challenge in healthcare, prompting exploration into non-pharmacological interventions to complement traditional treatments. OBJECTIVE: This systematic review explores the efficacy of lifestyle-based interventions in managing AD. METHODS: A comprehensive literature search was conducted in PubMed, Web of Science, and Scopus between 2018 and 2023, selecting randomized controlled trials examining factors such as exercise, diet, stress, and cognitive training in AD patients. RESULTS: The review revealed physical exercise as the predominant non-pharmacological intervention, accompanied by dietary modifications, cognitive training, and therapies such as mindfulness and music. While exercise demonstrated improvements in quality of life, its cognitive benefits were limited. Modified diets, such as Atkins and ketogenic, displayed inconsistent effects on cognitive function but influenced other health-related parameters. Additionally, probiotic therapy and novel cognitive training technologies were explored. CONCLUSIONS: Despite some interventions showing promise in enhancing cognitive function and slowing disease progression, uncertainties remain regarding the dose-response relationship, underlying mechanisms, and potential synergistic effects. Moreover, consideration of genetic and sex-based disparities is warranted. This synthesis underscores the need for further research to elucidate the nuances of non-pharmacological interventions in managing AD effectively. PROSPERO REGISTRATION NUMBER: CRD42023432823.

---

