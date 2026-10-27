# Ag–Ge phases

> Ag–Ge system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-GE.html · Markdown: https://data.orchid-project.org/phases/pages/AG-GE.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-GE) · [full JSON](https://data.orchid-project.org/phases/systems/AG-GE.json) · [Ag–Ge system page](https://data.orchid-project.org/systems/AG-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ge system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ag-ge-a4-diamond); _phase:ag-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1 | 13 | 3 |
| [BCC_A2](#phase-ag-ge-bcc-a2); _phase:ag-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ag-ge-fcc-a1); _phase:ag-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1240.27 K, x(Ge) 0–0.09978 | 13 | 3 |
| [HCP_A3](#phase-ag-ge-hcp-a3); _phase:ag-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ag-ge-liquid); _phase:ag-ge:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 920.27–2500 K, x(Ge) 0–1 | 16 | 3 |

## DIAMOND_A4 (Ag–Ge)

- Id: `phase:ag-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ge:a4-diamond)

Names (6): _corpus: _corpus:phase:ag-ge:a4-diamond  
_paper: _paper:10.1016/0040-6031(88)87047-3:dia, paper:10.1016/j.tca.2010.11.003:diamond_A4(Ge)  
_tdb: _tdb:AgGe-11Wan.tdb:DIAMOND_A4, tdb:AgGe-18Raj.tdb:DIAMOND_A4, tdb:AgGe-88Che-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[AgGe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb): DIAMOND_A4, type code %, sha256 `ee980cd7d96cd656…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : GE : !
~~~~

[AgGe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb): DIAMOND_A4, type code %, sha256 `76195dd4c052f435…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : GE : !
~~~~

[AgGe-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb): DIAMOND_A4, type code %, sha256 `30d36f0532b31852…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : AG GE% : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_
- [doi:10.1021/j150301a010](https://doi.org/10.1021/j150301a010) T. R. Briggs, R. O. McDuffie, L. H. Willisford, Germanium. XXXI. Alloys of Germanium: Silver-Germanium, J. Phys. Chem. 33, 1080-1096 (1929).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254) S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Ge)

- Id: `phase:ag-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ge:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-ge:bcc-a2  
_tdb: _tdb:AgGe-11Wan.tdb:BCC_A2, tdb:AgGe-18Raj.tdb:BCC_A2, tdb:AgGe-88Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AgGe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb): BCC_A2, type code %B, sha256 `ee980cd7d96cd656…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG GE : VA : !
~~~~

[AgGe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb): BCC_A2, type code %B, sha256 `76195dd4c052f435…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG GE : VA : !
~~~~

[AgGe-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb): BCC_A2, type code %B, sha256 `30d36f0532b31852…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AG GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011).  
_assessment that models this phase_

## FCC_A1 (Ag–Ge)

- Id: `phase:ag-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1240.27 K, x(Ge) 0–0.09978
- Literature: 13 values (13 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ge:fcc-a1)

Names (6): _corpus: _corpus:phase:ag-ge:fcc-a1  
_paper: _paper:10.1016/0040-6031(88)87047-3:fcc, paper:10.1016/j.tca.2010.11.003:fcc-A1(Ag)  
_tdb: _tdb:AgGe-11Wan.tdb:FCC_A1, tdb:AgGe-18Raj.tdb:FCC_A1, tdb:AgGe-88Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AgGe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb): FCC_A1, type code %A, sha256 `ee980cd7d96cd656…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% GE : VA : !
~~~~

[AgGe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb): FCC_A1, type code %A, sha256 `76195dd4c052f435…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% GE : VA : !
~~~~

[AgGe-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb): FCC_A1, type code %A, sha256 `30d36f0532b31852…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AG% GE : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_
- [doi:10.1021/j150301a010](https://doi.org/10.1021/j150301a010) T. R. Briggs, R. O. McDuffie, L. H. Willisford, Germanium. XXXI. Alloys of Germanium: Silver-Germanium, J. Phys. Chem. 33, 1080-1096 (1929).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254) S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Ge)

- Id: `phase:ag-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ge:hcp-a3)

Names (4): _corpus: _corpus:phase:ag-ge:hcp-a3  
_tdb: _tdb:AgGe-11Wan.tdb:HCP_A3, tdb:AgGe-18Raj.tdb:HCP_A3, tdb:AgGe-88Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AgGe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb): HCP_A3, type code %A, sha256 `ee980cd7d96cd656…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG GE : VA : !
~~~~

[AgGe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb): HCP_A3, type code %A, sha256 `76195dd4c052f435…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG GE : VA : !
~~~~

[AgGe-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb): HCP_A3, type code %A, sha256 `30d36f0532b31852…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AG GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018).  
_assessment that models this phase_
- [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011).  
_assessment that models this phase_

## LIQUID (Ag–Ge)

- Id: `phase:ag-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 920.27–2500 K, x(Ge) 0–1
- Literature: 16 values (16 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ge:liquid)

Names (7): _corpus: _corpus:phase:ag-ge:liquid  
_paper: _paper:10.1007/s11664-018-6216-7:liquid, paper:10.1016/0040-6031(88)87047-3:L, paper:10.1016/j.tca.2010.11.003:L  
_tdb: _tdb:AgGe-11Wan.tdb:LIQUID, tdb:AgGe-18Raj.tdb:LIQUID, tdb:AgGe-88Che-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AgGe-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-11Wan.tdb): LIQUID, type code %, sha256 `ee980cd7d96cd656…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG GE : !
~~~~

[AgGe-18Raj.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-18Raj.tdb): LIQUID, type code %, sha256 `76195dd4c052f435…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG GE : !
~~~~

[AgGe-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgGe-88Che-LB.tdb): LIQUID, type code %, sha256 `30d36f0532b31852…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AG GE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0040-6031(88)87047-3](https://doi.org/10.1016/0040-6031%2888%2987047-3) P.-Y. Chevalier, Critical assessment of thermodynamic data for the Ag-Ge system, Thermochimica Acta 130, 25-32 (1988).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.003](https://doi.org/10.1016/j.tca.2010.11.003) J. Wang, Y.J. Liu, C.Y. Tang, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic description of the Au–Ag–Ge ternary system, Thermochimica Acta 512, 240-246 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-018-6216-7](https://doi.org/10.1007/s11664-018-6216-7) V. B. Rajkumar, Sinn-Wen Chen, Phase Equilibria and Thermodynamic Descriptions of Ag-Ge and Ag-Ge-Ni Systems, Journal of Elec Materi 47, 3666-3677 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_
- [doi:10.1021/j150301a010](https://doi.org/10.1021/j150301a010) T. R. Briggs, R. O. McDuffie, L. H. Willisford, Germanium. XXXI. Alloys of Germanium: Silver-Germanium, J. Phys. Chem. 33, 1080-1096 (1929).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254) S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
