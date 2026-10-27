# Np–Zr phases

> Np–Zr system: 8 phases (tier A 5, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NP-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/NP-ZR.md

8 phases (tier A 5, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NP-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/NP-ZR.json) · [Np–Zr system page](https://data.orchid-project.org/systems/NP-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/NP-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Np–Zr system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAG_AD](#phase-np-zr-ad-tetrag); _phase:np-zr:ad-tetrag_ | beta-Np · A_d · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 551.48–880.13 K, x(Zr) 0–0.02097 | 6 | 4 |
| [BCC_A2](#phase-np-zr-bcc-a2); _phase:np-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 695.13–3999.1 K, x(Zr) 0–1 | 4 | 4 |
| [UZR2_DELTA](#phase-np-zr-delta-uzr2); _phase:np-zr:delta-uzr2_ | Hg2U · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–4000 K, x(Zr) 0.33334–0.83881 | 8 | 4 |
| [FCC_A1](#phase-np-zr-fcc-a1); _phase:np-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-np-zr-hcp-a3); _phase:np-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2123.99 K, x(Zr) 0.93672–1 | 6 | 4 |
| [LIQUID](#phase-np-zr-liquid); _phase:np-zr:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 881.96–4000 K, x(Zr) 0–1 | 2 | 4 |
| [NP4ZR_THETA](#phase-np-zr-np4zr-theta); _phase:np-zr:np4zr-theta_ | Pu4Zr · tP80 · P4/ncc (130) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 4 of 4 calculated diagram(s): 300–600 K, x(Zr) 0.2–0.2 | 4 | 4 |
| [ORTHO_AC](#phase-np-zr-ortho-ac); _phase:np-zr:ortho-ac_ | alpha-Np · A_c · oP8 · Pnma (62) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–562.48 K, x(Zr) 0–0.00585 | 2 | 4 |

## TETRAG_AD (Np–Zr)

- Id: `phase:np-zr:ad-tetrag`; status `assigned`
- Structure: beta-Np · A_d · tP4 · P4/nmm (129); type `st:a-d-beta-np-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 551.48–880.13 K, x(Zr) 0–0.02097
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:ad-tetrag)

Names (7): _corpus: _corpus:phase:np-zr:ad-tetrag, corpus:phase:np-zr:tetrag-ad  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:β-Np  
_tdb: _tdb:NpZr-10Kur.tdb:TETRAG_AD, tdb:NpZr-11Baj.tdb:TETRAG_AD, tdb:NpZr-14Xio.tdb:TETRAG_AD, tdb:NpZr-18Xie.tdb:TETRAG_AD  


### TDB models of TETRAG_AD (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): TETRAG_AD, type code %, sha256 `c70b656655da30f9…`

~~~~text
50: PHASE TETRAG_AD % 1 1 !
51: CONST TETRAG_AD : NP% ZR : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): TETRAG_AD, type code %, sha256 `ce3d595af559b9dc…`

~~~~text
48: PHASE TETRAG_AD % 1 1 !
49: CONST TETRAG_AD : NP% ZR : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): TETRAG_AD, type code %, sha256 `a50b3a238908cb6b…`

~~~~text
48: PHASE TETRAG_AD % 1 1 !
49: CONST TETRAG_AD : NP% ZR : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): TETRAG_AD, type code %, sha256 `df1afba7ad73bcfc…`

~~~~text
52: PHASE TETRAG_AD % 1 1 !
53: CONST TETRAG_AD : NP% ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## BCC_A2 (Np–Zr)

- Id: `phase:np-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 695.13–3999.1 K, x(Zr) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:bcc-a2)

Names (6): _corpus: _corpus:phase:np-zr:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:β-Zr  
_tdb: _tdb:NpZr-10Kur.tdb:BCC_A2, tdb:NpZr-11Baj.tdb:BCC_A2, tdb:NpZr-14Xio.tdb:BCC_A2, tdb:NpZr-18Xie.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): BCC_A2, type code %B, sha256 `c70b656655da30f9…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NP% ZR% : VA : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): BCC_A2, type code %B, sha256 `ce3d595af559b9dc…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NP% ZR% : VA : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): BCC_A2, type code %B, sha256 `a50b3a238908cb6b…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NP% ZR% : VA : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): BCC_A2, type code %B, sha256 `df1afba7ad73bcfc…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : NP% ZR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## UZR2_DELTA (Np–Zr)

- Id: `phase:np-zr:delta-uzr2`; status `assigned`
- Structure: Hg2U · hP3 · P6/mmm (191); type `st:hg2u-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:UZR2, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 4 of 4 calculated diagram(s): 300–4000 K, x(Zr) 0.33334–0.83881
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:delta-uzr2)

Names (7): _corpus: _corpus:phase:np-zr:delta-uzr2, corpus:phase:np-zr:uzr2-delta  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:δ-NpZr2  
_tdb: _tdb:NpZr-10Kur.tdb:UZR2_DELTA, tdb:NpZr-11Baj.tdb:UZR2_DELTA, tdb:NpZr-14Xio.tdb:UZR2_DELTA, tdb:NpZr-18Xie.tdb:UZR2_DELTA  


### TDB models of UZR2_DELTA (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): UZR2_DELTA, type code %, sha256 `c70b656655da30f9…`

~~~~text
61: PHASE UZR2_DELTA % 2 1 2 !
62: CONST UZR2_DELTA : NP% ZR : NP ZR% : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): UZR2_DELTA, type code %, sha256 `ce3d595af559b9dc…`

~~~~text
59: PHASE UZR2_DELTA % 2 1 2 !
60: CONST UZR2_DELTA : ZR : NP ZR : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): UZR2_DELTA, type code %, sha256 `a50b3a238908cb6b…`

~~~~text
59: PHASE UZR2_DELTA % 2 1 2 !
60: CONST UZR2_DELTA : ZR : NP ZR : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): UZR2_DELTA, type code %, sha256 `df1afba7ad73bcfc…`

~~~~text
63: PHASE UZR2_DELTA % 2 1 2 !
64: CONST UZR2_DELTA : ZR : NP ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## FCC_A1 (Np–Zr)

- Id: `phase:np-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:fcc-a1)

Names (5): _corpus: _corpus:phase:np-zr:fcc-a1  
_tdb: _tdb:NpZr-10Kur.tdb:FCC_A1, tdb:NpZr-11Baj.tdb:FCC_A1, tdb:NpZr-14Xio.tdb:FCC_A1, tdb:NpZr-18Xie.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): FCC_A1, type code %A, sha256 `c70b656655da30f9…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NP ZR : VA : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): FCC_A1, type code %A, sha256 `ce3d595af559b9dc…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : ZR : VA : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): FCC_A1, type code %A, sha256 `a50b3a238908cb6b…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : ZR : VA : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): FCC_A1, type code %A, sha256 `df1afba7ad73bcfc…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : ZR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## HCP_A3 (Np–Zr)

- Id: `phase:np-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2123.99 K, x(Zr) 0.93672–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:hcp-a3)

Names (6): _corpus: _corpus:phase:np-zr:hcp-a3  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:α-Zr  
_tdb: _tdb:NpZr-10Kur.tdb:HCP_A3, tdb:NpZr-11Baj.tdb:HCP_A3, tdb:NpZr-14Xio.tdb:HCP_A3, tdb:NpZr-18Xie.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): HCP_A3, type code %A, sha256 `c70b656655da30f9…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : NP ZR% : VA : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): HCP_A3, type code %A, sha256 `ce3d595af559b9dc…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NP ZR% : VA : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): HCP_A3, type code %A, sha256 `a50b3a238908cb6b…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NP ZR% : VA : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): HCP_A3, type code %A, sha256 `df1afba7ad73bcfc…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : NP ZR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## LIQUID (Np–Zr)

- Id: `phase:np-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 881.96–4000 K, x(Zr) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:liquid)

