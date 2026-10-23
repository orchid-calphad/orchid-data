# Ga–Pb phases

> Ga–Pb system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-PB.html · Markdown: https://data.orchid-project.org/phases/pages/GA-PB.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-PB) · [full JSON](https://data.orchid-project.org/phases/systems/GA-PB.json) · [Ga–Pb system page](https://data.orchid-project.org/systems/GA-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Pb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-pb-a11-orthorhombic); _phase:ga-pb:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(Pb) 0–0 | 6 | 2 |
| [BCC_A2](#phase-ga-pb-bcc-a2); _phase:ga-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ga-pb-fcc-a1); _phase:ga-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2499.36 K, x(Pb) 0.9955–1 | 7 | 2 |
| [HCP_A3](#phase-ga-pb-hcp-a3); _phase:ga-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ga-pb-liquid); _phase:ga-pb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 302.89–2500 K, x(Pb) 0–1 | 868 | 2 |

## ORTHORHOMBIC_A11 (Ga–Pb)

- Id: `phase:ga-pb:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(Pb) 0–0
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pb:a11-orthorhombic)

Names (5): _corpus: _corpus:phase:ga-pb:a11-orthorhombic, corpus:phase:ga-pb:orthorhombic-a11  
_paper: _paper:10.1007/bf02663678:Ga  
_tdb: _tdb:GaPb-91Ans-LB.tdb:ORTHORHOMBIC_A11, tdb:GaPb-96Mat.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[GaPb-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-91Ans-LB.tdb): ORTHORHOMBIC_A11, type code %, sha256 `b7c0fac2fcf8ff89…`

~~~~text
40: PHASE ORTHORHOMBIC_A11 % 1 1 !
41: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaPb-96Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-96Mat.tdb): ORTHORHOMBIC_A11, type code %, sha256 `7659e972abe1c767…`

~~~~text
42: PHASE ORTHORHOMBIC_A11 % 1 1 !
43: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663678](https://doi.org/10.1007/BF02663678) I. Ansara, F. Ajersch, J. Phase Equilib., 12, 73-77(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7) M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996).  
_assessment that models this phase_
- [doi:10.1002/zaac.19322090318](https://doi.org/10.1002/zaac.19322090318) N. A. Puschin, S. Stepanović, V. Stajić, Über die Legierungen des Galliums mit Zink, Cadmium, Quecksilber, Zinn, Blei, Wismut und Aluminium, Z. Anorg. Allg. Chem. 209, 329-334 (1932).  
_cited as the source of values for this phase_

## BCC_A2 (Ga–Pb)

- Id: `phase:ga-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pb:bcc-a2)

Names (3): _corpus: _corpus:phase:ga-pb:bcc-a2  
_tdb: _tdb:GaPb-91Ans-LB.tdb:BCC_A2, tdb:GaPb-96Mat.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GaPb-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-91Ans-LB.tdb): BCC_A2, type code %B, sha256 `b7c0fac2fcf8ff89…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GA PB : VA : !
~~~~

[GaPb-96Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-96Mat.tdb): BCC_A2, type code %B, sha256 `7659e972abe1c767…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : GA PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02663678](https://doi.org/10.1007/BF02663678) I. Ansara, F. Ajersch, J. Phase Equilib., 12, 73-77(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7) M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996).  
_assessment that models this phase_

## FCC_A1 (Ga–Pb)

- Id: `phase:ga-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2499.36 K, x(Pb) 0.9955–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pb:fcc-a1)

Names (5): _corpus: _corpus:phase:ga-pb:fcc-a1  
_paper: _paper:10.1007/bf02663678:(Pb), paper:10.1007/bf02663678:Pb  
_tdb: _tdb:GaPb-91Ans-LB.tdb:FCC_A1, tdb:GaPb-96Mat.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GaPb-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-91Ans-LB.tdb): FCC_A1, type code %A, sha256 `b7c0fac2fcf8ff89…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GA PB : VA : !
~~~~

[GaPb-96Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-96Mat.tdb): FCC_A1, type code %A, sha256 `7659e972abe1c767…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : GA PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02663678](https://doi.org/10.1007/BF02663678) I. Ansara, F. Ajersch, J. Phase Equilib., 12, 73-77(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7) M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996).  
_assessment that models this phase_
- [doi:10.1002/zaac.19322090318](https://doi.org/10.1002/zaac.19322090318) N. A. Puschin, S. Stepanović, V. Stajić, Über die Legierungen des Galliums mit Zink, Cadmium, Quecksilber, Zinn, Blei, Wismut und Aluminium, Z. Anorg. Allg. Chem. 209, 329-334 (1932).  
_cited as the source of values for this phase_

## HCP_A3 (Ga–Pb)

- Id: `phase:ga-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pb:hcp-a3)

