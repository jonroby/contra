# Q19: Does APOE genotype modify response to cholinesterase inhibitors in Alzheimer's disease?

Reviewed against the stricter bar in `.claude/CLAUDE.md` (see `question1.md`).

n=20 PMIDs.

**Current S/C/I**: 9 / 2 / 9
**Proposed S/C/I**: 4 / 9 / 7
**Net flips**: ~9 (the heaviest re-labeling load of any question)

Q19 has the largest correction load in the entire eval set. The
question asks whether APOE genotype **modifies** ChEI response — i.e.,
is there a treatment × genotype interaction? Most current `supports`
labels are anchored on studies that report APOE-stratified subgroup
analyses, but **multiple of those studies explicitly state APOE has no
interaction effect**. Re-reading the abstracts shows the underlying
literature is dominated by null interaction findings.

---

## Proposed flips

| PMID | Year | Current → Proposed | Reason |
|------|------|-------------------|--------|
| `10599773` | 1999 | **supports → contradicts** | Metrifonate + APOE pooled 4 RCTs, n=959. Verbatim: *"The interaction of APOE genotype and the metrifonate effect on cognitive performance were **not significant** (p = 0.25)."* Conclusion: *"the findings... do not clearly support an interaction between APOE genotype and metrifonate treatment effects."* Well-powered null on the interaction question. Current `supports` is wrong. |
| `22986607` | 2013 | **supports → contradicts** | CYP2D6 + APOE on donepezil n=110. Verbatim: *"the frequency of APOE ε4 carriers and noncarriers showed **no difference** between the [responder/non-responder] groups (P > 0.05)... We did not find the relationship between APOE ε4 status and the efficacy of donepezil in our study."* APOE specifically null. CYP2D6 was the relevant modifier, not APOE. The current `supports` label captures CYP2D6 finding but the question is about APOE. |
| `17132969` | 2006 | **supports → contradicts** | Rivastigmine + APOE prospective n=multicenter. Verbatim: *"the presence of at least one APOE epsilon4 allele **does not determine a difference** in the response to treatment with rivastigmine."* The note ("modifier effect") is wrong — the study explicitly says no difference. |
| `9777427` | 1998 | **supports → inconclusive** | Gender + APOE response n=107. Verbatim: *"While ApoE genotype **did not modify response to therapy in the short term**, there are indications that it may affect response over the longer term."* Hedged — short-term null, long-term speculative. Per strict bar, mixed/genuinely-uncertain → `inconclusive`. |
| `15289797` | 2004 | **supports → inconclusive** | Differential rivastigmine response in ε4 carriers vs non-carriers n=367. Verbatim: *"Both genotype-defined subgroups **showed quantitatively similar responses to therapy** (both P<0.05 vs placebo)."* I.e., both groups responded — which means APOE did *not* modify response. The label `supports` is based on the title's word "differential," but the actual finding is that the response magnitudes were similar. → `inconclusive` (or `contradicts`). |
| `26402762` | 2015 | **inconclusive → contradicts** | APOE-ε4 + donepezil pooled 3 RCTs. Verbatim: *"**No appreciable interaction** between donepezil response and APOE-ε4 carrier status or copy number was detected."* Well-powered (3 trials pooled) null on interaction. Per strict bar, this is `contradicts` for the modification question. |
| `27282366` | 2016 | **inconclusive → contradicts** | CYP2D6/APOE + donepezil meta n=1266. Verbatim: *"**No independent effect of APOE polymorphism** on donepezil clinical responses was found (OR 1.08, 95% CI 0.85-1.38; p = 0.53)."* APOE specifically null in pooled meta. |
| `16254428` | 2005 | **inconclusive → contradicts** | Korean galantamine + ε4 RCT n=202. Verbatim: *"**ApoE epsilon4 genotype does not affect galantamine-related improvements** in cognition, global rating, function and behavior."* Well-designed RCT explicitly null on interaction. |
| `27716659` | 2017 | **inconclusive → contradicts** | Donepezil + APOE/CYP2D6 naturalistic n=42. Verbatim: *"the good response pattern was influenced by the concentration of donepezil, **but not by APOE and CYP2D6 polymorphisms**."* APOE null. |
| `15636076` | 2004 | **inconclusive → supports** | Galanthamine + APOE retrospective n=84. Verbatim: *"The significant number of responders was observed among **apoE4 homozygous patients (71%; chi2 = 6.89; p = 0.032)**."* Statistically significant differential response. The current `inconclusive` is too cautious — there's a sig finding here. |

## Confirmed (no change)

- `8618881` (Poirier 1995 — ε4 predicts poor ChEI outcome on tacrine) — **supports ✓** (foundational study; >80% non-ε4 improved vs 60% of ε4 carriers worsened)
- `11173877` (APOE: NO influence on galantamine, n=1528) — **contradicts ✓** (well-powered null)
- `18401173` (donepezil + APOE n=51) — **inconclusive ✓** (small, ε4 carriers slightly more responsive p=0.03 — borderline)
- `18334913` (APOE ε4 + BCHE-K synergistic on placebo MCI→AD progression) — **supports ✓** (defensible — about treatment response in InDDEx rivastigmine trial)
- `27567841` (BCHE-K + APOE-ε4 modulate donepezil response in aMCI) — **supports ✓** (sig benefit at 3-yr follow-up in genotype carriers)
- `22012848` (APOE ε4 modulates BChE CSF — biomarker only) — **inconclusive ✓**
- `12566177` (CMRglc/CSF biomarkers — biomarker focus) — **inconclusive ✓**
- `23051684` (rivastigmine ± memantine + APOE n=146) — **supports ✓** (defensible — moderately severe ε4 carriers showed higher responder rates with combo)
- `30041236` (AChEI + APOE-ε4 meta — null pooled) — **contradicts ✓**
- `24479631` (BCHE + ApoE on cortical thickness — descriptive) — **inconclusive ✓**

