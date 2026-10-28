# Cu–Pt phases

> Cu–Pt system: 6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CU-PT.html · Markdown: https://data.orchid-project.org/phases/pages/CU-PT.md

6 phases (tier A 4, liquid 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CU-PT) · [full JSON](https://data.orchid-project.org/phases/systems/CU-PT.json) · [Cu–Pt system page](https://data.orchid-project.org/systems/CU-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/CU-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cu–Pt system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cu-pt-bcc-a2); _phase:cu-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [CUPT_L11](#phase-cu-pt-cupt-l11); _phase:cu-pt:cupt-l11_ | CuPt · L1_1 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1094.25 K, x(Pt) 0.36146–0.68399 | 5 | 1 |
| [FCC_4SL](#phase-cu-pt-fcc-4sl); _phase:cu-pt:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2041.5 K, x(Pt) 0–1 | 15 | 1 |
| [FCC_A1](#phase-cu-pt-fcc-a1); _phase:cu-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2030 K, x(Pt) 0–0.98 | 0 | 2 |
| [HCP_A3](#phase-cu-pt-hcp-a3); _phase:cu-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-cu-pt-liquid); _phase:cu-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1357.77–2500 K, x(Pt) 0–1 | 0 | 1 |

## BCC_A2 (Cu–Pt)

- Id: `phase:cu-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pt:bcc-a2)

Names (2): _corpus: _corpus:phase:cu-pt:bcc-a2  
_tdb: _tdb:CuPt-06Abe.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): BCC_A2, type code %B, sha256 `22e617239e135878…`

~~~~text
53: PHASE BCC_A2 %B 2 1 3 !
54: CONST BCC_A2 : CU PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006).  
_assessment that models this phase_

## CUPT_L11 (Cu–Pt)

- Id: `phase:cu-pt:cupt-l11`; status `assigned`
- Structure: CuPt · L1_1 · hR2 · R-3m (166); type `st:l1-1-cupt-hr2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CuPt-06Abe.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1094.25 K, x(Pt) 0.36146–0.68399
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pt:cupt-l11)

Names (3): _corpus: _corpus:phase:cu-pt:cupt-l11  
_paper: _paper:10.1361/105497196x92736:L11-CuPt  
_tdb: _tdb:CuPt-06Abe.tdb:CUPT_L11  


### TDB models of CUPT_L11 (1): PHASE and CONSTITUENT statements as written

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): CUPT_L11, type code %, sha256 `22e617239e135878…`

~~~~text
63: PHASE CUPT_L11 % 2 0.5 0.5 !
64: CONST CUPT_L11 : CU% PT : CU PT% : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0001-6160(62)90102-5](https://doi.org/10.1016/0001-6160%2862%2990102-5) R Oriani, W.K Murphy, Thermodynamics of ordering alloys—IV heats of formation of some alloys of transition metals, Acta Metallurgica 10, 879-885 (1962).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.39.5792](https://doi.org/10.1103/physrevb.39.5792) Satoshi Takizawa, Kiyoyuki Terakura, Tetsuo Mohri, Electronic theory for phase stability of nine\<i>AB\</i>binary alloys, with\<i>A=\</i>Ni, Pd, or Pt and\<i>B=\</i>Cu, Ag, or Au, Phys. Rev. B 39, 5792-5797 (1989).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.44.512](https://doi.org/10.1103/physrevb.44.512) Z. W. Lu, S.-H. Wei, Alex Zunger, S. Frota-Pessoa, L. G. Ferreira, First-principles statistical mechanics of structural stability of intermetallic compounds, Phys. Rev. B 44, 512-544 (1991).  
_cited as the source of values for this phase_
- [doi:10.1143/jpsj.65.2178](https://doi.org/10.1143/jpsj.65.2178) Satoshi Takizawa, A New Phase of Cu–Pt Alloy – Theoretical Prediction and Experimental Support, J. Phys. Soc. Jpn. 65, 2178-2181 (1996).  
_cited as the source of values for this phase_

## FCC_4SL (Cu–Pt)

- Id: `phase:cu-pt:fcc-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:CuPt-06Abe.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Pm-3m (221) — on-hull MP Cu3Pt at x(PT)=0.2500
- Candidate (dft_mp): R-3m (166) — on-hull MP CuPt at x(PT)=0.5000
- Candidate (dft_mp): Fm-3m (225) — on-hull MP CuPt7 at x(PT)=0.8750
- Candidate (dft_oqmd): R-3m (166) — on-hull OQMD Cu1 Pt1 at x(PT)=0.5000
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Cu1 Pt3 at x(PT)=0.7500
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Cu1 Pt7 at x(PT)=0.8750
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Cu3 Pt1 at x(PT)=0.2500
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Cu7 Pt1 at x(PT)=0.1250
- Stability: stable in 1 of 1 calculated diagram(s): 300–2041.5 K, x(Pt) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pt:fcc-4sl)

Names (5): _corpus: _corpus:phase:cu-pt:fcc-4sl  
_paper: _paper:10.1361/105497196x92736:L10-CuPt, paper:10.1361/105497196x92736:L12-Cu3Pt, paper:10.1361/105497196x92736:L12-CuPt3  
_tdb: _tdb:CuPt-06Abe.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): FCC_4SL, type code %AY, sha256 `22e617239e135878…`

~~~~text
48: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
49: CONST FCC_4SL : CU% PT : CU PT% : CU PT% : CU PT% : VA :  !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1103/physrevb.39.5792](https://doi.org/10.1103/physrevb.39.5792) Satoshi Takizawa, Kiyoyuki Terakura, Tetsuo Mohri, Electronic theory for phase stability of nine\<i>AB\</i>binary alloys, with\<i>A=\</i>Ni, Pd, or Pt and\<i>B=\</i>Cu, Ag, or Au, Phys. Rev. B 39, 5792-5797 (1989).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.44.512](https://doi.org/10.1103/physrevb.44.512) Z. W. Lu, S.-H. Wei, Alex Zunger, S. Frota-Pessoa, L. G. Ferreira, First-principles statistical mechanics of structural stability of intermetallic compounds, Phys. Rev. B 44, 512-544 (1991).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevlett.88.255506](https://doi.org/10.1103/physrevlett.88.255506) G. H. Jóhannesson, T. Bligaard, A. V. Ruban, H. L. Skriver, K. W. Jacobsen, J. K. Nørskov, Combined Electronic Structure and Evolutionary Search Approach to Materials Design, Phys. Rev. Lett. 88 (2002).  
_cited as the source of values for this phase_
- [doi:10.1143/jpsj.65.2178](https://doi.org/10.1143/jpsj.65.2178) Satoshi Takizawa, A New Phase of Cu–Pt Alloy – Theoretical Prediction and Experimental Support, J. Phys. Soc. Jpn. 65, 2178-2181 (1996).  
_cited as the source of values for this phase_

## FCC_A1 (Cu–Pt)

- Id: `phase:cu-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2030 K, x(Pt) 0–0.98
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pt:fcc-a1)

Names (3): _corpus: _corpus:phase:cu-pt:fcc-a1  
_tdb: _tdb:CuPt-06Abe.tdb:A1_FCC, tdb:CuPt-06Abe.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): A1_FCC, type code %A, sha256 `22e617239e135878…`

~~~~text
43: PHASE A1_FCC %A 2 1 1 !
44: CONST A1_FCC : CU PT : VA : !
~~~~

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): FCC_A1, type code %A, sha256 `22e617239e135878…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : CU PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006).  
_assessment that models this phase_

## HCP_A3 (Cu–Pt)

- Id: `phase:cu-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:cu-pt:hcp-a3  
_tdb: _tdb:CuPt-06Abe.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): HCP_A3, type code %A, sha256 `22e617239e135878…`

~~~~text
58: PHASE HCP_A3 %A 2 1 0.5 !
59: CONST HCP_A3 : CU PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006).  
_assessment that models this phase_

## LIQUID (Cu–Pt)

- Id: `phase:cu-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1357.77–2500 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cu-pt:liquid)

Names (2): _corpus: _corpus:phase:cu-pt:liquid  
_tdb: _tdb:CuPt-06Abe.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CuPt-06Abe.tdb](https://orchid-project.org/data/databases/sgte-binary/CuPt-06Abe.tdb): LIQUID, type code %, sha256 `22e617239e135878…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : CU PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497196X92736](https://doi.org/10.1361/105497196X92736) T. Abe, B. Sundman, H. Onodera, J. Phase Equilib. Diffus., 27, 5-13(2006).  
_assessment that models this phase_

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
