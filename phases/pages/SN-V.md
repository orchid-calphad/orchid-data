# Sn–V phases

> Sn–V system: 9 phases (tier A 5, liquid 1, needs_review 3); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-V.html · Markdown: https://data.orchid-project.org/phases/pages/SN-V.md

9 phases (tier A 5, liquid 1, needs_review 3); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-V) · [full JSON](https://data.orchid-project.org/phases/systems/SN-V.json) · [Sn–V system page](https://data.orchid-project.org/systems/SN-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–V system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-v-a4-diamond); _phase:sn-v:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [BCT_A5](#phase-sn-v-a5-bct); _phase:sn-v:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(V) 0–0 | 0 | 2 |
| [BCC_A2](#phase-sn-v-bcc-a2); _phase:sn-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.25 K, x(V) 0.84194–1 | 0 | 2 |
| [FCC_A1](#phase-sn-v-fcc-a1); _phase:sn-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-sn-v-hcp-a3); _phase:sn-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-sn-v-liquid); _phase:sn-v:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 505.08–4000 K, x(V) 0–1 | 4 | 2 |
| [SN2V_CB](#phase-sn-v-sn2v-cb); _phase:sn-v:sn2v-cb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1027.42 K, x(V) 0.34–0.34 | 0 | 1 |
| [SN3V2_CB](#phase-sn-v-sn3v2-cb); _phase:sn-v:sn3v2-cb_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1032.2 K, x(V) 0.4–0.4 | 0 | 1 |
| [SNV3_A15](#phase-sn-v-snv3-a15); _phase:sn-v:snv3-a15_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1871.31 K, x(V) 0.78–0.795 | 0 | 2 |

## DIAMOND_A4 (Sn–V)

- Id: `phase:sn-v:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:a4-diamond)

Names (3): _corpus: _corpus:phase:sn-v:a4-diamond  
_tdb: _tdb:SnV-02Stu-LB.tdb:DIAMOND_A4, tdb:SnV-08Che.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): DIAMOND_A4, type code %, sha256 `34ad8b6e7351ecab…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): DIAMOND_A4, type code %, sha256 `8c98bca6360bcce7…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## BCT_A5 (Sn–V)

- Id: `phase:sn-v:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–505.08 K, x(V) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:a5-bct)

Names (3): _corpus: _corpus:phase:sn-v:a5-bct  
_tdb: _tdb:SnV-02Stu-LB.tdb:BCT_A5, tdb:SnV-08Che.tdb:BCT_A5  


### TDB models of BCT_A5 (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): BCT_A5, type code %, sha256 `34ad8b6e7351ecab…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN : !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): BCT_A5, type code %, sha256 `8c98bca6360bcce7…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## BCC_A2 (Sn–V)

- Id: `phase:sn-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.25 K, x(V) 0.84194–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:bcc-a2)

Names (3): _corpus: _corpus:phase:sn-v:bcc-a2  
_tdb: _tdb:SnV-02Stu-LB.tdb:BCC_A2, tdb:SnV-08Che.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): BCC_A2, type code %B, sha256 `34ad8b6e7351ecab…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SN V% : VA : !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): BCC_A2, type code %B, sha256 `8c98bca6360bcce7…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SN V% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## FCC_A1 (Sn–V)

- Id: `phase:sn-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:fcc-a1)

Names (3): _corpus: _corpus:phase:sn-v:fcc-a1  
_tdb: _tdb:SnV-02Stu-LB.tdb:FCC_A1, tdb:SnV-08Che.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): FCC_A1, type code %A, sha256 `34ad8b6e7351ecab…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SN V : VA : !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): FCC_A1, type code %A, sha256 `8c98bca6360bcce7…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SN V : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## HCP_A3 (Sn–V)

- Id: `phase:sn-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:hcp-a3)

Names (3): _corpus: _corpus:phase:sn-v:hcp-a3  
_tdb: _tdb:SnV-02Stu-LB.tdb:HCP_A3, tdb:SnV-08Che.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): HCP_A3, type code %A, sha256 `34ad8b6e7351ecab…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SN V : VA: !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): HCP_A3, type code %A, sha256 `8c98bca6360bcce7…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SN V : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## LIQUID (Sn–V)

- Id: `phase:sn-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 505.08–4000 K, x(V) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:liquid)

Names (5): _corpus: _corpus:phase:sn-v:liquid  
_paper: _paper:10.1007/s11664-008-0530-4:Liquid, paper:10.1007/s11664-008-0530-4:liquid  
_tdb: _tdb:SnV-02Stu-LB.tdb:LIQUID, tdb:SnV-08Che.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): LIQUID, type code %, sha256 `34ad8b6e7351ecab…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN V : !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): LIQUID, type code %, sha256 `8c98bca6360bcce7…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## SN2V_CB (Sn–V)

