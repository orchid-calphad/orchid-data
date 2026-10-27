# H–Nd phases

> H–Nd system: 7 phases (tier A 3, tier C 1, liquid 1, gas 1, unresolved_no_candidates 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-ND.html · Markdown: https://data.orchid-project.org/phases/pages/H-ND.md

7 phases (tier A 3, tier C 1, liquid 1, gas 1, unresolved_no_candidates 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-ND) · [full JSON](https://data.orchid-project.org/phases/systems/H-ND.json) · [Markdown](https://data.orchid-project.org/phases/pages/H-ND.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Nd system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-nd-bcc-a2); _phase:h-nd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1086.59–2361.45 K, x(H) 0–0.54516 | 0 | 1 |
| [DHCP](#phase-h-nd-dhcp-a3); _phase:h-nd:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1203 K, x(H) 0–0.17182 | 0 | 1 |
| [FCC_A1](#phase-h-nd-fcc-a1); _phase:h-nd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GAS](#phase-h-nd-gas); _phase:h-nd:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 0.9817–1 | 0 | 1 |
| [LIQUID](#phase-h-nd-liquid); _phase:h-nd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1215.19–2500 K, x(H) 0–0.00503 | 0 | 1 |
| [NDH_GAMMA](#phase-h-nd-ndh-gamma); _phase:h-nd:ndh-gamma_ |  | unresolved_no_candidates | stable in 1 of 1 calculated diagram(s): 947.8–1159.89 K, x(H) 0.18876–0.33765 | 0 | 1 |
| [NDH2](#phase-h-nd-ndh2); _phase:h-nd:ndh2_ | CeH3 · cF44 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1373.17 K, x(H) 0.65323–0.66844 | 0 | 1 |

## BCC_A2 (H–Nd)

- Id: `phase:h-nd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1086.59–2361.45 K, x(H) 0–0.54516
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:bcc-a2)

Names (2): _corpus: _corpus:phase:h-nd:bcc-a2  
_tdb: _tdb:NdH-15Luo.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): BCC_A2, type code %B, sha256 `f14a165b6109893d…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : ND : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

## DHCP (H–Nd)

- Id: `phase:h-nd:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1203 K, x(H) 0–0.17182
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:dhcp-a3)

Names (2): _corpus: _corpus:phase:h-nd:dhcp-a3  
_tdb: _tdb:NdH-15Luo.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): DHCP, type code %, sha256 `f14a165b6109893d…`

~~~~text
40: PHASE DHCP % 2 1 2 !
41: CONST DHCP : ND : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

## FCC_A1 (H–Nd)

- Id: `phase:h-nd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:fcc-a1)

Names (2): _corpus: _corpus:phase:h-nd:fcc-a1  
_tdb: _tdb:NdH-15Luo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): FCC_A1, type code %A, sha256 `f14a165b6109893d…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : ND : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

## GAS (H–Nd)

- Id: `phase:h-nd:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 0.9817–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:gas)

Names (2): _corpus: _corpus:phase:h-nd:gas  
_tdb: _tdb:NdH-15Luo.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): GAS, type code %, sha256 `f14a165b6109893d…`

~~~~text
54: PHASE GAS:G % 1 1 !
55: CONST GAS:G : ND H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

## LIQUID (H–Nd)

- Id: `phase:h-nd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1215.19–2500 K, x(H) 0–0.00503
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:liquid)

Names (2): _corpus: _corpus:phase:h-nd:liquid  
_tdb: _tdb:NdH-15Luo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): LIQUID, type code %, sha256 `f14a165b6109893d…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : H ND : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

## NDH_GAMMA (H–Nd)

- Id: `phase:h-nd:ndh-gamma`; status `unresolved_no_candidates`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Stability: stable in 1 of 1 calculated diagram(s): 947.8–1159.89 K, x(H) 0.18876–0.33765
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:ndh-gamma)

Names (2): _corpus: _corpus:phase:h-nd:ndh-gamma  
_tdb: _tdb:NdH-15Luo.tdb:NDH_GAMMA  


### TDB models of NDH_GAMMA (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): NDH_GAMMA, type code %, sha256 `f14a165b6109893d…`

~~~~text
45: PHASE NDH_GAMMA % 2 1 2 !
46: CONST NDH_GAMMA : ND : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

## NDH2 (H–Nd)

- Id: `phase:h-nd:ndh2`; status `assigned`
- Structure: CeH3 · cF44 · Fm-3m (225); type `st:ceh3-cf44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1373.17 K, x(H) 0.65323–0.66844
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nd:ndh2)

Names (2): _corpus: _corpus:phase:h-nd:ndh2  
_tdb: _tdb:NdH-15Luo.tdb:NDH2  


### TDB models of NDH2 (1): PHASE and CONSTITUENT statements as written

[NdH-15Luo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdH-15Luo.tdb): NDH2, type code %, sha256 `f14a165b6109893d…`

~~~~text
51: PHASE NDH2 % 3 1 2 1 !
52: CONST NDH2 : ND : H VA : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.10.009](https://doi.org/10.1016/j.calphad.2015.10.009) Q. Luo, S.-L. Chen, J.-Y. Zhang, L. Li, K.-C. Chou, Q. Li, Calphad, 51, 282-91(2015).  
_assessment that models this phase_

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
