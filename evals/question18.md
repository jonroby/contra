# Q18: Is occupational aluminum exposure associated with Alzheimer's disease risk?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=9 PMIDs.

**Current S/C/I**: 4 / 3 / 2
**Proposed S/C/I**: 4 / 2 / 3 (after one major direction flip and two
relabelings)
**Final S/C/I (after reviewer pass)**: 4 / 2 / 3
**Net flips**: 3 (all confirmed)

This question has a notable mislabel: the most-relevant
meta-analysis on occupational aluminum exposure (`26247643`) reports
**OR 1.00 (CI 0.59-1.68)** — i.e., explicitly null — but is currently
labeled `supports` with a note saying "found increased AD risk." That's
a direct mislabel. Two other labels also reverse the abstract's
direction.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `26247643` | 2015 | **supports → contradicts** | Occupational Al exposure meta of 3 case-control studies, n=1056. Verbatim: *"Occupational aluminum exposure was **not associated with AD** (odds ratio, 1.00; 95% confidence interval, 0.59 to 1.68), even in sensitivity analysis."* Conclusion verbatim: *"The findings of the present meta-analysis **do not support** a causative role of aluminum in the pathogenesis of AD."* The current note ("found increased AD risk") **directly contradicts** the abstract. The pooled OR 1.00 with confidence intervals straddling null is a clear `contradicts` under the strict bar. **This is the most important flip in Q18 — the question's central piece of evidence is mislabeled.** |
| `39889875` | 2025 | **contradicts → inconclusive** | Environmental risk umbrella review. Verbatim: *"In a narrative review, we found that exposure to sulfur dioxide, proximity to roadways, ionizing radiation, **aluminum**, solvents, pesticides, and environmental tobacco smoke were also associated with dementia."* So aluminum was in the **narrative-review-positive list**, not the meta-analysis-positive list. The current `contradicts` label is not supported — the abstract actually mentions Al as associated with dementia in the narrative tier. Mixed direction → `inconclusive`. |
| `18000416` | 2007 | **contradicts → inconclusive** | Quebec aluminum smelter cohort mortality. Verbatim: *"Statistically significant causes of death were lung cancer (three plants); bladder cancer; chronic obstructive lung disease (two plants each); cancers of the stomach... and **Alzheimer's disease (one plant)**; and cerebrovascular disease (one plant)."* AD mortality WAS statistically significantly elevated in one of the three plants — the note ("no excess AD") is wrong. Direction is mixed across plants → `inconclusive` (or `supports` since 1/3 plants showed sig increase). Mark as `inconclusive` because not consistent across plants. |

## Confirmed (no change)

