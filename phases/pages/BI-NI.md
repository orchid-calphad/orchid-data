# Bi–Ni phases

> Bi–Ni system: 7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-NI.html · Markdown: https://data.orchid-project.org/phases/pages/BI-NI.md

7 phases (tier A 5, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-NI) · [full JSON](https://data.orchid-project.org/phases/systems/BI-NI.json) · [Bi–Ni system page](https://data.orchid-project.org/systems/BI-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Ni system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-ni-a7-rhombohedral); _phase:bi-ni:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–544.55 K, x(Ni) 0–0 | 34 | 7 |
| [BCC_A2](#phase-bi-ni-bcc-a2); _phase:bi-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [BI3NI](#phase-bi-ni-bi3ni); _phase:bi-ni:bi3ni_ | Bi3Ni · oP16 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 7 of 7 calculated diagram(s): 300–745.59 K, x(Ni) 0.25–0.25 | 80 | 7 |
| [BINI_B81](#phase-bi-ni-bini-b81); _phase:bi-ni:bini-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–924.57 K, x(Ni) 0.47901–0.50003 | 75 | 7 |
| [FCC_A1](#phase-bi-ni-fcc-a1); _phase:bi-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 7 of 7 calculated diagram(s): 300–2499.49 K, x(Ni) 0.97782–1 | 47 | 7 |
| [HCP_A3](#phase-bi-ni-hcp-a3); _phase:bi-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 7 calculated diagram(s) | 0 | 7 |
| [LIQUID](#phase-bi-ni-liquid); _phase:bi-ni:liquid_ | liquid | liquid | stable in 7 of 7 calculated diagram(s): 542.82–2500 K, x(Ni) 0–1 | 127 | 7 |

## RHOMBOHEDRAL_A7 (Bi–Ni)

- Id: `phase:bi-ni:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 7 of 7 calculated diagram(s): 300–544.55 K, x(Ni) 0–0
- Literature: 34 values (34 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:a7-rhombohedral)

Names (14): _corpus: _corpus:phase:bi-ni:a7-rhombohedral, corpus:phase:bi-ni:rhombohedral-a7  
_paper: _paper:10.1002/crat.200800391:(Bi), paper:10.1007/s11664-007-0256-8:(Bi), paper:10.1007/s11664-015-4272-9:(Bi), paper:10.1016/s1003-6326(11)60690-0:rhombohedral (Bi), paper:10.1361/15477030523030:(Bi)  
_tdb: _tdb:BiNi-05Vas.tdb:RHOMBOHEDRAL_A7, tdb:BiNi-07Seo.tdb:RHOMBOHEDRAL_A7, tdb:BiNi-07Vas.tdb:RHOMBOHEDRAL_A7, tdb:BiNi-09Vas.tdb:RHOMBOHEDRAL_A7, tdb:BiNi-11Wan.tdb:RHOMBOHEDRAL_A7, tdb:BiNi-16Liu.tdb:RHOMBOHEDRAL_A7, tdb:BiNi-20Gie.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ad600d039b2e958f…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `8d44fd0da5fd31a5…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `f08f20b79c718bd3…`

~~~~text
49: PHASE RHOMBOHEDRAL_A7 % 1 1 !
50: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `2d2d0758cb2cff93…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dcdf56b33716ef70…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6ee1cd85b3441fba…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (10 of 12; assessments first): 

- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90027-6](https://doi.org/10.1016/0022-5088%2888%2990027-6) P Feschotte, J.-M Rosset, Equilibres de phases dans le systeme binaire nickel-bismuth, Journal of the Less Common Metals 143, 31-37 (1988).  
_cited as the source of values for this phase_
- [doi:10.1051/metal/190805030110](https://doi.org/10.1051/metal/190805030110) A. Portevin, Les alliages de nickel et de bismuth, Rev. Met. Paris 5, 110-120 (1908).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Ni)

- Id: `phase:bi-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:bcc-a2)

Names (8): _corpus: _corpus:phase:bi-ni:bcc-a2  
_tdb: _tdb:BiNi-05Vas.tdb:BCC_A2, tdb:BiNi-07Seo.tdb:BCC_A2, tdb:BiNi-07Vas.tdb:BCC_A2, tdb:BiNi-09Vas.tdb:BCC_A2, tdb:BiNi-11Wan.tdb:BCC_A2, tdb:BiNi-16Liu.tdb:BCC_A2, tdb:BiNi-20Gie.tdb:BCC_A2  


### TDB models of BCC_A2 (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): BCC_A2, type code %B, sha256 `ad600d039b2e958f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI NI : VA : !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): BCC_A2, type code %B, sha256 `8d44fd0da5fd31a5…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BI NI : VA : !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): BCC_A2, type code %B, sha256 `f08f20b79c718bd3…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : BI NI : VA : !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): BCC_A2, type code %B, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BI NI : VA : !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): BCC_A2, type code %B, sha256 `2d2d0758cb2cff93…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : BI NI : VA : !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): BCC_A2, type code %B, sha256 `dcdf56b33716ef70…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BI NI : VA : !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): BCC_A2, type code %B, sha256 `6ee1cd85b3441fba…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : BI NI : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_

## BI3NI (Bi–Ni)

- Id: `phase:bi-ni:bi3ni`; status `assigned`
- Structure: Bi3Ni · oP16 · Pnma (62); type `st:bi3ni-op16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.7500, Ni 0.2500
- Stability: stable in 7 of 7 calculated diagram(s): 300–745.59 K, x(Ni) 0.25–0.25
- Literature: 80 values (80 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:bi3ni)

Names (13): _corpus: _corpus:phase:bi-ni:bi3ni  
_paper: _paper:10.1002/crat.200800391:NiBi3, paper:10.1007/s11664-007-0256-8:NiBi3, paper:10.1007/s11664-015-4272-9:Bi3Ni, paper:10.1016/s1003-6326(11)60690-0:Bi3Ni, paper:10.1361/15477030523030:NiBi3  
_tdb: _tdb:BiNi-05Vas.tdb:BI3NI, tdb:BiNi-07Seo.tdb:BI3NI, tdb:BiNi-07Vas.tdb:BI3NI, tdb:BiNi-09Vas.tdb:BI3NI, tdb:BiNi-11Wan.tdb:BI3NI, tdb:BiNi-16Liu.tdb:BI3NI, tdb:BiNi-20Gie.tdb:BI3NI  


### TDB models of BI3NI (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): BI3NI, type code %, sha256 `ad600d039b2e958f…`

~~~~text
47: PHASE BI3NI % 2 3 1 !
48: CONST BI3NI : BI : NI : !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): BI3NI, type code %, sha256 `8d44fd0da5fd31a5…`

~~~~text
48: PHASE BI3NI % 2 3 1 !
49: CONST BI3NI : BI : NI : !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): BI3NI, type code %, sha256 `f08f20b79c718bd3…`

~~~~text
54: PHASE BI3NI % 2 3 1 !
55: CONST BI3NI : BI : NI : !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): BI3NI, type code %, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
49: PHASE BI3NI % 2 3 1 !
50: CONST BI3NI : BI : NI : !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): BI3NI, type code %, sha256 `2d2d0758cb2cff93…`

~~~~text
53: PHASE BI3NI % 2 3 1 !
54: CONST BI3NI : BI : NI : !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): BI3NI, type code %, sha256 `dcdf56b33716ef70…`

~~~~text
49: PHASE BI3NI % 2 3 1 !
50: CONST BI3NI : BI : NI : !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): BI3NI, type code %, sha256 `6ee1cd85b3441fba…`

~~~~text
48: PHASE BI3NI % 2 3 1 !
49: CONST BI3NI : BI : NI : !
~~~~

Example references (10 of 16; assessments first): 

- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90027-6](https://doi.org/10.1016/0022-5088%2888%2990027-6) P Feschotte, J.-M Rosset, Equilibres de phases dans le systeme binaire nickel-bismuth, Journal of the Less Common Metals 143, 31-37 (1988).  
_cited as the source of values for this phase_
- [doi:10.1051/metal/190805030110](https://doi.org/10.1051/metal/190805030110) A. Portevin, Les alliages de nickel et de bismuth, Rev. Met. Paris 5, 110-120 (1908).  
_cited as the source of values for this phase_

## BINI_B81 (Bi–Ni)

- Id: `phase:bi-ni:bini-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–924.57 K, x(Ni) 0.47901–0.50003
- Literature: 75 values (75 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:bini-b81)

Names (13): _corpus: _corpus:phase:bi-ni:bini-b81  
_paper: _paper:10.1002/crat.200800391:NiBi, paper:10.1007/s11664-007-0256-8:NiBi, paper:10.1007/s11664-015-4272-9:BiNi, paper:10.1016/s1003-6326(11)60690-0:BiNi, paper:10.1361/15477030523030:NiBi  
_tdb: _tdb:BiNi-05Vas.tdb:BINI_B81, tdb:BiNi-07Seo.tdb:BINI_B81, tdb:BiNi-07Vas.tdb:BINI_B81, tdb:BiNi-09Vas.tdb:BINI_B81, tdb:BiNi-11Wan.tdb:BINI_B81, tdb:BiNi-16Liu.tdb:BINI_B81, tdb:BiNi-20Gie.tdb:BINI_B81  


### TDB models of BINI_B81 (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): BINI_B81, type code %, sha256 `ad600d039b2e958f…`

~~~~text
52: PHASE BINI_B81 % 2 1 1 !
53: CONST BINI_B81 : BI : BI NI% : !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): BINI_B81, type code %, sha256 `8d44fd0da5fd31a5…`

~~~~text
53: PHASE BINI_B81 % 3 1 1 1 !
54: CONST BINI_B81 : BI : NI : BI VA% : !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): BINI_B81, type code %, sha256 `f08f20b79c718bd3…`

~~~~text
59: PHASE BINI_B81 % 2 1 1 !
60: CONST BINI_B81 : BI : NI% VA : !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): BINI_B81, type code %, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
54: PHASE BINI_B81 % 3 1 1 1 !
55: CONST BINI_B81 : BI : NI : BI VA% : !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): BINI_B81, type code %, sha256 `2d2d0758cb2cff93…`

~~~~text
58: PHASE BINI_B81 % 3 1 1 1 !
59: CONST BINI_B81 : BI : NI VA : NI VA : !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): BINI_B81, type code %A, sha256 `dcdf56b33716ef70…`

