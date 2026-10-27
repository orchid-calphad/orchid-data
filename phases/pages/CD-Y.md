# Cd–Y phases

> Cd–Y system: 10 phases (tier A 4, tier C 5, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-Y.html · Markdown: https://data.orchid-project.org/phases/pages/CD-Y.md

10 phases (tier A 4, tier C 5, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-Y) · [full JSON](https://data.orchid-project.org/phases/systems/CD-Y.json) · [Cd–Y system page](https://data.orchid-project.org/systems/CD-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Y system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-y-bcc-a2); _phase:cd-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1751.15–2499.9 K, x(Y) 0.99999–1 | 0 | 1 |
| [CD2Y](#phase-cd-y-cd2y); _phase:cd-y:cd2y_ | Cd2Ce · hP3 · P-3m1 (164) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1295.48 K, x(Y) 0.33333–0.33333 | 0 | 1 |
| [CD3Y](#phase-cd-y-cd3y); _phase:cd-y:cd3y_ | Cd3Er · oC16 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1079.67 K, x(Y) 0.25–0.25 | 0 | 1 |
| [CD45Y11](#phase-cd-y-cd45y11); _phase:cd-y:cd45y11_ | Cd45Sm11 · cF448 · F-43m (216) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1038.34 K, x(Y) 0.19643–0.19643 | 0 | 1 |
| [CD58Y13](#phase-cd-y-cd58y13); _phase:cd-y:cd58y13_ | Gd13Zn58 · hP142 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1008.97 K, x(Y) 0.1831–0.1831 | 0 | 1 |
| [CD6Y](#phase-cd-y-cd6y); _phase:cd-y:cd6y_ | Cd6Y · cI184 · Im-3 (204) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–992.18 K, x(Y) 0.14286–0.14286 | 0 | 1 |
| [CDY_B2](#phase-cd-y-cdy-b2); _phase:cd-y:cdy-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1495.45 K, x(Y) 0.5–0.5 | 0 | 1 |
| [FCC_A1](#phase-cd-y-fcc-a1); _phase:cd-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cd-y-hcp-a3); _phase:cd-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 0–1 | 0 | 1 |
| [LIQUID](#phase-cd-y-liquid); _phase:cd-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 593.5–2500 K, x(Y) 0–1 | 0 | 1 |

## BCC_A2 (Cd–Y)

- Id: `phase:cd-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1751.15–2499.9 K, x(Y) 0.99999–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-y:bcc-a2  
_tdb: _tdb:CdY-01Kur-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): BCC_A2, type code %B, sha256 `7e3a3e5fe387605f…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : CD Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## CD2Y (Cd–Y)

- Id: `phase:cd-y:cd2y`; status `assigned`
- Structure: Cd2Ce · hP3 · P-3m1 (164); type `st:cd2ce-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1295.48 K, x(Y) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:cd2y)

Names (2): _corpus: _corpus:phase:cd-y:cd2y  
_tdb: _tdb:CdY-01Kur-LB.tdb:CD2Y  


### TDB models of CD2Y (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): CD2Y, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
70: PHASE CD2Y % 2 2 1 !
71: CONST CD2Y : CD : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## CD3Y (Cd–Y)

- Id: `phase:cd-y:cd3y`; status `assigned`
- Structure: Cd3Er · oC16 · Cmcm (63); type `st:cd3er-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_6_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.7500, Y 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1079.67 K, x(Y) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:cd3y)

Names (2): _corpus: _corpus:phase:cd-y:cd3y  
_tdb: _tdb:CdY-01Kur-LB.tdb:CD3Y  


### TDB models of CD3Y (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): CD3Y, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
65: PHASE CD3Y % 2 3 1 !
66: CONST CD3Y : CD : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## CD45Y11 (Cd–Y)

- Id: `phase:cd-y:cd45y11`; status `assigned`
- Structure: Cd45Sm11 · cF448 · F-43m (216); type `st:cd45sm11-cf448`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8036, Y 0.1964
- Stability: stable in 1 of 1 calculated diagram(s): 300–1038.34 K, x(Y) 0.19643–0.19643
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:cd45y11)

Names (2): _corpus: _corpus:phase:cd-y:cd45y11  
_tdb: _tdb:CdY-01Kur-LB.tdb:CD45Y11  


### TDB models of CD45Y11 (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): CD45Y11, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
60: PHASE CD45Y11 % 2 45 11 !
61: CONST CD45Y11 : CD : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## CD58Y13 (Cd–Y)

- Id: `phase:cd-y:cd58y13`; status `assigned`
- Structure: Gd13Zn58 · hP142 · P6_3/mmc (194); type `st:gd13zn58-hp142`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8169, Y 0.1831
- Stability: stable in 1 of 1 calculated diagram(s): 300–1008.97 K, x(Y) 0.1831–0.1831
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:cd58y13)

Names (2): _corpus: _corpus:phase:cd-y:cd58y13  
_tdb: _tdb:CdY-01Kur-LB.tdb:CD58Y13  


### TDB models of CD58Y13 (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): CD58Y13, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
55: PHASE CD58Y13 % 2 58 13 !
56: CONST CD58Y13 : CD : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## CD6Y (Cd–Y)

- Id: `phase:cd-y:cd6y`; status `assigned`
- Structure: Cd6Y · cI184 · Im-3 (204); type `st:cd6y-ci184`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.8571, Y 0.1429
- Stability: stable in 1 of 1 calculated diagram(s): 300–992.18 K, x(Y) 0.14286–0.14286
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:cd6y)

Names (2): _corpus: _corpus:phase:cd-y:cd6y  
_tdb: _tdb:CdY-01Kur-LB.tdb:CD6Y  


### TDB models of CD6Y (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): CD6Y, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
50: PHASE CD6Y % 2 6 1 !
51: CONST CD6Y : CD : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## CDY_B2 (Cd–Y)

- Id: `phase:cd-y:cdy-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.5000, Y 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1495.45 K, x(Y) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:cdy-b2)

Names (2): _corpus: _corpus:phase:cd-y:cdy-b2  
_tdb: _tdb:CdY-01Kur-LB.tdb:CDY_B2  


### TDB models of CDY_B2 (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): CDY_B2, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
75: PHASE CDY_B2 % 2 1 1 !
76: CONST CDY_B2 : CD : Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## FCC_A1 (Cd–Y)

- Id: `phase:cd-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-y:fcc-a1  
_tdb: _tdb:CdY-01Kur-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): FCC_A1, type code %A, sha256 `7e3a3e5fe387605f…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : CD Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## HCP_A3 (Cd–Y)

- Id: `phase:cd-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1751.15 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:hcp-a3)

Names (2): _corpus: _corpus:phase:cd-y:hcp-a3  
_tdb: _tdb:CdY-01Kur-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): HCP_A3, type code %A, sha256 `7e3a3e5fe387605f…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CD% Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
_assessment that models this phase_

## LIQUID (Cd–Y)

- Id: `phase:cd-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 593.5–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-y:liquid)

Names (2): _corpus: _corpus:phase:cd-y:liquid  
_tdb: _tdb:CdY-01Kur-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdY-01Kur-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdY-01Kur-LB.tdb): LIQUID, type code %, sha256 `7e3a3e5fe387605f…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : CD Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497101770338707](https://doi.org/10.1361/105497101770338707) Masaki Kurata, Yoshiharu Sakamura, Thermodynamic assessment of systems of actinide or rare earth with Cd, JPE 22, 232-240 (2001).  
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
