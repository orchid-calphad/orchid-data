# Ga–Sc phases

> Ga–Sc system: 10 phases (tier A 6, tier C 3, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-SC.html · Markdown: https://data.orchid-project.org/phases/pages/GA-SC.md

10 phases (tier A 6, tier C 3, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-SC) · [full JSON](https://data.orchid-project.org/phases/systems/GA-SC.json) · [Ga–Sc system page](https://data.orchid-project.org/systems/GA-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Sc system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-sc-a11-orthorhombic); _phase:ga-sc:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Sc) 0–0 | 2 | 1 |
| [BCC_A2](#phase-ga-sc-bcc-a2); _phase:ga-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1607.99–2499.24 K, x(Sc) 1–1 | 0 | 1 |
| [FCC_A1](#phase-ga-sc-fcc-a1); _phase:ga-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GA2SC](#phase-ga-sc-ga2sc); _phase:ga-sc:ga2sc_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1422.72 K, x(Sc) 0.33333–0.33333 | 6 | 1 |
| [GA3SC_L12](#phase-ga-sc-ga3sc-l12); _phase:ga-sc:ga3sc-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1303.59 K, x(Sc) 0.25–0.25 | 4 | 1 |
| [GA3SC5](#phase-ga-sc-ga3sc5); _phase:ga-sc:ga3sc5_ | Ga3Y5 · mC32 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1710.7 K, x(Sc) 0.625–0.625 | 6 | 1 |
| [GA4SC5](#phase-ga-sc-ga4sc5); _phase:ga-sc:ga4sc5_ | Ge10Ho11 · tI84 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1509.27 K, x(Sc) 0.55556–0.55556 | 4 | 1 |
| [GASC_B33](#phase-ga-sc-gasc-b33); _phase:ga-sc:gasc-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1372.01 K, x(Sc) 0.5–0.5 | 4 | 1 |
| [HCP_A3](#phase-ga-sc-hcp-a3); _phase:ga-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1812.99 K, x(Sc) 1–1 | 2 | 1 |
| [LIQUID](#phase-ga-sc-liquid); _phase:ga-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Sc) 0–1 | 16 | 1 |

## ORTHORHOMBIC_A11 (Ga–Sc)

- Id: `phase:ga-sc:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Sc) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:a11-orthorhombic)

Names (4): _corpus: _corpus:phase:ga-sc:a11-orthorhombic, corpus:phase:ga-sc:orthorhombic-a11  
_paper: _paper:10.1016/j.jallcom.2007.09.067:orth(Ga)  
_tdb: _tdb:GaSc-08Jun.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d874299ef43a14d4…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## BCC_A2 (Ga–Sc)

- Id: `phase:ga-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1607.99–2499.24 K, x(Sc) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-sc:bcc-a2  
_tdb: _tdb:GaSc-08Jun.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): BCC_A2, type code %B, sha256 `d874299ef43a14d4…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GA SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase_

## FCC_A1 (Ga–Sc)

- Id: `phase:ga-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-sc:fcc-a1  
_tdb: _tdb:GaSc-08Jun.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): FCC_A1, type code %A, sha256 `d874299ef43a14d4…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GA SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase_

## GA2SC (Ga–Sc)

- Id: `phase:ga-sc:ga2sc`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.6667, Sc 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1422.72 K, x(Sc) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:ga2sc)

Names (3): _corpus: _corpus:phase:ga-sc:ga2sc  
_paper: _paper:10.1016/j.jallcom.2007.09.067:ScGa2  
_tdb: _tdb:GaSc-08Jun.tdb:GA2SC  


### TDB models of GA2SC (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): GA2SC, type code %, sha256 `d874299ef43a14d4…`

~~~~text
53: PHASE GA2SC % 2 2 1 !
54: CONST GA2SC : GA : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA3SC_L12 (Ga–Sc)

- Id: `phase:ga-sc:ga3sc-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabjw and oqmd-30346, space group 221
- Stoichiometry: Ga 0.7500, Sc 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1303.59 K, x(Sc) 0.25–0.25
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:ga3sc-l12)

Names (5): _corpus: _corpus:phase:ga-sc:ga3sc-l12  
_mp: _mp:mp-aaaaabjw  
_oqmd: _oqmd:oqmd-30346  
_paper: _paper:10.1016/j.jallcom.2007.09.067:ScGa3  
_tdb: _tdb:GaSc-08Jun.tdb:GA3SC_L12  


### TDB models of GA3SC_L12 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): GA3SC_L12, type code %, sha256 `d874299ef43a14d4…`

~~~~text
48: PHASE GA3SC_L12 % 2 3 1 !
49: CONST GA3SC_L12 : GA : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA3SC5 (Ga–Sc)

- Id: `phase:ga-sc:ga3sc5`; status `assigned`
- Structure: Ga3Y5 · mC32 · C2/m (12); type `st:ga3y5-mc32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.3750, Sc 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1710.7 K, x(Sc) 0.625–0.625
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:ga3sc5)

Names (3): _corpus: _corpus:phase:ga-sc:ga3sc5  
_paper: _paper:10.1016/j.jallcom.2007.09.067:Sc5Ga3  
_tdb: _tdb:GaSc-08Jun.tdb:GA3SC5  


### TDB models of GA3SC5 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): GA3SC5, type code %, sha256 `d874299ef43a14d4…`

~~~~text
68: PHASE GA3SC5 % 2 3 5 !
69: CONST GA3SC5 : GA : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GA4SC5 (Ga–Sc)

- Id: `phase:ga-sc:ga4sc5`; status `assigned`
- Structure: Ge10Ho11 · tI84 · I4/mmm (139); type `st:ge10ho11-ti84`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.4444, Sc 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–1509.27 K, x(Sc) 0.55556–0.55556
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:ga4sc5)

Names (3): _corpus: _corpus:phase:ga-sc:ga4sc5  
_paper: _paper:10.1016/j.jallcom.2007.09.067:Sc5Ga4  
_tdb: _tdb:GaSc-08Jun.tdb:GA4SC5  


### TDB models of GA4SC5 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): GA4SC5, type code %, sha256 `d874299ef43a14d4…`

~~~~text
63: PHASE GA4SC5 % 2 4 5 !
64: CONST GA4SC5 : GA : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## GASC_B33 (Ga–Sc)

- Id: `phase:ga-sc:gasc-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaqwx and oqmd-30345, space group 63
- Stoichiometry: Ga 0.5000, Sc 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1372.01 K, x(Sc) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:gasc-b33)

Names (5): _corpus: _corpus:phase:ga-sc:gasc-b33  
_mp: _mp:mp-aaaaaqwx  
_oqmd: _oqmd:oqmd-30345  
_paper: _paper:10.1016/j.jallcom.2007.09.067:ScGa  
_tdb: _tdb:GaSc-08Jun.tdb:GASC_B33  


### TDB models of GASC_B33 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): GASC_B33, type code %, sha256 `d874299ef43a14d4…`

~~~~text
58: PHASE GASC_B33 % 2 1 1 !
59: CONST GASC_B33 : GA : SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## HCP_A3 (Ga–Sc)

- Id: `phase:ga-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1812.99 K, x(Sc) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:hcp-a3)

Names (3): _corpus: _corpus:phase:ga-sc:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2007.09.067:hcp(Sc)  
_tdb: _tdb:GaSc-08Jun.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): HCP_A3, type code %, sha256 `d874299ef43a14d4…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : GA SC% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
_cited as the source of values for this phase_

## LIQUID (Ga–Sc)

- Id: `phase:ga-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Sc) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-sc:liquid)

Names (3): _corpus: _corpus:phase:ga-sc:liquid  
_paper: _paper:10.1016/j.jallcom.2007.09.067:L  
_tdb: _tdb:GaSc-08Jun.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaSc-08Jun.tdb](https://orchid-project.org/data/databases/sgte-binary/GaSc-08Jun.tdb): LIQUID, type code %, sha256 `d874299ef43a14d4…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GA SC : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.067](https://doi.org/10.1016/j.jallcom.2007.09.067) Z.K. Jun, L.B. Liu, H.S. Liu, X.M. Huang, Z.P. Jin, Thermodynamic assessment of the Ga–Sc and Ga–Tb systems, Journal of Alloys and Compounds 463, 511-515 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(79)90170-x](https://doi.org/10.1016/0022-5088%2879%2990170-x) S.P Yatsenko, A.A Semyannikov, B.G Semenov, K.A Chuntonov, Phase diagrams of rare earth metals with gallium, Journal of the Less Common Metals 64, 185-199 (1979).  
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
