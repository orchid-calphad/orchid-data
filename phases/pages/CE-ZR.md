# Ce–Zr phases

> Ce–Zr system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/CE-ZR.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/CE-ZR.json) · [Ce–Zr system page](https://data.orchid-project.org/systems/CE-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Zr system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-zr-bcc-a2); _phase:ce-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 988.29–3999.1 K, x(Zr) 0–1 | 6 | 1 |
| [DHCP](#phase-ce-zr-dhcp-a3); _phase:ce-zr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 1 | 1 |
| [FCC_A1](#phase-ce-zr-fcc-a1); _phase:ce-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Zr) 0–0.00644 | 2 | 1 |
| [HCP_A3](#phase-ce-zr-hcp-a3); _phase:ce-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1139 K, x(Zr) 0.96921–1 | 6 | 1 |
| [LIQUID](#phase-ce-zr-liquid); _phase:ce-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1064.72–4000 K, x(Zr) 0–1 | 4 | 1 |

## BCC_A2 (Ce–Zr)

- Id: `phase:ce-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 988.29–3999.1 K, x(Zr) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-zr:bcc-a2)

Names (4): _corpus: _corpus:phase:ce-zr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.05.002:bcc-Ce, paper:10.1016/j.calphad.2014.05.002:bcc-Zr  
_tdb: _tdb:CeZr-14Mat.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CeZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/CeZr-14Mat.tdb): BCC_A2, type code %B, sha256 `321bbab73a2bea16…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CE% ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock et al., Experimental and thermodynamic assessment of the Ce–Zr system, Calphad 46, 213-219 (2014).  
_assessment that models this phase; reports values for this phase_

## DHCP (Ce–Zr)

- Id: `phase:ce-zr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-zr:dhcp-a3)

Names (4): _corpus: _corpus:phase:ce-zr:dhcp-a3, corpus:phase:ce-zr:dhcp  
_paper: _paper:10.1016/j.calphad.2014.05.002:β(Ce)  
_tdb: _tdb:CeZr-14Mat.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[CeZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/CeZr-14Mat.tdb): DHCP, type code %A, sha256 `321bbab73a2bea16…`

~~~~text
44: PHASE DHCP %A 1 1 !
45: CONST DHCP : CE% ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock et al., Experimental and thermodynamic assessment of the Ce–Zr system, Calphad 46, 213-219 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340590](https://doi.org/10.1361/105497199770340590) K. A. Gschneidner, V. K. Pecharsky, The standard state of cerium, JPE 20, 612-614 (1999).  
_cited as the source of values for this phase_

## FCC_A1 (Ce–Zr)

- Id: `phase:ce-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Zr) 0–0.00644
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:ce-zr:fcc-a1  
_paper: _paper:10.1016/j.calphad.2014.05.002:fcc-Ce  
_tdb: _tdb:CeZr-14Mat.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CeZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/CeZr-14Mat.tdb): FCC_A1, type code %A, sha256 `321bbab73a2bea16…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CE% ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock et al., Experimental and thermodynamic assessment of the Ce–Zr system, Calphad 46, 213-219 (2014).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Ce–Zr)

- Id: `phase:ce-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1139 K, x(Zr) 0.96921–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-zr:hcp-a3)

Names (3): _corpus: _corpus:phase:ce-zr:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.05.002:hcp-Zr  
_tdb: _tdb:CeZr-14Mat.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CeZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/CeZr-14Mat.tdb): HCP_A3, type code %A, sha256 `321bbab73a2bea16…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CE ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock et al., Experimental and thermodynamic assessment of the Ce–Zr system, Calphad 46, 213-219 (2014).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Ce–Zr)

- Id: `phase:ce-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1064.72–4000 K, x(Zr) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-zr:liquid)

Names (3): _corpus: _corpus:phase:ce-zr:liquid  
_paper: _paper:10.1016/j.calphad.2014.05.002:L  
_tdb: _tdb:CeZr-14Mat.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CeZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/CeZr-14Mat.tdb): LIQUID, type code %, sha256 `321bbab73a2bea16…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CE ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.05.002](https://doi.org/10.1016/j.calphad.2014.05.002) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, H. Wendrock et al., Experimental and thermodynamic assessment of the Ce–Zr system, Calphad 46, 213-219 (2014).  
_assessment that models this phase; reports values for this phase_

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
