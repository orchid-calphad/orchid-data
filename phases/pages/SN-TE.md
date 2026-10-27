# Sn–Te phases

> Sn–Te system: 8 phases (tier A 7, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SN-TE.html · Markdown: https://data.orchid-project.org/phases/pages/SN-TE.md

8 phases (tier A 7, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SN-TE) · [full JSON](https://data.orchid-project.org/phases/systems/SN-TE.json) · [Sn–Te system page](https://data.orchid-project.org/systems/SN-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/SN-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sn–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sn-te-a4-diamond); _phase:sn-te:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-sn-te-a5-bct); _phase:sn-te:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505 K, x(Te) 0–0 | 1 | 1 |
| [HEXAGONAL_A8](#phase-sn-te-a8-hexagonal); _phase:sn-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 6 | 1 |
| [BCC_A2](#phase-sn-te-bcc-a2); _phase:sn-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-sn-te-fcc-a1); _phase:sn-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-sn-te-hcp-a3); _phase:sn-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-sn-te-liquid); _phase:sn-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 505–2500 K, x(Te) 0–1 | 14 | 1 |
| [SNTE_B1](#phase-sn-te-snte-b1); _phase:sn-te:snte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1078.89 K, x(Te) 0.5–0.51053 | 18 | 1 |

## DIAMOND_A4 (Sn–Te)

- Id: `phase:sn-te:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:a4-diamond)

Names (2): _corpus: _corpus:phase:sn-te:a4-diamond  
_tdb: _tdb:SnTe-10Liu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): DIAMOND_A4, type code %, sha256 `0fe58ce9ad47e379…`

~~~~text
44: PHASE DIAMOND_A4 % 1 1 !
45: CONST DIAMOND_A4 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase_

## BCT_A5 (Sn–Te)

- Id: `phase:sn-te:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–505 K, x(Te) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:a5-bct)

Names (4): _corpus: _corpus:phase:sn-te:a5-bct, corpus:phase:sn-te:bct-a5  
_paper: _paper:10.1007/s11664-009-0985-y:bct  
_tdb: _tdb:SnTe-10Liu.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): BCT_A5, type code %, sha256 `0fe58ce9ad47e379…`

~~~~text
49: PHASE BCT_A5 % 1 1 !
50: CONST BCT_A5 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase; reports values for this phase_

## HEXAGONAL_A8 (Sn–Te)

- Id: `phase:sn-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:sn-te:a8-hexagonal, corpus:phase:sn-te:hexagonal-a8  
_paper: _paper:10.1007/s11664-009-0985-y:hex  
_tdb: _tdb:SnTe-10Liu.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): HEXAGONAL_A8, type code %, sha256 `0fe58ce9ad47e379…`

~~~~text
54: PHASE HEXAGONAL_A8 % 1 1 !
55: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19090640117](https://doi.org/10.1002/zaac.19090640117) Wilhelm Biltz, Werner Mecklenburg, Über die Zustandsdiagramme von Zinn mit Schwefel, Selen und Tellur, Z. Anorg. Chem. 64, 226-235 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654315](https://doi.org/10.1007/bf02654315) J. Rakotomavo, M. -C. Baron, C. Petot, Thermodynamic properties of liquid tin-tellurium alloys at high temperature, Metall Trans B 12, 461-467 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90280-5](https://doi.org/10.1016/0022-5088%2880%2990280-5) S. Kurosawa, Y. Nakamura, M. Shimoji, The electrical conductivity and the phase diagram of the molten tin-tellurium system, Journal of the Less Common Metals 70, 119-121 (1980).  
_cited as the source of values for this phase_

## BCC_A2 (Sn–Te)

- Id: `phase:sn-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:bcc-a2)

Names (2): _corpus: _corpus:phase:sn-te:bcc-a2  
_tdb: _tdb:SnTe-10Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): BCC_A2, type code %B, sha256 `0fe58ce9ad47e379…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase_

## FCC_A1 (Sn–Te)

- Id: `phase:sn-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:fcc-a1)

Names (2): _corpus: _corpus:phase:sn-te:fcc-a1  
_tdb: _tdb:SnTe-10Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): FCC_A1, type code %A, sha256 `0fe58ce9ad47e379…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase_

## HCP_A3 (Sn–Te)

- Id: `phase:sn-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:hcp-a3)

Names (2): _corpus: _corpus:phase:sn-te:hcp-a3  
_tdb: _tdb:SnTe-10Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): HCP_A3, type code %A, sha256 `0fe58ce9ad47e379…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : SN : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase_

## LIQUID (Sn–Te)

- Id: `phase:sn-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 505–2500 K, x(Te) 0–1
- Literature: 14 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:liquid)

