# Te–Zr phases

> Te–Zr system: 11 phases (tier A 7, tier B 3, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TE-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/TE-ZR.md

11 phases (tier A 7, tier B 3, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TE-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/TE-ZR.json) · [Markdown](https://data.orchid-project.org/phases/pages/TE-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Te–Zr system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-te-zr-a8-hexagonal); _phase:te-zr:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 1 |
| [BCC_A2](#phase-te-zr-bcc-a2); _phase:te-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1139–2952.85 K, x(Te) 0–0 | 0 | 1 |
| [FCC_A1](#phase-te-zr-fcc-a1); _phase:te-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-te-zr-hcp-a3); _phase:te-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1139 K, x(Te) 0–0 | 0 | 1 |
| [LIQUID](#phase-te-zr-liquid); _phase:te-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 719.41–4000 K, x(Te) 0–1 | 0 | 1 |
| [ZR3TE_D0E](#phase-te-zr-zr3te-d0e); _phase:te-zr:zr3te-d0e_ | Ni3P · D0_e · tI32 · I-4 (82) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1625.19 K, x(Te) 0.25–0.25 | 0 | 1 |
| [ZR5TE4](#phase-te-zr-zr5te4); _phase:te-zr:zr5te4_ | Ti5Te4 · tI18 · I4/m (87) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1834.65 K, x(Te) 0.44444–0.44444 | 0 | 1 |
| [ZRTE_BH](#phase-te-zr-zrte-bh); _phase:te-zr:zrte-bh_ | WC · B_h · hP2 · P-6m2 (187) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1504.56 K, x(Te) 0.5–0.5 | 0 | 1 |
| [ZRTE2_B81](#phase-te-zr-zrte2-b81); _phase:te-zr:zrte2-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1933.38 K, x(Te) 0.54601–0.66667 | 0 | 1 |
| [ZRTE3](#phase-te-zr-zrte3); _phase:te-zr:zrte3_ | ZrSe3 · mP8 · P2_1/m (11) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1231.31 K, x(Te) 0.75–0.75 | 0 | 1 |
| [ZRTE5](#phase-te-zr-zrte5); _phase:te-zr:zrte5_ | HfTe5 · oC24 · Cmcm (63) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–821.99 K, x(Te) 0.83333–0.83333 | 0 | 1 |

## HEXAGONAL_A8 (Te–Zr)

- Id: `phase:te-zr:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:a8-hexagonal)

Names (2): _corpus: _corpus:phase:te-zr:a8-hexagonal  
_tdb: _tdb:ZrTe-21Don.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): HEXAGONAL_A8, type code %, sha256 `6a4d51c982395e56…`

~~~~text
41: PHASE HEXAGONAL_A8 % 1 1 !
42: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## BCC_A2 (Te–Zr)

- Id: `phase:te-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Zr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1139–2952.85 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:bcc-a2)

Names (2): _corpus: _corpus:phase:te-zr:bcc-a2  
_tdb: _tdb:ZrTe-21Don.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): BCC_A2, type code %B, sha256 `6a4d51c982395e56…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## FCC_A1 (Te–Zr)

- Id: `phase:te-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Zr 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:te-zr:fcc-a1  
_tdb: _tdb:ZrTe-21Don.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): FCC_A1, type code %A, sha256 `6a4d51c982395e56…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## HCP_A3 (Te–Zr)

- Id: `phase:te-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Zr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1139 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:hcp-a3)

Names (2): _corpus: _corpus:phase:te-zr:hcp-a3  
_tdb: _tdb:ZrTe-21Don.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): HCP_A3, type code %A, sha256 `6a4d51c982395e56…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## LIQUID (Te–Zr)

- Id: `phase:te-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 719.41–4000 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:liquid)

Names (2): _corpus: _corpus:phase:te-zr:liquid  
_tdb: _tdb:ZrTe-21Don.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): LIQUID, type code %, sha256 `6a4d51c982395e56…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : TE ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## ZR3TE_D0E (Te–Zr)

- Id: `phase:te-zr:zr3te-d0e`; status `assigned`
- Structure: Ni3P · D0_e · tI32 · I-4 (82); type `st:d0-e-ni3p-ti32`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacqz and oqmd-646647, space group 82
- Stoichiometry: Te 0.2500, Zr 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1625.19 K, x(Te) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:zr3te-d0e)

Names (4): _corpus: _corpus:phase:te-zr:zr3te-d0e  
_mp: _mp:mp-aaaaacqz  
_oqmd: _oqmd:oqmd-646647  
_tdb: _tdb:ZrTe-21Don.tdb:ZR3TE_D0E  


### TDB models of ZR3TE_D0E (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): ZR3TE_D0E, type code %, sha256 `6a4d51c982395e56…`

~~~~text
46: PHASE ZR3TE_D0E % 2 3 1 !
47: CONST ZR3TE_D0E : ZR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## ZR5TE4 (Te–Zr)

- Id: `phase:te-zr:zr5te4`; status `assigned`
- Structure: Ti5Te4 · tI18 · I4/m (87); type `st:ti5te4-ti18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Te 0.4444, Zr 0.5556
- Stability: stable in 1 of 1 calculated diagram(s): 300–1834.65 K, x(Te) 0.44444–0.44444
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:zr5te4)

Names (4): _corpus: _corpus:phase:te-zr:zr5te4  
_mp: _mp:mp-aaaaaanm  
_oqmd: _oqmd:oqmd-646646  
_tdb: _tdb:ZrTe-21Don.tdb:ZR5TE4  


### TDB models of ZR5TE4 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): ZR5TE4, type code %, sha256 `6a4d51c982395e56…`

~~~~text
51: PHASE ZR5TE4 % 2 5 4 !
52: CONST ZR5TE4 : ZR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## ZRTE_BH (Te–Zr)

- Id: `phase:te-zr:zrte-bh`; status `assigned`
- Structure: WC · B_h · hP2 · P-6m2 (187); type `st:b-h-wc-hp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaachf and oqmd-31237, space group 187
- Stoichiometry: Te 0.5000, Zr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1504.56 K, x(Te) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:zrte-bh)

Names (4): _corpus: _corpus:phase:te-zr:zrte-bh  
_mp: _mp:mp-aaaaachf  
_oqmd: _oqmd:oqmd-31237  
_tdb: _tdb:ZrTe-21Don.tdb:ZRTE_BH  


### TDB models of ZRTE_BH (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): ZRTE_BH, type code %, sha256 `6a4d51c982395e56…`

~~~~text
56: PHASE ZRTE_BH % 2 1 1 !
57: CONST ZRTE_BH : ZR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## ZRTE2_B81 (Te–Zr)

- Id: `phase:te-zr:zrte2-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1933.38 K, x(Te) 0.54601–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:zrte2-b81)

Names (2): _corpus: _corpus:phase:te-zr:zrte2-b81  
_tdb: _tdb:ZrTe-21Don.tdb:ZRTE2_B81  


### TDB models of ZRTE2_B81 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): ZRTE2_B81, type code %, sha256 `6a4d51c982395e56…`

~~~~text
61: PHASE ZRTE2_B81 % 3 1 1 1 !
62: CONST ZRTE2_B81 : ZR% VA : ZR TE% : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## ZRTE3 (Te–Zr)

- Id: `phase:te-zr:zrte3`; status `assigned`
- Structure: ZrSe3 · mP8 · P2_1/m (11); type `st:zrse3-mp8`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Te 0.7500, Zr 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1231.31 K, x(Te) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:zrte3)

Names (4): _corpus: _corpus:phase:te-zr:zrte3  
_mp: _mp:mp-aaaaadcj  
_oqmd: _oqmd:oqmd-7677  
_tdb: _tdb:ZrTe-21Don.tdb:ZRTE3  


### TDB models of ZRTE3 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): ZRTE3, type code %, sha256 `6a4d51c982395e56…`

~~~~text
66: PHASE ZRTE3 % 2 1 3 !
67: CONST ZRTE3 : ZR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
_assessment that models this phase_

## ZRTE5 (Te–Zr)

- Id: `phase:te-zr:zrte5`; status `assigned`
- Structure: HfTe5 · oC24 · Cmcm (63); type `st:hfte5-oc24`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Te 0.8333, Zr 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–821.99 K, x(Te) 0.83333–0.83333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zr:zrte5)

Names (4): _corpus: _corpus:phase:te-zr:zrte5  
_mp: _mp:mp-aaaaaaxh  
_oqmd: _oqmd:oqmd-15246  
_tdb: _tdb:ZrTe-21Don.tdb:ZRTE5  


### TDB models of ZRTE5 (1): PHASE and CONSTITUENT statements as written

[ZrTe-21Don.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrTe-21Don.tdb): ZRTE5, type code %, sha256 `6a4d51c982395e56…`

~~~~text
71: PHASE ZRTE5 % 2 1 5 !
72: CONST ZRTE5 : ZR : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102281](https://doi.org/10.1016/j.calphad.2021.102281) C. Dong, J. Wang, B. Hu, L. Zhu, Q. Wu, Y. Du, Calphad, 74, 102281(2021).  
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
