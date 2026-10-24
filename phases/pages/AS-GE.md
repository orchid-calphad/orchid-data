# As–Ge phases

> As–Ge system: 8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-GE.html · Markdown: https://data.orchid-project.org/phases/pages/AS-GE.md

8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-GE) · [full JSON](https://data.orchid-project.org/phases/systems/AS-GE.json) · [As–Ge system page](https://data.orchid-project.org/systems/AS-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AS-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Ge system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-as-ge-a4-diamond); _phase:as-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(As) 0–0 | 0 | 3 |
| [RHOMBOHEDRAL_A7](#phase-as-ge-a7-rhombohedral); _phase:as-ge:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1090 K, x(As) 0.78006–1 | 0 | 3 |
| [BCC_A2](#phase-as-ge-bcc-a2); _phase:as-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-as-ge-fcc-a1); _phase:as-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GEAS](#phase-as-ge-geas); _phase:as-ge:geas_ | SiAs · mC24 · C2/m (12) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1036.76 K, x(As) 0.5–0.5 | 11 | 3 |
| [GEAS2](#phase-as-ge-geas2); _phase:as-ge:geas2_ | GeAs2 · oP24 · Pbam (55) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 300–1032.54 K, x(As) 0.66667–0.66667 | 11 | 3 |
| [HCP_A3](#phase-as-ge-hcp-a3); _phase:as-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-as-ge-liquid); _phase:as-ge:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1000.36–2500 K, x(As) 0–1 | 0 | 3 |

## DIAMOND_A4 (As–Ge)

- Id: `phase:as-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1211.4 K, x(As) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:a4-diamond)

Names (4): _corpus: _corpus:phase:as-ge:a4-diamond  
_tdb: _tdb:GeAs-21Wu.tdb:DIAMOND_A4, tdb:GeAs-22Che.tdb:DIAMOND_A4, tdb:GeAs-84Ans-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): DIAMOND_A4, type code %, sha256 `75aaefb0863ae898…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : GE : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): DIAMOND_A4, type code %, sha256 `235bd45af2ef5f66…`

~~~~text
40: PHASE DIAMOND_A4 % 1 1 !
41: CONST DIAMOND_A4 : GE : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): DIAMOND_A4, type code %, sha256 `715c9b2473ae9102…`

~~~~text
51: PHASE DIAMOND_A4 % 1 1 !
52: CONST DIAMOND_A4 : GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (As–Ge)

- Id: `phase:as-ge:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1090 K, x(As) 0.78006–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:as-ge:a7-rhombohedral  
_tdb: _tdb:GeAs-21Wu.tdb:RHOMBOHEDRAL_A7, tdb:GeAs-22Che.tdb:RHOMBOHEDRAL_A7, tdb:GeAs-84Ans-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `75aaefb0863ae898…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : AS% GE : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `235bd45af2ef5f66…`

~~~~text
45: PHASE RHOMBOHEDRAL_A7 % 1 1 !
46: CONST RHOMBOHEDRAL_A7 : AS% GE : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `715c9b2473ae9102…`

~~~~text
56: PHASE RHOMBOHEDRAL_A7 % 1 1 !
57: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## BCC_A2 (As–Ge)

- Id: `phase:as-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:bcc-a2)

Names (4): _corpus: _corpus:phase:as-ge:bcc-a2  
_tdb: _tdb:GeAs-21Wu.tdb:BCC_A2, tdb:GeAs-22Che.tdb:BCC_A2, tdb:GeAs-84Ans-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): BCC_A2, type code %B, sha256 `75aaefb0863ae898…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AS GE : VA : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): BCC_A2, type code %B, sha256 `235bd45af2ef5f66…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AS GE : VA : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): BCC_A2, type code %B, sha256 `715c9b2473ae9102…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : AS GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## FCC_A1 (As–Ge)

- Id: `phase:as-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:fcc-a1)

Names (4): _corpus: _corpus:phase:as-ge:fcc-a1  
_tdb: _tdb:GeAs-21Wu.tdb:FCC_A1, tdb:GeAs-22Che.tdb:FCC_A1, tdb:GeAs-84Ans-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): FCC_A1, type code %A, sha256 `75aaefb0863ae898…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AS GE : VA : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): FCC_A1, type code %A, sha256 `235bd45af2ef5f66…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AS GE : VA : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): FCC_A1, type code %A, sha256 `715c9b2473ae9102…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : AS GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## GEAS (As–Ge)

- Id: `phase:as-ge:geas`; status `assigned`
- Structure: SiAs · mC24 · C2/m (12); type `st:sias-mc24`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: As 0.5000, Ge 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–1036.76 K, x(As) 0.5–0.5
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:geas)

Names (7): _corpus: _corpus:phase:as-ge:geas  
_mp: _mp:mp-aaaaaodg  
_oqmd: _oqmd:oqmd-15392  
_paper: _paper:10.1007/s11664-022-09474-1:GeAs  
_tdb: _tdb:GeAs-21Wu.tdb:GEAS, tdb:GeAs-22Che.tdb:GEAS, tdb:GeAs-84Ans-LB.tdb:GEAS  


### TDB models of GEAS (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): GEAS, type code %, sha256 `75aaefb0863ae898…`

~~~~text
52: PHASE GEAS % 2 1 1 !
53: CONST GEAS : GE : AS : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): GEAS, type code %, sha256 `235bd45af2ef5f66…`

~~~~text
50: PHASE GEAS % 2 1 1 !
51: CONST GEAS : GE : AS : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): GEAS, type code %, sha256 `715c9b2473ae9102…`

