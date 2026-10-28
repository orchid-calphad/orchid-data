# Ca–H phases

> Ca–H system: 7 phases (tier A 4, liquid 1, gas 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-H.html · Markdown: https://data.orchid-project.org/phases/pages/CA-H.md

7 phases (tier A 4, liquid 1, gas 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-H) · [full JSON](https://data.orchid-project.org/phases/systems/CA-H.json) · [Ca–H system page](https://data.orchid-project.org/systems/CA-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–H system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-h-bcc-a2); _phase:ca-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 688.01–1306.02 K, x(H) 0–0.3427 | 0 | 2 |
| [CAH2_BETA](#phase-ca-h-cah2-beta); _phase:ca-h:cah2-beta_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 1053.15–1257.01 K, x(H) 0.66667–0.66667 | 2 | 2 |
| [CAH2_C37](#phase-ca-h-cah2-c37); _phase:ca-h:cah2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1053.28 K, x(H) 0.66667–0.66667 | 9 | 2 |
| [FCC_A1](#phase-ca-h-fcc-a1); _phase:ca-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1306.02 K, x(H) 0–0.01797 | 0 | 2 |
| [GAS](#phase-ca-h-gas); _phase:ca-h:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1 | 0 | 2 |
| [HCP_A3](#phase-ca-h-hcp-a3); _phase:ca-h:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 624.48–878.76 K, x(H) 0.01318–0.16929 | 1 | 2 |
| [LIQUID](#phase-ca-h-liquid); _phase:ca-h:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1110–2111.52 K, x(H) 0–0.48736 | 0 | 2 |

## BCC_A2 (Ca–H)

- Id: `phase:ca-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 688.01–1306.02 K, x(H) 0–0.3427
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:bcc-a2)

Names (3): _corpus: _corpus:phase:ca-h:bcc-a2  
_tdb: _tdb:CaH-11Wan.tdb:BCC_A2, tdb:CaH-12Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): BCC_A2, type code %B, sha256 `10f2af8543f879ee…`

~~~~text
40: PHASE BCC_A2 %B 2 1 1.5 !
41: CONST BCC_A2 : CA : H VA% : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): BCC_A2, type code %B, sha256 `e8d5c286231e6b11…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CA : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase_

## CAH2_BETA (Ca–H)

- Id: `phase:ca-h:cah2-beta`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Pnma (62) — on-hull MP CaH2 at x(H)=0.6667
- Candidate (dft_oqmd): Pnma (62) — on-hull OQMD Ca1 H2 at x(H)=0.6667
- Candidate (sgte_mmc2): (CaH2-beta) · Fm-3m (225) — Hallstedt 2025 mmc2 row for CAH2_BETA: CaH2-beta (possibly CaF2 structure)
- Stoichiometry: Ca 0.3333, H 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 1053.15–1257.01 K, x(H) 0.66667–0.66667
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:cah2-beta)

Names (4): _corpus: _corpus:phase:ca-h:cah2-beta  
_paper: _paper:10.1016/j.ijhydene.2011.08.018:βCaH2  
_tdb: _tdb:CaH-11Wan.tdb:CAH2_BETA, tdb:CaH-12Wan.tdb:CAH2_BETA  


### TDB models of CAH2_BETA (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): CAH2_BETA, type code %, sha256 `10f2af8543f879ee…`

~~~~text
55: PHASE CAH2_BETA % 2 1 2 !
56: CONST CAH2_BETA : CA : H : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): CAH2_BETA, type code %, sha256 `e8d5c286231e6b11…`

~~~~text
52: PHASE CAH2_BETA % 2 1 2 !
53: CONST CAH2_BETA : CA : H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_

## CAH2_C37 (Ca–H)

- Id: `phase:ca-h:cah2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 0.3333, H 0.6667
- Stability: stable in 2 of 2 calculated diagram(s): 300–1053.28 K, x(H) 0.66667–0.66667
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:cah2-c37)

Names (4): _corpus: _corpus:phase:ca-h:cah2-c37  
_paper: _paper:10.1016/j.ijhydene.2011.08.018:αCaH2  
_tdb: _tdb:CaH-11Wan.tdb:CAH2_C37, tdb:CaH-12Wan.tdb:CAH2_C37  


### TDB models of CAH2_C37 (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): CAH2_C37, type code %, sha256 `10f2af8543f879ee…`

~~~~text
50: PHASE CAH2_C37 % 2 1 2 !
51: CONST CAH2_C37 : CA : H : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): CAH2_C37, type code %, sha256 `e8d5c286231e6b11…`

~~~~text
47: PHASE CAH2_C37 % 2 1 2 !
48: CONST CAH2_C37 : CA : H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_

## FCC_A1 (Ca–H)

- Id: `phase:ca-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1306.02 K, x(H) 0–0.01797
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:fcc-a1)

Names (3): _corpus: _corpus:phase:ca-h:fcc-a1  
_tdb: _tdb:CaH-11Wan.tdb:FCC_A1, tdb:CaH-12Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): FCC_A1, type code %A, sha256 `10f2af8543f879ee…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CA% : H VA% : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): FCC_A1, type code %A, sha256 `e8d5c286231e6b11…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CA% : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase_

## GAS (Ca–H)

- Id: `phase:ca-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:gas)

Names (3): _corpus: _corpus:phase:ca-h:gas  
_tdb: _tdb:CaH-11Wan.tdb:GAS, tdb:CaH-12Wan.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): GAS, type code %, sha256 `10f2af8543f879ee…`

~~~~text
58: PHASE GAS:G % 1 1 !
59: CONST GAS:G : CA CA2 CAH H H2 : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): GAS, type code %, sha256 `e8d5c286231e6b11…`

~~~~text
55: PHASE GAS:G % 1 1 !
56: CONST GAS:G : CA CA2 CAH H H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase_

## HCP_A3 (Ca–H)

- Id: `phase:ca-h:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 624.48–878.76 K, x(H) 0.01318–0.16929
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:hcp-a3)

Names (4): _corpus: _corpus:phase:ca-h:hcp-a3  
_paper: _paper:10.1016/j.ijhydene.2011.08.018:CaH  
_tdb: _tdb:CaH-11Wan.tdb:HCP_A3, tdb:CaH-12Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): HCP_A3, type code %A, sha256 `10f2af8543f879ee…`

~~~~text
45: PHASE HCP_A3 %A 1 1 !
46: CONST HCP_A3 : CA CAH2 : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): HCP_A3, type code %A, sha256 `e8d5c286231e6b11…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CA : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_

## LIQUID (Ca–H)

- Id: `phase:ca-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1110–2111.52 K, x(H) 0–0.48736
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-h:liquid)

Names (3): _corpus: _corpus:phase:ca-h:liquid  
_tdb: _tdb:CaH-11Wan.tdb:LIQUID, tdb:CaH-12Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CaH-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-11Wan.tdb): LIQUID, type code %, sha256 `10f2af8543f879ee…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CA CAH2 H : !
~~~~

[CaH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/CaH-12Wan.tdb): LIQUID, type code %, sha256 `e8d5c286231e6b11…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CA H : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.ijhydene.2011.08.018](https://doi.org/10.1016/j.ijhydene.2011.08.018) Kun Wang, Junlin Du, Xiangcheng Kong, Xiaoqin Zeng, Jianxin Zou, Zhilin Li et al., Ab initio and thermodynamic investigation on the Ca–H system, International Journal of Hydrogen Energy 36, 13632-13639 (2011).  
_assessment that models this phase_

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
