# W–Zr phases

> W–Zr system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/W-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/W-ZR.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=W-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/W-ZR.json) · [W–Zr system page](https://data.orchid-project.org/systems/W-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/W-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the W–Zr system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-w-zr-bcc-a2); _phase:w-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.5 K, x(Zr) 0–1 | 0 | 3 |
| [FCC_A1](#phase-w-zr-fcc-a1); _phase:w-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-w-zr-hcp-a3); _phase:w-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2953.99 K, x(Zr) 0.98401–1 | 0 | 3 |
| [LIQUID](#phase-w-zr-liquid); _phase:w-zr:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 2008.01–4000 K, x(Zr) 0–1 | 0 | 3 |
| [W2ZR_C15](#phase-w-zr-w2zr-c15); _phase:w-zr:w2zr-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2483.01 K, x(Zr) 0.33333–0.33333 | 0 | 3 |

## BCC_A2 (W–Zr)

- Id: `phase:w-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.5 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:w-zr:bcc-a2)

Names (4): _corpus: _corpus:phase:w-zr:bcc-a2  
_tdb: _tdb:WZr-05Che-LB.tdb:BCC_A2, tdb:WZr-14Guo.tdb:BCC_A2, tdb:WZr-15Zho.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[WZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-05Che-LB.tdb): BCC_A2, type code %B, sha256 `af77465c41cacf96…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : W% ZR% : VA : !
~~~~

[WZr-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-14Guo.tdb): BCC_A2, type code %B, sha256 `d1406ccd7982049e…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : W% ZR% : VA : !
~~~~

[WZr-15Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-15Zho.tdb): BCC_A2, type code %B, sha256 `137a7e45504cb7ce…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : W% ZR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2015.02.002](https://doi.org/10.1016/j.ijrmhm.2015.02.002) Peng Zhou, Yingbiao Peng, Yong Du, Shequan Wang, Guanghua Wen, Thermodynamic modeling of the C–W–Zr system, International Journal of Refractory Metals and Hard Materials 50, 274-281 (2015).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## FCC_A1 (W–Zr)

- Id: `phase:w-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:w-zr:fcc-a1)

Names (4): _corpus: _corpus:phase:w-zr:fcc-a1  
_tdb: _tdb:WZr-05Che-LB.tdb:FCC_A1, tdb:WZr-14Guo.tdb:FCC_A1, tdb:WZr-15Zho.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[WZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-05Che-LB.tdb): FCC_A1, type code %A, sha256 `af77465c41cacf96…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : W ZR : VA : !
~~~~

[WZr-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-14Guo.tdb): FCC_A1, type code %A, sha256 `d1406ccd7982049e…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : W ZR : VA : !
~~~~

[WZr-15Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-15Zho.tdb): FCC_A1, type code %A, sha256 `137a7e45504cb7ce…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : W ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2015.02.002](https://doi.org/10.1016/j.ijrmhm.2015.02.002) Peng Zhou, Yingbiao Peng, Yong Du, Shequan Wang, Guanghua Wen, Thermodynamic modeling of the C–W–Zr system, International Journal of Refractory Metals and Hard Materials 50, 274-281 (2015).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## HCP_A3 (W–Zr)

- Id: `phase:w-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2953.99 K, x(Zr) 0.98401–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:w-zr:hcp-a3)

Names (4): _corpus: _corpus:phase:w-zr:hcp-a3  
_tdb: _tdb:WZr-05Che-LB.tdb:HCP_A3, tdb:WZr-14Guo.tdb:HCP_A3, tdb:WZr-15Zho.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[WZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-05Che-LB.tdb): HCP_A3, type code %A, sha256 `af77465c41cacf96…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : W ZR% : VA : !
~~~~

[WZr-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-14Guo.tdb): HCP_A3, type code %A, sha256 `d1406ccd7982049e…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : W ZR% : VA : !
~~~~

[WZr-15Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-15Zho.tdb): HCP_A3, type code %A, sha256 `137a7e45504cb7ce…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : W ZR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2015.02.002](https://doi.org/10.1016/j.ijrmhm.2015.02.002) Peng Zhou, Yingbiao Peng, Yong Du, Shequan Wang, Guanghua Wen, Thermodynamic modeling of the C–W–Zr system, International Journal of Refractory Metals and Hard Materials 50, 274-281 (2015).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## LIQUID (W–Zr)

- Id: `phase:w-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2008.01–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:w-zr:liquid)

Names (4): _corpus: _corpus:phase:w-zr:liquid  
_tdb: _tdb:WZr-05Che-LB.tdb:LIQUID, tdb:WZr-14Guo.tdb:LIQUID, tdb:WZr-15Zho.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[WZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-05Che-LB.tdb): LIQUID, type code %, sha256 `af77465c41cacf96…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : W ZR : !
~~~~

[WZr-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-14Guo.tdb): LIQUID, type code %, sha256 `d1406ccd7982049e…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : W ZR : !
~~~~

[WZr-15Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-15Zho.tdb): LIQUID, type code %, sha256 `137a7e45504cb7ce…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : W ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2015.02.002](https://doi.org/10.1016/j.ijrmhm.2015.02.002) Peng Zhou, Yingbiao Peng, Yong Du, Shequan Wang, Guanghua Wen, Thermodynamic modeling of the C–W–Zr system, International Journal of Refractory Metals and Hard Materials 50, 274-281 (2015).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

## W2ZR_C15 (W–Zr)

- Id: `phase:w-zr:w2zr-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaazz and oqmd-18179, space group 227
- Stoichiometry: W 0.6667, Zr 0.3333
- Stability: stable in 3 of 3 calculated diagram(s): 300–2483.01 K, x(Zr) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:w-zr:w2zr-c15)

Names (6): _corpus: _corpus:phase:w-zr:w2zr-c15  
_mp: _mp:mp-aaaaaazz  
_oqmd: _oqmd:oqmd-18179  
_tdb: _tdb:WZr-05Che-LB.tdb:W2ZR_C15, tdb:WZr-14Guo.tdb:W2ZR_C15, tdb:WZr-15Zho.tdb:W2ZR_C15  


### TDB models of W2ZR_C15 (3): PHASE and CONSTITUENT statements as written

[WZr-05Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-05Che-LB.tdb): W2ZR_C15, type code %, sha256 `af77465c41cacf96…`

~~~~text
40: PHASE W2ZR_C15 % 2 2 1 !
41: CONST W2ZR_C15 : W : ZR : !
~~~~

[WZr-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-14Guo.tdb): W2ZR_C15, type code %, sha256 `d1406ccd7982049e…`

~~~~text
41: PHASE W2ZR_C15 % 2 2 1 !
42: CONST W2ZR_C15 : W : ZR : !
~~~~

[WZr-15Zho.tdb](https://orchid-project.org/data/databases/sgte-binary/WZr-15Zho.tdb): W2ZR_C15, type code %, sha256 `137a7e45504cb7ce…`

~~~~text
44: PHASE W2ZR_C15 % 2 2 1 !
45: CONST W2ZR_C15 : W : ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.ijrmhm.2015.02.002](https://doi.org/10.1016/j.ijrmhm.2015.02.002) Peng Zhou, Yingbiao Peng, Yong Du, Shequan Wang, Guanghua Wen, Thermodynamic modeling of the C–W–Zr system, International Journal of Refractory Metals and Hard Materials 50, 274-281 (2015).  
_assessment that models this phase_
- [doi:10.3139/146.111125](https://doi.org/10.3139/146.111125) C. Guo, C. Li, S. Shang, Z. Du, Thermodynamic description of the Ta–W–Zr system, Int. J. Mater. Res. 105 (11) (2014) 1048–1056.  
_assessment that models this phase_

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
