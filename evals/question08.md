# Q8: Does deep brain stimulation of the fornix improve cognition in Alzheimer's?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=12 PMIDs.

**Current S/C/I**: 4 / 0 / 8
**Proposed S/C/I**: 0 / 3 / 9
**Net flips**: 6 (3 S→I, 1 I→C, plus 2 borderline I→C re-classifications)

The current labeling has zero `contradicts`, but multiple meta-analyses
explicitly find DBS does not improve cognition (one finds DBS subjects
get *worse*). This question's labels need significant correction.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `27567810` | 2016 | **inconclusive → contradicts** | ADvance Phase II RCT, n=42, primary outcome at 12 months: *"There were no significant differences in the primary cognitive outcomes (ADAS-Cog 13, CDR-SB) in the 'on' versus 'off' stimulation group at 12 months for the whole cohort."* Adequately-designed sham-controlled phase 2 trial with primary cognitive endpoint missed. The pivotal RCT for fornix DBS in AD. |
| `37123370` | 2023 | **inconclusive → contradicts** | DBS-AD systematic review and meta-analysis of 5 studies (6 comparisons). Verbatim: *"DBS had no impact on the cognitive ability in patients with AD"* (SMD 0.116, 95% CI -0.236 to 0.469, p=0.518). Subgroup: *"the fornix-DBS did not improve cognitive function in patients with AD"* (SMD 0.145, p=0.467). Pooled null. |
| `38088070` | 2024 | **inconclusive → contradicts** | rTMS/tDCS/DBS efficacy meta. Verbatim: *"DBS did not reverse the progression of cognitive decline (WMD of ADAS-Cog score in single-arm studies: **7.40, p<0.00001**)."* That's a significant *worsening* on ADAS-Cog with DBS — the strongest contradicting signal in the corpus. |
| `22566505` | 2012 | **supports → inconclusive** | Phase I open-label, n=5, no clinical primary endpoint. Reports cerebral glucose metabolism (PET) increases at 1 year + correlations with clinical outcomes. Mechanism / biomarker. Per strict bar, biomarker-only or mechanism studies → `inconclusive`. |
| `25721941` | 2015 | **supports → inconclusive** | Neurostimulation review covering rTMS, tDCS, transcranial electromagnetic, and DBS. Narrative. Says DBS *"might improve or at least stabilize cognitive functioning"* — hedged. Not primary efficacy evidence. |
| `34151817` | 2021 | **supports → inconclusive** | DBS-f age moderator analysis — **same cohort as `27567810`** (ADvance, n=42). Verbatim: *"the selected clinical measures did not differentiate between the 'on' and 'off' groups in the intent to treat (ITT) population."* Reports an age × treatment interaction with subgroup trends, but: *"While not significant, post-hoc analyses favored DBS-f 'off' versus 'on' over 12 months in the <65 age group but favored DBS-f 'on' versus 'off' in the ≥65 age group."* Sub-group trends, not significant. The current `supports` label is wrong; the parent ITT was null and the subgroup analysis is post-hoc. |
| `40243219` | 2025 | **supports → inconclusive** | Fornix vs NBM bilateral DBS, n=20, **prospective non-randomized observational** study. *No sham/placebo control*. "DBS significantly improved cognitive function" — but with no controls. Small, uncontrolled study. Per strict bar, this is genuinely mixed/exploratory. |

## Confirmed (no change)

- `26684775` (ADvance surgical safety report, descriptive, no efficacy primary) — **inconclusive ✓**
- `38141755` (DBS targets review, descriptive across fornix/NBM/VS) — **inconclusive ✓** (*"definitive conclusions regarding the utility of DBS for AD cannot be made"*)
- `37204563` (recent DBS trials review) — **inconclusive ✓**

## Borderline (not flipped, but flagged for cross-question policy decisions)

These entries match recurring policy categories flagged across questions. They are
left at their current label but tagged for a future cross-question policy pass.

| PMID | Year | Current | Policy category | Note |
|------|------|---------|-----------------|------|
| `36411282` | 2022 | `inconclusive` | (a) Subgroup-positive in null pooled effect | Connectomic neuromod meta, n=242. Overall pooled DBS effect 0.11 NS (p=0.63). ≥65 subgroup SMD 0.95 sig (p=0.004), <65 favors baseline NS (p=0.65). Currently `inconclusive` (genuinely mixed). Strict bar would also accept `inconclusive` here, but this is the same pattern as ADvance subgroup analyses — a positive subgroup signal in a null parent meta. Worth tagging for consistent treatment with `34151817` (which we are flipping supports→inconclusive). |
| `34083732` | 2021 | `inconclusive` | (b) Preclinical/mech-dominated review | NBM-DBS systematic review. Conclusion explicitly notes the "translation of these outcomes to current clinical practice is hampered" because animal studies used intact NBM, and calls for more preclinical work *before* further human exploration. The `inconclusive` label is consistent with the strict bar (preclinical-dominated, not clinical efficacy evidence), so no flip — but flag for the cross-question policy decision on how to treat preclinical-heavy reviews. |

