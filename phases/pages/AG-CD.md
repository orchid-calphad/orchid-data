# Ag–Cd phases

> Ag–Cd system: 8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-CD.html · Markdown: https://data.orchid-project.org/phases/pages/AG-CD.md

8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-CD) · [full JSON](https://data.orchid-project.org/phases/systems/AG-CD.json) · [Ag–Cd system page](https://data.orchid-project.org/systems/AG-CD.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-CD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Cd system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2CD3_D82](#phase-ag-cd-ag2cd3-d82); _phase:ag-cd:ag2cd3-d82_ |  | needs_review | stable in 1 of 2 calculated diagram(s): 300–903.4 K, x(Cd) 0.6–0.6 | 0 | 2 |
| [AGCD_A3](#phase-ag-cd-agcd-a3); _phase:ag-cd:agcd-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 497.81–734.39 K, x(Cd) 0.48276–0.54602 | 0 | 1 |
| [AGCD_B2](#phase-ag-cd-agcd-b2); _phase:ag-cd:agcd-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–516.94 K, x(Cd) 0.5–0.5 | 0 | 2 |
| [BCC_A2](#phase-ag-cd-bcc-a2); _phase:ag-cd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 701.38–992.97 K, x(Cd) 0.4272–0.59379 | 0 | 2 |
| [FCC_A1](#phase-ag-cd-fcc-a1); _phase:ag-cd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1234.93 K, x(Cd) 0–0.44276 | 0 | 2 |
| [HCP_A3](#phase-ag-cd-hcp-a3); _phase:ag-cd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–866.6 K, x(Cd) 0.66673–1 | 0 | 2 |
| [HCP_IM_A3](#phase-ag-cd-hcp-a3-im); _phase:ag-cd:hcp-a3-im_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–886.3 K, x(Cd) 0.49106–0.82749 | 0 | 1 |
| [LIQUID](#phase-ag-cd-liquid); _phase:ag-cd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 593.22–2500 K, x(Cd) 0–1 | 0 | 2 |

## AG2CD3_D82 (Ag–Cd)

- Id: `phase:ag-cd:ag2cd3-d82`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_2; stoichiometry_contradicts_D8_2:AgCd-04Che-LB.tdb; stoichiometry_contradicts_D8_2:AgCd-19Fis.tdb
- Candidate (name_token): Cu5Zn8 · D8_2 · cI52 · I-43m (217) — Strukturbericht/word 'D82' in the TDB name
- Candidate (sgte_mmc2): Cu5Zn8 · D8_2 · cI52 · I-43m (217) — Hallstedt 2025 mmc2 row for AG2CD3_D82: Ag2Cd3
- Candidate (tdb_comment): Cu5Zn8 · cI52 · I-43m — AgCd-04Che-LB.tdb: 'Prototype Cu5Zn8 (cI52, I-43m)'
- Candidate (tdb_comment): Cu5Zn8 · cI52 · I-43m — AgCd-19Fis.tdb: 'Prototype Cu5Zn8 (cI52, I-43m)'
- Stoichiometry: Ag 0.4000, Cd 0.6000
- Stability: stable in 1 of 2 calculated diagram(s): 300–903.4 K, x(Cd) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:ag2cd3-d82)

Names (3): _corpus: _corpus:phase:ag-cd:ag2cd3-d82  
_tdb: _tdb:AgCd-04Che-LB.tdb:AG2CD3_D82, tdb:AgCd-19Fis.tdb:AG2CD3_D82  


### TDB models of AG2CD3_D82 (2): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): AG2CD3_D82, type code %, sha256 `1069d30f1957b866…`

~~~~text
58: PHASE AG2CD3_D82 % 2 2 3 !
59: CONST AG2CD3_D82 : AG : CD : !
~~~~

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): AG2CD3_D82, type code %, sha256 `34c2dd35b1690188…`

~~~~text
51: PHASE AG2CD3_D82 % 2 2 3 !
52: CONST AG2CD3_D82 : AG : CD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## AGCD_A3 (Ag–Cd)

- Id: `phase:ag-cd:agcd-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 497.81–734.39 K, x(Cd) 0.48276–0.54602
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:agcd-a3)

Names (2): _corpus: _corpus:phase:ag-cd:agcd-a3  
_tdb: _tdb:AgCd-04Che-LB.tdb:AGCD_A3  


### TDB models of AGCD_A3 (1): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): AGCD_A3, type code %, sha256 `1069d30f1957b866…`

~~~~text
48: PHASE AGCD_A3 % 1 1 !
49: CONST AGCD_A3 : AG CD : !
~~~~

## AGCD_B2 (Ag–Cd)

- Id: `phase:ag-cd:agcd-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.5000, Cd 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–516.94 K, x(Cd) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:agcd-b2)

Names (3): _corpus: _corpus:phase:ag-cd:agcd-b2  
_tdb: _tdb:AgCd-04Che-LB.tdb:AGCD_B2, tdb:AgCd-19Fis.tdb:AGCD_B2  


### TDB models of AGCD_B2 (2): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): AGCD_B2, type code %, sha256 `1069d30f1957b866…`

~~~~text
53: PHASE AGCD_B2 % 2 1 1 !
54: CONST AGCD_B2 : AG : CD : !
~~~~

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): AGCD_B2, type code %, sha256 `34c2dd35b1690188…`

~~~~text
46: PHASE AGCD_B2 % 2 1 1 !
47: CONST AGCD_B2 : AG : CD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## BCC_A2 (Ag–Cd)

- Id: `phase:ag-cd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 701.38–992.97 K, x(Cd) 0.4272–0.59379
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-cd:bcc-a2  
_tdb: _tdb:AgCd-04Che-LB.tdb:BCC_A2, tdb:AgCd-19Fis.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): BCC_A2, type code %B, sha256 `1069d30f1957b866…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AG CD : VA : !
~~~~

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): BCC_A2, type code %B, sha256 `34c2dd35b1690188…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## FCC_A1 (Ag–Cd)

- Id: `phase:ag-cd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1234.93 K, x(Cd) 0–0.44276
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-cd:fcc-a1  
_tdb: _tdb:AgCd-04Che-LB.tdb:FCC_A1, tdb:AgCd-19Fis.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): FCC_A1, type code %A, sha256 `1069d30f1957b866…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AG% CD : VA : !
~~~~

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): FCC_A1, type code %A, sha256 `34c2dd35b1690188…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% CD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## HCP_A3 (Ag–Cd)

- Id: `phase:ag-cd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–866.6 K, x(Cd) 0.66673–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-cd:hcp-a3  
_tdb: _tdb:AgCd-04Che-LB.tdb:HCP_A3, tdb:AgCd-19Fis.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): HCP_A3, type code %A, sha256 `1069d30f1957b866…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AG CD% : VA : !
~~~~

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): HCP_A3, type code %A, sha256 `34c2dd35b1690188…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG CD% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## HCP_IM_A3 (Ag–Cd)

- Id: `phase:ag-cd:hcp-a3-im`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:IM); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–886.3 K, x(Cd) 0.49106–0.82749
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:hcp-a3-im)

Names (2): _corpus: _corpus:phase:ag-cd:hcp-a3-im  
_tdb: _tdb:AgCd-19Fis.tdb:HCP_IM_A3  


### TDB models of HCP_IM_A3 (1): PHASE and CONSTITUENT statements as written

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): HCP_IM_A3, type code %, sha256 `34c2dd35b1690188…`

~~~~text
41: PHASE HCP_IM_A3 % 1 1 !
42: CONST HCP_IM_A3 : AG CD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## LIQUID (Ag–Cd)

- Id: `phase:ag-cd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 593.22–2500 K, x(Cd) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cd:liquid)

Names (3): _corpus: _corpus:phase:ag-cd:liquid  
_tdb: _tdb:AgCd-04Che-LB.tdb:LIQUID, tdb:AgCd-19Fis.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgCd-04Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-04Che-LB.tdb): LIQUID, type code %, sha256 `1069d30f1957b866…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AG CD : !
~~~~

[AgCd-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCd-19Fis.tdb): LIQUID, type code %, sha256 `34c2dd35b1690188…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG CD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
