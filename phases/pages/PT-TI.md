# Pt–Ti phases

> Pt–Ti system: 10 phases (tier A 7, tier B 1, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PT-TI.html · Markdown: https://data.orchid-project.org/phases/pages/PT-TI.md

10 phases (tier A 7, tier B 1, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PT-TI) · [full JSON](https://data.orchid-project.org/phases/systems/PT-TI.json) · [Pt–Ti system page](https://data.orchid-project.org/systems/PT-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/PT-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pt–Ti system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pt-ti-bcc-a2); _phase:pt-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1112.87–1940.98 K, x(Ti) 0.91726–1 | 4 | 1 |
| [FCC_A1](#phase-pt-ti-fcc-a1); _phase:pt-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2073.38 K, x(Ti) 0–0.11595 | 4 | 1 |
| [HCP_A3](#phase-pt-ti-hcp-a3); _phase:pt-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 0.97816–1 | 2 | 1 |
| [LIQUID](#phase-pt-ti-liquid); _phase:pt-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1583.06–2500 K, x(Ti) 0–1 | 16 | 1 |
| [PT3TI_D024](#phase-pt-ti-pt3ti-d024); _phase:pt-ti:pt3ti-d024_ | Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2223.38 K, x(Ti) 0.19929–0.25 | 10 | 1 |
| [PT3TI4](#phase-pt-ti-pt3ti4); _phase:pt-ti:pt3ti4_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1478.17 K, x(Ti) 0.57143–0.57143 | 3 | 1 |
| [PT8TI](#phase-pt-ti-pt8ti); _phase:pt-ti:pt8ti_ | Pt8Ti · tI18 · I4/mmm (139) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1353.05 K, x(Ti) 0.11111–0.11111 | 2 | 1 |
| [PTTI_B19](#phase-pt-ti-ptti-b19); _phase:pt-ti:ptti-b19_ | AuCd · B19 · oP4 · Pmma (51) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1312.19 K, x(Ti) 0.47653–0.50121 | 6 | 1 |
| [PTTI_B2](#phase-pt-ti-ptti-b2); _phase:pt-ti:ptti-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1306.87–2106.45 K, x(Ti) 0.43883–0.51961 | 0 | 1 |
| [PTTI3_A15](#phase-pt-ti-ptti3-a15); _phase:pt-ti:ptti3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1772.47 K, x(Ti) 0.73275–0.78224 | 13 | 1 |

## BCC_A2 (Pt–Ti)

- Id: `phase:pt-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1112.87–1940.98 K, x(Ti) 0.91726–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:bcc-a2)

Names (3): _corpus: _corpus:phase:pt-ti:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2007.07.047:Bcc  
_tdb: _tdb:PtTi-08Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): BCC_A2, type code %B, sha256 `225d207ff370fad5…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PT TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pt–Ti)

- Id: `phase:pt-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2073.38 K, x(Ti) 0–0.11595
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:pt-ti:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2007.07.047:Fcc  
_tdb: _tdb:PtTi-08Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): FCC_A1, type code %A, sha256 `225d207ff370fad5…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PT TI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02644471](https://doi.org/10.1007/bf02644471) P. J. Meschter, W. L. Worrell, An investigation of high-temperature thermodynamic properties in the Pt-Ti system, Metall Trans A 7, 299-305 (1976).  
_cited as the source of values for this phase_

## HCP_A3 (Pt–Ti)

- Id: `phase:pt-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 0.97816–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:hcp-a3)

Names (3): _corpus: _corpus:phase:pt-ti:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2007.07.047:Hcp  
_tdb: _tdb:PtTi-08Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): HCP_A3, type code %A, sha256 `225d207ff370fad5…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : PT TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Pt–Ti)

- Id: `phase:pt-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1583.06–2500 K, x(Ti) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:liquid)

Names (3): _corpus: _corpus:phase:pt-ti:liquid  
_paper: _paper:10.1016/j.jallcom.2007.07.047:L  
_tdb: _tdb:PtTi-08Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): LIQUID, type code %, sha256 `225d207ff370fad5…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : PT TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2003.12.001](https://doi.org/10.1016/j.jallcom.2003.12.001) T Biggs, L.A Cornish, M.J Witcomb, M.B Cortie, Revised phase diagram for the Pt–Ti system from 30 to 60 at.% platinum, Journal of Alloys and Compounds 375, 120-127 (2004).  
_cited as the source of values for this phase_

## PT3TI_D024 (Pt–Ti)

- Id: `phase:pt-ti:pt3ti-d024`; status `assigned`
- Structure: Ni3Ti · D0_24 · hP16 · P6_3/mmc (194); type `st:d0-24-ni3ti-hp16`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2223.38 K, x(Ti) 0.19929–0.25
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:pt3ti-d024)

Names (4): _corpus: _corpus:phase:pt-ti:pt3ti-d024  
_paper: _paper:10.1016/j.jallcom.2007.07.047:TiPt3-, paper:10.1016/j.jallcom.2007.07.047:γ  
_tdb: _tdb:PtTi-08Li.tdb:PT3TI_D024  


### TDB models of PT3TI_D024 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): PT3TI_D024, type code %, sha256 `225d207ff370fad5…`

~~~~text
49: PHASE PT3TI_D024 % 2 3 1 !
50: CONST PT3TI_D024 : PT : PT TI% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02644471](https://doi.org/10.1007/bf02644471) P. J. Meschter, W. L. Worrell, An investigation of high-temperature thermodynamic properties in the Pt-Ti system, Metall Trans A 7, 299-305 (1976).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869304](https://doi.org/10.1007/bf02869304) J.L. Murray, Bull Alloy Phase Diagram 3 (1982) 329–335.  
_cited as the source of values for this phase_

## PT3TI4 (Pt–Ti)

- Id: `phase:pt-ti:pt3ti4`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Pt3Ti4) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Pt3Ti4) — Hallstedt 2025 mmc2 row for PT3TI4: Pt3Ti4
- Stoichiometry: Pt 0.4286, Ti 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1478.17 K, x(Ti) 0.57143–0.57143
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:pt3ti4)

Names (3): _corpus: _corpus:phase:pt-ti:pt3ti4  
_paper: _paper:10.1016/j.jallcom.2007.07.047:Ti4Pt3  
_tdb: _tdb:PtTi-08Li.tdb:PT3TI4  


### TDB models of PT3TI4 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): PT3TI4, type code %, sha256 `225d207ff370fad5…`

~~~~text
64: PHASE PT3TI4 % 2 3 4 !
65: CONST PT3TI4 : PT : TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2003.12.001](https://doi.org/10.1016/j.jallcom.2003.12.001) T Biggs, L.A Cornish, M.J Witcomb, M.B Cortie, Revised phase diagram for the Pt–Ti system from 30 to 60 at.% platinum, Journal of Alloys and Compounds 375, 120-127 (2004).  
_cited as the source of values for this phase_

## PT8TI (Pt–Ti)

- Id: `phase:pt-ti:pt8ti`; status `assigned`
- Structure: Pt8Ti · tI18 · I4/mmm (139); type `st:pt8ti-ti18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Pt 0.8889, Ti 0.1111
- Stability: stable in 1 of 1 calculated diagram(s): 300–1353.05 K, x(Ti) 0.11111–0.11111
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:pt8ti)

Names (5): _corpus: _corpus:phase:pt-ti:pt8ti  
_mp: _mp:mp-aaaabtqq  
_oqmd: _oqmd:oqmd-18017  
_paper: _paper:10.1016/j.jallcom.2007.07.047:TiPt8  
_tdb: _tdb:PtTi-08Li.tdb:PT8TI  


### TDB models of PT8TI (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): PT8TI, type code %, sha256 `225d207ff370fad5…`

~~~~text
44: PHASE PT8TI % 2 8 1 !
45: CONST PT8TI : PT : TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02644471](https://doi.org/10.1007/bf02644471) P. J. Meschter, W. L. Worrell, An investigation of high-temperature thermodynamic properties in the Pt-Ti system, Metall Trans A 7, 299-305 (1976).  
_cited as the source of values for this phase_

## PTTI_B19 (Pt–Ti)

- Id: `phase:pt-ti:ptti-b19`; status `assigned`
- Structure: AuCd · B19 · oP4 · Pmma (51); type `st:b19-aucd-op4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtTi-08Li.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1312.19 K, x(Ti) 0.47653–0.50121
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:ptti-b19)

Names (3): _corpus: _corpus:phase:pt-ti:ptti-b19  
_paper: _paper:10.1016/j.jallcom.2007.07.047:αTiPt  
_tdb: _tdb:PtTi-08Li.tdb:PTTI_B19  


### TDB models of PTTI_B19 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): PTTI_B19, type code %, sha256 `225d207ff370fad5…`

~~~~text
54: PHASE PTTI_B19 % 2 1 1 !
55: CONST PTTI_B19 : PT% TI : PT TI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02869304](https://doi.org/10.1007/bf02869304) J.L. Murray, Bull Alloy Phase Diagram 3 (1982) 329–335.  
_cited as the source of values for this phase_

## PTTI_B2 (Pt–Ti)

- Id: `phase:pt-ti:ptti-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtTi-08Li.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1306.87–2106.45 K, x(Ti) 0.43883–0.51961
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:ptti-b2)

Names (2): _corpus: _corpus:phase:pt-ti:ptti-b2  
_tdb: _tdb:PtTi-08Li.tdb:PTTI_B2  


### TDB models of PTTI_B2 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): PTTI_B2, type code %, sha256 `225d207ff370fad5…`

~~~~text
59: PHASE PTTI_B2 % 2 1 1 !
60: CONST PTTI_B2 : PT% TI : PT TI% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase_

## PTTI3_A15 (Pt–Ti)

- Id: `phase:pt-ti:ptti3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtTi-08Li.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1772.47 K, x(Ti) 0.73275–0.78224
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-ti:ptti3-a15)

Names (3): _corpus: _corpus:phase:pt-ti:ptti3-a15  
_paper: _paper:10.1016/j.jallcom.2007.07.047:Ti3Pt  
_tdb: _tdb:PtTi-08Li.tdb:PTTI3_A15  


### TDB models of PTTI3_A15 (1): PHASE and CONSTITUENT statements as written

[PtTi-08Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtTi-08Li.tdb): PTTI3_A15, type code %, sha256 `225d207ff370fad5…`

~~~~text
69: PHASE PTTI3_A15 % 2 1 3 !
70: CONST PTTI3_A15 : PT% TI : PT TI% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2007.07.047](https://doi.org/10.1016/j.jallcom.2007.07.047) Mei Li, Wei Han, Changrong Li, Thermodynamic assessment of the Pt–Ti system, Journal of Alloys and Compounds 461, 189-194 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2003.12.001](https://doi.org/10.1016/j.jallcom.2003.12.001) T Biggs, L.A Cornish, M.J Witcomb, M.B Cortie, Revised phase diagram for the Pt–Ti system from 30 to 60 at.% platinum, Journal of Alloys and Compounds 375, 120-127 (2004).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02869304](https://doi.org/10.1007/bf02869304) J.L. Murray, Bull Alloy Phase Diagram 3 (1982) 329–335.  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