## Cross-cutting issues

- **`27567810`, `34151817`, and `26684775` are all from the ADvance trial**
  (Phase II, n=42). Three PMIDs from one study, currently appearing as
  three separate votes (1 supports, 2 inconclusive). After flips, the
  three are labeled contradicts (primary endpoint paper) + inconclusive
  (post-hoc age subgroup) + inconclusive (surgical safety) — a more
  accurate representation but still triple-counted for retrieval P/R
  unless tagged for substudy filtering.
- **Policy issue (a) — subgroup-positive in null parent — appears twice**
  in this question: `34151817` (ADvance age × treatment subgroup, parent
  ITT null) and `36411282` (connectomic meta, ≥65 subgroup positive in
  null pooled effect). One is flipped (supports→inconclusive), one is
  already inconclusive. Same underlying pattern; consistent treatment
  matters for cross-question policy.
- **Policy issue (b) — preclinical-dominated review** appears in
  `34083732`. Currently `inconclusive` (correct), but flagged for the
  cross-question policy on how preclinical-heavy reviews should be
  surfaced.
- **No `contradicts` in the current labeling** is striking given that
  the pivotal phase II missed primary endpoints AND multiple metas show
  pooled null/worsening. The current label set significantly misrepresents
  the consensus.
- After flips: 0 supports, 3 contradicts, 9 inconclusive. The "contested"
  expected consensus is more accurate as "leaning negative."

## Highest-confidence flips for this question

- `27567810` inconclusive → contradicts (ADvance primary endpoint missed)
- `37123370` inconclusive → contradicts (pooled meta SMD 0.116 NS)
- `38088070` inconclusive → contradicts (DBS subjects significantly *worse* on ADAS-Cog, p<0.00001)
- `22566505` supports → inconclusive (n=5 open-label biomarker, no clinical primary)
- `34151817` supports → inconclusive (parent trial ITT null; this is post-hoc subgroup)
- `40243219` supports → inconclusive (n=20 non-randomized, no controls)

All six are unambiguous: either the abstract directly states no
significant cognitive effect, or the study lacks the design to support a
positive claim.


## signal_types (annotation layer)

Optional pattern tags per pmid. Used to distinguish "strong" vs "weak" within
a stance bucket. Untagged = strong/canonical; tagged = some caveat applies.

### Proposed new tags (Q8)

- `biomarker_only` — clinical study reporting only biomarker/imaging endpoints (e.g., PET glucose metabolism), no clinical efficacy primary
- `safety_only` — paper reports only surgical/procedural safety, AEs, or feasibility; no efficacy outcome
- `uncontrolled_observational` — prospective clinical study with no sham/placebo/randomization, efficacy claims rest on within-subject change

### Tag assignments

- `27567810` — `same_cohort_duplicate` (ADvance parent paper; cohort also reported in `34151817` and `26684775`). Note: still the strongest single contradicts signal in this set; tagging is for downstream substudy filtering only.
- `22566505` — `biomarker_only`, `pilot_positive` (n=5 phase I open-label; PET glucose metabolism endpoint, "correlations with clinical outcomes" but no clinical primary)
- `26684775` — `same_cohort_duplicate`, `safety_only` (ADvance surgical safety report; cohort also reported in `27567810` and `34151817`)
- `25721941` — `narrative_review` (covers rTMS, tDCS, transcranial EM, DBS; hedged "might improve or at least stabilize"; no pooled estimate for DBS)
- `34083732` — `preclinical_dominated` (NBM-DBS systematic review explicitly notes translation to clinical practice is hampered; calls for more preclinical work before further human studies)
- `37123370` — (none — clean canonical contradicts; pooled SMD 0.116 NS, fornix-DBS subgroup also NS)
- `36411282` — `subgroup_positive` (overall DBS pooled effect 0.11 NS; ≥65 subgroup SMD 0.95 sig — positive subgroup in null parent meta)
- `38141755` — `narrative_review` (descriptive systematic review across fornix/NBM/VS; "definitive conclusions regarding the utility of DBS for AD cannot be made"; no pooled estimate)
- `34151817` — `same_cohort_duplicate`, `subgroup_positive` (ADvance age × treatment moderator; ITT null, post-hoc age subgroup; cohort also reported in `27567810` and `26684775`)
- `38088070` — (none — clean canonical contradicts; DBS WMD on ADAS-Cog +7.40, p<0.00001, indicating worsening)
- `40243219` — `uncontrolled_observational`, `comparator_only` (n=20 prospective non-randomized; no sham/placebo arm; compares fornix vs NBM as the only contrast)
- `37204563` — `narrative_review` (descriptive overview of DBS trials in dementia; "cognitive outcomes uncertain"; no pooled estimate)
- All other pmids — untagged (none in this question)

