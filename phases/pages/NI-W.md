# Ni–W phases

> Ni–W system: 9 phases (tier A 4, tier C 2, liquid 1, needs_review 2); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-W.html · Markdown: https://data.orchid-project.org/phases/pages/NI-W.md

9 phases (tier A 4, tier C 2, liquid 1, needs_review 2); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-W) · [full JSON](https://data.orchid-project.org/phases/systems/NI-W.json) · [Ni–W system page](https://data.orchid-project.org/systems/NI-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–W system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ni-w-bcc-a2); _phase:ni-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.86 K, x(W) 0.9917–1 | 5 | 3 |
| [NI4X_D1A](#phase-ni-w-d1a-ni4x); _phase:ni-w:d1a-ni4x_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 304.84–1290 K, x(W) 0.2–0.2 | 15 | 3 |
| [FCC_A1](#phase-ni-w-fcc-a1); _phase:ni-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1790.73 K, x(W) 0–0.17637 | 6 | 3 |
| [HCP_A3](#phase-ni-w-hcp-a3); _phase:ni-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ni-w-liquid); _phase:ni-w:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1728.25–4000 K, x(W) 0–1 | 1 | 3 |
| [NI3W_D0A](#phase-ni-w-ni3w-d0a); _phase:ni-w:ni3w-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–848.8 K, x(W) 0.25–0.25 | 0 | 1 |
| [NI8W](#phase-ni-w-ni8w); _phase:ni-w:ni8w_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–802.5 K, x(W) 0.11111–0.11111 | 0 | 1 |
| [NIW](#phase-ni-w-niw); _phase:ni-w:niw_ | MoNi · oP56 · P2_12_12_1 (19) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1340.8 K, x(W) 0.5–0.5 | 10 | 2 |
| [NIW2](#phase-ni-w-niw2); _phase:ni-w:niw2_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–1340 K, x(W) 0.66667–0.66667 | 2 | 2 |

## BCC_A2 (Ni–W)

- Id: `phase:ni-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.86 K, x(W) 0.9917–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:bcc-a2)

Names (5): _corpus: _corpus:phase:ni-w:bcc-a2  
_paper: _paper:10.1007/bf02817278:bcc(W)  
_tdb: _tdb:NiW-08Pop.tdb:BCC_A2, tdb:NiW-17Iso.tdb:BCC_A2, tdb:NiW-86Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): BCC_A2, type code %B, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : NI W% : VA : !
~~~~

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): BCC_A2, type code %B, sha256 `feb57ad6eaab269b…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : NI W% : VA : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): BCC_A2, type code %B, sha256 `55903dd3fecb1bf8…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : NI W% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_
- [doi:10.1007/bf02644589](https://doi.org/10.1007/bf02644589) J. M. Walsh, M. J. Donachie, On a new intermetallic phase in the nickel-tungsten system, Metall Trans 4, 2854-2855 (1973).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(74)90349-4](https://doi.org/10.1016/0036-9748%2874%2990349-4) K.E Poulsen, S Rubæk, E.W Langer, A new intermetallic phase in the W-Ni system, Scripta Metallurgica 8, 1297-1300 (1974).  
_cited as the source of values for this phase_

## NI4X_D1A (Ni–W)

- Id: `phase:ni-w:d1a-ni4x`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaabtpb and oqmd-17851, space group 87
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:NI4X); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.8000, W 0.2000
- Stability: stable in 3 of 3 calculated diagram(s): 304.84–1290 K, x(W) 0.2–0.2
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:d1a-ni4x)

Names (8): _corpus: _corpus:phase:ni-w:d1a-ni4x, corpus:phase:ni-w:ni4x-d1a  
_mp: _mp:mp-aaaabtpb  
_oqmd: _oqmd:oqmd-17851  
_paper: _paper:10.1007/bf02817278:Ni4W  
_tdb: _tdb:NiW-08Pop.tdb:NI4X_D1A, tdb:NiW-17Iso.tdb:NI4X_D1A, tdb:NiW-86Fer-LB.tdb:NI4X_D1A  


### TDB models of NI4X_D1A (3): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): NI4X_D1A, type code %, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
43: PHASE NI4X_D1A % 2 4 1 !
44: CONST NI4X_D1A : NI : W : !
~~~~

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): NI4X_D1A, type code %, sha256 `feb57ad6eaab269b…`

~~~~text
58: PHASE NI4X_D1A % 2 4 1 !
59: CONST NI4X_D1A : NI : W : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): NI4X_D1A, type code %, sha256 `55903dd3fecb1bf8…`

~~~~text
50: PHASE NI4X_D1A % 2 4 1 !
51: CONST NI4X_D1A : NI : W : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_
- [doi:10.1016/0036-9748(74)90349-4](https://doi.org/10.1016/0036-9748%2874%2990349-4) K.E Poulsen, S Rubæk, E.W Langer, A new intermetallic phase in the W-Ni system, Scripta Metallurgica 8, 1297-1300 (1974).  
_cited as the source of values for this phase_

## FCC_A1 (Ni–W)

- Id: `phase:ni-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1790.73 K, x(W) 0–0.17637
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:fcc-a1)

Names (5): _corpus: _corpus:phase:ni-w:fcc-a1  
_paper: _paper:10.1007/bf02817278:fcc  
_tdb: _tdb:NiW-08Pop.tdb:FCC_A1, tdb:NiW-17Iso.tdb:FCC_A1, tdb:NiW-86Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): FCC_A1, type code %A, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : NI% W : VA : !
~~~~

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): FCC_A1, type code %A, sha256 `feb57ad6eaab269b…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : NI% W : VA : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): FCC_A1, type code %A, sha256 `55903dd3fecb1bf8…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : NI% W : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_
- [doi:10.1007/bf02644589](https://doi.org/10.1007/bf02644589) J. M. Walsh, M. J. Donachie, On a new intermetallic phase in the nickel-tungsten system, Metall Trans 4, 2854-2855 (1973).  
_cited as the source of values for this phase_
- [doi:10.1016/0036-9748(74)90349-4](https://doi.org/10.1016/0036-9748%2874%2990349-4) K.E Poulsen, S Rubæk, E.W Langer, A new intermetallic phase in the W-Ni system, Scripta Metallurgica 8, 1297-1300 (1974).  
_cited as the source of values for this phase_

## HCP_A3 (Ni–W)

- Id: `phase:ni-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:hcp-a3)

Names (4): _corpus: _corpus:phase:ni-w:hcp-a3  
_tdb: _tdb:NiW-08Pop.tdb:HCP_A3, tdb:NiW-17Iso.tdb:HCP_A3, tdb:NiW-86Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): HCP_A3, type code %A, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : NI W : VA : !
~~~~

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): HCP_A3, type code %A, sha256 `feb57ad6eaab269b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : NI W : VA : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): HCP_A3, type code %A, sha256 `55903dd3fecb1bf8…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : NI W : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_

## LIQUID (Ni–W)

- Id: `phase:ni-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1728.25–4000 K, x(W) 0–1
- Literature: 1 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:liquid)

Names (5): _corpus: _corpus:phase:ni-w:liquid  
_paper: _paper:10.1007/bf02817278:liquid  
_tdb: _tdb:NiW-08Pop.tdb:LIQUID, tdb:NiW-17Iso.tdb:LIQUID, tdb:NiW-86Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): LIQUID, type code %, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : NI W : !
~~~~

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): LIQUID, type code %, sha256 `feb57ad6eaab269b…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : NI W : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): LIQUID, type code %, sha256 `55903dd3fecb1bf8…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : NI W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_

## NI3W_D0A (Ni–W)

- Id: `phase:ni-w:ni3w-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Ni 0.7500, W 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–848.8 K, x(W) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:ni3w-d0a)

Names (2): _corpus: _corpus:phase:ni-w:ni3w-d0a  
_tdb: _tdb:NiW-17Iso.tdb:NI3W_D0A  


### TDB models of NI3W_D0A (1): PHASE and CONSTITUENT statements as written

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): NI3W_D0A, type code %, sha256 `feb57ad6eaab269b…`

~~~~text
63: PHASE NI3W_D0A % 2 3 1 !
64: CONST NI3W_D0A : NI : W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_

## NI8W (Ni–W)

- Id: `phase:ni-w:ni8w`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (tdb_comment): Pt8Ti · tI18 · I4/mmm — NiW-17Iso.tdb: 'Prototype Pt8Ti (tI18, I4/mmm)'
- Stability: stable in 1 of 1 calculated diagram(s): 300–802.5 K, x(W) 0.11111–0.11111
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:ni8w)

Names (2): _corpus: _corpus:phase:ni-w:ni8w  
_tdb: _tdb:NiW-17Iso.tdb:NI8W  


### TDB models of NI8W (1): PHASE and CONSTITUENT statements as written

[NiW-17Iso.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-17Iso.tdb): NI8W, type code %A, sha256 `feb57ad6eaab269b…`

~~~~text
53: PHASE NI8W %A 2 1 0.125 !
54: CONST NI8W : NI : VA W% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111557](https://doi.org/10.3139/146.111557) I. Isomaki, M. Hamalainien, M.H. Braga, M. Gasik, Int. J. Mater. Res., 108, 1025-35(2017).  
_assessment that models this phase_

## NIW (Ni–W)

- Id: `phase:ni-w:niw`; status `assigned`
- Structure: MoNi · oP56 · P2_12_12_1 (19); type `st:moni-op56`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ni 0.5000, W 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1340.8 K, x(W) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:niw)

Names (4): _corpus: _corpus:phase:ni-w:niw  
_paper: _paper:10.1007/bf02817278:NiW  
_tdb: _tdb:NiW-08Pop.tdb:NIW, tdb:NiW-86Fer-LB.tdb:NIW  


### TDB models of NIW (2): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): NIW, type code %, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
48: PHASE NIW % 2 1 1 !
49: CONST NIW : NI : W : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): NIW, type code %, sha256 `55903dd3fecb1bf8…`

~~~~text
55: PHASE NIW % 2 1 1 !
56: CONST NIW : NI : W : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.1016/0036-9748(74)90349-4](https://doi.org/10.1016/0036-9748%2874%2990349-4) K.E Poulsen, S Rubæk, E.W Langer, A new intermetallic phase in the W-Ni system, Scripta Metallurgica 8, 1297-1300 (1974).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02644589](https://doi.org/10.1007/bf02644589) J. M. Walsh, M. J. Donachie, On a new intermetallic phase in the nickel-tungsten system, Metall Trans 4, 2854-2855 (1973).  
_cited as the source of values for this phase_

## NIW2 (Ni–W)

- Id: `phase:ni-w:niw2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (NiW2) · tI96 — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (NiW2) · tI96 — Hallstedt 2025 mmc2 row for NIW2: NiW2
- Stoichiometry: Ni 0.3333, W 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1340 K, x(W) 0.66667–0.66667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-w:niw2)

Names (4): _corpus: _corpus:phase:ni-w:niw2  
_paper: _paper:10.1007/bf02817278:NiW2  
_tdb: _tdb:NiW-08Pop.tdb:NIW2, tdb:NiW-86Fer-LB.tdb:NIW2  


### TDB models of NIW2 (2): PHASE and CONSTITUENT statements as written

[NiW-08Pop.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-08Pop.tdb): NIW2, type code %, sha256 `e3c06f0d3fa4f8bf…`

~~~~text
53: PHASE NIW2 % 2 1 2 !
54: CONST NIW2 : NI : W : !
~~~~

[NiW-86Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiW-86Fer-LB.tdb): NIW2, type code %, sha256 `55903dd3fecb1bf8…`

~~~~text
60: PHASE NIW2 % 2 1 2 !
61: CONST NIW2 : NI : W : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02817278](https://doi.org/10.1007/BF02817278) A. Fernandez Guillermet, L. Ostlund, Metall. Trans. A, 17A, 1809-23(1986).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2008.04.003](https://doi.org/10.1016/j.intermet.2008.04.003) J. Popovič, P. Brož, J. Buršík, Microstructure and phase equilibria in the Ni–Al–W system, Intermetallics 16, 884-888 (2008).  
_assessment that models this phase_
- [doi:10.1016/0036-9748(74)90349-4](https://doi.org/10.1016/0036-9748%2874%2990349-4) K.E Poulsen, S Rubæk, E.W Langer, A new intermetallic phase in the W-Ni system, Scripta Metallurgica 8, 1297-1300 (1974).  
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
