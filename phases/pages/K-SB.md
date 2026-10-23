# K–Sb phases

> K–Sb system: 9 phases (tier A 5, tier C 3, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/K-SB.html · Markdown: https://data.orchid-project.org/phases/pages/K-SB.md

9 phases (tier A 5, tier C 3, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=K-SB) · [full JSON](https://data.orchid-project.org/phases/systems/K-SB.json) · [K–Sb system page](https://data.orchid-project.org/systems/K-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/K-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the K–Sb system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-k-sb-a7-rhombohedral); _phase:k-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 3 | 1 |
| [BCC_A2](#phase-k-sb-bcc-a2); _phase:k-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(Sb) 0–0 | 2 | 1 |
| [FCC_A1](#phase-k-sb-fcc-a1); _phase:k-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-k-sb-hcp-a3); _phase:k-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [K3SB_D018](#phase-k-sb-k3sb-d018); _phase:k-sb:k3sb-d018_ | Na3As · D0_18 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1112.34 K, x(Sb) 0.25–0.25 | 6 | 1 |
| [K5SB4](#phase-k-sb-k5sb4); _phase:k-sb:k5sb4_ | Rb5As4 · mC20 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–777.23 K, x(Sb) 0.44444–0.44444 | 5 | 1 |
| [KSB](#phase-k-sb-ksb); _phase:k-sb:ksb_ | LiAs · mP16 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–887.55 K, x(Sb) 0.5–0.5 | 11 | 1 |
| [KSB2](#phase-k-sb-ksb2); _phase:k-sb:ksb2_ | KSb2 · mC12 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–671.16 K, x(Sb) 0.66667–0.66667 | 7 | 1 |
| [LIQUID](#phase-k-sb-liquid); _phase:k-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 336.53–2500 K, x(Sb) 0–1 | 21 | 1 |

## RHOMBOHEDRAL_A7 (K–Sb)

- Id: `phase:k-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:k-sb:a7-rhombohedral, corpus:phase:k-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2013.07.009:Sb  
_tdb: _tdb:KSb-13Liu.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `74f0dfc1d973f462…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (K–Sb)

- Id: `phase:k-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(Sb) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:bcc-a2)

Names (3): _corpus: _corpus:phase:k-sb:bcc-a2  
_paper: _paper:10.1016/j.tca.2013.07.009:K  
_tdb: _tdb:KSb-13Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): BCC_A2, type code %B, sha256 `74f0dfc1d973f462…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : K% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (K–Sb)

- Id: `phase:k-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:k-sb:fcc-a1  
_tdb: _tdb:KSb-13Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): FCC_A1, type code %A, sha256 `74f0dfc1d973f462…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : K SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase_

## HCP_A3 (K–Sb)

- Id: `phase:k-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:hcp-a3)

Names (2): _corpus: _corpus:phase:k-sb:hcp-a3  
_tdb: _tdb:KSb-13Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): HCP_A3, type code %A, sha256 `74f0dfc1d973f462…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : K SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase_

## K3SB_D018 (K–Sb)

- Id: `phase:k-sb:k3sb-d018`; status `assigned`
- Structure: Na3As · D0_18 · hP8 · P6_3/mmc (194); type `st:d0-18-na3as-hp8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1112.34 K, x(Sb) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:k3sb-d018)

Names (3): _corpus: _corpus:phase:k-sb:k3sb-d018  
_paper: _paper:10.1016/j.tca.2013.07.009:K3Sb  
_tdb: _tdb:KSb-13Liu.tdb:K3SB_D018  


### TDB models of K3SB_D018 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): K3SB_D018, type code %, sha256 `74f0dfc1d973f462…`

~~~~text
51: PHASE K3SB_D018 % 2 3 1 !
52: CONST K3SB_D018 : K : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_

## K5SB4 (K–Sb)

- Id: `phase:k-sb:k5sb4`; status `assigned`
- Structure: Rb5As4 · mC20 · C2/m (12); type `st:rb5as4-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–777.23 K, x(Sb) 0.44444–0.44444
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:k5sb4)

Names (3): _corpus: _corpus:phase:k-sb:k5sb4  
_paper: _paper:10.1016/j.tca.2013.07.009:K5Sb4  
_tdb: _tdb:KSb-13Liu.tdb:K5SB4  


### TDB models of K5SB4 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): K5SB4, type code %, sha256 `74f0dfc1d973f462…`

~~~~text
56: PHASE K5SB4 % 2 5 4 !
57: CONST K5SB4 : K : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_

## KSB (K–Sb)

- Id: `phase:k-sb:ksb`; status `assigned`
- Structure: LiAs · mP16 · P2_1/c (14); type `st:lias-mp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–887.55 K, x(Sb) 0.5–0.5
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:ksb)

Names (3): _corpus: _corpus:phase:k-sb:ksb  
_paper: _paper:10.1016/j.tca.2013.07.009:KSb  
_tdb: _tdb:KSb-13Liu.tdb:KSB  


### TDB models of KSB (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): KSB, type code %, sha256 `74f0dfc1d973f462…`

~~~~text
61: PHASE KSB % 2 1 1 !
62: CONST KSB : K : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.454540](https://doi.org/10.1063/1.454540) Marie-Louise Saboungi, Julie Ellefson, Gerald K. Johnson, Werner Freyland, Liquid potassium–antimony alloys: Investigation of some thermodynamic properties, The Journal of Chemical Physics 88, 5812-5817 (1988).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-1982-0612](https://doi.org/10.1515/zna-1982-0612) H. Redslob, G. Steinleitner, W. Freyland, Transition to Semiconducting Characteristics in Liquid Alkalimetal-Antimony-Alloys, Zeitschrift für Naturforschung A 37, 587-593 (1982).  
_cited as the source of values for this phase_

## KSB2 (K–Sb)

- Id: `phase:k-sb:ksb2`; status `assigned`
- Structure: KSb2 · mC12 · C2/m (12); type `st:ksb2-mc12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–671.16 K, x(Sb) 0.66667–0.66667
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:ksb2)

Names (3): _corpus: _corpus:phase:k-sb:ksb2  
_paper: _paper:10.1016/j.tca.2013.07.009:KSb2  
_tdb: _tdb:KSb-13Liu.tdb:KSB2  


### TDB models of KSB2 (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): KSB2, type code %, sha256 `74f0dfc1d973f462…`

~~~~text
66: PHASE KSB2 % 2 1 2 !
67: CONST KSB2 : K : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_

## LIQUID (K–Sb)

- Id: `phase:k-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 336.53–2500 K, x(Sb) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-sb:liquid)

Names (3): _corpus: _corpus:phase:k-sb:liquid  
_paper: _paper:10.1016/j.tca.2013.07.009:L  
_tdb: _tdb:KSb-13Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[KSb-13Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/KSb-13Liu.tdb): LIQUID, type code %, sha256 `74f0dfc1d973f462…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : K K3SB SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2013.07.009](https://doi.org/10.1016/j.tca.2013.07.009) Yajun Liu, Jun Xu, Zhitao Kang, Jiang Wang, Thermodynamic descriptions and phase diagrams for Sb–Na and Sb–K binary systems, Thermochimica Acta 569, 119-126 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1063/1.454540](https://doi.org/10.1063/1.454540) Marie-Louise Saboungi, Julie Ellefson, Gerald K. Johnson, Werner Freyland, Liquid potassium–antimony alloys: Investigation of some thermodynamic properties, The Journal of Chemical Physics 88, 5812-5817 (1988).  
_cited as the source of values for this phase_
- [doi:10.1515/zna-1982-0612](https://doi.org/10.1515/zna-1982-0612) H. Redslob, G. Steinleitner, W. Freyland, Transition to Semiconducting Characteristics in Liquid Alkalimetal-Antimony-Alloys, Zeitschrift für Naturforschung A 37, 587-593 (1982).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
