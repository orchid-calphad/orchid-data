# H–Rh phases

> H–Rh system: 6 phases (tier A 3, liquid 1, gas 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-RH.html · Markdown: https://data.orchid-project.org/phases/pages/H-RH.md

6 phases (tier A 3, liquid 1, gas 2); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-RH) · [full JSON](https://data.orchid-project.org/phases/systems/H-RH.json) · [H–Rh system page](https://data.orchid-project.org/systems/H-RH.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-RH.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Rh system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-rh-bcc-a2); _phase:h-rh:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-h-rh-fcc-a1); _phase:h-rh:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2691.99 K, x(H) 0–0.0007 | 0 | 1 |
| [GAS](#phase-h-rh-gas); _phase:h-rh:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(H) 1–1 | 0 | 1 |
| [H2GAS](#phase-h-rh-h2gas); _phase:h-rh:h2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 301.11–1091.11 K, x(H) 1–1 | 0 | 1 |
| [HCP_A3](#phase-h-rh-hcp-a3); _phase:h-rh:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-h-rh-liquid); _phase:h-rh:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2230.23–4000 K, x(H) 0–0.00509 | 0 | 1 |

## BCC_A2 (H–Rh)

- Id: `phase:h-rh:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Rh 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-rh:bcc-a2)

Names (2): _corpus: _corpus:phase:h-rh:bcc-a2  
_tdb: _tdb:RhH-10Jou.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[RhH-10Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/RhH-10Jou.tdb): BCC_A2, type code %B, sha256 `11908978f20a818d…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : RH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2010.01.006](https://doi.org/10.1016/j.ijhydene.2010.01.006) J.-M. Joubert, A Calphad-type equation of state for hydrogen gas and its application to the assessment of Rh–H system, International Journal of Hydrogen Energy 35, 2104-2111 (2010).  
_assessment that models this phase_

## FCC_A1 (H–Rh)

- Id: `phase:h-rh:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2691.99 K, x(H) 0–0.0007
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-rh:fcc-a1)

Names (2): _corpus: _corpus:phase:h-rh:fcc-a1  
_tdb: _tdb:RhH-10Jou.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[RhH-10Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/RhH-10Jou.tdb): FCC_A1, type code %A, sha256 `11908978f20a818d…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : RH : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2010.01.006](https://doi.org/10.1016/j.ijhydene.2010.01.006) J.-M. Joubert, A Calphad-type equation of state for hydrogen gas and its application to the assessment of Rh–H system, International Journal of Hydrogen Energy 35, 2104-2111 (2010).  
_assessment that models this phase_

## GAS (H–Rh)

- Id: `phase:h-rh:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-rh:gas)

Names (2): _corpus: _corpus:phase:h-rh:gas  
_tdb: _tdb:RhH-10Jou.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[RhH-10Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/RhH-10Jou.tdb): GAS, type code %, sha256 `11908978f20a818d…`

~~~~text
49: PHASE GAS:G % 1 1 !
50: CONST GAS:G : H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2010.01.006](https://doi.org/10.1016/j.ijhydene.2010.01.006) J.-M. Joubert, A Calphad-type equation of state for hydrogen gas and its application to the assessment of Rh–H system, International Journal of Hydrogen Energy 35, 2104-2111 (2010).  
_assessment that models this phase_

## H2GAS (H–Rh)

- Id: `phase:h-rh:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 301.11–1091.11 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-rh:h2gas)

Names (2): _corpus: _corpus:phase:h-rh:h2gas  
_tdb: _tdb:RhH-10Jou.tdb:H2GAS  


### TDB models of H2GAS (1): PHASE and CONSTITUENT statements as written

[RhH-10Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/RhH-10Jou.tdb): H2GAS, type code %, sha256 `11908978f20a818d…`

~~~~text
52: PHASE H2GAS % 1 1 !
53: CONST H2GAS : H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2010.01.006](https://doi.org/10.1016/j.ijhydene.2010.01.006) J.-M. Joubert, A Calphad-type equation of state for hydrogen gas and its application to the assessment of Rh–H system, International Journal of Hydrogen Energy 35, 2104-2111 (2010).  
_assessment that models this phase_

## HCP_A3 (H–Rh)

- Id: `phase:h-rh:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Rh 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-rh:hcp-a3)

Names (2): _corpus: _corpus:phase:h-rh:hcp-a3  
_tdb: _tdb:RhH-10Jou.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[RhH-10Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/RhH-10Jou.tdb): HCP_A3, type code %A, sha256 `11908978f20a818d…`

~~~~text
46: PHASE HCP_A3 %A 2 1 2 !
47: CONST HCP_A3 : RH : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2010.01.006](https://doi.org/10.1016/j.ijhydene.2010.01.006) J.-M. Joubert, A Calphad-type equation of state for hydrogen gas and its application to the assessment of Rh–H system, International Journal of Hydrogen Energy 35, 2104-2111 (2010).  
_assessment that models this phase_

## LIQUID (H–Rh)

- Id: `phase:h-rh:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2230.23–4000 K, x(H) 0–0.00509
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-rh:liquid)

Names (2): _corpus: _corpus:phase:h-rh:liquid  
_tdb: _tdb:RhH-10Jou.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[RhH-10Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/RhH-10Jou.tdb): LIQUID, type code %, sha256 `11908978f20a818d…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : H RH : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijhydene.2010.01.006](https://doi.org/10.1016/j.ijhydene.2010.01.006) J.-M. Joubert, A Calphad-type equation of state for hydrogen gas and its application to the assessment of Rh–H system, International Journal of Hydrogen Energy 35, 2104-2111 (2010).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
