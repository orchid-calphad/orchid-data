# Cu–Eu phases

> Cu–Eu system: 8 phases (tier A 5, tier C 2, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-EU.html · Markdown: https://data.orchid-project.org/phases/pages/CU-EU.md

8 phases (tier A 5, tier C 2, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-EU) · [full JSON](https://data.orchid-project.org/phases/systems/CU-EU.json) · [Cu–Eu system page](https://data.orchid-project.org/systems/CU-EU.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-EU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Eu system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-eu-bcc-a2); _phase:cu-eu:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Eu) 0.99932–1 | 2 | 1 |
| [CU2EU](#phase-cu-eu-cu2eu); _phase:cu-eu:cu2eu_ | Hg2K · oI12 · Imma (74) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–865.88 K, x(Eu) 0.33333–0.33333 | 4 | 1 |
| [CU5EU_D2D](#phase-cu-eu-cu5eu-d2d); _phase:cu-eu:cu5eu-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1114.73 K, x(Eu) 0.16667–0.16667 | 6 | 1 |
| [CUEU_B27](#phase-cu-eu-cueu-b27); _phase:cu-eu:cueu-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–801.33 K, x(Eu) 0.5–0.5 | 4 | 1 |
| [CUEU2](#phase-cu-eu-cueu2); _phase:cu-eu:cueu2_ | Ca2Cu · oP12 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–727.82 K, x(Eu) 0.66667–0.66667 | 4 | 1 |
| [FCC_A1](#phase-cu-eu-fcc-a1); _phase:cu-eu:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1407.52 K, x(Eu) 0–0 | 2 | 1 |
| [HCP_A3](#phase-cu-eu-hcp-a3); _phase:cu-eu:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-eu-liquid); _phase:cu-eu:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 724.22–2500 K, x(Eu) 0–1 | 12 | 1 |

## BCC_A2 (Cu–Eu)

- Id: `phase:cu-eu:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Eu) 0.99932–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:bcc-a2)

Names (3): _corpus: _corpus:phase:cu-eu:bcc-a2  
_paper: _paper:10.1016/j.calphad.2006.11.003:BCC(Eu)  
_tdb: _tdb:CuEu-07Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): BCC_A2, type code %B, sha256 `4a0bb1c43d7e14de…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CU EU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## CU2EU (Cu–Eu)

- Id: `phase:cu-eu:cu2eu`; status `assigned`
- Structure: Hg2K · oI12 · Imma (74); type `st:hg2k-oi12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_74_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.6667, Eu 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–865.88 K, x(Eu) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:cu2eu)

Names (3): _corpus: _corpus:phase:cu-eu:cu2eu  
_paper: _paper:10.1016/j.calphad.2006.11.003:Cu2Eu  
_tdb: _tdb:CuEu-07Zha.tdb:CU2EU  


### TDB models of CU2EU (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): CU2EU, type code %, sha256 `4a0bb1c43d7e14de…`

~~~~text
55: PHASE CU2EU % 2 2 1 !
56: CONST CU2EU : CU : EU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## CU5EU_D2D (Cu–Eu)

- Id: `phase:cu-eu:cu5eu-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadbm and oqmd-18820, space group 191
- Stoichiometry: Cu 0.8333, Eu 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1114.73 K, x(Eu) 0.16667–0.16667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:cu5eu-d2d)

Names (5): _corpus: _corpus:phase:cu-eu:cu5eu-d2d  
_mp: _mp:mp-aaaaadbm  
_oqmd: _oqmd:oqmd-18820  
_paper: _paper:10.1016/j.calphad.2006.11.003:Cu5Eu  
_tdb: _tdb:CuEu-07Zha.tdb:CU5EU_D2D  


### TDB models of CU5EU_D2D (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): CU5EU_D2D, type code %, sha256 `4a0bb1c43d7e14de…`

~~~~text
50: PHASE CU5EU_D2D % 2 5 1 !
51: CONST CU5EU_D2D : CU : EU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## CUEU_B27 (Cu–Eu)

- Id: `phase:cu-eu:cueu-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacjwut and oqmd-29636, space group 62
- Stoichiometry: Cu 0.5000, Eu 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–801.33 K, x(Eu) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:cueu-b27)

Names (5): _corpus: _corpus:phase:cu-eu:cueu-b27  
_mp: _mp:mp-aaacjwut  
_oqmd: _oqmd:oqmd-29636  
_paper: _paper:10.1016/j.calphad.2006.11.003:CuEu  
_tdb: _tdb:CuEu-07Zha.tdb:CUEU_B27  


### TDB models of CUEU_B27 (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): CUEU_B27, type code %, sha256 `4a0bb1c43d7e14de…`

~~~~text
60: PHASE CUEU_B27 % 2 1 1 !
61: CONST CUEU_B27 : CU : EU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## CUEU2 (Cu–Eu)

- Id: `phase:cu-eu:cueu2`; status `assigned`
- Structure: Ca2Cu · oP12 · Pnma (62); type `st:ca2cu-op12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_6_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cu 0.3333, Eu 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–727.82 K, x(Eu) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:cueu2)

Names (3): _corpus: _corpus:phase:cu-eu:cueu2  
_paper: _paper:10.1016/j.calphad.2006.11.003:CuEu2  
_tdb: _tdb:CuEu-07Zha.tdb:CUEU2  


### TDB models of CUEU2 (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): CUEU2, type code %, sha256 `4a0bb1c43d7e14de…`

~~~~text
65: PHASE CUEU2 % 2 1 2 !
66: CONST CUEU2 : CU : EU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Eu)

- Id: `phase:cu-eu:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1407.52 K, x(Eu) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-eu:fcc-a1  
_paper: _paper:10.1016/j.calphad.2006.11.003:FCC(Cu)  
_tdb: _tdb:CuEu-07Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): FCC_A1, type code %A, sha256 `4a0bb1c43d7e14de…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CU% EU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## HCP_A3 (Cu–Eu)

- Id: `phase:cu-eu:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cu 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-eu:hcp-a3  
_tdb: _tdb:CuEu-07Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): HCP_A3, type code %A, sha256 `4a0bb1c43d7e14de…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CU : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase_

## LIQUID (Cu–Eu)

- Id: `phase:cu-eu:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 724.22–2500 K, x(Eu) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-eu:liquid)

Names (3): _corpus: _corpus:phase:cu-eu:liquid  
_paper: _paper:10.1016/j.calphad.2006.11.003:L  
_tdb: _tdb:CuEu-07Zha.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuEu-07Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CuEu-07Zha.tdb): LIQUID, type code %, sha256 `4a0bb1c43d7e14de…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CU EU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.11.003](https://doi.org/10.1016/j.calphad.2006.11.003) L.G. Zhang, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of Cu–Eu and Cu–Yb system, Calphad 31, 264-268 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(85)90378-9](https://doi.org/10.1016/0022-5088%2885%2990378-9) G.A. Costa, E.A. Franceschi, A. Tawansi, Phase equilibria in the EuCu system, Journal of the Less Common Metals 106, 175-182 (1985).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
