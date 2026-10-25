# Mn–Ta phases

> Mn–Ta system: 8 phases (tier A 7, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-TA.html · Markdown: https://data.orchid-project.org/phases/pages/MN-TA.md

8 phases (tier A 7, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-TA) · [full JSON](https://data.orchid-project.org/phases/systems/MN-TA.json) · [Mn–Ta system page](https://data.orchid-project.org/systems/MN-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–Ta system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-ta-bcc-a2); _phase:mn-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(Ta) 0–1 | 0 | 2 |
| [C14_LAVES](#phase-mn-ta-c14-laves); _phase:mn-ta:c14-laves_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2070.13 K, x(Ta) 0.30661–0.39902 | 0 | 1 |
| [CBCC_A12](#phase-mn-ta-cbcc-a12); _phase:mn-ta:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1036.88 K, x(Ta) 0–0.01438 | 0 | 2 |
| [CUB_A13](#phase-mn-ta-cub-a13); _phase:mn-ta:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 970.44–1382.2 K, x(Ta) 0–0.00936 | 0 | 2 |
| [FCC_A1](#phase-mn-ta-fcc-a1); _phase:mn-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1347.37–1478.5 K, x(Ta) 0–0.01739 | 0 | 2 |
| [HCP_A3](#phase-mn-ta-hcp-a3); _phase:mn-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-mn-ta-liquid); _phase:mn-ta:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1457.71–4000 K, x(Ta) 0–1 | 2 | 2 |
| [MN2TA_C14](#phase-mn-ta-mn2ta-c14); _phase:mn-ta:mn2ta-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1939.38 K, x(Ta) 0.33333–0.33333 | 0 | 1 |

## BCC_A2 (Mn–Ta)

- Id: `phase:mn-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:bcc-a2)

Names (3): _corpus: _corpus:phase:mn-ta:bcc-a2  
_tdb: _tdb:MnTa-14Wan.tdb:BCC_A2, tdb:MnTa-21Yan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): BCC_A2, type code %B, sha256 `ce5846ac254fa431…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MN% TA% : VA : !
~~~~

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): BCC_A2, type code %B, sha256 `76adf07bc5bd18ca…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MN% TA% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_
- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
_assessment that models this phase_

## C14_LAVES (Mn–Ta)

- Id: `phase:mn-ta:c14-laves`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MnTa-21Yan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2070.13 K, x(Ta) 0.30661–0.39902
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:c14-laves)

Names (2): _corpus: _corpus:phase:mn-ta:c14-laves  
_tdb: _tdb:MnTa-21Yan.tdb:C14_LAVES  


### TDB models of C14_LAVES (1): PHASE and CONSTITUENT statements as written

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): C14_LAVES, type code %, sha256 `76adf07bc5bd18ca…`

~~~~text
53: PHASE C14_LAVES % 2 2 1 !
54: CONST C14_LAVES : MN% TA : MN TA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_

## CBCC_A12 (Mn–Ta)

- Id: `phase:mn-ta:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1036.88 K, x(Ta) 0–0.01438
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:cbcc-a12)

Names (3): _corpus: _corpus:phase:mn-ta:cbcc-a12  
_tdb: _tdb:MnTa-14Wan.tdb:CBCC_A12, tdb:MnTa-21Yan.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): CBCC_A12, type code %A, sha256 `ce5846ac254fa431…`

~~~~text
46: PHASE CBCC_A12 %A 2 1 1 !
47: CONST CBCC_A12 : MN% TA : VA : !
~~~~

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): CBCC_A12, type code %A, sha256 `76adf07bc5bd18ca…`

~~~~text
43: PHASE CBCC_A12 %A 2 1 1 !
44: CONST CBCC_A12 : MN% TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_
- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
_assessment that models this phase_

## CUB_A13 (Mn–Ta)

- Id: `phase:mn-ta:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 970.44–1382.2 K, x(Ta) 0–0.00936
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:cub-a13)

Names (3): _corpus: _corpus:phase:mn-ta:cub-a13  
_tdb: _tdb:MnTa-14Wan.tdb:CUB_A13, tdb:MnTa-21Yan.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): CUB_A13, type code %, sha256 `ce5846ac254fa431…`

~~~~text
51: PHASE CUB_A13 % 2 1 1 !
52: CONST CUB_A13 : MN% TA : VA : !
~~~~

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): CUB_A13, type code %, sha256 `76adf07bc5bd18ca…`

~~~~text
48: PHASE CUB_A13 % 2 1 1 !
49: CONST CUB_A13 : MN% TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_
- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
_assessment that models this phase_

## FCC_A1 (Mn–Ta)

- Id: `phase:mn-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1347.37–1478.5 K, x(Ta) 0–0.01739
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:fcc-a1)

Names (3): _corpus: _corpus:phase:mn-ta:fcc-a1  
_tdb: _tdb:MnTa-14Wan.tdb:FCC_A1, tdb:MnTa-21Yan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): FCC_A1, type code %A, sha256 `ce5846ac254fa431…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MN% TA : VA : !
~~~~

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): FCC_A1, type code %A, sha256 `76adf07bc5bd18ca…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MN% TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_
- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
_assessment that models this phase_

## HCP_A3 (Mn–Ta)

- Id: `phase:mn-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:hcp-a3)

Names (3): _corpus: _corpus:phase:mn-ta:hcp-a3  
_tdb: _tdb:MnTa-14Wan.tdb:HCP_A3, tdb:MnTa-21Yan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): HCP_A3, type code %A, sha256 `ce5846ac254fa431…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MN TA : VA : !
~~~~

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): HCP_A3, type code %A, sha256 `76adf07bc5bd18ca…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MN TA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase_
- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
_assessment that models this phase_

## LIQUID (Mn–Ta)

- Id: `phase:mn-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1457.71–4000 K, x(Ta) 0–1
- Literature: 2 values (0 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:liquid)

Names (4): _corpus: _corpus:phase:mn-ta:liquid  
_paper: _paper:10.1016/j.jallcom.2021.158715:liquid  
_tdb: _tdb:MnTa-14Wan.tdb:LIQUID, tdb:MnTa-21Yan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): LIQUID, type code %, sha256 `ce5846ac254fa431…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MN TA : !
~~~~

[MnTa-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-21Yan.tdb): LIQUID, type code %, sha256 `76adf07bc5bd18ca…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MN TA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2021.158715](https://doi.org/10.1016/j.jallcom.2021.158715) Xinlin Yan, Pavel Brož, Jan Vřešťál, Jiří Vlach, Jiří Buršík, Martina Mazalová et al., On the constitution and thermodynamic modeling of the phase diagrams Nb-Mn and Ta-Mn, Journal of Alloys and Compounds 865, 158715 (2021).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
_assessment that models this phase_

## MN2TA_C14 (Mn–Ta)

- Id: `phase:mn-ta:mn2ta-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaastq and oqmd-19153, space group 194
- Stoichiometry: Mn 0.6667, Ta 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1939.38 K, x(Ta) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-ta:mn2ta-c14)

Names (4): _corpus: _corpus:phase:mn-ta:mn2ta-c14  
_mp: _mp:mp-aaaaastq  
_oqmd: _oqmd:oqmd-19153  
_tdb: _tdb:MnTa-14Wan.tdb:MN2TA_C14  


### TDB models of MN2TA_C14 (1): PHASE and CONSTITUENT statements as written

[MnTa-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/MnTa-14Wan.tdb): MN2TA_C14, type code %, sha256 `ce5846ac254fa431…`

~~~~text
56: PHASE MN2TA_C14 % 2 2 1 !
57: CONST MN2TA_C14 : MN : TA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111135](https://doi.org/10.3139/146.111135) C. Wang, C. Zhao, Z. Lin, X. Liu, Int J. Mater. Res., 105, 1179-90(2014).  
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