~~~~text
54: PHASE BINI_B81 %A 3 0.3334 0.3333 0.3333 !
55: CONST BINI_B81 : BI : NI VA : NI VA : !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): BINI_B81, type code %, sha256 `6ee1cd85b3441fba…`

~~~~text
53: PHASE BINI_B81 % 3 1 1 1 !
54: CONST BINI_B81 : BI : NI VA : NI VA% : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90027-6](https://doi.org/10.1016/0022-5088%2888%2990027-6) P Feschotte, J.-M Rosset, Equilibres de phases dans le systeme binaire nickel-bismuth, Journal of the Less Common Metals 143, 31-37 (1988).  
_cited as the source of values for this phase_
- [doi:10.1051/metal/190805030110](https://doi.org/10.1051/metal/190805030110) A. Portevin, Les alliages de nickel et de bismuth, Rev. Met. Paris 5, 110-120 (1908).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Ni)

- Id: `phase:bi-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 300–2499.49 K, x(Ni) 0.97782–1
- Literature: 47 values (47 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:fcc-a1)

Names (16): _corpus: _corpus:phase:bi-ni:fcc-a1  
_paper: _paper:10.1002/crat.200800391:(Ni), paper:10.1007/s11664-007-0256-8:fcc, paper:10.1007/s11664-015-4272-9:fcc(Ag), paper:10.1007/s11664-015-4272-9:fcc(Cu), paper:10.1007/s11664-015-4272-9:fcc(Cu,Ni), paper:10.1007/s11664-015-4272-9:fcc(Ni), paper:10.1016/s1003-6326(11)60690-0:fcc(Ni), paper:10.1361/15477030523030:(Ni)  
_tdb: _tdb:BiNi-05Vas.tdb:FCC_A1, tdb:BiNi-07Seo.tdb:FCC_A1, tdb:BiNi-07Vas.tdb:FCC_A1, tdb:BiNi-09Vas.tdb:FCC_A1, tdb:BiNi-11Wan.tdb:FCC_A1, tdb:BiNi-16Liu.tdb:FCC_A1, tdb:BiNi-20Gie.tdb:FCC_A1  


### TDB models of FCC_A1 (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): FCC_A1, type code %A, sha256 `ad600d039b2e958f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI NI% : VA : !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): FCC_A1, type code %A, sha256 `8d44fd0da5fd31a5…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BI NI% : VA : !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): FCC_A1, type code %A, sha256 `f08f20b79c718bd3…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : BI NI% : VA : !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): FCC_A1, type code %A, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BI NI% : VA : !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): FCC_A1, type code %A, sha256 `2d2d0758cb2cff93…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : BI NI% : VA : !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): FCC_A1, type code %A, sha256 `dcdf56b33716ef70…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BI NI% : VA : !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): FCC_A1, type code %A, sha256 `6ee1cd85b3441fba…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : BI NI% : VA : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_
- [doi:10.1557/jmr.2009.0302](https://doi.org/10.1557/jmr.2009.0302) Feng Gao, Cuiping Wang, X.J. Liu, Yoshikazu Takaku, I. Ohnuma, Kiyohito Ishida, Experimental investigation and thermodynamic calculation in the Ag–Bi–Ni and Cu–Bi–Ni systems, J. Mater. Res. 24, 2644-2653 (2009).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_
- [doi:10.1007/s11669-005-0134-0](https://doi.org/10.1007/s11669-005-0134-0) G. P. Vassilev, X. J. Liu, K. Ishida, Experimental studies and thermodynamic optimization of the Ni-Bi system, J Phs Eqil and Diff 26, 161-168 (2005).  
_cited as the source of values for this phase_

## HCP_A3 (Bi–Ni)

- Id: `phase:bi-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 7 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:hcp-a3)

