# Ca–Li phases

> Ca–Li system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-LI.html · Markdown: https://data.orchid-project.org/phases/pages/CA-LI.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-LI) · [full JSON](https://data.orchid-project.org/phases/systems/CA-LI.json) · [Ca–Li system page](https://data.orchid-project.org/systems/CA-LI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-LI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Li system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-li-bcc-a2); _phase:ca-li:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1124 K, x(Li) 0–1 | 4 | 1 |
| [CALI2_C14](#phase-ca-li-cali2-c14); _phase:ca-li:cali2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–515.52 K, x(Li) 0.66667–0.66667 | 4 | 1 |
| [FCC_A1](#phase-ca-li-fcc-a1); _phase:ca-li:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–719.03 K, x(Li) 0–0.09611 | 4 | 1 |
| [HCP_A3](#phase-ca-li-hcp-a3); _phase:ca-li:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ca-li-liquid); _phase:ca-li:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 418.05–2500 K, x(Li) 0–1 | 6 | 1 |

## BCC_A2 (Ca–Li)

- Id: `phase:ca-li:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1124 K, x(Li) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-li:bcc-a2)

Names (4): _corpus: _corpus:phase:ca-li:bcc-a2  
_paper: _paper:10.1016/s0040-6031(01)00842-5:(Li), paper:10.1016/s0040-6031(01)00842-5:βCa  
_tdb: _tdb:CaLi-02Gro-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaLi-02Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb): BCC_A2, type code %B, sha256 `91ea24f374ce086f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CA% LI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873196](https://doi.org/10.1007/bf02873196) C. W. Bale, A. D. Pelton, The Ca−Li (Calcium-Lithium) system, JPE 8, 125-127 (1987).  
_cited as the source of values for this phase_

## CALI2_C14 (Ca–Li)

- Id: `phase:ca-li:cali2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 0.3333, Li 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–515.52 K, x(Li) 0.66667–0.66667
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-li:cali2-c14)

Names (3): _corpus: _corpus:phase:ca-li:cali2-c14  
_paper: _paper:10.1016/s0040-6031(01)00842-5:CaLi2  
_tdb: _tdb:CaLi-02Gro-LB.tdb:CALI2_C14  


### TDB models of CALI2_C14 (1): PHASE and CONSTITUENT statements as written

[CaLi-02Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb): CALI2_C14, type code %, sha256 `91ea24f374ce086f…`

~~~~text
41: PHASE CALI2_C14 % 2 1 2 !
42: CONST CALI2_C14 : CA : LI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873196](https://doi.org/10.1007/bf02873196) C. W. Bale, A. D. Pelton, The Ca−Li (Calcium-Lithium) system, JPE 8, 125-127 (1987).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–Li)

- Id: `phase:ca-li:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–719.03 K, x(Li) 0–0.09611
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-li:fcc-a1)

Names (3): _corpus: _corpus:phase:ca-li:fcc-a1  
_paper: _paper:10.1016/s0040-6031(01)00842-5:αCa  
_tdb: _tdb:CaLi-02Gro-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaLi-02Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb): FCC_A1, type code %A, sha256 `91ea24f374ce086f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CA% LI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873196](https://doi.org/10.1007/bf02873196) C. W. Bale, A. D. Pelton, The Ca−Li (Calcium-Lithium) system, JPE 8, 125-127 (1987).  
_cited as the source of values for this phase_

## HCP_A3 (Ca–Li)

- Id: `phase:ca-li:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-li:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-li:hcp-a3  
_tdb: _tdb:CaLi-02Gro-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaLi-02Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb): HCP_A3, type code %A, sha256 `91ea24f374ce086f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CA LI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002).  
_assessment that models this phase_

## LIQUID (Ca–Li)

- Id: `phase:ca-li:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 418.05–2500 K, x(Li) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-li:liquid)

Names (4): _corpus: _corpus:phase:ca-li:liquid  
_paper: _paper:10.1016/s0040-6031(01)00842-5:Liquid, paper:10.1016/s0040-6031(01)00842-5:liquid  
_tdb: _tdb:CaLi-02Gro-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaLi-02Gro-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CaLi-02Gro-LB.tdb): LIQUID, type code %, sha256 `91ea24f374ce086f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CA LI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0040-6031(01)00842-5](https://doi.org/10.1016/S0040-6031%2801%2900842-5) J. Groebner, R. Schmid-Fetzer, A. Pisch, C. Colinet, V.V. Pavlyuk, G.S. Dmytriv, D.G. Kevorkov, O.I. Bodak, Thermochim. Acta, 389, 85-94(2002).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02873196](https://doi.org/10.1007/bf02873196) C. W. Bale, A. D. Pelton, The Ca−Li (Calcium-Lithium) system, JPE 8, 125-127 (1987).  
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
