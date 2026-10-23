# Ge–V phases

> Ge–V system: 9 phases (tier A 6, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-V.html · Markdown: https://data.orchid-project.org/phases/pages/GE-V.md

9 phases (tier A 6, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-V) · [full JSON](https://data.orchid-project.org/phases/systems/GE-V.json) · [Ge–V system page](https://data.orchid-project.org/systems/GE-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–V system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-v-a4-diamond); _phase:ge-v:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(V) 0–0 | 6 | 2 |
| [BCC_A2](#phase-ge-v-bcc-a2); _phase:ge-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.83 K, x(V) 0.95323–1 | 6 | 2 |
| [FCC_A1](#phase-ge-v-fcc-a1); _phase:ge-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GE31V17](#phase-ge-v-ge31v17); _phase:ge-v:ge31v17_ | Ge31V17 · tP192 · P-4n2 (118) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1233.33 K, x(V) 0.35417–0.35417 | 8 | 2 |
| [GE3V5_D8M](#phase-ge-v-ge3v5-d8m); _phase:ge-v:ge3v5-d8m_ | W5Si3 · D8_m · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2234 K, x(V) 0.625–0.625 | 12 | 2 |
| [GE8V11](#phase-ge-v-ge8v11); _phase:ge-v:ge8v11_ | Cr11Ge8 · oP76 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1894.8 K, x(V) 0.57895–0.57895 | 8 | 2 |
| [GEV3_A15](#phase-ge-v-gev3-a15); _phase:ge-v:gev3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2193.04 K, x(V) 0.75–0.75 | 12 | 2 |
| [HCP_A3](#phase-ge-v-hcp-a3); _phase:ge-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ge-v-liquid); _phase:ge-v:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1200.82–4000 K, x(V) 0–1 | 32 | 2 |

## DIAMOND_A4 (Ge–V)

- Id: `phase:ge-v:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(V) 0–0
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:a4-diamond)

Names (6): _corpus: _corpus:phase:ge-v:a4-diamond, corpus:phase:ge-v:diamond-a4  
_paper: _paper:10.1016/j.intermet.2008.01.002:(Ge), paper:10.1016/j.tca.2010.11.018:Ge  
_tdb: _tdb:GeV-08Wan.tdb:DIAMOND_A4, tdb:GeV-11Yua.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): DIAMOND_A4, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : GE : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): DIAMOND_A4, type code %, sha256 `b27275b455d680ff…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : GE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Ge–V)

- Id: `phase:ge-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.83 K, x(V) 0.95323–1
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:bcc-a2)

Names (5): _corpus: _corpus:phase:ge-v:bcc-a2  
_paper: _paper:10.1016/j.intermet.2008.01.002:(V), paper:10.1016/j.tca.2010.11.018:(V)  
_tdb: _tdb:GeV-08Wan.tdb:BCC_A2, tdb:GeV-11Yua.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): BCC_A2, type code %B, sha256 `e22a7c5ff3693ca3…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : GE V% : VA : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): BCC_A2, type code %B, sha256 `b27275b455d680ff…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : GE V% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ge–V)

- Id: `phase:ge-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:fcc-a1)

Names (3): _corpus: _corpus:phase:ge-v:fcc-a1  
_tdb: _tdb:GeV-08Wan.tdb:FCC_A1, tdb:GeV-11Yua.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): FCC_A1, type code %A, sha256 `e22a7c5ff3693ca3…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : GE V : VA : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): FCC_A1, type code %A, sha256 `b27275b455d680ff…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : GE V : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase_

## GE31V17 (Ge–V)

- Id: `phase:ge-v:ge31v17`; status `assigned`
- Structure: Ge31V17 · tP192 · P-4n2 (118); type `st:ge31v17-tp192`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.6458, V 0.3542
- Stability: stable in 2 of 2 calculated diagram(s): 300–1233.33 K, x(V) 0.35417–0.35417
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:ge31v17)

Names (5): _corpus: _corpus:phase:ge-v:ge31v17  
_paper: _paper:10.1016/j.intermet.2008.01.002:V17Ge31, paper:10.1016/j.tca.2010.11.018:V17Ge31  
_tdb: _tdb:GeV-08Wan.tdb:GE31V17, tdb:GeV-11Yua.tdb:GE31V17  


### TDB models of GE31V17 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): GE31V17, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
47: PHASE GE31V17 % 2 31 17 !
48: CONST GE31V17 : GE : V : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): GE31V17, type code %, sha256 `b27275b455d680ff…`

~~~~text
47: PHASE GE31V17 % 2 31 17 !
48: CONST GE31V17 : GE : V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

## GE3V5_D8M (Ge–V)

- Id: `phase:ge-v:ge3v5-d8m`; status `assigned`
- Structure: W5Si3 · D8_m · tI32 · I4/mcm (140); type `st:d8-m-w5si3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 0.3750, V 0.6250
- Stability: stable in 2 of 2 calculated diagram(s): 300–2234 K, x(V) 0.625–0.625
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:ge3v5-d8m)

Names (5): _corpus: _corpus:phase:ge-v:ge3v5-d8m  
_paper: _paper:10.1016/j.intermet.2008.01.002:V5Ge3, paper:10.1016/j.tca.2010.11.018:V5Ge3  
_tdb: _tdb:GeV-08Wan.tdb:GE3V5_D8M, tdb:GeV-11Yua.tdb:GE3V5_D8M  


### TDB models of GE3V5_D8M (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): GE3V5_D8M, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
58: PHASE GE3V5_D8M % 2 3 5 !
59: CONST GE3V5_D8M : GE : V : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): GE3V5_D8M, type code %, sha256 `b27275b455d680ff…`

~~~~text
58: PHASE GE3V5_D8M % 2 3 5 !
59: CONST GE3V5_D8M : GE : V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

## GE8V11 (Ge–V)

- Id: `phase:ge-v:ge8v11`; status `assigned`
- Structure: Cr11Ge8 · oP76 · Pnma (62); type `st:cr11ge8-op76`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.4211, V 0.5789
- Stability: stable in 2 of 2 calculated diagram(s): 300–1894.8 K, x(V) 0.57895–0.57895
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:ge8v11)

Names (5): _corpus: _corpus:phase:ge-v:ge8v11  
_paper: _paper:10.1016/j.intermet.2008.01.002:V11Ge8, paper:10.1016/j.tca.2010.11.018:V11Ge8  
_tdb: _tdb:GeV-08Wan.tdb:GE8V11, tdb:GeV-11Yua.tdb:GE8V11  


### TDB models of GE8V11 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): GE8V11, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
52: PHASE GE8V11 % 2 8 11 !
53: CONST GE8V11 : GE : V : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): GE8V11, type code %, sha256 `b27275b455d680ff…`

~~~~text
52: PHASE GE8V11 % 2 8 11 !
53: CONST GE8V11 : GE : V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

## GEV3_A15 (Ge–V)

- Id: `phase:ge-v:gev3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabuz and oqmd-3829, space group 223
- Stoichiometry: Ge 0.2500, V 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–2193.04 K, x(V) 0.75–0.75
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:gev3-a15)

Names (7): _corpus: _corpus:phase:ge-v:gev3-a15  
_mp: _mp:mp-aaaaabuz  
_oqmd: _oqmd:oqmd-3829  
_paper: _paper:10.1016/j.intermet.2008.01.002:V3Ge, paper:10.1016/j.tca.2010.11.018:V3Ge  
_tdb: _tdb:GeV-08Wan.tdb:GEV3_A15, tdb:GeV-11Yua.tdb:GEV3_A15  


### TDB models of GEV3_A15 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): GEV3_A15, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
63: PHASE GEV3_A15 % 2 1 3 !
64: CONST GEV3_A15 : GE : V : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): GEV3_A15, type code %, sha256 `b27275b455d680ff…`

