# Ag–Ir phases

> Ag–Ir system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-IR.html · Markdown: https://data.orchid-project.org/phases/pages/AG-IR.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-IR) · [full JSON](https://data.orchid-project.org/phases/systems/AG-IR.json) · [Ag–Ir system page](https://data.orchid-project.org/systems/AG-IR.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-IR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Ir system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-ir-bcc-a2); _phase:ag-ir:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ag-ir-fcc-a1); _phase:ag-ir:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.72 K, x(Ir) 0–1 | 0 | 1 |
| [HCP_A3](#phase-ag-ir-hcp-a3); _phase:ag-ir:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ag-ir-liquid); _phase:ag-ir:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1234.01–4000 K, x(Ir) 0–1 | 0 | 1 |

## BCC_A2 (Ag–Ir)

- Id: `phase:ag-ir:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ir:bcc-a2)

Names (2): _corpus: _corpus:phase:ag-ir:bcc-a2  
_tdb: _tdb:AgIr-86Kar-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AgIr-86Kar-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIr-86Kar-LB.tdb): BCC_A2, type code %B, sha256 `8e51e6432e086899…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AG IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873021](https://doi.org/10.1007/BF02873021) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 7, 359-60(1986).  
_assessment that models this phase_

## FCC_A1 (Ag–Ir)

- Id: `phase:ag-ir:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.72 K, x(Ir) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ir:fcc-a1)

Names (2): _corpus: _corpus:phase:ag-ir:fcc-a1  
_tdb: _tdb:AgIr-86Kar-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AgIr-86Kar-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIr-86Kar-LB.tdb): FCC_A1, type code %A, sha256 `8e51e6432e086899…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AG% IR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873021](https://doi.org/10.1007/BF02873021) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 7, 359-60(1986).  
_assessment that models this phase_

## HCP_A3 (Ag–Ir)

- Id: `phase:ag-ir:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ir:hcp-a3)

Names (2): _corpus: _corpus:phase:ag-ir:hcp-a3  
_tdb: _tdb:AgIr-86Kar-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AgIr-86Kar-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIr-86Kar-LB.tdb): HCP_A3, type code %A, sha256 `8e51e6432e086899…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AG IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873021](https://doi.org/10.1007/BF02873021) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 7, 359-60(1986).  
_assessment that models this phase_

## LIQUID (Ag–Ir)

- Id: `phase:ag-ir:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1234.01–4000 K, x(Ir) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-ir:liquid)

Names (2): _corpus: _corpus:phase:ag-ir:liquid  
_tdb: _tdb:AgIr-86Kar-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AgIr-86Kar-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgIr-86Kar-LB.tdb): LIQUID, type code %, sha256 `8e51e6432e086899…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AG IR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02873021](https://doi.org/10.1007/BF02873021) I. Karakaya, W.T. Thompson, Bull. Alloy Phase Diag., 7, 359-60(1986).  
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