Names (8): _corpus: _corpus:phase:bi-ni:hcp-a3  
_tdb: _tdb:BiNi-05Vas.tdb:HCP_A3, tdb:BiNi-07Seo.tdb:HCP_A3, tdb:BiNi-07Vas.tdb:HCP_A3, tdb:BiNi-09Vas.tdb:HCP_A3, tdb:BiNi-11Wan.tdb:HCP_A3, tdb:BiNi-16Liu.tdb:HCP_A3, tdb:BiNi-20Gie.tdb:HCP_A3  


### TDB models of HCP_A3 (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): HCP_A3, type code %A, sha256 `ad600d039b2e958f…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI NI : VA: !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): HCP_A3, type code %A, sha256 `8d44fd0da5fd31a5…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BI NI : VA: !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): HCP_A3, type code %A, sha256 `f08f20b79c718bd3…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : BI NI : VA: !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): HCP_A3, type code %A, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BI NI : VA: !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): HCP_A3, type code %A, sha256 `2d2d0758cb2cff93…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : BI NI : VA: !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): HCP_A3, type code %A, sha256 `dcdf56b33716ef70…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BI NI : VA: !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): HCP_A3, type code %A, sha256 `6ee1cd85b3441fba…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : BI NI : VA: !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase_
- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_

