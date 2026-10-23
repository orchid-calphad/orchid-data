# S–Se phases

> S–Se system: 6 phases (tier A 2, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/S-SE.html · Markdown: https://data.orchid-project.org/phases/pages/S-SE.md

6 phases (tier A 2, liquid 1, gas 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=S-SE) · [full JSON](https://data.orchid-project.org/phases/systems/S-SE.json) · [S–Se system page](https://data.orchid-project.org/systems/S-SE.html) · [Markdown](https://data.orchid-project.org/phases/pages/S-SE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the S–Se system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-s-se-a16-orthorhombic); _phase:s-se:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(Se) 0–0.15751 | 0 | 1 |
| [HEXAGONAL_A8](#phase-s-se-a8-hexagonal); _phase:s-se:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 0.90441–1 | 0 | 1 |
| [GAS](#phase-s-se-gas); _phase:s-se:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 735.04–2500 K, x(Se) 0–1 | 0 | 1 |
| [LIQUID](#phase-s-se-liquid); _phase:s-se:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 356.72–1040 K, x(Se) 0–1 | 0 | 1 |
| [MONOCLINIC_S](#phase-s-se-s-monoclinic); _phase:s-se:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |
| [SSE](#phase-s-se-sse); _phase:s-se:sse_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–433.11 K, x(Se) 0.34802–0.83282 | 0 | 1 |

## ORTHORHOMBIC_A16 (S–Se)

- Id: `phase:s-se:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–384.34 K, x(Se) 0–0.15751
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-se:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:s-se:a16-orthorhombic  
_tdb: _tdb:SSe-17Gua.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[SSe-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb): ORTHORHOMBIC_A16, type code %, sha256 `69fc3205ab133df2…`

~~~~text
49: PHASE ORTHORHOMBIC_A16 % 1 1 !
50: CONST ORTHORHOMBIC_A16 : S% SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017).  
_assessment that models this phase_

## HEXAGONAL_A8 (S–Se)

- Id: `phase:s-se:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–494 K, x(Se) 0.90441–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-se:a8-hexagonal)

Names (2): _corpus: _corpus:phase:s-se:a8-hexagonal  
_tdb: _tdb:SSe-17Gua.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[SSe-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb): HEXAGONAL_A8, type code %, sha256 `69fc3205ab133df2…`

~~~~text
44: PHASE HEXAGONAL_A8 % 1 1 !
45: CONST HEXAGONAL_A8 : S SE% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017).  
_assessment that models this phase_

## GAS (S–Se)

- Id: `phase:s-se:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 735.04–2500 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-se:gas)

Names (2): _corpus: _corpus:phase:s-se:gas  
_tdb: _tdb:SSe-17Gua.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[SSe-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb): GAS, type code %, sha256 `69fc3205ab133df2…`

~~~~text
62: PHASE GAS:G % 1 1 !
63: CONST GAS:G : S S2 S3 S4 S5 S6 S7 S8 SSE SE SE2 SE3 SE4 SE5 SE6 SE7 SE8 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017).  
_assessment that models this phase_

## LIQUID (S–Se)

- Id: `phase:s-se:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 356.72–1040 K, x(Se) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-se:liquid)

Names (2): _corpus: _corpus:phase:s-se:liquid  
_tdb: _tdb:SSe-17Gua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SSe-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb): LIQUID, type code %, sha256 `69fc3205ab133df2…`

~~~~text
39: PHASE LIQUID:L % 1 1 !
40: CONST LIQUID:L : S SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017).  
_assessment that models this phase_

## MONOCLINIC_S (S–Se)

- Id: `phase:s-se:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — SSe-17Gua.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-se:s-monoclinic)

Names (2): _corpus: _corpus:phase:s-se:s-monoclinic  
_tdb: _tdb:SSe-17Gua.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[SSe-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb): MONOCLINIC_S, type code %, sha256 `69fc3205ab133df2…`

~~~~text
54: PHASE MONOCLINIC_S % 1 1 !
55: CONST MONOCLINIC_S : S% SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017).  
_assessment that models this phase_

## SSE (S–Se)

- Id: `phase:s-se:sse`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (SSe) — Hallstedt 2025 mmc2 row for SSE: SSe (X-phase)
- Stability: stable in 1 of 1 calculated diagram(s): 300–433.11 K, x(Se) 0.34802–0.83282
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:s-se:sse)

Names (2): _corpus: _corpus:phase:s-se:sse  
_tdb: _tdb:SSe-17Gua.tdb:SSE  


### TDB models of SSE (1): PHASE and CONSTITUENT statements as written

[SSe-17Gua.tdb](https://orchid-project.org/data/databases/sgte-binary/SSe-17Gua.tdb): SSE, type code %, sha256 `69fc3205ab133df2…`

~~~~text
59: PHASE SSE % 1 1 !
60: CONST SSE : S SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.10.037](https://doi.org/10.1016/j.jallcom.2016.10.037) Pin-Wen Guan, Shun-Li Shang, Greta Lindwall, Tim Anderson, Zi-Kui Liu, First-principles calculations and thermodynamic modeling of the S-Se system and implications for chalcogenide alloys, Journal of Alloys and Compounds 694, 510-521 (2017).  
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