---

## Abstracts (n=12)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 27567810 — current stance: `inconclusive`

**Stance justification:** > There were no significant differences in the primary cognitive outcomes (ADAS-Cog 13, CDR-SB) in the "on" versus "off" stimulation group at 12 months for the whole cohort.

**Golden note:** ADvance Phase II — primary endpoint missed, subgroup signal in older patients.

**A Phase II Study of Fornix Deep Brain Stimulation in Mild Alzheimer's Disease.**

*Journal of Alzheimer's disease : JAD*, 2016. Types: Clinical Trial, Phase II; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't; Research Support, N.I.H., Extramural

> BACKGROUND: Deep brain stimulation (DBS) is used to modulate the activity of dysfunctional brain circuits. The safety and efficacy of DBS in dementia is unknown. OBJECTIVE: To assess DBS of memory circuits as a treatment for patients with mild Alzheimer's disease (AD). METHODS: We evaluated active "on" versus sham "off" bilateral DBS directed at the fornix-a major fiber bundle in the brain's memory circuit-in a randomized, double-blind trial (ClinicalTrials.gov NCT01608061) in 42 patients with mild AD. We measured cognitive function and cerebral glucose metabolism up to 12 months post-implantation. RESULTS: Surgery and electrical stimulation were safe and well tolerated. There were no significant differences in the primary cognitive outcomes (ADAS-Cog 13, CDR-SB) in the "on" versus "off" stimulation group at 12 months for the whole cohort. Patients receiving stimulation showed increased metabolism at 6 months but this was not significant at 12 months. On post-hoc analysis, there was a significant interaction between age and treatment outcome: in contrast to patients <65 years old (n = 12) whose results trended toward being worse with DBS ON versus OFF, in patients≥65 (n = 30) DBS-f ON treatment was associated with a trend toward both benefit on clinical outcomes and a greater increase in cerebral glucose metabolism. CONCLUSION: DBS for AD was safe and associated with increased cerebral glucose metabolism. There were no differences in cognitive outcomes for participants as a whole, but participants aged≥65 years may have derived benefit while there was possible worsening in patients below age 65 years with stimulation.

---

### PMID 22566505 — current stance: `supports`

**Stance justification:** > In similar cortical regions, higher baseline metabolism prior to DBS and increased metabolism after 1 year of DBS were correlated with better outcomes in global cognition, memory, and quality of life.

**Golden note:** Fornix DBS Phase I — increased cerebral metabolism after 1 year.

**Increased cerebral metabolism after 1 year of deep brain stimulation in Alzheimer disease.**

*Archives of neurology*, 2012. Types: Clinical Trial; Journal Article; Research Support, N.I.H., Extramural

> BACKGROUND: The importance of developing unique, neural circuitry-based treatments for the cognitive and neuropsychiatric symptoms of Alzheimer disease (AD) was the impetus for a phase I study of deep brain stimulation (DBS) in patients with AD that targeted the fornix. OBJECTIVE: To test the hypotheses that DBS would increase cerebral glucose metabolism in cortical and hippocampal circuits and that increased metabolism would be correlated with better clinical outcomes. DESIGN: Open-label trial. SETTING: Academic medical center. PATIENTS: A total of 5 patients with mild, probable AD (1 woman and 4 men, with a mean [SD] age of 62.6 [4.2] years). INTERVENTION: Deep brain stimulation of the fornix. MAIN OUTCOME MEASURES: All patients underwent clinical follow-up and high-resolution positron emission tomography studies of cerebral glucose metabolism after 1 year of DBS. RESULTS: Functional connectivity analyses revealed that 1 year of DBS increased cerebral glucose metabolism in 2 orthogonal networks: a frontal-temporal-parietal-striatal-thalamic network and a frontal-temporal-parietal-occipital-hippocampal network. In similar cortical regions, higher baseline metabolism prior to DBS and increased metabolism after 1 year of DBS were correlated with better outcomes in global cognition, memory, and quality of life. CONCLUSIONS: Increased connectivity after 1 year of DBS is observed, which is in contrast to the decreased connectivity observed over the course of AD. The persistent cortical metabolic increases after 1 year of DBS were associated with better clinical outcomes in this patient sample and are greater in magnitude and more extensive in the effects on cortical circuitry compared with the effects reported for pharmacotherapy over 1 year in AD.

