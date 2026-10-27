# Hg–In phases

> Hg–In system: 9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HG-IN.html · Markdown: https://data.orchid-project.org/phases/pages/HG-IN.md

9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HG-IN) · [full JSON](https://data.orchid-project.org/phases/systems/HG-IN.json) · [Hg–In system page](https://data.orchid-project.org/systems/HG-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/HG-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hg–In system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-hg-in-a10-rhombo); _phase:hg-in:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 4 | 2 |
| [TETRAGONAL_A6](#phase-hg-in-a6-tetragonal); _phase:hg-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–524.75 K, x(In) 0.94442–1 | 0 | 2 |
| [BCC_A2](#phase-hg-in-bcc-a2); _phase:hg-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-hg-in-fcc-a1); _phase:hg-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(In) 0–0.93234 | 6 | 2 |
| [GAMMA_PU](#phase-hg-in-gamma-pu); _phase:hg-in:gamma-pu_ | gamma-Pu · oF8 · Fddd (70) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 4 | 2 |
| [HCP_A3](#phase-hg-in-hcp-a3); _phase:hg-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HGIN](#phase-hg-in-hgin); _phase:hg-in:hgin_ | HgIn · hR2 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 2 calculated diagram(s) | 8 | 2 |
| [HGIN2](#phase-hg-in-hgin2); _phase:hg-in:hgin2_ |  | needs_review | not stable in 2 calculated diagram(s) | 2 | 2 |
| [LIQUID](#phase-hg-in-liquid); _phase:hg-in:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(In) 0–1 | 12 | 2 |

## RHOMBO_A10 (Hg–In)

- Id: `phase:hg-in:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:a10-rhombo)

Names (4): _corpus: _corpus:phase:hg-in:a10-rhombo  
_paper: _paper:10.1016/j.tca.2009.02.020:Rhombo  
_tdb: _tdb:HgIn-09Gie.tdb:RHOMBO_A10, tdb:HgIn-98Han.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): RHOMBO_A10, type code %, sha256 `6cbb48c284a17292…`

~~~~text
51: PHASE RHOMBO_A10 % 1 1 !
52: CONST RHOMBO_A10 : HG% IN : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): RHOMBO_A10, type code %, sha256 `0316d13b9f5f843a…`

~~~~text
51: PHASE RHOMBO_A10 % 1 1 !
52: CONST RHOMBO_A10 : HG% IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## TETRAGONAL_A6 (Hg–In)

- Id: `phase:hg-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–524.75 K, x(In) 0.94442–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:a6-tetragonal)

Names (3): _corpus: _corpus:phase:hg-in:a6-tetragonal  
_tdb: _tdb:HgIn-09Gie.tdb:TETRAGONAL_A6, tdb:HgIn-98Han.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): TETRAGONAL_A6, type code %, sha256 `6cbb48c284a17292…`

~~~~text
46: PHASE TETRAGONAL_A6 % 1 1 !
47: CONST TETRAGONAL_A6 : HG IN% : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): TETRAGONAL_A6, type code %, sha256 `0316d13b9f5f843a…`

~~~~text
46: PHASE TETRAGONAL_A6 % 1 1 !
47: CONST TETRAGONAL_A6 : HG IN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## BCC_A2 (Hg–In)

- Id: `phase:hg-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:bcc-a2)

Names (3): _corpus: _corpus:phase:hg-in:bcc-a2  
_tdb: _tdb:HgIn-09Gie.tdb:BCC_A2, tdb:HgIn-98Han.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): BCC_A2, type code %B, sha256 `6cbb48c284a17292…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : IN : VA : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): BCC_A2, type code %B, sha256 `0316d13b9f5f843a…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## FCC_A1 (Hg–In)

- Id: `phase:hg-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(In) 0–0.93234
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:fcc-a1)

Names (4): _corpus: _corpus:phase:hg-in:fcc-a1  
_paper: _paper:10.1016/j.tca.2009.02.020:FCC_A1  
_tdb: _tdb:HgIn-09Gie.tdb:FCC_A1, tdb:HgIn-98Han.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): FCC_A1, type code %A, sha256 `6cbb48c284a17292…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HG IN% : VA : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): FCC_A1, type code %A, sha256 `0316d13b9f5f843a…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HG IN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## GAMMA_PU (Hg–In)

- Id: `phase:hg-in:gamma-pu`; status `assigned`
- Structure: gamma-Pu · oF8 · Fddd (70); type `st:gamma-pu-of8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:PU, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:gamma-pu)

Names (4): _corpus: _corpus:phase:hg-in:gamma-pu  
_paper: _paper:10.1016/j.tca.2009.02.020:FCO  
_tdb: _tdb:HgIn-09Gie.tdb:GAMMA_PU, tdb:HgIn-98Han.tdb:GAMMA_PU  


### TDB models of GAMMA_PU (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): GAMMA_PU, type code %, sha256 `6cbb48c284a17292…`

~~~~text
56: PHASE GAMMA_PU % 1 1 !
57: CONST GAMMA_PU : HG IN : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): GAMMA_PU, type code %, sha256 `0316d13b9f5f843a…`

~~~~text
56: PHASE GAMMA_PU % 1 1 !
57: CONST GAMMA_PU : HG IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HCP_A3 (Hg–In)

- Id: `phase:hg-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:hcp-a3)

