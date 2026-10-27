# Cu–Ni phases

> Cu–Ni system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-NI.html · Markdown: https://data.orchid-project.org/phases/pages/CU-NI.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-NI) · [full JSON](https://data.orchid-project.org/phases/systems/CU-NI.json) · [Cu–Ni system page](https://data.orchid-project.org/systems/CU-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Ni system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-ni-bcc-a2); _phase:cu-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-cu-ni-fcc-a1); _phase:cu-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1728.25 K, x(Ni) 0–1 | 0 | 4 |
| [HCP_A3](#phase-cu-ni-hcp-a3); _phase:cu-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-cu-ni-liquid); _phase:cu-ni:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1357.77–2500 K, x(Ni) 0–1 | 0 | 4 |

## BCC_A2 (Cu–Ni)

- Id: `phase:cu-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ni:bcc-a2)

Names (5): _corpus: _corpus:phase:cu-ni:bcc-a2  
_tdb: _tdb:CuNi-07Tur.tdb:BCC_A2, tdb:CuNi-87Jan.tdb:BCC_A2, tdb:CuNi-89Sri.tdb:BCC_A2, tdb:CuNi-92Mey-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CuNi-07Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-07Tur.tdb): BCC_A2, type code %B, sha256 `10031ba89321cab1…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CU NI : VA : !
~~~~

[CuNi-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-87Jan.tdb): BCC_A2, type code %B, sha256 `c378a4dea0f2dadf…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU NI : VA : !
~~~~

[CuNi-89Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-89Sri.tdb): BCC_A2, type code %B, sha256 `39b018ea8c7d3c13…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CU NI : VA : !
~~~~

[CuNi-92Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-92Mey-LB.tdb): BCC_A2, type code %B, sha256 `7e52adda858e3021…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CU NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007).  
_assessment that models this phase_
- [doi:10.1179/mst.1989.5.5.427](https://doi.org/10.1179/mst.1989.5.5.427) S. Srikanth, K. T. Jacob, Thermodynamic properties of Cu–Ni alloys: measurements and assessment, Materials Science and Technology 5, 427-434 (1989).  
_assessment that models this phase_

## FCC_A1 (Cu–Ni)

- Id: `phase:cu-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1728.25 K, x(Ni) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ni:fcc-a1)

Names (5): _corpus: _corpus:phase:cu-ni:fcc-a1  
_tdb: _tdb:CuNi-07Tur.tdb:FCC_A1, tdb:CuNi-87Jan.tdb:FCC_A1, tdb:CuNi-89Sri.tdb:FCC_A1, tdb:CuNi-92Mey-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CuNi-07Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-07Tur.tdb): FCC_A1, type code %A, sha256 `10031ba89321cab1…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CU% NI% : VA : !
~~~~

[CuNi-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-87Jan.tdb): FCC_A1, type code %A, sha256 `c378a4dea0f2dadf…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU% NI% : VA : !
~~~~

[CuNi-89Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-89Sri.tdb): FCC_A1, type code %A, sha256 `39b018ea8c7d3c13…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CU% NI% : VA : !
~~~~

[CuNi-92Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-92Mey-LB.tdb): FCC_A1, type code %A, sha256 `7e52adda858e3021…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CU% NI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007).  
_assessment that models this phase_
- [doi:10.1179/mst.1989.5.5.427](https://doi.org/10.1179/mst.1989.5.5.427) S. Srikanth, K. T. Jacob, Thermodynamic properties of Cu–Ni alloys: measurements and assessment, Materials Science and Technology 5, 427-434 (1989).  
_assessment that models this phase_

## HCP_A3 (Cu–Ni)

- Id: `phase:cu-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ni:hcp-a3)

Names (5): _corpus: _corpus:phase:cu-ni:hcp-a3  
_tdb: _tdb:CuNi-07Tur.tdb:HCP_A3, tdb:CuNi-87Jan.tdb:HCP_A3, tdb:CuNi-89Sri.tdb:HCP_A3, tdb:CuNi-92Mey-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CuNi-07Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-07Tur.tdb): HCP_A3, type code %A, sha256 `10031ba89321cab1…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CU NI : VA : !
~~~~

[CuNi-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-87Jan.tdb): HCP_A3, type code %A, sha256 `c378a4dea0f2dadf…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU NI : VA : !
~~~~

[CuNi-89Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-89Sri.tdb): HCP_A3, type code %A, sha256 `39b018ea8c7d3c13…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CU NI : VA : !
~~~~

[CuNi-92Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-92Mey-LB.tdb): HCP_A3, type code %A, sha256 `7e52adda858e3021…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CU NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007).  
_assessment that models this phase_
- [doi:10.1179/mst.1989.5.5.427](https://doi.org/10.1179/mst.1989.5.5.427) S. Srikanth, K. T. Jacob, Thermodynamic properties of Cu–Ni alloys: measurements and assessment, Materials Science and Technology 5, 427-434 (1989).  
_assessment that models this phase_

## LIQUID (Cu–Ni)

- Id: `phase:cu-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1357.77–2500 K, x(Ni) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-ni:liquid)

Names (5): _corpus: _corpus:phase:cu-ni:liquid  
_tdb: _tdb:CuNi-07Tur.tdb:LIQUID, tdb:CuNi-87Jan.tdb:LIQUID, tdb:CuNi-89Sri.tdb:LIQUID, tdb:CuNi-92Mey-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CuNi-07Tur.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-07Tur.tdb): LIQUID, type code %, sha256 `10031ba89321cab1…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CU NI : !
~~~~

[CuNi-87Jan.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-87Jan.tdb): LIQUID, type code %, sha256 `c378a4dea0f2dadf…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU NI : !
~~~~

[CuNi-89Sri.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-89Sri.tdb): LIQUID, type code %, sha256 `39b018ea8c7d3c13…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CU NI : !
~~~~

[CuNi-92Mey-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CuNi-92Mey-LB.tdb): LIQUID, type code %, sha256 `7e52adda858e3021…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CU NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11106-007-0013-9](https://doi.org/10.1007/s11106-007-0013-9) M. A. Turchanin, P. G. Agraval, Phase equilibria and thermodynamics of binary copper systems with 3d-metals. V. Copper-cobalt system, Powder Metall Met Ceram 46, 77-89 (2007).  
_assessment that models this phase_
- [doi:10.1179/mst.1989.5.5.427](https://doi.org/10.1179/mst.1989.5.5.427) S. Srikanth, K. T. Jacob, Thermodynamic properties of Cu–Ni alloys: measurements and assessment, Materials Science and Technology 5, 427-434 (1989).  
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