---

### PMID 26684775 — current stance: `inconclusive`

**Stance justification:** > At 90 days after surgery, bilateral fornix DBS was well tolerated by patients with mild, probable AD.

**Golden note:** ADvance surgical safety report — descriptive, no efficacy primary.

**Bilateral deep brain stimulation of the fornix for Alzheimer's disease: surgical safety in the ADvance trial.**

*Journal of neurosurgery*, 2015. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> OBJECT This report describes the stereotactic technique, hospitalization, and 90-day perioperative safety of bilateral deep brain stimulation (DBS) of the fornix in patients who underwent DBS for the treatment of mild, probable Alzheimer's disease (AD). METHODS The ADvance Trial is a multicenter, 12-month, double-blind, randomized, controlled feasibility study being conducted to evaluate the safety, efficacy, and tolerability of DBS of the fornix in patients with mild, probable AD. Intraoperative and perioperative data were collected prospectively. All patients underwent postoperative MRI. Stereotactic analyses were performed in a blinded fashion by a single surgeon. Adverse events (AEs) were reported to an independent clinical events committee and adjudicated to determine the relationship between the AE and the study procedure. RESULTS Between June 6, 2012, and April 28, 2014, a total of 42 patients with mild, probable AD were treated with bilateral fornix DBS (mean age 68.2 ± 7.8 years; range 48.0-79.7 years; 23 men and 19 women). The mean planned target coordinates were x = 5.2 ± 1.0 mm (range 3.0-7.9 mm), y = 9.6 ± 0.9 mm (range 8.0-11.6 mm), z = -7.5 ± 1.2 mm (range -5.4 to -10.0 mm), and the mean postoperative stereotactic radial error on MRI was 1.5 ± 1.0 mm (range 0.2-4.0 mm). The mean length of hospitalization was 1.4 ± 0.8 days. Twenty-six (61.9%) patients experienced 64 AEs related to the study procedure, of which 7 were serious AEs experienced by 5 patients (11.9%). Four (9.5%) patients required return to surgery: 2 patients for explantation due to infection, 1 patient for lead repositioning, and 1 patient for chronic subdural hematoma. No patients experienced neurological deficits as a result of the study, and no deaths were reported. CONCLUSIONS Accurate targeting of DBS to the fornix without direct injury to it is feasible across surgeons and treatment centers. At 90 days after surgery, bilateral fornix DBS was well tolerated by patients with mild, probable AD. Clinical trial registration no.: NCT01608061 ( clinicaltrials.gov ).

---

### PMID 25721941 — current stance: `supports`

**Stance justification:** > it has been demonstrated that DBS of fornix/hypothalamus and nucleus basalis of Meynert might improve or at least stabilize cognitive functioning in AD.

**Golden note:** Neurostimulation review — DBS one of several promising approaches in AD.

**Neurostimulation in Alzheimer's disease: from basic research to clinical applications.**

*Neurological sciences : official journal of the Italian Neurological Society and of the Italian Society of Clinical Neurophysiology*, 2015. Types: Journal Article; Systematic Review

> The development of different methods of brain stimulation provides a promising therapeutic tool with potentially beneficial effects on subjects with impaired cognitive functions. We performed a systematic review of the studies published in the field of neurostimulation in Alzheimer's disease (AD), from basic research to clinical applications. The main methods of non-invasive brain stimulation are repetitive transcranial magnetic stimulation and transcranial direct current stimulation. Preliminary findings have suggested that both techniques can enhance performances on several cognitive functions impaired in AD. Another non-invasive emerging neuromodulatory approach, the transcranial electromagnetic treatment, was found to reverse cognitive impairment in AD transgenic mice and even improves cognitive performance in normal mice. Experimental studies suggest that high-frequency electromagnetic fields may be critically important in AD prevention and treatment through their action at mitochondrial level. Finally, the application of a widely known invasive technique, the deep brain stimulation (DBS), has increasingly been considered as a therapeutic option also for patients with AD; it has been demonstrated that DBS of fornix/hypothalamus and nucleus basalis of Meynert might improve or at least stabilize cognitive functioning in AD. Initial encouraging results provide support for continuing to investigate non-invasive and invasive brain stimulation approaches as an adjuvant treatment for AD patients.

