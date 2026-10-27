# Ca–Mn phases

> Ca–Mn system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-MN.html · Markdown: https://data.orchid-project.org/phases/pages/CA-MN.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-MN) · [full JSON](https://data.orchid-project.org/phases/systems/CA-MN.json) · [Ca–Mn system page](https://data.orchid-project.org/systems/CA-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Mn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-mn-bcc-a2); _phase:ca-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 716.04–1623.99 K, x(Mn) 0–1 | 0 | 1 |
| [CBCC_A12](#phase-ca-mn-cbcc-a12); _phase:ca-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–980 K, x(Mn) 1–1 | 0 | 1 |
| [CUB_A13](#phase-ca-mn-cub-a13); _phase:ca-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 980–1480 K, x(Mn) 1–1 | 0 | 1 |
| [FCC_A1](#phase-ca-mn-fcc-a1); _phase:ca-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1490 K, x(Mn) 0–1 | 0 | 1 |
| [HCP_A3](#phase-ca-mn-hcp-a3); _phase:ca-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ca-mn-liquid); _phase:ca-mn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1111.81–2500 K, x(Mn) 0–1 | 0 | 1 |

## BCC_A2 (Ca–Mn)

- Id: `phase:ca-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 716.04–1623.99 K, x(Mn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mn:bcc-a2)

Names (2): _corpus: _corpus:phase:ca-mn:bcc-a2  
_tdb: _tdb:CaMn-16Dil.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaMn-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMn-16Dil.tdb): BCC_A2, type code %B, sha256 `45760714f309b6fd…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CA% MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.03.005](https://doi.org/10.1016/j.calphad.2016.03.005) D. Dilner, Calphad, 53, 55-61(2016).  
_assessment that models this phase_

## CBCC_A12 (Ca–Mn)

- Id: `phase:ca-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–980 K, x(Mn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mn:cbcc-a12)

Names (2): _corpus: _corpus:phase:ca-mn:cbcc-a12  
_tdb: _tdb:CaMn-16Dil.tdb:CBCC_A12  


### TDB models of CBCC_A12 (1): PHASE and CONSTITUENT statements as written

[CaMn-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMn-16Dil.tdb): CBCC_A12, type code %A, sha256 `45760714f309b6fd…`

~~~~text
39: PHASE CBCC_A12 %A 2 1 1 !
40: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.03.005](https://doi.org/10.1016/j.calphad.2016.03.005) D. Dilner, Calphad, 53, 55-61(2016).  
_assessment that models this phase_

## CUB_A13 (Ca–Mn)

- Id: `phase:ca-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 980–1480 K, x(Mn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mn:cub-a13)

Names (2): _corpus: _corpus:phase:ca-mn:cub-a13  
_tdb: _tdb:CaMn-16Dil.tdb:CUB_A13  


### TDB models of CUB_A13 (1): PHASE and CONSTITUENT statements as written

[CaMn-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMn-16Dil.tdb): CUB_A13, type code %, sha256 `45760714f309b6fd…`

~~~~text
44: PHASE CUB_A13 % 2 1 1 !
45: CONST CUB_A13 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.03.005](https://doi.org/10.1016/j.calphad.2016.03.005) D. Dilner, Calphad, 53, 55-61(2016).  
_assessment that models this phase_

## FCC_A1 (Ca–Mn)

- Id: `phase:ca-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1490 K, x(Mn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mn:fcc-a1)

Names (2): _corpus: _corpus:phase:ca-mn:fcc-a1  
_tdb: _tdb:CaMn-16Dil.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaMn-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMn-16Dil.tdb): FCC_A1, type code %A, sha256 `45760714f309b6fd…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CA% MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.03.005](https://doi.org/10.1016/j.calphad.2016.03.005) D. Dilner, Calphad, 53, 55-61(2016).  
_assessment that models this phase_

## HCP_A3 (Ca–Mn)

- Id: `phase:ca-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mn:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-mn:hcp-a3  
_tdb: _tdb:CaMn-16Dil.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaMn-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMn-16Dil.tdb): HCP_A3, type code %A, sha256 `45760714f309b6fd…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CA MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.03.005](https://doi.org/10.1016/j.calphad.2016.03.005) D. Dilner, Calphad, 53, 55-61(2016).  
_assessment that models this phase_

## LIQUID (Ca–Mn)

- Id: `phase:ca-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1111.81–2500 K, x(Mn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-mn:liquid)

Names (2): _corpus: _corpus:phase:ca-mn:liquid  
_tdb: _tdb:CaMn-16Dil.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaMn-16Dil.tdb](https://orchid-project.org/data/databases/sgte-binary/CaMn-16Dil.tdb): LIQUID, type code %, sha256 `45760714f309b6fd…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CA MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.03.005](https://doi.org/10.1016/j.calphad.2016.03.005) D. Dilner, Calphad, 53, 55-61(2016).  
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
