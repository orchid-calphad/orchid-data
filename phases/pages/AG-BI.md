# Ag–Bi phases

> Ag–Bi system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-BI.html · Markdown: https://data.orchid-project.org/phases/pages/AG-BI.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-BI) · [full JSON](https://data.orchid-project.org/phases/systems/AG-BI.json) · [Ag–Bi system page](https://data.orchid-project.org/systems/AG-BI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-BI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Bi system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-ag-bi-a7-rhombohedral); _phase:ag-bi:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Bi) 1–1 | 0 | 3 |
| [BCC_A2](#phase-ag-bi-bcc-a2); _phase:ag-bi:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ag-bi-fcc-a1); _phase:ag-bi:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1243.59 K, x(Bi) 0–0.0287 | 0 | 3 |
| [HCP_A3](#phase-ag-bi-hcp-a3); _phase:ag-bi:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ag-bi-liquid); _phase:ag-bi:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 534.75–2500 K, x(Bi) 0–1 | 0 | 3 |

## RHOMBOHEDRAL_A7 (Ag–Bi)

- Id: `phase:ag-bi:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Bi) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-bi:a7-rhombohedral)

Names (4): _corpus: _corpus:phase:ag-bi:a7-rhombohedral  
_tdb: _tdb:AgBi-94Kat.tdb:RHOMBOHEDRAL_A7, tdb:AgBi-98Luk-LB.tdb:RHOMBOHEDRAL_A7, tdb:AgBi-99Ass.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[AgBi-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-94Kat.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9b254b03596511d9…`

~~~~text
43: PHASE RHOMBOHEDRAL_A7 % 1 1 !
44: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[AgBi-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-98Luk-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `2ed35ed6e53cf51f…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[AgBi-99Ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-99Ass.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `7518266c4e2a3c78…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1111/j.1151-2916.1999.tb01821.x](https://doi.org/10.1111/j.1151-2916.1999.tb01821.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase Diagram Study and Thermodynamic Optimization of the Ag‐Bi‐O System, Journal of the American Ceramic Society 82, 711-715 (1999).  
_assessment that models this phase_

## BCC_A2 (Ag–Bi)

- Id: `phase:ag-bi:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-bi:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-bi:bcc-a2  
_tdb: _tdb:AgBi-94Kat.tdb:BCC_A2, tdb:AgBi-98Luk-LB.tdb:BCC_A2, tdb:AgBi-99Ass.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AgBi-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-94Kat.tdb): BCC_A2, type code %B, sha256 `9b254b03596511d9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG BI : VA : !
~~~~

[AgBi-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-98Luk-LB.tdb): BCC_A2, type code %B, sha256 `2ed35ed6e53cf51f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG BI : VA : !
~~~~

[AgBi-99Ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-99Ass.tdb): BCC_A2, type code %B, sha256 `7518266c4e2a3c78…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AG BI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1111/j.1151-2916.1999.tb01821.x](https://doi.org/10.1111/j.1151-2916.1999.tb01821.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase Diagram Study and Thermodynamic Optimization of the Ag‐Bi‐O System, Journal of the American Ceramic Society 82, 711-715 (1999).  
_assessment that models this phase_

## FCC_A1 (Ag–Bi)

- Id: `phase:ag-bi:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1243.59 K, x(Bi) 0–0.0287
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-bi:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-bi:fcc-a1  
_tdb: _tdb:AgBi-94Kat.tdb:FCC_A1, tdb:AgBi-98Luk-LB.tdb:FCC_A1, tdb:AgBi-99Ass.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AgBi-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-94Kat.tdb): FCC_A1, type code %A, sha256 `9b254b03596511d9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% BI : VA : !
~~~~

[AgBi-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-98Luk-LB.tdb): FCC_A1, type code %A, sha256 `2ed35ed6e53cf51f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% BI : VA : !
~~~~

[AgBi-99Ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-99Ass.tdb): FCC_A1, type code %A, sha256 `7518266c4e2a3c78…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AG% BI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1111/j.1151-2916.1999.tb01821.x](https://doi.org/10.1111/j.1151-2916.1999.tb01821.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase Diagram Study and Thermodynamic Optimization of the Ag‐Bi‐O System, Journal of the American Ceramic Society 82, 711-715 (1999).  
_assessment that models this phase_

## HCP_A3 (Ag–Bi)

- Id: `phase:ag-bi:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-bi:hcp-a3)

Names (4): _corpus: _corpus:phase:ag-bi:hcp-a3  
_tdb: _tdb:AgBi-94Kat.tdb:HCP_A3, tdb:AgBi-98Luk-LB.tdb:HCP_A3, tdb:AgBi-99Ass.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AgBi-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-94Kat.tdb): HCP_A3, type code %A, sha256 `9b254b03596511d9…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG BI : VA : !
~~~~

[AgBi-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-98Luk-LB.tdb): HCP_A3, type code %A, sha256 `2ed35ed6e53cf51f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG BI : VA : !
~~~~

[AgBi-99Ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-99Ass.tdb): HCP_A3, type code %A, sha256 `7518266c4e2a3c78…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AG BI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1111/j.1151-2916.1999.tb01821.x](https://doi.org/10.1111/j.1151-2916.1999.tb01821.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase Diagram Study and Thermodynamic Optimization of the Ag‐Bi‐O System, Journal of the American Ceramic Society 82, 711-715 (1999).  
_assessment that models this phase_

## LIQUID (Ag–Bi)

- Id: `phase:ag-bi:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 534.75–2500 K, x(Bi) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-bi:liquid)

Names (4): _corpus: _corpus:phase:ag-bi:liquid  
_tdb: _tdb:AgBi-94Kat.tdb:LIQUID, tdb:AgBi-98Luk-LB.tdb:LIQUID, tdb:AgBi-99Ass.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AgBi-94Kat.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-94Kat.tdb): LIQUID, type code %, sha256 `9b254b03596511d9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG BI : !
~~~~

[AgBi-98Luk-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-98Luk-LB.tdb): LIQUID, type code %, sha256 `2ed35ed6e53cf51f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG BI : !
~~~~

[AgBi-99Ass.tdb](https://orchid-project.org/data/databases/sgte-binary/AgBi-99Ass.tdb): LIQUID, type code %, sha256 `7518266c4e2a3c78…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AG BI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02653345](https://doi.org/10.1007/BF02653345) U.R. Kattner, W.J. Boettinger, J. Electron. Mater., 23, 603-10(1994).  
_assessment that models this phase_
- [doi:10.1111/j.1151-2916.1999.tb01821.x](https://doi.org/10.1111/j.1151-2916.1999.tb01821.x) Jérôme Assal, Bengt Hallstedt, Ludwig J. Gauckler, Experimental Phase Diagram Study and Thermodynamic Optimization of the Ag‐Bi‐O System, Journal of the American Ceramic Society 82, 711-715 (1999).  
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
