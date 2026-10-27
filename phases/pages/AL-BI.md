# Al–Bi phases

> Al–Bi system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AL-BI.html · Markdown: https://data.orchid-project.org/phases/pages/AL-BI.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AL-BI) · [full JSON](https://data.orchid-project.org/phases/systems/AL-BI.json) · [Al–Bi system page](https://data.orchid-project.org/systems/AL-BI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AL-BI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Al–Bi system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-al-bi-a7-rhombohedral); _phase:al-bi:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Bi) 1–1 | 1 | 3 |
| [BCC_A2](#phase-al-bi-bcc-a2); _phase:al-bi:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-al-bi-fcc-a1); _phase:al-bi:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–934.47 K, x(Bi) 0–0.00061 | 2 | 3 |
| [HCP_A3](#phase-al-bi-hcp-a3); _phase:al-bi:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-al-bi-liquid); _phase:al-bi:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 543.33–2500 K, x(Bi) 0–1 | 145 | 3 |

## RHOMBOHEDRAL_A7 (Al–Bi)

- Id: `phase:al-bi:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Bi 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–544.55 K, x(Bi) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-bi:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:al-bi:a7-rhombohedral  
_paper: _paper:10.1007/bf02868547:Bi  
_tdb: _tdb:AlBi-06Kim.tdb:RHOMBOHEDRAL_A7, tdb:AlBi-09Mir.tdb:RHOMBOHEDRAL_A7, tdb:AlBi-84McA-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (3): PHASE and CONSTITUENT statements as written

[AlBi-06Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-06Kim.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `4fadaae9c10c6b6b…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[AlBi-09Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-09Mir.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `eddf53291d6feb32…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

[AlBi-84McA-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-84McA-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `da883e23d8b9f383…`

~~~~text
41: PHASE RHOMBOHEDRAL_A7 % 1 1 !
42: CONST RHOMBOHEDRAL_A7 : BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02868547](https://doi.org/10.1007/BF02868547) A.J. McAlister, Bull. Alloy Phase Diag., 5, 247-50(1984).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1088/0965-0393/14/7/006](https://doi.org/10.1088/0965-0393/14/7/006) S S Kim, T H Sanders, Thermodynamic assessment of the metastable liquidi in the Al–In, Al–Bi and Al–Pb systems, Modelling Simul. Mater. Sci. Eng. 14, 1181-1188 (2006).  
_assessment that models this phase_
- [doi:10.3139/146.110009](https://doi.org/10.3139/146.110009) D. Mirkovic, J. Groebner, I. Kaban, W. Hoyer, R. Schmid-Fetzer, Int. J. Mater. Res., 100, 176-88(2009).  
_assessment that models this phase_

## BCC_A2 (Al–Bi)

- Id: `phase:al-bi:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-bi:bcc-a2)

Names (4): _corpus: _corpus:phase:al-bi:bcc-a2  
_tdb: _tdb:AlBi-06Kim.tdb:BCC_A2, tdb:AlBi-09Mir.tdb:BCC_A2, tdb:AlBi-84McA-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AlBi-06Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-06Kim.tdb): BCC_A2, type code %B, sha256 `4fadaae9c10c6b6b…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : AL BI : VA : !
~~~~

[AlBi-09Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-09Mir.tdb): BCC_A2, type code %B, sha256 `eddf53291d6feb32…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AL BI : VA : !
~~~~

[AlBi-84McA-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-84McA-LB.tdb): BCC_A2, type code %B, sha256 `da883e23d8b9f383…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AL BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02868547](https://doi.org/10.1007/BF02868547) A.J. McAlister, Bull. Alloy Phase Diag., 5, 247-50(1984).  
_assessment that models this phase_
- [doi:10.1088/0965-0393/14/7/006](https://doi.org/10.1088/0965-0393/14/7/006) S S Kim, T H Sanders, Thermodynamic assessment of the metastable liquidi in the Al–In, Al–Bi and Al–Pb systems, Modelling Simul. Mater. Sci. Eng. 14, 1181-1188 (2006).  
_assessment that models this phase_
- [doi:10.3139/146.110009](https://doi.org/10.3139/146.110009) D. Mirkovic, J. Groebner, I. Kaban, W. Hoyer, R. Schmid-Fetzer, Int. J. Mater. Res., 100, 176-88(2009).  
_assessment that models this phase_

## FCC_A1 (Al–Bi)

- Id: `phase:al-bi:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–934.47 K, x(Bi) 0–0.00061
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-bi:fcc-a1)