- Id: `phase:sn-v:sn2v-cb`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C_b; stoichiometry_contradicts_C_b:SnV-08Che.tdb
- Candidate (name_token): CuMg2 · C_b · oF48 · Fddd (70) — Strukturbericht/word 'CB' in the TDB name
- Candidate (sgte_mmc2): CuMg2 · C_b · oF48 · Fddd (70) — Hallstedt 2025 mmc2 row for SN2V_CB: Sn2V
- Candidate (tdb_comment): CuMg2 · oF48 · Fddd — SnV-08Che.tdb: 'Prototype CuMg2 (oF48, Fddd)'
- Stoichiometry: Sn 0.6600, V 0.3400
- Stability: stable in 1 of 1 calculated diagram(s): 300–1027.42 K, x(V) 0.34–0.34
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:sn2v-cb)

Names (2): _corpus: _corpus:phase:sn-v:sn2v-cb  
_tdb: _tdb:SnV-08Che.tdb:SN2V_CB  


### TDB models of SN2V_CB (1): PHASE and CONSTITUENT statements as written

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): SN2V_CB, type code %, sha256 `8c98bca6360bcce7…`

~~~~text
54: PHASE SN2V_CB %  2 0.66 0.34 !
55: CONST SN2V_CB : SN : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_

## SN3V2_CB (Sn–V)

- Id: `phase:sn-v:sn3v2-cb`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C_b; stoichiometry_contradicts_C_b:SnV-02Stu-LB.tdb
- Candidate (name_token): CuMg2 · C_b · oF48 · Fddd (70) — Strukturbericht/word 'CB' in the TDB name
- Candidate (sgte_mmc2): CuMg2 · C_b · oF48 · Fddd (70) — Hallstedt 2025 mmc2 row for SN3V2_CB: Sn3V2
- Candidate (tdb_comment): CuMg2 · oF48 · Fddd — SnV-02Stu-LB.tdb: 'Prototype CuMg2 (oF48, Fddd)'
- Stoichiometry: Sn 0.6000, V 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1032.2 K, x(V) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:sn3v2-cb)

Names (2): _corpus: _corpus:phase:sn-v:sn3v2-cb  
_tdb: _tdb:SnV-02Stu-LB.tdb:SN3V2_CB  


### TDB models of SN3V2_CB (1): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): SN3V2_CB, type code %, sha256 `34ad8b6e7351ecab…`

~~~~text
54: PHASE SN3V2_CB %  2 3 2 !
55: CONST SN3V2_CB : SN : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
_assessment that models this phase_

## SNV3_A15 (Sn–V)

- Id: `phase:sn-v:snv3-a15`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; stoichiometry_contradicts_A15:SnV-02Stu-LB.tdb; stoichiometry_contradicts_A15:SnV-08Che.tdb
- Candidate (name_token): Cr3Si · A15 · cP8 · Pm-3n (223) — Strukturbericht/word 'A15' in the TDB name
- Candidate (sgte_mmc2): Cr3Si · A15 · cP8 · Pm-3n (223) — Hallstedt 2025 mmc2 row for SNV3_A15: SnV3
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — SnV-02Stu-LB.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Candidate (tdb_comment): Cr3Si · cP8 · Pm-3n — SnV-08Che.tdb: 'Prototype Cr3Si (cP8, Pm-3n)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–1871.31 K, x(V) 0.78–0.795
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-v:snv3-a15)

Names (3): _corpus: _corpus:phase:sn-v:snv3-a15  
_tdb: _tdb:SnV-02Stu-LB.tdb:SNV3_A15, tdb:SnV-08Che.tdb:SNV3_A15  


### TDB models of SNV3_A15 (2): PHASE and CONSTITUENT statements as written

[SnV-02Stu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-02Stu-LB.tdb): SNV3_A15, type code %, sha256 `34ad8b6e7351ecab…`

~~~~text
59: PHASE SNV3_A15 %  2 0.41 1.59 !
60: CONST SNV3_A15 : SN : V : !
~~~~

[SnV-08Che.tdb](https://orchid-project.org/data/databases/sgte-binary/SnV-08Che.tdb): SNV3_A15, type code %, sha256 `8c98bca6360bcce7…`

~~~~text
59: PHASE SNV3_A15 %  2 0.22 0.78 !
60: CONST SNV3_A15 : SN : V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-008-0530-4](https://doi.org/10.1007/s11664-008-0530-4) Chih-Chi Chen, Wojcieh Gierlotka, Sinn-Wen Chen, Phase Equilibria of the Sn-V System and Interfacial Reactions in Sn/V Couples, Journal of Elec Materi 37, 1727-1733 (2008).  
_assessment that models this phase_
- [doi:10.3139/ijmr-2002-0009](https://doi.org/10.3139/ijmr-2002-0009) T. Studnitzky, B. Onderka, R. Schmid-Fetzer, Z. Metallkd., 93, 48-57(2002).  
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