---

### PMID 34083732 — current stance: `inconclusive`

**Stance justification:** > However, the clinical effects are highly variable, which questions the suggested basic principles underlying these clinical trials.

**Golden note:** NBM-DBS review — clinical effects 'highly variable'.

**Electrical stimulation of the nucleus basalis of meynert: a systematic review of preclinical and clinical data.**

*Scientific reports*, 2021. Types: Journal Article; Meta-Analysis; Systematic Review

> Deep brain stimulation (DBS) of the nucleus basalis of Meynert (NBM) has been clinically investigated in Alzheimer's disease (AD) and Lewy body dementia (LBD). However, the clinical effects are highly variable, which questions the suggested basic principles underlying these clinical trials. Therefore, preclinical and clinical data on the design of NBM stimulation experiments and its effects on behavioral and neurophysiological aspects are systematically reviewed here. Animal studies have shown that electrical stimulation of the NBM enhanced cognition, increased the release of acetylcholine, enhanced cerebral blood flow, released several neuroprotective factors, and facilitates plasticity of cortical and subcortical receptive fields. However, the translation of these outcomes to current clinical practice is hampered by the fact that mainly animals with an intact NBM were used, whereas most animals were stimulated unilaterally, with different stimulation paradigms for only restricted timeframes. Future animal research has to refine the NBM stimulation methods, using partially lesioned NBM nuclei, to better resemble the clinical situation in AD, and LBD. More preclinical data on the effect of stimulation of lesioned NBM should be present, before DBS of the NBM in human is explored further.

---

### PMID 37123370 — current stance: `inconclusive`

**Stance justification:** > DBS had no impact on the cognitive ability in patients with AD [0.116 SMD, 95% confidence interval (CI), -0.236 to 0.469, p = 0.518]. According to subgroup analysis, the fornix-DBS did not improve cognitive function in patients with AD (0.145 SMD, 95%CI, -0.246 to 0.537, p = 0.467).

**Golden note:** DBS-AD systematic review/meta — modest, heterogeneous.

**Deep brain stimulation for the treatment of Alzheimer's disease: A systematic review and meta-analysis.**

*Frontiers in neuroscience*, 2023. Types: Systematic Review; Journal Article

> BACKGROUND: One of the experimental neuromodulation techniques being researched for the treatment of Alzheimer's disease (AD) is deep brain stimulation (DBS). To evaluate the effectiveness of DBS in AD, we performed a systematic review and meta-analysis of the available evidence. METHODS: From the inception through December 2021, the following databases were searched: Medline via PubMed, Scopus, Embase, Cochrane Library, and Web of Science. The search phrases used were "Alzheimer's disease," "AD," "deep brain stimulation," and "DBS." The information from the included articles was gathered using a standardized data-collecting form. In the included papers, the Cochrane Collaboration methodology was used to evaluate the risk of bias. A fixed-effects model was used to conduct the meta-analysis. RESULTS: Only five distinct publications and 6 different comparisons (one study consisted of two phases) were included out of the initial 524 papers that were recruited. DBS had no impact on the cognitive ability in patients with AD [0.116 SMD, 95% confidence interval (CI), -0.236 to 0.469, p = 0.518]. The studies' overall heterogeneity was not significant (κ2 = 6.23, T 2 = 0.053, df = 5, I 2 = 19.76%, p = 0.284). According to subgroup analysis, the fornix-DBS did not improve cognitive function in patients with AD (0.145 SMD, 95%CI, -0.246 to 0.537, p = 0.467). Unfavorable neurological and non-neurological outcomes were also reported. CONCLUSION: The inconsistencies and heterogeneity of the included publications in various target and age groups of a small number of AD patients were brought to light by this meta-analysis. To determine if DBS is useful in the treatment of AD, further studies with larger sample sizes and randomized, double-blinded, sham-controlled designs are required.

---

### PMID 36411282 — current stance: `inconclusive`

**Stance justification:** > On fixed-effect meta-analysis, non-invasive neuromodulation favored baseline, with effect size -0.40(95% [CI], -0.73, -0.06, p = 0.02), while that of DBS was 0.11(95% [CI] -0.34, 0.56, p = 0.63), in favor of DBS.

