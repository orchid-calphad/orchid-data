# Gd–Si phases

> Gd–Si system: 10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-SI.html · Markdown: https://data.orchid-project.org/phases/pages/GD-SI.md

10 phases (tier A 6, tier C 1, liquid 1, needs_review 2); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-SI) · [full JSON](https://data.orchid-project.org/phases/systems/GD-SI.json) · [Gd–Si system page](https://data.orchid-project.org/systems/GD-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Si system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-gd-si-a4-diamond); _phase:gd-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.54 K, x(Si) 1–1 | 0 | 1 |
| [BCC_A2](#phase-gd-si-bcc-a2); _phase:gd-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1508.16–1593.16 K, x(Si) 0–0 | 0 | 1 |
| [FCC_A1](#phase-gd-si-fcc-a1); _phase:gd-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GD3SI5_C32](#phase-gd-si-gd3si5-c32); _phase:gd-si:gd3si5-c32_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1936.19 K, x(Si) 0.625–0.625 | 0 | 1 |
| [GD5SI3_D88](#phase-gd-si-gd5si3-d88); _phase:gd-si:gd5si3-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2019.97 K, x(Si) 0.375–0.375 | 0 | 1 |
| [GD5SI4](#phase-gd-si-gd5si4); _phase:gd-si:gd5si4_ | Ge4Sm5 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2045.62 K, x(Si) 0.44444–0.44444 | 6 | 1 |
| [GDSI_B27](#phase-gd-si-gdsi-b27); _phase:gd-si:gdsi-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2107.12 K, x(Si) 0.5–0.5 | 0 | 1 |
| [GDSI2](#phase-gd-si-gdsi2); _phase:gd-si:gdsi2_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1874.01 K, x(Si) 0.66667–0.66667 | 0 | 1 |
| [HCP_A3](#phase-gd-si-hcp-a3); _phase:gd-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1508.16 K, x(Si) 0–0 | 3 | 1 |
| [LIQUID](#phase-gd-si-liquid); _phase:gd-si:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1352.27–2500 K, x(Si) 0–1 | 21 | 1 |

## DIAMOND_A4 (Gd–Si)

- Id: `phase:gd-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.54 K, x(Si) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:a4-diamond)

Names (2): _corpus: _corpus:phase:gd-si:a4-diamond  
_tdb: _tdb:GdSi-07Hua.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): DIAMOND_A4, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## BCC_A2 (Gd–Si)

- Id: `phase:gd-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1508.16–1593.16 K, x(Si) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:bcc-a2)

Names (2): _corpus: _corpus:phase:gd-si:bcc-a2  
_tdb: _tdb:GdSi-07Hua.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): BCC_A2, type code %B, sha256 `e9d1c9c91a440a0c…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : GD% SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## FCC_A1 (Gd–Si)

- Id: `phase:gd-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:fcc-a1)

Names (2): _corpus: _corpus:phase:gd-si:fcc-a1  
_tdb: _tdb:GdSi-07Hua.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): FCC_A1, type code %A, sha256 `e9d1c9c91a440a0c…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : GD SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## GD3SI5_C32 (Gd–Si)

- Id: `phase:gd-si:gd3si5-c32`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C32; stoichiometry_contradicts_C32:GdSi-07Hua.tdb
- Candidate (dft_oqmd): Cc (9) — on-hull OQMD Gd3 Si5 at x(SI)=0.6250
- Candidate (name_token): AlB2 · C32 · hP3 · P6/mmm (191) — Strukturbericht/word 'C32' in the TDB name
- Candidate (sgte_mmc2): AlB2 · C32 · hP3 · P6/mmm (191) — Hallstedt 2025 mmc2 row for GD3SI5_C32: Gd3Si5
- Candidate (tdb_comment): AlB2 · hP3 · P6/mmm — GdSi-07Hua.tdb: 'Prototype AlB2 (hP3, P6/mmm)'
- Stoichiometry: Gd 0.3750, Si 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1936.19 K, x(Si) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:gd3si5-c32)

Names (2): _corpus: _corpus:phase:gd-si:gd3si5-c32  
_tdb: _tdb:GdSi-07Hua.tdb:GD3SI5_C32  


### TDB models of GD3SI5_C32 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): GD3SI5_C32, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
66: PHASE GD3SI5_C32 % 2 3 5 !
67: CONST GD3SI5_C32 : GD : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## GD5SI3_D88 (Gd–Si)

- Id: `phase:gd-si:gd5si3-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Gd 0.6250, Si 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–2019.97 K, x(Si) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:gd5si3-d88)

Names (2): _corpus: _corpus:phase:gd-si:gd5si3-d88  
_tdb: _tdb:GdSi-07Hua.tdb:GD5SI3_D88  


### TDB models of GD5SI3_D88 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): GD5SI3_D88, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
51: PHASE GD5SI3_D88 % 2 5 3 !
52: CONST GD5SI3_D88 : GD : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## GD5SI4 (Gd–Si)

- Id: `phase:gd-si:gd5si4`; status `assigned`
- Structure: Ge4Sm5 · oP36 · Pnma (62); type `st:ge4sm5-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Gd 0.5556, Si 0.4444
- Stability: stable in 1 of 1 calculated diagram(s): 300–2045.62 K, x(Si) 0.44444–0.44444
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:gd5si4)

Names (3): _corpus: _corpus:phase:gd-si:gd5si4  
_paper: _paper:10.1016/j.jallcom.2006.09.068:Gd5Si4  
_tdb: _tdb:GdSi-07Hua.tdb:GD5SI4  


### TDB models of GD5SI4 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): GD5SI4, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
56: PHASE GD5SI4 % 2 5 4 !
57: CONST GD5SI4 : GD : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase; reports values for this phase_

## GDSI_B27 (Gd–Si)

- Id: `phase:gd-si:gdsi-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabifpr and oqmd-12494, space group 62
- Stoichiometry: Gd 0.5000, Si 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2107.12 K, x(Si) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:gdsi-b27)

Names (4): _corpus: _corpus:phase:gd-si:gdsi-b27  
_mp: _mp:mp-aaabifpr  
_oqmd: _oqmd:oqmd-12494  
_tdb: _tdb:GdSi-07Hua.tdb:GDSI_B27  


### TDB models of GDSI_B27 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): GDSI_B27, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
61: PHASE GDSI_B27 % 2 1 1 !
62: CONST GDSI_B27 : GD : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## GDSI2 (Gd–Si)

- Id: `phase:gd-si:gdsi2`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_oqmd; no_structure_token
- Candidate (dft_mp): I4_1/amd (141) — on-hull MP GdSi2 at x(SI)=0.6667
- Candidate (tdb_comment): Si2Th · tI12 · I4_1/amd — GdSi-07Hua.tdb: 'Prototype Si2Th (tI12, I4_1/amd) and GdSi1.4 ? (oI12, Imma)'
- Stoichiometry: Gd 0.3333, Si 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1874.01 K, x(Si) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:gdsi2)

Names (2): _corpus: _corpus:phase:gd-si:gdsi2  
_tdb: _tdb:GdSi-07Hua.tdb:GDSI2  


### TDB models of GDSI2 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): GDSI2, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
71: PHASE GDSI2 % 2 1 2 !
72: CONST GDSI2 : GD : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase_

## HCP_A3 (Gd–Si)

- Id: `phase:gd-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1508.16 K, x(Si) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:hcp-a3)

Names (3): _corpus: _corpus:phase:gd-si:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2006.09.068:hcp (Gd)  
_tdb: _tdb:GdSi-07Hua.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): HCP_A3, type code %A, sha256 `e9d1c9c91a440a0c…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : GD% SI : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Gd–Si)

- Id: `phase:gd-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1352.27–2500 K, x(Si) 0–1
- Literature: 21 values (21 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-si:liquid)

Names (3): _corpus: _corpus:phase:gd-si:liquid  
_paper: _paper:10.1016/j.jallcom.2006.09.068:Liquid  
_tdb: _tdb:GdSi-07Hua.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GdSi-07Hua.tdb](https://orchid-project.org/data/databases/sgte-binary/GdSi-07Hua.tdb): LIQUID, type code %, sha256 `e9d1c9c91a440a0c…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : GD SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2006.09.068](https://doi.org/10.1016/j.jallcom.2006.09.068) Mianliang Huang, Deborah L. Schlagel, Frederick A. Schmidt, Thomas A. Lograsso, Experimental investigation and thermodynamic modeling of the Gd–Si system, Journal of Alloys and Compounds 441, 94-100 (2007).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
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
