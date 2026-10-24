# Ni–Sb phases

> Ni–Sb system: 11 phases (tier A 7, liquid 1, needs_review 2, unresolved_no_candidates 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-SB.html · Markdown: https://data.orchid-project.org/phases/pages/NI-SB.md

11 phases (tier A 7, liquid 1, needs_review 2, unresolved_no_candidates 1); 9 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-SB) · [full JSON](https://data.orchid-project.org/phases/systems/NI-SB.json) · [Ni–Sb system page](https://data.orchid-project.org/systems/NI-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Sb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-ni-sb-a7-rhombohedral); _phase:ni-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–903.56 K, x(Sb) 1–1 | 10 | 4 |
| [BCC_A2](#phase-ni-sb-bcc-a2); _phase:ni-sb:bcc-a2_ |  | needs_review | stable in 1 of 4 calculated diagram(s): 803.04–1413.04 K, x(Sb) 0.24453–0.29057 | 52 | 4 |
| [FCC_A1](#phase-ni-sb-fcc-a1); _phase:ni-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1730.24 K, x(Sb) 0–0.10338 | 27 | 4 |
| [HCP_A3](#phase-ni-sb-hcp-a3); _phase:ni-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-ni-sb-liquid); _phase:ni-sb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 890.32–2500 K, x(Sb) 0–1 | 73 | 4 |
| [NI3SB_D03](#phase-ni-sb-ni3sb-d03); _phase:ni-sb:ni3sb-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 802.63–1444.23 K, x(Sb) 0.25493–0.29478 | 26 | 3 |
| [NI3SB_D0A](#phase-ni-sb-ni3sb-d0a); _phase:ni-sb:ni3sb-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–990 K, x(Sb) 0.23685–0.25 | 22 | 4 |
| [NI5SB2_LT](#phase-ni-sb-ni5sb2); _phase:ni-sb:ni5sb2_ |  | needs_review | stable in 4 of 4 calculated diagram(s): 300–884.35 K, x(Sb) 0.27394–0.28571 | 18 | 4 |
| [NI5SB2-LT](#phase-ni-sb-ni5sb2-lt); _phase:ni-sb:ni5sb2-lt_ |  | unresolved_no_candidates | no calculated diagram | 0 | 0 |
| [NISB_B81](#phase-ni-sb-nisb-b81); _phase:ni-sb:nisb-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2500 K, x(Sb) 0.43752–0.54484 | 50 | 4 |
| [NISB2_C18](#phase-ni-sb-nisb2-c18); _phase:ni-sb:nisb2-c18_ | alpha-FeS2 · C18 · oP6 · Pnnm (58) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–901.22 K, x(Sb) 0.66667–0.66667 | 22 | 4 |

## RHOMBOHEDRAL_A7 (Ni–Sb)

- Id: `phase:ni-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 4 of 4 calculated diagram(s): 300–903.56 K, x(Sb) 1–1
- Literature: 10 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:a7-rhombohedral)

Names (8): _corpus: _corpus:phase:ni-sb:a7-rhombohedral, corpus:phase:ni-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2008.02.001:εSb, paper:10.1016/s1001-0521(08)60150-3:rhomb (Sb)  
_tdb: _tdb:NiSb-08Cao.tdb:RHOMBOHEDRAL_A7, tdb:NiSb-08Zha.tdb:RHOMBOHEDRAL_A7, tdb:NiSb-13Cao.tdb:RHOMBOHEDRAL_A7, tdb:NiSb-14Kro.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
50: PHASE RHOMBOHEDRAL_A7 % 1 1 !
51: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `1ab705f632704a07…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `15754b2a707f1c85…`

~~~~text
49: PHASE RHOMBOHEDRAL_A7 % 1 1 !
50: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_

## BCC_A2 (Ni–Sb)

- Id: `phase:ni-sb:bcc-a2`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:BCC_A2
- Candidate (dft_mp): C2/m (12) — on-hull MP Ni5Sb2 at x(SB)=0.2857
- Candidate (dft_oqmd): Pmmn (59) — on-hull OQMD Ni3 Sb1 at x(SB)=0.2500
- Candidate (dft_oqmd): C2 (5) — on-hull OQMD Ni5 Sb2 at x(SB)=0.2857
- Candidate (literature_printed): BiF3 · cF16 — printed with a label mapped to this phase
- Candidate (name_token): W · A2 · cI2 · Im-3m (229) — Strukturbericht/word 'A2' in the TDB name
- Candidate (sgte_mmc2): BiF3 · D0_3 · cF16 · Fm-3m (225) — Hallstedt 2025 mmc2 row for BCC_A2: Ni3Sb (high T), Ni3Sn (high T)
- Stability: stable in 1 of 4 calculated diagram(s): 803.04–1413.04 K, x(Sb) 0.24453–0.29057
- Literature: 52 values (52 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:bcc-a2)

Names (8): _corpus: _corpus:phase:ni-sb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2008.02.001:(β'Ni5Sb2), paper:10.1016/j.calphad.2008.02.001:(βNi3Sb), paper:10.1016/j.calphad.2008.02.001:(βNi5Sb2)  
_tdb: _tdb:NiSb-08Cao.tdb:BCC_A2, tdb:NiSb-08Zha.tdb:BCC_A2, tdb:NiSb-13Cao.tdb:BCC_A2, tdb:NiSb-14Kro.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): BCC_A2, type code %B, sha256 `c50b9c6a21205dfe…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : NI SB : VA : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): BCC_A2, type code %B, sha256 `1ab705f632704a07…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NI SB : VA : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): BCC_A2, type code %B, sha256 `57b2cd3fde2a4256…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : NI SB : VA : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): BCC_A2, type code %B, sha256 `15754b2a707f1c85…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : NI SB : VA : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19865330226](https://doi.org/10.1002/zaac.19865330226) Robert Leubolt, Herbert Ipser, Peter Terzieff, Kurt L. Komarek, Nonstoichiometry in B8‐Type NiSb, Zeitschrift anorg allge chemie 533, 205-214 (1986).  
_cited as the source of values for this phase_

## FCC_A1 (Ni–Sb)

- Id: `phase:ni-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1730.24 K, x(Sb) 0–0.10338
- Literature: 27 values (27 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:fcc-a1)

Names (7): _corpus: _corpus:phase:ni-sb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2008.02.001:(αNi), paper:10.1016/s1001-0521(08)60150-3:fcc(Ni)  
_tdb: _tdb:NiSb-08Cao.tdb:FCC_A1, tdb:NiSb-08Zha.tdb:FCC_A1, tdb:NiSb-13Cao.tdb:FCC_A1, tdb:NiSb-14Kro.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): FCC_A1, type code %A, sha256 `c50b9c6a21205dfe…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : NI% SB : VA : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): FCC_A1, type code %A, sha256 `1ab705f632704a07…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NI% SB : VA : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): FCC_A1, type code %A, sha256 `57b2cd3fde2a4256…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : NI% SB : VA : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): FCC_A1, type code %A, sha256 `15754b2a707f1c85…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : NI% SB : VA : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_

## HCP_A3 (Ni–Sb)

- Id: `phase:ni-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:hcp-a3)

Names (5): _corpus: _corpus:phase:ni-sb:hcp-a3  
_tdb: _tdb:NiSb-08Cao.tdb:HCP_A3, tdb:NiSb-08Zha.tdb:HCP_A3, tdb:NiSb-13Cao.tdb:HCP_A3, tdb:NiSb-14Kro.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): HCP_A3, type code %A, sha256 `c50b9c6a21205dfe…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : NI SB : VA : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): HCP_A3, type code %A, sha256 `1ab705f632704a07…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NI SB : VA : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): HCP_A3, type code %A, sha256 `57b2cd3fde2a4256…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : NI SB : VA : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): HCP_A3, type code %A, sha256 `15754b2a707f1c85…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : NI SB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase_

## LIQUID (Ni–Sb)

- Id: `phase:ni-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 890.32–2500 K, x(Sb) 0–1
- Literature: 73 values (72 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:liquid)

Names (7): _corpus: _corpus:phase:ni-sb:liquid  
_paper: _paper:10.1016/j.calphad.2008.02.001:L, paper:10.1016/s1001-0521(08)60150-3:L  
_tdb: _tdb:NiSb-08Cao.tdb:LIQUID, tdb:NiSb-08Zha.tdb:LIQUID, tdb:NiSb-13Cao.tdb:LIQUID, tdb:NiSb-14Kro.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): LIQUID, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : NI SB : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): LIQUID, type code %, sha256 `1ab705f632704a07…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NI SB : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): LIQUID, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : NI SB : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): LIQUID, type code %, sha256 `15754b2a707f1c85…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : NI SB : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19865330226](https://doi.org/10.1002/zaac.19865330226) Robert Leubolt, Herbert Ipser, Peter Terzieff, Kurt L. Komarek, Nonstoichiometry in B8‐Type NiSb, Zeitschrift anorg allge chemie 533, 205-214 (1986).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
_cited as the source of values for this phase_

## NI3SB_D03 (Ni–Sb)

- Id: `phase:ni-sb:ni3sb-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 802.63–1444.23 K, x(Sb) 0.25493–0.29478
- Literature: 26 values (26 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:ni3sb-d03)

Names (5): _corpus: _corpus:phase:ni-sb:ni3sb-d03  
_paper: _paper:10.1016/s1001-0521(08)60150-3:Ni3Sb_HT  
_tdb: _tdb:NiSb-08Cao.tdb:NI3SB_D03, tdb:NiSb-08Zha.tdb:NI3SB_D03, tdb:NiSb-13Cao.tdb:NI3SB_D03  


### TDB models of NI3SB_D03 (3): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): NI3SB_D03, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
60: PHASE NI3SB_D03 % 3 2 1 1 !
61: CONST NI3SB_D03 : NI% VA : NI : NI SB% : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): NI3SB_D03, type code %, sha256 `1ab705f632704a07…`

~~~~text
52: PHASE NI3SB_D03 % 3 2 1 1 !
53: CONST NI3SB_D03 : NI% VA : NI VA% : SB : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): NI3SB_D03, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
58: PHASE NI3SB_D03 % 3 2 1 1 !
59: CONST NI3SB_D03 : NI% VA : NI VA% : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase_

