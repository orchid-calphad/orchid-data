# C–Ta phases

> C–Ta system: 7 phases (tier A 4, liquid 1, needs_review 1, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/C-TA.html · Markdown: https://data.orchid-project.org/phases/pages/C-TA.md

7 phases (tier A 4, liquid 1, needs_review 1, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=C-TA) · [full JSON](https://data.orchid-project.org/phases/systems/C-TA.json) · [C–Ta system page](https://data.orchid-project.org/systems/C-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/C-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the C–Ta system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-c-ta-a4-diamond); _phase:c-ta:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GRAPHITE_A9](#phase-c-ta-a9-graphite); _phase:c-ta:a9-graphite_ | C (graphite) · A9 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 1–1 | 2 | 3 |
| [BCC_A2](#phase-c-ta-bcc-a2); _phase:c-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3289.99 K, x(C) 0–0.08363 | 2 | 3 |
| [FCC_A1](#phase-c-ta-fcc-a1); _phase:c-ta:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 0.37866–0.5 | 6 | 3 |
| [HCP_A3](#phase-c-ta-hcp-a3); _phase:c-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3635.99 K, x(C) 0.27446–0.33333 | 4 | 3 |
| [LIQUID](#phase-c-ta-liquid); _phase:c-ta:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 3073.71–4000 K, x(C) 0–0.75326 | 8 | 3 |
| [TA4C3](#phase-c-ta-ta4c3); _phase:c-ta:ta4c3_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2442.8 K, x(C) 0.386–0.4 | 0 | 2 |

## DIAMOND_A4 (C–Ta)

- Id: `phase:c-ta:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:a4-diamond)

Names (4): _corpus: _corpus:phase:c-ta:a4-diamond  
_tdb: _tdb:TaC-16Pan.tdb:DIAMOND_A4, tdb:TaC-17Zha.tdb:DIAMOND_A4, tdb:TaC-96Fri-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): DIAMOND_A4, type code %, sha256 `ca6090d1f360ccc3…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : C : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): DIAMOND_A4, type code %, sha256 `3552b962491e2504…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : C : !
~~~~

[TaC-96Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-96Fri-LB.tdb): DIAMOND_A4, type code %, sha256 `1f785b985585aadd…`

~~~~text
53: PHASE DIAMOND_A4 % 1 1 !
54: CONST DIAMOND_A4 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(96)02197-4](https://doi.org/10.1016/0925-8388%2896%2902197-4) K. Frisk, A. Fernández Guillermet, Gibbs energy coupling of the phase diagram and thermochemistry in the tantalum-carbon system, Journal of Alloys and Compounds 238, 167-179 (1996).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
_assessment that models this phase_

## GRAPHITE_A9 (C–Ta)

- Id: `phase:c-ta:a9-graphite`; status `assigned`
- Structure: C (graphite) · A9 · hP4 · P6_3/mmc (194); type `st:a9-c-graphite-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: C 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:a9-graphite)

Names (5): _corpus: _corpus:phase:c-ta:a9-graphite  
_paper: _paper:10.1016/0925-8388(96)02197-4:gr  
_tdb: _tdb:TaC-16Pan.tdb:GRAPHITE_A9, tdb:TaC-17Zha.tdb:GRAPHITE_A9, tdb:TaC-96Fri-LB.tdb:GRAPHITE_A9  


### TDB models of GRAPHITE_A9 (3): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): GRAPHITE_A9, type code %, sha256 `ca6090d1f360ccc3…`

~~~~text
46: PHASE GRAPHITE_A9 % 1 1 !
47: CONST GRAPHITE_A9 : C : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): GRAPHITE_A9, type code %, sha256 `3552b962491e2504…`

~~~~text
47: PHASE GRAPHITE_A9 % 1 1 !
48: CONST GRAPHITE_A9 : C : !
~~~~

[TaC-96Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-96Fri-LB.tdb): GRAPHITE_A9, type code %, sha256 `1f785b985585aadd…`

~~~~text
58: PHASE GRAPHITE_A9 % 1 1 !
59: CONST GRAPHITE_A9 : C : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(96)02197-4](https://doi.org/10.1016/0925-8388%2896%2902197-4) K. Frisk, A. Fernández Guillermet, Gibbs energy coupling of the phase diagram and thermochemistry in the tantalum-carbon system, Journal of Alloys and Compounds 238, 167-179 (1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
_assessment that models this phase_

## BCC_A2 (C–Ta)

- Id: `phase:c-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3289.99 K, x(C) 0–0.08363
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:bcc-a2)

Names (5): _corpus: _corpus:phase:c-ta:bcc-a2  
_paper: _paper:10.1016/0925-8388(96)02197-4:B.c.c.  
_tdb: _tdb:TaC-16Pan.tdb:BCC_A2, tdb:TaC-17Zha.tdb:BCC_A2, tdb:TaC-96Fri-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): BCC_A2, type code %B, sha256 `ca6090d1f360ccc3…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : TA : C VA% : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): BCC_A2, type code %B, sha256 `3552b962491e2504…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : TA : C VA% : !
~~~~

[TaC-96Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-96Fri-LB.tdb): BCC_A2, type code %B, sha256 `1f785b985585aadd…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : TA : C VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(96)02197-4](https://doi.org/10.1016/0925-8388%2896%2902197-4) K. Frisk, A. Fernández Guillermet, Gibbs energy coupling of the phase diagram and thermochemistry in the tantalum-carbon system, Journal of Alloys and Compounds 238, 167-179 (1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
_assessment that models this phase_

## FCC_A1 (C–Ta)

- Id: `phase:c-ta:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(C) 0.37866–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:fcc-a1)

Names (5): _corpus: _corpus:phase:c-ta:fcc-a1  
_paper: _paper:10.1016/0925-8388(96)02197-4:TaC  
_tdb: _tdb:TaC-16Pan.tdb:FCC_A1, tdb:TaC-17Zha.tdb:FCC_A1, tdb:TaC-96Fri-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): FCC_A1, type code %A, sha256 `ca6090d1f360ccc3…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : TA : C% VA : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): FCC_A1, type code %A, sha256 `3552b962491e2504…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : TA : C% VA : !
~~~~

[TaC-96Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-96Fri-LB.tdb): FCC_A1, type code %A, sha256 `1f785b985585aadd…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : TA : C% VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(96)02197-4](https://doi.org/10.1016/0925-8388%2896%2902197-4) K. Frisk, A. Fernández Guillermet, Gibbs energy coupling of the phase diagram and thermochemistry in the tantalum-carbon system, Journal of Alloys and Compounds 238, 167-179 (1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
_assessment that models this phase_

## HCP_A3 (C–Ta)

- Id: `phase:c-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3635.99 K, x(C) 0.27446–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:hcp-a3)

Names (5): _corpus: _corpus:phase:c-ta:hcp-a3  
_paper: _paper:10.1016/0925-8388(96)02197-4:Ta2C  
_tdb: _tdb:TaC-16Pan.tdb:HCP_A3, tdb:TaC-17Zha.tdb:HCP_A3, tdb:TaC-96Fri-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): HCP_A3, type code %A, sha256 `ca6090d1f360ccc3…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : TA : C% VA : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): HCP_A3, type code %A, sha256 `3552b962491e2504…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : TA : C% VA : !
~~~~

[TaC-96Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-96Fri-LB.tdb): HCP_A3, type code %A, sha256 `1f785b985585aadd…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : TA : C% VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(96)02197-4](https://doi.org/10.1016/0925-8388%2896%2902197-4) K. Frisk, A. Fernández Guillermet, Gibbs energy coupling of the phase diagram and thermochemistry in the tantalum-carbon system, Journal of Alloys and Compounds 238, 167-179 (1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
_assessment that models this phase_

## LIQUID (C–Ta)

- Id: `phase:c-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 3073.71–4000 K, x(C) 0–0.75326
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:liquid)

Names (5): _corpus: _corpus:phase:c-ta:liquid  
_paper: _paper:10.1016/0925-8388(96)02197-4:L  
_tdb: _tdb:TaC-16Pan.tdb:LIQUID, tdb:TaC-17Zha.tdb:LIQUID, tdb:TaC-96Fri-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): LIQUID, type code %, sha256 `ca6090d1f360ccc3…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : C TA : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): LIQUID, type code %, sha256 `3552b962491e2504…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : C TA : !
~~~~

[TaC-96Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-96Fri-LB.tdb): LIQUID, type code %, sha256 `1f785b985585aadd…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : C TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/0925-8388(96)02197-4](https://doi.org/10.1016/0925-8388%2896%2902197-4) K. Frisk, A. Fernández Guillermet, Gibbs energy coupling of the phase diagram and thermochemistry in the tantalum-carbon system, Journal of Alloys and Compounds 238, 167-179 (1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
_assessment that models this phase_

## TA4C3 (C–Ta)

- Id: `phase:c-ta:ta4c3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:models_disagree_on_composition; models_disagree_on_composition; no_structure_token
- Candidate (sgte_mmc2): In3Te4 · hR7 · R-3m (166) — Hallstedt 2025 mmc2 row for TA4C3: Ta4C3
- Candidate (sgte_mmc2): In3Te4 · hR7 · R-3m (166) — Hallstedt 2025 mmc2 row for TA4C3: Ta4C3 (or rather Ta3C2)
- Candidate (tdb_comment): In3Te4 · hR7 · R-3m — TaC-16Pan.tdb: 'Prototype In3Te4 (hR7, R-3m)'
- Candidate (tdb_comment): In3Te4 · hR7 · R-3m — TaC-17Zha.tdb: 'Prototype In3Te4 (hR7, R-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–2442.8 K, x(C) 0.386–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:c-ta:ta4c3)

Names (3): _corpus: _corpus:phase:c-ta:ta4c3  
_tdb: _tdb:TaC-16Pan.tdb:TA4C3, tdb:TaC-17Zha.tdb:TA4C3  


### TDB models of TA4C3 (2): PHASE and CONSTITUENT statements as written

[TaC-16Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-16Pan.tdb): TA4C3, type code %, sha256 `ca6090d1f360ccc3…`

~~~~text
51: PHASE TA4C3 % 2 0.614 0.386 !
52: CONST TA4C3 : TA : C : !
~~~~

[TaC-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/TaC-17Zha.tdb): TA4C3, type code %, sha256 `3552b962491e2504…`

~~~~text
52: PHASE TA4C3 % 2 3 2 !
53: CONST TA4C3 : TA : C : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.02.001](https://doi.org/10.1016/j.calphad.2016.02.001) Y. Pan, P. Zhou, Y. Peng, Y. Du, F. Luo, Calphad, 53, 1-9(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2017.09.003](https://doi.org/10.1016/j.calphad.2017.09.003) C. Zhang, H. Yin, Y. Du, Y. Pan, P. Deng, Calphad, 59, 99-1069(2017).  
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
