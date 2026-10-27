# Np–U phases

> Np–U system: 9 phases (tier A 6, liquid 1, needs_review 2); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NP-U.html · Markdown: https://data.orchid-project.org/phases/pages/NP-U.md

9 phases (tier A 6, liquid 1, needs_review 2); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NP-U) · [full JSON](https://data.orchid-project.org/phases/systems/NP-U.json) · [Np–U system page](https://data.orchid-project.org/systems/NP-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/NP-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Np–U system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-np-u-a20-orthorhombic); _phase:np-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–942.02 K, x(U) 0.53691–1 | 0 | 2 |
| [TETRAG_AD](#phase-np-u-ad-tetrag); _phase:np-u:ad-tetrag_ | beta-Np · A_d · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 458.9–896.5 K, x(U) 0–0.26653 | 0 | 2 |
| [BCC_A2](#phase-np-u-bcc-a2); _phase:np-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 856.06–2542.99 K, x(U) 0–1 | 0 | 2 |
| [FCC_A1](#phase-np-u-fcc-a1); _phase:np-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-np-u-hcp-a3); _phase:np-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-np-u-liquid); _phase:np-u:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 917.28–4000 K, x(U) 0–1 | 0 | 2 |
| [NPU_ZETA](#phase-np-u-npu-zeta); _phase:np-u:npu-zeta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–946.63 K, x(U) 0.23414–0.71951 | 0 | 2 |
| [ORTHO_AC](#phase-np-u-ortho-ac); _phase:np-u:ortho-ac_ | alpha-Np · A_c · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–555.02 K, x(U) 0–0.1032 | 0 | 2 |
| [TETRAGONAL_U](#phase-np-u-u-tetragonal); _phase:np-u:u-tetragonal_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 914.55–1048.82 K, x(U) 0.69334–1 | 0 | 2 |

## ORTHORHOMBIC_A20 (Np–U)

- Id: `phase:np-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–942.02 K, x(U) 0.53691–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:a20-orthorhombic)

Names (3): _corpus: _corpus:phase:np-u:a20-orthorhombic  
_tdb: _tdb:NpU-10Kur.tdb:ORTHORHOMBIC_A20, tdb:NpU-18Xie.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `f85b49b94decbbee…`

~~~~text
52: PHASE ORTHORHOMBIC_A20 % 1 1 !
53: CONST ORTHORHOMBIC_A20 : NP U% : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): ORTHORHOMBIC_A20, type code %, sha256 `1d2cc8e207135d92…`

~~~~text
50: PHASE ORTHORHOMBIC_A20 % 1 1 !
51: CONST ORTHORHOMBIC_A20 : NP U% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## TETRAG_AD (Np–U)

- Id: `phase:np-u:ad-tetrag`; status `assigned`
- Structure: beta-Np · A_d · tP4 · P4/nmm (129); type `st:a-d-beta-np-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 458.9–896.5 K, x(U) 0–0.26653
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:ad-tetrag)

Names (3): _corpus: _corpus:phase:np-u:ad-tetrag  
_tdb: _tdb:NpU-10Kur.tdb:TETRAG_AD, tdb:NpU-18Xie.tdb:TETRAG_AD  


### TDB models of TETRAG_AD (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): TETRAG_AD, type code %, sha256 `f85b49b94decbbee…`

~~~~text
47: PHASE TETRAG_AD % 1 1 !
48: CONST TETRAG_AD : NP% U : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): TETRAG_AD, type code %, sha256 `1d2cc8e207135d92…`

~~~~text
45: PHASE TETRAG_AD % 1 1 !
46: CONST TETRAG_AD : NP% U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## BCC_A2 (Np–U)

- Id: `phase:np-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 856.06–2542.99 K, x(U) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:bcc-a2)

Names (3): _corpus: _corpus:phase:np-u:bcc-a2  
_tdb: _tdb:NpU-10Kur.tdb:BCC_A2, tdb:NpU-18Xie.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): BCC_A2, type code %B, sha256 `f85b49b94decbbee…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NP% U% : VA : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): BCC_A2, type code %B, sha256 `1d2cc8e207135d92…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NP% U% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## FCC_A1 (Np–U)

- Id: `phase:np-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:fcc-a1)

Names (3): _corpus: _corpus:phase:np-u:fcc-a1  
_tdb: _tdb:NpU-10Kur.tdb:FCC_A1, tdb:NpU-18Xie.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): FCC_A1, type code %A, sha256 `f85b49b94decbbee…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NP U : VA : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): FCC_A1, type code %A, sha256 `1d2cc8e207135d92…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NP U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## HCP_A3 (Np–U)

- Id: `phase:np-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:hcp-a3)

Names (3): _corpus: _corpus:phase:np-u:hcp-a3  
_tdb: _tdb:NpU-10Kur.tdb:HCP_A3, tdb:NpU-18Xie.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): HCP_A3, type code %A, sha256 `f85b49b94decbbee…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NP U : VA : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): HCP_A3, type code %A, sha256 `1d2cc8e207135d92…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NP U : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## LIQUID (Np–U)

- Id: `phase:np-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 917.28–4000 K, x(U) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:liquid)