Names (6): _corpus: _corpus:phase:np-zr:liquid  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:L  
_tdb: _tdb:NpZr-10Kur.tdb:LIQUID, tdb:NpZr-11Baj.tdb:LIQUID, tdb:NpZr-14Xio.tdb:LIQUID, tdb:NpZr-18Xie.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): LIQUID, type code %, sha256 `c70b656655da30f9…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : NP ZR : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): LIQUID, type code %, sha256 `ce3d595af559b9dc…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NP ZR : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): LIQUID, type code %, sha256 `a50b3a238908cb6b…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NP ZR : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): LIQUID, type code %, sha256 `df1afba7ad73bcfc…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : NP ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## NP4ZR_THETA (Np–Zr)

- Id: `phase:np-zr:np4zr-theta`; status `assigned`
- Structure: Pu4Zr · tP80 · P4/ncc (130); type `st:pu4zr-tp80`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Np 0.8000, Zr 0.2000
- Stability: stable in 4 of 4 calculated diagram(s): 300–600 K, x(Zr) 0.2–0.2
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:np4zr-theta)

Names (6): _corpus: _corpus:phase:np-zr:np4zr-theta  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:θ-Np4Zr  
_tdb: _tdb:NpZr-10Kur.tdb:NP4ZR_THETA, tdb:NpZr-11Baj.tdb:NP4ZR_THETA, tdb:NpZr-14Xio.tdb:NP4ZR_THETA, tdb:NpZr-18Xie.tdb:NP4ZR_THETA  


