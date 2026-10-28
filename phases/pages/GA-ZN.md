# Ga–Zn phases

> Ga–Zn system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/GA-ZN.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/GA-ZN.json) · [Ga–Zn system page](https://data.orchid-project.org/systems/GA-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-zn-a11-orthorhombic); _phase:ga-zn:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 298.92–302.91 K, x(Zn) 0–0 | 5 | 2 |
| [BCC_A2](#phase-ga-zn-bcc-a2); _phase:ga-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ga-zn-fcc-a1); _phase:ga-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-ga-zn-hcp-a3); _phase:ga-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–692.68 K, x(Zn) 0.97407–1 | 5 | 2 |
| [LIQUID](#phase-ga-zn-liquid); _phase:ga-zn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 298.92–2500 K, x(Zn) 0–1 | 44 | 2 |

## ORTHORHOMBIC_A11 (Ga–Zn)

- Id: `phase:ga-zn:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 298.92–302.91 K, x(Zn) 0–0
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-zn:a11-orthorhombic)

Names (4): _corpus: _corpus:phase:ga-zn:a11-orthorhombic  
_paper: _paper:10.1007/bf02841587:(Ga)  
_tdb: _tdb:GaZn-00Mat.tdb:ORTHORHOMBIC_A11, tdb:GaZn-90Dut-LB.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[GaZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-00Mat.tdb): ORTHORHOMBIC_A11, type code %, sha256 `688443414f166727…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaZn-90Dut-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-90Dut-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `8ccd9ff21da57f9d…`

~~~~text
41: PHASE ORTHORHOMBIC_A11 % 1 1 !
42: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02841587](https://doi.org/10.1007/BF02841587) J. Dutkiewicz, Z. Moser, Z. Zabdyr, D.D. Gohil, T.G. Chart, I. Ansara, C. Girard, Bull. Alloy Phase Diag., 11, 77-82(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## BCC_A2 (Ga–Zn)

- Id: `phase:ga-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:ga-zn:bcc-a2  
_tdb: _tdb:GaZn-00Mat.tdb:BCC_A2, tdb:GaZn-90Dut-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GaZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-00Mat.tdb): BCC_A2, type code %B, sha256 `688443414f166727…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GA ZN : VA : !
~~~~

[GaZn-90Dut-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-90Dut-LB.tdb): BCC_A2, type code %B, sha256 `8ccd9ff21da57f9d…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GA ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02841587](https://doi.org/10.1007/BF02841587) J. Dutkiewicz, Z. Moser, Z. Zabdyr, D.D. Gohil, T.G. Chart, I. Ansara, C. Girard, Bull. Alloy Phase Diag., 11, 77-82(1990).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## FCC_A1 (Ga–Zn)

- Id: `phase:ga-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-zn:fcc-a1)

Names (3): _corpus: _corpus:phase:ga-zn:fcc-a1  
_tdb: _tdb:GaZn-00Mat.tdb:FCC_A1, tdb:GaZn-90Dut-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GaZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-00Mat.tdb): FCC_A1, type code %A, sha256 `688443414f166727…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GA ZN : VA : !
~~~~

[GaZn-90Dut-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-90Dut-LB.tdb): FCC_A1, type code %A, sha256 `8ccd9ff21da57f9d…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GA ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02841587](https://doi.org/10.1007/BF02841587) J. Dutkiewicz, Z. Moser, Z. Zabdyr, D.D. Gohil, T.G. Chart, I. Ansara, C. Girard, Bull. Alloy Phase Diag., 11, 77-82(1990).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## HCP_A3 (Ga–Zn)

- Id: `phase:ga-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–692.68 K, x(Zn) 0.97407–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-zn:hcp-a3)

Names (4): _corpus: _corpus:phase:ga-zn:hcp-a3  
_paper: _paper:10.1007/bf02841587:(Zn)  
_tdb: _tdb:GaZn-00Mat.tdb:HCP_A3, tdb:GaZn-90Dut-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GaZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-00Mat.tdb): HCP_A3, type code %A, sha256 `688443414f166727…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GA ZN : VA: !
~~~~

[GaZn-90Dut-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-90Dut-LB.tdb): HCP_A3, type code %A, sha256 `8ccd9ff21da57f9d…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : GA ZN : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02841587](https://doi.org/10.1007/BF02841587) J. Dutkiewicz, Z. Moser, Z. Zabdyr, D.D. Gohil, T.G. Chart, I. Ansara, C. Girard, Bull. Alloy Phase Diag., 11, 77-82(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
_assessment that models this phase_

## LIQUID (Ga–Zn)

- Id: `phase:ga-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 298.92–2500 K, x(Zn) 0–1
- Literature: 44 values (44 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-zn:liquid)

Names (4): _corpus: _corpus:phase:ga-zn:liquid  
_paper: _paper:10.1007/bf02841587:L  
_tdb: _tdb:GaZn-00Mat.tdb:LIQUID, tdb:GaZn-90Dut-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GaZn-00Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-00Mat.tdb): LIQUID, type code %, sha256 `688443414f166727…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GA ZN : !
~~~~

[GaZn-90Dut-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaZn-90Dut-LB.tdb): LIQUID, type code %, sha256 `8ccd9ff21da57f9d…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GA ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02841587](https://doi.org/10.1007/BF02841587) J. Dutkiewicz, Z. Moser, Z. Zabdyr, D.D. Gohil, T.G. Chart, I. Ansara, C. Girard, Bull. Alloy Phase Diag., 11, 77-82(1990).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(01)00004-9](https://doi.org/10.1016/S0364-5916%2801%2900004-9) M. Mathon, K. Jardet, E. Aragon, P. Satre, A. Sebaoun, Calphad, 24, 253-84(2000).  
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
