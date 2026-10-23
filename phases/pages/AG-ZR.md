# Ag–Zr phases

> Ag–Zr system: 6 phases (tier A 4, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/AG-ZR.md

6 phases (tier A 4, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/AG-ZR.json) · [Ag–Zr system page](https://data.orchid-project.org/systems/AG-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Zr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AGZR_B11](#phase-ag-zr-agzr-b11); _phase:ag-zr:agzr-b11_ | CuTi-gamma · B11 · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1439.67 K, x(Zr) 0.5–0.5 | 0 | 2 |
| [AGZR2](#phase-ag-zr-agzr2); _phase:ag-zr:agzr2_ | CuZr2 · tI6 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1472.62 K, x(Zr) 0.66667–0.66667 | 5 | 2 |
| [BCC_A2](#phase-ag-zr-bcc-a2); _phase:ag-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1092.97–3999.1 K, x(Zr) 0.78454–1 | 0 | 2 |
| [FCC_A1](#phase-ag-zr-fcc-a1); _phase:ag-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1236.42 K, x(Zr) 0–0.03279 | 0 | 2 |
| [HCP_A3](#phase-ag-zr-hcp-a3); _phase:ag-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2120.62 K, x(Zr) 0.98451–1 | 0 | 2 |
| [LIQUID](#phase-ag-zr-liquid); _phase:ag-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1216.42–4000 K, x(Zr) 0–1 | 3 | 2 |

## AGZR_B11 (Ag–Zr)

- Id: `phase:ag-zr:agzr-b11`; status `assigned`
- Structure: CuTi-gamma · B11 · tP4 · P4/nmm (129); type `st:b11-cuti-gamma-tp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqqh and oqmd-10690, space group 129
- Stoichiometry: Ag 0.5000, Zr 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1439.67 K, x(Zr) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zr:agzr-b11)

Names (5): _corpus: _corpus:phase:ag-zr:agzr-b11  
_mp: _mp:mp-aaaaaqqh  
_oqmd: _oqmd:oqmd-10690  
_tdb: _tdb:AgZr-16Hsi.tdb:AGZR_B11, tdb:AgZr-98Spe-LB.tdb:AGZR_B11  


### TDB models of AGZR_B11 (2): PHASE and CONSTITUENT statements as written

[AgZr-16Hsi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-16Hsi.tdb): AGZR_B11, type code %, sha256 `d8c54b1503abab3b…`

~~~~text
40: PHASE AGZR_B11 % 2 1 1 !
41: CONST AGZR_B11 : AG : ZR : !
~~~~

[AgZr-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-98Spe-LB.tdb): AGZR_B11, type code %, sha256 `bdaa7160c9ce0be1…`

~~~~text
40: PHASE AGZR_B11 % 2 0.5 0.5 !
41: CONST AGZR_B11 : AG : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.08.001](https://doi.org/10.1016/j.calphad.2016.08.001) H.-S. Hsiao, S.-M. Liang, R. Schmid-Fetzer, Y. Yen, Calphad, 55, 77-87(2016).  
_assessment that models this phase_

## AGZR2 (Ag–Zr)

- Id: `phase:ag-zr:agzr2`; status `assigned`
- Structure: CuZr2 · tI6 · I4/mmm (139); type `st:cuzr2-ti6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.3333, Zr 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1472.62 K, x(Zr) 0.66667–0.66667
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zr:agzr2)

Names (4): _corpus: _corpus:phase:ag-zr:agzr2  
_paper: _paper:10.1016/j.calphad.2006.09.001:AgZr2  
_tdb: _tdb:AgZr-16Hsi.tdb:AGZR2, tdb:AgZr-98Spe-LB.tdb:AGZR2  


### TDB models of AGZR2 (2): PHASE and CONSTITUENT statements as written

[AgZr-16Hsi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-16Hsi.tdb): AGZR2, type code %, sha256 `d8c54b1503abab3b…`

~~~~text
45: PHASE AGZR2 % 2 1 2 !
46: CONST AGZR2 : AG : ZR : !
~~~~

[AgZr-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-98Spe-LB.tdb): AGZR2, type code %, sha256 `bdaa7160c9ce0be1…`

~~~~text
45: PHASE AGZR2 % 2 1 2 !
46: CONST AGZR2 : AG : ZR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2016.08.001](https://doi.org/10.1016/j.calphad.2016.08.001) H.-S. Hsiao, S.-M. Liang, R. Schmid-Fetzer, Y. Yen, Calphad, 55, 77-87(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.001](https://doi.org/10.1016/j.calphad.2006.09.001) X.C. He, H. Wang, H.S. Liu, Z.P. Jin, Thermodynamic description of the Cu–Ag–Zr system, Calphad 30, 367-374 (2006).  
_reports values for this phase_
- [doi:10.1007/bf02667477](https://doi.org/10.1007/bf02667477) I. Karakaya, W. T. Thompson, The Ag-Zr (silver-zirconium) system, JPE 13, 143-146 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90105-1](https://doi.org/10.1016/0022-5088%2888%2990105-1) Kanghou Zhang, Huaizhi Zhao, Yuehua Zhou, An investigation of the Ag-Zr phase diagram, Journal of the Less Common Metals 138, 173-177 (1988).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Zr)

- Id: `phase:ag-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1092.97–3999.1 K, x(Zr) 0.78454–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zr:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-zr:bcc-a2  
_tdb: _tdb:AgZr-16Hsi.tdb:BCC_A2, tdb:AgZr-98Spe-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgZr-16Hsi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-16Hsi.tdb): BCC_A2, type code %B, sha256 `d8c54b1503abab3b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG ZR% : VA : !
~~~~

[AgZr-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-98Spe-LB.tdb): BCC_A2, type code %B, sha256 `bdaa7160c9ce0be1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.08.001](https://doi.org/10.1016/j.calphad.2016.08.001) H.-S. Hsiao, S.-M. Liang, R. Schmid-Fetzer, Y. Yen, Calphad, 55, 77-87(2016).  
_assessment that models this phase_

## FCC_A1 (Ag–Zr)

- Id: `phase:ag-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1236.42 K, x(Zr) 0–0.03279
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:ag-zr:fcc-a1  
_tdb: _tdb:AgZr-16Hsi.tdb:FCC_A1, tdb:AgZr-98Spe-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgZr-16Hsi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-16Hsi.tdb): FCC_A1, type code %A, sha256 `d8c54b1503abab3b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% ZR : VA : !
~~~~

[AgZr-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-98Spe-LB.tdb): FCC_A1, type code %A, sha256 `bdaa7160c9ce0be1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.08.001](https://doi.org/10.1016/j.calphad.2016.08.001) H.-S. Hsiao, S.-M. Liang, R. Schmid-Fetzer, Y. Yen, Calphad, 55, 77-87(2016).  
_assessment that models this phase_

## HCP_A3 (Ag–Zr)

- Id: `phase:ag-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2120.62 K, x(Zr) 0.98451–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zr:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-zr:hcp-a3  
_tdb: _tdb:AgZr-16Hsi.tdb:HCP_A3, tdb:AgZr-98Spe-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgZr-16Hsi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-16Hsi.tdb): HCP_A3, type code %A, sha256 `d8c54b1503abab3b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG ZR% : VA : !
~~~~

[AgZr-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-98Spe-LB.tdb): HCP_A3, type code %A, sha256 `bdaa7160c9ce0be1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.08.001](https://doi.org/10.1016/j.calphad.2016.08.001) H.-S. Hsiao, S.-M. Liang, R. Schmid-Fetzer, Y. Yen, Calphad, 55, 77-87(2016).  
_assessment that models this phase_

## LIQUID (Ag–Zr)

- Id: `phase:ag-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1216.42–4000 K, x(Zr) 0–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-zr:liquid)

Names (5): _corpus: _corpus:phase:ag-zr:liquid  
_paper: _paper:10.1016/j.calphad.2006.09.001:L, paper:10.1016/j.calphad.2006.09.001:liquid  
_tdb: _tdb:AgZr-16Hsi.tdb:LIQUID, tdb:AgZr-98Spe-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgZr-16Hsi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-16Hsi.tdb): LIQUID, type code %, sha256 `d8c54b1503abab3b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG ZR : !
~~~~

[AgZr-98Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgZr-98Spe-LB.tdb): LIQUID, type code %, sha256 `bdaa7160c9ce0be1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG ZR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2016.08.001](https://doi.org/10.1016/j.calphad.2016.08.001) H.-S. Hsiao, S.-M. Liang, R. Schmid-Fetzer, Y. Yen, Calphad, 55, 77-87(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2006.09.001](https://doi.org/10.1016/j.calphad.2006.09.001) X.C. He, H. Wang, H.S. Liu, Z.P. Jin, Thermodynamic description of the Cu–Ag–Zr system, Calphad 30, 367-374 (2006).  
_reports values for this phase_
- [doi:10.1007/bf02667477](https://doi.org/10.1007/bf02667477) I. Karakaya, W. T. Thompson, The Ag-Zr (silver-zirconium) system, JPE 13, 143-146 (1992).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90105-1](https://doi.org/10.1016/0022-5088%2888%2990105-1) Kanghou Zhang, Huaizhi Zhao, Yuehua Zhou, An investigation of the Ag-Zr phase diagram, Journal of the Less Common Metals 138, 173-177 (1988).  
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