**Golden note:** Connectomic neuromodulation review — cognitive outcome unclear.

**Connectomic neuromodulation for Alzheimer's disease: A systematic review and meta-analysis of invasive and non-invasive techniques.**

*Translational psychiatry*, 2022. Types: Meta-Analysis; Systematic Review; Journal Article

> Deep brain stimulation (DBS) and non-invasive neuromodulation are currently being investigated for treating network dysfunction in Alzheimer's Disease (AD). However, due to heterogeneity in techniques and targets, the cognitive outcome and brain network connectivity remain unknown. We performed a systematic review, meta-analysis, and normative functional connectivity to determine the cognitive outcome and brain networks of DBS and non-invasive neuromodulation in AD. PubMed, Embase, and Web of Science were searched using three concepts: dementia, brain connectome, and brain stimulation, with filters for English, human studies, and publication dates 1980-2021. Additional records from clinicaltrials.gov were added. Inclusion criteria were AD study with DBS or non-invasive neuromodulation and a cognitive outcome. Exclusion criteria were less than 3-months follow-up, severe dementia, and focused ultrasound intervention. Bias was assessed using Centre for Evidence-Based Medicine levels of evidence. We performed meta-analysis, with subgroup analysis based on type and age at neuromodulation. To determine the patterns of neuromodulation-induced brain network activation, we performed normative functional connectivity using rsfMRI of 1000 healthy subjects. Six studies, with 242 AD patients, met inclusion criteria. On fixed-effect meta-analysis, non-invasive neuromodulation favored baseline, with effect size -0.40(95% [CI], -0.73, -0.06, p = 0.02), while that of DBS was 0.11(95% [CI] -0.34, 0.56, p = 0.63), in favor of DBS. In patients ≥65 years old, DBS improved cognitive outcome, 0.95(95% [CI] 0.31, 1.58, p = 0.004), whereas in patients <65 years old baseline was favored, -0.17(95% [CI] -0.93, 0.58, p = 0.65). Functional connectivity regions were in the default mode (DMN), salience (SN), central executive (CEN) networks, and Papez circuit. The subgenual cingulate and anterior limb of internal capsule (ALIC) showed connectivity to all targets of neuromodulation. This meta-analysis provides level II evidence of a difference in response of AD patients to DBS, based on age at intervention. Brain stimulation in AD may modulate DMN, SN, CEN, and Papez circuit, with the subgenual cingulate and ALIC as potential targets.

---

### PMID 38141755 — current stance: `inconclusive`

**Stance justification:** > Because of varying study parameters, varying outcome measures, varying study durations, and limited cohort sizes, definitive conclusions regarding the utility of DBS for AD cannot be made.

**Golden note:** DBS systematic review of targets — efficacy varies; no consistent benefit.

**Deep Brain Stimulation as an Emerging Therapy for Cognitive Decline in Alzheimer Disease: Systematic Review of Evidence and Current Targets.**

*World neurosurgery*, 2023. Types: Systematic Review; Journal Article

> OBJECTIVE: With no cure for Alzheimer disease (AD), current efforts involve therapeutics that prevent further cognitive impairment. Deep brain stimulation (DBS) has been studied for its potential to mitigate AD symptoms. This systematic review investigates the efficacy of current and previous targets for their ability to slow cognitive decline in treating AD. METHODS: A systematic review of the literature was performed through a search of the PubMed, Scopus, and Web of Science databases. Human studies between 1994 and 2023 were included. Sample size, cognitive outcomes, and complications were recorded for each study. RESULTS: Fourteen human studies were included: 7 studies with 6 distinct cohorts (n = 56) targeted the fornix, 6 studies with 3 distinct cohorts (n = 17) targeted the nucleus basalis of Meynert (NBM), and 1 study (n = 3) investigated DBS of the ventral striatum (VS). The Alzheimer's Disease Assessment Scale-Cognitive Subscale, Mini-Mental State Examination, and Clinical Dementia Rating Scale Sum of Boxes were used as the primary outcomes. In 5 of 6 cohorts where DBS targeted the fornix, cognitive decline was slowed based on the Alzheimer's Disease Assessment Scale-Cognitive Subscale or Mini-Mental State Examination scores. In 2 of 3 NBM cohorts, a similar reduction was reported. When DBS targeted the VS, the patients' Clinical Dementia Rating Scale Sum of Boxes scores indicated a slowed decline. CONCLUSIONS: This review summarizes current evidence and addresses variability in study designs regarding the therapeutic benefit of DBS of the fornix, NBM, and VS. Because of varying study parameters, varying outcome measures, varying study durations, and limited cohort sizes, definitive conclusions regarding the utility of DBS for AD cannot be made. Further investigation is needed to determine the safety and efficacy of DBS for AD.

