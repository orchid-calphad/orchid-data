# Co–O phases

> Co–O system: 9 phases (tier A 4, tier C 1, liquid 2, gas 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-O.html · Markdown: https://data.orchid-project.org/phases/pages/CO-O.md

9 phases (tier A 4, tier C 1, liquid 2, gas 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-O) · [full JSON](https://data.orchid-project.org/phases/systems/CO-O.json) · [Co–O system page](https://data.orchid-project.org/systems/CO-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–O system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HALITE_B1](#phase-co-o-b1-halite); _phase:co-o:b1-halite_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1916.89 K, x(O) 0.5–0.5 | 15 | 1 |
| [BCC_A2](#phase-co-o-bcc-a2); _phase:co-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-co-o-fcc-a1); _phase:co-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 693.99–1767.99 K, x(O) 0–0.00123 | 6 | 1 |
| [GAS](#phase-co-o-gas); _phase:co-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1524.39–2500 K, x(O) 0.99862–1 | 0 | 1 |
| [SPINEL_H11](#phase-co-o-h11-spinel); _phase:co-o:h11-spinel_ | Al2MgO4 · H1_1 · cF56 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1185 K, x(O) 0.57143–0.57143 | 5 | 1 |
| [HCP_A3](#phase-co-o-hcp-a3); _phase:co-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1726.24 K, x(O) 0–0.00052 | 0 | 1 |
| [ION](#phase-co-o-ion); _phase:co-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1766.99–2500 K, x(O) 0–0.50213 | 0 | 1 |
| [LIQUID](#phase-co-o-liquid); _phase:co-o:liquid_ | liquid | liquid | not stable in 1 calculated diagram(s) | 17 | 1 |
| [O2GAS](#phase-co-o-o2gas); _phase:co-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–1185 K, x(O) 1–1 | 0 | 1 |

## HALITE_B1 (Co–O)

- Id: `phase:co-o:b1-halite`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1916.89 K, x(O) 0.5–0.5
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:b1-halite)

Names (3): _corpus: _corpus:phase:co-o:b1-halite  
_paper: _paper:10.1361/105497103770330514:CoO  
_tdb: _tdb:CoO-03Che-LB.tdb:HALITE_B1  


### TDB models of HALITE_B1 (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): HALITE_B1, type code %A, sha256 `6da44079fa3d4ae1…`

~~~~text
56: PHASE HALITE_B1:I %A 2 1 1 !
57: CONST HALITE_B1:I : CO+2 : O-2 : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans1960.29.125](https://doi.org/10.2320/matertrans1960.29.125) G. M. Kale, S. S. Pandit, K. T. Jacob, Thermodynamics of Cobalt (II, III) Oxide (Co&lt;SUB&gt;3&lt;/SUB&gt;O&lt;SUB&gt;4&lt;/SUB&gt;): Evidence of Phase Transition, Trans. JIM 29, 125-132 (1988).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.41.8_803](https://doi.org/10.2320/jinstmet1952.41.8_803) Nobumasa Kemori, Iwao Katayama, Zensaku Kozuka, Measurements of Standard Molar Free Energies of Formation of NiO, Cu&lt;SUB&gt;2&lt;/SUB&gt;O and CoO by EMF Method at High Temperatures, J.Japan Inst.Metals 41, 803-808 (1977).  
_cited as the source of values for this phase_

## BCC_A2 (Co–O)

- Id: `phase:co-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:bcc-a2)

Names (2): _corpus: _corpus:phase:co-o:bcc-a2  
_tdb: _tdb:CoO-03Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): BCC_A2, type code %B, sha256 `6da44079fa3d4ae1…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : CO : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase_

## FCC_A1 (Co–O)

- Id: `phase:co-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 693.99–1767.99 K, x(O) 0–0.00123
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:fcc-a1)

Names (3): _corpus: _corpus:phase:co-o:fcc-a1  
_paper: _paper:10.1361/105497103770330514:Co(fcc)  
_tdb: _tdb:CoO-03Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): FCC_A1, type code %A, sha256 `6da44079fa3d4ae1…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : CO : O VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.41.8_803](https://doi.org/10.2320/jinstmet1952.41.8_803) Nobumasa Kemori, Iwao Katayama, Zensaku Kozuka, Measurements of Standard Molar Free Energies of Formation of NiO, Cu&lt;SUB&gt;2&lt;/SUB&gt;O and CoO by EMF Method at High Temperatures, J.Japan Inst.Metals 41, 803-808 (1977).  
_cited as the source of values for this phase_

## GAS (Co–O)

- Id: `phase:co-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1524.39–2500 K, x(O) 0.99862–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:gas)

Names (2): _corpus: _corpus:phase:co-o:gas  
_tdb: _tdb:CoO-03Che-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): GAS, type code %, sha256 `6da44079fa3d4ae1…`

~~~~text
67: PHASE GAS:G % 1 1 !
68: CONST GAS:G : CO COO CO2 O O2 O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase_

## SPINEL_H11 (Co–O)

- Id: `phase:co-o:h11-spinel`; status `assigned`
- Structure: Al2MgO4 · H1_1 · cF56 · Fd-3m (227); type `st:h1-1-al2mgo4-cf56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:SPINEL); structure as stated in the SGTE crystallographic table for this phase name and system
- Caveat: partitioned order/disorder model in CoO-03Che-LB.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1185 K, x(O) 0.57143–0.57143
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:h11-spinel)

Names (3): _corpus: _corpus:phase:co-o:h11-spinel  
_paper: _paper:10.1361/105497103770330514:Co3O4  
_tdb: _tdb:CoO-03Che-LB.tdb:SPINEL_H11  


### TDB models of SPINEL_H11 (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): SPINEL_H11, type code %, sha256 `6da44079fa3d4ae1…`

~~~~text
61: PHASE SPINEL_H11:I % 3 1 2 4 !
62: CONST SPINEL_H11:I : CO+2 CO+3 : CO+2 CO+3 : O-2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans1960.29.125](https://doi.org/10.2320/matertrans1960.29.125) G. M. Kale, S. S. Pandit, K. T. Jacob, Thermodynamics of Cobalt (II, III) Oxide (Co&lt;SUB&gt;3&lt;/SUB&gt;O&lt;SUB&gt;4&lt;/SUB&gt;): Evidence of Phase Transition, Trans. JIM 29, 125-132 (1988).  
_cited as the source of values for this phase_

## HCP_A3 (Co–O)

- Id: `phase:co-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1726.24 K, x(O) 0–0.00052
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:hcp-a3)

Names (2): _corpus: _corpus:phase:co-o:hcp-a3  
_tdb: _tdb:CoO-03Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): HCP_A3, type code %A, sha256 `6da44079fa3d4ae1…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : CO : O VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase_

## ION (Co–O)

- Id: `phase:co-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1766.99–2500 K, x(O) 0–0.50213
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:ion)

Names (2): _corpus: _corpus:phase:co-o:ion  
_tdb: _tdb:CoO-03Che-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): ION, type code %, sha256 `6da44079fa3d4ae1…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : CO+2 CO+3 : O-2 VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase_

## LIQUID (Co–O)

- Id: `phase:co-o:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Co 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 17 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:liquid)

Names (5): _corpus: _corpus:phase:co-o:liquid  
_paper: _paper:10.1361/105497103770330514:L1, paper:10.1361/105497103770330514:L2, paper:10.1361/105497103770330514:liquid  
_tdb: _tdb:CoO-03Che-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): LIQUID, type code %, sha256 `6da44079fa3d4ae1…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : CO : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19512650110](https://doi.org/10.1002/zaac.19512650110) P. Asanti, E. J. Kohlmeyer, Über die thermischen Eigenschaften der Verbindungen von Kobalt mit Sauerstoff und Schwefel, Zeitschrift anorg allge chemie 265, 90-98 (1951).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.41.8_803](https://doi.org/10.2320/jinstmet1952.41.8_803) Nobumasa Kemori, Iwao Katayama, Zensaku Kozuka, Measurements of Standard Molar Free Energies of Formation of NiO, Cu&lt;SUB&gt;2&lt;/SUB&gt;O and CoO by EMF Method at High Temperatures, J.Japan Inst.Metals 41, 803-808 (1977).  
_cited as the source of values for this phase_

## O2GAS (Co–O)

- Id: `phase:co-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1185 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-o:o2gas)

Names (2): _corpus: _corpus:phase:co-o:o2gas  
_tdb: _tdb:CoO-03Che-LB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[CoO-03Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoO-03Che-LB.tdb): O2GAS, type code %, sha256 `6da44079fa3d4ae1…`

~~~~text
64: PHASE O2GAS % 1 1 !
65: CONST O2GAS : O2 :!
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497103770330514](https://doi.org/10.1361/105497103770330514) Ming Chen, Bengt Hallstedt, Ludwig J. Gauckler, Thermodynamic assessment of the Co-O system, JPE 24, 212-227 (2003).  
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