## NI3SB_D0A (Ni–Sb)

- Id: `phase:ni-sb:ni3sb-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–990 K, x(Sb) 0.23685–0.25
- Literature: 22 values (22 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:ni3sb-d0a)

Names (9): _corpus: _corpus:phase:ni-sb:ni3sb-d0a  
_paper: _paper:10.1016/j.calphad.2008.02.001:(δNi3Sb), paper:10.1016/j.calphad.2008.02.001:δNi3Sb, paper:10.1016/j.calphad.2008.02.001:δNi4Sb, paper:10.1016/s1001-0521(08)60150-3:Ni3Sb  
_tdb: _tdb:NiSb-08Cao.tdb:NI3SB_D0A, tdb:NiSb-08Zha.tdb:NI3SB_D0A, tdb:NiSb-13Cao.tdb:NI3SB_D0A, tdb:NiSb-14Kro.tdb:NI3SB_D0A  


### TDB models of NI3SB_D0A (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): NI3SB_D0A, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
55: PHASE NI3SB_D0A % 2 3 1 !
56: CONST NI3SB_D0A : NI : SB : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): NI3SB_D0A, type code %, sha256 `1ab705f632704a07…`

~~~~text
47: PHASE NI3SB_D0A % 2 3 1 !
48: CONST NI3SB_D0A : NI : NI SB% : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): NI3SB_D0A, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
53: PHASE NI3SB_D0A % 2 3 1 !
54: CONST NI3SB_D0A : NI : NI SB% : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): NI3SB_D0A, type code %, sha256 `15754b2a707f1c85…`

~~~~text
54: PHASE NI3SB_D0A % 2 3 1 !
55: CONST NI3SB_D0A : NI : NI SB% : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_

## NI5SB2_LT (Ni–Sb)

- Id: `phase:ni-sb:ni5sb2`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_structure_token; off_stoichiometric_model
- Candidate (literature_printed): Ni5Sb2 · mC28 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): Ni5Sb2 · mC28 · C2 (5) — Hallstedt 2025 mmc2 row for NI5SB2_LT: Ni5Sb2 (low T)
- Candidate (tdb_comment): Ni5Sb2 · mC28 · C2 — NiSb-08Cao.tdb: 'Prototype Ni5Sb2 (mC28, C2)'
- Candidate (tdb_comment): Ni5Sb2 · mC28 · C2 — NiSb-08Zha.tdb: 'Prototype Ni5Sb2 (mC28, C2)'
- Candidate (tdb_comment): Ni5Sb2 · mC28 · C2 — NiSb-13Cao.tdb: 'Prototype Ni5Sb2 (mC28, C2)'
- Candidate (tdb_comment): Ni5Sb2 · mC28 · C2 — NiSb-14Kro.tdb: 'Prototype Ni5Sb2 (mC28, C2)'
- Stability: stable in 4 of 4 calculated diagram(s): 300–884.35 K, x(Sb) 0.27394–0.28571
- Literature: 18 values (18 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:ni5sb2)

Names (9): _corpus: _corpus:phase:ni-sb:ni5sb2  
_paper: _paper:10.1016/j.calphad.2008.02.001:(θNi5Sb2), paper:10.1016/j.calphad.2008.02.001:θNi5Sb2, paper:10.1016/j.calphad.2008.02.001:θNi7Sb3, paper:10.1016/s1001-0521(08)60150-3:Ni7Sb3  
_tdb: _tdb:NiSb-08Cao.tdb:NI5SB2_LT, tdb:NiSb-08Zha.tdb:NI5SB2_LT, tdb:NiSb-13Cao.tdb:NI5SB2_LT, tdb:NiSb-14Kro.tdb:NI5SB2_LT  


### TDB models of NI5SB2_LT (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): NI5SB2_LT, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
65: PHASE NI5SB2_LT % 2 0.717 0.283 !
66: CONST NI5SB2_LT : NI : SB : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): NI5SB2_LT, type code %, sha256 `1ab705f632704a07…`

~~~~text
57: PHASE NI5SB2_LT % 2 5 2 !
58: CONST NI5SB2_LT : NI : NI SB% : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): NI5SB2_LT, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
63: PHASE NI5SB2_LT % 2 5 2 !
64: CONST NI5SB2_LT : NI : NI SB% : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): NI5SB2_LT, type code %, sha256 `15754b2a707f1c85…`

~~~~text
59: PHASE NI5SB2_LT % 2 5 2 !
60: CONST NI5SB2_LT : NI : NI SB% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_

## NI5SB2-LT (Ni–Sb)

- Id: `phase:ni-sb:ni5sb2-lt`; status `unresolved_no_candidates`
- No structure assigned. Why: no_bundled_tdb_model; no_structure_token
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:ni5sb2-lt)

Names (1): _corpus: _corpus:phase:ni-sb:ni5sb2-lt  


## NISB_B81 (Ni–Sb)

- Id: `phase:ni-sb:nisb-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2500 K, x(Sb) 0.43752–0.54484
- Literature: 50 values (50 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:nisb-b81)

