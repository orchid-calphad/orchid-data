# Gd–Zr phases

> Gd–Zr system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/GD-ZR.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/GD-ZR.json) · [Gd–Zr system page](https://data.orchid-project.org/systems/GD-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Zr system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-gd-zr-bcc-a2); _phase:gd-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300.25–3999.1 K, x(Zr) 0–1 | 24 | 4 |
| [FCC_A1](#phase-gd-zr-fcc-a1); _phase:gd-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-gd-zr-hcp-a3); _phase:gd-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–1625.95 K, x(Zr) 0–1 | 40 | 4 |
| [LIQUID](#phase-gd-zr-liquid); _phase:gd-zr:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1475.4–4000 K, x(Zr) 0–1 | 23 | 4 |

## BCC_A2 (Gd–Zr)

- Id: `phase:gd-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300.25–3999.1 K, x(Zr) 0–1
- Literature: 24 values (24 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-zr:bcc-a2)

Names (10): _corpus: _corpus:phase:gd-zr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2012.08.001:bcc-Gd, paper:10.1016/j.calphad.2012.08.001:bcc-Zr, paper:10.1016/j.tca.2014.07.014:bcc_Zr, paper:10.1361/105497101770339283:bcc-Gd, paper:10.1361/105497101770339283:bcc-Zr  
_tdb: _tdb:GdZr-01Zin-LB.tdb:BCC_A2, tdb:GdZr-12Mat.tdb:BCC_A2, tdb:GdZr-14Bo.tdb:BCC_A2, tdb:GdZr-18Mat.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[GdZr-01Zin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-01Zin-LB.tdb): BCC_A2, type code %B, sha256 `731c7eb124b1facc…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GD ZR : VA : !
~~~~

[GdZr-12Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-12Mat.tdb): BCC_A2, type code %B, sha256 `ba6c913991472ec3…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : GD ZR : VA : !
~~~~

[GdZr-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-14Bo.tdb): BCC_A2, type code %B, sha256 `d95180cc64867ffa…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GD ZR : VA : !
~~~~

[GdZr-18Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-18Mat.tdb): BCC_A2, type code %B, sha256 `b9962f2048151f05…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : GD ZR : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497101770339283](https://doi.org/10.1361/105497101770339283) M. Zinkevich, N. Mattern, H. J. Seifer, Thermodynamic assessment of Gd-Zr and Gd-Mo systems, JPE 22, 43-50 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.08.001](https://doi.org/10.1016/j.calphad.2012.08.001) N. Mattern, J.H. Han, M. Zinkevich, O. Shuleshova, I. Kaban, D. Holland-Moritz et al., Experimental and thermodynamic assessment of the Gd–Zr system, Calphad 39, 27-32 (2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.04.008](https://doi.org/10.1016/j.calphad.2018.04.008) N. Mattern, J.H. Han, R. Nowak, O. Fabrichnaya, I. Kaban, O. Shuleshova, N. Sobczak, Calphad, 61, 237-45(2018).  
_assessment that models this phase_

## FCC_A1 (Gd–Zr)

- Id: `phase:gd-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-zr:fcc-a1)

Names (5): _corpus: _corpus:phase:gd-zr:fcc-a1  
_tdb: _tdb:GdZr-01Zin-LB.tdb:FCC_A1, tdb:GdZr-12Mat.tdb:FCC_A1, tdb:GdZr-14Bo.tdb:FCC_A1, tdb:GdZr-18Mat.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[GdZr-01Zin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-01Zin-LB.tdb): FCC_A1, type code %A, sha256 `731c7eb124b1facc…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GD ZR : VA : !
~~~~

[GdZr-12Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-12Mat.tdb): FCC_A1, type code %A, sha256 `ba6c913991472ec3…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : GD ZR : VA : !
~~~~

[GdZr-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-14Bo.tdb): FCC_A1, type code %A, sha256 `d95180cc64867ffa…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GD ZR : VA : !
~~~~

[GdZr-18Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-18Mat.tdb): FCC_A1, type code %A, sha256 `b9962f2048151f05…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : GD ZR : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.08.001](https://doi.org/10.1016/j.calphad.2012.08.001) N. Mattern, J.H. Han, M. Zinkevich, O. Shuleshova, I. Kaban, D. Holland-Moritz et al., Experimental and thermodynamic assessment of the Gd–Zr system, Calphad 39, 27-32 (2012).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.04.008](https://doi.org/10.1016/j.calphad.2018.04.008) N. Mattern, J.H. Han, R. Nowak, O. Fabrichnaya, I. Kaban, O. Shuleshova, N. Sobczak, Calphad, 61, 237-45(2018).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase_
- [doi:10.1361/105497101770339283](https://doi.org/10.1361/105497101770339283) M. Zinkevich, N. Mattern, H. J. Seifer, Thermodynamic assessment of Gd-Zr and Gd-Mo systems, JPE 22, 43-50 (2001).  
_assessment that models this phase_

## HCP_A3 (Gd–Zr)

- Id: `phase:gd-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–1625.95 K, x(Zr) 0–1
- Literature: 40 values (40 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-zr:hcp-a3)

Names (8): _corpus: _corpus:phase:gd-zr:hcp-a3  
_paper: _paper:10.1016/j.calphad.2012.08.001:hcp-Gd, paper:10.1361/105497101770339283:hcp-Gd, paper:10.1361/105497101770339283:hcp-Zr  
_tdb: _tdb:GdZr-01Zin-LB.tdb:HCP_A3, tdb:GdZr-12Mat.tdb:HCP_A3, tdb:GdZr-14Bo.tdb:HCP_A3, tdb:GdZr-18Mat.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[GdZr-01Zin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-01Zin-LB.tdb): HCP_A3, type code %A, sha256 `731c7eb124b1facc…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GD ZR : VA : !
~~~~

[GdZr-12Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-12Mat.tdb): HCP_A3, type code %A, sha256 `ba6c913991472ec3…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : GD ZR : VA : !
~~~~

[GdZr-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-14Bo.tdb): HCP_A3, type code %A, sha256 `d95180cc64867ffa…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : GD ZR : VA : !
~~~~

[GdZr-18Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-18Mat.tdb): HCP_A3, type code %A, sha256 `b9962f2048151f05…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : GD ZR : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2012.08.001](https://doi.org/10.1016/j.calphad.2012.08.001) N. Mattern, J.H. Han, M. Zinkevich, O. Shuleshova, I. Kaban, D. Holland-Moritz et al., Experimental and thermodynamic assessment of the Gd–Zr system, Calphad 39, 27-32 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497101770339283](https://doi.org/10.1361/105497101770339283) M. Zinkevich, N. Mattern, H. J. Seifer, Thermodynamic assessment of Gd-Zr and Gd-Mo systems, JPE 22, 43-50 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.04.008](https://doi.org/10.1016/j.calphad.2018.04.008) N. Mattern, J.H. Han, R. Nowak, O. Fabrichnaya, I. Kaban, O. Shuleshova, N. Sobczak, Calphad, 61, 237-45(2018).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase_

## LIQUID (Gd–Zr)

- Id: `phase:gd-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1475.4–4000 K, x(Zr) 0–1
- Literature: 23 values (23 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-zr:liquid)

Names (8): _corpus: _corpus:phase:gd-zr:liquid  
_paper: _paper:10.1016/j.calphad.2012.08.001:L, paper:10.1016/j.tca.2014.07.014:Liquid, paper:10.1361/105497101770339283:Liquid  
_tdb: _tdb:GdZr-01Zin-LB.tdb:LIQUID, tdb:GdZr-12Mat.tdb:LIQUID, tdb:GdZr-14Bo.tdb:LIQUID, tdb:GdZr-18Mat.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[GdZr-01Zin-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-01Zin-LB.tdb): LIQUID, type code %, sha256 `731c7eb124b1facc…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GD ZR : !
~~~~

[GdZr-12Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-12Mat.tdb): LIQUID, type code %, sha256 `ba6c913991472ec3…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : GD ZR : !
~~~~

[GdZr-14Bo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-14Bo.tdb): LIQUID, type code %, sha256 `d95180cc64867ffa…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GD ZR : !
~~~~

[GdZr-18Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GdZr-18Mat.tdb): LIQUID, type code %, sha256 `b9962f2048151f05…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : GD ZR : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1361/105497101770339283](https://doi.org/10.1361/105497101770339283) M. Zinkevich, N. Mattern, H. J. Seifer, Thermodynamic assessment of Gd-Zr and Gd-Mo systems, JPE 22, 43-50 (2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2012.08.001](https://doi.org/10.1016/j.calphad.2012.08.001) N. Mattern, J.H. Han, M. Zinkevich, O. Shuleshova, I. Kaban, D. Holland-Moritz et al., Experimental and thermodynamic assessment of the Gd–Zr system, Calphad 39, 27-32 (2012).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.tca.2014.07.014](https://doi.org/10.1016/j.tca.2014.07.014) H. Bo, L.B. Liu, J.L. Hu, X.D. Zhang, Z.P. Jin, Thermodynamic re-assessment of the Al–Gd and Gd–Zr systems, Thermochimica Acta 591, 51-56 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2018.04.008](https://doi.org/10.1016/j.calphad.2018.04.008) N. Mattern, J.H. Han, R. Nowak, O. Fabrichnaya, I. Kaban, O. Shuleshova, N. Sobczak, Calphad, 61, 237-45(2018).  
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
