# Se–Sn phases

> Se–Sn system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SE-SN.html · Markdown: https://data.orchid-project.org/phases/pages/SE-SN.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SE-SN) · [full JSON](https://data.orchid-project.org/phases/systems/SE-SN.json) · [Se–Sn system page](https://data.orchid-project.org/systems/SE-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SE-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Se–Sn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-se-sn-a4-diamond); _phase:se-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-se-sn-a5-bct); _phase:se-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505.06 K, x(Se) 0–0 | 17 | 1 |
| [HEXAGONAL_A8](#phase-se-sn-a8-hexagonal); _phase:se-sn:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–493.92 K, x(Se) 1–1 | 10 | 1 |
| [LIQUID](#phase-se-sn-liquid); _phase:se-sn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 493.92–2500 K, x(Se) 0–1 | 68 | 1 |
| [SNSE_B16](#phase-se-sn-snse-b16); _phase:se-sn:snse-b16_ | GeS · B16 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–796.51 K, x(Se) 0.5–0.5 | 45 | 1 |
| [SNSE_B33](#phase-se-sn-snse-b33); _phase:se-sn:snse-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 796.51–1146.92 K, x(Se) 0.5–0.5 | 27 | 1 |
| [SNSE2_C6](#phase-se-sn-snse2-c6); _phase:se-sn:snse2-c6_ | CdI2 · C6 · hP3 · P-3m1 (164) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–920.37 K, x(Se) 0.66667–0.66667 | 44 | 1 |

## DIAMOND_A4 (Se–Sn)

- Id: `phase:se-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:a4-diamond)

Names (2): _corpus: _corpus:phase:se-sn:a4-diamond  
_tdb: _tdb:SnSe-96Feu-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): DIAMOND_A4, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
30: PHASE DIAMOND_A4 % 1 1 !
31: CONST DIAMOND_A4 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase_

## BCT_A5 (Se–Sn)

- Id: `phase:se-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–505.06 K, x(Se) 0–0
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:a5-bct)

Names (4): _corpus: _corpus:phase:se-sn:a5-bct, corpus:phase:se-sn:bct-a5  
_paper: _paper:10.1007/bf02648368:βSn  
_tdb: _tdb:SnSe-96Feu-LB.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): BCT_A5, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
35: PHASE BCT_A5 % 1 1 !
36: CONST BCT_A5 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase; reports values for this phase_

## HEXAGONAL_A8 (Se–Sn)

- Id: `phase:se-sn:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Se 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–493.92 K, x(Se) 1–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:a8-hexagonal)

Names (4): _corpus: _corpus:phase:se-sn:a8-hexagonal, corpus:phase:se-sn:hexagonal-a8  
_paper: _paper:10.1007/bf02648368:Se  
_tdb: _tdb:SnSe-96Feu-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): HEXAGONAL_A8, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
40: PHASE HEXAGONAL_A8 % 1 1 !
41: CONST HEXAGONAL_A8 : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Se–Sn)

- Id: `phase:se-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 493.92–2500 K, x(Se) 0–1
- Literature: 68 values (68 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:liquid)

Names (5): _corpus: _corpus:phase:se-sn:liquid  
_paper: _paper:10.1007/bf02648368:L1, paper:10.1007/bf02648368:L2, paper:10.1007/bf02648368:liquid  
_tdb: _tdb:SnSe-96Feu-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): LIQUID, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : SE SN SNSE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/matertrans1989.35.118](https://doi.org/10.2320/matertrans1989.35.118) Katsunori Yamaguchi, Kazuo Kameda, Yoichi Takeda, Kimio Itagaki, Measurements of High Temperature Heat Content of the II&amp;ndash;VI and IV&amp;ndash;VI (II: Zn, Cd IV: Sn, Pb VI: Se, Te) Compounds, Mater. Trans., JIM 35, 118-124 (1994).  
_cited as the source of values for this phase_

## SNSE_B16 (Se–Sn)

- Id: `phase:se-sn:snse-b16`; status `assigned`
- Structure: GeS · B16 · oP8 · Pnma (62); type `st:b16-ges-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Se 0.5000, Sn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–796.51 K, x(Se) 0.5–0.5
- Literature: 45 values (45 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:snse-b16)

Names (3): _corpus: _corpus:phase:se-sn:snse-b16  
_paper: _paper:10.1007/bf02648368:αSnSe  
_tdb: _tdb:SnSe-96Feu-LB.tdb:SNSE_B16  


### TDB models of SNSE_B16 (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): SNSE_B16, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
45: PHASE SNSE_B16 % 2 1 1 !
46: CONST SNSE_B16 : SN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase; reports values for this phase_

## SNSE_B33 (Se–Sn)

- Id: `phase:se-sn:snse-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Se 0.5000, Sn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 796.51–1146.92 K, x(Se) 0.5–0.5
- Literature: 27 values (27 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:snse-b33)

Names (3): _corpus: _corpus:phase:se-sn:snse-b33  
_paper: _paper:10.1007/bf02648368:βSnSe  
_tdb: _tdb:SnSe-96Feu-LB.tdb:SNSE_B33  


### TDB models of SNSE_B33 (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): SNSE_B33, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
50: PHASE SNSE_B33 % 2 1 1 !
51: CONST SNSE_B33 : SN : SE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase; reports values for this phase_

## SNSE2_C6 (Se–Sn)

- Id: `phase:se-sn:snse2-c6`; status `assigned`
- Structure: CdI2 · C6 · hP3 · P-3m1 (164); type `st:c6-cdi2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaazp and oqmd-8151, space group 164
- Stoichiometry: Se 0.6667, Sn 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–920.37 K, x(Se) 0.66667–0.66667
- Literature: 44 values (44 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:se-sn:snse2-c6)

Names (5): _corpus: _corpus:phase:se-sn:snse2-c6  
_mp: _mp:mp-aaaaaazp  
_oqmd: _oqmd:oqmd-8151  
_paper: _paper:10.1007/bf02648368:SnSe2  
_tdb: _tdb:SnSe-96Feu-LB.tdb:SNSE2_C6  


### TDB models of SNSE2_C6 (1): PHASE and CONSTITUENT statements as written

[SnSe-96Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SnSe-96Feu-LB.tdb): SNSE2_C6, type code %, sha256 `1a2bab98ceb7b79f…`

~~~~text
55: PHASE SNSE2_C6 % 2 1 2 !
56: CONST SNSE2_C6 : SN : SE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02648368](https://doi.org/10.1007/BF02648368) Y. Feutelais, M. Majid, B. Legendre, S.G. Fries, J. Phase Equilib., 17, 40-49(1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(92)87043-a](https://doi.org/10.1016/0040-6031%2892%2987043-a) Steve Boone, O.J. Kleppa, Enthalpies of formation for Group IV selenides (GeSe2, GeSe2(am), SnSe, SnSe2, PbSe) by direct-combination drop calorimetry, Thermochimica Acta 197, 109-121 (1992).  
_cited as the source of values for this phase_

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