Names (3): _corpus: _corpus:phase:ga-pb:hcp-a3  
_tdb: _tdb:GaPb-91Ans-LB.tdb:HCP_A3, tdb:GaPb-96Mat.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GaPb-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-91Ans-LB.tdb): HCP_A3, type code %A, sha256 `b7c0fac2fcf8ff89…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GA PB : VA : !
~~~~

[GaPb-96Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-96Mat.tdb): HCP_A3, type code %A, sha256 `7659e972abe1c767…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : GA PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02663678](https://doi.org/10.1007/BF02663678) I. Ansara, F. Ajersch, J. Phase Equilib., 12, 73-77(1991).  
_assessment that models this phase_
- [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7) M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996).  
_assessment that models this phase_

## LIQUID (Ga–Pb)

- Id: `phase:ga-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 302.89–2500 K, x(Pb) 0–1
- Literature: 868 values (866 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-pb:liquid)

Names (7): _corpus: _corpus:phase:ga-pb:liquid  
_paper: _paper:10.1007/bf02663678:L, paper:10.1007/bf02663678:L1, paper:10.1007/bf02663678:L2, paper:10.1016/0925-8388(95)02178-7:liquid  
_tdb: _tdb:GaPb-91Ans-LB.tdb:LIQUID, tdb:GaPb-96Mat.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GaPb-91Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-91Ans-LB.tdb): LIQUID, type code %, sha256 `b7c0fac2fcf8ff89…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GA PB : !
~~~~

[GaPb-96Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/GaPb-96Mat.tdb): LIQUID, type code %, sha256 `7659e972abe1c767…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : GA PB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1016/0925-8388(95)02178-7](https://doi.org/10.1016/0925-8388%2895%2902178-7) M. Mathon, J.M. Miane, P. Gaune, M. Gambino, J.P. Bros, Gallium + lead system: molar heat capacity and miscibility gap, Journal of Alloys and Compounds 237, 155-164 (1996).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02663678](https://doi.org/10.1007/BF02663678) I. Ansara, F. Ajersch, J. Phase Equilib., 12, 73-77(1991).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(73)90149-5](https://doi.org/10.1016/0022-5088%2873%2990149-5) A.F. Kwong, Z.A. Munir, Thermodynamic properties of liquid gallium-lead alloys, Journal of the Less Common Metals 30, 387-395 (1973).  
_cited as the source of values for this phase_
- [doi:10.1021/je60056a024](https://doi.org/10.1021/je60056a024) Alessandro Desideri, Vincenzo Piacente, Thermodynamic properties of liquid gallium alloys. I. Gallium-lead, J. Chem. Eng. Data 18, 90-93 (1973).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19322090318](https://doi.org/10.1002/zaac.19322090318) N. A. Puschin, S. Stepanović, V. Stajić, Über die Legierungen des Galliums mit Zink, Cadmium, Quecksilber, Zinn, Blei, Wismut und Aluminium, Z. Anorg. Allg. Chem. 209, 329-334 (1932).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(71)90093-2](https://doi.org/10.1016/0022-5088%2871%2990093-2) B Predel, D.W Stein, Thermodynamische Untersuchung der Systeme Gallium-Blei und Gallium-Thallium, Journal of the Less Common Metals 24, 159-171 (1971).  
_cited as the source of values for this phase_

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
