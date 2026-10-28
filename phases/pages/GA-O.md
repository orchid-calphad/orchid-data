# Ga–O phases

> Ga–O system: 11 phases (tier A 5, tier C 2, liquid 1, gas 2, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-O.html · Markdown: https://data.orchid-project.org/phases/pages/GA-O.md

11 phases (tier A 5, tier C 2, liquid 1, gas 2, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-O) · [full JSON](https://data.orchid-project.org/phases/systems/GA-O.json) · [Ga–O system page](https://data.orchid-project.org/systems/GA-O.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-O.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–O system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-o-a11-orthorhombic); _phase:ga-o:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(O) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ga-o-bcc-a2); _phase:ga-o:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CORUNDUM_D51](#phase-ga-o-d51-corundum); _phase:ga-o:d51-corundum_ | alpha-Al2O3 · D5_1 · hR10 · R-3c (167) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ga-o-fcc-a1); _phase:ga-o:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GA2O3_BETA](#phase-ga-o-ga2o3-beta); _phase:ga-o:ga2o3-beta_ | beta-Ga2O3 · mC20 · C2/m (12) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–867.91 K, x(O) 0.6–0.6 | 4 | 1 |
| [GA2O3_D53](#phase-ga-o-ga2o3-d53); _phase:ga-o:ga2o3-d53_ | Mn2O3 · D5_3 · cI80 · Ia-3 (206) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 1 | 1 |
| [GA2O3_H11](#phase-ga-o-ga2o3-h11); _phase:ga-o:ga2o3-h11_ |  | needs_review | not stable in 1 calculated diagram(s) | 1 | 1 |
| [GAS](#phase-ga-o-gas); _phase:ga-o:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1603.22–2500 K, x(O) 0.00188–0.33796 | 1 | 1 |
| [HCP_A3](#phase-ga-o-hcp-a3); _phase:ga-o:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ION](#phase-ga-o-ion); _phase:ga-o:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(O) 0–0.5996 | 0 | 1 |
| [O2GAS](#phase-ga-o-o2gas); _phase:ga-o:o2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–445 K, x(O) 1–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (Ga–O)

- Id: `phase:ga-o:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(O) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:ga-o:a11-orthorhombic  
_tdb: _tdb:GaO-04Zin.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): ORTHORHOMBIC_A11, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
56: PHASE ORTHORHOMBIC_A11 % 1 1 !
57: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

## BCC_A2 (Ga–O)

- Id: `phase:ga-o:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-o:bcc-a2  
_tdb: _tdb:GaO-04Zin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): BCC_A2, type code %B, sha256 `3fb8f43e1c88636a…`

~~~~text
46: PHASE BCC_A2 %B 2 1 3 !
47: CONST BCC_A2 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

## CORUNDUM_D51 (Ga–O)

- Id: `phase:ga-o:d51-corundum`; status `assigned`
- Structure: alpha-Al2O3 · D5_1 · hR10 · R-3c (167); type `st:d5-1-alpha-al2o3-hr10`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:CORUNDUM); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:d51-corundum)

Names (2): _corpus: _corpus:phase:ga-o:d51-corundum  
_tdb: _tdb:GaO-04Zin.tdb:CORUNDUM_D51  


### TDB models of CORUNDUM_D51 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): CORUNDUM_D51, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
61: PHASE CORUNDUM_D51:I % 2 2 3 !
62: CONST CORUNDUM_D51:I : GA+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

## FCC_A1 (Ga–O)

- Id: `phase:ga-o:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-o:fcc-a1  
_tdb: _tdb:GaO-04Zin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): FCC_A1, type code %A, sha256 `3fb8f43e1c88636a…`

~~~~text
41: PHASE FCC_A1 %A 2 1 1 !
42: CONST FCC_A1 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

## GA2O3_BETA (Ga–O)

- Id: `phase:ga-o:ga2o3-beta`; status `assigned`
- Structure: beta-Ga2O3 · mC20 · C2/m (12); type `st:beta-ga2o3-mc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–867.91 K, x(O) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:ga2o3-beta)

Names (3): _corpus: _corpus:phase:ga-o:ga2o3-beta  
_paper: _paper:10.1111/j.1551-2916.2004.00683.x:β-Ga2O3  
_tdb: _tdb:GaO-04Zin.tdb:GA2O3_BETA  


### TDB models of GA2O3_BETA (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): GA2O3_BETA, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
66: PHASE GA2O3_BETA:I % 2 2 3 !
67: CONST GA2O3_BETA:I : GA+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase; reports values for this phase_

## GA2O3_D53 (Ga–O)

- Id: `phase:ga-o:ga2o3-d53`; status `assigned`
- Structure: Mn2O3 · D5_3 · cI80 · Ia-3 (206); type `st:d5-3-mn2o3-ci80`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:ga2o3-d53)

Names (3): _corpus: _corpus:phase:ga-o:ga2o3-d53  
_paper: _paper:10.1111/j.1551-2916.2004.00683.x:δ-Ga2O3†  
_tdb: _tdb:GaO-04Zin.tdb:GA2O3_D53  


### TDB models of GA2O3_D53 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): GA2O3_D53, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
76: PHASE GA2O3_D53:I % 2 2 3 !
77: CONST GA2O3_D53:I : GA+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase; reports values for this phase_

## GA2O3_H11 (Ga–O)

- Id: `phase:ga-o:ga2o3-h11`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:site_ratios_contradict_H1_1; site_ratios_contradict_H1_1:GaO-04Zin.tdb
- Candidate (name_token): Al2MgO4 · H1_1 · cF56 · Fd-3m (227) — Strukturbericht/word 'H11' in the TDB name
- Candidate (sgte_mmc2): Al2MgO4 · H1_1 · cF56 · Fd-3m (227) — Hallstedt 2025 mmc2 row for GA2O3_H11: gamma-Ga2O3 (metastable)
- Candidate (tdb_comment): Al2MgO4 · cF56 · Fd-3m — GaO-04Zin.tdb: 'Prototype Al2MgO4 (cF56, Fd-3m), gamma-Ga2O3'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:ga2o3-h11)

Names (3): _corpus: _corpus:phase:ga-o:ga2o3-h11  
_paper: _paper:10.1111/j.1551-2916.2004.00683.x:γ-Ga2O3†  
_tdb: _tdb:GaO-04Zin.tdb:GA2O3_H11  


### TDB models of GA2O3_H11 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): GA2O3_H11, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
71: PHASE GA2O3_H11:I % 2 2 3 !
72: CONST GA2O3_H11:I : GA+3 : O-2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase; reports values for this phase_

## GAS (Ga–O)

- Id: `phase:ga-o:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1603.22–2500 K, x(O) 0.00188–0.33796
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:gas)

Names (3): _corpus: _corpus:phase:ga-o:gas  
_paper: _paper:10.1111/j.1551-2916.2004.00683.x:gas  
_tdb: _tdb:GaO-04Zin.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): GAS, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
79: PHASE GAS:G % 1 1 !
80: CONST GAS:G : GA GA2 GAO GA2O O O2% O3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ga–O)

- Id: `phase:ga-o:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:hcp-a3)

