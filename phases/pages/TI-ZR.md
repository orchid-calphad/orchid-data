# Ti–Zr phases

> Ti–Zr system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TI-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/TI-ZR.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TI-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/TI-ZR.json) · [Ti–Zr system page](https://data.orchid-project.org/systems/TI-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/TI-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ti–Zr system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ti-zr-bcc-a2); _phase:ti-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 823.63–3999.1 K, x(Zr) 0–1 | 0 | 5 |
| [FCC_A1](#phase-ti-zr-fcc-a1); _phase:ti-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-ti-zr-hcp-a3); _phase:ti-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 299.64–2124 K, x(Zr) 0–1 | 0 | 5 |
| [LIQUID](#phase-ti-zr-liquid); _phase:ti-zr:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1805.58–4000 K, x(Zr) 0–1 | 1 | 5 |

## BCC_A2 (Ti–Zr)

- Id: `phase:ti-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 823.63–3999.1 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-zr:bcc-a2)

Names (6): _corpus: _corpus:phase:ti-zr:bcc-a2  
_tdb: _tdb:TiZr-08Tur.tdb:BCC_A2, tdb:TiZr-16Cui.tdb:BCC_A2, tdb:TiZr-17Sri.tdb:BCC_A2, tdb:TiZr-20Jia.tdb:BCC_A2, tdb:TiZr-94Har-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[TiZr-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-08Tur.tdb): BCC_A2, type code %B, sha256 `0cc6a63009d222a5…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : TI ZR : VA : !
~~~~

[TiZr-16Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-16Cui.tdb): BCC_A2, type code %B, sha256 `6c69e4367f79c33e…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : TI ZR : VA : !
~~~~

[TiZr-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-17Sri.tdb): BCC_A2, type code %B, sha256 `889b36cdc39231a0…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : TI ZR : VA : !
~~~~

[TiZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-20Jia.tdb): BCC_A2, type code %B, sha256 `e4904d8e52b1795c…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : TI ZR : VA : !
~~~~

[TiZr-94Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-94Har-LB.tdb): BCC_A2, type code %B, sha256 `a3a08b354c28b6a1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : TI ZR : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11106-008-9039-x](https://doi.org/10.1007/s11106-008-9039-x) M. A. Turchanin, P. G. Agraval, A. R. Abdulov, Thermodynamic assessment of the Cu-Ti-Zr system. II. Cu-Zr and Ti-Zr systems, Powder Metall Met Ceram 47, 428-446 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90019-1](https://doi.org/10.1016/0925-8388%2894%2990019-1) K.C. Hari Kumar, P. Wollants, L. Delacy, Thermodynamic assessment of the TiZr system and calculation of the NbTiZr phase diagram, Journal of Alloys and Compounds 206, 121-127 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_

## FCC_A1 (Ti–Zr)

- Id: `phase:ti-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-zr:fcc-a1)

Names (6): _corpus: _corpus:phase:ti-zr:fcc-a1  
_tdb: _tdb:TiZr-08Tur.tdb:FCC_A1, tdb:TiZr-16Cui.tdb:FCC_A1, tdb:TiZr-17Sri.tdb:FCC_A1, tdb:TiZr-20Jia.tdb:FCC_A1, tdb:TiZr-94Har-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[TiZr-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-08Tur.tdb): FCC_A1, type code %A, sha256 `0cc6a63009d222a5…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : TI ZR : VA : !
~~~~

[TiZr-16Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-16Cui.tdb): FCC_A1, type code %A, sha256 `6c69e4367f79c33e…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : TI ZR : VA : !
~~~~

[TiZr-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-17Sri.tdb): FCC_A1, type code %A, sha256 `889b36cdc39231a0…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : TI ZR : VA : !
~~~~

[TiZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-20Jia.tdb): FCC_A1, type code %A, sha256 `e4904d8e52b1795c…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : TI ZR : VA : !
~~~~

[TiZr-94Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-94Har-LB.tdb): FCC_A1, type code %A, sha256 `a3a08b354c28b6a1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : TI ZR : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11106-008-9039-x](https://doi.org/10.1007/s11106-008-9039-x) M. A. Turchanin, P. G. Agraval, A. R. Abdulov, Thermodynamic assessment of the Cu-Ti-Zr system. II. Cu-Zr and Ti-Zr systems, Powder Metall Met Ceram 47, 428-446 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90019-1](https://doi.org/10.1016/0925-8388%2894%2990019-1) K.C. Hari Kumar, P. Wollants, L. Delacy, Thermodynamic assessment of the TiZr system and calculation of the NbTiZr phase diagram, Journal of Alloys and Compounds 206, 121-127 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_

## HCP_A3 (Ti–Zr)

- Id: `phase:ti-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 299.64–2124 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-zr:hcp-a3)

Names (6): _corpus: _corpus:phase:ti-zr:hcp-a3  
_tdb: _tdb:TiZr-08Tur.tdb:HCP_A3, tdb:TiZr-16Cui.tdb:HCP_A3, tdb:TiZr-17Sri.tdb:HCP_A3, tdb:TiZr-20Jia.tdb:HCP_A3, tdb:TiZr-94Har-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[TiZr-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-08Tur.tdb): HCP_A3, type code %A, sha256 `0cc6a63009d222a5…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : TI ZR : VA : !
~~~~

[TiZr-16Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-16Cui.tdb): HCP_A3, type code %A, sha256 `6c69e4367f79c33e…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : TI ZR : VA : !
~~~~

[TiZr-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-17Sri.tdb): HCP_A3, type code %A, sha256 `889b36cdc39231a0…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : TI ZR : VA : !
~~~~

[TiZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-20Jia.tdb): HCP_A3, type code %A, sha256 `e4904d8e52b1795c…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : TI ZR : VA : !
~~~~

[TiZr-94Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-94Har-LB.tdb): HCP_A3, type code %A, sha256 `a3a08b354c28b6a1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : TI ZR : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11106-008-9039-x](https://doi.org/10.1007/s11106-008-9039-x) M. A. Turchanin, P. G. Agraval, A. R. Abdulov, Thermodynamic assessment of the Cu-Ti-Zr system. II. Cu-Zr and Ti-Zr systems, Powder Metall Met Ceram 47, 428-446 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90019-1](https://doi.org/10.1016/0925-8388%2894%2990019-1) K.C. Hari Kumar, P. Wollants, L. Delacy, Thermodynamic assessment of the TiZr system and calculation of the NbTiZr phase diagram, Journal of Alloys and Compounds 206, 121-127 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_

## LIQUID (Ti–Zr)

- Id: `phase:ti-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1805.58–4000 K, x(Zr) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ti-zr:liquid)

Names (7): _corpus: _corpus:phase:ti-zr:liquid  
_paper: _paper:10.1016/j.calphad.2011.10.003:L  
_tdb: _tdb:TiZr-08Tur.tdb:LIQUID, tdb:TiZr-16Cui.tdb:LIQUID, tdb:TiZr-17Sri.tdb:LIQUID, tdb:TiZr-20Jia.tdb:LIQUID, tdb:TiZr-94Har-LB.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[TiZr-08Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-08Tur.tdb): LIQUID, type code %, sha256 `0cc6a63009d222a5…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : TI ZR : !
~~~~

[TiZr-16Cui.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-16Cui.tdb): LIQUID, type code %, sha256 `6c69e4367f79c33e…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : TI ZR : !
~~~~

[TiZr-17Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-17Sri.tdb): LIQUID, type code %, sha256 `889b36cdc39231a0…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : TI ZR : !
~~~~

[TiZr-20Jia.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-20Jia.tdb): LIQUID, type code %, sha256 `e4904d8e52b1795c…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : TI ZR : !
~~~~

[TiZr-94Har-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/TiZr-94Har-LB.tdb): LIQUID, type code %, sha256 `a3a08b354c28b6a1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : TI ZR : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11106-008-9039-x](https://doi.org/10.1007/s11106-008-9039-x) M. A. Turchanin, P. G. Agraval, A. R. Abdulov, Thermodynamic assessment of the Cu-Ti-Zr system. II. Cu-Zr and Ti-Zr systems, Powder Metall Met Ceram 47, 428-446 (2008).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(94)90019-1](https://doi.org/10.1016/0925-8388%2894%2990019-1) K.C. Hari Kumar, P. Wollants, L. Delacy, Thermodynamic assessment of the TiZr system and calculation of the NbTiZr phase diagram, Journal of Alloys and Compounds 206, 121-127 (1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.09.003](https://doi.org/10.1016/j.calphad.2016.09.003) J. Cui, C. Guo, L. Zou, C. Li, Z. Du, Calphad, 55, 189-98(2016).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2016.12.003](https://doi.org/10.1016/j.calphad.2016.12.003) S. Sridar, R. Kumar, K.C. Hari Kumar, Calphad, 56, 102-107(2017).  
_assessment that models this phase_
- [doi:10.1016/j.mtla.2020.100701](https://doi.org/10.1016/j.mtla.2020.100701) Chao Jiang, Robert D. Mariani, Cynthia A. Adkins, Ab initio investigation and thermodynamic modeling of the Mo–Ti–Zr system, Materialia 10, 100701 (2020).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.10.003](https://doi.org/10.1016/j.calphad.2011.10.003) G. Cacciamani, P. Riani, F. Valenza, Equilibrium between MB2 (M=Ti,Zr,Hf) UHTC and Ni: A thermodynamic database for the B–Hf–Ni–Ti–Zr system, Calphad 35, 601-619 (2011).  
_reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
