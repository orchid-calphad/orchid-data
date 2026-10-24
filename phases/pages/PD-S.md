# Pd–S phases

> Pd–S system: 10 phases (tier A 5, tier B 2, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PD-S.html · Markdown: https://data.orchid-project.org/phases/pages/PD-S.md

10 phases (tier A 5, tier B 2, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PD-S) · [full JSON](https://data.orchid-project.org/phases/systems/PD-S.json) · [Pd–S system page](https://data.orchid-project.org/systems/PD-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/PD-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pd–S system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-pd-s-a16-orthorhombic); _phase:pd-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–368.3 K, x(S) 1–1 | 0 | 1 |
| [BCC_A2](#phase-pd-s-bcc-a2); _phase:pd-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-pd-s-fcc-a1); _phase:pd-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1852.05 K, x(S) 0–0 | 2 | 1 |
| [HCP_A3](#phase-pd-s-hcp-a3); _phase:pd-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pd-s-liquid); _phase:pd-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(S) 0–1 | 10 | 1 |
| [PD16S7](#phase-pd-s-pd16s7); _phase:pd-s:pd16s7_ | Pd16S7 · cI46 · I-43m (217) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–917.23 K, x(S) 0.30435–0.30435 | 9 | 1 |
| [PD3S](#phase-pd-s-pd3s); _phase:pd-s:pd3s_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 836.33–918.75 K, x(S) 0.25–0.25 | 9 | 1 |
| [PD4S](#phase-pd-s-pd4s); _phase:pd-s:pd4s_ | Pd4Se · tP10 · P-42_1c (114) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1047.05 K, x(S) 0.2–0.2 | 11 | 1 |
| [PDS_B34](#phase-pd-s-pds-b34); _phase:pd-s:pds-b34_ | PdS · B34 · tP16 · P4_2/m (84) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1272.85 K, x(S) 0.5–0.5 | 9 | 1 |
| [MONOCLINIC_S](#phase-pd-s-s-monoclinic); _phase:pd-s:s-monoclinic_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 368.3–2499.55 K, x(S) 1–1 | 0 | 1 |

## ORTHORHOMBIC_A16 (Pd–S)

- Id: `phase:pd-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–368.3 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:pd-s:a16-orthorhombic  
_tdb: _tdb:PdS-10Hu.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): ORTHORHOMBIC_A16, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
48: PHASE ORTHORHOMBIC_A16 % 1 1 !
49: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase_

## BCC_A2 (Pd–S)

- Id: `phase:pd-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:bcc-a2)

Names (2): _corpus: _corpus:phase:pd-s:bcc-a2  
_tdb: _tdb:PdS-10Hu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): BCC_A2, type code %B, sha256 `11a6e85b5b6570eb…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : PD S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase_

## FCC_A1 (Pd–S)

- Id: `phase:pd-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1852.05 K, x(S) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:fcc-a1)

Names (3): _corpus: _corpus:phase:pd-s:fcc-a1  
_paper: _paper:10.1016/j.calphad.2010.07.002:(Pd)  
_tdb: _tdb:PdS-10Hu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): FCC_A1, type code %A, sha256 `11a6e85b5b6570eb…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : PD S : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645396](https://doi.org/10.1007/bf02645396) H Okamoto, Pd-s (palladium-sulfur), JPE 13, 106-107 (1992).  
_cited as the source of values for this phase_

## HCP_A3 (Pd–S)

- Id: `phase:pd-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:hcp-a3)

Names (2): _corpus: _corpus:phase:pd-s:hcp-a3  
_tdb: _tdb:PdS-10Hu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): HCP_A3, type code %A, sha256 `11a6e85b5b6570eb…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase_

## LIQUID (Pd–S)

- Id: `phase:pd-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(S) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:liquid)

Names (3): _corpus: _corpus:phase:pd-s:liquid  
_paper: _paper:10.1016/j.calphad.2010.07.002:L  
_tdb: _tdb:PdS-10Hu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): LIQUID, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : PD S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645396](https://doi.org/10.1007/bf02645396) H Okamoto, Pd-s (palladium-sulfur), JPE 13, 106-107 (1992).  
_cited as the source of values for this phase_

## PD16S7 (Pd–S)

- Id: `phase:pd-s:pd16s7`; status `assigned`
- Structure: Pd16S7 · cI46 · I-43m (217); type `st:pd16s7-ci46`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Pd 0.6957, S 0.3043
- Stability: stable in 1 of 1 calculated diagram(s): 300–917.23 K, x(S) 0.30435–0.30435
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:pd16s7)

