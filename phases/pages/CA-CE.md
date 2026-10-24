# Ca–Ce phases

> Ca–Ce system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-CE.html · Markdown: https://data.orchid-project.org/phases/pages/CA-CE.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-CE) · [full JSON](https://data.orchid-project.org/phases/systems/CA-CE.json) · [Ca–Ce system page](https://data.orchid-project.org/systems/CA-CE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-CE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Ce system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-ce-bcc-a2); _phase:ca-ce:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 715.65–2499.5 K, x(Ce) 0–1 | 15 | 2 |
| [DHCP](#phase-ca-ce-dhcp-a3); _phase:ca-ce:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ca-ce-fcc-a1); _phase:ca-ce:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1000 K, x(Ce) 0–1 | 2 | 2 |
| [HCP_A3](#phase-ca-ce-hcp-a3); _phase:ca-ce:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ca-ce-liquid); _phase:ca-ce:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1057–2500 K, x(Ce) 0–1 | 5 | 2 |

## BCC_A2 (Ca–Ce)

- Id: `phase:ca-ce:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 715.65–2499.5 K, x(Ce) 0–1
- Literature: 15 values (15 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ce:bcc-a2)

Names (6): _corpus: _corpus:phase:ca-ce:bcc-a2  
_paper: _paper:10.1007/s10853-007-2002-2:βCa, paper:10.1016/j.jallcom.2007.09.020:bcc, paper:10.1016/j.jallcom.2007.09.020:bcc(Ca)  
_tdb: _tdb:CaCe-07Ham.tdb:BCC_A2, tdb:CaCe-08Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CaCe-07Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-07Ham.tdb): BCC_A2, type code %B, sha256 `c783a715a2b1db9f…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CA% CE% : VA : !
~~~~

[CaCe-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-08Zha.tdb): BCC_A2, type code %B, sha256 `e5b5b58aa607f94b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : CA% CE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020) Hui Zhang, Yi Wang, Shunli Shang, Long-Qing Chen, Zi-Kui Liu, Thermodynamic modeling of Mg–Ca–Ce system by combining first-principles and CALPHAD method, Journal of Alloys and Compounds 463, 294-301 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2) Milan Hampl, Joachim Gröbner, Rainer Schmid-Fetzer, Experimental study of phase equilibria and solidification microstructures of Mg–Ca–Ce alloys combined with thermodynamic modeling, J Mater Sci 42, 10023-10031 (2007).  
_assessment that models this phase; reports values for this phase_

## DHCP (Ca–Ce)

- Id: `phase:ca-ce:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ce:dhcp-a3)

Names (4): _corpus: _corpus:phase:ca-ce:dhcp-a3, corpus:phase:ca-ce:dhcp  
_tdb: _tdb:CaCe-07Ham.tdb:DHCP, tdb:CaCe-08Zha.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[CaCe-07Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-07Ham.tdb): DHCP, type code %A, sha256 `c783a715a2b1db9f…`

~~~~text
42: PHASE DHCP %A 2 1 0.5 !
43: CONST DHCP : CE : VA% : !
~~~~

[CaCe-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-08Zha.tdb): DHCP, type code %A, sha256 `e5b5b58aa607f94b…`

~~~~text
44: PHASE DHCP %A 2 1 0.5 !
45: CONST DHCP : CE : VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2) Milan Hampl, Joachim Gröbner, Rainer Schmid-Fetzer, Experimental study of phase equilibria and solidification microstructures of Mg–Ca–Ce alloys combined with thermodynamic modeling, J Mater Sci 42, 10023-10031 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020) Hui Zhang, Yi Wang, Shunli Shang, Long-Qing Chen, Zi-Kui Liu, Thermodynamic modeling of Mg–Ca–Ce system by combining first-principles and CALPHAD method, Journal of Alloys and Compounds 463, 294-301 (2008).  
_assessment that models this phase_

## FCC_A1 (Ca–Ce)

