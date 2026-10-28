# N–Zr phases

> N–Zr system: 6 phases (tier A 2, liquid 1, gas 2, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/N-ZR.md

6 phases (tier A 2, liquid 1, gas 2, interstitial_fcc_a1_compound 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/N-ZR.json) · [N–Zr system page](https://data.orchid-project.org/systems/N-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–Zr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-n-zr-bcc-a2); _phase:n-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1139.03–2153.32 K, x(N) 0–0.06386 | 2 | 2 |
| [FCC_A1](#phase-n-zr-fcc-a1); _phase:n-zr:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 2 of 2 calculated diagram(s): 300–3300.91 K, x(N) 0.38143–0.5 | 12 | 2 |
| [GAS](#phase-n-zr-gas); _phase:n-zr:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300.24–4000 K, x(N) 0.97934–1 | 0 | 2 |
| [HCP_A3](#phase-n-zr-hcp-a3); _phase:n-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2272.29 K, x(N) 0–0.23084 | 2 | 2 |
| [LIQUID](#phase-n-zr-liquid); _phase:n-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2032.86–4000 K, x(N) 0–0.37367 | 0 | 2 |
| [N2GAS](#phase-n-zr-n2gas); _phase:n-zr:n2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2185 K, x(N) 1–1 | 0 | 2 |

## BCC_A2 (N–Zr)

- Id: `phase:n-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1139.03–2153.32 K, x(N) 0–0.06386
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-zr:bcc-a2)

Names (4): _corpus: _corpus:phase:n-zr:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2003.10.051:bcc  
_tdb: _tdb:ZrN-04Ma.tdb:BCC_A2, tdb:ZrN-17Sri.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ZrN-04Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-04Ma.tdb): BCC_A2, type code %B, sha256 `8443e7ae10cd938f…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : ZR : VA% N : !
~~~~

[ZrN-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-17Sri.tdb): BCC_A2, type code %B, sha256 `db8a7c91478b8f7f…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : ZR : VA% N : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.051](https://doi.org/10.1016/j.jallcom.2003.10.051) Xiaoyan Ma, Changrong Li, Kewu Bai, Ping Wu, Weijing Zhang, Thermodynamic assessment of the Zr–N system, Journal of Alloys and Compounds 373, 194-201 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_

## FCC_A1 (N–Zr)

- Id: `phase:n-zr:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3300.91 K, x(N) 0.38143–0.5
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-zr:fcc-a1)

Names (4): _corpus: _corpus:phase:n-zr:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2003.10.051:ZrN  
_tdb: _tdb:ZrN-04Ma.tdb:FCC_A1, tdb:ZrN-17Sri.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ZrN-04Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-04Ma.tdb): FCC_A1, type code %A, sha256 `8443e7ae10cd938f…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : ZR : VA N% : !
~~~~

[ZrN-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-17Sri.tdb): FCC_A1, type code %A, sha256 `db8a7c91478b8f7f…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : ZR : VA N% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.051](https://doi.org/10.1016/j.jallcom.2003.10.051) Xiaoyan Ma, Changrong Li, Kewu Bai, Ping Wu, Weijing Zhang, Thermodynamic assessment of the Zr–N system, Journal of Alloys and Compounds 373, 194-201 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1103/physrevb.45.11557](https://doi.org/10.1103/physrevb.45.11557) A. Fernández Guillermet, J. Häglund, G. Grimvall, Cohesive properties of 4\<i>d\</i>-transition-metal carbides and nitrides in the NaCl-type structure, Phys. Rev. B 45, 11557-11567 (1992).  
_cited as the source of values for this phase_

## GAS (N–Zr)

- Id: `phase:n-zr:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.24–4000 K, x(N) 0.97934–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-zr:gas)

Names (3): _corpus: _corpus:phase:n-zr:gas  
_tdb: _tdb:ZrN-04Ma.tdb:GAS, tdb:ZrN-17Sri.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[ZrN-04Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-04Ma.tdb): GAS, type code %, sha256 `8443e7ae10cd938f…`

~~~~text
48: PHASE GAS:G % 1 1 !
49: CONST GAS:G : N N2 N3 ZR ZR2 ZRN : !
~~~~

[ZrN-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-17Sri.tdb): GAS, type code %, sha256 `db8a7c91478b8f7f…`

~~~~text
52: PHASE GAS:G % 1 1 !
53: CONST GAS:G : N N2 N3 ZR ZR2 ZRN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.10.051](https://doi.org/10.1016/j.jallcom.2003.10.051) Xiaoyan Ma, Changrong Li, Kewu Bai, Ping Wu, Weijing Zhang, Thermodynamic assessment of the Zr–N system, Journal of Alloys and Compounds 373, 194-201 (2004).  
_assessment that models this phase_

## HCP_A3 (N–Zr)

- Id: `phase:n-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2272.29 K, x(N) 0–0.23084
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-zr:hcp-a3)

Names (4): _corpus: _corpus:phase:n-zr:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2003.10.051:hcp  
_tdb: _tdb:ZrN-04Ma.tdb:HCP_A3, tdb:ZrN-17Sri.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ZrN-04Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-04Ma.tdb): HCP_A3, type code %A, sha256 `8443e7ae10cd938f…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : ZR : VA% N : !
~~~~

[ZrN-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-17Sri.tdb): HCP_A3, type code %A, sha256 `db8a7c91478b8f7f…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : ZR : VA% N : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2003.10.051](https://doi.org/10.1016/j.jallcom.2003.10.051) Xiaoyan Ma, Changrong Li, Kewu Bai, Ping Wu, Weijing Zhang, Thermodynamic assessment of the Zr–N system, Journal of Alloys and Compounds 373, 194-201 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_

## LIQUID (N–Zr)

- Id: `phase:n-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2032.86–4000 K, x(N) 0–0.37367
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-zr:liquid)

Names (3): _corpus: _corpus:phase:n-zr:liquid  
_tdb: _tdb:ZrN-04Ma.tdb:LIQUID, tdb:ZrN-17Sri.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ZrN-04Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-04Ma.tdb): LIQUID, type code %, sha256 `8443e7ae10cd938f…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : ZR N : !
~~~~

[ZrN-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-17Sri.tdb): LIQUID, type code %, sha256 `db8a7c91478b8f7f…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : ZR N : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.10.051](https://doi.org/10.1016/j.jallcom.2003.10.051) Xiaoyan Ma, Changrong Li, Kewu Bai, Ping Wu, Weijing Zhang, Thermodynamic assessment of the Zr–N system, Journal of Alloys and Compounds 373, 194-201 (2004).  
_assessment that models this phase_

## N2GAS (N–Zr)

- Id: `phase:n-zr:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2185 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-zr:n2gas)

Names (3): _corpus: _corpus:phase:n-zr:n2gas  
_tdb: _tdb:ZrN-04Ma.tdb:N2GAS, tdb:ZrN-17Sri.tdb:N2GAS  


### TDB models of N2GAS (2): PHASE and CONSTITUENT statements as written

[ZrN-04Ma.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-04Ma.tdb): N2GAS, type code %, sha256 `8443e7ae10cd938f…`

~~~~text
45: PHASE N2GAS % 1 1 !
46: CONST N2GAS : N2 : !
~~~~

[ZrN-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/ZrN-17Sri.tdb): N2GAS, type code %, sha256 `db8a7c91478b8f7f…`

~~~~text
49: PHASE N2GAS % 1 1 !
50: CONST N2GAS : N2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2003.10.051](https://doi.org/10.1016/j.jallcom.2003.10.051) Xiaoyan Ma, Changrong Li, Kewu Bai, Ping Wu, Weijing Zhang, Thermodynamic assessment of the Zr–N system, Journal of Alloys and Compounds 373, 194-201 (2004).  
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