## Cross-cutting issues

- **Systematic mislabeling pattern**: ~9 of 20 papers in this question
  appear to be labeled based on whether the *paper title* suggests a
  modifier effect (e.g., "Differential rivastigmine response in
  APOE..." → `supports`) rather than whether the *abstract conclusion*
  reports a significant interaction. After re-reading abstracts, the
  bulk finding in this literature is **null**.
- **The expected_consensus is "contested"** — and indeed it is, but
  in a different way than the current labels suggest. The contested
  ness is not "some studies positive, some negative" but rather
  "early small studies suggested an effect, larger replications
  showed null." The proposed re-labeling makes this pattern visible.
- After flips: 4/9/7 — strongly leans negative on the modification
  question, with `contradicts` count rising from 2 to 9. This better
  reflects the actual primary literature.

## Highest-confidence flips for this question

- `10599773`, `22986607`, `17132969` supports → contradicts —
  all three abstracts explicitly state APOE does NOT modify ChEI
  response, but were labeled `supports`. Direct mislabels.
- `26402762`, `27282366`, `16254428`, `27716659` inconclusive → contradicts
  — all four abstracts explicitly use "no significant interaction"
  or "does not affect" language for APOE × ChEI; should be `contradicts`
  under the strict bar.


---

## Abstracts (n=20)

Stance labels reflect the **proposed** stance after this review, annotated with `[FLIP from <prev>]` where changed.

### PMID 8618881 — current stance: `supports`

**Golden note:** Poirier 1995 — ε4 predicts cholinergic deficits and lower ChEI treatment outcome.

**Apolipoprotein E4 allele as a predictor of cholinergic deficits and treatment outcome in Alzheimer disease.**

*Proceedings of the National Academy of Sciences of the United States of America*, 1995. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> Apolipoprotein E (apoE) is critical in the modulation of cholesterol and phospholipid transport between cells of different types. Human apoE is a polymorphic protein with three common alleles, APO epsilon 2, APO epsilon 3, and APO epsilon 4. ApoE4 is associated with sporadic and late-onset familial Alzheimer disease (AD). Gene dose was shown to have an effect on risk of developing AD, age of onset, accumulation of senile plaques in the brain, and reduction of choline acetyltransferase (ChAT) activity in the hippocampus of AD subjects. To characterize the possible impact of the apoE4 allele on cholinergic markers in AD, we examined the effect of apoE4 allele copy number on pre- and postsynaptic markers of cholinergic activity. ApoE4 allele copy number showed an inverse relationship with residual brain ChAT activity and nicotinic receptor binding sites in both the hippocampal formation and the temporal cortex of AD subjects. AD cases lacking the apoE4 allele showed ChAT activities close or within age-matched normal control values. The effect of the apoE4 allele on cholinomimetic drug responsiveness was assessed next in a group (n = 40) of AD patients who completed a double-blind, 30-week clinical trial of the cholinesterase inhibitor tacrine. Results showed that > 80% of apoE4-negative AD patients showed marked improvement after 30 weeks as measured by the AD assessment scale (ADAS), whereas 60% of apoE4 carriers had ADAS scores that were worse compared to baseline. These results strongly support the concept that apoE4 plays a crucial role in the cholinergic dysfunction associated with AD and may be a prognostic indicator of poor response to therapy with acetylcholinesterase inhibitors in AD patients.

---

### PMID 9777427 — current stance: `supports`

**Golden note:** Gender + APOE genotype as predictors of anticholinesterase response — ε4 modifies outcome.

**Effect of gender and apolipoprotein E genotype on response to anticholinesterase therapy in Alzheimer's disease.**

*International journal of geriatric psychiatry*, 1998. Types: Clinical Trial; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND: Anticholinesterase therapies offer modest benefit to subgroups of AD sufferers. However, there has previously been no way of predicting which patients will respond to any of the drugs. OBJECTIVE: To discover if gender and/or apolipoprotein E genotype can be used as predictors of response in the clinical setting. DESIGN: 107 patients from the Bristol Memory Disorders Clinic took part in a double-blinded or open label trial of tacrine therapy for between 3 and 12 months or an open label trial of galanthamine therapy for 3 months. RESULTS: After 3 months of therapy, gender was found to be the only significant influence on the number of responders to anticholinesterase therapy. Men had a 73% greater chance of responding than women (p = 0.012). While ApoE genotype did not modify response to therapy in the short term, there are indications that it may affect response over the longer term (up to 12 months), and also that the initial advantage of male gender may not be maintained after 3 months. CONCLUSION: Gender is likely to be a more powerful determinant of outcome of anticholinesterase treatment than apolipoprotein E status in the short term.

---

### PMID 11173877 — current stance: `contradicts`

**Golden note:** APOE genotype: NO influence on galantamine efficacy. Clear negative.

**APOE genotype: no influence on galantamine treatment efficacy nor on rate of decline in Alzheimer's disease.**

*Dementia and geriatric cognitive disorders*, 2001. Types: Journal Article; Multicenter Study

> Apolipoprotein E (APOE) has been extensively demonstrated to be a genetic risk factor for Alzheimer's disease (AD). Associations of APOE genotype have been reported with age at AD onset, rate of decline, and responsiveness to therapy. This study aimed to test these hypotheses in a large study population of AD patients. APOE genotype was determined from 1,528 Caucasian subjects, diagnosed by NINCDS/ADRDA criteria as probable AD patients, enrolled in four international placebo-controlled clinical trials of 3--12 months duration, designed to evaluate efficacy of treatment with galantamine or sabeluzole. In addition to patient demographics and baseline scores for Mini Mental State Examination, scores on the Disability Assessment for Dementia (DAD) and the cognitive subscale of the Alzheimer's Disease Assessment Scale (ADAS-cog) were recorded at the start, during, and at the end of the study. APOE epsilon 4 homozygotes had a significantly lower age at disease onset compared to patients with other APOE genotypes. The epsilon 4 allele was significantly over-represented in females compared to males, and in the group of subjects with an AD family history. Based on longitudinal data of 504 placebo-treated AD patients, the linear annual rate of change in score was 5 points on the ADAS-cog scale and 11 on the DAD scale. The epsilon 4 allele copy number did not influence these rates of decline. Sabeluzole treatment was not effective in the overall group compared to the placebo-treated group, nor in any subgroup stratified by epsilon 4 allele count. Galantamine produced cognitive and functional improvement that were not affected by epsilon 4 allele count. In conclusion, our data confirm a strong association between epsilon 4 homozygotes and age at onset of AD but do not support an effect of epsilon 4 allele copy number on rate of cognitive and functional decline nor on the efficacy of galantamine in patients with AD.

---

### PMID 18401173 — current stance: `inconclusive`

**Golden note:** Donepezil + ApoE — described as 'matter of controversy', mixed results.

**Effect of ApoE genotype on response to donepezil in patients with Alzheimer's disease.**

*Dementia and geriatric cognitive disorders*, 2008. Types: Clinical Trial; Journal Article; Research Support, Non-U.S. Gov't

> BACKGROUND/AIMS: The possible influence of apolipoprotein E (ApoE) genotype on the response to acetylcholinesterase inhibitor therapy in patients with Alzheimer's disease (AD) remains a matter of controversy. In order to address this issue, we investigated the effects of ApoE genotype on the clinical response to donepezil in patients with mild to moderate AD. METHODS: An open study was carried out in 51 patients with probable AD who were treated with 5-10 mg of donepezil per day for 48 weeks. RESULTS: Eighteen (35.3%) of the 51 patients had 1 or 2 ApoE epsilon4 alleles. ApoE epsilon4 carriers with AD showed a mean 1.1-point increase from the baseline score of 23.9 on the 70-point Alzheimer's Disease Assessment Scale-Cognitive Component at 48 weeks, while the ApoE epsilon4 noncarrier group showed a 3.1-point increase from the baseline score of 22.5 (p = 0.03). The ApoE epsilon4 carrier group exhibited a mean 0.13-point worsening from the baseline score of 0.97 on the Korean Instrumental Activities of Daily Living at 48 weeks, while the ApoE epsilon4 noncarrier group exhibited a 0.17-point worsening from the baseline score of 0.64 (p = 0.05). CONCLUSION: AD patients who carry the ApoE epsilon4 allele may respond more favorably to donepezil than epsilon4 noncarriers.

---

### PMID 18334913 — current stance: `supports`

**Golden note:** Synergistic APOE ε4 + BCHE-K predicts MCI→AD progression on rivastigmine.

**Synergistic effect of apolipoprotein E epsilon4 and butyrylcholinesterase K-variant on progression from mild cognitive impairment to Alzheimer's disease.**

*Pharmacogenetics and genomics*, 2008. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> OBJECTIVE: To evaluate the synergistic effects of the apolipoprotein E (APOE) epsilon4 and butyrylcholinesterase K-variant (BCHE-K) alleles on progression to Alzheimer's disease (AD) in individuals with mild cognitive impairment (MCI). METHODS: This was a post-hoc exploratory analysis from a 3-4-year, randomized, placebo-controlled study of rivastigmine in participants with MCI (InDDEx study). Participants who consented to genetic testing were included in the current analyses. The incidence of progression to AD, cognitive decline and changes in MRI brain volumes were investigated in participants from the placebo arm of the InDDEx study. RESULTS: Of the 1018 participants in the overall study, 464 were successfully genotyped for both APOE and butyrylcholinesterase. Of these, 68 (14.7%) carried > or =1 APOE epsilon4 and > or =1 BCHE-K allele. The presence of APOE epsilon4 was associated with a significantly higher incidence of progression to AD whereas the presence of BCHE-K had no independent effect on progression. A synergistic effect of the combined presence of APOE epsilon4 and BCHE-K on the time to clinical diagnosis of AD and on MRI brain volumes was seen. Progression to AD and hippocampal volumetric loss was greatest in participants who carried both APOE epsilon4 and BCHE-K alleles and lowest in BCHE-K carriers without the APOE epsilon4 allele. CONCLUSION: In MCI, the risk of cognitive decline, hippocampal volumetric loss and progression to AD seems to be the greatest in individuals who carry at least one copy of both the BCHE-K and APOE epsilon4 alleles.

---

### PMID 10599773 — current stance: `supports`

**Golden note:** Metrifonate + APOE genotype interaction detected.

**Metrifonate treatment of AD: influence of APOE genotype.**

*Neurology*, 1999. Types: Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial

> OBJECTIVE: To investigate whether an interaction exists between APOE genotype and the response of AD patients to metrifonate treatment and whether APOE genotype independently affects the rate of AD progression. BACKGROUND: Metrifonate is a new acetylcholinesterase inhibitor for the treatment of AD symptoms. METHODS: Data were pooled from four prospective, randomized, double-blind, placebo-controlled clinical trials and analyzed retrospectively. A total of 959 patients who received once-daily placebo (n = 374) or metrifonate (30 to 60 mg based on weight or a 50-mg fixed dose, n = 585) for up to 26 weeks agreed to APOE genotyping. RESULTS: Metrifonate clearly improved the cognitive performance of the AD patients when compared with placebo (Alzheimer's Disease Assessment Scale-Cognitive Subscale [ADAS-Cog], p = 0.0001). The interaction of APOE genotype and the metrifonate effect on cognitive performance were not significant (p = 0.25). Metrifonate also clearly improved the global function of the AD patients when compared with placebo (Clinician's Interview-Based Impression of Change with Caregiver Input [CIBIC-Plus], p = 0.0001). The interaction of APOE genotype with the metrifonate effect on global function also was not significant (p = 0.70). No significant three-way interactions were observed among APOE genotype, gender, and response to metrifonate treatment (ADAS-Cog, p = 0.68; CIBIC-Plus, p = 0.26). APOE genotype did not influence disease progression as evaluated by either cognitive performance (ADAS-Cog, p = 0.93) or global function (CIBIC-Plus, p = 0.64). CONCLUSIONS: The findings from these studies of up to 26 weeks' duration do not clearly support an interaction between APOE genotype and metrifonate treatment effects. They suggest that APOE genotypes do not necessarily predict an AD patient's response to metrifonate treatment and that APOE genotype may not influence the rate of disease progression for patients with mild to moderate AD.

---

### PMID 22986607 — current stance: `supports`

**Golden note:** CYP2D6*10 + APOE polymorphisms affect donepezil efficacy.

**Effect of CYP2D6*10 and APOE polymorphisms on the efficacy of donepezil in patients with Alzheimer's disease.**

*The American journal of the medical sciences*, 2013. Types: Clinical Trial; Journal Article

> BACKGROUND: The aim of this study was to evaluate the effect of CYP2D6*10 and APOE polymorphisms on both steady-state plasma concentrations (Cp) and clinical response of donepezil in patients with mild-to-moderate Alzheimer's disease (AD). METHODS: A total of 110 Chinese AD patients participated in this study. Patients were treated with 5 to 10 mg of donepezil daily for 6 months. The genotypes of CYP2D6*10 and APOE were analyzed by polymerase chain reaction-restriction fragment length polymorphism. The steady-state Cp of donepezil was measured by high-performance liquid chromatography-tandem mass spectrometric assay method. The cognition of patients was evaluated at baseline and at 6-month follow-up by Mini-Mental Status Examination and Alzheimer Disease Assessment Scale-Cognitive subscale. RESULTS: At 6-month follow-up, 56 of 96 patients (58.3%) were evaluated as responders and 40 patients (41.7%) as nonresponders to donepezil treatment. A significantly higher frequency of patients with genotypes CYP2D6*1/*10 and *10/*10 were found in responders than in nonresponders (P < 0.05). Besides, patients with CYP2D6*1/*10 and *10/*10 genotypes had higher Cp of donepezil and improved cognition scores than those with CYP2D6*1/*1 genotype (P < 0.05). However, the frequency of APOE [Latin Small Letter Open E]4 carriers and noncarriers showed no difference between the 2 groups (P > 0.05). CONCLUSIONS: AD patients with mutant allele (*10) in CYP2D6 gene may respond better to donepezil than those with wild allele (*1). We did not find the relationship between APOE [Latin Small Letter Open E]4 status and the efficacy of donepezil in our study.

---

### PMID 15289797 — current stance: `supports`

**Golden note:** Differential rivastigmine response in ε4 carriers vs non-carriers.

**Differential qualitative responses to rivastigmine in APOE epsilon 4 carriers and noncarriers.**

*The pharmacogenomics journal*, 2004. Types: Comparative Study; Journal Article; Research Support, Non-U.S. Gov't

> This retrospective analysis of two double-blind, placebo-controlled studies in patients with mild to moderately severe AD investigated the efficacy of rivastigmine 6-12 mg/day on cognitive outcomes in patients with or without the apolipoprotein (APOE) epsilon4 allele. APOE data were collected from patients who consented to pharmacogenetic testing. Treatment differences within each subgroup were compared, using the Observed Case (OC) population. The APOE epsilon4 and non-APOE epsilon4 subgroups comprised 246 and 121 patients, respectively. Overall, APOE epsilon4 noncarriers showed greater decline than carriers (P<0.05). However, at 26 weeks, placebo-treated APOE epsilon4 patients declined 3.04 points below baseline on the cognitive subscale of the Alzheimer's Disease Assessment Scale (ADAS-cog), and rivastigmine-treated patients improved by 1.67 points. Non-APOE epsilon4 placebo-treated patients declined by 4.59 points and rivastigmine-treated patients declined by 0.48 points. Thus, non-APOE epsilon4 carriers showed a less favorable course under either placebo or rivastigmine, but both genotype-defined subgroups showed quantitatively similar responses to therapy (both P<0.05 vs placebo).

---

### PMID 27567841 — current stance: `supports`

**Golden note:** BCHE-K + APOE-ε4 modulate donepezil response in aMCI.

**Butyrylcholinesterase K and Apolipoprotein E-ɛ4 Reduce the Age of Onset of Alzheimer's Disease, Accelerate Cognitive Decline, and Modulate Donepezil Response in Mild Cognitively Impaired Subjects.**

*Journal of Alzheimer's disease : JAD*, 2016. Types: Journal Article; Randomized Controlled Trial

> BACKGROUND: Genetic heterogeneity in amnestic mild cognitively impaired (aMCI) subjects could lead to variations in progression rates and response to cholinomimetic agents. Together with the apolipoprotein E4 (APOE-ɛ4) gene, butyrylcholinesterase (BCHE) has become recently one of the few Alzheimer's disease (AD) susceptibility genes with distinct pharmacogenomic properties. OBJECTIVE: To validate candidate genes (APOE/BCHE) which display associations with age of onset of AD and donepezil efficacy in aMCI subjects. METHODS: Using the Petersen et al. (2005) study on vitamin E and donepezil efficacy in aMCI, we contrasted the effects of BCHE and APOE variants on donepezil drug response using the Alzheimer's Disease Assessment Score-Cognition (ADAS-Cog) scale. Independently, we assessed the effects of APOE/BCHE genotypes on age of onset and cortical choline acetyltransferase activity in autopsy-confirmed AD and age-matched control subjects. RESULTS: Statistical analyses revealed a significant earlier age of onset in AD for APOE-ɛ4, BCHE-K*, and APOE-ɛ4/BCHE-K* carriers. Among the carriers of APOE-ɛ4 and BCHE-K*, the benefit of donepezil was evident at the end of the three-year follow-up. The responder's pharmacogenomic profile is consistent with reduced brain cholinergic activity measured in APOE-ɛ4 and BCHE-K* positive subjects. CONCLUSIONS: APOE-ɛ4 and BCHE-K* positive subjects display an earlier age of onset of AD, an accelerated cognitive decline and a greater cognitive benefits to donepezil therapy. These results clearly emphasize the necessity of monitoring potential pharmacogenomic effects in this population of subjects, and suggest enrichment strategies for secondary prevention trials involving prodromal AD subjects.

---

### PMID 22012848 — current stance: `inconclusive`

**Golden note:** APOE ε4 modulates BChE CSF phenotype — biomarker, not direct treatment outcome.

**Apolipoprotein ε4 modulates phenotype of butyrylcholinesterase in CSF of patients with Alzheimer's disease.**

*Journal of Alzheimer's disease : JAD*, 2012. Types: Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't

> Butyrylcholinesterase K (BCHE-K) is associated with increased risk of developing Alzheimer's disease (AD) in apolipoprotein ε (APOE4) carriers, while among APOE4 non-carriers BCHE-K appears to be protective. Nonetheless, pure pharmacogenetic reports have provided conflicting results. To provide insights about these controversies, we combined BCHE-K pharmacogenetic observations in AD patients (n = 179) with proteomic and enzymatic analysis of plasma, cerebrospinal fluid (CSF), or both samples. We found that BCHE-K genotype was overrepresented among the AD patients (χ(2) = 14.21, p < 0.0001). Plasma BuChE activity was gene dose-dependently 20-50% less among K-carriers (p < 0.001). CSF BuChE activity did not show such robust K-gene dosage-dependency, because K homozygotes (n = 9) had 30-40% less activity compared to both non-carriers (n = 78, p < 0.01) and heterozygotes (n = 42, p < 0.09). CSF ApoE protein expression was also altered by presence of K-allele (p < 0.001, n = 129). Mutually, APOE4 altered phenotypic display of BuChE variants in CSF (p < 0.01, n = 129). In absence of APOE4, CSF BuChE activity was essentially indistinguishable among K-carriers (n = 16) and non-carriers (n = 17, p < 0.8) although the K-carriers had 24-39% less circulating BuChE protein. In contrast in presence of APOE4, the K-carriers (n = 35) had K allele dose-dependently a BuChE phenotype with 14-46% reduced activity compared to K non-carriers (p < 0.001, n = 59), despite an essentially identical BChE concentration in CSF (1 ± 4%, p < 0.8). Pattern of the patients' cognitive performance in MMSE closely resembled the APOE4-derived phenotypic display of BuChE variants. APOE4-dependent outcome of BCHE-K genotype as AD risk factor arises through a differential phenotypic modulation of BuChE. Future pharmacogenetic studies should include assessment of the subjects' true phenotypic display of BuChE.

---

### PMID 12566177 — current stance: `inconclusive`

**Golden note:** CMRglc/CSF biomarkers + APOE in long-term ChEI — biomarker focus.

**Cerebral glucose metabolism, cerebrospinal fluid-beta-amyloid1-42 (CSF-Abeta42), tau and apolipoprotein E genotype in long-term rivastigmine and tacrine treated Alzheimer disease (AD) patients.**

*Neuroscience letters*, 2003. Types: Clinical Trial; Journal Article; Research Support, Non-U.S. Gov't

> We evaluated cerebral glucose metabolism (CMRglc) and cerebrospinal fluid (CSF) levels of tau and beta-amyloid(1-42) (Abeta42), in relation to apolipoprotein E (ApoE) genotype, in patients with mild Alzheimer disease (AD) treated with rivastigmine (n=11) and tacrine (n=16) for 1 year; and two untreated AD groups. The rivastigmine-treated AD patients showed a significant increase in CMRglc as compared to both tacrine-treated and untreated AD subjects. The rivastigmine-treated AD group showed no change in CSF-tau levels after 1 year, while in contrast a significant increase as seen in tacrine-treated and untreated AD patients. The CSF-tau changes were mainly seen in ApoE epsilon4 carriers. There was no significant change in Abeta42 after 1-year treatment with either rivastigmine or tacrine. This study shows that the two long-term cholinesterase inhibitor treatments exert different effects on biological markers for AD.

---

### PMID 26402762 — current stance: `inconclusive`

**Golden note:** APOE-ε4 + donepezil response — 'inconsistent results across studies'.

**APOE-ɛ4 Carrier Status and Donepezil Response in Patients with Alzheimer's Disease.**

*Journal of Alzheimer's disease : JAD*, 2015. Types: Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND: Previous studies have investigated associations between apolipoprotein E (APOE)-ɛ4 allele status and acetylcholinesterase inhibitor treatment response in patients with Alzheimer's disease. The ability to draw definitive conclusions regarding the effect of APOE-ɛ4 genotype on treatment response has been hindered by inconsistent results among studies and methodological limitations that restrict interpretation of study findings. OBJECTIVE: To determine whether APOE-ɛ4 carrier status influences the magnitude of change in 13-item Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-cog) score associated with acetylcholinesterase inhibitor treatment (i.e., donepezil). METHODS: Analyses were performed using pooled data from the donepezil and placebo treatment arms of three consecutive, similarly designed, 12-week, multi-national, randomized clinical studies that enrolled patients with mild-to-moderate Alzheimer's disease. Correlations between APOE-ɛ4 carrier status and ADAS-cog scores were evaluated using analysis of covariance. RESULTS: No appreciable interaction between donepezil response and APOE-ɛ4 carrier status or copy number was detected. Both carriers and non-carriers of APOE-ɛ4 who received donepezil experienced significant improvements from baseline in ADAS-cog score versus placebo (p <  0.05). Change from baseline to final observation in the donepezil treatment group was - 2.95 for APOE-ɛ4 carriers and - 4.09 for non-carriers (p = 0.23). In contrast, non-carriers of APOE-ɛ4 in the placebo treatment group exhibited a greater improvement from baseline versus carriers (-2.38 versus - 0.60, p = 0.05). CONCLUSION: Within this population, APOE genotype had no statistically significant effect on cognitive response to donepezil treatment; however, APOE-ɛ4 allele status was associated with a difference in the magnitude of the change in ADAS-cog of placebo-treated patients.

