# Ge–K phases

> Ge–K system: 8 phases (tier A 4, tier B 1, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-K.html · Markdown: https://data.orchid-project.org/phases/pages/GE-K.md

8 phases (tier A 4, tier B 1, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-K) · [full JSON](https://data.orchid-project.org/phases/systems/GE-K.json) · [Ge–K system page](https://data.orchid-project.org/systems/GE-K.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-K.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–K system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-k-a4-diamond); _phase:ge-k:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(K) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ge-k-bcc-a2); _phase:ge-k:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(K) 1–1 | 0 | 1 |
| [FCC_A1](#phase-ge-k-fcc-a1); _phase:ge-k:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE4K](#phase-ge-k-ge4k); _phase:ge-k:ge4k_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1398.17 K, x(K) 0.2–0.2 | 1 | 1 |
| [GEK](#phase-ge-k-gek); _phase:ge-k:gek_ | GeK · cP64 · P-43n (218) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1364.17 K, x(K) 0.5–0.5 | 2 | 1 |
| [GEK3](#phase-ge-k-gek3); _phase:ge-k:gek3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1156.87 K, x(K) 0.75–0.75 | 0 | 1 |
| [HCP_A3](#phase-ge-k-hcp-a3); _phase:ge-k:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-k-liquid); _phase:ge-k:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 333.75–2500 K, x(K) 0–1 | 0 | 1 |

## DIAMOND_A4 (Ge–K)

- Id: `phase:ge-k:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1211.4 K, x(K) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:a4-diamond)

Names (2): _corpus: _corpus:phase:ge-k:a4-diamond  
_tdb: _tdb:GeK-12Wan.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): DIAMOND_A4, type code %, sha256 `d591f02833106db8…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## BCC_A2 (Ge–K)

- Id: `phase:ge-k:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(K) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-k:bcc-a2  
_tdb: _tdb:GeK-12Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): BCC_A2, type code %B, sha256 `d591f02833106db8…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GE K% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## FCC_A1 (Ge–K)

- Id: `phase:ge-k:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-k:fcc-a1  
_tdb: _tdb:GeK-12Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): FCC_A1, type code %A, sha256 `d591f02833106db8…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GE K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## GE4K (Ge–K)

- Id: `phase:ge-k:ge4k`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Ge4K) — Hallstedt 2025 mmc2 row for GE4K: Ge4K
- Stoichiometry: Ge 0.8000, K 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1398.17 K, x(K) 0.2–0.2
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:ge4k)

Names (3): _corpus: _corpus:phase:ge-k:ge4k  
_paper: _paper:10.1016/j.calphad.2012.01.004:Ge4K  
_tdb: _tdb:GeK-12Wan.tdb:GE4K  


### TDB models of GE4K (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): GE4K, type code %, sha256 `d591f02833106db8…`

~~~~text
48: PHASE GE4K % 2 4 1 !
49: CONST GE4K : GE : K : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase; reports values for this phase_

## GEK (Ge–K)

- Id: `phase:ge-k:gek`; status `assigned`
- Structure: GeK · cP64 · P-43n (218); type `st:gek-cp64`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ge 0.5000, K 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1364.17 K, x(K) 0.5–0.5
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:gek)

Names (5): _corpus: _corpus:phase:ge-k:gek  
_mp: _mp:mp-aaaaadeo  
_oqmd: _oqmd:oqmd-649065  
_paper: _paper:10.1016/j.calphad.2012.01.004:GeK  
_tdb: _tdb:GeK-12Wan.tdb:GEK  


### TDB models of GEK (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): GEK, type code %, sha256 `d591f02833106db8…`

~~~~text
53: PHASE GEK % 2 1 1 !
54: CONST GEK : GE : K : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19613120310](https://doi.org/10.1002/zaac.19613120310) R. Schäfer, W. Klemm, Das Verhalten der Alkalimetalle zu Halbmetallen. IX. Weitere Beiträge zur Kenntnis der Silicide und Germanide der Alkalimetalle, Zeitschrift anorg allge chemie 312, 214-220 (1961).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19613130108](https://doi.org/10.1002/zaac.19613130108) E. Busmann, Das Verhalten der Alkalimetalle zu Halbmetallen. X. Die Kristallstrukturen von KSi, RbSi, CsSi, KGe, RbGe und CsGe, Zeitschrift anorg allge chemie 313, 90-106 (1961).  
_cited as the source of values for this phase_

## GEK3 (Ge–K)

- Id: `phase:ge-k:gek3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (GeK3) — Hallstedt 2025 mmc2 row for GEK3: GeK3
- Stoichiometry: Ge 0.2500, K 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1156.87 K, x(K) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:gek3)

Names (2): _corpus: _corpus:phase:ge-k:gek3  
_tdb: _tdb:GeK-12Wan.tdb:GEK3  


### TDB models of GEK3 (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): GEK3, type code %, sha256 `d591f02833106db8…`

~~~~text
58: PHASE GEK3 % 2 1 3 !
59: CONST GEK3 : GE : K : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## HCP_A3 (Ge–K)

- Id: `phase:ge-k:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-k:hcp-a3  
_tdb: _tdb:GeK-12Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): HCP_A3, type code %A, sha256 `d591f02833106db8…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GE K : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## LIQUID (Ge–K)

- Id: `phase:ge-k:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 333.75–2500 K, x(K) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-k:liquid)

Names (2): _corpus: _corpus:phase:ge-k:liquid  
_tdb: _tdb:GeK-12Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeK-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeK-12Wan.tdb): LIQUID, type code %, sha256 `d591f02833106db8…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GE K : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
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
