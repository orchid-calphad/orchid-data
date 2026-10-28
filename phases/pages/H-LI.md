# H–Li phases

> H–Li system: 6 phases (tier A 4, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-LI.html · Markdown: https://data.orchid-project.org/phases/pages/H-LI.md

6 phases (tier A 4, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-LI) · [full JSON](https://data.orchid-project.org/phases/systems/H-LI.json) · [Markdown](https://data.orchid-project.org/phases/pages/H-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Li system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-li-bcc-a2); _phase:h-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1908.6 K, x(H) 0–0 | 0 | 3 |
| [FCC_A1](#phase-h-li-fcc-a1); _phase:h-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [GAS](#phase-h-li-gas); _phase:h-li:gas_ | gas | gas | stable in 3 of 3 calculated diagram(s): 300–2500 K, x(H) 0–1 | 0 | 3 |
| [HCP_A3](#phase-h-li-hcp-a3); _phase:h-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIH_B1](#phase-h-li-lih-b1); _phase:h-li:lih-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–971.43 K, x(H) 0.5–0.5 | 0 | 3 |
| [LIQUID](#phase-h-li-liquid); _phase:h-li:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 452.67–1908.6 K, x(H) 0–0.50191 | 0 | 3 |

## BCC_A2 (H–Li)

- Id: `phase:h-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1908.6 K, x(H) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-li:bcc-a2)

Names (4): _corpus: _corpus:phase:h-li:bcc-a2  
_tdb: _tdb:LiH-12Wan.tdb:BCC_A2, tdb:LiH-17Lia.tdb:BCC_A2, tdb:LiH-93Pel.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[LiH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-12Wan.tdb): BCC_A2, type code %B, sha256 `40699b258c36f046…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : LI : VA : !
~~~~

[LiH-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-17Lia.tdb): BCC_A2, type code %B, sha256 `24d02f09548eb615…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : LI : H VA% : !
~~~~

[LiH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-93Pel.tdb): BCC_A2, type code %B, sha256 `4f4f06725deec911…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : LI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2017.02.024](https://doi.org/10.1016/j.intermet.2017.02.024) Song-Mao Liang, Franziska Taubert, Artem Kozlov, Jürgen Seidel, Florian Mertens, Rainer Schmid-Fetzer, Thermodynamics of Li-Si and Li-Si-H phase diagrams applied to hydrogen absorption and Li-ion batteries, Intermetallics 81, 32-46 (2017).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_

## FCC_A1 (H–Li)

- Id: `phase:h-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-li:fcc-a1)

Names (4): _corpus: _corpus:phase:h-li:fcc-a1  
_tdb: _tdb:LiH-12Wan.tdb:FCC_A1, tdb:LiH-17Lia.tdb:FCC_A1, tdb:LiH-93Pel.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[LiH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-12Wan.tdb): FCC_A1, type code %A, sha256 `40699b258c36f046…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : LI : VA : !
~~~~

[LiH-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-17Lia.tdb): FCC_A1, type code %A, sha256 `24d02f09548eb615…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : LI : VA : !
~~~~

[LiH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-93Pel.tdb): FCC_A1, type code %A, sha256 `4f4f06725deec911…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : LI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2017.02.024](https://doi.org/10.1016/j.intermet.2017.02.024) Song-Mao Liang, Franziska Taubert, Artem Kozlov, Jürgen Seidel, Florian Mertens, Rainer Schmid-Fetzer, Thermodynamics of Li-Si and Li-Si-H phase diagrams applied to hydrogen absorption and Li-ion batteries, Intermetallics 81, 32-46 (2017).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_

## GAS (H–Li)

- Id: `phase:h-li:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500 K, x(H) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-li:gas)

Names (4): _corpus: _corpus:phase:h-li:gas  
_tdb: _tdb:LiH-12Wan.tdb:GAS, tdb:LiH-17Lia.tdb:GAS, tdb:LiH-93Pel.tdb:GAS  


### TDB models of GAS (3): PHASE and CONSTITUENT statements as written

[LiH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-12Wan.tdb): GAS, type code %, sha256 `40699b258c36f046…`

~~~~text
53: PHASE GAS:G % 1 1 !
54: CONST GAS:G : H H2 LI LI2 LIH : !
~~~~

[LiH-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-17Lia.tdb): GAS, type code %, sha256 `24d02f09548eb615…`

~~~~text
55: PHASE GAS:G % 1 1 !
56: CONST GAS:G : H H2 LI LI2 LIH : !
~~~~

[LiH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-93Pel.tdb): GAS, type code %, sha256 `4f4f06725deec911…`

~~~~text
51: PHASE GAS:G % 1 1 !
52: CONST GAS:G : H H2 LI LI2 LIH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2017.02.024](https://doi.org/10.1016/j.intermet.2017.02.024) Song-Mao Liang, Franziska Taubert, Artem Kozlov, Jürgen Seidel, Florian Mertens, Rainer Schmid-Fetzer, Thermodynamics of Li-Si and Li-Si-H phase diagrams applied to hydrogen absorption and Li-ion batteries, Intermetallics 81, 32-46 (2017).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_

## HCP_A3 (H–Li)

- Id: `phase:h-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Li 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-li:hcp-a3)

Names (4): _corpus: _corpus:phase:h-li:hcp-a3  
_tdb: _tdb:LiH-12Wan.tdb:HCP_A3, tdb:LiH-17Lia.tdb:HCP_A3, tdb:LiH-93Pel.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[LiH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-12Wan.tdb): HCP_A3, type code %A, sha256 `40699b258c36f046…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : LI : VA : !
~~~~

[LiH-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-17Lia.tdb): HCP_A3, type code %A, sha256 `24d02f09548eb615…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : LI : VA : !
~~~~

[LiH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-93Pel.tdb): HCP_A3, type code %A, sha256 `4f4f06725deec911…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : LI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2017.02.024](https://doi.org/10.1016/j.intermet.2017.02.024) Song-Mao Liang, Franziska Taubert, Artem Kozlov, Jürgen Seidel, Florian Mertens, Rainer Schmid-Fetzer, Thermodynamics of Li-Si and Li-Si-H phase diagrams applied to hydrogen absorption and Li-ion batteries, Intermetallics 81, 32-46 (2017).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_

## LIH_B1 (H–Li)

- Id: `phase:h-li:lih-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaabjbr and oqmd-1103967, space group 225
- Stoichiometry: H 0.5000, Li 0.5000
- Stability: stable in 3 of 3 calculated diagram(s): 300–971.43 K, x(H) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-li:lih-b1)

Names (6): _corpus: _corpus:phase:h-li:lih-b1  
_mp: _mp:mp-aaaabjbr  
_oqmd: _oqmd:oqmd-1103967  
_tdb: _tdb:LiH-12Wan.tdb:LIH_B1, tdb:LiH-17Lia.tdb:LIH_B1, tdb:LiH-93Pel.tdb:LIH_B1  


### TDB models of LIH_B1 (3): PHASE and CONSTITUENT statements as written

[LiH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-12Wan.tdb): LIH_B1, type code %, sha256 `40699b258c36f046…`

~~~~text
50: PHASE LIH_B1 % 2 1 1 !
51: CONST LIH_B1 : LI : H : !
~~~~

[LiH-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-17Lia.tdb): LIH_B1, type code %, sha256 `24d02f09548eb615…`

~~~~text
52: PHASE LIH_B1 % 2 1 1 !
53: CONST LIH_B1 : LI : H : !
~~~~

[LiH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-93Pel.tdb): LIH_B1, type code %, sha256 `4f4f06725deec911…`

~~~~text
48: PHASE LIH_B1 % 2 1 1 !
49: CONST LIH_B1 : LI : H : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2017.02.024](https://doi.org/10.1016/j.intermet.2017.02.024) Song-Mao Liang, Franziska Taubert, Artem Kozlov, Jürgen Seidel, Florian Mertens, Rainer Schmid-Fetzer, Thermodynamics of Li-Si and Li-Si-H phase diagrams applied to hydrogen absorption and Li-ion batteries, Intermetallics 81, 32-46 (2017).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
_assessment that models this phase_

## LIQUID (H–Li)

- Id: `phase:h-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 452.67–1908.6 K, x(H) 0–0.50191
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-li:liquid)

Names (4): _corpus: _corpus:phase:h-li:liquid  
_tdb: _tdb:LiH-12Wan.tdb:LIQUID, tdb:LiH-17Lia.tdb:LIQUID, tdb:LiH-93Pel.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[LiH-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-12Wan.tdb): LIQUID, type code %, sha256 `40699b258c36f046…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : H LI LIH : !
~~~~

[LiH-17Lia.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-17Lia.tdb): LIQUID, type code %, sha256 `24d02f09548eb615…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : H LI LIH : !
~~~~

[LiH-93Pel.tdb](https://orchid-project.org/data/databases/sgte-binary/LiH-93Pel.tdb): LIQUID, type code %, sha256 `4f4f06725deec911…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : LI LIH : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-012-9997-z](https://doi.org/10.1007/s11669-012-9997-z) Man Wang, Weihua Sun, Chunsheng Sha, Biao Hu, Yong Du, Lixian Sun et al., Thermodynamic Modeling of the Li-H and Ca-H Systems, J. Phase Equilib. Diffus. 33, 89-96 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2017.02.024](https://doi.org/10.1016/j.intermet.2017.02.024) Song-Mao Liang, Franziska Taubert, Artem Kozlov, Jürgen Seidel, Florian Mertens, Rainer Schmid-Fetzer, Thermodynamics of Li-Si and Li-Si-H phase diagrams applied to hydrogen absorption and Li-ion batteries, Intermetallics 81, 32-46 (2017).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1993-841107](https://doi.org/10.1515/ijmr-1993-841107) A.D. Pelton, Z. Metallkd., 84, 767-72(1993).  
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