- `27729011` (environmental risk SR) — **inconclusive ✓** (Al "moderate evidence" but mixed)
- `25233067` (Al critical review 2014) — **contradicts ✓** ("no consistent and convincing evidence to associate the Al found in food and drinking water... with increased risk for AD")
- `12520766` (Italian foundry workers case-control n=64+32) — **supports ✓** (small but reports neurotoxic effects + cognitive testing differences)
- `12602134` (Spanish drinking water review) — **inconclusive ✓**
- `37777128` (Al exposure + cognitive performance meta) — **supports ✓** (sig worse cognitive performance in occupationally exposed workers)
- `40749395` (env Al + AD risk meta) — **supports ✓** (Hedges' g 2.451 sig)

## Cross-cutting issues

- **Outcome scope mismatch**: `37777128` reports cognitive performance
  decrement, not AD specifically. `40749395` is environmental
  (drinking water + diet) Al, not occupational. The question is
  specifically *occupational Al exposure*, but ~3 of 9 papers conflate
  occupational with environmental sources.
- **The `supports` and `contradicts` labels are both right and wrong
  for this question** depending on whether you weight (a) the
  highest-quality occupational-specific meta (`26247643`, null) or
  (b) the broader Al-exposure-cognition signal (significantly worse
  performance, `37777128`). After the proposed flips, the corpus
  shows: 4 supports / 2 contradicts / 3 inconclusive — closer to
  the `expected_consensus: "contested"` than the current 4/3/2 because
  the major mislabel is corrected.

## Highest-confidence flips for this question

- `26247643` supports → contradicts — **the central meta on the
  question explicitly says "do not support a causative role"; the
  current label is a direct mislabel.**

## Reviewer pass (Q18)

All 3 originally proposed flips **confirmed**:

- `26247643` supports → contradicts — meta OR 1.00 (CI 0.59-1.68); verbatim
  conclusion "do not support a causative role." Clean meta-analysis-null
  flip.
- `39889875` contradicts → inconclusive — Al is in the narrative-review
  positive list ("also associated with dementia"); the current
  `contradicts` label inverts the abstract.
- `18000416` contradicts → inconclusive — AD mortality WAS statistically
  significantly elevated in 1 of 3 plants. Mixed direction across plants.

No additional verbatim-mismatch flips identified.

**Borderline (not flipped):**

- `40749395` supports — environmental Al meta (Hedges' g 2.451 sig). The
  abstract lists occupational settings as one exposure source but
  the pooled effect mixes environmental (water/diet/soil) with occupational.
  The question asks specifically about occupational Al; this is a
  `wrong_population` / scope-mismatch flag, but the direction is supported
  by sig pooled effect — keeping `supports`.
- `37777128` supports — cognitive performance meta (processing speed,
  working memory, attention, reaction time), not AD diagnosis. Outcome
  scope mismatch but conclusion explicitly extends discourse to AD.
  Sig pooled effect → keeping `supports` with caveat tag.
- `12520766` supports — small Italian foundry case-control (n=64 vs 32)
  with MMSE/CDT/P300 endpoints, not AD diagnosis. Author conclusion
  speculative ("authors raise the question whether"). Borderline
  pilot/proof-of-concept — keeping `supports` per existing review.

**Recurring policy issues observed in Q18:**

- (b) preclinical/mechanism-dominated review labeled `supports`: not
  applicable here (the supports labels are empirical, not preclinical).
- Outcome scope mismatch (`37777128`, `40749395`, `12520766`): not one
  of the 3 cross-question categories, but already flagged in the
  Cross-cutting issues section above. Tag as `wrong_population` /
  `non_diagnostic_outcome`.

**Final S/C/I after this pass: 4 / 2 / 3** (confirms reviewer's proposal).

## signal_types (annotation layer)

Tags annotate caveats orthogonal to the stance label. They do not change
the stance; they describe *why* a researcher should read the entry with
care.

### Proposed new tags (Q18)

- `non_diagnostic_outcome` — paper measures cognitive performance,
  biomarkers, or mortality proxies rather than clinical AD diagnosis,
  even though the question is framed around AD risk. Distinct from
  `biomarker_only` (which implies no clinical endpoint at all);
  `non_diagnostic_outcome` covers cases where the outcome IS clinical
  but isn't AD diagnosis specifically (e.g., processing speed, P300
  latency, all-cause dementia mortality at one of N plants).

### Tags by PMID

| PMID | Stance (final) | Tags |
|------|----------------|------|
| `27729011` | inconclusive | `broad_scope_review`, `hedged_meta` |
| `25233067` | contradicts | `broad_scope_review` |
| `12520766` | supports | `case_series_underpowered`, `non_diagnostic_outcome`, `pilot_positive` |
| `26247643` | contradicts (FLIP) | `hedged_meta` |
| `39889875` | inconclusive (FLIP) | `narrative_review`, `split_outcome` |
| `18000416` | inconclusive (FLIP) | `subgroup_positive`, `non_diagnostic_outcome` |
| `12602134` | inconclusive | `narrative_review`, `wrong_population` |
| `37777128` | supports | `non_diagnostic_outcome`, `wrong_population` |
| `40749395` | supports | `wrong_population` |

**Tag distribution (9 pmids tagged, 16 tag-instances):**

- `wrong_population`: 3 (12602134, 37777128, 40749395)
- `non_diagnostic_outcome`: 3 (12520766, 18000416, 37777128)
- `broad_scope_review`: 2 (27729011, 25233067)
- `narrative_review`: 2 (39889875, 12602134)
- `hedged_meta`: 2 (27729011, 26247643)
- `case_series_underpowered`: 1 (12520766)
- `pilot_positive`: 1 (12520766)
- `split_outcome`: 1 (39889875)
- `subgroup_positive`: 1 (18000416)

Notes:

- `wrong_population` here flags occupational-vs-environmental scope
  mismatch (the question is specifically occupational Al exposure).
- The two `supports` papers that survive review (`37777128`, `40749395`)
  are both flagged with caveats — researchers reading the bucket should
  see that the strongest "supports" evidence is on cognitive performance
  generally or environmental exposure broadly, NOT occupational AD
  diagnosis specifically.
- `26247643` (the central occupational-AD meta, now correctly labeled
  `contradicts`) is `hedged_meta` because the abstract explicitly hedges
  ("a role for aluminum cannot be definitively excluded"). The hedge does
  NOT change the stance — pooled OR 1.00 with CI straddling null is a
  meta-analysis null finding.

---

## Abstracts (n=9)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 27729011 — current stance: `inconclusive`

**Stance justification:** > There is at least moderate evidence implicating the following risk factors: air pollution; aluminium; silicon; selenium; pesticides; vitamin D deficiency; and electric and magnetic fields.

**Golden note:** Environmental risk factors systematic review — Al evidence limited and mixed.

**Environmental risk factors for dementia: a systematic review.**

*BMC geriatrics*, 2016. Types: Journal Article; Systematic Review

> BACKGROUND: Dementia risk reduction is a major and growing public health priority. While certain modifiable risk factors for dementia have been identified, there remains a substantial proportion of unexplained risk. There is evidence that environmental risk factors may explain some of this risk. Thus, we present the first comprehensive systematic review of environmental risk factors for dementia. METHODS: We searched the PubMed and Web of Science databases from their inception to January 2016, bibliographies of review articles, and articles related to publically available environmental data. Articles were included if they examined the association between an environmental risk factor and dementia. Studies with another outcome (for example, cognition), a physiological measure of the exposure, case studies, animal studies, and studies of nutrition were excluded. Data were extracted from individual studies which were, in turn, appraised for methodological quality. The strength and consistency of the overall evidence for each risk factor identified was assessed. RESULTS: We screened 4784 studies and included 60 in the review. Risk factors were considered in six categories: air quality, toxic heavy metals, other metals, other trace elements, occupational-related exposures, and miscellaneous environmental factors. Few studies took a life course approach. There is at least moderate evidence implicating the following risk factors: air pollution; aluminium; silicon; selenium; pesticides; vitamin D deficiency; and electric and magnetic fields. CONCLUSIONS: Studies varied widely in size and quality and therefore we must be circumspect in our conclusions. Nevertheless, this extensive review suggests that future research could focus on a short list of environmental risk factors for dementia. Furthermore, further robust, longitudinal studies with repeated measures of environmental exposures are required to confirm these associations.

---

### PMID 25233067 — current stance: `contradicts`

**Stance justification:** > Aluminum has been held responsible for human morbidity and mortality, but there is no consistent and convincing evidence to associate the Al found in food and drinking water at the doses and chemical forms presently consumed by people living in North America and Western Europe with increased risk for Alzheimer's disease (AD).

**Golden note:** Comprehensive Al exposure systematic review — concludes evidence does NOT support Al causation.

**Systematic review of potential health risks posed by pharmaceutical, occupational and consumer exposures to metallic and nanoscale aluminum, aluminum oxides, aluminum hydroxide and its soluble salts.**

*Critical reviews in toxicology*, 2014. Types: Journal Article; Research Support, Non-U.S. Gov't; Systematic Review

> Abstract Aluminum (Al) is a ubiquitous substance encountered both naturally (as the third most abundant element) and intentionally (used in water, foods, pharmaceuticals, and vaccines); it is also present in ambient and occupational airborne particulates. Existing data underscore the importance of Al physical and chemical forms in relation to its uptake, accumulation, and systemic bioavailability. The present review represents a systematic examination of the peer-reviewed literature on the adverse health effects of Al materials published since a previous critical evaluation compiled by Krewski et al. (2007) . Challenges encountered in carrying out the present review reflected the experimental use of different physical and chemical Al forms, different routes of administration, and different target organs in relation to the magnitude, frequency, and duration of exposure. Wide variations in diet can result in Al intakes that are often higher than the World Health Organization provisional tolerable weekly intake (PTWI), which is based on studies with Al citrate. Comparing daily dietary Al exposures on the basis of "total Al"assumes that gastrointestinal bioavailability for all dietary Al forms is equivalent to that for Al citrate, an approach that requires validation. Current occupational exposure limits (OELs) for identical Al substances vary as much as 15-fold. The toxicity of different Al forms depends in large measure on their physical behavior and relative solubility in water. The toxicity of soluble Al forms depends upon the delivered dose of Al(+3) to target tissues. Trivalent Al reacts with water to produce bidentate superoxide coordination spheres [Al(O2)(H2O4)(+2) and Al(H2O)6 (+3)] that after complexation with O2(•-), generate Al superoxides [Al(O2(•))](H2O5)](+2). Semireduced AlO2(•) radicals deplete mitochondrial Fe and promote generation of H2O2, O2 (•-) and OH(•). Thus, it is the Al(+3)-induced formation of oxygen radicals that accounts for the oxidative damage that leads to intrinsic apoptosis. In contrast, the toxicity of the insoluble Al oxides depends primarily on their behavior as particulates. Aluminum has been held responsible for human morbidity and mortality, but there is no consistent and convincing evidence to associate the Al found in food and drinking water at the doses and chemical forms presently consumed by people living in North America and Western Europe with increased risk for Alzheimer's disease (AD). Neither is there clear evidence to show use of Al-containing underarm antiperspirants or cosmetics increases the risk of AD or breast cancer. Metallic Al, its oxides, and common Al salts have not been shown to be either genotoxic or carcinogenic. Aluminum exposures during neonatal and pediatric parenteral nutrition (PN) can impair bone mineralization and delay neurological development. Adverse effects to vaccines with Al adjuvants have occurred; however, recent controlled trials found that the immunologic response to certain vaccines with Al adjuvants was no greater, and in some cases less than, that after identical vaccination without Al adjuvants. The scientific literature on the adverse health effects of Al is extensive. Health risk assessments for Al must take into account individual co-factors (e.g., age, renal function, diet, gastric pH). Conclusions from the current review point to the need for refinement of the PTWI, reduction of Al contamination in PN solutions, justification for routine addition of Al to vaccines, and harmonization of OELs for Al substances.

---

### PMID 12520766 — current stance: `supports`

**Stance justification:** > These findings suggest a role of aluminium in early neurotoxic effects that can be detected at a pre-clinical stage by P300, MMSE, MMSE-time, CDT-time and CDT score, considering a 10 micrograms/l cut-off level of serum aluminium, in aluminium foundry workers with concomitant high blood levels of iron.

**Golden note:** Italian foundry workers case-control — neurotoxic effects, suggests role in AD.

**Neurotoxic effects of aluminium among foundry workers and Alzheimer's disease.**

*Neurotoxicology*, 2002. Types: Comparative Study; Journal Article

> BACKGROUND: In a cross-sectional case-control study conducted in northern Italy, 64 former aluminium dust-exposed workers were compared with 32 unexposed controls from other companies matched for age, professional training, economic status, educational and clinical features. The findings lead the authors to suggest a possible role of the inhalation of aluminium dust in pre-clinical mild cognitive disorder which might prelude Alzheimer's disease (AD) or AD-like neurological deterioration. METHODS: The investigation involved a standardised occupational and medical history with particular attention to exposure and symptoms, assessments of neurotoxic metals in serum: aluminium (Al-s), copper (Cu-s) and zinc (Zn-s), and in blood: manganese (Mn-b), lead (Pb-b) and iron (Fe-b). Cognitive functions were assessed by the Mini Mental State Examination (MMSE), the Clock Drawing Test (CDT) and auditory evoked Event-Related Potential (ERP-P300). To detect early signs of mild cognitive impairment (MCI), the time required to solve the MMSE (MMSE-time) and CDT (CDT-time) was also measured. RESULTS: Significantly higher internal doses of Al-s and Fe-b were found in the ex-employees compared to the control group. The neuropsychological tests showed a significant difference in the latency of P300, MMSE score, MMSE-time, CDT score and CDT-time between the exposed and the control population. P300 latency was found to correlate positively with Al-s and MMSE-time. Al-s has significant effects on all tests: a negative relationship was observed between internal Al concentrations, MMSE score and CDT score; a positive relationship was found between internal Al concentrations, MMSE-time and CDT-time. All the potential confounders such as age, height, weight, blood pressure, schooling years, alcohol, coffee consumption and smoking habit were taken into account. CONCLUSIONS: These findings suggest a role of aluminium in early neurotoxic effects that can be detected at a pre-clinical stage by P300, MMSE, MMSE-time, CDT-time and CDT score, considering a 10 micrograms/l cut-off level of serum aluminium, in aluminium foundry workers with concomitant high blood levels of iron. The authors raise the question whether pre-clinical detection of aluminium neurotoxicity and consequent early treatment might help to prevent or retard the onset of AD or AD-like pathologies.

---

### PMID 26247643 — current stance: `supports`

**Stance justification:** > Occupational aluminum exposure was not associated with AD (odds ratio, 1.00; 95% confidence interval, 0.59 to 1.68), even in sensitivity analysis excluding studies with low-quality assessment scores (odds ratio, 1.06; 95% confidence interval, 0.36 to 3.10). The findings of the present meta-analysis do not support a causative role of aluminum in the pathogenesis of AD.

**Golden note:** Occupational Al exposure meta — found increased AD risk.

**Occupational Exposure to Aluminum and Alzheimer Disease: A Meta-Analysis.**

*Journal of occupational and environmental medicine*, 2015. Types: Journal Article; Meta-Analysis

> OBJECTIVE: We conducted a meta-analysis to systematically quantify the association between occupational exposure to aluminum and risk of Alzheimer disease (AD). METHODS: Electronic database searches were conducted up to March 2015 for controlled studies. Study quality was assessed using the Newcastle-Ottawa Scale. RESULTS: Three retrospective case-control studies, involving 1056 participants, met the criteria for inclusion. All studies used surrogate informants to ascertain exposure. Occupational aluminum exposure was not associated with AD (odds ratio, 1.00; 95% confidence interval, 0.59 to 1.68), even in sensitivity analysis excluding studies with low-quality assessment scores (odds ratio, 1.06; 95% confidence interval, 0.36 to 3.10). CONCLUSIONS: The findings of the present meta-analysis do not support a causative role of aluminum in the pathogenesis of AD. Nevertheless, in the absence of prospective studies with more precise ascertainment of exposure, a role for aluminum cannot be definitively excluded.

---

### PMID 39889875 — current stance: `contradicts`

**Stance justification:** > In a narrative review, we found that exposure to sulfur dioxide, proximity to roadways, ionizing radiation, aluminum, solvents, pesticides, and environmental tobacco smoke were also associated with dementia.

**Golden note:** Recent umbrella review — Al not a confirmed environmental risk factor for dementia.

**Environmental risk factors for all-cause dementia, Alzheimer's disease dementia, vascular dementia, and mild cognitive impairment: An umbrella review and meta-analysis.**

*Environmental research*, 2025. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: Mitigation of environmental risk factors for neurocognitive disorders could reduce the number of incident cases. We sought to synthesize the literature on environmental risk factors for dementia and mild cognitive impairment. METHODS: We conducted an umbrella review and meta-analysis. Multiple databases were systematically searched to identify systematic reviews and meta-analyses of longitudinal studies examining environmental risk factors for dementia or mild cognitive impairment. We used random effects multi-level, meta-analytic models to synthesize risk ratios for each risk factor while accounting for overlap in the studies within reviews. As a secondary objective, we examined risk factors for two common phenotypes of dementia: Alzheimer's disease dementia and vascular dementia. RESULTS: A total of 19 reviews containing 37 meta-analyses were included umbrella review. We found 9 factors where exposure was associated with higher risks of all-cause dementia: fine particulate matter, particulate matter, nitrogen dioxide, nitrogen oxides, carbon monoxide, shift work, night shift work, chronic noise, and extremely-low frequency magnetic fields. Neighbourhood greenness was associated with a lower risk of all-cause dementia. In a narrative review, we found that exposure to sulfur dioxide, proximity to roadways, ionizing radiation, aluminum, solvents, pesticides, and environmental tobacco smoke were also associated with dementia. We also found that fine particulate matter, extremely-low frequency magnetic fields, sulfur dioxide, chronic noise, and pesticides were related to Alzheimer's disease dementia. Fine particulate matter, particulate matter, and chronic noise were related to vascular dementia. No systematic review reported on mild cognitive impairment. CONCLUSION: Achieving stronger air quality targets has the potential to reduce population-level dementia risk. Neighbourhood (i.e., greenness and chronic noise) and occupational (i.e., shift work) characteristics are associated with dementia and are viable public health intervention points. Additional research should examine the relationship between other environmental risk factors and mild cognitive impairment and specific types of dementia.

---

### PMID 18000416 — current stance: `contradicts`

**Stance justification:** > Statistically significant causes of death were lung cancer (three plants); bladder cancer; chronic obstructive lung disease (two plants each); cancers of the stomach, digestive system unspecified, rectum and rectosigmoid, pancreas, and larynx; Alzheimer's disease (one plant); and cerebrovascular disease (one plant).

**Golden note:** Quebec Al smelter cohort mortality — no excess AD.

**Mortality and cancer experience of Quebec aluminum reduction plant workers. Part 2: mortality of three cohorts hired on or before january 1, 1951.**

*Journal of occupational and environmental medicine*, 2007. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> OBJECTIVE: To describe the mortality of Quebec aluminum smelter workers employed before 1951. METHODS: The mortality of 5,977 men hired at three plants on or before January 1, 1951 was compared with that of Quebec men. Relationships to benzo[a]pyrene, benzene-soluble material, and smoking were examined. RESULTS: Statistically significant causes of death were lung cancer (three plants); bladder cancer; chronic obstructive lung disease (two plants each); cancers of the stomach, digestive system unspecified, rectum and rectosigmoid, pancreas, and larynx; Alzheimer's disease (one plant); and cerebrovascular disease (one plant). Not significant increases were also observed. CONCLUSIONS: Mortality from cancer of the lung and bladder and chronic obstructive pulmonary disease are related to exposure in Söderberg smelters. The cause of increased stomach cancer mortality is unclear. Excess mortality from some other diseases may be explained by factors other than coal tar pitch volatiles exposure.

---

### PMID 12602134 — current stance: `inconclusive`

**Stance justification:** > These epidemiological studies entail certain methodological limitations, and their results are not consistent, so the results available to date therefore not making it possible to clearly determine that any relationship exists between exposure to aluminum and the etiology of Alzheimer's disease.

**Golden note:** Spanish review — drinking water focus, mixed conclusion.

**[Review of studies on exposure to aluminum and Alzheimer's disease].**

*Revista espanola de salud publica*, 2002. Types: Comparative Study; English Abstract; Journal Article; Review

> A review has been made of the epidemiological studies published evaluating the role of aluminum as a risk factor for developing Alzheimer's disease. A search for published studies was conducted in the Medline database by combining the terms "Aluminum" and "Alzheimer's disease". In most of the studies reviewed, exposure to aluminum in drinking water was examined. These studies suggest that a relationship exists between aluminum (Al) and Alzheimer's disease involving relative risks of around 2 for populations exposed to Al concentrations in drinking water higher than 0.1 mg/l. Types of exposure to this metal by other means (food, medications and occupational exposure) have received little attention. These epidemiological studies entail certain methodological limitations, and their results are not consistent, so the results available to date therefore not making it possible to clearly determine that any relationship exists between exposure to aluminum and the etiology of Alzheimer's disease. Nevertheless, the toxic effect of aluminum on human health cannot be ruled out either, and thus exposure to aluminum should be monitored and limited as far as possible.

---

### PMID 37777128 — current stance: `supports`

**Stance justification:** > We found significant worse performances in workers occupationally exposed to aluminum regarding processing speed, working memory, attention, and reaction time after exclusion of outliers.

**Golden note:** Al exposure + cognitive performance meta — occupational Al associated with worse cognition.

**Aluminum exposure and cognitive performance: A meta-analysis.**

*The Science of the total environment*, 2023. Types: Meta-Analysis; Journal Article

> BACKGROUND: Aluminum is increasingly used in various industrial processes due to its beneficial properties. Occupational exposure to aluminum, however, has been linked to several adverse health effects. The impact of occupational aluminum exposure on worker's cognitive performance and its contribution in developing neurodegenerative diseases is highly discussed with competing results. METHOD: We conducted a literature search via online databases until June 2023. Applicable studies fulfilling inclusion criteria investigating the effects of occupational aluminum exposure on cognitive functions were gathered. Results were aggregated using random effects meta-analysis and the effect size g. We further explored types of publication biases, moderating variables and exposure-effect relationships using meta-regressions. RESULTS: The final sample consisted of 18 studies with 87 effect sizes for seven cognitive functions. We found significant worse performances in workers occupationally exposed to aluminum regarding processing speed, working memory, attention, and reaction time after exclusion of outliers. Additionally, we found increased blood plasma aluminum significantly predicting decreased cognitive performance in exposed workers. CONCLUSION: Our results show decreased performance levels in processing speed, working memory, attention and reaction time in workers occupationally exposed to aluminum compared to controls. Furthermore, we found that aluminum in blood plasma was the only biomarker as significant predictor of cognitive performance. We discuss recommendations for further research in relation to occupational health and safety. Finally, we extend the discourse between occupational aluminum exposure and development of neurodegenerative diseases like Alzheimer's disease.

---

### PMID 40749395 — current stance: `supports`

**Stance justification:** > Although few studies confirmed Al-induced brain pathology as a direct cause of dementia, meta-analysis of four eligible studies revealed a strong association between Al exposure and AD (Hedges' g = 2.451), despite high heterogeneity across data sources and outcome measures.

**Golden note:** Environmental Al + AD risk meta — found association.

**Environmental aluminum exposure and Alzheimer's disease risk: Evidence from a systematic review and meta-analysis.**

*Ecotoxicology and environmental safety*, 2025. Types: Journal Article; Systematic Review; Meta-Analysis

> Aluminum (Al) is a widespread environmental contaminant with suspected links to neurodegenerative diseases, particularly Alzheimer's disease (AD). This systematic review and meta-analysis aimed to evaluate the association between environmental Al exposure and the risk of AD by synthesizing evidence from diverse sources and study designs. A systematic review was conducted following Preferred Reporting Items for Systematic Reviews and Meta-Analyses guidelines. Literature searches were performed in PubMed, Scopus, Web of Science, EMBASE, and the gray literature up to June 2024. After duplicate removal and screening of 6504 records, 54 eligible studies on Al exposure and dementia/AD were included. Data extraction focused on exposure media, Al concentrations, Al and AD/dementia correlation, and geographic context. Screening was independently conducted by two reviewers, with good inter-rater reliability (Kappa = 0.75). Meta-analysis was conducted on the studies that reported sufficient quantitative data, using Hedges' g to estimate the effect size of Al exposure on AD. The included studies demonstrated considerable spatial and temporal variation. Of the 54 studies, 26 reported a positive association between Al exposure and AD or dementia, while 24 found no or negative associations. Major exposure sources included contaminated water, soil, diet, occupational settings, and medical interventions. Although few studies confirmed Al-induced brain pathology as a direct cause of dementia, meta-analysis of four eligible studies revealed a strong association between Al exposure and AD (Hedges' g = 2.451), despite high heterogeneity across data sources and outcome measures. Our findings suggest that environmental Al exposure may contribute to the development of AD, though it is likely one of several interacting risk factors. Environmental conditions appear to influence both Al bioaccumulation and its neurotoxic effects related to cognitive decline.

---

