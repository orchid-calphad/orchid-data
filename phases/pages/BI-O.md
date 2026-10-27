# Bi–O phases

> Bi–O system: 6 phases (tier A 2, tier C 1, liquid 1, gas 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-O.html · Markdown: https://data.orchid-project.org/phases/pages/BI-O.md

6 phases (tier A 2, tier C 1, liquid 1, gas 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-O) · [full JSON](https://data.orchid-project.org/phases/systems/BI-O.json) · [Bi–O system page](https://data.orchid-project.org/systems/BI-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–O system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-o-a7-rhombohedral); _phase:bi-o:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(O) 0–0 | 1 | 1 |
| [BI2O3_ALPHA](#phase-bi-o-bi2o3-alpha); _phase:bi-o:bi2o3-alpha_ | alpha-Bi2O3 · mP20 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1002.13 K, x(O) 0.6–0.6 | 34 | 1 |
| [BI2O3_C1](#phase-bi-o-bi2o3-c1); _phase:bi-o:bi2o3-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1002.13–1060.59 K, x(O) 0.6–0.6 | 25 | 1 |
| [GAS](#phase-bi-o-gas); _phase:bi-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1825.76–1966.02 K, x(O) 0–0.92757 | 0 | 1 |
| [ION](#phase-bi-o-ion); _phase:bi-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 544.55–1966.02 K, x(O) 0–0.59458 | 25 | 1 |
| [O2GAS](#phase-bi-o-o2gas); _phase:bi-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–925 K, x(O) 1–1 | 0 | 1 |

## RHOMBOHEDRAL_A7 (Bi–O)

- Id: `phase:bi-o:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(O) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-o:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:bi-o:a7-rhombohedral  
_paper: _paper:10.1007/bf02667306:Bi  
_tdb: _tdb:BiO-95Ris-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiO-95Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `77661bfd1c983207…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995).  
_assessment that models this phase; reports values for this phase_

## BI2O3_ALPHA (Bi–O)

- Id: `phase:bi-o:bi2o3-alpha`; status `assigned`
- Structure: alpha-Bi2O3 · mP20 · P2_1/c (14); type `st:alpha-bi2o3-mp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1002.13 K, x(O) 0.6–0.6
- Literature: 34 values (34 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-o:bi2o3-alpha)

Names (5): _corpus: _corpus:phase:bi-o:bi2o3-alpha  
_paper: _paper:10.1007/bf02667306:α, paper:10.1007/bf02667306:α, δ, paper:10.1007/bf02667306:α-Bi2O3  
_tdb: _tdb:BiO-95Ris-LB.tdb:BI2O3_ALPHA  


### TDB models of BI2O3_ALPHA (1): PHASE and CONSTITUENT statements as written

[BiO-95Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb): BI2O3_ALPHA, type code %, sha256 `77661bfd1c983207…`

~~~~text
52: PHASE BI2O3_ALPHA % 1 1 !
53: CONST BI2O3_ALPHA : BI2O3 : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0036-9748(71)90168-2](https://doi.org/10.1016/0036-9748%2871%2990168-2) A.V. Ramana Rao, V.B. Tare, Free energy of formation of Bi2O3, Scripta Metallurgica 5, 807-811 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(80)87127-9](https://doi.org/10.1016/0040-6031%2880%2987127-9) Krzysztop Fitzner, Diffusivity, activity and solubility of oxygen in liquid bismuth, Thermochimica Acta 35, 277-286 (1980).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2403593](https://doi.org/10.1149/1.2403593) D. Chatterji, J. V. Smith, Free Energy of Formation of Bi\[sub 2\]O\[sub 3\], Sb\[sub 2\]O\[sub 3\], and TeO\[sub 2\] from EMF Measurements, J. Electrochem. Soc. 120, 889 (1973).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.55.5_536](https://doi.org/10.2320/jinstmet1952.55.5_536) Kazuo Kameda, Katsunori Yamaguchi, Activity Measurements of Liquid Ag-Bi Alloys by an EMF Method Using a Zirconia Electrolyte, J.Japan Inst.Metals 55, 536-544 (1991).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.56.8_900](https://doi.org/10.2320/jinstmet1952.56.8_900) Kazuo Kameda, Katsunori Yamaguchi, Toshiko Kon, Activity of Liquid Tl-Bi Alloys Measured by an EMF Method Using Zirconia Electrolyte, J.Japan Inst.Metals 56, 900-906 (1992).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19623180307](https://doi.org/10.1002/zaac.19623180307) G. Gattow, H. Schröder, Über Wismutoxide. III. Die Kristallstruktur der Hochtemperaturmodifikation von Wismut(III)‐oxid (δ‐Bi\<sub>2\</sub>O\<sub>3\</sub>), Zeitschrift anorg allge chemie 318, 176-189 (1962).  
_cited as the source of values for this phase_
- [doi:10.1021/j100723a031](https://doi.org/10.1021/j100723a031) C. N. Ramachandra Rao, G. V. Subba Rao, S. Ramdas, Phase transformations and electrical properties of bismuth sesquioxide, J. Phys. Chem. 73, 672-675 (1969).  
_cited as the source of values for this phase_
- [doi:10.1021/je60035a021](https://doi.org/10.1021/je60035a021) Daniel Cubicciotti, Harold Eding, Enthalpy and entropy increments above 298.degree.K. for bismuth(III) bromide, bismuth(III) oxide, thallium(III) oxide, and thallium(I) oxide, J. Chem. Eng. Data 12, 548-551 (1967).  
_cited as the source of values for this phase_
- [doi:10.6028/jres.069a.023](https://doi.org/10.6028/jres.069a.023) Ernest M. Levin, Clyde L. McDaniel, Heats of transformations in bismuth oxide by differential thermal analysis, J. RES. NATL. BUR. STAN. SECT. A. 69A, 237 (1965).  
_cited as the source of values for this phase_

## BI2O3_C1 (Bi–O)

- Id: `phase:bi-o:bi2o3-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1002.13–1060.59 K, x(O) 0.6–0.6
- Literature: 25 values (25 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-o:bi2o3-c1)

Names (3): _corpus: _corpus:phase:bi-o:bi2o3-c1  
_paper: _paper:10.1007/bf02667306:δ-Bi2O3  
_tdb: _tdb:BiO-95Ris-LB.tdb:BI2O3_C1  


### TDB models of BI2O3_C1 (1): PHASE and CONSTITUENT statements as written

[BiO-95Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb): BI2O3_C1, type code %, sha256 `77661bfd1c983207…`

~~~~text
57: PHASE BI2O3_C1 % 1 1 !
58: CONST BI2O3_C1 : BI2O3 : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/je60035a021](https://doi.org/10.1021/je60035a021) Daniel Cubicciotti, Harold Eding, Enthalpy and entropy increments above 298.degree.K. for bismuth(III) bromide, bismuth(III) oxide, thallium(III) oxide, and thallium(I) oxide, J. Chem. Eng. Data 12, 548-551 (1967).  
_cited as the source of values for this phase_
- [doi:10.6028/jres.069a.023](https://doi.org/10.6028/jres.069a.023) Ernest M. Levin, Clyde L. McDaniel, Heats of transformations in bismuth oxide by differential thermal analysis, J. RES. NATL. BUR. STAN. SECT. A. 69A, 237 (1965).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19623180307](https://doi.org/10.1002/zaac.19623180307) G. Gattow, H. Schröder, Über Wismutoxide. III. Die Kristallstruktur der Hochtemperaturmodifikation von Wismut(III)‐oxid (δ‐Bi\<sub>2\</sub>O\<sub>3\</sub>), Zeitschrift anorg allge chemie 318, 176-189 (1962).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19643280106](https://doi.org/10.1002/zaac.19643280106) G. Gattow, D. Schütze, Über Wismutoxide. VI. Überein Wismut (III)‐oxid mit höherem Sauerstoffgehalt (β‐Modifikation), Zeitschrift anorg allge chemie 328, 44-68 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(71)90168-2](https://doi.org/10.1016/0036-9748%2871%2990168-2) A.V. Ramana Rao, V.B. Tare, Free energy of formation of Bi2O3, Scripta Metallurgica 5, 807-811 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(80)87127-9](https://doi.org/10.1016/0040-6031%2880%2987127-9) Krzysztop Fitzner, Diffusivity, activity and solubility of oxygen in liquid bismuth, Thermochimica Acta 35, 277-286 (1980).  
_cited as the source of values for this phase_
- [doi:10.1021/j100723a031](https://doi.org/10.1021/j100723a031) C. N. Ramachandra Rao, G. V. Subba Rao, S. Ramdas, Phase transformations and electrical properties of bismuth sesquioxide, J. Phys. Chem. 73, 672-675 (1969).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.55.5_536](https://doi.org/10.2320/jinstmet1952.55.5_536) Kazuo Kameda, Katsunori Yamaguchi, Activity Measurements of Liquid Ag-Bi Alloys by an EMF Method Using a Zirconia Electrolyte, J.Japan Inst.Metals 55, 536-544 (1991).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.56.8_900](https://doi.org/10.2320/jinstmet1952.56.8_900) Kazuo Kameda, Katsunori Yamaguchi, Toshiko Kon, Activity of Liquid Tl-Bi Alloys Measured by an EMF Method Using Zirconia Electrolyte, J.Japan Inst.Metals 56, 900-906 (1992).  
_cited as the source of values for this phase_

## GAS (Bi–O)

- Id: `phase:bi-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1825.76–1966.02 K, x(O) 0–0.92757
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-o:gas)

Names (2): _corpus: _corpus:phase:bi-o:gas  
_tdb: _tdb:BiO-95Ris-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[BiO-95Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb): GAS, type code %, sha256 `77661bfd1c983207…`

~~~~text
60: PHASE GAS:G % 1 1 !
61: CONST GAS:G : BI BI2 BI3 BI4 O O2 O3 
               BIO BI2O_C2V BI2O_DH BI2O2 BI2O3 BI3O4 BI4O6 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995).  
_assessment that models this phase_

## ION (Bi–O)

- Id: `phase:bi-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 544.55–1966.02 K, x(O) 0–0.59458
- Literature: 25 values (25 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-o:ion)

Names (6): _corpus: _corpus:phase:bi-o:ion, corpus:phase:bi-o:ion-2, corpus:phase:bi-o:liquid  
_paper: _paper:10.1007/bf02667306:L1, paper:10.1007/bf02667306:L2  
_tdb: _tdb:BiO-95Ris-LB.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[BiO-95Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb): ION, type code %, sha256 `77661bfd1c983207…`

~~~~text
42: PHASE ION:Y % 2 1 1 !
43: CONST ION:Y : BI+3 : O-2 VA O : !
~~~~

Example references (10 of 10; assessments first): 

- [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19623180307](https://doi.org/10.1002/zaac.19623180307) G. Gattow, H. Schröder, Über Wismutoxide. III. Die Kristallstruktur der Hochtemperaturmodifikation von Wismut(III)‐oxid (δ‐Bi\<sub>2\</sub>O\<sub>3\</sub>), Zeitschrift anorg allge chemie 318, 176-189 (1962).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19643280106](https://doi.org/10.1002/zaac.19643280106) G. Gattow, D. Schütze, Über Wismutoxide. VI. Überein Wismut (III)‐oxid mit höherem Sauerstoffgehalt (β‐Modifikation), Zeitschrift anorg allge chemie 328, 44-68 (1964).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(71)90168-2](https://doi.org/10.1016/0036-9748%2871%2990168-2) A.V. Ramana Rao, V.B. Tare, Free energy of formation of Bi2O3, Scripta Metallurgica 5, 807-811 (1971).  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(80)87127-9](https://doi.org/10.1016/0040-6031%2880%2987127-9) Krzysztop Fitzner, Diffusivity, activity and solubility of oxygen in liquid bismuth, Thermochimica Acta 35, 277-286 (1980).  
_cited as the source of values for this phase_
- [doi:10.1021/j100723a031](https://doi.org/10.1021/j100723a031) C. N. Ramachandra Rao, G. V. Subba Rao, S. Ramdas, Phase transformations and electrical properties of bismuth sesquioxide, J. Phys. Chem. 73, 672-675 (1969).  
_cited as the source of values for this phase_
- [doi:10.1021/je60035a021](https://doi.org/10.1021/je60035a021) Daniel Cubicciotti, Harold Eding, Enthalpy and entropy increments above 298.degree.K. for bismuth(III) bromide, bismuth(III) oxide, thallium(III) oxide, and thallium(I) oxide, J. Chem. Eng. Data 12, 548-551 (1967).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.55.5_536](https://doi.org/10.2320/jinstmet1952.55.5_536) Kazuo Kameda, Katsunori Yamaguchi, Activity Measurements of Liquid Ag-Bi Alloys by an EMF Method Using a Zirconia Electrolyte, J.Japan Inst.Metals 55, 536-544 (1991).  
_cited as the source of values for this phase_
- [doi:10.2320/jinstmet1952.56.8_900](https://doi.org/10.2320/jinstmet1952.56.8_900) Kazuo Kameda, Katsunori Yamaguchi, Toshiko Kon, Activity of Liquid Tl-Bi Alloys Measured by an EMF Method Using Zirconia Electrolyte, J.Japan Inst.Metals 56, 900-906 (1992).  
_cited as the source of values for this phase_
- [doi:10.6028/jres.069a.023](https://doi.org/10.6028/jres.069a.023) Ernest M. Levin, Clyde L. McDaniel, Heats of transformations in bismuth oxide by differential thermal analysis, J. RES. NATL. BUR. STAN. SECT. A. 69A, 237 (1965).  
_cited as the source of values for this phase_

## O2GAS (Bi–O)

- Id: `phase:bi-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–925 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-o:o2gas)

Names (2): _corpus: _corpus:phase:bi-o:o2gas  
_tdb: _tdb:BiO-95Ris-LB.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[BiO-95Ris-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiO-95Ris-LB.tdb): O2GAS, type code %, sha256 `77661bfd1c983207…`

~~~~text
64: PHASE O2GAS % 1 1 !
65: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02667306](https://doi.org/10.1007/BF02667306) D. Risold, B. Hallstedt, L.J. Gauckler, H.L. Lukas, S.G. Fries, J. Phase Equilib., 16, 223-34(1995).  
_assessment that models this phase_

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
