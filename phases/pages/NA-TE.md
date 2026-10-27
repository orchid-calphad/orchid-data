# Na–Te phases

> Na–Te system: 8 phases (tier A 5, tier C 2, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NA-TE.html · Markdown: https://data.orchid-project.org/phases/pages/NA-TE.md

8 phases (tier A 5, tier C 2, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NA-TE) · [full JSON](https://data.orchid-project.org/phases/systems/NA-TE.json) · [Na–Te system page](https://data.orchid-project.org/systems/NA-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/NA-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Na–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-na-te-a8-hexagonal); _phase:na-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 2 | 1 |
| [BCC_A2](#phase-na-te-bcc-a2); _phase:na-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(Te) 0–0 | 0 | 1 |
| [FCC_A1](#phase-na-te-fcc-a1); _phase:na-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-na-te-hcp-a3); _phase:na-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-na-te-liquid); _phase:na-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 370.87–2500 K, x(Te) 0–1 | 12 | 1 |
| [NA2TE_C1](#phase-na-te-na2te-c1); _phase:na-te:na2te-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1236.23 K, x(Te) 0.33333–0.33333 | 6 | 1 |
| [NATE](#phase-na-te-nate); _phase:na-te:nate_ | NaTe · oP48 · Pbcn (60) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–628.27 K, x(Te) 0.5–0.5 | 10 | 1 |
| [NATE3](#phase-na-te-nate3); _phase:na-te:nate3_ | NaTe3 · hP48 · P-3c1 (165) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–736.09 K, x(Te) 0.75–0.75 | 9 | 1 |

## HEXAGONAL_A8 (Na–Te)

- Id: `phase:na-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:na-te:a8-hexagonal, corpus:phase:na-te:hexagonal-a8  
_paper: _paper:10.1016/j.jallcom.2013.11.094:Te  
_tdb: _tdb:NaTe-14Che.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): HEXAGONAL_A8, type code %, sha256 `345a0a074cafc669…`

~~~~text
51: PHASE HEXAGONAL_A8 % 1 1 !
52: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j150301a004](https://doi.org/10.1021/j150301a004) C. A. Kraus, S. W. Glass, Liquid Mixtures of Tellurium and Sodium Telluride. I. Specific Resistance as a Function of Compostion and Temperature, J. Phys. Chem. 33, 984-994 (1929).  
_cited as the source of values for this phase_

## BCC_A2 (Na–Te)

- Id: `phase:na-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:bcc-a2)

Names (2): _corpus: _corpus:phase:na-te:bcc-a2  
_tdb: _tdb:NaTe-14Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): BCC_A2, type code %B, sha256 `345a0a074cafc669…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## FCC_A1 (Na–Te)

- Id: `phase:na-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:fcc-a1)

Names (2): _corpus: _corpus:phase:na-te:fcc-a1  
_tdb: _tdb:NaTe-14Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): FCC_A1, type code %A, sha256 `345a0a074cafc669…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## HCP_A3 (Na–Te)

- Id: `phase:na-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Na 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:hcp-a3)

Names (2): _corpus: _corpus:phase:na-te:hcp-a3  
_tdb: _tdb:NaTe-14Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): HCP_A3, type code %A, sha256 `345a0a074cafc669…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : NA : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## LIQUID (Na–Te)

- Id: `phase:na-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 370.87–2500 K, x(Te) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:liquid)

Names (3): _corpus: _corpus:phase:na-te:liquid  
_paper: _paper:10.1016/j.jallcom.2013.11.094:liq  
_tdb: _tdb:NaTe-14Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): LIQUID, type code %, sha256 `345a0a074cafc669…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : NA NA2TE NATE3 TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j150301a004](https://doi.org/10.1021/j150301a004) C. A. Kraus, S. W. Glass, Liquid Mixtures of Tellurium and Sodium Telluride. I. Specific Resistance as a Function of Compostion and Temperature, J. Phys. Chem. 33, 984-994 (1929).  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19890930105](https://doi.org/10.1002/bbpc.19890930105) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Thermodynamic properties of molten Na‐Te solutions, Ber Bunsenges Phys Chem 93, 18-24 (1989).  
_cited as the source of values for this phase_

## NA2TE_C1 (Na–Te)

- Id: `phase:na-te:na2te-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaedc and oqmd-11318, space group 225
- Stoichiometry: Na 0.6667, Te 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1236.23 K, x(Te) 0.33333–0.33333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:na2te-c1)