Names (2): _corpus: _corpus:phase:ga-o:hcp-a3  
_tdb: _tdb:GaO-04Zin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): HCP_A3, type code %A, sha256 `3fb8f43e1c88636a…`

~~~~text
51: PHASE HCP_A3 %A 2 1 0.5 !
52: CONST HCP_A3 : GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

## ION (Ga–O)

- Id: `phase:ga-o:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(O) 0–0.5996
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:ion)

Names (2): _corpus: _corpus:phase:ga-o:ion  
_tdb: _tdb:GaO-04Zin.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): ION, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
36: PHASE ION:Y % 2 1 1 !
37: CONST ION:Y : GA+3 : O-2 VA O : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

## O2GAS (Ga–O)

- Id: `phase:ga-o:o2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–445 K, x(O) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-o:o2gas)

Names (2): _corpus: _corpus:phase:ga-o:o2gas  
_tdb: _tdb:GaO-04Zin.tdb:O2GAS  


### TDB models of O2GAS (1): PHASE and CONSTITUENT statements as written

[GaO-04Zin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaO-04Zin.tdb): O2GAS, type code %, sha256 `3fb8f43e1c88636a…`

~~~~text
82: PHASE O2GAS % 1 1 !
83: CONST O2GAS : O2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/j.1551-2916.2004.00683.x](https://doi.org/10.1111/j.1551-2916.2004.00683.x) Matvei Zinkevich, Fritz Aldinger, Thermodynamic Assessment of the Gallium‐Oxygen System, Journal of the American Ceramic Society 87, 683-691 (2004).  
_assessment that models this phase_

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
