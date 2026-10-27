# Ba–Co phases

> Ba–Co system: 4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-CO.html · Markdown: https://data.orchid-project.org/phases/pages/BA-CO.md

4 phases (tier A 3, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-CO) · [full JSON](https://data.orchid-project.org/phases/systems/BA-CO.json) · [Ba–Co system page](https://data.orchid-project.org/systems/BA-CO.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-CO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Co system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ba-co-bcc-a2); _phase:ba-co:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Co) 0–0.0009 | 0 | 1 |
| [FCC_A1](#phase-ba-co-fcc-a1); _phase:ba-co:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 694.99–2499.23 K, x(Co) 0.99862–1 | 0 | 1 |
| [HCP_A3](#phase-ba-co-hcp-a3); _phase:ba-co:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–694.99 K, x(Co) 1–1 | 0 | 1 |
| [LIQUID](#phase-ba-co-liquid); _phase:ba-co:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 991.26–2500 K, x(Co) 0–1 | 0 | 1 |

## BCC_A2 (Ba–Co)

- Id: `phase:ba-co:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Co) 0–0.0009
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-co:bcc-a2)

Names (2): _corpus: _corpus:phase:ba-co:bcc-a2  
_tdb: _tdb:BaCo-19Hal.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BaCo-19Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCo-19Hal.tdb): BCC_A2, type code %B, sha256 `d6ff8cb4dc90e38b…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : BA% CO : VA : !
~~~~

## FCC_A1 (Ba–Co)

- Id: `phase:ba-co:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 694.99–2499.23 K, x(Co) 0.99862–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-co:fcc-a1)

Names (2): _corpus: _corpus:phase:ba-co:fcc-a1  
_tdb: _tdb:BaCo-19Hal.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BaCo-19Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCo-19Hal.tdb): FCC_A1, type code %A, sha256 `d6ff8cb4dc90e38b…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : BA CO% : VA : !
~~~~

## HCP_A3 (Ba–Co)

- Id: `phase:ba-co:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–694.99 K, x(Co) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-co:hcp-a3)

Names (2): _corpus: _corpus:phase:ba-co:hcp-a3  
_tdb: _tdb:BaCo-19Hal.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BaCo-19Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCo-19Hal.tdb): HCP_A3, type code %A, sha256 `d6ff8cb4dc90e38b…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : BA CO% : VA : !
~~~~

## LIQUID (Ba–Co)

- Id: `phase:ba-co:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 991.26–2500 K, x(Co) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-co:liquid)

Names (2): _corpus: _corpus:phase:ba-co:liquid  
_tdb: _tdb:BaCo-19Hal.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaCo-19Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/BaCo-19Hal.tdb): LIQUID, type code %, sha256 `d6ff8cb4dc90e38b…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : BA CO : !
~~~~

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
