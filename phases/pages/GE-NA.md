# Ge–Na phases

> Ge–Na system: 8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GE-NA.html · Markdown: https://data.orchid-project.org/phases/pages/GE-NA.md

8 phases (tier A 4, tier C 1, liquid 1, needs_review 2); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GE-NA) · [full JSON](https://data.orchid-project.org/phases/systems/GE-NA.json) · [Ge–Na system page](https://data.orchid-project.org/systems/GE-NA.html) · [Markdown](https://data.orchid-project.org/phases/pages/GE-NA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ge–Na system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ge-na-a4-diamond); _phase:ge-na:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1216.5 K, x(Na) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ge-na-bcc-a2); _phase:ge-na:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–370.83 K, x(Na) 1–1 | 0 | 1 |
| [FCC_A1](#phase-ge-na-fcc-a1); _phase:ge-na:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GE4NA](#phase-ge-na-ge4na); _phase:ge-na:ge4na_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1430.13 K, x(Na) 0.2–0.2 | 0 | 1 |
| [GENA](#phase-ge-na-gena); _phase:ge-na:gena_ | GeNa · mP32 · P2_1/c (14) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1426.36 K, x(Na) 0.5–0.5 | 0 | 1 |
| [GENA3](#phase-ge-na-gena3); _phase:ge-na:gena3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1104.2 K, x(Na) 0.75–0.75 | 0 | 1 |
| [HCP_A3](#phase-ge-na-hcp-a3); _phase:ge-na:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ge-na-liquid); _phase:ge-na:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 370.83–2500 K, x(Na) 0–1 | 0 | 1 |

## DIAMOND_A4 (Ge–Na)

- Id: `phase:ge-na:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1216.5 K, x(Na) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:a4-diamond)

Names (2): _corpus: _corpus:phase:ge-na:a4-diamond  
_tdb: _tdb:GeNa-12Wan.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): DIAMOND_A4, type code %, sha256 `7b555c87d0a1d637…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## BCC_A2 (Ge–Na)

- Id: `phase:ge-na:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–370.83 K, x(Na) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:bcc-a2)

Names (2): _corpus: _corpus:phase:ge-na:bcc-a2  
_tdb: _tdb:GeNa-12Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): BCC_A2, type code %B, sha256 `7b555c87d0a1d637…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GE NA% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## FCC_A1 (Ge–Na)

- Id: `phase:ge-na:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:fcc-a1)

Names (2): _corpus: _corpus:phase:ge-na:fcc-a1  
_tdb: _tdb:GeNa-12Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): FCC_A1, type code %A, sha256 `7b555c87d0a1d637…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GE NA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## GE4NA (Ge–Na)

- Id: `phase:ge-na:ge4na`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Ge4Na) — Hallstedt 2025 mmc2 row for GE4NA: Ge4Na
- Stoichiometry: Ge 0.8000, Na 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1430.13 K, x(Na) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:ge4na)

Names (2): _corpus: _corpus:phase:ge-na:ge4na  
_tdb: _tdb:GeNa-12Wan.tdb:GE4NA  


### TDB models of GE4NA (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): GE4NA, type code %, sha256 `7b555c87d0a1d637…`

~~~~text
48: PHASE GE4NA % 2 4 1 !
49: CONST GE4NA : GE : NA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## GENA (Ge–Na)

- Id: `phase:ge-na:gena`; status `assigned`
- Structure: GeNa · mP32 · P2_1/c (14); type `st:gena-mp32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_14_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ge 0.5000, Na 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1426.36 K, x(Na) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:gena)

Names (2): _corpus: _corpus:phase:ge-na:gena  
_tdb: _tdb:GeNa-12Wan.tdb:GENA  


### TDB models of GENA (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): GENA, type code %, sha256 `7b555c87d0a1d637…`

~~~~text
53: PHASE GENA % 2 1 1 !
54: CONST GENA : GE : NA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## GENA3 (Ge–Na)

- Id: `phase:ge-na:gena3`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (GeNa3) — Hallstedt 2025 mmc2 row for GENA3: GeNa3
- Stoichiometry: Ge 0.2500, Na 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1104.2 K, x(Na) 0.75–0.75
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:gena3)

Names (2): _corpus: _corpus:phase:ge-na:gena3  
_tdb: _tdb:GeNa-12Wan.tdb:GENA3  


### TDB models of GENA3 (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): GENA3, type code %, sha256 `7b555c87d0a1d637…`

~~~~text
58: PHASE GENA3 % 2 1 3 !
59: CONST GENA3 : GE : NA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## HCP_A3 (Ge–Na)

- Id: `phase:ge-na:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:hcp-a3)

Names (2): _corpus: _corpus:phase:ge-na:hcp-a3  
_tdb: _tdb:GeNa-12Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): HCP_A3, type code %A, sha256 `7b555c87d0a1d637…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GE NA : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
_assessment that models this phase_

## LIQUID (Ge–Na)

- Id: `phase:ge-na:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 370.83–2500 K, x(Na) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ge-na:liquid)

Names (2): _corpus: _corpus:phase:ge-na:liquid  
_tdb: _tdb:GeNa-12Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GeNa-12Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/GeNa-12Wan.tdb): LIQUID, type code %, sha256 `7b555c87d0a1d637…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GE NA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.01.004](https://doi.org/10.1016/j.calphad.2012.01.004) Yaru Wang, Peisheng Wang, Dongdong Zhao, Biao Hu, Yong Du, Honghui Xu et al., Thermodynamic description of the Ge–Na and Ge–K systems using the CALPHAD approach supported by first-principles calculations, Calphad 37, 72-76 (2012).  
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
