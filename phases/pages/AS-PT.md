# As–Pt phases

> As–Pt system: 7 phases (tier A 5, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AS-PT.html · Markdown: https://data.orchid-project.org/phases/pages/AS-PT.md

7 phases (tier A 5, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AS-PT) · [full JSON](https://data.orchid-project.org/phases/systems/AS-PT.json) · [As–Pt system page](https://data.orchid-project.org/systems/AS-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/AS-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the As–Pt system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-as-pt-a7-rhombohedral); _phase:as-pt:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–888.4 K, x(As) 1–1 | 1 | 1 |
| [BCC_A2](#phase-as-pt-bcc-a2); _phase:as-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-as-pt-fcc-a1); _phase:as-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2048.36 K, x(As) 0–5e-05 | 3 | 1 |
| [GAS](#phase-as-pt-gas); _phase:as-pt:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 888.4–2500 K, x(As) 1–1 | 0 | 1 |
| [HCP_A3](#phase-as-pt-hcp-a3); _phase:as-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-as-pt-liquid); _phase:as-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 873.36–2500 K, x(As) 0–0.62307 | 6 | 1 |
| [PTAS2_C2](#phase-as-pt-ptas2-c2); _phase:as-pt:ptas2-c2_ | beta-FeS2 · C2 · cP12 · Pa-3 (205) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1735.83 K, x(As) 0.66667–0.66667 | 6 | 1 |

## RHOMBOHEDRAL_A7 (As–Pt)

- Id: `phase:as-pt:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: As 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–888.4 K, x(As) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:as-pt:a7-rhombohedral, corpus:phase:as-pt:rhombohedral-a7  
_paper: _paper:10.1016/j.jallcom.2006.07.063:Rhom(As)  
_tdb: _tdb:PtAs-07Li.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `27c15f179ff3234b…`

~~~~text
48: PHASE RHOMBOHEDRAL_A7 % 1 1 !
49: CONST RHOMBOHEDRAL_A7 : AS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (As–Pt)

- Id: `phase:as-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:bcc-a2)

Names (2): _corpus: _corpus:phase:as-pt:bcc-a2  
_tdb: _tdb:PtAs-07Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): BCC_A2, type code %B, sha256 `27c15f179ff3234b…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : AS PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase_

## FCC_A1 (As–Pt)

- Id: `phase:as-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2048.36 K, x(As) 0–5e-05
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:fcc-a1)

Names (3): _corpus: _corpus:phase:as-pt:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2006.07.063:fcc(Pt)  
_tdb: _tdb:PtAs-07Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): FCC_A1, type code %A, sha256 `27c15f179ff3234b…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : AS PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase; reports values for this phase_

## GAS (As–Pt)

- Id: `phase:as-pt:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 888.4–2500 K, x(As) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:gas)

Names (2): _corpus: _corpus:phase:as-pt:gas  
_tdb: _tdb:PtAs-07Li.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): GAS, type code %, sha256 `27c15f179ff3234b…`

~~~~text
56: PHASE GAS:G % 1 1 !
57: CONST GAS:G : AS% AS2 AS4 PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase_

## HCP_A3 (As–Pt)

- Id: `phase:as-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:as-pt:hcp-a3  
_tdb: _tdb:PtAs-07Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): HCP_A3, type code %A, sha256 `27c15f179ff3234b…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : AS PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase_

## LIQUID (As–Pt)

- Id: `phase:as-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 873.36–2500 K, x(As) 0–0.62307
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:liquid)

Names (3): _corpus: _corpus:phase:as-pt:liquid  
_paper: _paper:10.1016/j.jallcom.2006.07.063:L  
_tdb: _tdb:PtAs-07Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): LIQUID, type code %, sha256 `27c15f179ff3234b…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : AS PT : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02898270](https://doi.org/10.1007/bf02898270) H. Okamoto, Bull. Alloy Phase Diagrams 11 (1990) 508–510.  
_cited as the source of values for this phase_

## PTAS2_C2 (As–Pt)

- Id: `phase:as-pt:ptas2-c2`; status `assigned`
- Structure: beta-FeS2 · C2 · cP12 · Pa-3 (205); type `st:c2-beta-fes2-cp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadsr and oqmd-4540, space group 205
- Stoichiometry: As 0.6667, Pt 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1735.83 K, x(As) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:as-pt:ptas2-c2)

Names (5): _corpus: _corpus:phase:as-pt:ptas2-c2  
_mp: _mp:mp-aaaaadsr  
_oqmd: _oqmd:oqmd-4540  
_paper: _paper:10.1016/j.jallcom.2006.07.063:As2Pt  
_tdb: _tdb:PtAs-07Li.tdb:PTAS2_C2  


### TDB models of PTAS2_C2 (1): PHASE and CONSTITUENT statements as written

[PtAs-07Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PtAs-07Li.tdb): PTAS2_C2, type code %, sha256 `27c15f179ff3234b…`

~~~~text
53: PHASE PTAS2_C2 % 2 1 2 !
54: CONST PTAS2_C2 : PT : AS : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2006.07.063](https://doi.org/10.1016/j.jallcom.2006.07.063) Mei Li, Changrong Li, Fuming Wang, Weijing Zhang, The thermodynamic assessment of the As–Pt system and the analysis of the Pt/GaAs interfacial reactions, Journal of Alloys and Compounds 437, 71-79 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02898270](https://doi.org/10.1007/bf02898270) H. Okamoto, Bull. Alloy Phase Diagrams 11 (1990) 508–510.  
_cited as the source of values for this phase_

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
