# Ba–Ti phases

> Ba–Ti system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-TI.html · Markdown: https://data.orchid-project.org/phases/pages/BA-TI.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-TI) · [full JSON](https://data.orchid-project.org/phases/systems/BA-TI.json) · [Ba–Ti system page](https://data.orchid-project.org/systems/BA-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Ti system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ba-ti-bcc-a2); _phase:ba-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.73 K, x(Ti) 0–1 | 6 | 1 |
| [FCC_A1](#phase-ba-ti-fcc-a1); _phase:ba-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 10 | 1 |
| [HCP_A3](#phase-ba-ti-hcp-a3); _phase:ba-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 1–1 | 10 | 1 |
| [LIQUID](#phase-ba-ti-liquid); _phase:ba-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 999.92–2500 K, x(Ti) 0–1 | 0 | 1 |

## BCC_A2 (Ba–Ti)

- Id: `phase:ba-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.73 K, x(Ti) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ti:bcc-a2)

Names (3): _corpus: _corpus:phase:ba-ti:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2006.03.096:Bcc  
_tdb: _tdb:BaTi-07Sha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BaTi-07Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/BaTi-07Sha.tdb): BCC_A2, type code %B, sha256 `c2404dc113a3c952…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : BA% TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096) Shunli Shang, Zhi-Jie Liu, Zi-Kui Liu, Thermodynamic modeling of the Ba–Ni–Ti system, Journal of Alloys and Compounds 430, 188-193 (2007).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Ba–Ti)

- Id: `phase:ba-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:ba-ti:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2006.03.096:Fcc  
_tdb: _tdb:BaTi-07Sha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BaTi-07Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/BaTi-07Sha.tdb): FCC_A1, type code %A, sha256 `c2404dc113a3c952…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : BA TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096) Shunli Shang, Zhi-Jie Liu, Zi-Kui Liu, Thermodynamic modeling of the Ba–Ni–Ti system, Journal of Alloys and Compounds 430, 188-193 (2007).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ba–Ti)

- Id: `phase:ba-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1154.99 K, x(Ti) 1–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ti:hcp-a3)

Names (3): _corpus: _corpus:phase:ba-ti:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2006.03.096:Hcp  
_tdb: _tdb:BaTi-07Sha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BaTi-07Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/BaTi-07Sha.tdb): HCP_A3, type code %A, sha256 `c2404dc113a3c952…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : BA TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096) Shunli Shang, Zhi-Jie Liu, Zi-Kui Liu, Thermodynamic modeling of the Ba–Ni–Ti system, Journal of Alloys and Compounds 430, 188-193 (2007).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ba–Ti)

- Id: `phase:ba-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 999.92–2500 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ti:liquid)

Names (2): _corpus: _corpus:phase:ba-ti:liquid  
_tdb: _tdb:BaTi-07Sha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaTi-07Sha.tdb](https://orchid-project.org/data/databases/sgte-binary/BaTi-07Sha.tdb): LIQUID, type code %, sha256 `c2404dc113a3c952…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : BA TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.03.096](https://doi.org/10.1016/j.jallcom.2006.03.096) Shunli Shang, Zhi-Jie Liu, Zi-Kui Liu, Thermodynamic modeling of the Ba–Ni–Ti system, Journal of Alloys and Compounds 430, 188-193 (2007).  
_assessment that models this phase_

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