~~~~text
63: PHASE GEV3_A15 % 2 1 3 !
64: CONST GEV3_A15 : GE : V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ge–V)

- Id: `phase:ge-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:hcp-a3)

Names (3): _corpus: _corpus:phase:ge-v:hcp-a3  
_tdb: _tdb:GeV-08Wan.tdb:HCP_A3, tdb:GeV-11Yua.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): HCP_A3, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : GE V : VA : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): HCP_A3, type code %, sha256 `b27275b455d680ff…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : GE V : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase_

## LIQUID (Ge–V)

- Id: `phase:ge-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1200.82–4000 K, x(V) 0–1
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-v:liquid)

Names (5): _corpus: _corpus:phase:ge-v:liquid  
_paper: _paper:10.1016/j.intermet.2008.01.002:L, paper:10.1016/j.tca.2010.11.018:L  
_tdb: _tdb:GeV-08Wan.tdb:LIQUID, tdb:GeV-11Yua.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GeV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-08Wan.tdb): LIQUID, type code %, sha256 `e22a7c5ff3693ca3…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : GE V : !
~~~~

[GeV-11Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/GeV-11Yua.tdb): LIQUID, type code %, sha256 `b27275b455d680ff…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : GE V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2010.11.018](https://doi.org/10.1016/j.tca.2010.11.018) Xiaoming Yuan, Weihua Sun, Yoonsung Chung, Honghui Xu, Shuhong Liu, Yong Du et al., Heat contents of the intermetallics V3Ge and V5Ge3 and thermodynamic modeling of the Ge–V system, Thermochimica Acta 513, 100-105 (2011).  
_assessment that models this phase; reports values for this phase_

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