Names (5): _corpus: _corpus:phase:pd-s:pd16s7  
_mp: _mp:mp-aaaaaapd  
_oqmd: _oqmd:oqmd-6171  
_paper: _paper:10.1016/j.calphad.2010.07.002:Pd16S7  
_tdb: _tdb:PdS-10Hu.tdb:PD16S7  


### TDB models of PD16S7 (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): PD16S7, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
68: PHASE PD16S7 % 2 16 7 !
69: CONST PD16S7 : PD : S : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645396](https://doi.org/10.1007/bf02645396) H Okamoto, Pd-s (palladium-sulfur), JPE 13, 106-107 (1992).  
_cited as the source of values for this phase_
- [doi:10.1006/jcht.1997.0328](https://doi.org/10.1006/jcht.1997.0328) A. Zubkov, T. Fujino, N. Sato, K. Yamada, Enthalpies of formation of the palladium sulphides, The Journal of Chemical Thermodynamics 30, 571-581 (1998).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02657499](https://doi.org/10.1007/bf02657499) Jeffrey R. Taylor, Phase relationships and thermodynamic properties of the Pd-S system, Metall Trans B 16, 143-148 (1985).  
_cited as the source of values for this phase_

## PD3S (Pd–S)

- Id: `phase:pd-s:pd3s`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_dft; dft_space_group_63_matches_6_structure_types; no_structure_token; sgte_mmc2_row_disagrees_with_dft
- Candidate (dft_mp): Cmcm (63) — on-hull MP Pd3S at x(S)=0.2500
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Pd3 S1 at x(S)=0.2500
- Candidate (dft_space_group_and_stoichiometry): (AgCa3) · oC16 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Cd3Er · oC16 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): CeZn3 · oC16 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): DyGe3 · oC16 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): Re3B · E1_a · oC16 · Cmcm (63) — space group 63 and stoichiometry match
- Candidate (dft_space_group_and_stoichiometry): NdTe3 · oC16 · Cmcm (63) — space group 63 and stoichiometry match
- Stoichiometry: Pd 0.7500, S 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 836.33–918.75 K, x(S) 0.25–0.25
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:pd3s)

Names (3): _corpus: _corpus:phase:pd-s:pd3s  
_paper: _paper:10.1016/j.calphad.2010.07.002:Pd3S  
_tdb: _tdb:PdS-10Hu.tdb:PD3S  