---

### PMID 27282366 — current stance: `inconclusive`

**Golden note:** CYP2D6/APOE + donepezil systematic review — controversy persists.

**Effect of the CYP2D6 and APOE Polymorphisms on the Efficacy of Donepezil in Patients with Alzheimer's Disease: A Systematic Review and Meta-Analysis.**

*CNS drugs*, 2016. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: Differential responses to donepezil treatment in patients with Alzheimer's disease (AD) have been observed in clinical practice. It remains controversial whether, and to what extent, individual variation in the genes responsible for drug metabolism (CYP2D6) or those associated with AD pathogenesis (APOE) modulate the response to donepezil treatment. OBJECTIVE: The aim of this study was to better understand the potential link between donepezil treatment response and CYP2D6 or APOE polymorphisms. METHODS: We performed a meta-analysis based on data collected from 1266 donepezil-treated AD patients, and evaluated the association of CYP2D6 or APOE polymorphisms with treatment effectiveness. RESULTS: No significant difference was observed in the responder rate of donepezil treatment between the normal function CYP2D6 alleles group and the decreased/non-functional group [odds ratio (OR) 1.34, 95 % confidence interval (CI) 0.5-3.58; p = 0.56]. However, compared with the increased function CYP2D6 alleles group, the normal function group had a better response to donepezil treatment (OR 1.52, 95 % CI 1.14-2.03; p = 0.005). For the specific CYP2D6 single nucleotide polymorphism rs1080985, patients who carried the G allele had a significantly higher risk of poor response to donepezil treatment. After adjusting the data based on APOE genotype, it was observed that only individuals bearing both the APOE-ε4 allele and the rs1080985-G allele showed a significant increase in the frequency of treatment non-response (OR 1.73, 95 % CI 1.07-2.09; p = 0.03). No independent effect of APOE polymorphism on donepezil clinical responses was found (OR 1.08, 95 % CI 0.85-1.38; p = 0.53). Lastly, in a subgroup analysis based on ethnicity, all results remained consistent. CONCLUSION: The CYP2D6 genotype may be potentially effective for predicting the response to donepezil treatment in AD patients.

