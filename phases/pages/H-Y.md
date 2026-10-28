# H–Y phases

> H–Y system: 6 phases (tier A 1, liquid 1, gas 2, needs_review 1, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-Y.html · Markdown: https://data.orchid-project.org/phases/pages/H-Y.md

6 phases (tier A 1, liquid 1, gas 2, needs_review 1, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-Y) · [full JSON](https://data.orchid-project.org/phases/systems/H-Y.json) · [H–Y system page](https://data.orchid-project.org/systems/H-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Y system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-y-bcc-a2); _phase:h-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 397.65–1795.28 K, x(H) 0–6e-05 | 0 | 2 |
| [FCC_A1](#phase-h-y-fcc-a1); _phase:h-y:fcc-a1_ | CaF2 · C1 · cF12 · Fm-3m (225) | assigned | stable in 2 of 2 calculated diagram(s): 300–1721.6 K, x(H) 0.47001–0.67677 | 10 | 2 |
| [GAS](#phase-h-y-gas); _phase:h-y:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300.62–2500 K, x(H) 0.99795–1 | 8 | 2 |
| [H2GAS](#phase-h-y-h2gas); _phase:h-y:h2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1092.08 K, x(H) 1–1 | 2 | 2 |
| [HCP_A3](#phase-h-y-hcp-a3); _phase:h-y:hcp-a3_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–2303.37 K, x(H) 0–0.74997 | 12 | 2 |
| [LIQUID](#phase-h-y-liquid); _phase:h-y:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 397.65–2500 K, x(H) 0–0 | 0 | 2 |

## BCC_A2 (H–Y)

- Id: `phase:h-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 397.65–1795.28 K, x(H) 0–6e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-y:bcc-a2)

Names (3): _corpus: _corpus:phase:h-y:bcc-a2  
_tdb: _tdb:YH-18Fu.tdb:BCC_A2, tdb:YH-20Pen.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[YH-18Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb): BCC_A2, type code %B, sha256 `32726376eb96be71…`

~~~~text
41: PHASE BCC_A2 %B 2 1 1 !
42: CONST BCC_A2 : Y : H VA% : !
~~~~

[YH-20Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb): BCC_A2, type code %B, sha256 `d8a7b7aea58fca94…`

~~~~text
38: PHASE BCC_A2 %B 2 1 1 !
39: CONST BCC_A2 : Y : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) Jiaqing Peng, Ming Wu, Fu Du, Fengli Yang, Jianyun Shen, Lijun Wang et al., Thermodynamic modelling of Y–H and Y–Zr–H system aided by first-principles and its application in bulk hydride moderator fabrication, Journal of Nuclear Materials 531, 152035 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) Kai Fu, Xiaojing Jiang, Yanru Guo, Shuan Li, Jie Zheng, Wenhuai Tian et al., Experimental investigation and thermodynamic assessment of the yttrium-hydrogen binary system, Progress in Natural Science: Materials International 28, 332-336 (2018).  
_assessment that models this phase_

## FCC_A1 (H–Y)

- Id: `phase:h-y:fcc-a1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1721.6 K, x(H) 0.47001–0.67677
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-y:fcc-a1)

Names (4): _corpus: _corpus:phase:h-y:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2020.152035:fcc  
_tdb: _tdb:YH-18Fu.tdb:FCC_A1, tdb:YH-20Pen.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[YH-18Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb): FCC_A1, type code %A, sha256 `32726376eb96be71…`

~~~~text
36: PHASE FCC_A1 %A 3 1 1 2 !
37: CONST FCC_A1 : Y : H VA% : H% VA : !
~~~~

[YH-20Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb): FCC_A1, type code %A, sha256 `d8a7b7aea58fca94…`

~~~~text
33: PHASE FCC_A1 %A 3 1 1 2 !
34: CONST FCC_A1 : Y : H VA% : H% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) Jiaqing Peng, Ming Wu, Fu Du, Fengli Yang, Jianyun Shen, Lijun Wang et al., Thermodynamic modelling of Y–H and Y–Zr–H system aided by first-principles and its application in bulk hydride moderator fabrication, Journal of Nuclear Materials 531, 152035 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) Kai Fu, Xiaojing Jiang, Yanru Guo, Shuan Li, Jie Zheng, Wenhuai Tian et al., Experimental investigation and thermodynamic assessment of the yttrium-hydrogen binary system, Progress in Natural Science: Materials International 28, 332-336 (2018).  
_assessment that models this phase_

## GAS (H–Y)

- Id: `phase:h-y:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.62–2500 K, x(H) 0.99795–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-y:gas)

Names (4): _corpus: _corpus:phase:h-y:gas  
_paper: _paper:10.1016/j.jnucmat.2020.152035:GAS(H2)  
_tdb: _tdb:YH-18Fu.tdb:GAS, tdb:YH-20Pen.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[YH-18Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb): GAS, type code %, sha256 `32726376eb96be71…`

~~~~text
49: PHASE GAS:G % 1 1 !
50: CONST GAS:G : H H2 Y : !
~~~~

[YH-20Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb): GAS, type code %, sha256 `d8a7b7aea58fca94…`

~~~~text
46: PHASE GAS:G % 1 1 !
47: CONST GAS:G : H H2 Y : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) Jiaqing Peng, Ming Wu, Fu Du, Fengli Yang, Jianyun Shen, Lijun Wang et al., Thermodynamic modelling of Y–H and Y–Zr–H system aided by first-principles and its application in bulk hydride moderator fabrication, Journal of Nuclear Materials 531, 152035 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) Kai Fu, Xiaojing Jiang, Yanru Guo, Shuan Li, Jie Zheng, Wenhuai Tian et al., Experimental investigation and thermodynamic assessment of the yttrium-hydrogen binary system, Progress in Natural Science: Materials International 28, 332-336 (2018).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1021/j100892a004](https://doi.org/10.1021/j100892a004) L. N. Yannopoulos, R. K. Edwards, P. G. Wahlbeck, The Thermodynamics of the Yttrium-Hydrogen System\<sup>1\</sup>, J. Phys. Chem. 69, 2510-2515 (1965).  
_cited as the source of values for this phase_
- [doi:10.1149/1.2425565](https://doi.org/10.1149/1.2425565) C. E. Lundin, J. P. Blackledge, Pressure-Temperature-Composition Relationships of the Yttrium-Hydrogen System, J. Electrochem. Soc. 109, 838 (1962).  
_cited as the source of values for this phase_

## H2GAS (H–Y)

- Id: `phase:h-y:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1092.08 K, x(H) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-y:h2gas)

Names (4): _corpus: _corpus:phase:h-y:h2gas  
_paper: _paper:10.1016/j.pnsc.2018.04.001:Gas(H2)  
_tdb: _tdb:YH-18Fu.tdb:H2GAS, tdb:YH-20Pen.tdb:H2GAS  


### TDB models of H2GAS (2): PHASE and CONSTITUENT statements as written

[YH-18Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb): H2GAS, type code %, sha256 `32726376eb96be71…`

~~~~text
52: PHASE H2GAS % 1 1 !
53: CONST H2GAS : H2 : !
~~~~

[YH-20Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb): H2GAS, type code %, sha256 `d8a7b7aea58fca94…`

~~~~text
49: PHASE H2GAS % 1 1 !
50: CONST H2GAS : H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) Kai Fu, Xiaojing Jiang, Yanru Guo, Shuan Li, Jie Zheng, Wenhuai Tian et al., Experimental investigation and thermodynamic assessment of the yttrium-hydrogen binary system, Progress in Natural Science: Materials International 28, 332-336 (2018).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) Jiaqing Peng, Ming Wu, Fu Du, Fengli Yang, Jianyun Shen, Lijun Wang et al., Thermodynamic modelling of Y–H and Y–Zr–H system aided by first-principles and its application in bulk hydride moderator fabrication, Journal of Nuclear Materials 531, 152035 (2020).  
_assessment that models this phase_

## HCP_A3 (H–Y)

- Id: `phase:h-y:hcp-a3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:HCP_A3
- Candidate (literature_printed): HoH3 · hP24 — printed with a label mapped to this phase
- Candidate (name_token): Mg · A3 · hP2 · P6_3/mmc (194) — Strukturbericht/word 'A3' in the TDB name
- Candidate (sgte_mmc2): HoH3 · hP24 · P-3c1 (165) — Hallstedt 2025 mmc2 row for HCP_A3: DyH3, ErH3, GdH3, YH3
- Stability: stable in 2 of 2 calculated diagram(s): 300–2303.37 K, x(H) 0–0.74997
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-y:hcp-a3)

Names (6): _corpus: _corpus:phase:h-y:hcp-a3  
_paper: _paper:10.1016/j.jnucmat.2020.152035:HCP(Y), paper:10.1016/j.jnucmat.2020.152035:hcp, paper:10.1016/j.pnsc.2018.04.001:α-Y  
_tdb: _tdb:YH-18Fu.tdb:HCP_A3, tdb:YH-20Pen.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[YH-18Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb): HCP_A3, type code %A, sha256 `32726376eb96be71…`

~~~~text
46: PHASE HCP_A3 %A 3 1 1 2 !
47: CONST HCP_A3 : Y : H VA% : H VA% : !
~~~~

[YH-20Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb): HCP_A3, type code %A, sha256 `d8a7b7aea58fca94…`

~~~~text
43: PHASE HCP_A3 %A 3 1 1 2 !
44: CONST HCP_A3 : Y : H VA% : H VA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) Jiaqing Peng, Ming Wu, Fu Du, Fengli Yang, Jianyun Shen, Lijun Wang et al., Thermodynamic modelling of Y–H and Y–Zr–H system aided by first-principles and its application in bulk hydride moderator fabrication, Journal of Nuclear Materials 531, 152035 (2020).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) Kai Fu, Xiaojing Jiang, Yanru Guo, Shuan Li, Jie Zheng, Wenhuai Tian et al., Experimental investigation and thermodynamic assessment of the yttrium-hydrogen binary system, Progress in Natural Science: Materials International 28, 332-336 (2018).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1149/1.2425565](https://doi.org/10.1149/1.2425565) C. E. Lundin, J. P. Blackledge, Pressure-Temperature-Composition Relationships of the Yttrium-Hydrogen System, J. Electrochem. Soc. 109, 838 (1962).  
_cited as the source of values for this phase_

## LIQUID (H–Y)

- Id: `phase:h-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stoichiometry: Y 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 397.65–2500 K, x(H) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-y:liquid)

Names (3): _corpus: _corpus:phase:h-y:liquid  
_tdb: _tdb:YH-18Fu.tdb:LIQUID, tdb:YH-20Pen.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[YH-18Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-18Fu.tdb): LIQUID, type code %, sha256 `32726376eb96be71…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : Y : !
~~~~

[YH-20Pen.tdb](https://orchid-project.org/data/databases/sgte-binary/YH-20Pen.tdb): LIQUID, type code %, sha256 `d8a7b7aea58fca94…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2020.152035](https://doi.org/10.1016/j.jnucmat.2020.152035) Jiaqing Peng, Ming Wu, Fu Du, Fengli Yang, Jianyun Shen, Lijun Wang et al., Thermodynamic modelling of Y–H and Y–Zr–H system aided by first-principles and its application in bulk hydride moderator fabrication, Journal of Nuclear Materials 531, 152035 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.pnsc.2018.04.001](https://doi.org/10.1016/j.pnsc.2018.04.001) Kai Fu, Xiaojing Jiang, Yanru Guo, Shuan Li, Jie Zheng, Wenhuai Tian et al., Experimental investigation and thermodynamic assessment of the yttrium-hydrogen binary system, Progress in Natural Science: Materials International 28, 332-336 (2018).  
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