### TDB models of NP4ZR_THETA (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): NP4ZR_THETA, type code %, sha256 `c70b656655da30f9…`

~~~~text
55: PHASE NP4ZR_THETA % 2 4 1 !
56: CONST NP4ZR_THETA : NP : ZR : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): NP4ZR_THETA, type code %, sha256 `ce3d595af559b9dc…`

~~~~text
53: PHASE NP4ZR_THETA % 2 4 1 !
54: CONST NP4ZR_THETA : NP : ZR : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): NP4ZR_THETA, type code %, sha256 `a50b3a238908cb6b…`

~~~~text
53: PHASE NP4ZR_THETA % 2 4 1 !
54: CONST NP4ZR_THETA : NP : ZR : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): NP4ZR_THETA, type code %, sha256 `df1afba7ad73bcfc…`

~~~~text
57: PHASE NP4ZR_THETA % 2 4 1 !
58: CONST NP4ZR_THETA : NP : ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

## ORTHO_AC (Np–Zr)

- Id: `phase:np-zr:ortho-ac`; status `assigned`
- Structure: alpha-Np · A_c · oP8 · Pnma (62); type `st:a-c-alpha-np-op8`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–562.48 K, x(Zr) 0–0.00585
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-zr:ortho-ac)

Names (6): _corpus: _corpus:phase:np-zr:ortho-ac  
_paper: _paper:10.1016/j.jnucmat.2010.10.085:α-Np  
_tdb: _tdb:NpZr-10Kur.tdb:ORTHO_AC, tdb:NpZr-11Baj.tdb:ORTHO_AC, tdb:NpZr-14Xio.tdb:ORTHO_AC, tdb:NpZr-18Xie.tdb:ORTHO_AC  


### TDB models of ORTHO_AC (4): PHASE and CONSTITUENT statements as written

[NpZr-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-10Kur.tdb): ORTHO_AC, type code %, sha256 `c70b656655da30f9…`

~~~~text
45: PHASE ORTHO_AC % 1 1 !
46: CONST ORTHO_AC : NP% ZR : !
~~~~

[NpZr-11Baj.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-11Baj.tdb): ORTHO_AC, type code %, sha256 `ce3d595af559b9dc…`

~~~~text
43: PHASE ORTHO_AC % 1 1 !
44: CONST ORTHO_AC : NP% ZR : !
~~~~

[NpZr-14Xio.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-14Xio.tdb): ORTHO_AC, type code %, sha256 `a50b3a238908cb6b…`

~~~~text
43: PHASE ORTHO_AC % 1 1 !
44: CONST ORTHO_AC : NP% ZR : !
~~~~

[NpZr-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpZr-18Xie.tdb): ORTHO_AC, type code %, sha256 `df1afba7ad73bcfc…`

~~~~text
47: PHASE ORTHO_AC % 1 1 !
48: CONST ORTHO_AC : NP% ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2010.10.085](https://doi.org/10.1016/j.jnucmat.2010.10.085) Saurabh Bajaj, Andres Garay, Alexander Landa, Per Söderlind, Patrice Turchi, Raymundo Arróyave, Thermodynamic study of the Np–Zr system, Journal of Nuclear Materials 409, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.06.023](https://doi.org/10.1016/j.jnucmat.2014.06.023) Wei Xiong, Wei Xie, Dane Morgan, Thermodynamic evaluation of the Np–Zr system using CALPHAD and ab initio methods, Journal of Nuclear Materials 452, 569-577 (2014).  
_assessment that models this phase_

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