- Id: `phase:ca-ce:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1000 K, x(Ce) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ce:fcc-a1)

Names (4): _corpus: _corpus:phase:ca-ce:fcc-a1  
_paper: _paper:10.1007/s10853-007-2002-2:αCe  
_tdb: _tdb:CaCe-07Ham.tdb:FCC_A1, tdb:CaCe-08Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CaCe-07Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-07Ham.tdb): FCC_A1, type code %A, sha256 `c783a715a2b1db9f…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CA% CE% : VA : !
~~~~

[CaCe-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-08Zha.tdb): FCC_A1, type code %A, sha256 `e5b5b58aa607f94b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : CA% CE% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2) Milan Hampl, Joachim Gröbner, Rainer Schmid-Fetzer, Experimental study of phase equilibria and solidification microstructures of Mg–Ca–Ce alloys combined with thermodynamic modeling, J Mater Sci 42, 10023-10031 (2007).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020) Hui Zhang, Yi Wang, Shunli Shang, Long-Qing Chen, Zi-Kui Liu, Thermodynamic modeling of Mg–Ca–Ce system by combining first-principles and CALPHAD method, Journal of Alloys and Compounds 463, 294-301 (2008).  
_assessment that models this phase_

## HCP_A3 (Ca–Ce)

- Id: `phase:ca-ce:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ce:hcp-a3)

Names (3): _corpus: _corpus:phase:ca-ce:hcp-a3  
_tdb: _tdb:CaCe-07Ham.tdb:HCP_A3, tdb:CaCe-08Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CaCe-07Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-07Ham.tdb): HCP_A3, type code %A, sha256 `c783a715a2b1db9f…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CA CE : VA : !
~~~~

[CaCe-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-08Zha.tdb): HCP_A3, type code %A, sha256 `e5b5b58aa607f94b…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : CA CE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2) Milan Hampl, Joachim Gröbner, Rainer Schmid-Fetzer, Experimental study of phase equilibria and solidification microstructures of Mg–Ca–Ce alloys combined with thermodynamic modeling, J Mater Sci 42, 10023-10031 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020) Hui Zhang, Yi Wang, Shunli Shang, Long-Qing Chen, Zi-Kui Liu, Thermodynamic modeling of Mg–Ca–Ce system by combining first-principles and CALPHAD method, Journal of Alloys and Compounds 463, 294-301 (2008).  
_assessment that models this phase_

## LIQUID (Ca–Ce)

- Id: `phase:ca-ce:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1057–2500 K, x(Ce) 0–1
- Literature: 5 values (5 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ce:liquid)

Names (6): _corpus: _corpus:phase:ca-ce:liquid  
_paper: _paper:10.1007/s10853-007-2002-2:L″, paper:10.1016/j.jallcom.2007.09.020:Liquid 1, paper:10.1016/j.jallcom.2007.09.020:liquid 2  
_tdb: _tdb:CaCe-07Ham.tdb:LIQUID, tdb:CaCe-08Zha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CaCe-07Ham.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-07Ham.tdb): LIQUID, type code %, sha256 `c783a715a2b1db9f…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CA CE : !
~~~~

[CaCe-08Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/CaCe-08Zha.tdb): LIQUID, type code %, sha256 `e5b5b58aa607f94b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : CA CE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2007.09.020](https://doi.org/10.1016/j.jallcom.2007.09.020) Hui Zhang, Yi Wang, Shunli Shang, Long-Qing Chen, Zi-Kui Liu, Thermodynamic modeling of Mg–Ca–Ce system by combining first-principles and CALPHAD method, Journal of Alloys and Compounds 463, 294-301 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s10853-007-2002-2](https://doi.org/10.1007/s10853-007-2002-2) Milan Hampl, Joachim Gröbner, Rainer Schmid-Fetzer, Experimental study of phase equilibria and solidification microstructures of Mg–Ca–Ce alloys combined with thermodynamic modeling, J Mater Sci 42, 10023-10031 (2007).  
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
