# Bi–Y phases

> Bi–Y system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-Y.html · Markdown: https://data.orchid-project.org/phases/pages/BI-Y.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-Y) · [full JSON](https://data.orchid-project.org/phases/systems/BI-Y.json) · [Bi–Y system page](https://data.orchid-project.org/systems/BI-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Y system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-y-a7-rhombohedral); _phase:bi-y:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Y) 0–0 | 2 | 1 |
| [BCC_A2](#phase-bi-y-bcc-a2); _phase:bi-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300.72–2499.47 K, x(Y) 1–1 | 0 | 1 |
| [BI3Y5](#phase-bi-y-bi3y5); _phase:bi-y:bi3y5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1804.07 K, x(Y) 0.625–0.625 | 5 | 1 |
| [BIY_B1](#phase-bi-y-biy-b1); _phase:bi-y:biy-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2293.25 K, x(Y) 0.5–0.5 | 6 | 1 |
| [FCC_A1](#phase-bi-y-fcc-a1); _phase:bi-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-y-hcp-a3); _phase:bi-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1751.97 K, x(Y) 0.99795–1 | 2 | 1 |
| [LIQUID](#phase-bi-y-liquid); _phase:bi-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 544.55–2500 K, x(Y) 0–1 | 8 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Y)

- Id: `phase:bi-y:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Y) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-y:a7-rhombohedral, corpus:phase:bi-y:rhombohedral-a7  
_paper: _paper:10.1007/s11669-011-9939-1:(Bi)  
_tdb: _tdb:BiY-11Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `ac3d63c817a8399a…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI% Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90159-3](https://doi.org/10.1016/0022-5088%2869%2990159-3) F.A. Schmidt, O.D. McMasters, R.R. Lichtenberg, The yttrium-bismuth alloy system, Journal of the Less Common Metals 18, 215-220 (1969).  
_cited as the source of values for this phase_

## BCC_A2 (Bi–Y)

- Id: `phase:bi-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.72–2499.47 K, x(Y) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-y:bcc-a2  
_tdb: _tdb:BiY-11Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): BCC_A2, type code %B, sha256 `ac3d63c817a8399a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase_

## BI3Y5 (Bi–Y)

- Id: `phase:bi-y:bi3y5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Y 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1804.07 K, x(Y) 0.625–0.625
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:bi3y5)

Names (3): _corpus: _corpus:phase:bi-y:bi3y5  
_paper: _paper:10.1007/s11669-011-9939-1:Bi3Y5  
_tdb: _tdb:BiY-11Wan.tdb:BI3Y5  


### TDB models of BI3Y5 (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): BI3Y5, type code %, sha256 `ac3d63c817a8399a…`

~~~~text
52: PHASE BI3Y5 % 2 3 5 !
53: CONST BI3Y5 : BI : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90159-3](https://doi.org/10.1016/0022-5088%2869%2990159-3) F.A. Schmidt, O.D. McMasters, R.R. Lichtenberg, The yttrium-bismuth alloy system, Journal of the Less Common Metals 18, 215-220 (1969).  
_cited as the source of values for this phase_

## BIY_B1 (Bi–Y)

- Id: `phase:bi-y:biy-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Y 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2293.25 K, x(Y) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:biy-b1)

Names (3): _corpus: _corpus:phase:bi-y:biy-b1  
_paper: _paper:10.1007/s11669-011-9939-1:BiY  
_tdb: _tdb:BiY-11Wan.tdb:BIY_B1  


### TDB models of BIY_B1 (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): BIY_B1, type code %, sha256 `ac3d63c817a8399a…`

~~~~text
47: PHASE BIY_B1 % 2 1 1 !
48: CONST BIY_B1 : BI : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90159-3](https://doi.org/10.1016/0022-5088%2869%2990159-3) F.A. Schmidt, O.D. McMasters, R.R. Lichtenberg, The yttrium-bismuth alloy system, Journal of the Less Common Metals 18, 215-220 (1969).  
_cited as the source of values for this phase_

## FCC_A1 (Bi–Y)

- Id: `phase:bi-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-y:fcc-a1  
_tdb: _tdb:BiY-11Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): FCC_A1, type code %A, sha256 `ac3d63c817a8399a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase_

## HCP_A3 (Bi–Y)

- Id: `phase:bi-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1751.97 K, x(Y) 0.99795–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-y:hcp-a3  
_paper: _paper:10.1007/s11669-011-9939-1:(αY)  
_tdb: _tdb:BiY-11Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): HCP_A3, type code %A, sha256 `ac3d63c817a8399a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI Y% : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90159-3](https://doi.org/10.1016/0022-5088%2869%2990159-3) F.A. Schmidt, O.D. McMasters, R.R. Lichtenberg, The yttrium-bismuth alloy system, Journal of the Less Common Metals 18, 215-220 (1969).  
_cited as the source of values for this phase_

## LIQUID (Bi–Y)

- Id: `phase:bi-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 544.55–2500 K, x(Y) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-y:liquid)

Names (3): _corpus: _corpus:phase:bi-y:liquid  
_paper: _paper:10.1007/s11669-011-9939-1:L  
_tdb: _tdb:BiY-11Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiY-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiY-11Wan.tdb): LIQUID, type code %, sha256 `ac3d63c817a8399a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-011-9939-1](https://doi.org/10.1007/s11669-011-9939-1) S. L. Wang, Z. B. Hu, F. Gao, C. P. Wang, X. J. Liu, Thermodynamic Assessments of the Bi-Tb and Bi-Y Systems, J. Phase Equilib. Diffus. 32, 441-446 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90159-3](https://doi.org/10.1016/0022-5088%2869%2990159-3) F.A. Schmidt, O.D. McMasters, R.R. Lichtenberg, The yttrium-bismuth alloy system, Journal of the Less Common Metals 18, 215-220 (1969).  
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
