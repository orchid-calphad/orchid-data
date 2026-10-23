# H–Pd phases

> H–Pd system: 5 phases (tier A 3, liquid 1, gas 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-PD.html · Markdown: https://data.orchid-project.org/phases/pages/H-PD.md

5 phases (tier A 3, liquid 1, gas 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-PD) · [full JSON](https://data.orchid-project.org/phases/systems/H-PD.json) · [H–Pd system page](https://data.orchid-project.org/systems/H-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Pd system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-pd-bcc-a2); _phase:h-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-h-pd-fcc-a1); _phase:h-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1837 K, x(H) 0–0.42015 | 0 | 2 |
| [GAS](#phase-h-pd-gas); _phase:h-pd:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0.96914–1 | 0 | 2 |
| [HCP_A3](#phase-h-pd-hcp-a3); _phase:h-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-h-pd-liquid); _phase:h-pd:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1827.65–2500 K, x(H) 0–0.00919 | 0 | 2 |

## BCC_A2 (H–Pd)

- Id: `phase:h-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-pd:bcc-a2)

Names (3): _corpus: _corpus:phase:h-pd:bcc-a2  
_tdb: _tdb:PdH-07Hua.tdb:BCC_A2, tdb:PdH-09Jou.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PdH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-07Hua.tdb): BCC_A2, type code %B, sha256 `a5ce3026a64660d7…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : PD : VA : !
~~~~

[PdH-09Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-09Jou.tdb): BCC_A2, type code %B, sha256 `34eb31f6fe65cd0f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : PD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.09.021](https://doi.org/10.1016/j.jnucmat.2009.09.021) J.-M. Joubert, S. Thiébaut, Thermodynamic assessment of the Pd–H–D–T system, Journal of Nuclear Materials 395, 79-88 (2009).  
_assessment that models this phase_

## FCC_A1 (H–Pd)

- Id: `phase:h-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1837 K, x(H) 0–0.42015
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-pd:fcc-a1)

Names (3): _corpus: _corpus:phase:h-pd:fcc-a1  
_tdb: _tdb:PdH-07Hua.tdb:FCC_A1, tdb:PdH-09Jou.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PdH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-07Hua.tdb): FCC_A1, type code %A, sha256 `a5ce3026a64660d7…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : PD% : H VA% : !
~~~~

[PdH-09Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-09Jou.tdb): FCC_A1, type code %A, sha256 `34eb31f6fe65cd0f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : PD% : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.09.021](https://doi.org/10.1016/j.jnucmat.2009.09.021) J.-M. Joubert, S. Thiébaut, Thermodynamic assessment of the Pd–H–D–T system, Journal of Nuclear Materials 395, 79-88 (2009).  
_assessment that models this phase_

## GAS (H–Pd)

- Id: `phase:h-pd:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0.96914–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-pd:gas)

Names (3): _corpus: _corpus:phase:h-pd:gas  
_tdb: _tdb:PdH-07Hua.tdb:GAS, tdb:PdH-09Jou.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[PdH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-07Hua.tdb): GAS, type code %, sha256 `a5ce3026a64660d7…`

~~~~text
42: PHASE GAS:G % 1 1 !
43: CONST GAS:G : H H2 PD : !
~~~~

[PdH-09Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-09Jou.tdb): GAS, type code %, sha256 `34eb31f6fe65cd0f…`

~~~~text
43: PHASE GAS:G % 1 1 !
44: CONST GAS:G : H H2 PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.09.021](https://doi.org/10.1016/j.jnucmat.2009.09.021) J.-M. Joubert, S. Thiébaut, Thermodynamic assessment of the Pd–H–D–T system, Journal of Nuclear Materials 395, 79-88 (2009).  
_assessment that models this phase_

## HCP_A3 (H–Pd)

- Id: `phase:h-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-pd:hcp-a3)

Names (3): _corpus: _corpus:phase:h-pd:hcp-a3  
_tdb: _tdb:PdH-07Hua.tdb:HCP_A3, tdb:PdH-09Jou.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PdH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-07Hua.tdb): HCP_A3, type code %A, sha256 `a5ce3026a64660d7…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : PD : VA : !
~~~~

[PdH-09Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-09Jou.tdb): HCP_A3, type code %A, sha256 `34eb31f6fe65cd0f…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : PD : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.09.021](https://doi.org/10.1016/j.jnucmat.2009.09.021) J.-M. Joubert, S. Thiébaut, Thermodynamic assessment of the Pd–H–D–T system, Journal of Nuclear Materials 395, 79-88 (2009).  
_assessment that models this phase_

## LIQUID (H–Pd)

- Id: `phase:h-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1827.65–2500 K, x(H) 0–0.00919
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-pd:liquid)

Names (3): _corpus: _corpus:phase:h-pd:liquid  
_tdb: _tdb:PdH-07Hua.tdb:LIQUID, tdb:PdH-09Jou.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PdH-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-07Hua.tdb): LIQUID, type code %, sha256 `a5ce3026a64660d7…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : H PD : !
~~~~

[PdH-09Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/PdH-09Jou.tdb): LIQUID, type code %, sha256 `34eb31f6fe65cd0f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : H PD : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2007.02.002](https://doi.org/10.1016/j.calphad.2007.02.002) Weiming Huang, Susanne M. Opalka, Da Wang, Ted B. Flanagan, Thermodynamic modelling of the Cu–Pd–H system, Calphad 31, 315-329 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2009.09.021](https://doi.org/10.1016/j.jnucmat.2009.09.021) J.-M. Joubert, S. Thiébaut, Thermodynamic assessment of the Pd–H–D–T system, Journal of Nuclear Materials 395, 79-88 (2009).  
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