Names (8): _corpus: _corpus:phase:ni-sb:nisb-b81  
_paper: _paper:10.1016/j.calphad.2008.02.001:(γNiSb), paper:10.1016/j.calphad.2008.02.001:γNiSb, paper:10.1016/s1001-0521(08)60150-3:NiSb  
_tdb: _tdb:NiSb-08Cao.tdb:NISB_B81, tdb:NiSb-08Zha.tdb:NISB_B81, tdb:NiSb-13Cao.tdb:NISB_B81, tdb:NiSb-14Kro.tdb:NISB_B81  


### TDB models of NISB_B81 (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): NISB_B81, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
70: PHASE NISB_B81 % 3 1 1 1 !
71: CONST NISB_B81 : NI% VA : NI VA% : SB : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): NISB_B81, type code %, sha256 `1ab705f632704a07…`

~~~~text
62: PHASE NISB_B81 % 3 1 1 1 !
63: CONST NISB_B81 : NI% VA : NI VA% : SB : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): NISB_B81, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
68: PHASE NISB_B81 % 3 1 1 1 !
69: CONST NISB_B81 : NI% VA : NI VA% : NI SB% : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): NISB_B81, type code %, sha256 `15754b2a707f1c85…`

~~~~text
64: PHASE NISB_B81 % 3 1 1 1 !
65: CONST NISB_B81 : NI% VA : NI VA% : NI SB% : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1002/zaac.19865330226](https://doi.org/10.1002/zaac.19865330226) Robert Leubolt, Herbert Ipser, Peter Terzieff, Kurt L. Komarek, Nonstoichiometry in B8‐Type NiSb, Zeitschrift anorg allge chemie 533, 205-214 (1986).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
_cited as the source of values for this phase_

## NISB2_C18 (Ni–Sb)

- Id: `phase:ni-sb:nisb2-c18`; status `assigned`
- Structure: alpha-FeS2 · C18 · oP6 · Pnnm (58); type `st:c18-alpha-fes2-op6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabdlf and oqmd-7569, space group 58
- Stoichiometry: Ni 0.3333, Sb 0.6667
- Stability: stable in 4 of 4 calculated diagram(s): 300–901.22 K, x(Sb) 0.66667–0.66667
- Literature: 22 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-sb:nisb2-c18)

Names (10): _corpus: _corpus:phase:ni-sb:nisb2-c18  
_mp: _mp:mp-aaaabdlf  
_oqmd: _oqmd:oqmd-7569  
_paper: _paper:10.1016/j.calphad.2008.02.001:(ζNi4Sb5), paper:10.1016/j.calphad.2008.02.001:ζNiSb2, paper:10.1016/s1001-0521(08)60150-3:NiSb2  
_tdb: _tdb:NiSb-08Cao.tdb:NISB2_C18, tdb:NiSb-08Zha.tdb:NISB2_C18, tdb:NiSb-13Cao.tdb:NISB2_C18, tdb:NiSb-14Kro.tdb:NISB2_C18  


### TDB models of NISB2_C18 (4): PHASE and CONSTITUENT statements as written

[NiSb-08Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Cao.tdb): NISB2_C18, type code %, sha256 `c50b9c6a21205dfe…`

~~~~text
75: PHASE NISB2_C18 % 2 1 2 !
76: CONST NISB2_C18 : NI : SB : !
~~~~

[NiSb-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-08Zha.tdb): NISB2_C18, type code %, sha256 `1ab705f632704a07…`

~~~~text
67: PHASE NISB2_C18 % 2 1 2 !
68: CONST NISB2_C18 : NI : SB : !
~~~~

[NiSb-13Cao.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-13Cao.tdb): NISB2_C18, type code %, sha256 `57b2cd3fde2a4256…`

~~~~text
73: PHASE NISB2_C18 % 2 1 2 !
74: CONST NISB2_C18 : NI : SB : !
~~~~

[NiSb-14Kro.tdb](https://orchid-project.org/data/databases/sgte-binary/NiSb-14Kro.tdb): NISB2_C18, type code %, sha256 `15754b2a707f1c85…`

~~~~text
69: PHASE NISB2_C18 % 2 1 2 !
70: CONST NISB2_C18 : NI : SB : !
~~~~

Example references (9 of 9; assessments first): 

- [doi:10.1016/j.calphad.2008.02.001](https://doi.org/10.1016/j.calphad.2008.02.001) Yubi Zhang, Changrong Li, Zhenmin Du, Cuiping Guo, A thermodynamic assessment of Ni–Sb system, Calphad 32, 378-388 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S1001-0521(08)60150-3](https://doi.org/10.1016/S1001-0521%2808%2960150-3) Z. Cao, Y. Takaku, I. Ohnuma, R. Kainuma, H. Zhu, K. Ishida, Rare. Met., 27, 384-92(2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-013-2599-7](https://doi.org/10.1007/s11664-013-2599-7) Zhanmin Cao, Wei Xie, Kunpeng Wang, Guangwei Du, Zhiyu Qiao, Thermodynamic Assessment of the In-Ni-Sb System and Predictions for Thermally Stable Contacts to InSb, Journal of Elec Materi 42, 2615-2629 (2013).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.11.007](https://doi.org/10.1016/j.calphad.2013.11.007) Ales Kroupa, Ratikanta Mishra, Divakar Rajamohan, Hans Flandorfer, Andrew Watson, Herbert Ipser, Phase equilibria in the ternary Ni–Sb–Sn system: Experiments and calculations, Calphad 45, 151-166 (2014).  
_assessment that models this phase_
- [doi:10.1016/0022-5088(89)90235-x](https://doi.org/10.1016/0022-5088%2889%2990235-x) P. Feschotte, D. Lorin, Les systemes binaires Fe-Sb, Co-Sb et Ni-Sb, Journal of the Less Common Metals 155, 255-269 (1989).  
_cited as the source of values for this phase_
- [doi:10.1016/0025-5408(72)90207-3](https://doi.org/10.1016/0025-5408%2872%2990207-3) J. Naud, D. Parijs, Contribution a l'etude des systemes NiSb et CoNiSb par diffraction-X, Materials Research Bulletin 7, 301-308 (1972).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19060490107](https://doi.org/10.1002/zaac.19060490107) K. Lossew, Metallographische Mitteilungen aus dem Institut für anorganische Chemie der Universität Göttingen. XXIV. Über die Legierungen des Nickels mit Antimon, Z. Anorg. Chem. 49, 58-71 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19865330226](https://doi.org/10.1002/zaac.19865330226) Robert Leubolt, Herbert Ipser, Peter Terzieff, Kurt L. Komarek, Nonstoichiometry in B8‐Type NiSb, Zeitschrift anorg allge chemie 533, 205-214 (1986).  
_cited as the source of values for this phase_
- [doi:10.3891/acta.chem.scand.31a-0517](https://doi.org/10.3891/acta.chem.scand.31a-0517) Arne Kjekshus, Trond Rakke, Pentti Salomaa, H. Svanholt, Paul Hagenmuller, Arne F. Andresen, High Temperature Studies of Marcasite and Arsenopyrite Type Compounds., Acta Chem. Scand. 31a, 517-529 (1977).  
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