Names (5): _corpus: _corpus:phase:al-bi:fcc-a1  
_paper: _paper:10.1007/bf02868547:(Al)  
_tdb: _tdb:AlBi-06Kim.tdb:FCC_A1, tdb:AlBi-09Mir.tdb:FCC_A1, tdb:AlBi-84McA-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AlBi-06Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-06Kim.tdb): FCC_A1, type code %A, sha256 `4fadaae9c10c6b6b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : AL% BI : VA : !
~~~~

[AlBi-09Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-09Mir.tdb): FCC_A1, type code %A, sha256 `eddf53291d6feb32…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AL% BI : VA : !
~~~~

[AlBi-84McA-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-84McA-LB.tdb): FCC_A1, type code %A, sha256 `da883e23d8b9f383…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AL% BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02868547](https://doi.org/10.1007/BF02868547) A.J. McAlister, Bull. Alloy Phase Diag., 5, 247-50(1984).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1088/0965-0393/14/7/006](https://doi.org/10.1088/0965-0393/14/7/006) S S Kim, T H Sanders, Thermodynamic assessment of the metastable liquidi in the Al–In, Al–Bi and Al–Pb systems, Modelling Simul. Mater. Sci. Eng. 14, 1181-1188 (2006).  
_assessment that models this phase_
- [doi:10.3139/146.110009](https://doi.org/10.3139/146.110009) D. Mirkovic, J. Groebner, I. Kaban, W. Hoyer, R. Schmid-Fetzer, Int. J. Mater. Res., 100, 176-88(2009).  
_assessment that models this phase_

## HCP_A3 (Al–Bi)

- Id: `phase:al-bi:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-bi:hcp-a3)

Names (4): _corpus: _corpus:phase:al-bi:hcp-a3  
_tdb: _tdb:AlBi-06Kim.tdb:HCP_A3, tdb:AlBi-09Mir.tdb:HCP_A3, tdb:AlBi-84McA-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AlBi-06Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-06Kim.tdb): HCP_A3, type code %A, sha256 `4fadaae9c10c6b6b…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : AL BI : VA : !
~~~~

[AlBi-09Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-09Mir.tdb): HCP_A3, type code %A, sha256 `eddf53291d6feb32…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AL BI : VA : !
~~~~

[AlBi-84McA-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-84McA-LB.tdb): HCP_A3, type code %A, sha256 `da883e23d8b9f383…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AL BI : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02868547](https://doi.org/10.1007/BF02868547) A.J. McAlister, Bull. Alloy Phase Diag., 5, 247-50(1984).  
_assessment that models this phase_
- [doi:10.1088/0965-0393/14/7/006](https://doi.org/10.1088/0965-0393/14/7/006) S S Kim, T H Sanders, Thermodynamic assessment of the metastable liquidi in the Al–In, Al–Bi and Al–Pb systems, Modelling Simul. Mater. Sci. Eng. 14, 1181-1188 (2006).  
_assessment that models this phase_
- [doi:10.3139/146.110009](https://doi.org/10.3139/146.110009) D. Mirkovic, J. Groebner, I. Kaban, W. Hoyer, R. Schmid-Fetzer, Int. J. Mater. Res., 100, 176-88(2009).  
_assessment that models this phase_

## LIQUID (Al–Bi)

- Id: `phase:al-bi:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 543.33–2500 K, x(Bi) 0–1
- Literature: 145 values (145 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:al-bi:liquid)

Names (6): _corpus: _corpus:phase:al-bi:liquid  
_paper: _paper:10.1007/bf02868547:L, paper:10.1007/bf02868547:liquid  
_tdb: _tdb:AlBi-06Kim.tdb:LIQUID, tdb:AlBi-09Mir.tdb:LIQUID, tdb:AlBi-84McA-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AlBi-06Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-06Kim.tdb): LIQUID, type code %, sha256 `4fadaae9c10c6b6b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : AL BI : !
~~~~

[AlBi-09Mir.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-09Mir.tdb): LIQUID, type code %, sha256 `eddf53291d6feb32…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AL BI : !
~~~~

[AlBi-84McA-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AlBi-84McA-LB.tdb): LIQUID, type code %, sha256 `da883e23d8b9f383…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AL BI : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02868547](https://doi.org/10.1007/BF02868547) A.J. McAlister, Bull. Alloy Phase Diag., 5, 247-50(1984).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1088/0965-0393/14/7/006](https://doi.org/10.1088/0965-0393/14/7/006) S S Kim, T H Sanders, Thermodynamic assessment of the metastable liquidi in the Al–In, Al–Bi and Al–Pb systems, Modelling Simul. Mater. Sci. Eng. 14, 1181-1188 (2006).  
_assessment that models this phase_
- [doi:10.3139/146.110009](https://doi.org/10.3139/146.110009) D. Mirkovic, J. Groebner, I. Kaban, W. Hoyer, R. Schmid-Fetzer, Int. J. Mater. Res., 100, 176-88(2009).  
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