---

### PMID 17132969 — current stance: `supports`

**Golden note:** Rivastigmine efficacy related to ε4 — modifier effect.

**Relationship between the efficacy of rivastigmine and apolipoprotein E (epsilon4) in patients with mild to moderately severe Alzheimer disease.**

*Alzheimer disease and associated disorders*, 2006. Types: Clinical Trial; Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't

> Alzheimer disease is the most common form of dementia in Western countries and the leading cause of disability in the over-65 population. Apolipoprotein E (APOE) is a multifunctional protein implied in lipid metabolism and neurobiology. Polymorphisms of the APOE gene have been associated with a variety of medical disorders, from arteriosclerosis to AD. A high frequency of the APOE epsilon4 allele has been found in patients with AD and they seem to have a higher risk of developing the disease. Various authors have suggested a possible relationship between the efficacy of cholinesterase inhibitors and the presence of the APOE epsilon4 allele. The purpose of the present study was to compare prospectively the efficacy of rivastigmine in patients with mild to moderately severe AD presenting different polymorphisms of the APOE gene on chromosome 19 and to determine if there was a difference in the response to rivastigmine treatment in AD patients with the APOE epsilon4 allele (heterozygous or homozygous) versus patients who had other forms of APOE, such as epsilon2 and epsilon3. This was an open-label, nonrandomized, multicenter study in patients over 50 years of age diagnosed with mild to moderately severe AD. The results of the analysis of this study indicate that the presence of at least one APOE epsilon4 allele does not determine a difference in the response to treatment with rivastigmine. The data indicate that knowledge of the patient's genotype is not necessary for treatment with rivastigmine. It would be interesting in the future to analyze the interaction between these 2 factors using other available anticholinesterase drugs.

