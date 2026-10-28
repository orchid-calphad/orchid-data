# Bi–Gd phases

> Bi–Gd system: 9 phases (tier A 6, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-GD.html · Markdown: https://data.orchid-project.org/phases/pages/BI-GD.md

9 phases (tier A 6, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-GD) · [full JSON](https://data.orchid-project.org/phases/systems/BI-GD.json) · [Bi–Gd system page](https://data.orchid-project.org/systems/BI-GD.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-GD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Gd system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-gd-a7-rhombohedral); _phase:bi-gd:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Gd) 0–0 | 2 | 1 |
| [BCC_A2](#phase-bi-gd-bcc-a2); _phase:bi-gd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1508.15–2499.4 K, x(Gd) 1–1 | 0 | 1 |
| [BI2GD](#phase-bi-gd-bi2gd); _phase:bi-gd:bi2gd_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1179.06 K, x(Gd) 0.33333–0.33333 | 4 | 1 |
| [BI3GD4_D73](#phase-bi-gd-bi3gd4-d73); _phase:bi-gd:bi3gd4-d73_ | Th3P4 · D7_3 · cI28 · I-43d (220) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1852.34 K, x(Gd) 0.57143–0.57143 | 4 | 1 |
| [BI3GD5](#phase-bi-gd-bi3gd5); _phase:bi-gd:bi3gd5_ | Bi3Y5 · oP32 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1751.06 K, x(Gd) 0.625–0.625 | 4 | 1 |
| [BIGD_B1](#phase-bi-gd-bigd-b1); _phase:bi-gd:bigd-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2041.69 K, x(Gd) 0.5–0.5 | 6 | 1 |
| [FCC_A1](#phase-bi-gd-fcc-a1); _phase:bi-gd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-bi-gd-hcp-a3); _phase:bi-gd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1508.15 K, x(Gd) 1–1 | 2 | 1 |
| [LIQUID](#phase-bi-gd-liquid); _phase:bi-gd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 540.71–2500 K, x(Gd) 0–1 | 18 | 1 |

## RHOMBOHEDRAL_A7 (Bi–Gd)

- Id: `phase:bi-gd:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–544.55 K, x(Gd) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:bi-gd:a7-rhombohedral, corpus:phase:bi-gd:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2013.01.003:Rhomb_A7 (Bi)  
_tdb: _tdb:BiGd-13Wan.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `deb2422aa42efa6f…`

~~~~text
46: PHASE RHOMBOHEDRAL_A7 % 1 1 !
47: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Bi–Gd)

- Id: `phase:bi-gd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1508.15–2499.4 K, x(Gd) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:bcc-a2)

Names (2): _corpus: _corpus:phase:bi-gd:bcc-a2  
_tdb: _tdb:BiGd-13Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): BCC_A2, type code %B, sha256 `deb2422aa42efa6f…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : BI GD% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase_

## BI2GD (Bi–Gd)

- Id: `phase:bi-gd:bi2gd`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (literature_printed): (Bi2Gd) · ? — printed with a label mapped to this phase
- Candidate (sgte_mmc2): (Bi2Gd) — Hallstedt 2025 mmc2 row for BI2GD: Bi2Gd
- Stoichiometry: Bi 0.6667, Gd 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1179.06 K, x(Gd) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:bi2gd)

Names (3): _corpus: _corpus:phase:bi-gd:bi2gd  
_paper: _paper:10.1016/j.calphad.2013.01.003:GdBi2  
_tdb: _tdb:BiGd-13Wan.tdb:BI2GD  


### TDB models of BI2GD (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): BI2GD, type code %, sha256 `deb2422aa42efa6f…`

~~~~text
51: PHASE BI2GD % 2 2 1 !
52: CONST BI2GD : BI : GD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

## BI3GD4_D73 (Bi–Gd)

- Id: `phase:bi-gd:bi3gd4-d73`; status `assigned`
- Structure: Th3P4 · D7_3 · cI28 · I-43d (220); type `st:d7-3-th3p4-ci28`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.4286, Gd 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1852.34 K, x(Gd) 0.57143–0.57143
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:bi3gd4-d73)

Names (3): _corpus: _corpus:phase:bi-gd:bi3gd4-d73  
_paper: _paper:10.1016/j.calphad.2013.01.003:Gd4Bi3  
_tdb: _tdb:BiGd-13Wan.tdb:BI3GD4_D73  


### TDB models of BI3GD4_D73 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): BI3GD4_D73, type code %, sha256 `deb2422aa42efa6f…`

~~~~text
61: PHASE BI3GD4_D73 % 2 3 4 !
62: CONST BI3GD4_D73 : BI : GD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

## BI3GD5 (Bi–Gd)

- Id: `phase:bi-gd:bi3gd5`; status `assigned`
- Structure: Bi3Y5 · oP32 · Pnma (62); type `st:bi3y5-op32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Bi 0.3750, Gd 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1751.06 K, x(Gd) 0.625–0.625
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:bi3gd5)

Names (3): _corpus: _corpus:phase:bi-gd:bi3gd5  
_paper: _paper:10.1016/j.calphad.2013.01.003:Gd5Bi3  
_tdb: _tdb:BiGd-13Wan.tdb:BI3GD5  


### TDB models of BI3GD5 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): BI3GD5, type code %, sha256 `deb2422aa42efa6f…`

~~~~text
66: PHASE BI3GD5 % 2 3 5 !
67: CONST BI3GD5 : BI : GD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

## BIGD_B1 (Bi–Gd)

- Id: `phase:bi-gd:bigd-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 0.5000, Gd 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2041.69 K, x(Gd) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:bigd-b1)

Names (3): _corpus: _corpus:phase:bi-gd:bigd-b1  
_paper: _paper:10.1016/j.calphad.2013.01.003:GdBi  
_tdb: _tdb:BiGd-13Wan.tdb:BIGD_B1  


### TDB models of BIGD_B1 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): BIGD_B1, type code %, sha256 `deb2422aa42efa6f…`

~~~~text
56: PHASE BIGD_B1 % 2 1 1 !
57: CONST BIGD_B1 : BI : GD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Bi–Gd)

- Id: `phase:bi-gd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:fcc-a1)

Names (2): _corpus: _corpus:phase:bi-gd:fcc-a1  
_tdb: _tdb:BiGd-13Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): FCC_A1, type code %A, sha256 `deb2422aa42efa6f…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : BI GD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase_

## HCP_A3 (Bi–Gd)

- Id: `phase:bi-gd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1508.15 K, x(Gd) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:hcp-a3)

Names (3): _corpus: _corpus:phase:bi-gd:hcp-a3  
_paper: _paper:10.1016/j.calphad.2013.01.003:Hcp_A3 (Gd)  
_tdb: _tdb:BiGd-13Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): HCP_A3, type code %A, sha256 `deb2422aa42efa6f…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : BI GD% : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Bi–Gd)

- Id: `phase:bi-gd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 540.71–2500 K, x(Gd) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-gd:liquid)

Names (4): _corpus: _corpus:phase:bi-gd:liquid  
_paper: _paper:10.1016/j.calphad.2013.01.003:L, paper:10.1016/j.calphad.2013.01.003:Liquid  
_tdb: _tdb:BiGd-13Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BiGd-13Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/BiGd-13Wan.tdb): LIQUID, type code %, sha256 `deb2422aa42efa6f…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : BI GD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.003](https://doi.org/10.1016/j.calphad.2013.01.003) Jinsan Wang, Changrong Li, Cuiping Guo, Zhenmin Du, Bo Wu, Thermodynamic assessment of the Gd–Bi and the Ho–Bi systems, Calphad 41, 1-5 (2013).  
_assessment that models this phase; reports values for this phase_

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
