# Ce–Y phases

> Ce–Y system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-Y.html · Markdown: https://data.orchid-project.org/phases/pages/CE-Y.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-Y) · [full JSON](https://data.orchid-project.org/phases/systems/CE-Y.json) · [Ce–Y system page](https://data.orchid-project.org/systems/CE-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–Y system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-y-bcc-a2); _phase:ce-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 954.4–2499.5 K, x(Y) 0–1 | 10 | 3 |
| [DHCP](#phase-ce-y-dhcp); _phase:ce-y:dhcp_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 0 |
| [DHCP](#phase-ce-y-dhcp-a3); _phase:ce-y:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1055.23 K, x(Y) 0–0.5458 | 10 | 3 |
| [FCC_A1](#phase-ce-y-fcc-a1); _phase:ce-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1001.33 K, x(Y) 0–0.12683 | 6 | 3 |
| [HCP_A3](#phase-ce-y-hcp-a3); _phase:ce-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1752.15 K, x(Y) 0.6283–1 | 4 | 3 |
| [LIQUID](#phase-ce-y-liquid); _phase:ce-y:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1060.35–2500 K, x(Y) 0–1 | 0 | 3 |

## BCC_A2 (Ce–Y)

- Id: `phase:ce-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 954.4–2499.5 K, x(Y) 0–1
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-y:bcc-a2)

Names (6): _corpus: _corpus:phase:ce-y:bcc-a2  
_paper: _paper:10.1016/j.calphad.2006.02.002:bcc_a2, paper:10.1016/j.ssi.2008.06.011:bcc  
_tdb: _tdb:CeY-06Men.tdb:BCC_A2, tdb:CeY-08Dju.tdb:BCC_A2, tdb:CeY-08Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CeY-06Men.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-06Men.tdb): BCC_A2, type code %B, sha256 `1ae8c2335e970ff1…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CE% Y% : VA : !
~~~~

[CeY-08Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Dju.tdb): BCC_A2, type code %B, sha256 `dec06e9f8d832c22…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CE Y : VA : !
~~~~

[CeY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Guo.tdb): BCC_A2, type code %B, sha256 `6052d6790f767fad…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CE% Y% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002) F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ce–Y system, Calphad 30, 323-325 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011) D DJUROVIC, M ZINKEVICH, F ALDINGER, Thermodynamic modeling of the cerium–yttrium–oxygen system, Solid State Ionics 179, 1902-1911 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_
- [doi:10.1007/s11661-997-0129-z](https://doi.org/10.1007/s11661-997-0129-z) H. Flandorfer, M. Giovannini, A. Saccone, R. Rogi, R. Ferro, The Ce-Mg-Y system, Metall Mater Trans A 28, 265-276 (1997).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02892383](https://doi.org/10.1007/bf02892383) K. A. Gschneidner, F. W. Calderwood, The Ce−Y (Cerium−Yttrium) system, Bulletin of Alloy Phase Diagrams 3, 192-194 (1982).  
_cited as the source of values for this phase_

## DHCP (Ce–Y)

- Id: `phase:ce-y:dhcp`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-y:dhcp)

Names (1): _corpus: _corpus:phase:ce-y:dhcp  


## DHCP (Ce–Y)

- Id: `phase:ce-y:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1055.23 K, x(Y) 0–0.5458
- Literature: 10 values (10 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-y:dhcp-a3)

Names (6): _corpus: _corpus:phase:ce-y:dhcp-a3  
_paper: _paper:10.1016/j.calphad.2006.02.002:dhcp, paper:10.1016/j.ssi.2008.06.011:dhcp  
_tdb: _tdb:CeY-06Men.tdb:DHCP, tdb:CeY-08Dju.tdb:DHCP, tdb:CeY-08Guo.tdb:DHCP  


### TDB models of DHCP (3): PHASE and CONSTITUENT statements as written

[CeY-06Men.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-06Men.tdb): DHCP, type code %A, sha256 `1ae8c2335e970ff1…`

~~~~text
43: PHASE DHCP %A 1 1 !
44: CONST DHCP : CE% Y : !
~~~~

[CeY-08Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Dju.tdb): DHCP, type code %A, sha256 `dec06e9f8d832c22…`

~~~~text
45: PHASE DHCP %A 1 1 !
46: CONST DHCP : CE Y : !
~~~~

[CeY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Guo.tdb): DHCP, type code %A, sha256 `6052d6790f767fad…`

~~~~text
42: PHASE DHCP %A 1 1 !
43: CONST DHCP : CE% Y : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002) F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ce–Y system, Calphad 30, 323-325 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011) D DJUROVIC, M ZINKEVICH, F ALDINGER, Thermodynamic modeling of the cerium–yttrium–oxygen system, Solid State Ionics 179, 1902-1911 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_
- [doi:10.1007/s11661-997-0129-z](https://doi.org/10.1007/s11661-997-0129-z) H. Flandorfer, M. Giovannini, A. Saccone, R. Rogi, R. Ferro, The Ce-Mg-Y system, Metall Mater Trans A 28, 265-276 (1997).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02892383](https://doi.org/10.1007/bf02892383) K. A. Gschneidner, F. W. Calderwood, The Ce−Y (Cerium−Yttrium) system, Bulletin of Alloy Phase Diagrams 3, 192-194 (1982).  
_cited as the source of values for this phase_

## FCC_A1 (Ce–Y)

- Id: `phase:ce-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1001.33 K, x(Y) 0–0.12683
- Literature: 6 values (6 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-y:fcc-a1)

Names (6): _corpus: _corpus:phase:ce-y:fcc-a1  
_paper: _paper:10.1016/j.calphad.2006.02.002:fcc_a1, paper:10.1016/j.ssi.2008.06.011:fcc  
_tdb: _tdb:CeY-06Men.tdb:FCC_A1, tdb:CeY-08Dju.tdb:FCC_A1, tdb:CeY-08Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CeY-06Men.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-06Men.tdb): FCC_A1, type code %A, sha256 `1ae8c2335e970ff1…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CE% Y : VA : !
~~~~

[CeY-08Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Dju.tdb): FCC_A1, type code %A, sha256 `dec06e9f8d832c22…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CE% Y : VA% : !
~~~~

[CeY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Guo.tdb): FCC_A1, type code %A, sha256 `6052d6790f767fad…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CE% Y : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002) F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ce–Y system, Calphad 30, 323-325 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011) D DJUROVIC, M ZINKEVICH, F ALDINGER, Thermodynamic modeling of the cerium–yttrium–oxygen system, Solid State Ionics 179, 1902-1911 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_
- [doi:10.1007/bf02892383](https://doi.org/10.1007/bf02892383) K. A. Gschneidner, F. W. Calderwood, The Ce−Y (Cerium−Yttrium) system, Bulletin of Alloy Phase Diagrams 3, 192-194 (1982).  
_cited as the source of values for this phase_
- [doi:10.1007/s11661-997-0129-z](https://doi.org/10.1007/s11661-997-0129-z) H. Flandorfer, M. Giovannini, A. Saccone, R. Rogi, R. Ferro, The Ce-Mg-Y system, Metall Mater Trans A 28, 265-276 (1997).  
_cited as the source of values for this phase_

## HCP_A3 (Ce–Y)

- Id: `phase:ce-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1752.15 K, x(Y) 0.6283–1
- Literature: 4 values (4 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-y:hcp-a3)

Names (6): _corpus: _corpus:phase:ce-y:hcp-a3  
_paper: _paper:10.1016/j.calphad.2006.02.002:hcp, paper:10.1016/j.ssi.2008.06.011:hcp  
_tdb: _tdb:CeY-06Men.tdb:HCP_A3, tdb:CeY-08Dju.tdb:HCP_A3, tdb:CeY-08Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CeY-06Men.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-06Men.tdb): HCP_A3, type code %A, sha256 `1ae8c2335e970ff1…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CE Y% : VA : !
~~~~

[CeY-08Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Dju.tdb): HCP_A3, type code %A, sha256 `dec06e9f8d832c22…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CE Y% : VA% : !
~~~~

[CeY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Guo.tdb): HCP_A3, type code %A, sha256 `6052d6790f767fad…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CE Y% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002) F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ce–Y system, Calphad 30, 323-325 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011) D DJUROVIC, M ZINKEVICH, F ALDINGER, Thermodynamic modeling of the cerium–yttrium–oxygen system, Solid State Ionics 179, 1902-1911 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_
- [doi:10.1007/s11661-997-0129-z](https://doi.org/10.1007/s11661-997-0129-z) H. Flandorfer, M. Giovannini, A. Saccone, R. Rogi, R. Ferro, The Ce-Mg-Y system, Metall Mater Trans A 28, 265-276 (1997).  
_cited as the source of values for this phase_

## LIQUID (Ce–Y)

- Id: `phase:ce-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1060.35–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-y:liquid)