---

### PMID 15636076 — current stance: `inconclusive`

**Golden note:** Galanthamine retrospective + APOE — no clear effect.

**ApoE genotyping and response to galanthamine in Alzheimer's disease--a real life retrospective study.**

*Collegium antropologicum*, 2004. Types: Clinical Trial; Journal Article

> This study was undertaken to evaluate the effect of galanthamine, a new cholinesterase inhibitor on cognitive performances in 84 patients with various apoE genotype and Alzheimer's disease (AD) during the six-month treatment. The diagnosis of AD was made on the basis of NINCDS/ADRDN criteria. ApoE4 genotype was determined by PCR procedure. The cognitive performance was assessed MMSE at baseline and six months later. The difference among the groups was statistically analyzed by ANOVA model and Pearson's chi2-test. The MMSE at baseline in all completes was 18.0 +/- 3.73, whereas the mean value of MMSE after 6 months was 16.4 +/- 5.61 indicating significant deterioration (p < 0.01). Of the 84 patients, 14 (169%) were apoE4 homozygous, 41 (49%) were heterozygous, whereas 29 (35%) were apoE4 negative. The significant number of responders was observed among apoE4 homozygous patients (71%; chi2 = 6.89; p = 0.032). The subgroup of apoE4 homozygous patients with AD in its mild to moderate stage may be considered as responders to galanthamine.

