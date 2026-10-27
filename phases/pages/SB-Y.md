# Sb–Y phases

> Sb–Y system: 9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-Y.html · Markdown: https://data.orchid-project.org/phases/pages/SB-Y.md

9 phases (tier A 7, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-Y) · [full JSON](https://data.orchid-project.org/phases/systems/SB-Y.json) · [Sb–Y system page](https://data.orchid-project.org/systems/SB-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Y system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-sb-y-a7-rhombohedral); _phase:sb-y:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Y) 0–0 | 2 | 1 |
| [BCC_A2](#phase-sb-y-bcc-a2); _phase:sb-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1728.01–2498.89 K, x(Y) 0.993–1 | 2 | 1 |
| [FCC_A1](#phase-sb-y-fcc-a1); _phase:sb-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-sb-y-hcp-a3); _phase:sb-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1786.14 K, x(Y) 0.98777–1 | 4 | 1 |
| [LIQUID](#phase-sb-y-liquid); _phase:sb-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 897.07–2500 K, x(Y) 0–1 | 14 | 1 |
| [SB3Y4_D73](#phase-sb-y-sb3y4-d73); _phase:sb-y:sb3y4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1937.55–2393.33 K, x(Y) 0.57143–0.57143 | 6 | 1 |
| [SB3Y5_D88](#phase-sb-y-sb3y5-d88); _phase:sb-y:sb3y5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1970.37 K, x(Y) 0.625–0.625 | 6 | 1 |
| [SBY_B1](#phase-sb-y-sby-b1); _phase:sb-y:sby-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Y) 0.5–0.5 | 8 | 1 |
| [SBY3](#phase-sb-y-sby3); _phase:sb-y:sby3_ | Ti3P · tP32 · P4_2/n (86) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1514.23 K, x(Y) 0.75–0.75 | 6 | 1 |

## RHOMBOHEDRAL_A7 (Sb–Y)

- Id: `phase:sb-y:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Y) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:sb-y:a7-rhombohedral, corpus:phase:sb-y:rhombohedral-a7  
_paper: _paper:10.1016/j.jallcom.2008.07.105:Rhom.Sb  
_tdb: _tdb:SbY-09Zha.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6718da107ce22a10…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## BCC_A2 (Sb–Y)

- Id: `phase:sb-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1728.01–2498.89 K, x(Y) 0.993–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:bcc-a2)

Names (3): _corpus: _corpus:phase:sb-y:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.07.105:Bcc_Y  
_tdb: _tdb:SbY-09Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): BCC_A2, type code %B, sha256 `6718da107ce22a10…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : SB Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## FCC_A1 (Sb–Y)

- Id: `phase:sb-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:fcc-a1)

Names (2): _corpus: _corpus:phase:sb-y:fcc-a1  
_tdb: _tdb:SbY-09Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): FCC_A1, type code %A, sha256 `6718da107ce22a10…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : SB Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase_

## HCP_A3 (Sb–Y)

- Id: `phase:sb-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1786.14 K, x(Y) 0.98777–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:hcp-a3)

Names (3): _corpus: _corpus:phase:sb-y:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.07.105:Hcp_Y  
_tdb: _tdb:SbY-09Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): HCP_A3, type code %A, sha256 `6718da107ce22a10…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : SB Y% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## LIQUID (Sb–Y)

- Id: `phase:sb-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 897.07–2500 K, x(Y) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:liquid)

Names (3): _corpus: _corpus:phase:sb-y:liquid  
_paper: _paper:10.1016/j.jallcom.2008.07.105:L  
_tdb: _tdb:SbY-09Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): LIQUID, type code %, sha256 `6718da107ce22a10…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : SB Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## SB3Y4_D73 (Sb–Y)

- Id: `phase:sb-y:sb3y4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.4286, Y 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 1937.55–2393.33 K, x(Y) 0.57143–0.57143
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:sb3y4-d73)

Names (3): _corpus: _corpus:phase:sb-y:sb3y4-d73  
_paper: _paper:10.1016/j.jallcom.2008.07.105:Sb3Y4  
_tdb: _tdb:SbY-09Zha.tdb:SB3Y4_D73  


### TDB models of SB3Y4_D73 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): SB3Y4_D73, type code %, sha256 `6718da107ce22a10…`

~~~~text
57: PHASE SB3Y4_D73 % 2 3 4 !
58: CONST SB3Y4_D73 : SB : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## SB3Y5_D88 (Sb–Y)

- Id: `phase:sb-y:sb3y5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacprcc and oqmd-31051, space group 193
- Stoichiometry: Sb 0.3750, Y 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1970.37 K, x(Y) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:sb3y5-d88)

Names (5): _corpus: _corpus:phase:sb-y:sb3y5-d88  
_mp: _mp:mp-aaacprcc  
_oqmd: _oqmd:oqmd-31051  
_paper: _paper:10.1016/j.jallcom.2008.07.105:Sb3Y5  
_tdb: _tdb:SbY-09Zha.tdb:SB3Y5_D88  


### TDB models of SB3Y5_D88 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): SB3Y5_D88, type code %, sha256 `6718da107ce22a10…`

~~~~text
62: PHASE SB3Y5_D88 % 2 3 5 !
63: CONST SB3Y5_D88 : SB : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## SBY_B1 (Sb–Y)

- Id: `phase:sb-y:sby-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 0.5000, Y 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Y) 0.5–0.5
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:sby-b1)

Names (3): _corpus: _corpus:phase:sb-y:sby-b1  
_paper: _paper:10.1016/j.jallcom.2008.07.105:SbY  
_tdb: _tdb:SbY-09Zha.tdb:SBY_B1  


### TDB models of SBY_B1 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): SBY_B1, type code %, sha256 `6718da107ce22a10…`

~~~~text
52: PHASE SBY_B1 % 2 1 1 !
53: CONST SBY_B1 : SB : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

## SBY3 (Sb–Y)

- Id: `phase:sb-y:sby3`; status `assigned`
- Structure: Ti3P · tP32 · P4_2/n (86); type `st:ti3p-tp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sb 0.2500, Y 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1514.23 K, x(Y) 0.75–0.75
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-y:sby3)

Names (3): _corpus: _corpus:phase:sb-y:sby3  
_paper: _paper:10.1016/j.jallcom.2008.07.105:SbY3  
_tdb: _tdb:SbY-09Zha.tdb:SBY3  


### TDB models of SBY3 (1): PHASE and CONSTITUENT statements as written

[SbY-09Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/SbY-09Zha.tdb): SBY3, type code %, sha256 `6718da107ce22a10…`

~~~~text
67: PHASE SBY3 % 2 1 3 !
68: CONST SBY3 : SB : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.105](https://doi.org/10.1016/j.jallcom.2008.07.105) L.G. Zhang, H.M. Chen, H.Q. Dong, G.X. Huang, L.B. Liu, Z.P. Jin, Thermodynamic description of the Al–Sb–Y system, Journal of Alloys and Compounds 475, 233-237 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(70)90045-7](https://doi.org/10.1016/0022-5088%2870%2990045-7) F.A. Schmidt, O.D. McMasters, Yttrium-antimony alloy system, Journal of the Less Common Metals 21, 415-425 (1970).  
_cited as the source of values for this phase_

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
