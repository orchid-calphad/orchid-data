# Ge–Sb phases

> Ge–Sb system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-SB.html · Markdown: https://data.orchid-project.org/phases/pages/GE-SB.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-SB) · [full JSON](https://data.orchid-project.org/phases/systems/GE-SB.json) · [Ge–Sb system page](https://data.orchid-project.org/systems/GE-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Sb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-sb-a4-diamond); _phase:ge-sb:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1211.4 K, x(Sb) 0–0.00031 | 7 | 4 |
| [RHOMBOHEDRAL_A7](#phase-ge-sb-a7-rhombohedral); _phase:ge-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1428.78 K, x(Sb) 0.93753–1 | 7 | 4 |
| [BCC_A2](#phase-ge-sb-bcc-a2); _phase:ge-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-ge-sb-fcc-a1); _phase:ge-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-ge-sb-hcp-a3); _phase:ge-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-ge-sb-liquid); _phase:ge-sb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 854.35–2500 K, x(Sb) 0–1 | 12 | 4 |

## DIAMOND_A4 (Ge–Sb)

- Id: `phase:ge-sb:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1211.4 K, x(Sb) 0–0.00031
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sb:a4-diamond)

Names (7): _corpus: _corpus:phase:ge-sb:a4-diamond, corpus:phase:ge-sb:diamond-a4  
_paper: _paper:10.1016/j.tca.2011.03.008:diamond  
_tdb: _tdb:GeSb-09Wan.tdb:DIAMOND_A4, tdb:GeSb-11Liu.tdb:DIAMOND_A4, tdb:GeSb-89Che-LB.tdb:DIAMOND_A4, tdb:GeSb-99Sch.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (4): PHASE and CONSTITUENT statements as written

[GeSb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-09Wan.tdb): DIAMOND_A4, type code %, sha256 `dea266b7c521d694…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : GE% SB : !
~~~~

[GeSb-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-11Liu.tdb): DIAMOND_A4, type code %, sha256 `de4f32c2b1c6e2c2…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : GE% SB : !
~~~~

[GeSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-89Che-LB.tdb): DIAMOND_A4, type code %, sha256 `6f34fa372184c8f1…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : GE% SB : !
~~~~

[GeSb-99Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-99Sch.tdb): DIAMOND_A4, type code %, sha256 `dd406e1392cfa749…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : GE% SB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.tca.2011.03.008](https://doi.org/10.1016/j.tca.2011.03.008) Jinming Liu, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Ge–Sb and Ge–Sb–Sn systems, Thermochimica Acta 520, 38-47 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87148-5](https://doi.org/10.1016/0040-6031%2889%2987148-5) Pierre-Yves Chewvalier, A thermodynamic evaluation of the Ge-In, Ge-Pb, Ge-Sb, Ge-Tl and Ge-Zn systems, Thermochimica Acta 155, 227-240 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.06.030](https://doi.org/10.1016/j.jallcom.2009.06.030) J. Wang, C. Leinenbach, M. Roth, Thermodynamic description of the Au–Ge–Sb ternary system, Journal of Alloys and Compounds 485, 577-582 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1515/ijmr-1999-900703](https://doi.org/10.1515/ijmr-1999-900703) A. Schlieper, R. Blachnik, Z. Metallkd., 90, 475-85(1999).  
_assessment that models this phase_
- [doi:10.1002/zaac.19402440211](https://doi.org/10.1002/zaac.19402440211) Herbert Stöhr, Wilhelm Klemm, Über Zweistoffsysteme mit Germanium. II. Germanium/Arsen, Germanium/Antimon, Germanium/Wismut, Z. Anorg. Allg. Chem. 244, 205-223 (1940).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868990](https://doi.org/10.1007/bf02868990) R.W. Olesinski, G.J. Abbaschian, The Ge–Sb system, Bull. Alloy Phase Diagrams 7 (1986) 219–222.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2008.12.009](https://doi.org/10.1016/j.jssc.2008.12.009) Navida Nasir, Andriy Grytsiv, Peter Rogl, Adriana Saccone, Gerald Giester, Phase equilibria in systems Ce–M–Sb (M=Si, Ge, Sn) and superstructure Ce12Ge9−xSb23+x (x=3.8±0.1), Journal of Solid State Chemistry 182, 645-656 (2009).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1940-320302](https://doi.org/10.1515/ijmr-1940-320302) K. Ruttewit, G. Masing, On the alloys of germanium with bismuth, antimony, iron and nickel, Z. Metallkd. 32 (1940) 52–61.  
_cited as the source of values for this phase_

## RHOMBOHEDRAL_A7 (Ge–Sb)

- Id: `phase:ge-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1428.78 K, x(Sb) 0.93753–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sb:a7-rhombohedral)

Names (7): _corpus: _corpus:phase:ge-sb:a7-rhombohedral, corpus:phase:ge-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.tca.2011.03.008:rhom  
_tdb: _tdb:GeSb-09Wan.tdb:RHOMBOHEDRAL_A7, tdb:GeSb-11Liu.tdb:RHOMBOHEDRAL_A7, tdb:GeSb-89Che-LB.tdb:RHOMBOHEDRAL_A7, tdb:GeSb-99Sch.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (4): PHASE and CONSTITUENT statements as written

[GeSb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-09Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dea266b7c521d694…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : GE SB% : !
~~~~

[GeSb-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-11Liu.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `de4f32c2b1c6e2c2…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : GE SB% : !
~~~~

[GeSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-89Che-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `6f34fa372184c8f1…`

~~~~text
49: PHASE RHOMBOHEDRAL_A7 % 1 1 !
50: CONST RHOMBOHEDRAL_A7 : GE SB% : !
~~~~

[GeSb-99Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-99Sch.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `dd406e1392cfa749…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.tca.2011.03.008](https://doi.org/10.1016/j.tca.2011.03.008) Jinming Liu, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Ge–Sb and Ge–Sb–Sn systems, Thermochimica Acta 520, 38-47 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87148-5](https://doi.org/10.1016/0040-6031%2889%2987148-5) Pierre-Yves Chewvalier, A thermodynamic evaluation of the Ge-In, Ge-Pb, Ge-Sb, Ge-Tl and Ge-Zn systems, Thermochimica Acta 155, 227-240 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1016/j.jallcom.2009.06.030](https://doi.org/10.1016/j.jallcom.2009.06.030) J. Wang, C. Leinenbach, M. Roth, Thermodynamic description of the Au–Ge–Sb ternary system, Journal of Alloys and Compounds 485, 577-582 (2009).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1515/ijmr-1999-900703](https://doi.org/10.1515/ijmr-1999-900703) A. Schlieper, R. Blachnik, Z. Metallkd., 90, 475-85(1999).  
_assessment that models this phase_
- [doi:10.1002/zaac.19402440211](https://doi.org/10.1002/zaac.19402440211) Herbert Stöhr, Wilhelm Klemm, Über Zweistoffsysteme mit Germanium. II. Germanium/Arsen, Germanium/Antimon, Germanium/Wismut, Z. Anorg. Allg. Chem. 244, 205-223 (1940).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02868990](https://doi.org/10.1007/bf02868990) R.W. Olesinski, G.J. Abbaschian, The Ge–Sb system, Bull. Alloy Phase Diagrams 7 (1986) 219–222.  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2008.12.009](https://doi.org/10.1016/j.jssc.2008.12.009) Navida Nasir, Andriy Grytsiv, Peter Rogl, Adriana Saccone, Gerald Giester, Phase equilibria in systems Ce–M–Sb (M=Si, Ge, Sn) and superstructure Ce12Ge9−xSb23+x (x=3.8±0.1), Journal of Solid State Chemistry 182, 645-656 (2009).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1940-320302](https://doi.org/10.1515/ijmr-1940-320302) K. Ruttewit, G. Masing, On the alloys of germanium with bismuth, antimony, iron and nickel, Z. Metallkd. 32 (1940) 52–61.  
_cited as the source of values for this phase_

## BCC_A2 (Ge–Sb)

- Id: `phase:ge-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sb:bcc-a2)

Names (5): _corpus: _corpus:phase:ge-sb:bcc-a2  
_tdb: _tdb:GeSb-09Wan.tdb:BCC_A2, tdb:GeSb-11Liu.tdb:BCC_A2, tdb:GeSb-89Che-LB.tdb:BCC_A2, tdb:GeSb-99Sch.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[GeSb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-09Wan.tdb): BCC_A2, type code %, sha256 `dea266b7c521d694…`

~~~~text
29: PHASE BCC_A2 % 2 1 3 !
30: CONST BCC_A2 : GE SB : VA : !
~~~~

[GeSb-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-11Liu.tdb): BCC_A2, type code %, sha256 `de4f32c2b1c6e2c2…`

~~~~text
29: PHASE BCC_A2 % 2 1 3 !
30: CONST BCC_A2 : GE SB : VA : !
~~~~

[GeSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-89Che-LB.tdb): BCC_A2, type code %, sha256 `6f34fa372184c8f1…`

~~~~text
34: PHASE BCC_A2 % 2 1 3 !
35: CONST BCC_A2 : GE SB : VA : !
~~~~

[GeSb-99Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-99Sch.tdb): BCC_A2, type code %, sha256 `dd406e1392cfa749…`

~~~~text
29: PHASE BCC_A2 % 2 1 3 !
30: CONST BCC_A2 : GE SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(89)87148-5](https://doi.org/10.1016/0040-6031%2889%2987148-5) Pierre-Yves Chewvalier, A thermodynamic evaluation of the Ge-In, Ge-Pb, Ge-Sb, Ge-Tl and Ge-Zn systems, Thermochimica Acta 155, 227-240 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.06.030](https://doi.org/10.1016/j.jallcom.2009.06.030) J. Wang, C. Leinenbach, M. Roth, Thermodynamic description of the Au–Ge–Sb ternary system, Journal of Alloys and Compounds 485, 577-582 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.03.008](https://doi.org/10.1016/j.tca.2011.03.008) Jinming Liu, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Ge–Sb and Ge–Sb–Sn systems, Thermochimica Acta 520, 38-47 (2011).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900703](https://doi.org/10.1515/ijmr-1999-900703) A. Schlieper, R. Blachnik, Z. Metallkd., 90, 475-85(1999).  
_assessment that models this phase_

## FCC_A1 (Ge–Sb)

- Id: `phase:ge-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sb:fcc-a1)

Names (5): _corpus: _corpus:phase:ge-sb:fcc-a1  
_tdb: _tdb:GeSb-09Wan.tdb:FCC_A1, tdb:GeSb-11Liu.tdb:FCC_A1, tdb:GeSb-89Che-LB.tdb:FCC_A1, tdb:GeSb-99Sch.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[GeSb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-09Wan.tdb): FCC_A1, type code %, sha256 `dea266b7c521d694…`

~~~~text
24: PHASE FCC_A1 % 2 1 1 !
25: CONST FCC_A1 : GE SB : VA : !
~~~~

[GeSb-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-11Liu.tdb): FCC_A1, type code %, sha256 `de4f32c2b1c6e2c2…`

~~~~text
24: PHASE FCC_A1 % 2 1 1 !
25: CONST FCC_A1 : GE SB : VA : !
~~~~

[GeSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-89Che-LB.tdb): FCC_A1, type code %, sha256 `6f34fa372184c8f1…`

~~~~text
29: PHASE FCC_A1 % 2 1 1 !
30: CONST FCC_A1 : GE SB : VA : !
~~~~

[GeSb-99Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-99Sch.tdb): FCC_A1, type code %, sha256 `dd406e1392cfa749…`

~~~~text
24: PHASE FCC_A1 % 2 1 1 !
25: CONST FCC_A1 : GE SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(89)87148-5](https://doi.org/10.1016/0040-6031%2889%2987148-5) Pierre-Yves Chewvalier, A thermodynamic evaluation of the Ge-In, Ge-Pb, Ge-Sb, Ge-Tl and Ge-Zn systems, Thermochimica Acta 155, 227-240 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.06.030](https://doi.org/10.1016/j.jallcom.2009.06.030) J. Wang, C. Leinenbach, M. Roth, Thermodynamic description of the Au–Ge–Sb ternary system, Journal of Alloys and Compounds 485, 577-582 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.03.008](https://doi.org/10.1016/j.tca.2011.03.008) Jinming Liu, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Ge–Sb and Ge–Sb–Sn systems, Thermochimica Acta 520, 38-47 (2011).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900703](https://doi.org/10.1515/ijmr-1999-900703) A. Schlieper, R. Blachnik, Z. Metallkd., 90, 475-85(1999).  
_assessment that models this phase_

## HCP_A3 (Ge–Sb)

- Id: `phase:ge-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sb:hcp-a3)

Names (5): _corpus: _corpus:phase:ge-sb:hcp-a3  
_tdb: _tdb:GeSb-09Wan.tdb:HCP_A3, tdb:GeSb-11Liu.tdb:HCP_A3, tdb:GeSb-89Che-LB.tdb:HCP_A3, tdb:GeSb-99Sch.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[GeSb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-09Wan.tdb): HCP_A3, type code %, sha256 `dea266b7c521d694…`

~~~~text
34: PHASE HCP_A3 % 2 1 0.5 !
35: CONST HCP_A3 : GE SB : VA: !
~~~~

[GeSb-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-11Liu.tdb): HCP_A3, type code %, sha256 `de4f32c2b1c6e2c2…`

~~~~text
34: PHASE HCP_A3 % 2 1 0.5 !
35: CONST HCP_A3 : GE SB : VA: !
~~~~

[GeSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-89Che-LB.tdb): HCP_A3, type code %, sha256 `6f34fa372184c8f1…`

~~~~text
39: PHASE HCP_A3 % 2 1 0.5 !
40: CONST HCP_A3 : GE SB : VA: !
~~~~

[GeSb-99Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-99Sch.tdb): HCP_A3, type code %, sha256 `dd406e1392cfa749…`

~~~~text
34: PHASE HCP_A3 % 2 1 0.5 !
35: CONST HCP_A3 : GE SB : VA: !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(89)87148-5](https://doi.org/10.1016/0040-6031%2889%2987148-5) Pierre-Yves Chewvalier, A thermodynamic evaluation of the Ge-In, Ge-Pb, Ge-Sb, Ge-Tl and Ge-Zn systems, Thermochimica Acta 155, 227-240 (1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.06.030](https://doi.org/10.1016/j.jallcom.2009.06.030) J. Wang, C. Leinenbach, M. Roth, Thermodynamic description of the Au–Ge–Sb ternary system, Journal of Alloys and Compounds 485, 577-582 (2009).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2011.03.008](https://doi.org/10.1016/j.tca.2011.03.008) Jinming Liu, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Ge–Sb and Ge–Sb–Sn systems, Thermochimica Acta 520, 38-47 (2011).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1999-900703](https://doi.org/10.1515/ijmr-1999-900703) A. Schlieper, R. Blachnik, Z. Metallkd., 90, 475-85(1999).  
_assessment that models this phase_

## LIQUID (Ge–Sb)

- Id: `phase:ge-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 854.35–2500 K, x(Sb) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-sb:liquid)

Names (7): _corpus: _corpus:phase:ge-sb:liquid  
_paper: _paper:10.1016/j.jallcom.2009.06.030:L, paper:10.1016/j.tca.2011.03.008:Liq.  
_tdb: _tdb:GeSb-09Wan.tdb:LIQUID, tdb:GeSb-11Liu.tdb:LIQUID, tdb:GeSb-89Che-LB.tdb:LIQUID, tdb:GeSb-99Sch.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[GeSb-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-09Wan.tdb): LIQUID, type code %, sha256 `dea266b7c521d694…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : GE SB : !
~~~~

[GeSb-11Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-11Liu.tdb): LIQUID, type code %, sha256 `de4f32c2b1c6e2c2…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : GE SB : !
~~~~

[GeSb-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-89Che-LB.tdb): LIQUID, type code %, sha256 `6f34fa372184c8f1…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GE SB : !
~~~~

[GeSb-99Sch.tdb](https://orchid-project.org/data/databases/sgte-binary/GeSb-99Sch.tdb): LIQUID, type code %, sha256 `dd406e1392cfa749…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : GE SB : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.tca.2011.03.008](https://doi.org/10.1016/j.tca.2011.03.008) Jinming Liu, Cuiping Guo, Changrong Li, Zhenmin Du, Thermodynamic optimization of the Ge–Sb and Ge–Sb–Sn systems, Thermochimica Acta 520, 38-47 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2009.06.030](https://doi.org/10.1016/j.jallcom.2009.06.030) J. Wang, C. Leinenbach, M. Roth, Thermodynamic description of the Au–Ge–Sb ternary system, Journal of Alloys and Compounds 485, 577-582 (2009).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87148-5](https://doi.org/10.1016/0040-6031%2889%2987148-5) Pierre-Yves Chewvalier, A thermodynamic evaluation of the Ge-In, Ge-Pb, Ge-Sb, Ge-Tl and Ge-Zn systems, Thermochimica Acta 155, 227-240 (1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1515/ijmr-1999-900703](https://doi.org/10.1515/ijmr-1999-900703) A. Schlieper, R. Blachnik, Z. Metallkd., 90, 475-85(1999).  
_assessment that models this phase_
- [doi:10.1007/bf02868990](https://doi.org/10.1007/bf02868990) R.W. Olesinski, G.J. Abbaschian, The Ge–Sb system, Bull. Alloy Phase Diagrams 7 (1986) 219–222.  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19402440211](https://doi.org/10.1002/zaac.19402440211) Herbert Stöhr, Wilhelm Klemm, Über Zweistoffsysteme mit Germanium. II. Germanium/Arsen, Germanium/Antimon, Germanium/Wismut, Z. Anorg. Allg. Chem. 244, 205-223 (1940).  
_cited as the source of values for this phase_
- [doi:10.1016/j.jssc.2008.12.009](https://doi.org/10.1016/j.jssc.2008.12.009) Navida Nasir, Andriy Grytsiv, Peter Rogl, Adriana Saccone, Gerald Giester, Phase equilibria in systems Ce–M–Sb (M=Si, Ge, Sn) and superstructure Ce12Ge9−xSb23+x (x=3.8±0.1), Journal of Solid State Chemistry 182, 645-656 (2009).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1940-320302](https://doi.org/10.1515/ijmr-1940-320302) K. Ruttewit, G. Masing, On the alloys of germanium with bismuth, antimony, iron and nickel, Z. Metallkd. 32 (1940) 52–61.  
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