---

### PMID 16254428 — current stance: `inconclusive`

**Golden note:** Korean galantamine RCT + ε4 — small, mixed.

**Effect of the apolipoprotein E epsilon4 allele on the efficacy and tolerability of galantamine in the treatment of Alzheimer's disease.**

*Dementia and geriatric cognitive disorders*, 2005. Types: Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> OBJECTIVE: To investigate the effect of the apolipoprotein E (ApoE) epsilon4 allele on the efficacy and tolerability of galantamine treatment. METHODS: A total of 202 patients with mild to moderate Alzheimer's disease participated in a 16-week, prospective, multi-center, randomized, double-blind galantamine trial in a Korean population. Patients were assessed at baseline and after 4, 8 and 16 weeks of randomized treatment using the 11-item cognitive subscale of the Alzheimer's Disease Assessment Scale (ADAS-cog/11), the Clinician's Interview-Based Impression of Change plus Caregiver Input (CIBIC-plus), the Disability Assessment for Dementia Scale (DAD), the Behavioural Pathology in Alzheimer's Disease Rating Scale (BEHAVE-AD) and adverse events. ApoE genotypes were determined for all subjects. RESULTS: Of the 202 subjects, 115 carried at least one ApoE epsilon4 allele and 87 did not. In both ApoE epsilon4 carriers and ApoE epsilon4 noncarriers, significant improvements were detected relative to baseline on ADAS-cog/11, CIBIC-plus, DAD and BEHAVE-AD. ApoE epsilon4 noncarriers showed better improvement in mean total BEHAVE-AD score and mean psychosis (delusions and hallucinations) subscale score than ApoE epsilon4 carriers. The incidence of weight loss was significantly higher in ApoE epsilon4 carriers (n = 11; 9.6%) than in ApoE epsilon4 noncarriers (n = 1; 1.2%) during this 16-week study, even though 92% of patients who complained of weight loss completed this 16-week trial successfully. CONCLUSION: ApoE epsilon4 genotype does not affect galantamine-related improvements in cognition, global rating, function and behavior. Longer prospective studies with larger patient populations are required to confirm these new findings.

