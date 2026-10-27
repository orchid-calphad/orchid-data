# Cr–H phases

> Cr–H system: 6 phases (tier A 3, liquid 1, gas 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-H.html · Markdown: https://data.orchid-project.org/phases/pages/CR-H.md

6 phases (tier A 3, liquid 1, gas 2); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-H) · [full JSON](https://data.orchid-project.org/phases/systems/CR-H.json) · [Cr–H system page](https://data.orchid-project.org/systems/CR-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–H system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-h-bcc-a2); _phase:cr-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2179.98 K, x(H) 0–0.00062 | 0 | 1 |
| [FCC_A1](#phase-cr-h-fcc-a1); _phase:cr-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-cr-h-gas); _phase:cr-h:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(H) 1–1 | 0 | 1 |
| [H2GAS](#phase-cr-h-h2gas); _phase:cr-h:h2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.47–1090.47 K, x(H) 1–1 | 0 | 1 |
| [HCP_A3](#phase-cr-h-hcp-a3); _phase:cr-h:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cr-h-liquid); _phase:cr-h:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2175.93–4000 K, x(H) 0–0.00276 | 0 | 1 |

## BCC_A2 (Cr–H)

- Id: `phase:cr-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2179.98 K, x(H) 0–0.00062
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-h:bcc-a2)

Names (2): _corpus: _corpus:phase:cr-h:bcc-a2  
_tdb: _tdb:CrH-22Dot.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CrH-22Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb): BCC_A2, type code %B, sha256 `f1aa3481524abf0b…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CR : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022).  
_assessment that models this phase_

## FCC_A1 (Cr–H)

- Id: `phase:cr-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-h:fcc-a1)

Names (2): _corpus: _corpus:phase:cr-h:fcc-a1  
_tdb: _tdb:CrH-22Dot.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CrH-22Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb): FCC_A1, type code %A, sha256 `f1aa3481524abf0b…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CR : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022).  
_assessment that models this phase_

## GAS (Cr–H)

- Id: `phase:cr-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-h:gas)

Names (2): _corpus: _corpus:phase:cr-h:gas  
_tdb: _tdb:CrH-22Dot.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[CrH-22Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb): GAS, type code %, sha256 `f1aa3481524abf0b…`

~~~~text
48: PHASE GAS:G % 1 1 !
49: CONST GAS:G : H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022).  
_assessment that models this phase_

## H2GAS (Cr–H)

- Id: `phase:cr-h:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.47–1090.47 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-h:h2gas)

Names (2): _corpus: _corpus:phase:cr-h:h2gas  
_tdb: _tdb:CrH-22Dot.tdb:H2GAS  


### TDB models of H2GAS (1): PHASE and CONSTITUENT statements as written

[CrH-22Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb): H2GAS, type code %, sha256 `f1aa3481524abf0b…`

~~~~text
51: PHASE H2GAS % 1 1 !
52: CONST H2GAS : H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022).  
_assessment that models this phase_

## HCP_A3 (Cr–H)

- Id: `phase:cr-h:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-h:hcp-a3)

Names (2): _corpus: _corpus:phase:cr-h:hcp-a3  
_tdb: _tdb:CrH-22Dot.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CrH-22Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb): HCP_A3, type code %A, sha256 `f1aa3481524abf0b…`

~~~~text
45: PHASE HCP_A3 %A 2 1 1 !
46: CONST HCP_A3 : CR : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022).  
_assessment that models this phase_

## LIQUID (Cr–H)

- Id: `phase:cr-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2175.93–4000 K, x(H) 0–0.00276
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-h:liquid)

Names (2): _corpus: _corpus:phase:cr-h:liquid  
_tdb: _tdb:CrH-22Dot.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CrH-22Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/CrH-22Dot.tdb): LIQUID, type code %, sha256 `f1aa3481524abf0b…`

~~~~text
29: PHASE LIQUID:L % 2 1 1 !
30: CONST LIQUID:L : CR : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2022.04.245](https://doi.org/10.1016/j.ijhydene.2022.04.245) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Thermodynamic modeling of Cr and Cr–H systems up to high temperatures and high pressures, International Journal of Hydrogen Energy 47, 23293-23309 (2022).  
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
