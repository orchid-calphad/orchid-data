# Cd–Na phases

> Cd–Na system: 6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-NA.html · Markdown: https://data.orchid-project.org/phases/pages/CD-NA.md

6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-NA) · [full JSON](https://data.orchid-project.org/phases/systems/CD-NA.json) · [Cd–Na system page](https://data.orchid-project.org/systems/CD-NA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Na system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-na-bcc-a2); _phase:cd-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(Na) 1–1 | 2 | 1 |
| [CD11NA2_D8C](#phase-cd-na-cd11na2-d8c); _phase:cd-na:cd11na2-d8c_ | Mg2Zn11 · D8_c · cP39 · Pm-3 (200) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–631.51 K, x(Na) 0.15385–0.15385 | 8 | 1 |
| [CD2NA](#phase-cd-na-cd2na); _phase:cd-na:cd2na_ | Cd2Na · cF1192 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–653.87 K, x(Na) 0.33333–0.33333 | 10 | 1 |
| [FCC_A1](#phase-cd-na-fcc-a1); _phase:cd-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cd-na-hcp-a3); _phase:cd-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–605.96 K, x(Na) 0–0 | 3 | 1 |
| [LIQUID](#phase-cd-na-liquid); _phase:cd-na:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 368.4–2500 K, x(Na) 0–1 | 16 | 1 |

## BCC_A2 (Cd–Na)

- Id: `phase:cd-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–370.87 K, x(Na) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-na:bcc-a2)

Names (3): _corpus: _corpus:phase:cd-na:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2008.05.106:bcc  
_tdb: _tdb:CdNa-09Liu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdNa-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb): BCC_A2, type code %B, sha256 `4bd4b64380b14098…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CD NA% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070520117](https://doi.org/10.1002/zaac.19070520117) N. S. Kurnakow, A. N. Kusnetzow, Cadmide des Natriums, Z. Anorg. Chem. 52, 173-185 (1907).  
_cited as the source of values for this phase_

## CD11NA2_D8C (Cd–Na)

- Id: `phase:cd-na:cd11na2-d8c`; status `assigned`
- Structure: Mg2Zn11 · D8_c · cP39 · Pm-3 (200); type `st:d8-c-mg2zn11-cp39`; tier A: standard phase name; confidence high
- Stoichiometry: Cd 0.8462, Na 0.1538
- Stability: stable in 1 of 1 calculated diagram(s): 300–631.51 K, x(Na) 0.15385–0.15385
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-na:cd11na2-d8c)

Names (3): _corpus: _corpus:phase:cd-na:cd11na2-d8c  
_paper: _paper:10.1016/j.jallcom.2008.05.106:Cd11Na2  
_tdb: _tdb:CdNa-09Liu.tdb:CD11NA2_D8C  


### TDB models of CD11NA2_D8C (1): PHASE and CONSTITUENT statements as written

[CdNa-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb): CD11NA2_D8C, type code %, sha256 `4bd4b64380b14098…`

~~~~text
42: PHASE CD11NA2_D8C % 2 11 2 !
43: CONST CD11NA2_D8C : CD : NA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070520117](https://doi.org/10.1002/zaac.19070520117) N. S. Kurnakow, A. N. Kusnetzow, Cadmide des Natriums, Z. Anorg. Chem. 52, 173-185 (1907).  
_cited as the source of values for this phase_

## CD2NA (Cd–Na)

- Id: `phase:cd-na:cd2na`; status `assigned`
- Structure: Cd2Na · cF1192 · Fd-3m (227); type `st:cd2na-cf1192`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cd 0.6667, Na 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–653.87 K, x(Na) 0.33333–0.33333
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-na:cd2na)

Names (3): _corpus: _corpus:phase:cd-na:cd2na  
_paper: _paper:10.1016/j.jallcom.2008.05.106:Cd2Na  
_tdb: _tdb:CdNa-09Liu.tdb:CD2NA  


### TDB models of CD2NA (1): PHASE and CONSTITUENT statements as written

[CdNa-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb): CD2NA, type code %, sha256 `4bd4b64380b14098…`

~~~~text
47: PHASE CD2NA % 2 2 1 !
48: CONST CD2NA : CD : NA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070520117](https://doi.org/10.1002/zaac.19070520117) N. S. Kurnakow, A. N. Kusnetzow, Cadmide des Natriums, Z. Anorg. Chem. 52, 173-185 (1907).  
_cited as the source of values for this phase_

## FCC_A1 (Cd–Na)

- Id: `phase:cd-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-na:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-na:fcc-a1  
_tdb: _tdb:CdNa-09Liu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdNa-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb): FCC_A1, type code %A, sha256 `4bd4b64380b14098…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CD NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009).  
_assessment that models this phase_

## HCP_A3 (Cd–Na)

- Id: `phase:cd-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–605.96 K, x(Na) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-na:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-na:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2008.05.106:hcp  
_tdb: _tdb:CdNa-09Liu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdNa-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb): HCP_A3, type code %A, sha256 `4bd4b64380b14098…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CD% NA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070520117](https://doi.org/10.1002/zaac.19070520117) N. S. Kurnakow, A. N. Kusnetzow, Cadmide des Natriums, Z. Anorg. Chem. 52, 173-185 (1907).  
_cited as the source of values for this phase_

## LIQUID (Cd–Na)

- Id: `phase:cd-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 368.4–2500 K, x(Na) 0–1
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-na:liquid)

Names (4): _corpus: _corpus:phase:cd-na:liquid  
_paper: _paper:10.1016/j.jallcom.2008.05.106:L, paper:10.1016/j.jallcom.2008.05.106:liquid  
_tdb: _tdb:CdNa-09Liu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdNa-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdNa-09Liu.tdb): LIQUID, type code %, sha256 `4bd4b64380b14098…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CD NA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.05.106](https://doi.org/10.1016/j.jallcom.2008.05.106) Yajun Liu, Di Yu, Yang Ge, Thermodynamic optimization of the Cd–Na and Cd–Tl binary systems, Journal of Alloys and Compounds 473, 60-64 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19060500118](https://doi.org/10.1002/zaac.19060500118) C. H. Mathewson, Metallographische Mitteilung aus dem Institut für anorganische Chemie der Universität Göttingen. XXXIV. Natrium‐Blei‐, Natrium‐Kadmium‐, Natrium‐Wismut‐ und Natrium‐Antimonlegierungen, Z. Anorg. Chem. 50, 171-198 (1906).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070520117](https://doi.org/10.1002/zaac.19070520117) N. S. Kurnakow, A. N. Kusnetzow, Cadmide des Natriums, Z. Anorg. Chem. 52, 173-185 (1907).  
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