---

### PMID 34151817 — current stance: `supports`

**Stance justification:** > However, the selected clinical measures did not differentiate between the "on" and "off" groups in the intent to treat (ITT) population.

**Golden note:** DBS-f age-moderator analysis — older patients showed better outcomes (subgroup positive).

**Effect of Age on Clinical Trial Outcome in Participants with Probable Alzheimer's Disease.**

*Journal of Alzheimer's disease : JAD*, 2021. Types: Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't

> BACKGROUND: Age may affect treatment outcome in trials of mild probable Alzheimer's disease (AD). OBJECTIVE: We examined age as a moderator of outcome in an exploratory study of deep brain stimulation targeting the fornix (DBS-f) region in participants with AD. METHODS: Forty-two participants were implanted with DBS electrodes and randomized to double-blind DBS-f stimulation ("on") or sham DBS-f ("off") for 12 months. RESULTS: The intervention was safe and well tolerated. However, the selected clinical measures did not differentiate between the "on" and "off" groups in the intent to treat (ITT) population. There was a significant age by time interaction with the Alzheimer's Disease Assessment Scale; ADAS-cog-13 (p = 0.028). Six of the 12 enrolled participants < 65 years old (50%) markedly declined on the ADAS-cog-13 versus only 6.7%of the 30 participants≥65 years old regardless of treatment assignment (p = 0.005). While not significant, post-hoc analyses favored DBS-f "off" versus "on" over 12 months in the < 65 age group but favored DBS-f "on" versus "off" in the≥65 age group on all clinical metrics. On the integrated Alzheimer's Disease rating scale (iADRS), the effect size contrasting DBS-f "on" versus "off" changed from +0.2 (favoring "off") in the < 65 group to -0.52 (favoring "on") in the≥65 age group. CONCLUSION: The findings highlight issues with subject selection in clinical trials for AD. Faster disease progression in younger AD participants with different AD sub-types may influence the results. Biomarker confirmation and genotyping to differentiate AD subtypes is important for future clinical trials.

---

### PMID 38088070 — current stance: `inconclusive`

**Stance justification:** > DBS did not reverse the progression of cognitive decline (WMD of ADAS-Cog score in single-arm studies: 7.40, p < 0.00001).

**Golden note:** rTMS/tDCS/DBS meta — DBS efficacy mixed.

**Efficacy analysis of three brain stimulation techniques for Alzheimer's disease: a meta-analysis of repeated transcranial magnetic stimulation, transcranial direct current stimulation, and deep brain stimulation.**

*Expert review of neurotherapeutics*, 2024. Types: Meta-Analysis; Systematic Review; Journal Article; Research Support, Non-U.S. Gov't

> INTRODUCTION: This systematic review and meta-analysis study investigates the efficacy of repeated transcranial magnetic stimulation (rTMS), transcranial direct current stimulation (tDCS), and deep brain stimulation (DBS) using neuropsychological assessments as a potential treatment option for Alzheimer's disease (AD). METHODS: PubMed, Embase, and the Cochrane Library were searched for studies on rTMS, tDCS, and DBS for the treatment of patients with AD between April 1970 and October 2022. The mini-Mental State Examination (MMSE) and AD Assessment Scale - Cognitive Subscale (ADAS-Cog) were adopted as the efficacy index. RESULTS: The analysis yielded 17 eligible studies. rTMS greatly improved the cognition of patients with AD (immediate post-treatment WMD of MMSE score: 2.06, p < 0.00001; short-term follow-up WMD of MMSE score: 2.12, p = 0.006; WMD of ADAS-Cog score in single-arm studies: -4.97, p = 0.001). DBS did not reverse the progression of cognitive decline (WMD of ADAS-Cog score in single-arm studies: 7.40, p < 0.00001). Furthermore, tDCS demonstrated no significant efficacy in improving cognition in random clinical trials or single-arm studies. CONCLUSION: rTMS is a promising non-medicinal alternative for cognitive improvement inpatients with AD.

---

### PMID 40243219 — current stance: `supports`

**Stance justification:** > Early on, DBS significantly improved cognitive function and quality of life.

**Golden note:** Fornix vs NBM bilateral DBS comparison — both effective in severe AD.