---

### PMID 27716659 — current stance: `inconclusive`

**Golden note:** Donepezil + APOE/CYP2D6 naturalistic — mixed.

**Clinical Response to Donepezil in Mild and Moderate Dementia: Relationship to Drug Plasma Concentration and CYP2D6 and APOE Genetic Polymorphisms.**

*Journal of Alzheimer's disease : JAD*, 2017. Types: Journal Article; Observational Study

> The clinical response to donepezil in patients with mild and moderate dementia was investigated in relation to the drug plasma concentration and APOE and CYP2D6 polymorphisms. In a prospective naturalistic observational study, 42 patients with Alzheimer's disease (AD) and AD with cerebrovascular disease who took donepezil (10 mg) for 12 months were evaluated. Their DNA was genotyped, and the donepezil plasma concentrations were measured after 3, 6, and 12 months. Good responders scored ≥-1 on the Mini-Mental State Examination at 12 months in comparison to the baseline score. The study results indicated the good response pattern was influenced by the concentration of donepezil, but not by APOE and CYP2D6 polymorphisms.

---

### PMID 23051684 — current stance: `supports`

**Golden note:** Rivastigmine ± memantine response affected by APOE genotype.

**Response to rivastigmine transdermal patch or memantine plus rivastigmine patch is affected by apolipoprotein E genotype in Alzheimer patients.**

