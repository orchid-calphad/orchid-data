# Al–Am phases

> Al–Am system: 10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-AM.html · Markdown: https://data.orchid-project.org/phases/pages/AL-AM.md

10 phases (tier A 7, tier C 1, liquid 1, needs_review 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-AM) · [full JSON](https://data.orchid-project.org/phases/systems/AL-AM.json) · [Al–Am system page](https://data.orchid-project.org/systems/AL-AM.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-AM.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Am system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AL2AM_C15](#phase-al-am-al2am-c15); _phase:al-am:al2am-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1876.11 K, x(Am) 0.33333–0.33333 | 0 | 1 |
| [AL3AM_L12](#phase-al-am-al3am-l12); _phase:al-am:al3am-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1635.59 K, x(Am) 0.25–0.25 | 0 | 1 |
| [AL4AM_D1B](#phase-al-am-al4am-d1b); _phase:al-am:al4am-d1b_ | Al4U · D1_b · oI20 · Imma (74) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1203.36 K, x(Am) 0.2–0.2 | 0 | 1 |
| [ALAM](#phase-al-am-alam); _phase:al-am:alam_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 500–1030.05 K, x(Am) 0.5–0.5 | 0 | 1 |
| [ALAM3](#phase-al-am-alam3); _phase:al-am:alam3_ | Pb3Sr · tP4 · P4/mmm (123) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–978.13 K, x(Am) 0.75–0.75 | 0 | 1 |
| [BCC_A2](#phase-al-am-bcc-a2); _phase:al-am:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1350.05–2499.13 K, x(Am) 0.99989–1 | 0 | 1 |
| [DHCP](#phase-al-am-dhcp-a3); _phase:al-am:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1348.13 K, x(Am) 1–1 | 0 | 1 |
| [FCC_A1](#phase-al-am-fcc-a1); _phase:al-am:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1354.74 K, x(Am) 0–1 | 0 | 1 |
| [HCP_A3](#phase-al-am-hcp-a3); _phase:al-am:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-al-am-liquid); _phase:al-am:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 911.76–2500 K, x(Am) 0–1 | 0 | 1 |

## AL2AM_C15 (Al–Am)

- Id: `phase:al-am:al2am-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.6667, Am 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1876.11 K, x(Am) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:al2am-c15)

Names (2): _corpus: _corpus:phase:al-am:al2am-c15  
_tdb: _tdb:AlAm-16Per.tdb:AL2AM_C15  


### TDB models of AL2AM_C15 (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): AL2AM_C15, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
59: PHASE AL2AM_C15 % 2 2 1 !
60: CONST AL2AM_C15 : AL : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## AL3AM_L12 (Al–Am)

- Id: `phase:al-am:al3am-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.7500, Am 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1635.59 K, x(Am) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:al3am-l12)

Names (2): _corpus: _corpus:phase:al-am:al3am-l12  
_tdb: _tdb:AlAm-16Per.tdb:AL3AM_L12  


### TDB models of AL3AM_L12 (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): AL3AM_L12, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
54: PHASE AL3AM_L12 % 2 3 1 !
55: CONST AL3AM_L12 : AL : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## AL4AM_D1B (Al–Am)

- Id: `phase:al-am:al4am-d1b`; status `assigned`
- Structure: Al4U · D1_b · oI20 · Imma (74); type `st:d1-b-al4u-oi20`; tier A: standard phase name; confidence high
- Stoichiometry: Al 0.8000, Am 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1203.36 K, x(Am) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:al4am-d1b)

Names (2): _corpus: _corpus:phase:al-am:al4am-d1b  
_tdb: _tdb:AlAm-16Per.tdb:AL4AM_D1B  


### TDB models of AL4AM_D1B (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): AL4AM_D1B, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
49: PHASE AL4AM_D1B % 2 4 1 !
50: CONST AL4AM_D1B : AL : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## ALAM (Al–Am)

- Id: `phase:al-am:alam`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): AlPu · cI58 — Hallstedt 2025 mmc2 row for ALAM: AlAm
- Candidate (tdb_comment):  — AlAm-16Per.tdb: 'Prototype AlPu (cI58)'
- Stoichiometry: Al 0.5000, Am 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 500–1030.05 K, x(Am) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:alam)

Names (2): _corpus: _corpus:phase:al-am:alam  
_tdb: _tdb:AlAm-16Per.tdb:ALAM  


### TDB models of ALAM (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): ALAM, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
64: PHASE ALAM % 2 1 1 !
65: CONST ALAM : AL : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## ALAM3 (Al–Am)

- Id: `phase:al-am:alam3`; status `assigned`
- Structure: Pb3Sr · tP4 · P4/mmm (123); type `st:pb3sr-tp4`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Al 0.2500, Am 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–978.13 K, x(Am) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:alam3)

Names (2): _corpus: _corpus:phase:al-am:alam3  
_tdb: _tdb:AlAm-16Per.tdb:ALAM3  


### TDB models of ALAM3 (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): ALAM3, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
69: PHASE ALAM3 % 2 1 3 !
70: CONST ALAM3 : AL : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## BCC_A2 (Al–Am)

- Id: `phase:al-am:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1350.05–2499.13 K, x(Am) 0.99989–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:bcc-a2)

Names (2): _corpus: _corpus:phase:al-am:bcc-a2  
_tdb: _tdb:AlAm-16Per.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): BCC_A2, type code %B, sha256 `a017cb6517ba77cb…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL AM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## DHCP (Al–Am)

- Id: `phase:al-am:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Am 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1348.13 K, x(Am) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:dhcp-a3)

Names (2): _corpus: _corpus:phase:al-am:dhcp-a3  
_tdb: _tdb:AlAm-16Per.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): DHCP, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
44: PHASE DHCP % 1 1 !
45: CONST DHCP : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## FCC_A1 (Al–Am)

- Id: `phase:al-am:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1354.74 K, x(Am) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:fcc-a1)

Names (2): _corpus: _corpus:phase:al-am:fcc-a1  
_tdb: _tdb:AlAm-16Per.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): FCC_A1, type code %A, sha256 `a017cb6517ba77cb…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL% AM% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## HCP_A3 (Al–Am)

- Id: `phase:al-am:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Al 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:hcp-a3)

Names (2): _corpus: _corpus:phase:al-am:hcp-a3  
_tdb: _tdb:AlAm-16Per.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): HCP_A3, type code %A, sha256 `a017cb6517ba77cb…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
_assessment that models this phase_

## LIQUID (Al–Am)

- Id: `phase:al-am:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 911.76–2500 K, x(Am) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-am:liquid)

Names (2): _corpus: _corpus:phase:al-am:liquid  
_tdb: _tdb:AlAm-16Per.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AlAm-16Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AlAm-16Per.tdb): LIQUID, type code %, sha256 `a017cb6517ba77cb…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jnucmat.2016.09.012](https://doi.org/10.1016/j.jnucmat.2016.09.012) A. Perron, P.E.A. Turchi, A. Landa, B. Oudot, B. Ravat, F. Delaunay, Thermodynamic assessments and inter-relationships between systems involving Al, Am, Ga, Pu, and U, Journal of Nuclear Materials 482, 187-200 (2016).  
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
