# K–Na phases

> K–Na system: 5 phases (tier A 4, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/K-NA.html · Markdown: https://data.orchid-project.org/phases/pages/K-NA.md

5 phases (tier A 4, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=K-NA) · [full JSON](https://data.orchid-project.org/phases/systems/K-NA.json) · [K–Na system page](https://data.orchid-project.org/systems/K-NA.html) · [Markdown](https://data.orchid-project.org/phases/pages/K-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the K–Na system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-k-na-bcc-a2); _phase:k-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 298.34–370.87 K, x(Na) 0–1 | 15 | 2 |
| [FCC_A1](#phase-k-na-fcc-a1); _phase:k-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-k-na-hcp-a3); _phase:k-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [KNA2_C14](#phase-k-na-kna2-c14); _phase:k-na:kna2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 15 | 2 |
| [LIQUID](#phase-k-na-liquid); _phase:k-na:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 298.34–2500 K, x(Na) 0–1 | 15 | 2 |

## BCC_A2 (K–Na)

- Id: `phase:k-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 298.34–370.87 K, x(Na) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-na:bcc-a2)

Names (5): _corpus: _corpus:phase:k-na:bcc-a2  
_paper: _paper:10.1016/j.msea.2005.11.037:bcc (K), paper:10.1016/j.msea.2005.11.037:bcc (Na)  
_tdb: _tdb:KNa-06Zha.tdb:BCC_A2, tdb:KNa-11Ren.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[KNa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-06Zha.tdb): BCC_A2, type code %B, sha256 `07051d7fbcc606b0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : K NA : VA : !
~~~~

[KNa-11Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-11Ren.tdb): BCC_A2, type code %B, sha256 `25965ca4d96d0c6d…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : K NA : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.06.005](https://doi.org/10.1016/j.calphad.2011.06.005) Xin Ren, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic assessments of six binary systems of alkali metals, Calphad 35, 446-454 (2011).  
_assessment that models this phase_
- [doi:10.1002/zaac.19020300105](https://doi.org/10.1002/zaac.19020300105) N. S. Kurnakow, N. A. Puschin, Über die Schmeltztemperaturen der Legierungen des Natriums mit Kalium, Z. Anorg. Chem. 30, 109-112 (1902).  
_cited as the source of values for this phase_
- [doi:10.1021/j150551a004](https://doi.org/10.1021/j150551a004) C. A. Krier, R. S. Craig, W. E. Wallace, Low Temperature Heat Capacities and Related Properties of Potassium and Na\<sub>2\</sub>K, J. Phys. Chem. 61, 522-529 (1957).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9696502870](https://doi.org/10.1039/tf9696502870) J. B. Ott, J. R. Goates, D. R. Anderson, H. T. Hall, Solid-liquid phase equilibria in the sodium + potassium system, Trans. Faraday Soc. 65, 2870 (1969).  
_cited as the source of values for this phase_
- [doi:10.1139/p56-045](https://doi.org/10.1139/p56-045) D. K. C. MacDonald, W. B. Pearson, Lois T. Towle, AN INVESTIGATION OF THE SODIUM-POTASSIUM EQUILIBRIUM DIAGRAM, Can. J. Phys. 34, 389-394 (1956).  
_cited as the source of values for this phase_

## FCC_A1 (K–Na)

- Id: `phase:k-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-na:fcc-a1)

Names (3): _corpus: _corpus:phase:k-na:fcc-a1  
_tdb: _tdb:KNa-06Zha.tdb:FCC_A1, tdb:KNa-11Ren.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[KNa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-06Zha.tdb): FCC_A1, type code %A, sha256 `07051d7fbcc606b0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : K NA : VA : !
~~~~

[KNa-11Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-11Ren.tdb): FCC_A1, type code %A, sha256 `25965ca4d96d0c6d…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : K NA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.06.005](https://doi.org/10.1016/j.calphad.2011.06.005) Xin Ren, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic assessments of six binary systems of alkali metals, Calphad 35, 446-454 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## HCP_A3 (K–Na)

- Id: `phase:k-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-na:hcp-a3)

Names (3): _corpus: _corpus:phase:k-na:hcp-a3  
_tdb: _tdb:KNa-06Zha.tdb:HCP_A3, tdb:KNa-11Ren.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[KNa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-06Zha.tdb): HCP_A3, type code %, sha256 `07051d7fbcc606b0…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : K NA : VA : !
~~~~

[KNa-11Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-11Ren.tdb): HCP_A3, type code %, sha256 `25965ca4d96d0c6d…`

~~~~text
35: PHASE HCP_A3 % 2 1 0.5 !
36: CONST HCP_A3 : K NA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2011.06.005](https://doi.org/10.1016/j.calphad.2011.06.005) Xin Ren, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic assessments of six binary systems of alkali metals, Calphad 35, 446-454 (2011).  
_assessment that models this phase_
- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase_

## KNA2_C14 (K–Na)

- Id: `phase:k-na:kna2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: K 0.3333, Na 0.6667
- Stability: not stable in 2 calculated diagram(s)
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-na:kna2-c14)

Names (4): _corpus: _corpus:phase:k-na:kna2-c14  
_paper: _paper:10.1016/j.msea.2005.11.037:KNa2  
_tdb: _tdb:KNa-06Zha.tdb:KNA2_C14, tdb:KNa-11Ren.tdb:KNA2_C14  


### TDB models of KNA2_C14 (2): PHASE and CONSTITUENT statements as written

[KNa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-06Zha.tdb): KNA2_C14, type code %, sha256 `07051d7fbcc606b0…`

~~~~text
41: PHASE KNA2_C14 % 2 1 2 !
42: CONST KNA2_C14 : K : NA : !
~~~~

[KNa-11Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-11Ren.tdb): KNA2_C14, type code %, sha256 `25965ca4d96d0c6d…`

~~~~text
40: PHASE KNA2_C14 % 2 1 2 !
41: CONST KNA2_C14 : K : NA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.06.005](https://doi.org/10.1016/j.calphad.2011.06.005) Xin Ren, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic assessments of six binary systems of alkali metals, Calphad 35, 446-454 (2011).  
_assessment that models this phase_
- [doi:10.1002/zaac.19020300105](https://doi.org/10.1002/zaac.19020300105) N. S. Kurnakow, N. A. Puschin, Über die Schmeltztemperaturen der Legierungen des Natriums mit Kalium, Z. Anorg. Chem. 30, 109-112 (1902).  
_cited as the source of values for this phase_
- [doi:10.1021/j150551a004](https://doi.org/10.1021/j150551a004) C. A. Krier, R. S. Craig, W. E. Wallace, Low Temperature Heat Capacities and Related Properties of Potassium and Na\<sub>2\</sub>K, J. Phys. Chem. 61, 522-529 (1957).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9696502870](https://doi.org/10.1039/tf9696502870) J. B. Ott, J. R. Goates, D. R. Anderson, H. T. Hall, Solid-liquid phase equilibria in the sodium + potassium system, Trans. Faraday Soc. 65, 2870 (1969).  
_cited as the source of values for this phase_
- [doi:10.1139/p56-045](https://doi.org/10.1139/p56-045) D. K. C. MacDonald, W. B. Pearson, Lois T. Towle, AN INVESTIGATION OF THE SODIUM-POTASSIUM EQUILIBRIUM DIAGRAM, Can. J. Phys. 34, 389-394 (1956).  
_cited as the source of values for this phase_

## LIQUID (K–Na)

- Id: `phase:k-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 298.34–2500 K, x(Na) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-na:liquid)

Names (4): _corpus: _corpus:phase:k-na:liquid  
_paper: _paper:10.1016/j.msea.2005.11.037:Liquid  
_tdb: _tdb:KNa-06Zha.tdb:LIQUID, tdb:KNa-11Ren.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[KNa-06Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-06Zha.tdb): LIQUID, type code %, sha256 `07051d7fbcc606b0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : K NA : !
~~~~

[KNa-11Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/KNa-11Ren.tdb): LIQUID, type code %, sha256 `25965ca4d96d0c6d…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : K NA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/j.msea.2005.11.037](https://doi.org/10.1016/j.msea.2005.11.037) Shengjun Zhang, Carl Brubaker, Chao Jiang, Mei Yang, Yu Zhong, Qingyou Han et al., A combined first-principles calculation and thermodynamic modeling of the F–K–Na system, Materials Science and Engineering: A 418, 161-171 (2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.06.005](https://doi.org/10.1016/j.calphad.2011.06.005) Xin Ren, Changrong Li, Zhenmin Du, Cuiping Guo, Thermodynamic assessments of six binary systems of alkali metals, Calphad 35, 446-454 (2011).  
_assessment that models this phase_
- [doi:10.1002/zaac.19020300105](https://doi.org/10.1002/zaac.19020300105) N. S. Kurnakow, N. A. Puschin, Über die Schmeltztemperaturen der Legierungen des Natriums mit Kalium, Z. Anorg. Chem. 30, 109-112 (1902).  
_cited as the source of values for this phase_
- [doi:10.1021/j150551a004](https://doi.org/10.1021/j150551a004) C. A. Krier, R. S. Craig, W. E. Wallace, Low Temperature Heat Capacities and Related Properties of Potassium and Na\<sub>2\</sub>K, J. Phys. Chem. 61, 522-529 (1957).  
_cited as the source of values for this phase_
- [doi:10.1039/tf9696502870](https://doi.org/10.1039/tf9696502870) J. B. Ott, J. R. Goates, D. R. Anderson, H. T. Hall, Solid-liquid phase equilibria in the sodium + potassium system, Trans. Faraday Soc. 65, 2870 (1969).  
_cited as the source of values for this phase_
- [doi:10.1139/p56-045](https://doi.org/10.1139/p56-045) D. K. C. MacDonald, W. B. Pearson, Lois T. Towle, AN INVESTIGATION OF THE SODIUM-POTASSIUM EQUILIBRIUM DIAGRAM, Can. J. Phys. 34, 389-394 (1956).  
_cited as the source of values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