Names (3): _corpus: _corpus:phase:np-u:liquid  
_tdb: _tdb:NpU-10Kur.tdb:LIQUID, tdb:NpU-18Xie.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): LIQUID, type code %, sha256 `f85b49b94decbbee…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NP U : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): LIQUID, type code %, sha256 `1d2cc8e207135d92…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NP U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## NPU_ZETA (Np–U)

- Id: `phase:np-u:npu-zeta`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): PuU-zeta · hR58 · R-3m (166) — Hallstedt 2025 mmc2 row for NPU_ZETA: NpU-zeta
- Candidate (tdb_comment): PuU-zeta · hR58 · R-3m — NpU-10Kur.tdb: 'Prototype PuU-zeta (hR58, R-3m)'
- Candidate (tdb_comment): PuU-zeta · hR58 · R-3m — NpU-18Xie.tdb: 'Prototype PuU-zeta (hR58, R-3m)'
- Stability: stable in 2 of 2 calculated diagram(s): 300–946.63 K, x(U) 0.23414–0.71951
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:npu-zeta)

Names (3): _corpus: _corpus:phase:np-u:npu-zeta  
_tdb: _tdb:NpU-10Kur.tdb:NPU_ZETA, tdb:NpU-18Xie.tdb:NPU_ZETA  


### TDB models of NPU_ZETA (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): NPU_ZETA, type code %, sha256 `f85b49b94decbbee…`

~~~~text
62: PHASE NPU_ZETA % 1 1 !
63: CONST NPU_ZETA : NP U : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): NPU_ZETA, type code %, sha256 `1d2cc8e207135d92…`

~~~~text
60: PHASE NPU_ZETA % 2 1 2 !
61: CONST NPU_ZETA : NP U : NP U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## ORTHO_AC (Np–U)

- Id: `phase:np-u:ortho-ac`; status `assigned`
- Structure: alpha-Np · A_c · oP8 · Pnma (62); type `st:a-c-alpha-np-op8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–555.02 K, x(U) 0–0.1032
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:ortho-ac)

Names (3): _corpus: _corpus:phase:np-u:ortho-ac  
_tdb: _tdb:NpU-10Kur.tdb:ORTHO_AC, tdb:NpU-18Xie.tdb:ORTHO_AC  


### TDB models of ORTHO_AC (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): ORTHO_AC, type code %, sha256 `f85b49b94decbbee…`

~~~~text
42: PHASE ORTHO_AC % 1 1 !
43: CONST ORTHO_AC : NP% U : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): ORTHO_AC, type code %, sha256 `1d2cc8e207135d92…`

~~~~text
40: PHASE ORTHO_AC % 1 1 !
41: CONST ORTHO_AC : NP% U : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
_assessment that models this phase_

## TETRAGONAL_U (Np–U)

- Id: `phase:np-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — NpU-10Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — NpU-18Xie.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 2 of 2 calculated diagram(s): 914.55–1048.82 K, x(U) 0.69334–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:np-u:u-tetragonal)

Names (3): _corpus: _corpus:phase:np-u:u-tetragonal  
_tdb: _tdb:NpU-10Kur.tdb:TETRAGONAL_U, tdb:NpU-18Xie.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (2): PHASE and CONSTITUENT statements as written

[NpU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-10Kur.tdb): TETRAGONAL_U, type code %, sha256 `f85b49b94decbbee…`

~~~~text
57: PHASE TETRAGONAL_U % 1 1 !
58: CONST TETRAGONAL_U : NP U% : !
~~~~

[NpU-18Xie.tdb](https://orchid-project.org/data/databases/sgte-binary/NpU-18Xie.tdb): TETRAGONAL_U, type code %, sha256 `1d2cc8e207135d92…`

~~~~text
55: PHASE TETRAGONAL_U % 1 1 !
56: CONST TETRAGONAL_U : NP U% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.commatsci.2017.11.042](https://doi.org/10.1016/j.commatsci.2017.11.042) Wei Xie, Dane Morgan, CALPHAD modeling and ab initio calculations of the Np-U-Zr system, Computational Materials Science 143, 505-514 (2018).  
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