## LIQUID (Bi–Ni)

- Id: `phase:bi-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 7 of 7 calculated diagram(s): 542.82–2500 K, x(Ni) 0–1
- Literature: 127 values (124 accepted) from 5 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-ni:liquid)

Names (15): _corpus: _corpus:phase:bi-ni:liquid  
_paper: _paper:10.1002/crat.200800391:L, paper:10.1002/crat.200800391:liquid, paper:10.1007/s11664-007-0256-8:L, paper:10.1007/s11664-015-4272-9:L, paper:10.1007/s11664-015-4272-9:Liquid, paper:10.1016/s1003-6326(11)60690-0:L, paper:10.1361/15477030523030:L  
_tdb: _tdb:BiNi-05Vas.tdb:LIQUID, tdb:BiNi-07Seo.tdb:LIQUID, tdb:BiNi-07Vas.tdb:LIQUID, tdb:BiNi-09Vas.tdb:LIQUID, tdb:BiNi-11Wan.tdb:LIQUID, tdb:BiNi-16Liu.tdb:LIQUID, tdb:BiNi-20Gie.tdb:LIQUID  


### TDB models of LIQUID (7): PHASE and CONSTITUENT statements as written

[BiNi-05Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-05Vas.tdb): LIQUID, type code %, sha256 `ad600d039b2e958f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI NI : !
~~~~

