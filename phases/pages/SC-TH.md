# Sc–Th phases

> Sc–Th system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SC-TH.html · Markdown: https://data.orchid-project.org/phases/pages/SC-TH.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SC-TH) · [full JSON](https://data.orchid-project.org/phases/systems/SC-TH.json) · [Sc–Th system page](https://data.orchid-project.org/systems/SC-TH.html) · [Markdown](https://data.orchid-project.org/phases/pages/SC-TH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sc–Th system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-sc-th-bcc-a2); _phase:sc-th:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1423.13–2022.99 K, x(Th) 0–1 | 11 | 1 |
| [FCC_A1](#phase-sc-th-fcc-a1); _phase:sc-th:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1633.2 K, x(Th) 0.36725–1 | 5 | 1 |
| [HCP_A3](#phase-sc-th-hcp-a3); _phase:sc-th:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Th) 0–0.21171 | 5 | 1 |
| [LIQUID](#phase-sc-th-liquid); _phase:sc-th:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1678.37–4000 K, x(Th) 0–1 | 4 | 1 |

## BCC_A2 (Sc–Th)

- Id: `phase:sc-th:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1423.13–2022.99 K, x(Th) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-th:bcc-a2)

Names (5): _corpus: _corpus:phase:sc-th:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.02.018:(βSc, βTh), paper:10.1016/j.jallcom.2008.02.018:βSc, paper:10.1016/j.jallcom.2008.02.018:βTh  
_tdb: _tdb:ScTh-09Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ScTh-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScTh-09Liu.tdb): BCC_A2, type code %B, sha256 `8d3c6dbf1d99af30…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : SC TH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sc–Th)

- Id: `phase:sc-th:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1633.2 K, x(Th) 0.36725–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-th:fcc-a1)

Names (3): _corpus: _corpus:phase:sc-th:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2008.02.018:αTh  
_tdb: _tdb:ScTh-09Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ScTh-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScTh-09Liu.tdb): FCC_A1, type code %A, sha256 `8d3c6dbf1d99af30…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : SC TH% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Sc–Th)

- Id: `phase:sc-th:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Th) 0–0.21171
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-th:hcp-a3)

Names (3): _corpus: _corpus:phase:sc-th:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.02.018:αSc  
_tdb: _tdb:ScTh-09Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ScTh-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScTh-09Liu.tdb): HCP_A3, type code %A, sha256 `8d3c6dbf1d99af30…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : SC% TH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Sc–Th)

- Id: `phase:sc-th:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1678.37–4000 K, x(Th) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-th:liquid)

Names (3): _corpus: _corpus:phase:sc-th:liquid  
_paper: _paper:10.1016/j.jallcom.2008.02.018:L  
_tdb: _tdb:ScTh-09Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ScTh-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/ScTh-09Liu.tdb): LIQUID, type code %, sha256 `8d3c6dbf1d99af30…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : SC TH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.02.018](https://doi.org/10.1016/j.jallcom.2008.02.018) X.J. Liu, S.L. Wang, C.P. Wang, Thermodynamic assessments of the Sc–M (M: Ag, B and Th) systems, Journal of Alloys and Compounds 469, 186-192 (2009).  
_assessment that models this phase; reports values for this phase_

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
