# Pb–S phases

> Pb–S system: 7 phases (tier A 5, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-S.html · Markdown: https://data.orchid-project.org/phases/pages/PB-S.md

7 phases (tier A 5, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-S) · [full JSON](https://data.orchid-project.org/phases/systems/PB-S.json) · [Pb–S system page](https://data.orchid-project.org/systems/PB-S.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-S.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–S system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A16](#phase-pb-s-a16-orthorhombic); _phase:pb-s:a16-orthorhombic_ | alpha-S · A16 · oF128 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–385.34 K, x(S) 1–1 | 0 | 1 |
| [BCC_A2](#phase-pb-s-bcc-a2); _phase:pb-s:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-pb-s-fcc-a1); _phase:pb-s:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–609.61 K, x(S) 0–0 | 1 | 1 |
| [HCP_A3](#phase-pb-s-hcp-a3); _phase:pb-s:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pb-s-liquid); _phase:pb-s:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1 | 4 | 1 |
| [PBS_B1](#phase-pb-s-pbs-b1); _phase:pb-s:pbs-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2141.78 K, x(S) 0.5–0.5 | 4 | 1 |
| [MONOCLINIC_S](#phase-pb-s-s-monoclinic); _phase:pb-s:s-monoclinic_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## ORTHORHOMBIC_A16 (Pb–S)

- Id: `phase:pb-s:a16-orthorhombic`; status `assigned`
- Structure: alpha-S · A16 · oF128 · Fddd (70); type `st:a16-alpha-s-of128`; tier A: standard phase name; confidence high
- Stoichiometry: S 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–385.34 K, x(S) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:a16-orthorhombic)

Names (2): _corpus: _corpus:phase:pb-s:a16-orthorhombic  
_tdb: _tdb:PbS-14Hua.tdb:ORTHORHOMBIC_A16  


### TDB models of ORTHORHOMBIC_A16 (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): ORTHORHOMBIC_A16, type code %, sha256 `af71b52445492a1d…`

~~~~text
44: PHASE ORTHORHOMBIC_A16 % 1 1 !
45: CONST ORTHORHOMBIC_A16 : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## BCC_A2 (Pb–S)

- Id: `phase:pb-s:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:bcc-a2)

Names (2): _corpus: _corpus:phase:pb-s:bcc-a2  
_tdb: _tdb:PbS-14Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): BCC_A2, type code %B, sha256 `af71b52445492a1d…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PB S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## FCC_A1 (Pb–S)

- Id: `phase:pb-s:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–609.61 K, x(S) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:fcc-a1)

Names (3): _corpus: _corpus:phase:pb-s:fcc-a1  
_paper: _paper:10.1007/s11664-014-3004-x:fcc  
_tdb: _tdb:PbS-14Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): FCC_A1, type code %A, sha256 `af71b52445492a1d…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PB% S : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Pb–S)

- Id: `phase:pb-s:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:hcp-a3)

Names (2): _corpus: _corpus:phase:pb-s:hcp-a3  
_tdb: _tdb:PbS-14Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): HCP_A3, type code %A, sha256 `af71b52445492a1d…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : PB : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

## LIQUID (Pb–S)

- Id: `phase:pb-s:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 384.34–2500 K, x(S) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:liquid)

Names (4): _corpus: _corpus:phase:pb-s:liquid  
_paper: _paper:10.1007/s11664-014-3004-x:liq, paper:10.1007/s11664-014-3004-x:liq2  
_tdb: _tdb:PbS-14Hua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): LIQUID, type code %, sha256 `af71b52445492a1d…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : PB PBS S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2475/001c.125221](https://doi.org/10.2475/001c.125221) G. Kullerud, The Lead-Sulfur System, American Journal of Science 267-A (1969).  
_cited as the source of values for this phase_

## PBS_B1 (Pb–S)

- Id: `phase:pb-s:pbs-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabfmi and oqmd-11589, space group 225
- Stoichiometry: Pb 0.5000, S 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2141.78 K, x(S) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:pbs-b1)

Names (5): _corpus: _corpus:phase:pb-s:pbs-b1  
_mp: _mp:mp-aaaabfmi  
_oqmd: _oqmd:oqmd-11589  
_paper: _paper:10.1007/s11664-014-3004-x:PbS  
_tdb: _tdb:PbS-14Hua.tdb:PBS_B1  


### TDB models of PBS_B1 (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): PBS_B1, type code %, sha256 `af71b52445492a1d…`

~~~~text
54: PHASE PBS_B1 % 2 1 1 !
55: CONST PBS_B1 : PB : S : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2475/001c.125221](https://doi.org/10.2475/001c.125221) G. Kullerud, The Lead-Sulfur System, American Journal of Science 267-A (1969).  
_cited as the source of values for this phase_

## MONOCLINIC_S (Pb–S)

- Id: `phase:pb-s:s-monoclinic`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:MONOCLINIC; no_structure_token
- Candidate (sgte_mmc2): beta-S · mP48 · P2_1/c (14) — Hallstedt 2025 mmc2 row for MONOCLINIC_S: beta-S
- Candidate (tdb_comment): beta-S · mP48 · P2_1/a — PbS-14Hua.tdb: 'Prototype beta-S (mP48, P2_1/a)'
- Stoichiometry: S 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-s:s-monoclinic)

Names (3): _corpus: _corpus:phase:pb-s:s-monoclinic, corpus:phase:pb-s:monoclinic-s  
_tdb: _tdb:PbS-14Hua.tdb:MONOCLINIC_S  


### TDB models of MONOCLINIC_S (1): PHASE and CONSTITUENT statements as written

[PbS-14Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PbS-14Hua.tdb): MONOCLINIC_S, type code %, sha256 `af71b52445492a1d…`

~~~~text
49: PHASE MONOCLINIC_S % 1 1 !
50: CONST MONOCLINIC_S : S : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-014-3004-x](https://doi.org/10.1007/s11664-014-3004-x) Shenming Huang, Yajun Liu, Yang Chen, Zhitao Kang, Thermodynamic Descriptions and Phase Diagrams for Pb-S and Bi-S Binary Systems, Journal of Elec Materi 43, 1237-1243 (2014).  
_assessment that models this phase_

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