Names (4): _corpus: _corpus:phase:ce-y:liquid  
_tdb: _tdb:CeY-06Men.tdb:LIQUID, tdb:CeY-08Dju.tdb:LIQUID, tdb:CeY-08Guo.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CeY-06Men.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-06Men.tdb): LIQUID, type code %, sha256 `1ae8c2335e970ff1…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CE Y : !
~~~~

[CeY-08Dju.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Dju.tdb): LIQUID, type code %, sha256 `dec06e9f8d832c22…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CE Y : !
~~~~

[CeY-08Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CeY-08Guo.tdb): LIQUID, type code %, sha256 `6052d6790f767fad…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CE Y : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2006.02.002](https://doi.org/10.1016/j.calphad.2006.02.002) F.G. Meng, L.B. Liu, H.S. Liu, Z.P. Jin, Thermodynamic assessment of the Ce–Y system, Calphad 30, 323-325 (2006).  
_assessment that models this phase_
- [doi:10.1016/j.ssi.2008.06.011](https://doi.org/10.1016/j.ssi.2008.06.011) D DJUROVIC, M ZINKEVICH, F ALDINGER, Thermodynamic modeling of the cerium–yttrium–oxygen system, Solid State Ionics 179, 1902-1911 (2008).  
_assessment that models this phase_
- [doi:10.3139/146.101685](https://doi.org/10.3139/146.101685) Cuiping Guo, Zhenmin Du, Changrong Li, Thermodynamic description of the Ce-Mg-Y and Mg-Nd-Y systems, International Journal of Materials Research 99, 650-688 (2008).  
_assessment that models this phase_

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
