# Nd–Y phases

> Nd–Y system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ND-Y.html · Markdown: https://data.orchid-project.org/phases/pages/ND-Y.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ND-Y) · [full JSON](https://data.orchid-project.org/phases/systems/ND-Y.json) · [Nd–Y system page](https://data.orchid-project.org/systems/ND-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/ND-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nd–Y system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nd-y-bcc-a2); _phase:nd-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1127.88–2498.92 K, x(Y) 0–1 | 0 | 1 |
| [DHCP](#phase-nd-y-dhcp-a3); _phase:nd-y:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1308.58 K, x(Y) 0–0.3464 | 0 | 1 |
| [FCC_A1](#phase-nd-y-fcc-a1); _phase:nd-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-nd-y-hcp-a3); _phase:nd-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 0.34906–1 | 0 | 1 |
| [LIQUID](#phase-nd-y-liquid); _phase:nd-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1289–2500 K, x(Y) 0–1 | 0 | 1 |
| [ND2Y_C19](#phase-nd-y-nd2y-c19); _phase:nd-y:nd2y-c19_ | CdCl2 · C19 · hR3 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.54 K, x(Y) 0.32305–0.35945 | 0 | 1 |

## BCC_A2 (Nd–Y)

- Id: `phase:nd-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1127.88–2498.92 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-y:bcc-a2)

Names (2): _corpus: _corpus:phase:nd-y:bcc-a2  
_tdb: _tdb:NdY-08Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NdY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdY-08Guo.tdb): BCC_A2, type code %B, sha256 `5b90a7eae7aa25ae…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : ND% Y% : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_

## DHCP (Nd–Y)

- Id: `phase:nd-y:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1308.58 K, x(Y) 0–0.3464
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-y:dhcp-a3)

Names (2): _corpus: _corpus:phase:nd-y:dhcp-a3  
_tdb: _tdb:NdY-08Guo.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[NdY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdY-08Guo.tdb): DHCP, type code %A, sha256 `5b90a7eae7aa25ae…`

~~~~text
40: PHASE DHCP %A 1 1 !
41: CONST DHCP : ND% Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_

## FCC_A1 (Nd–Y)

- Id: `phase:nd-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-y:fcc-a1)

Names (2): _corpus: _corpus:phase:nd-y:fcc-a1  
_tdb: _tdb:NdY-08Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NdY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdY-08Guo.tdb): FCC_A1, type code %A, sha256 `5b90a7eae7aa25ae…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : ND Y : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_

## HCP_A3 (Nd–Y)

- Id: `phase:nd-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 0.34906–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-y:hcp-a3)

Names (2): _corpus: _corpus:phase:nd-y:hcp-a3  
_tdb: _tdb:NdY-08Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NdY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdY-08Guo.tdb): HCP_A3, type code %A, sha256 `5b90a7eae7aa25ae…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : ND Y% : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_

## LIQUID (Nd–Y)

- Id: `phase:nd-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1289–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-y:liquid)

Names (2): _corpus: _corpus:phase:nd-y:liquid  
_tdb: _tdb:NdY-08Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NdY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdY-08Guo.tdb): LIQUID, type code %, sha256 `5b90a7eae7aa25ae…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : ND Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_

## ND2Y_C19 (Nd–Y)

- Id: `phase:nd-y:nd2y-c19`; status `assigned`
- Structure: CdCl2 · C19 · hR3 · R-3m (166); type `st:c19-cdcl2-hr3`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in NdY-08Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.54 K, x(Y) 0.32305–0.35945
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-y:nd2y-c19)

Names (2): _corpus: _corpus:phase:nd-y:nd2y-c19  
_tdb: _tdb:NdY-08Guo.tdb:ND2Y_C19  


### TDB models of ND2Y_C19 (1): PHASE and CONSTITUENT statements as written

[NdY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/NdY-08Guo.tdb): ND2Y_C19, type code %, sha256 `5b90a7eae7aa25ae…`

~~~~text
45: PHASE ND2Y_C19 % 2 2 1 !
46: CONST ND2Y_C19 : ND% Y : ND Y% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
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
