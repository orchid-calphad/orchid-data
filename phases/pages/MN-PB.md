# Mn–Pb phases

> Mn–Pb system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-PB.html · Markdown: https://data.orchid-project.org/phases/pages/MN-PB.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-PB) · [full JSON](https://data.orchid-project.org/phases/systems/MN-PB.json) · [Mn–Pb system page](https://data.orchid-project.org/systems/MN-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Pb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-pb-bcc-a2); _phase:mn-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1400–1528.16 K, x(Pb) 0–0.68 | 0 | 2 |
| [CBCC_A12](#phase-mn-pb-cbcc-a12); _phase:mn-pb:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–980 K, x(Pb) 0–0 | 0 | 2 |
| [CUB_A13](#phase-mn-pb-cub-a13); _phase:mn-pb:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 980–1444.99 K, x(Pb) 0–0 | 0 | 2 |
| [FCC_A1](#phase-mn-pb-fcc-a1); _phase:mn-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Pb) 0–1 | 0 | 2 |
| [HCP_A3](#phase-mn-pb-hcp-a3); _phase:mn-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-mn-pb-liquid); _phase:mn-pb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 569.27–2500 K, x(Pb) 0–1 | 0 | 2 |

## BCC_A2 (Mn–Pb)

- Id: `phase:mn-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1400–1528.16 K, x(Pb) 0–0.68
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:mn-pb:bcc-a2  
_tdb: _tdb:MnPb-03Din-LB.tdb:BCC_A2, tdb:MnPb-87Din.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MnPb-03Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-03Din-LB.tdb): BCC_A2, type code %B, sha256 `8e4bfbc81e63630c…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MN% PB : VA : !
~~~~

[MnPb-87Din.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-87Din.tdb): BCC_A2, type code %B, sha256 `c1f9f8be18442595…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MN% PB : VA : !
~~~~

## CBCC_A12 (Mn–Pb)

- Id: `phase:mn-pb:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–980 K, x(Pb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pb:cbcc-a12)

Names (3): _corpus: _corpus:phase:mn-pb:cbcc-a12  
_tdb: _tdb:MnPb-03Din-LB.tdb:CBCC_A12, tdb:MnPb-87Din.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[MnPb-03Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-03Din-LB.tdb): CBCC_A12, type code %A, sha256 `8e4bfbc81e63630c…`

~~~~text
43: PHASE CBCC_A12 %A 2 1 1 !
44: CONST CBCC_A12 : MN : VA : !
~~~~

[MnPb-87Din.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-87Din.tdb): CBCC_A12, type code %A, sha256 `c1f9f8be18442595…`

~~~~text
44: PHASE CBCC_A12 %A 2 1 1 !
45: CONST CBCC_A12 : MN : VA : !
~~~~

## CUB_A13 (Mn–Pb)

- Id: `phase:mn-pb:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 980–1444.99 K, x(Pb) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pb:cub-a13)

Names (3): _corpus: _corpus:phase:mn-pb:cub-a13  
_tdb: _tdb:MnPb-03Din-LB.tdb:CUB_A13, tdb:MnPb-87Din.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[MnPb-03Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-03Din-LB.tdb): CUB_A13, type code %, sha256 `8e4bfbc81e63630c…`

~~~~text
48: PHASE CUB_A13 % 2 1 1 !
49: CONST CUB_A13 : MN : VA : !
~~~~

[MnPb-87Din.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-87Din.tdb): CUB_A13, type code %, sha256 `c1f9f8be18442595…`

~~~~text
49: PHASE CUB_A13 % 2 1 1 !
50: CONST CUB_A13 : MN : VA : !
~~~~

## FCC_A1 (Mn–Pb)

- Id: `phase:mn-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Pb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pb:fcc-a1)

Names (3): _corpus: _corpus:phase:mn-pb:fcc-a1  
_tdb: _tdb:MnPb-03Din-LB.tdb:FCC_A1, tdb:MnPb-87Din.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MnPb-03Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-03Din-LB.tdb): FCC_A1, type code %A, sha256 `8e4bfbc81e63630c…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MN% PB% : VA : !
~~~~

[MnPb-87Din.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-87Din.tdb): FCC_A1, type code %A, sha256 `c1f9f8be18442595…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MN% PB% : VA : !
~~~~

## HCP_A3 (Mn–Pb)

- Id: `phase:mn-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pb:hcp-a3)

Names (3): _corpus: _corpus:phase:mn-pb:hcp-a3  
_tdb: _tdb:MnPb-03Din-LB.tdb:HCP_A3, tdb:MnPb-87Din.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MnPb-03Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-03Din-LB.tdb): HCP_A3, type code %A, sha256 `8e4bfbc81e63630c…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MN PB : VA : !
~~~~

[MnPb-87Din.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-87Din.tdb): HCP_A3, type code %A, sha256 `c1f9f8be18442595…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MN PB : VA : !
~~~~

## LIQUID (Mn–Pb)

- Id: `phase:mn-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 569.27–2500 K, x(Pb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-pb:liquid)

Names (3): _corpus: _corpus:phase:mn-pb:liquid  
_tdb: _tdb:MnPb-03Din-LB.tdb:LIQUID, tdb:MnPb-87Din.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnPb-03Din-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-03Din-LB.tdb): LIQUID, type code %, sha256 `8e4bfbc81e63630c…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MN PB : !
~~~~

[MnPb-87Din.tdb](https://orchid-project.org/data/databases/sgte-binary/MnPb-87Din.tdb): LIQUID, type code %, sha256 `c1f9f8be18442595…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MN PB : !
~~~~

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