### TDB models of PD3S (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): PD3S, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
63: PHASE PD3S % 2 3 1 !
64: CONST PD3S : PD : S : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645396](https://doi.org/10.1007/bf02645396) H Okamoto, Pd-s (palladium-sulfur), JPE 13, 106-107 (1992).  
_cited as the source of values for this phase_
- [doi:10.1006/jcht.1997.0328](https://doi.org/10.1006/jcht.1997.0328) A. Zubkov, T. Fujino, N. Sato, K. Yamada, Enthalpies of formation of the palladium sulphides, The Journal of Chemical Thermodynamics 30, 571-581 (1998).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02657499](https://doi.org/10.1007/bf02657499) Jeffrey R. Taylor, Phase relationships and thermodynamic properties of the Pd-S system, Metall Trans B 16, 143-148 (1985).  
_cited as the source of values for this phase_

## PD4S (Pd–S)

- Id: `phase:pd-s:pd4s`; status `assigned`
- Structure: Pd4Se · tP10 · P-42_1c (114); type `st:pd4se-tp10`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Pd 0.8000, S 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1047.05 K, x(S) 0.2–0.2
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:pd4s)

Names (5): _corpus: _corpus:phase:pd-s:pd4s  
_mp: _mp:mp-aaaaalot  
_oqmd: _oqmd:oqmd-4447  
_paper: _paper:10.1016/j.calphad.2010.07.002:Pd4S  
_tdb: _tdb:PdS-10Hu.tdb:PD4S  


### TDB models of PD4S (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): PD4S, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
58: PHASE PD4S % 2 4 1 !
59: CONST PD4S : PD : S : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645396](https://doi.org/10.1007/bf02645396) H Okamoto, Pd-s (palladium-sulfur), JPE 13, 106-107 (1992).  
_cited as the source of values for this phase_
- [doi:10.1246/bcsj.35.1543](https://doi.org/10.1246/bcsj.35.1543) Kichizo Niwa, Toshio Yokokawa, Toshiro Isoya, Equilibria in the PdS–H2–Pd4S–H2S and Pd4S–H2–Pd–H2S Systems, Bulletin of the Chemical Society of Japan 35, 1543-1545 (1962).  
_cited as the source of values for this phase_
- [doi:10.1006/jcht.1997.0328](https://doi.org/10.1006/jcht.1997.0328) A. Zubkov, T. Fujino, N. Sato, K. Yamada, Enthalpies of formation of the palladium sulphides, The Journal of Chemical Thermodynamics 30, 571-581 (1998).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02657499](https://doi.org/10.1007/bf02657499) Jeffrey R. Taylor, Phase relationships and thermodynamic properties of the Pd-S system, Metall Trans B 16, 143-148 (1985).  
_cited as the source of values for this phase_

## PDS_B34 (Pd–S)

- Id: `phase:pd-s:pds-b34`; status `assigned`
- Structure: PdS · B34 · tP16 · P4_2/m (84); type `st:b34-pds-tp16`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1272.85 K, x(S) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:pds-b34)

Names (3): _corpus: _corpus:phase:pd-s:pds-b34  
_paper: _paper:10.1016/j.calphad.2010.07.002:PdS  
_tdb: _tdb:PdS-10Hu.tdb:PDS_B34  


### TDB models of PDS_B34 (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): PDS_B34, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
73: PHASE PDS_B34 % 2 1 1 !
74: CONST PDS_B34 : PD : S : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02645396](https://doi.org/10.1007/bf02645396) H Okamoto, Pd-s (palladium-sulfur), JPE 13, 106-107 (1992).  
_cited as the source of values for this phase_
- [doi:10.1246/bcsj.35.1543](https://doi.org/10.1246/bcsj.35.1543) Kichizo Niwa, Toshio Yokokawa, Toshiro Isoya, Equilibria in the PdS–H2–Pd4S–H2S and Pd4S–H2–Pd–H2S Systems, Bulletin of the Chemical Society of Japan 35, 1543-1545 (1962).  
_cited as the source of values for this phase_
- [doi:10.1006/jcht.1997.0328](https://doi.org/10.1006/jcht.1997.0328) A. Zubkov, T. Fujino, N. Sato, K. Yamada, Enthalpies of formation of the palladium sulphides, The Journal of Chemical Thermodynamics 30, 571-581 (1998).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02657499](https://doi.org/10.1007/bf02657499) Jeffrey R. Taylor, Phase relationships and thermodynamic properties of the Pd-S system, Metall Trans B 16, 143-148 (1985).  
_cited as the source of values for this phase_

## MONOCLINIC_S (Pd–S)

- Id: `phase:pd-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — PdS-10Hu.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 368.3–2499.55 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-s:s-monoclinic)

Names (2): _corpus: _corpus:phase:pd-s:s-monoclinic  
_tdb: _tdb:PdS-10Hu.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[PdS-10Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/PdS-10Hu.tdb): MONOCLINIC_S, type code %, sha256 `11a6e85b5b6570eb…`

~~~~text
53: PHASE MONOCLINIC_S % 1 1 !
54: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2010.07.002](https://doi.org/10.1016/j.calphad.2010.07.002) Rongxiang Hu, Michael C. Gao, Ömer N. Doğan, Paul King, Michael Widom, Thermodynamic modeling of the Pd–S system supported by first-principles calculations, Calphad 34, 324-331 (2010).  
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
