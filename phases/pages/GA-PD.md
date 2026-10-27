# Ga–Pd phases

> Ga–Pd system: 10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-PD.html · Markdown: https://data.orchid-project.org/phases/pages/GA-PD.md

10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-PD) · [full JSON](https://data.orchid-project.org/phases/systems/GA-PD.json) · [Ga–Pd system page](https://data.orchid-project.org/systems/GA-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Pd system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-pd-a11-orthorhombic); _phase:ga-pd:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 297.43–302.91 K, x(Pd) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ga-pd-bcc-a2); _phase:ga-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-ga-pd-fcc-a1); _phase:ga-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.24 K, x(Pd) 0.91085–1 | 0 | 1 |
| [GA3PD5](#phase-ga-pd-ga3pd5); _phase:ga-pd:ga3pd5_ | Ge3Rh5 · oP16 · Pbam (55) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1324.01 K, x(Pd) 0.625–0.625 | 0 | 1 |
| [GA5PD](#phase-ga-pd-ga5pd); _phase:ga-pd:ga5pd_ | Ga5Pd · tI24 · I4/mcm (140) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–454.06 K, x(Pd) 0.16667–0.16667 | 0 | 1 |
| [GA7PD3](#phase-ga-pd-ga7pd3); _phase:ga-pd:ga7pd3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–702.1 K, x(Pd) 0.3–0.3 | 0 | 1 |
| [GAPD_B20](#phase-ga-pd-gapd-b20); _phase:ga-pd:gapd-b20_ | FeSi · B20 · cP8 · P2_13 (198) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1302.98 K, x(Pd) 0.5–0.5 | 0 | 1 |
| [GAPD2_C37](#phase-ga-pd-gapd2-c37); _phase:ga-pd:gapd2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1539.73 K, x(Pd) 0.66667–0.74419 | 0 | 1 |
| [HCP_A3](#phase-ga-pd-hcp-a3); _phase:ga-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ga-pd-liquid); _phase:ga-pd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 297.43–2500 K, x(Pd) 0–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (Ga–Pd)

- Id: `phase:ga-pd:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 297.43–302.91 K, x(Pd) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:ga-pd:a11-orthorhombic  
_tdb: _tdb:GaPd-99Gro.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): ORTHORHOMBIC_A11, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
47: PHASE ORTHORHOMBIC_A11 % 1 1 !
48: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## BCC_A2 (Ga–Pd)

- Id: `phase:ga-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-pd:bcc-a2  
_tdb: _tdb:GaPd-99Gro.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): BCC_A2, type code %B, sha256 `1d2b39ec052d1b19…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : GA PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## FCC_A1 (Ga–Pd)

- Id: `phase:ga-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.24 K, x(Pd) 0.91085–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-pd:fcc-a1  
_tdb: _tdb:GaPd-99Gro.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): FCC_A1, type code %A, sha256 `1d2b39ec052d1b19…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : GA PD% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## GA3PD5 (Ga–Pd)

- Id: `phase:ga-pd:ga3pd5`; status `assigned`
- Structure: Ge3Rh5 · oP16 · Pbam (55); type `st:ge3rh5-op16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ga 0.3750, Pd 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1324.01 K, x(Pd) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:ga3pd5)

Names (2): _corpus: _corpus:phase:ga-pd:ga3pd5  
_tdb: _tdb:GaPd-99Gro.tdb:GA3PD5  


### TDB models of GA3PD5 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): GA3PD5, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
67: PHASE GA3PD5 % 2 3 5 !
68: CONST GA3PD5 : GA : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## GA5PD (Ga–Pd)

- Id: `phase:ga-pd:ga5pd`; status `assigned`
- Structure: Ga5Pd · tI24 · I4/mcm (140); type `st:ga5pd-ti24`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ga 0.8333, Pd 0.1667
- Stability: stable in 1 of 1 calculated diagram(s): 300–454.06 K, x(Pd) 0.16667–0.16667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:ga5pd)

Names (4): _corpus: _corpus:phase:ga-pd:ga5pd  
_mp: _mp:mp-aaaabtjg  
_oqmd: _oqmd:oqmd-17279  
_tdb: _tdb:GaPd-99Gro.tdb:GA5PD  


### TDB models of GA5PD (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): GA5PD, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
52: PHASE GA5PD % 2 5 1 !
53: CONST GA5PD : GA : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## GA7PD3 (Ga–Pd)

- Id: `phase:ga-pd:ga7pd3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_dft; no_structure_token; sgte_mmc2_row_disagrees_with_dft
- Candidate (dft_mp): Im-3m (229) — on-hull MP Ga7Pd3 at x(PD)=0.3000
- Candidate (dft_oqmd): Im-3m (229) — on-hull OQMD Ga7 Pd3 at x(PD)=0.3000
- Candidate (sgte_mmc2): Ga7Pd3 · mC20 · C2/m (12) — Hallstedt 2025 mmc2 row for GA7PD3: Ga7Pd3
- Candidate (tdb_comment): Ga7Pd3 · mC20 · C2/m — GaPd-99Gro.tdb: 'Prototype Ga7Pd3 (mC20, C2/m)'
- Stoichiometry: Ga 0.7000, Pd 0.3000
- Stability: stable in 1 of 1 calculated diagram(s): 300–702.1 K, x(Pd) 0.3–0.3
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:ga7pd3)

Names (2): _corpus: _corpus:phase:ga-pd:ga7pd3  
_tdb: _tdb:GaPd-99Gro.tdb:GA7PD3  


### TDB models of GA7PD3 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): GA7PD3, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
57: PHASE GA7PD3 % 2 7 3 !
58: CONST GA7PD3 : GA : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## GAPD_B20 (Ga–Pd)

- Id: `phase:ga-pd:gapd-b20`; status `assigned`
- Structure: FeSi · B20 · cP8 · P2_13 (198); type `st:b20-fesi-cp8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacjjlu and oqmd-23801, space group 198
- Stoichiometry: Ga 0.5000, Pd 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1302.98 K, x(Pd) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:gapd-b20)

Names (4): _corpus: _corpus:phase:ga-pd:gapd-b20  
_mp: _mp:mp-aaacjjlu  
_oqmd: _oqmd:oqmd-23801  
_tdb: _tdb:GaPd-99Gro.tdb:GAPD_B20  


### TDB models of GAPD_B20 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): GAPD_B20, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
62: PHASE GAPD_B20 % 2 1 1 !
63: CONST GAPD_B20 : GA : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## GAPD2_C37 (Ga–Pd)

- Id: `phase:ga-pd:gapd2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1539.73 K, x(Pd) 0.66667–0.74419
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:gapd2-c37)

Names (2): _corpus: _corpus:phase:ga-pd:gapd2-c37  
_tdb: _tdb:GaPd-99Gro.tdb:GAPD2_C37  


### TDB models of GAPD2_C37 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): GAPD2_C37, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
72: PHASE GAPD2_C37 % 2 1 2 !
73: CONST GAPD2_C37 : GA% PD : PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## HCP_A3 (Ga–Pd)

- Id: `phase:ga-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:hcp-a3)

Names (2): _corpus: _corpus:phase:ga-pd:hcp-a3  
_tdb: _tdb:GaPd-99Gro.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): HCP_A3, type code %A, sha256 `1d2b39ec052d1b19…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : GA PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## LIQUID (Ga–Pd)

- Id: `phase:ga-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 297.43–2500 K, x(Pd) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pd:liquid)

Names (2): _corpus: _corpus:phase:ga-pd:liquid  
_tdb: _tdb:GaPd-99Gro.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaPd-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPd-99Gro.tdb): LIQUID, type code %, sha256 `1d2b39ec052d1b19…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : GA PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
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