Names (2): _corpus: _corpus:phase:hg-in:hcp-a3  
_tdb: _tdb:HgIn-98Han.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): HCP_A3, type code %A, sha256 `0316d13b9f5f843a…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : HG IN : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HGIN (Hg–In)

- Id: `phase:hg-in:hgin`; status `assigned`
- Structure: HgIn · hR2 · R-3m (166); type `st:hgin-hr2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 2 calculated diagram(s)
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:hgin)

Names (4): _corpus: _corpus:phase:hg-in:hgin  
_paper: _paper:10.1016/j.tca.2009.02.020:HgIn  
_tdb: _tdb:HgIn-09Gie.tdb:HGIN, tdb:HgIn-98Han.tdb:HGIN  


### TDB models of HGIN (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): HGIN, type code %, sha256 `6cbb48c284a17292…`

~~~~text
61: PHASE HGIN % 2 1 1 !
62: CONST HGIN : HG% IN : HG IN% : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): HGIN, type code %, sha256 `0316d13b9f5f843a…`

~~~~text
61: PHASE HGIN % 2 1 1 !
62: CONST HGIN : HG% IN : HG IN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## HGIN2 (Hg–In)

- Id: `phase:hg-in:hgin2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (HgIn2) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (HgIn2) — Hallstedt 2025 mmc2 row for HGIN2: HgIn2
- Stoichiometry: Hg 0.3333, In 0.6667
- Stability: not stable in 2 calculated diagram(s)
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:hgin2)

Names (4): _corpus: _corpus:phase:hg-in:hgin2  
_paper: _paper:10.1016/j.tca.2009.02.020:HgIn2  
_tdb: _tdb:HgIn-09Gie.tdb:HGIN2, tdb:HgIn-98Han.tdb:HGIN2  


### TDB models of HGIN2 (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): HGIN2, type code %, sha256 `6cbb48c284a17292…`

~~~~text
66: PHASE HGIN2 % 2 1 2 !
67: CONST HGIN2 : HG : IN : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): HGIN2, type code %, sha256 `0316d13b9f5f843a…`

~~~~text
66: PHASE HGIN2 % 2 1 2 !
67: CONST HGIN2 : HG : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
_assessment that models this phase_

## LIQUID (Hg–In)

- Id: `phase:hg-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(In) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-in:liquid)

Names (4): _corpus: _corpus:phase:hg-in:liquid  
_paper: _paper:10.1016/j.tca.2009.02.020:L  
_tdb: _tdb:HgIn-09Gie.tdb:LIQUID, tdb:HgIn-98Han.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HgIn-09Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-09Gie.tdb): LIQUID, type code %, sha256 `6cbb48c284a17292…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : HG IN : !
~~~~

[HgIn-98Han.tdb](https://orchid-project.org/data/databases/sgte-binary/HgIn-98Han.tdb): LIQUID, type code %, sha256 `0316d13b9f5f843a…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : HG IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2009.02.020](https://doi.org/10.1016/j.tca.2009.02.020) Wojcieh Gierlotka, Piotr Jarosz, Sinn-wen Chen, Liquid phase vapor pressure measurement and thermodynamics assessment of the Hg–In binary system, Thermochimica Acta 491, 29-34 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(98)00036-4](https://doi.org/10.1016/S0364-5916%2898%2900036-4) S.C. Hansen, Calphad, 22, 359-73(1998).  
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
