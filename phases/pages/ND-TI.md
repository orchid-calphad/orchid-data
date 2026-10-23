# Nd–Ti phases

> Nd–Ti system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ND-TI.html · Markdown: https://data.orchid-project.org/phases/pages/ND-TI.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ND-TI) · [full JSON](https://data.orchid-project.org/phases/systems/ND-TI.json) · [Nd–Ti system page](https://data.orchid-project.org/systems/ND-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/ND-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nd–Ti system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nd-ti-bcc-a2); _phase:nd-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1126.92–2499.7 K, x(Ti) 0–1 | 6 | 1 |
| [DHCP](#phase-nd-ti-dhcp); _phase:nd-ti:dhcp_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 0 |
| [DHCP](#phase-nd-ti-dhcp-a3); _phase:nd-ti:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1160 K, x(Ti) 0–0.54 | 5 | 1 |
| [FCC_A1](#phase-nd-ti-fcc-a1); _phase:nd-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1160–1160 K, x(Ti) 0.1–0.41 | 0 | 1 |
| [HCP_A3](#phase-nd-ti-hcp-a3); _phase:nd-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1162.96 K, x(Ti) 0.11–1 | 5 | 1 |
| [LIQUID](#phase-nd-ti-liquid); _phase:nd-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1285.72–2500 K, x(Ti) 0–1 | 8 | 1 |

## BCC_A2 (Nd–Ti)

- Id: `phase:nd-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1126.92–2499.7 K, x(Ti) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-ti:bcc-a2)

Names (4): _corpus: _corpus:phase:nd-ti:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.08.002:bcc-Nd, paper:10.1016/j.calphad.2014.08.002:bcc-Ti  
_tdb: _tdb:NdTi-14Mat.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[NdTi-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdTi-14Mat.tdb): BCC_A2, type code %B, sha256 `92541b455dbef5e9…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : ND TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014).  
_assessment that models this phase; reports values for this phase_

## DHCP (Nd–Ti)

- Id: `phase:nd-ti:dhcp`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-ti:dhcp)

Names (1): _corpus: _corpus:phase:nd-ti:dhcp  


## DHCP (Nd–Ti)

- Id: `phase:nd-ti:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1160 K, x(Ti) 0–0.54
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-ti:dhcp-a3)

Names (4): _corpus: _corpus:phase:nd-ti:dhcp-a3  
_paper: _paper:10.1016/j.calphad.2014.08.002:Nd, paper:10.1016/j.calphad.2014.08.002:dhcp-Nd  
_tdb: _tdb:NdTi-14Mat.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[NdTi-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdTi-14Mat.tdb): DHCP, type code %, sha256 `92541b455dbef5e9…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : ND% TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Nd–Ti)

- Id: `phase:nd-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1160–1160 K, x(Ti) 0.1–0.41
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-ti:fcc-a1)

Names (2): _corpus: _corpus:phase:nd-ti:fcc-a1  
_tdb: _tdb:NdTi-14Mat.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[NdTi-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdTi-14Mat.tdb): FCC_A1, type code %A, sha256 `92541b455dbef5e9…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : ND TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014).  
_assessment that models this phase_

## HCP_A3 (Nd–Ti)

- Id: `phase:nd-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1162.96 K, x(Ti) 0.11–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-ti:hcp-a3)

Names (4): _corpus: _corpus:phase:nd-ti:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.08.002:Ti, paper:10.1016/j.calphad.2014.08.002:hcp-Ti  
_tdb: _tdb:NdTi-14Mat.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NdTi-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdTi-14Mat.tdb): HCP_A3, type code %A, sha256 `92541b455dbef5e9…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : ND TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Nd–Ti)

- Id: `phase:nd-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1285.72–2500 K, x(Ti) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-ti:liquid)

Names (4): _corpus: _corpus:phase:nd-ti:liquid  
_paper: _paper:10.1016/j.calphad.2014.08.002:L1, paper:10.1016/j.calphad.2014.08.002:L2  
_tdb: _tdb:NdTi-14Mat.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NdTi-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdTi-14Mat.tdb): LIQUID, type code %, sha256 `92541b455dbef5e9…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : ND TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.08.002](https://doi.org/10.1016/j.calphad.2014.08.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Ti system, Calphad 47, 136-143 (2014).  
_assessment that models this phase; reports values for this phase_

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
