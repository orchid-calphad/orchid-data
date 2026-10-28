# Co–Pt phases

> Co–Pt system: 7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-PT.html · Markdown: https://data.orchid-project.org/phases/pages/CO-PT.md

7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-PT) · [full JSON](https://data.orchid-project.org/phases/systems/CO-PT.json) · [Co–Pt system page](https://data.orchid-project.org/systems/CO-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Pt system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-pt-bcc-a2); _phase:co-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [COPT_L10](#phase-co-pt-copt-l10); _phase:co-pt:copt-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1101.5 K, x(Pt) 0.39722–0.63247 | 0 | 1 |
| [COPT3_L12](#phase-co-pt-copt3-l12); _phase:co-pt:copt3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1026.9 K, x(Pt) 0.69701–0.77468 | 0 | 1 |
| [FCC_4SL](#phase-co-pt-fcc-4sl); _phase:co-pt:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2041.5 K, x(Pt) 0–1 | 0 | 1 |
| [FCC_A1](#phase-co-pt-fcc-a1); _phase:co-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2499 K, x(Pt) 0–1 | 0 | 4 |
| [HCP_A3](#phase-co-pt-hcp-a3); _phase:co-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–887.96 K, x(Pt) 0–0.40323 | 0 | 3 |
| [LIQUID](#phase-co-pt-liquid); _phase:co-pt:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1700.78–2500 K, x(Pt) 0–1 | 0 | 3 |

## BCC_A2 (Co–Pt)

- Id: `phase:co-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:bcc-a2)

Names (4): _corpus: _corpus:phase:co-pt:bcc-a2  
_tdb: _tdb:CoPt-01Oik.tdb:BCC_A2, tdb:CoPt-11Kim.tdb:BCC_A2, tdb:CoPt-90Spe-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CoPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-01Oik.tdb): BCC_A2, type code %B, sha256 `adf708dbafc5b2c3…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO PT : VA : !
~~~~

[CoPt-11Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb): BCC_A2, type code %B, sha256 `335cf2628217f37f…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : CO PT : VA : !
~~~~

[CoPt-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb): BCC_A2, type code %B, sha256 `8a9bf4d4f4636b89…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO PT : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005) DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## COPT_L10 (Co–Pt)

- Id: `phase:co-pt:copt-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1101.5 K, x(Pt) 0.39722–0.63247
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:copt-l10)

Names (2): _corpus: _corpus:phase:co-pt:copt-l10  
_tdb: _tdb:CoPt-90Spe-LB.tdb:COPT_L10  


### TDB models of COPT_L10 (1): PHASE and CONSTITUENT statements as written

[CoPt-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb): COPT_L10, type code %A, sha256 `8a9bf4d4f4636b89…`

~~~~text
40: PHASE COPT_L10 %A 1 1 !
41: CONST COPT_L10 : CO PT : !
~~~~

## COPT3_L12 (Co–Pt)

- Id: `phase:co-pt:copt3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1026.9 K, x(Pt) 0.69701–0.77468
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:copt3-l12)

Names (2): _corpus: _corpus:phase:co-pt:copt3-l12  
_tdb: _tdb:CoPt-90Spe-LB.tdb:COPT3_L12  


### TDB models of COPT3_L12 (1): PHASE and CONSTITUENT statements as written

[CoPt-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb): COPT3_L12, type code %A, sha256 `8a9bf4d4f4636b89…`

~~~~text
45: PHASE COPT3_L12 %A 1 1 !
46: CONST COPT3_L12 : CO PT : !
~~~~

## FCC_4SL (Co–Pt)

- Id: `phase:co-pt:fcc-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:CoPt-11Kim.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; sgte_mmc2_rows_disagree; unrecognised_name_tokens:4SL
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP Co3Pt at x(PT)=0.2500
- Candidate (dft_mp): P4/mmm (123) — on-hull MP CoPt at x(PT)=0.5000
- Candidate (dft_mp): Pm-3m (221) — on-hull MP CoPt3 at x(PT)=0.7500
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Co1 Pt2 at x(PT)=0.6667
- Candidate (dft_oqmd): I4/mmm (139) — on-hull OQMD Co1 Pt8 at x(PT)=0.8889
- Candidate (dft_oqmd): Pm (6) — on-hull OQMD Co19 Pt1 at x(PT)=0.0500
- Candidate (dft_oqmd): C2/m (12) — on-hull OQMD Co2 Pt7 at x(PT)=0.7778
- Candidate (dft_oqmd): P63/mmc (194) — on-hull OQMD Co3 Pt1 at x(PT)=0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–2041.5 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:fcc-4sl)

Names (2): _corpus: _corpus:phase:co-pt:fcc-4sl  
_tdb: _tdb:CoPt-11Kim.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[CoPt-11Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb): FCC_4SL, type code %AY, sha256 `335cf2628217f37f…`

~~~~text
37: PHASE FCC_4SL:F %AY 5 0.25 0.25 0.25 0.25 1 !
38: CONST FCC_4SL:F : CO PT : CO PT : CO PT : CO PT : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005) DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011).  
_assessment that models this phase_

## FCC_A1 (Co–Pt)

- Id: `phase:co-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2499 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:fcc-a1)

Names (5): _corpus: _corpus:phase:co-pt:fcc-a1  
_tdb: _tdb:CoPt-01Oik.tdb:FCC_A1, tdb:CoPt-11Kim.tdb:A1_FCC, tdb:CoPt-11Kim.tdb:FCC_A1, tdb:CoPt-90Spe-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CoPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-01Oik.tdb): FCC_A1, type code %A, sha256 `adf708dbafc5b2c3…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% PT% : VA : !
~~~~

[CoPt-11Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb): A1_FCC, type code %A, sha256 `335cf2628217f37f…`

~~~~text
32: PHASE A1_FCC %A 2 1 1 !
33: CONST A1_FCC : CO PT : VA : !
~~~~

[CoPt-11Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb): FCC_A1, type code %A, sha256 `335cf2628217f37f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% PT% : VA : !
~~~~

[CoPt-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb): FCC_A1, type code %A, sha256 `8a9bf4d4f4636b89…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% PT% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005) DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## HCP_A3 (Co–Pt)

- Id: `phase:co-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–887.96 K, x(Pt) 0–0.40323
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:hcp-a3)

Names (4): _corpus: _corpus:phase:co-pt:hcp-a3  
_tdb: _tdb:CoPt-01Oik.tdb:HCP_A3, tdb:CoPt-11Kim.tdb:HCP_A3, tdb:CoPt-90Spe-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CoPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-01Oik.tdb): HCP_A3, type code %A, sha256 `adf708dbafc5b2c3…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CO% PT : VA : !
~~~~

[CoPt-11Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb): HCP_A3, type code %A, sha256 `335cf2628217f37f…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CO% PT : VA : !
~~~~