*Dementia and geriatric cognitive disorders*, 2012. Types: Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> BACKGROUND/AIMS: The apolipoprotein E (APOE) genotype in response to pharmacological treatments in patients with Alzheimer's disease (AD) remains a matter of controversy. This analysis investigated the effect of the APOE genotype on the clinical response to rivastigmine transdermal patch monotherapy or memantine plus rivastigmine patch in patients with mild to moderate AD. METHODS: Two hundred and six (n = 206) patients with probable AD and Mini-Mental State Examination (MMSE) scores of 10-20 were randomized to rivastigmine patch monotherapy or memantine plus rivastigmine patch for 24 weeks. Of the 206 patients with probable AD, 146 patients who consented to genetic testing for APOE were included and assessed for this subgroup study. RESULTS: There were no significant differences on MMSE, NPI, ADAS-cog, ADCS-ADL, CDR-SB, NPI and FAB between rivastigmine patch monotherapy and memantine plus rivastigmine patch according to the APOE genotype. However, patients with moderately severe AD (MMSE ≤15) who were APOE ε4 carriers showed higher responder rates on ADCS-ADL with memantine plus rivastigmine patch compared to rivastigmine patch monotherapy. CONCLUSION: Moderately severe AD patients with the APOE ε4 allele may respond more favorably to memantine plus rivastigmine patch than ε4 noncarriers.

---

### PMID 30041236 — current stance: `contradicts`

**Golden note:** AChEI cognitive response + APOE-ε4 meta — limited differential effect.

**Effect of Apolipoprotein E ɛ4 Carrier Status on Cognitive Response to Acetylcholinesterase Inhibitors in Patients with Alzheimer's Disease: A Systematic Review and Meta-Analysis.**

*Dementia and geriatric cognitive disorders*, 2018. Types: Journal Article; Meta-Analysis; Systematic Review

> BACKGROUND: The apolipoprotein E ɛ4 (APOE ɛ4) genotype is the major genetic risk factor for Alzheimer's disease (AD). However, its effect on an individual's response to treatment is less well understood. Many studies have reported that the presence or absence of APOE ɛ4 may have influence on the therapeutic response for acetylcholinesterase inhibitors (AChEIs), but the results were inconsistent. This study performed a systematic review and meta-analysis to evaluate the association between response of treatment with AChEIs and the APOE ɛ4 carrier status. METHODS: Clinical studies with AD patients reporting APOE ɛ4 genotype were included in the analysis. Cognitive outcome was measured by the change in Mini-Mental State Examination (MMSE), cognition subscales of the Alzheimer's Disease Assessment Scale (ADAS-cog), or Cognitive Abilities Screening Instrument (CASI). A random effects model was employed to calculate the standardized mean difference (SMD) and odds ratio (OR). RESULTS: Of the 284 screened abstracts, 38 studies were identified, 30 of which were included for meta-analysis. Continuous data for assessing the association between APOE ε4 and cognitive outcomes of AChEIs were available from 18 studies. The cognitive outcomes showed no significant difference between APOE ε4 carriers and APOE ε4 non-carriers (SMD = 0.022, 95% CI: -0.089∼0.133, p = 0.702, I2 = 55.3%). Twelve studies with binary data were included, also revealing insignificant difference between the two groups (OR = 1.164, 95% CI: 0.928∼1.459, p = 0.189, I2 = 16.4%). Subgroup analysis indicated that AChEIs were significantly more effective than placebo in both groups. CONCLUSIONS: APOE ɛ4 carrier status had no significant influence on the treatment response to AChEIs in patients with AD. AChEIs had a positive therapeutic effect compared with placebo regardless of APOE ε4 carrier status.

---

### PMID 24479631 — current stance: `inconclusive`

**Golden note:** BCHE + ApoE on cortical thickness/NPS — descriptive imaging.

**Butyrylcholinesterase K and apolipoprotein ε4 affect cortical thickness and neuropsychiatric symptoms in Alzheimer's disease.**

*Current Alzheimer research*, 2014. Types: Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't

> Two major genotypes are known to affect the development and progression of Alzheimer's disease (AD) and its response to cholinesterase inhibitors: the apolipoprotein E (ApoE) and butyrylcholinesterase genes (BChE). This study analyzed the effects of the BChE and ApoE genotypes on the cortical thickness of patients with AD and examined how these genotypes affect the neuropsychiatric symptoms of AD. AD-drug-naïve patients who met the probable AD criteria proposed by the National Institute of Neurological and Communicative Disorders and Stroke-Alzheimer's Disease and Related Disorders Association were recruited. Of 96 patients with AD, 65 were eligible for cortical thickness analysis. 3D T1-weighted images were acquired, and the cortical regions were segmented using the constrained Laplacian-based automated segmentation with proximities (CLASP) algorithm. Neuropsychiatric symptoms were measured by Neuropsychiatric Inventory (NPI) scores. BChE wild-type carriers (BChE-W) showed more thinning in the left dorsolateral prefrontal cortex, including the lateral premotor regions and anterior cingulate cortex, than did BChE-K variant carriers (BChE-K). ApoE-ε4 carriers had a thinner left medial prefrontal cortex, left superior frontal cortex, and left posterior cingulate cortex than did ApoE-ε4 non-carriers. Statistical analyses revealed that BChE-K carriers showed significantly less severe aberrant motor behavioral symptoms and that ε4 non-carriers showed less severe anxiety and indifference symptoms. The current findings show that, similar to ApoE-ε4 non-carriers, BChE-K carriers are protected from the pathological detriments of AD that affect frontal cortical thickness and neuropsychiatric symptoms. This study visually demonstrated the effects of the BChE-K and ApoE genotypes on the structural degeneration and complex aspects of the symptoms of AD.

---

