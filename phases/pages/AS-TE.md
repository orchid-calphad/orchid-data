# As–Te phases

> As–Te system: 8 phases (tier A 5, tier C 1, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-TE.html · Markdown: https://data.orchid-project.org/phases/pages/AS-TE.md

8 phases (tier A 5, tier C 1, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-TE) · [full JSON](https://data.orchid-project.org/phases/systems/AS-TE.json) · [As–Te system page](https://data.orchid-project.org/systems/AS-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AS-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-as-te-a7-rhombohedral); _phase:as-te:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–888.37 K, x(Te) 0–0 | 0 | 1 |
| [HEXAGONAL_A8](#phase-as-te-a8-hexagonal); _phase:as-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 1 |
| [AS2TE3](#phase-as-te-as2te3); _phase:as-te:as2te3_ | As2Te3 · mC20 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–652.75 K, x(Te) 0.6–0.6 | 0 | 1 |
| [BCC_A2](#phase-as-te-bcc-a2); _phase:as-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-as-te-fcc-a1); _phase:as-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-as-te-gas); _phase:as-te:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 888.37–2500 K, x(Te) 0–1 | 0 | 1 |
| [HCP_A3](#phase-as-te-hcp-a3); _phase:as-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-as-te-liquid); _phase:as-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 632.66–1310 K, x(Te) 0.37009–1 | 0 | 1 |

## RHOMBOHEDRAL_A7 (As–Te)

- Id: `phase:as-te:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–888.37 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:as-te:a7-rhombohedral  
_tdb: _tdb:AsTe-20Yua.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `95641bd1ffe25475…`

~~~~text
55: PHASE RHOMBOHEDRAL_A7 % 1 1 !
56: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## HEXAGONAL_A8 (As–Te)

- Id: `phase:as-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:a8-hexagonal)

Names (2): _corpus: _corpus:phase:as-te:a8-hexagonal  
_tdb: _tdb:AsTe-20Yua.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): HEXAGONAL_A8, type code %, sha256 `95641bd1ffe25475…`

~~~~text
62: PHASE HEXAGONAL_A8 % 1 1 !
63: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## AS2TE3 (As–Te)

- Id: `phase:as-te:as2te3`; status `assigned`
- Structure: As2Te3 · mC20 · C2/m (12); type `st:as2te3-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_12_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: As 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–652.75 K, x(Te) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:as2te3)

Names (2): _corpus: _corpus:phase:as-te:as2te3  
_tdb: _tdb:AsTe-20Yua.tdb:AS2TE3  


### TDB models of AS2TE3 (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): AS2TE3, type code %, sha256 `95641bd1ffe25475…`

~~~~text
67: PHASE AS2TE3 % 2 2 3 !
68: CONST AS2TE3 : AS : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## BCC_A2 (As–Te)

- Id: `phase:as-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:bcc-a2)

Names (2): _corpus: _corpus:phase:as-te:bcc-a2  
_tdb: _tdb:AsTe-20Yua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): BCC_A2, type code %B, sha256 `95641bd1ffe25475…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : AS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## FCC_A1 (As–Te)

- Id: `phase:as-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:fcc-a1)

Names (2): _corpus: _corpus:phase:as-te:fcc-a1  
_tdb: _tdb:AsTe-20Yua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): FCC_A1, type code %A, sha256 `95641bd1ffe25475…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : AS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## GAS (As–Te)

- Id: `phase:as-te:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 888.37–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:gas)

Names (2): _corpus: _corpus:phase:as-te:gas  
_tdb: _tdb:AsTe-20Yua.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): GAS, type code %, sha256 `95641bd1ffe25475…`

~~~~text
70: PHASE GAS:G % 1 1 !
71: CONST GAS:G : AS AS2 AS4 ASTE TE TE2 TE3 TE4 TE5 TE6 TE7 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## HCP_A3 (As–Te)

- Id: `phase:as-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:hcp-a3)

Names (2): _corpus: _corpus:phase:as-te:hcp-a3  
_tdb: _tdb:AsTe-20Yua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): HCP_A3, type code %A, sha256 `95641bd1ffe25475…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : AS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
_assessment that models this phase_

## LIQUID (As–Te)

- Id: `phase:as-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 632.66–1310 K, x(Te) 0.37009–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-te:liquid)

Names (2): _corpus: _corpus:phase:as-te:liquid  
_tdb: _tdb:AsTe-20Yua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AsTe-20Yua.tdb](https://orchid-project.org/data/databases/sgte-binary/AsTe-20Yua.tdb): LIQUID, type code %, sha256 `95641bd1ffe25475…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : AS TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2020.101743](https://doi.org/10.1016/j.calphad.2020.101743) H. Yuan, J. Wang, B. Hu, R. Zhao, Y. Du, S.-Y. Zhang, Calphad, 68, 101743(2020).  
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