[CoPt-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb): HCP_A3, type code %A, sha256 `8a9bf4d4f4636b89…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% PT : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005) DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
_assessment that models this phase_

## LIQUID (Co–Pt)

- Id: `phase:co-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1700.78–2500 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-pt:liquid)

Names (4): _corpus: _corpus:phase:co-pt:liquid  
_tdb: _tdb:CoPt-01Oik.tdb:LIQUID, tdb:CoPt-11Kim.tdb:LIQUID, tdb:CoPt-90Spe-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CoPt-01Oik.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-01Oik.tdb): LIQUID, type code %, sha256 `adf708dbafc5b2c3…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO PT : !
~~~~

[CoPt-11Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-11Kim.tdb): LIQUID, type code %, sha256 `335cf2628217f37f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO PT : !
~~~~

[CoPt-90Spe-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoPt-90Spe-LB.tdb): LIQUID, type code %, sha256 `8a9bf4d4f4636b89…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO PT : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.04.005](https://doi.org/10.1016/j.calphad.2011.04.005) DongEung Kim, James E. Saal, Liangcai Zhou, ShunLi Shang, Yong Du, Zi-Kui Liu, Thermodynamic modeling of fcc order/disorder transformations in the Co–Pt system, Calphad 35, 323-330 (2011).  
_assessment that models this phase_
- [doi:10.1016/S0304-8853(00)00520-5](https://doi.org/10.1016/S0304-8853%2800%2900520-5) K. Oikawa, G.W. Qin, T. Ikeshoji, O. Kitakami, Y. Shimada, K. Ishida, K. Fukamichi, J. Magn. Magn. Mater., 236, 220-33(2001).  
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