Names (3): _corpus: _corpus:phase:sn-te:liquid  
_paper: _paper:10.1007/s11664-009-0985-y:L  
_tdb: _tdb:SnTe-10Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): LIQUID, type code %, sha256 `0fe58ce9ad47e379…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : SN SNTE TE : !
~~~~

Example references (7 of 7; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19090640117](https://doi.org/10.1002/zaac.19090640117) Wilhelm Biltz, Werner Mecklenburg, Über die Zustandsdiagramme von Zinn mit Schwefel, Selen und Tellur, Z. Anorg. Chem. 64, 226-235 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654315](https://doi.org/10.1007/bf02654315) J. Rakotomavo, M. -C. Baron, C. Petot, Thermodynamic properties of liquid tin-tellurium alloys at high temperature, Metall Trans B 12, 461-467 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90280-5](https://doi.org/10.1016/0022-5088%2880%2990280-5) S. Kurosawa, Y. Nakamura, M. Shimoji, The electrical conductivity and the phase diagram of the molten tin-tellurium system, Journal of the Less Common Metals 70, 119-121 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3697(63)90038-6](https://doi.org/10.1016/0022-3697%2863%2990038-6) R.F. Brebrick, Deviations from stoichiometry and electrical properties in SnTe, Journal of Physics and Chemistry of Solids 24, 27-36 (1963).  
_cited as the source of values for this phase_
- [doi:10.1143/jjap.1.277](https://doi.org/10.1143/jjap.1.277) Jun-ichi Umeda, Manu Jeong, Toshihiro Okada, Tin-Tellurium Phase Diagram in the Vicinity of Stannous Telluride SnTe, Jpn. J. Appl. Phys. 1, 277 (1962).  
_cited as the source of values for this phase_

## SNTE_B1 (Sn–Te)

- Id: `phase:sn-te:snte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1078.89 K, x(Te) 0.5–0.51053
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sn-te:snte-b1)

Names (3): _corpus: _corpus:phase:sn-te:snte-b1  
_paper: _paper:10.1007/s11664-009-0985-y:SnTe  
_tdb: _tdb:SnTe-10Liu.tdb:SNTE_B1  


### TDB models of SNTE_B1 (1): PHASE and CONSTITUENT statements as written

[SnTe-10Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/SnTe-10Liu.tdb): SNTE_B1, type code %, sha256 `0fe58ce9ad47e379…`

~~~~text
59: PHASE SNTE_B1 % 2 1 1 !
60: CONST SNTE_B1 : SN VA : TE : !
~~~~

Example references (8 of 8; assessments first): 

- [doi:10.1007/s11664-009-0985-y](https://doi.org/10.1007/s11664-009-0985-y) Yajun Liu, Dong Liang, Lijun Zhang, Thermodynamic Descriptions for the Sn-Te and Pb-Sn-Te Systems, Journal of Elec Materi 39, 246-257 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19090640117](https://doi.org/10.1002/zaac.19090640117) Wilhelm Biltz, Werner Mecklenburg, Über die Zustandsdiagramme von Zinn mit Schwefel, Selen und Tellur, Z. Anorg. Chem. 64, 226-235 (1909).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19100690102](https://doi.org/10.1002/zaac.19100690102) Matsusuke Kobayashi, Über die Legierungen des Tellurs mit Cadmium und Zinn, Z. Anorg. Chem. 69, 1-9 (1911).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02654315](https://doi.org/10.1007/bf02654315) J. Rakotomavo, M. -C. Baron, C. Petot, Thermodynamic properties of liquid tin-tellurium alloys at high temperature, Metall Trans B 12, 461-467 (1981).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(80)90280-5](https://doi.org/10.1016/0022-5088%2880%2990280-5) S. Kurosawa, Y. Nakamura, M. Shimoji, The electrical conductivity and the phase diagram of the molten tin-tellurium system, Journal of the Less Common Metals 70, 119-121 (1980).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-3697(63)90038-6](https://doi.org/10.1016/0022-3697%2863%2990038-6) R.F. Brebrick, Deviations from stoichiometry and electrical properties in SnTe, Journal of Physics and Chemistry of Solids 24, 27-36 (1963).  
_cited as the source of values for this phase_
- [doi:10.1021/je60020a019](https://doi.org/10.1021/je60020a019) Chikara. Hirayama, Thermodynamic Properties of Solid Monoxides, Monosulfides, Monoselenides, and Monotellurides of Ge, Sn, and Pb., J. Chem. Eng. Data 9, 65-68 (1964).  
_cited as the source of values for this phase_
- [doi:10.1143/jjap.1.277](https://doi.org/10.1143/jjap.1.277) Jun-ichi Umeda, Manu Jeong, Toshihiro Okada, Tin-Tellurium Phase Diagram in the Vicinity of Stannous Telluride SnTe, Jpn. J. Appl. Phys. 1, 277 (1962).  
_cited as the source of values for this phase_

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