[BiNi-07Seo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Seo.tdb): LIQUID, type code %, sha256 `8d44fd0da5fd31a5…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BI NI : !
~~~~

[BiNi-07Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-07Vas.tdb): LIQUID, type code %, sha256 `f08f20b79c718bd3…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : BI NI : !
~~~~

[BiNi-09Vas.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-09Vas.tdb): LIQUID, type code %, sha256 `1bbdd3b0fa5e8e35…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BI NI : !
~~~~

[BiNi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-11Wan.tdb): LIQUID, type code %, sha256 `2d2d0758cb2cff93…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : BI NI : !
~~~~

[BiNi-16Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-16Liu.tdb): LIQUID, type code %, sha256 `dcdf56b33716ef70…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BI NI : !
~~~~

[BiNi-20Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiNi-20Gie.tdb): LIQUID, type code %, sha256 `6ee1cd85b3441fba…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : BI NI : !
~~~~

Example references (10 of 14; assessments first): 

- [doi:10.1007/s11664-015-4272-9](https://doi.org/10.1007/s11664-015-4272-9) Yuling Liu, Shuhong Liu, Cong Zhang, Xingxu Lu, Chong Chen, Yong Du et al., Thermodynamic Assessment of the Bi–Ni and Bi–Ni–X (X = Ag, Cu) Systems, Journal of Elec Materi 45, 1041-1056 (2016).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/crat.200800391](https://doi.org/10.1002/crat.200800391) G. Vassilev, V. Gandova, P. Docheva, Comments and reconciliation of the Ni–Bi‐system thermodynamic reassessments, Cryst. Res. Technol. 44, 25-30 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/15477030523030](https://doi.org/10.1361/15477030523030) G.P. Vassilev, X.J. Liu, K. Ishida, Experimental Studies and Thermodynamic Optimization of the Ni-Bi System, Journal of Phase Equilibria &amp; Diffusion 26, 161-168 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1003-6326(11)60690-0](https://doi.org/10.1016/S1003-6326%2811%2960690-0) J. Wang, F.G. Meng, L.B. Liu, Z.P. Jin, Trans. Nonferrous Met. Soc. China, 21, 139-45(2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-007-0256-8](https://doi.org/10.1007/s11664-007-0256-8) Sun-Kyoung Seo, Moon Gi Cho, Hyuck Mo Lee, Thermodynamic Assessment of the Ni-Bi Binary System and Phase Equilibria of the Sn-Bi-Ni Ternary System, Journal of Elec Materi 36, 1536-1544 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2020.101750](https://doi.org/10.1016/j.calphad.2020.101750) W. Gierlotka, J. Lee, V. Lim, W. Gasior, A. Debski, Calphad, 69, 101750(2020).  
_assessment that models this phase_
- [doi:10.3139/146.101499](https://doi.org/10.3139/146.101499) Gueorgui P. Vassilev, Jolanta Romanowska, Grzegorz Wnuk, Bismuth activity measurements and thermodynamic re-optimization of the Ni–Bi System, International Journal of Materials Research 98, 468-475 (2007).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080570103](https://doi.org/10.1002/zaac.19080570103) G. Voss, Die Legierungen: Nickel‐Zinn, Nickel‐Blei, Nickel‐Thallium, Nickel‐Wismut, Nickel‐Chrom, Nickel‐Magnesium, Nickel‐Zink und Nickel‐Cadmium, Z. Anorg. Chem. 57, 34-71 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90027-6](https://doi.org/10.1016/0022-5088%2888%2990027-6) P Feschotte, J.-M Rosset, Equilibres de phases dans le systeme binaire nickel-bismuth, Journal of the Less Common Metals 143, 31-37 (1988).  
_cited as the source of values for this phase_
- [doi:10.1051/metal/190805030110](https://doi.org/10.1051/metal/190805030110) A. Portevin, Les alliages de nickel et de bismuth, Rev. Met. Paris 5, 110-120 (1908).  
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