~~~~text
61: PHASE GEAS % 2 1 1 !
62: CONST GEAS : GE : AS : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_
- [doi:10.3891/acta.chem.scand.21-0593](https://doi.org/10.3891/acta.chem.scand.21-0593) Tommy Wadsten, M. Vikan, C. Krohn, Åke Nilsson, H. Theorell, R. Blinc et al., The Crystal Structures of SiP2, SiAs2, and GeP., Acta Chem. Scand. 21, 593-594 (1967).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)02186-8](https://doi.org/10.1016/0925-8388%2895%2902186-8) K. Fitzner, O.J. Kleppa, Direct synthesis calorimetry of some binary alloys in the systems SiAs, GeAs and SnAs, Journal of Alloys and Compounds 238, 187-192 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/s0021-9614(71)80107-6](https://doi.org/10.1016/s0021-9614%2871%2980107-6) R. Blachnik, A. Schneider, High-temperature enthalpies of As2Te3, Sb2Se3, Bi2Se3, GeAs, GeAs2, and SnAs, The Journal of Chemical Thermodynamics 3, 227-233 (1971).  
_cited as the source of values for this phase_

## GEAS2 (As–Ge)

- Id: `phase:as-ge:geas2`; status `assigned`
- Structure: GeAs2 · oP24 · Pbam (55); type `st:geas2-op24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_55_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: As 0.6667, Ge 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–1032.54 K, x(As) 0.66667–0.66667
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:geas2)

Names (5): _corpus: _corpus:phase:as-ge:geas2  
_paper: _paper:10.1007/s11664-022-09474-1:GeAs2  
_tdb: _tdb:GeAs-21Wu.tdb:GEAS2, tdb:GeAs-22Che.tdb:GEAS2, tdb:GeAs-84Ans-LB.tdb:GEAS2  


### TDB models of GEAS2 (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): GEAS2, type code %, sha256 `75aaefb0863ae898…`

~~~~text
57: PHASE GEAS2 % 2 1 2 !
58: CONST GEAS2 : GE : AS : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): GEAS2, type code %, sha256 `235bd45af2ef5f66…`

~~~~text
55: PHASE GEAS2 % 2 1 2 !
56: CONST GEAS2 : GE : AS : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): GEAS2, type code %, sha256 `715c9b2473ae9102…`

~~~~text
66: PHASE GEAS2 % 2 1 2 !
67: CONST GEAS2 : GE : AS : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_
- [doi:10.1107/s0365110x62000407](https://doi.org/10.1107/s0365110x62000407) J. H. Bryden, The crystal structures of the germanium–arsenic compounds: I. Germanium diarsenide, GeAs\<sub>2\</sub>, Acta Cryst 15, 167-171 (1962).  
_cited as the source of values for this phase_
- [doi:10.1016/0925-8388(95)02186-8](https://doi.org/10.1016/0925-8388%2895%2902186-8) K. Fitzner, O.J. Kleppa, Direct synthesis calorimetry of some binary alloys in the systems SiAs, GeAs and SnAs, Journal of Alloys and Compounds 238, 187-192 (1996).  
_cited as the source of values for this phase_
- [doi:10.1016/s0021-9614(71)80107-6](https://doi.org/10.1016/s0021-9614%2871%2980107-6) R. Blachnik, A. Schneider, High-temperature enthalpies of As2Te3, Sb2Se3, Bi2Se3, GeAs, GeAs2, and SnAs, The Journal of Chemical Thermodynamics 3, 227-233 (1971).  
_cited as the source of values for this phase_

## HCP_A3 (As–Ge)

- Id: `phase:as-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:hcp-a3)

Names (4): _corpus: _corpus:phase:as-ge:hcp-a3  
_tdb: _tdb:GeAs-21Wu.tdb:HCP_A3, tdb:GeAs-22Che.tdb:HCP_A3, tdb:GeAs-84Ans-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): HCP_A3, type code %A, sha256 `75aaefb0863ae898…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AS GE : VA : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): HCP_A3, type code %A, sha256 `235bd45af2ef5f66…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AS GE : VA : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): HCP_A3, type code %A, sha256 `715c9b2473ae9102…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : AS GE : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

## LIQUID (As–Ge)

- Id: `phase:as-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1000.36–2500 K, x(As) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-ge:liquid)

Names (4): _corpus: _corpus:phase:as-ge:liquid  
_tdb: _tdb:GeAs-21Wu.tdb:LIQUID, tdb:GeAs-22Che.tdb:LIQUID, tdb:GeAs-84Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[GeAs-21Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-21Wu.tdb): LIQUID, type code %, sha256 `75aaefb0863ae898…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AS GE : !
~~~~

[GeAs-22Che.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-22Che.tdb): LIQUID, type code %, sha256 `235bd45af2ef5f66…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AS GE : !
~~~~

[GeAs-84Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeAs-84Ans-LB.tdb): LIQUID, type code %, sha256 `715c9b2473ae9102…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : AS GE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11664-022-09474-1](https://doi.org/10.1007/s11664-022-09474-1) Shanxiong Chen, Jiong Wang, Shangzhao Yu, Biao Hu, Qing Wu, Yong Du, Thermodynamic Modeling of the Ge-X (X = As, Se, S, P) Systems, J. Electron. Mater. 51, 2114-2130 (2022).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(84)90035-X](https://doi.org/10.1016/0364-5916%2884%2990035-X) I. Ansara, D. Dutartre, Calphad, 8, 323-42(1984).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2021.102296](https://doi.org/10.1016/j.calphad.2021.102296) L. Wu, Y. Du, M. Premovic, B. Hu, H. Zhang, J. Wang, Y. Liu, Calphad, 74, 102296(2021).  
_assessment that models this phase_

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