**Efficacy and Safety of Bilateral Deep Brain Stimulation (DBS) for Severe Alzheimer's Disease: A Comparative Analysis of Fornix Versus Basal Ganglia of Meynert.**

*CNS neuroscience & therapeutics*, 2025. Types: Comparative Study; Journal Article; Observational Study

> BACKGROUND: Deep brain stimulation (DBS) is a novel therapy for severe Alzheimer's disease (AD). However, there is an ongoing debate regarding the optimal target for DBS, particularly the fornix and the basal ganglia of Meynert (NBM). OBJECTIVE: This study aimed to investigate the safety and efficacy of DBS for severe AD and to compare the fornix and the NBM as potential targets. METHODS: We conducted a prospective, nonrandomized clinical study involving 20 patients with severe AD (MMSE score 0 to 10, CDR level 3) from January 2015 to August 2022, comprising 12 males and eight females, with a mean age of 59.05 ± 6.45 years. All patients underwent DBS treatment, among which 14 received bilateral fornix implantation, while six received bilateral implantation in the NBM. Electrical stimulation commenced 1 month postoperatively. We assessed the patients before surgery, followed by evaluations at 1 month, 3 months, 6 months, and 12 months poststimulation. Primary outcome measures focused on changes in cognitive function, assessed using the MMSE, MoCA, ADAS-Cog, and CDR scales. Secondary measures encompassed quality of life, caregiver burden, neuropsychiatric symptoms, and sleep disturbances, evaluated through the BI, FAQ, FIM, ZBI, NPI, HAMA, HAMD, and PSQI scales. RESULTS: All patients tolerated DBS well, with no serious adverse effects reported. Early on, DBS significantly improved cognitive function and quality of life. Long-term benefits include the improvement of neuropsychiatric symptoms and sleep disorders and the alleviation of caregiver burden. Comparison between DBS targeting the NBM and fornix revealed no significant differences in overall scale scores. However, upon deeper analysis, NBM-DBS exhibited a more pronounced improvement in neuropsychiatric symptoms, particularly in NPI scores. CONCLUSION: DBS is a potential therapeutic approach for severe AD, capable of improving patients' cognitive function, quality of life, and neuropsychiatric symptoms. Notably, NBM-DBS showed distinct advantages in ameliorating neuropsychiatric symptoms, providing valuable insights for clinically selecting the optimal DBS target. TRIAL REGISTRATION: ClinicalTrials.gov identifier: NCT03115814.

---

### PMID 37204563 — current stance: `inconclusive`

**Stance justification:** > The population investigated is small and heterogeneous, published results from clinical trials are under-represented, severe adverse events not negligible, and cognitive outcomes uncertain.

**Golden note:** Recent DBS trials in dementia review — descriptive.

**An updated overview of recent and ongoing deep brain stimulation (DBS) trials in patients with dementia: a systematic review.**

*Neurological sciences : official journal of the Italian Neurological Society and of the Italian Society of Clinical Neurophysiology*, 2023. Types: Systematic Review; Journal Article

> BACKGROUND: Dementia affects more than 55 million people worldwide. Several technologies have been developed to slow cognitive decline: deep brain stimulation (DBS) of network targets in Alzheimer's disease (AD) and dementia with Lewy bodies (DLB) have been recently investigated. OBJECTIVE: This study aimed to review the characteristics of the populations, protocols, and outcomes of patients with dementia enrolled in clinical trials investigating the feasibility and efficacy of DBS. MATERIALS AND METHODS: A systematic search of all registered RCTs was performed on Clinicaltrials.gov and EudraCT, while a systematic literature review was conducted on PubMed, Scopus, Cochrane, and APA PsycInfo to identify published trials. RESULTS: The literature search yielded 2122 records, and the clinical trial search 15 records. Overall, 17 studies were included. Two of 17 studies were open-label studies reporting no NCT/EUCT code and were analysed separately. Of 12 studies investigating the role of DBS in AD, we included 5 published RCTs, 2 unregistered open-label (OL) studies, 3 recruiting studies, and 2 unpublished trials with no evidence of completion. The overall risk of bias was assessed as moderate-high. Our review showed significant heterogeneity in the recruited populations regarding age, disease severity, informed consent availability, inclusion, and exclusion criteria. Notably, the standard mean of overall severe adverse events was moderately high (SAEs: 9.10 ± 7.10%). CONCLUSION: The population investigated is small and heterogeneous, published results from clinical trials are under-represented, severe adverse events not negligible, and cognitive outcomes uncertain. Overall, the validity of these studies requires confirmation based on forthcoming higher-quality clinical trials.

---

