# Ca–Ni phases

> Ca–Ni system: 8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CA-NI.html · Markdown: https://data.orchid-project.org/phases/pages/CA-NI.md

8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CA-NI) · [full JSON](https://data.orchid-project.org/phases/systems/CA-NI.json) · [Ca–Ni system page](https://data.orchid-project.org/systems/CA-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CA-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ca–Ni system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ca-ni-bcc-a2); _phase:ca-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 716.15–1124.6 K, x(Ni) 0–0.00017 | 2 | 1 |
| [CA2NI7](#phase-ca-ni-ca2ni7); _phase:ca-ni:ca2ni7_ | Co7Gd2 · hR18 · R-3m (166) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1376.06 K, x(Ni) 0.77778–0.77778 | 4 | 1 |
| [CANI2_C15](#phase-ca-ni-cani2-c15); _phase:ca-ni:cani2-c15_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1119.79 K, x(Ni) 0.66667–0.66667 | 7 | 1 |
| [CANI3](#phase-ca-ni-cani3); _phase:ca-ni:cani3_ | Ni3Pu · hR12 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1252.09 K, x(Ni) 0.75–0.75 | 4 | 1 |
| [CANI5_D2D](#phase-ca-ni-cani5-d2d); _phase:ca-ni:cani5-d2d_ | CaCu5 · D2_d · hP6 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1461.99 K, x(Ni) 0.83333–0.83333 | 6 | 1 |
| [FCC_A1](#phase-ca-ni-fcc-a1); _phase:ca-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.19 K, x(Ni) 0–1 | 2 | 1 |
| [HCP_A3](#phase-ca-ni-hcp-a3); _phase:ca-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ca-ni-liquid); _phase:ca-ni:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 899.6–2500 K, x(Ni) 0–1 | 12 | 1 |

## BCC_A2 (Ca–Ni)

- Id: `phase:ca-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 716.15–1124.6 K, x(Ni) 0–0.00017
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:bcc-a2)

Names (3): _corpus: _corpus:phase:ca-ni:bcc-a2  
_paper: _paper:10.1016/j.calphad.2005.08.006:Ca-bcc  
_tdb: _tdb:CaNi-05Isl.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): BCC_A2, type code %B, sha256 `d411c40b677aa318…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CA% NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
_cited as the source of values for this phase_

## CA2NI7 (Ca–Ni)

- Id: `phase:ca-ni:ca2ni7`; status `assigned`
- Structure: Co7Gd2 · hR18 · R-3m (166); type `st:co7gd2-hr18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ca 0.2222, Ni 0.7778
- Stability: stable in 1 of 1 calculated diagram(s): 300–1376.06 K, x(Ni) 0.77778–0.77778
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:ca2ni7)

Names (5): _corpus: _corpus:phase:ca-ni:ca2ni7  
_mp: _mp:mp-aaackycj  
_oqmd: _oqmd:oqmd-2026083  
_paper: _paper:10.1016/j.calphad.2005.08.006:Ca2Ni7  
_tdb: _tdb:CaNi-05Isl.tdb:CA2NI7  


### TDB models of CA2NI7 (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): CA2NI7, type code %, sha256 `d411c40b677aa318…`

~~~~text
56: PHASE CA2NI7 % 2 2 7 !
57: CONST CA2NI7 : CA : NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
_cited as the source of values for this phase_

## CANI2_C15 (Ca–Ni)

- Id: `phase:ca-ni:cani2-c15`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 0.3333, Ni 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1119.79 K, x(Ni) 0.66667–0.66667
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:cani2-c15)

Names (3): _corpus: _corpus:phase:ca-ni:cani2-c15  
_paper: _paper:10.1016/j.calphad.2005.08.006:CaNi2  
_tdb: _tdb:CaNi-05Isl.tdb:CANI2_C15  


### TDB models of CANI2_C15 (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): CANI2_C15, type code %, sha256 `d411c40b677aa318…`

~~~~text
46: PHASE CANI2_C15 % 2 1 2 !
47: CONST CANI2_C15 : CA : NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
_cited as the source of values for this phase_

## CANI3 (Ca–Ni)

- Id: `phase:ca-ni:cani3`; status `assigned`
- Structure: Ni3Pu · hR12 · R-3m (166); type `st:ni3pu-hr12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ca 0.2500, Ni 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1252.09 K, x(Ni) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:cani3)

Names (3): _corpus: _corpus:phase:ca-ni:cani3  
_paper: _paper:10.1016/j.calphad.2005.08.006:CaNi3  
_tdb: _tdb:CaNi-05Isl.tdb:CANI3  


### TDB models of CANI3 (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): CANI3, type code %, sha256 `d411c40b677aa318…`

~~~~text
51: PHASE CANI3 % 2 1 3 !
52: CONST CANI3 : CA : NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
_cited as the source of values for this phase_

## CANI5_D2D (Ca–Ni)

- Id: `phase:ca-ni:cani5-d2d`; status `assigned`
- Structure: CaCu5 · D2_d · hP6 · P6/mmm (191); type `st:d2-d-cacu5-hp6`; tier A: standard phase name; confidence high
- Stoichiometry: Ca 0.1667, Ni 0.8333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1461.99 K, x(Ni) 0.83333–0.83333
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:cani5-d2d)

Names (3): _corpus: _corpus:phase:ca-ni:cani5-d2d  
_paper: _paper:10.1016/j.calphad.2005.08.006:CaNi5  
_tdb: _tdb:CaNi-05Isl.tdb:CANI5_D2D  


### TDB models of CANI5_D2D (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): CANI5_D2D, type code %, sha256 `d411c40b677aa318…`

~~~~text
61: PHASE CANI5_D2D % 2 1 5 !
62: CONST CANI5_D2D : CA : NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
_cited as the source of values for this phase_

## FCC_A1 (Ca–Ni)

- Id: `phase:ca-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.19 K, x(Ni) 0–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:fcc-a1)

Names (3): _corpus: _corpus:phase:ca-ni:fcc-a1  
_paper: _paper:10.1016/j.calphad.2005.08.006:Ni-fcc  
_tdb: _tdb:CaNi-05Isl.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): FCC_A1, type code %A, sha256 `d411c40b677aa318…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CA% NI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
_cited as the source of values for this phase_

## HCP_A3 (Ca–Ni)

- Id: `phase:ca-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:hcp-a3)

Names (2): _corpus: _corpus:phase:ca-ni:hcp-a3  
_tdb: _tdb:CaNi-05Isl.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): HCP_A3, type code %A, sha256 `d411c40b677aa318…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CA NI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase_

## LIQUID (Ca–Ni)

- Id: `phase:ca-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 899.6–2500 K, x(Ni) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ca-ni:liquid)

Names (3): _corpus: _corpus:phase:ca-ni:liquid  
_paper: _paper:10.1016/j.calphad.2005.08.006:L  
_tdb: _tdb:CaNi-05Isl.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CaNi-05Isl.tdb](https://orchid-project.org/data/databases/sgte-binary/CaNi-05Isl.tdb): LIQUID, type code %, sha256 `d411c40b677aa318…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CA NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2005.08.006](https://doi.org/10.1016/j.calphad.2005.08.006) F. Islam, M. Medraj, The phase equilibria in the Mg–Ni–Ca system, Calphad 29, 289-302 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(90)90338-k](https://doi.org/10.1016/0022-5088%2890%2990338-k) M. Notin, D. Belbacha, M. Rahmane, J. Hertz, G. Saindrenan, J.L. Jorda, Experimental diagram and numerical optimization of the CaNi system, Journal of the Less Common Metals 162, 221-229 (1990).  
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
