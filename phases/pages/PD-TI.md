# Pd–Ti phases

> Pd–Ti system: 10 phases (tier A 8, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PD-TI.html · Markdown: https://data.orchid-project.org/phases/pages/PD-TI.md

10 phases (tier A 8, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PD-TI) · [full JSON](https://data.orchid-project.org/phases/systems/PD-TI.json) · [Pd–Ti system page](https://data.orchid-project.org/systems/PD-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/PD-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pd–Ti system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pd-ti-bcc-a2); _phase:pd-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 868.41–1890 K, x(Ti) 0.52–1 | 6 | 2 |
| [B2_BCC](#phase-pd-ti-bcc-b2); _phase:pd-ti:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 783–2499.73 K, x(Ti) 0.44392–1 | 11 | 1 |
| [FCC_A1](#phase-pd-ti-fcc-a1); _phase:pd-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1829.99 K, x(Ti) 0–0.21354 | 4 | 1 |
| [HCP_A3](#phase-pd-ti-hcp-a3); _phase:pd-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1163.41 K, x(Ti) 0.97157–1 | 2 | 1 |
| [LIQUID](#phase-pd-ti-liquid); _phase:pd-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1395.98–2500 K, x(Ti) 0–1 | 17 | 1 |
| [PD3TI_D024](#phase-pd-ti-pd3ti-d024); _phase:pd-ti:pd3ti-d024_ | Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1802.54 K, x(Ti) 0.25–0.25 | 6 | 1 |
| [PD3TI2](#phase-pd-ti-pd3ti2); _phase:pd-ti:pd3ti2_ | Pd3Ti2 · oC20 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1602.73 K, x(Ti) 0.4–0.4 | 6 | 1 |
| [PDTI_B19](#phase-pd-ti-pdti-b19); _phase:pd-ti:pdti-b19_ | AuCd · B19 · oP4 · Pmma (51) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–813.01 K, x(Ti) 0.48749–0.51282 | 5 | 1 |
| [PDTI_C11B](#phase-pd-ti-pdti-c11b); _phase:pd-ti:pdti-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1684.79 K, x(Ti) 0.33603–0.66667 | 11 | 1 |
| [PDTI3_A15](#phase-pd-ti-pdti3-a15); _phase:pd-ti:pdti3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–963.06 K, x(Ti) 0.75–0.75 | 4 | 1 |

## BCC_A2 (Pd–Ti)

- Id: `phase:pd-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 868.41–1890 K, x(Ti) 0.52–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:bcc-a2)

Names (4): _corpus: _corpus:phase:pd-ti:bcc-a2  
_paper: _paper:10.1016/j.calphad.2011.07.004:bcc  
_tdb: _tdb:PdTi-11Guo.tdb:A2_BCC, tdb:PdTi-11Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): A2_BCC, type code %B, sha256 `e8810155ee2f9664…`

~~~~text
37: PHASE A2_BCC %B 2 1 3 !
38: CONST A2_BCC : PD TI% : VA : !
~~~~

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): BCC_A2, type code %B, sha256 `e8810155ee2f9664…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PD TI% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## B2_BCC (Pd–Ti)

- Id: `phase:pd-ti:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: PdTi-11Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in PdTi-11Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 783–2499.73 K, x(Ti) 0.44392–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:bcc-b2)

Names (4): _corpus: _corpus:phase:pd-ti:bcc-b2, corpus:phase:pd-ti:b2-bcc  
_paper: _paper:10.1016/j.calphad.2011.07.004:βPdTi  
_tdb: _tdb:PdTi-11Guo.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): B2_BCC, type code %BO, sha256 `e8810155ee2f9664…`

~~~~text
42: PHASE B2_BCC %BO 3 0.5 0.5 3 !
43: CONST B2_BCC : PD% TI : PD TI% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## FCC_A1 (Pd–Ti)

- Id: `phase:pd-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1829.99 K, x(Ti) 0–0.21354
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:pd-ti:fcc-a1  
_paper: _paper:10.1016/j.calphad.2011.07.004:fcc  
_tdb: _tdb:PdTi-11Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): FCC_A1, type code %A, sha256 `e8810155ee2f9664…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PD% TI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## HCP_A3 (Pd–Ti)

- Id: `phase:pd-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1163.41 K, x(Ti) 0.97157–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:hcp-a3)

Names (3): _corpus: _corpus:phase:pd-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2011.07.004:hcp  
_tdb: _tdb:PdTi-11Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): HCP_A3, type code %A, sha256 `e8810155ee2f9664…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : PD TI% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## LIQUID (Pd–Ti)

- Id: `phase:pd-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1395.98–2500 K, x(Ti) 0–1
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:liquid)

Names (3): _corpus: _corpus:phase:pd-ti:liquid  
_paper: _paper:10.1016/j.calphad.2011.07.004:L  
_tdb: _tdb:PdTi-11Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): LIQUID, type code %, sha256 `e8810155ee2f9664…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PD TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## PD3TI_D024 (Pd–Ti)

- Id: `phase:pd-ti:pd3ti-d024`; status `assigned`
- Structure: Ni3Ti · D0_24 · hP16 · P6_3/mmc (194); type `st:d0-24-ni3ti-hp16`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaackxzb and oqmd-21293, space group 194
- Stoichiometry: Pd 0.7500, Ti 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1802.54 K, x(Ti) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:pd3ti-d024)

Names (5): _corpus: _corpus:phase:pd-ti:pd3ti-d024  
_mp: _mp:mp-aaackxzb  
_oqmd: _oqmd:oqmd-21293  
_paper: _paper:10.1016/j.calphad.2011.07.004:Pd3Ti  
_tdb: _tdb:PdTi-11Guo.tdb:PD3TI_D024  


### TDB models of PD3TI_D024 (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): PD3TI_D024, type code %, sha256 `e8810155ee2f9664…`

~~~~text
52: PHASE PD3TI_D024 % 2 3 1 !
53: CONST PD3TI_D024 : PD : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## PD3TI2 (Pd–Ti)

- Id: `phase:pd-ti:pd3ti2`; status `assigned`
- Structure: Pd3Ti2 · oC20 · Cmcm (63); type `st:pd3ti2-oc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pd 0.6000, Ti 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1602.73 K, x(Ti) 0.4–0.4
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:pd3ti2)

Names (3): _corpus: _corpus:phase:pd-ti:pd3ti2  
_paper: _paper:10.1016/j.calphad.2011.07.004:Pd3Ti2  
_tdb: _tdb:PdTi-11Guo.tdb:PD3TI2  


### TDB models of PD3TI2 (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): PD3TI2, type code %, sha256 `e8810155ee2f9664…`

~~~~text
62: PHASE PD3TI2 % 2 3 2 !
63: CONST PD3TI2 : PD : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## PDTI_B19 (Pd–Ti)

- Id: `phase:pd-ti:pdti-b19`; status `assigned`
- Structure: AuCd · B19 · oP4 · Pmma (51); type `st:b19-aucd-op4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdTi-11Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–813.01 K, x(Ti) 0.48749–0.51282
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:pdti-b19)

Names (3): _corpus: _corpus:phase:pd-ti:pdti-b19  
_paper: _paper:10.1016/j.calphad.2011.07.004:αPdTi  
_tdb: _tdb:PdTi-11Guo.tdb:PDTI_B19  


### TDB models of PDTI_B19 (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): PDTI_B19, type code %, sha256 `e8810155ee2f9664…`

~~~~text
67: PHASE PDTI_B19 % 2 1 1 !
68: CONST PDTI_B19 : PD% TI : PD TI% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_

## PDTI_C11B (Pd–Ti)

- Id: `phase:pd-ti:pdti-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdTi-11Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1684.79 K, x(Ti) 0.33603–0.66667
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:pdti-c11b)

Names (4): _corpus: _corpus:phase:pd-ti:pdti-c11b  
_paper: _paper:10.1016/j.calphad.2011.07.004:Pd2Ti, paper:10.1016/j.calphad.2011.07.004:PdTi2  
_tdb: _tdb:PdTi-11Guo.tdb:PDTI_C11B  


### TDB models of PDTI_C11B (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): PDTI_C11B, type code %, sha256 `e8810155ee2f9664…`

~~~~text
57: PHASE PDTI_C11B % 2 2 1 !
58: CONST PDTI_C11B : PD TI : PD TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
_cited as the source of values for this phase_

## PDTI3_A15 (Pd–Ti)

- Id: `phase:pd-ti:pdti3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacjliq and oqmd-21288, space group 223
- Stoichiometry: Pd 0.2500, Ti 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–963.06 K, x(Ti) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-ti:pdti3-a15)

Names (5): _corpus: _corpus:phase:pd-ti:pdti3-a15  
_mp: _mp:mp-aaacjliq  
_oqmd: _oqmd:oqmd-21288  
_paper: _paper:10.1016/j.calphad.2011.07.004:PdTi3  
_tdb: _tdb:PdTi-11Guo.tdb:PDTI3_A15  


### TDB models of PDTI3_A15 (1): PHASE and CONSTITUENT statements as written

[PdTi-11Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PdTi-11Guo.tdb): PDTI3_A15, type code %, sha256 `e8810155ee2f9664…`

~~~~text
72: PHASE PDTI3_A15 % 2 1 3 !
73: CONST PDTI3_A15 : PD : TI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2011.07.004](https://doi.org/10.1016/j.calphad.2011.07.004) Cuiping Guo, Mei Li, Changrong Li, Zhenmin Du, A thermodynamic modeling of the Pd–Ti system, Calphad 35, 512-517 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02652177](https://doi.org/10.1007/bf02652177) H. Okamoto, Pd-Ti (palladium-titanium), JPE 14, 128-129 (1993).  
_cited as the source of values for this phase_
- [doi:10.1016/j.msea.2006.01.120](https://doi.org/10.1016/j.msea.2006.01.120) T. Yamamuro, Y. Morizono, J. Honjyo, M. Nishida, Phase equilibrium and martensitic transformation in near equiatomic Ti Pd alloys, Materials Science and Engineering: A 438-440, 327-331 (2006).  
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