Names (5): _corpus: _corpus:phase:na-te:na2te-c1  
_mp: _mp:mp-aaaaaedc  
_oqmd: _oqmd:oqmd-11318  
_paper: _paper:10.1016/j.jallcom.2013.11.094:Na2Te  
_tdb: _tdb:NaTe-14Che.tdb:NA2TE_C1  


### TDB models of NA2TE_C1 (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): NA2TE_C1, type code %, sha256 `345a0a074cafc669…`

~~~~text
56: PHASE NA2TE_C1 % 2 2 1 !
57: CONST NA2TE_C1 : NA : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.19890930105](https://doi.org/10.1002/bbpc.19890930105) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Thermodynamic properties of molten Na‐Te solutions, Ber Bunsenges Phys Chem 93, 18-24 (1989).  
_cited as the source of values for this phase_
- [doi:10.1021/j150301a004](https://doi.org/10.1021/j150301a004) C. A. Kraus, S. W. Glass, Liquid Mixtures of Tellurium and Sodium Telluride. I. Specific Resistance as a Function of Compostion and Temperature, J. Phys. Chem. 33, 984-994 (1929).  
_cited as the source of values for this phase_

## NATE (Na–Te)

- Id: `phase:na-te:nate`; status `assigned`
- Structure: NaTe · oP48 · Pbcn (60); type `st:nate-op48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Na 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–628.27 K, x(Te) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:nate)

Names (3): _corpus: _corpus:phase:na-te:nate  
_paper: _paper:10.1016/j.jallcom.2013.11.094:NaTe  
_tdb: _tdb:NaTe-14Che.tdb:NATE  


### TDB models of NATE (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): NATE, type code %, sha256 `345a0a074cafc669…`

~~~~text
61: PHASE NATE % 2 1 1 !
62: CONST NATE : NA : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/bbpc.19890930105](https://doi.org/10.1002/bbpc.19890930105) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Thermodynamic properties of molten Na‐Te solutions, Ber Bunsenges Phys Chem 93, 18-24 (1989).  
_cited as the source of values for this phase_
- [doi:10.1021/j150301a004](https://doi.org/10.1021/j150301a004) C. A. Kraus, S. W. Glass, Liquid Mixtures of Tellurium and Sodium Telluride. I. Specific Resistance as a Function of Compostion and Temperature, J. Phys. Chem. 33, 984-994 (1929).  
_cited as the source of values for this phase_

## NATE3 (Na–Te)

- Id: `phase:na-te:nate3`; status `assigned`
- Structure: NaTe3 · hP48 · P-3c1 (165); type `st:nate3-hp48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_165_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Na 0.2500, Te 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–736.09 K, x(Te) 0.75–0.75
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:na-te:nate3)

Names (3): _corpus: _corpus:phase:na-te:nate3  
_paper: _paper:10.1016/j.jallcom.2013.11.094:NaTe3  
_tdb: _tdb:NaTe-14Che.tdb:NATE3  


### TDB models of NATE3 (1): PHASE and CONSTITUENT statements as written

[NaTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb): NATE3, type code %, sha256 `345a0a074cafc669…`

~~~~text
66: PHASE NATE3 % 2 1 3 !
67: CONST NATE3 : NA : TE : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/j150301a004](https://doi.org/10.1021/j150301a004) C. A. Kraus, S. W. Glass, Liquid Mixtures of Tellurium and Sodium Telluride. I. Specific Resistance as a Function of Compostion and Temperature, J. Phys. Chem. 33, 984-994 (1929).  
_cited as the source of values for this phase_
- [doi:10.1002/bbpc.19890930105](https://doi.org/10.1002/bbpc.19890930105) Anthony Petric, Arthur D. Pelton, Marie‐Louise Saboungi, Thermodynamic properties of molten Na‐Te solutions, Ber Bunsenges Phys Chem 93, 18-24 (1989).  
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
