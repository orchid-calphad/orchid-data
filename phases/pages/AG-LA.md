# Ag–La phases

> Ag–La system: 9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-LA.html · Markdown: https://data.orchid-project.org/phases/pages/AG-LA.md

9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-LA) · [full JSON](https://data.orchid-project.org/phases/systems/AG-LA.json) · [Ag–La system page](https://data.orchid-project.org/systems/AG-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–La system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AG2LA](#phase-ag-la-ag2la); _phase:ag-la:ag2la_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1127.3 K, x(La) 0.33333–0.33333 | 4 | 1 |
| [AG51LA14](#phase-ag-la-ag51la14); _phase:ag-la:ag51la14_ | Ag51Gd14 · hP68 · P6/m (175) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1272.5 K, x(La) 0.21538–0.21538 | 8 | 1 |
| [AG5LA_C14](#phase-ag-la-ag5la-c14); _phase:ag-la:ag5la-c14_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1099.45 K, x(La) 0.16667–0.16667 | 6 | 1 |
| [AGLA_B2](#phase-ag-la-agla-b2); _phase:ag-la:agla-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1147.56 K, x(La) 0.5–0.5 | 6 | 1 |
| [BCC_A2](#phase-ag-la-bcc-a2); _phase:ag-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1067.37–2500 K, x(La) 0.63094–1 | 0 | 1 |
| [DHCP](#phase-ag-la-dhcp-a3); _phase:ag-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1133.35 K, x(La) 1–1 | 0 | 1 |
| [FCC_A1](#phase-ag-la-fcc-a1); _phase:ag-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1243.57 K, x(La) 0–1 | 5 | 1 |
| [HCP_A3](#phase-ag-la-hcp-a3); _phase:ag-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-la-liquid); _phase:ag-la:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 802.58–2500 K, x(La) 0–1 | 17 | 1 |

## AG2LA (Ag–La)

- Id: `phase:ag-la:ag2la`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.6667, La 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1127.3 K, x(La) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:ag2la)

Names (3): _corpus: _corpus:phase:ag-la:ag2la  
_paper: _paper:10.1016/s0925-8388(99)00686-6:Ag2La  
_tdb: _tdb:AgLa-00Li.tdb:AG2LA  


### TDB models of AG2LA (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): AG2LA, type code %, sha256 `3c614db77cf33b53…`

~~~~text
58: PHASE AG2LA % 2 2 1 !
59: CONST AG2LA : AG : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1974-651210](https://doi.org/10.1515/ijmr-1974-651210) Stefano Delfino, Riccardo Ferro, Renzo Capelli, Aldo Borsese, Phase Equilibria in the Silver-Lanthanum System, International Journal of Materials Research 65, 781-783 (1974).  
_cited as the source of values for this phase_

## AG51LA14 (Ag–La)

- Id: `phase:ag-la:ag51la14`; status `assigned`
- Structure: Ag51Gd14 · hP68 · P6/m (175); type `st:ag51gd14-hp68`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ag 0.7846, La 0.2154
- Stability: stable in 1 of 1 calculated diagram(s): 300–1272.5 K, x(La) 0.21538–0.21538
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:ag51la14)

Names (3): _corpus: _corpus:phase:ag-la:ag51la14  
_paper: _paper:10.1016/s0925-8388(99)00686-6:Ag51La14  
_tdb: _tdb:AgLa-00Li.tdb:AG51LA14  


### TDB models of AG51LA14 (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): AG51LA14, type code %, sha256 `3c614db77cf33b53…`

~~~~text
53: PHASE AG51LA14 % 2 51 14 !
54: CONST AG51LA14 : AG : LA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1974-651210](https://doi.org/10.1515/ijmr-1974-651210) Stefano Delfino, Riccardo Ferro, Renzo Capelli, Aldo Borsese, Phase Equilibria in the Silver-Lanthanum System, International Journal of Materials Research 65, 781-783 (1974).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1982-730308](https://doi.org/10.1515/ijmr-1982-730308) Theodor Heumann, Heinz Dirkes, Phase Eauilibria in the System Ag-25 at.% La, International Journal of Materials Research 73, 172-173 (1982).  
_cited as the source of values for this phase_

## AG5LA_C14 (Ag–La)

- Id: `phase:ag-la:ag5la-c14`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C14; stoichiometry_contradicts_C14:AgLa-00Li.tdb
- Candidate (literature_printed): MgZn2 · hP12 — printed with a label mapped to this phase
- Candidate (name_token): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Strukturbericht/word 'C14' in the TDB name
- Candidate (sgte_mmc2): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for AG5LA_C14: Ag5La
- Candidate (tdb_comment): MgZn2 · hP12 · P6_3/mmc — AgLa-00Li.tdb: 'Prototype MgZn2 (hP12, P6_3/mmc)'
- Stoichiometry: Ag 0.8333, La 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1099.45 K, x(La) 0.16667–0.16667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:ag5la-c14)

Names (3): _corpus: _corpus:phase:ag-la:ag5la-c14  
_paper: _paper:10.1016/s0925-8388(99)00686-6:Ag5La  
_tdb: _tdb:AgLa-00Li.tdb:AG5LA_C14  


### TDB models of AG5LA_C14 (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): AG5LA_C14, type code %, sha256 `3c614db77cf33b53…`

~~~~text
48: PHASE AG5LA_C14 % 2 5 1 !
49: CONST AG5LA_C14 : AG : LA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1974-651210](https://doi.org/10.1515/ijmr-1974-651210) Stefano Delfino, Riccardo Ferro, Renzo Capelli, Aldo Borsese, Phase Equilibria in the Silver-Lanthanum System, International Journal of Materials Research 65, 781-783 (1974).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1982-730308](https://doi.org/10.1515/ijmr-1982-730308) Theodor Heumann, Heinz Dirkes, Phase Eauilibria in the System Ag-25 at.% La, International Journal of Materials Research 73, 172-173 (1982).  
_cited as the source of values for this phase_

## AGLA_B2 (Ag–La)

- Id: `phase:ag-la:agla-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 0.5000, La 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1147.56 K, x(La) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:agla-b2)

Names (3): _corpus: _corpus:phase:ag-la:agla-b2  
_paper: _paper:10.1016/s0925-8388(99)00686-6:AgLa  
_tdb: _tdb:AgLa-00Li.tdb:AGLA_B2  


### TDB models of AGLA_B2 (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): AGLA_B2, type code %A, sha256 `3c614db77cf33b53…`

~~~~text
63: PHASE AGLA_B2 %A 2 1 1 !
64: CONST AGLA_B2 : AG : LA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1974-651210](https://doi.org/10.1515/ijmr-1974-651210) Stefano Delfino, Riccardo Ferro, Renzo Capelli, Aldo Borsese, Phase Equilibria in the Silver-Lanthanum System, International Journal of Materials Research 65, 781-783 (1974).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–La)

- Id: `phase:ag-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1067.37–2500 K, x(La) 0.63094–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-la:bcc-a2  
_tdb: _tdb:AgLa-00Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): BCC_A2, type code %B, sha256 `3c614db77cf33b53…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG LA% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase_

## DHCP (Ag–La)

- Id: `phase:ag-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1133.35 K, x(La) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:dhcp-a3)

Names (2): _corpus: _corpus:phase:ag-la:dhcp-a3  
_tdb: _tdb:AgLa-00Li.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): DHCP, type code %, sha256 `3c614db77cf33b53…`

~~~~text
43: PHASE DHCP % 1 1 !
44: CONST DHCP : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase_

## FCC_A1 (Ag–La)

- Id: `phase:ag-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1243.57 K, x(La) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-la:fcc-a1  
_paper: _paper:10.1016/s0925-8388(99)00686-6:Ag, paper:10.1016/s0925-8388(99)00686-6:β-La  
_tdb: _tdb:AgLa-00Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): FCC_A1, type code %A, sha256 `3c614db77cf33b53…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% LA% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1974-651210](https://doi.org/10.1515/ijmr-1974-651210) Stefano Delfino, Riccardo Ferro, Renzo Capelli, Aldo Borsese, Phase Equilibria in the Silver-Lanthanum System, International Journal of Materials Research 65, 781-783 (1974).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1982-730308](https://doi.org/10.1515/ijmr-1982-730308) Theodor Heumann, Heinz Dirkes, Phase Eauilibria in the System Ag-25 at.% La, International Journal of Materials Research 73, 172-173 (1982).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–La)

- Id: `phase:ag-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ag 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-la:hcp-a3  
_tdb: _tdb:AgLa-00Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): HCP_A3, type code %A, sha256 `3c614db77cf33b53…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase_

## LIQUID (Ag–La)

- Id: `phase:ag-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 802.58–2500 K, x(La) 0–1
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-la:liquid)

Names (3): _corpus: _corpus:phase:ag-la:liquid  
_paper: _paper:10.1016/s0925-8388(99)00686-6:L  
_tdb: _tdb:AgLa-00Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgLa-00Li.tdb](https://orchid-project.org/data/databases/sgte-binary/AgLa-00Li.tdb): LIQUID, type code %, sha256 `3c614db77cf33b53…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG LA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0925-8388(99)00686-6](https://doi.org/10.1016/S0925-8388%2899%2900686-6) Z. Li, X. Su, F. Yin, C. Chen, J. Alloys Compd., 299, 195-98(2000).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1515/ijmr-1974-651210](https://doi.org/10.1515/ijmr-1974-651210) Stefano Delfino, Riccardo Ferro, Renzo Capelli, Aldo Borsese, Phase Equilibria in the Silver-Lanthanum System, International Journal of Materials Research 65, 781-783 (1974).  
_cited as the source of values for this phase_
- [doi:10.1515/ijmr-1982-730308](https://doi.org/10.1515/ijmr-1982-730308) Theodor Heumann, Heinz Dirkes, Phase Eauilibria in the System Ag-25 at.% La, International Journal of Materials Research 73, 172-173 (1982).  
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
