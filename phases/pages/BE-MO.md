# Be–Mo phases

> Be–Mo system: 8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BE-MO.html · Markdown: https://data.orchid-project.org/phases/pages/BE-MO.md

8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BE-MO) · [full JSON](https://data.orchid-project.org/phases/systems/BE-MO.json) · [Be–Mo system page](https://data.orchid-project.org/systems/BE-MO.html) · [Markdown](https://data.orchid-project.org/phases/pages/BE-MO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Be–Mo system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-be-mo-bcc-a2); _phase:be-mo:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.73 K, x(Mo) 0–1 | 0 | 1 |
| [BE12MO_D2B](#phase-be-mo-be12mo-d2b); _phase:be-mo:be12mo-d2b_ | Mn12Th · D2_b · tI26 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1976.92 K, x(Mo) 0.07692–0.07692 | 2 | 1 |
| [BE22MO](#phase-be-mo-be22mo); _phase:be-mo:be22mo_ | Zn22Zr · cF184 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1554.84 K, x(Mo) 0.04348–0.04348 | 2 | 1 |
| [BE2MO_C14](#phase-be-mo-be2mo-c14); _phase:be-mo:be2mo-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2342.91 K, x(Mo) 0.33333–0.33333 | 2 | 1 |
| [BEMO3_A15](#phase-be-mo-bemo3-a15); _phase:be-mo:bemo3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1175.9 K, x(Mo) 0.75–0.75 | 2 | 1 |
| [FCC_A1](#phase-be-mo-fcc-a1); _phase:be-mo:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-be-mo-hcp-a3); _phase:be-mo:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1527.01 K, x(Mo) 0–0 | 0 | 1 |
| [LIQUID](#phase-be-mo-liquid); _phase:be-mo:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1558.26–4000 K, x(Mo) 0–1 | 0 | 1 |

## BCC_A2 (Be–Mo)

- Id: `phase:be-mo:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.73 K, x(Mo) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:bcc-a2)

Names (2): _corpus: _corpus:phase:be-mo:bcc-a2  
_tdb: _tdb:BeMo-07Nak.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): BCC_A2, type code %B, sha256 `75fb8f02c9ac7f20…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BE MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase_

## BE12MO_D2B (Be–Mo)

- Id: `phase:be-mo:be12mo-d2b`; status `assigned`
- Structure: Mn12Th · D2_b · tI26 · I4/mmm (139); type `st:d2-b-mn12th-ti26`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacet and oqmd-10889, space group 139
- Stoichiometry: Be 0.9231, Mo 0.0769
- Stability: stable in 1 of 1 calculated diagram(s): 300–1976.92 K, x(Mo) 0.07692–0.07692
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:be12mo-d2b)

Names (5): _corpus: _corpus:phase:be-mo:be12mo-d2b  
_mp: _mp:mp-aaaaacet  
_oqmd: _oqmd:oqmd-10889  
_paper: _paper:10.2320/jinstmet.71.187:Be12Mo  
_tdb: _tdb:BeMo-07Nak.tdb:BE12MO_D2B  


### TDB models of BE12MO_D2B (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): BE12MO_D2B, type code %, sha256 `75fb8f02c9ac7f20…`

~~~~text
46: PHASE BE12MO_D2B % 2 12 1 !
47: CONST BE12MO_D2B : BE : MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase; reports values for this phase_

## BE22MO (Be–Mo)

- Id: `phase:be-mo:be22mo`; status `assigned`
- Structure: Zn22Zr · cF184 · Fd-3m (227); type `st:zn22zr-cf184`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Be 0.9565, Mo 0.0435
- Stability: stable in 1 of 1 calculated diagram(s): 300–1554.84 K, x(Mo) 0.04348–0.04348
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:be22mo)

Names (3): _corpus: _corpus:phase:be-mo:be22mo  
_paper: _paper:10.2320/jinstmet.71.187:Be22Mo  
_tdb: _tdb:BeMo-07Nak.tdb:BE22MO  


### TDB models of BE22MO (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): BE22MO, type code %, sha256 `75fb8f02c9ac7f20…`

~~~~text
41: PHASE BE22MO % 2 22 1 !
42: CONST BE22MO : BE : MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase; reports values for this phase_

## BE2MO_C14 (Be–Mo)

- Id: `phase:be-mo:be2mo-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacmn and oqmd-10888, space group 194
- Stoichiometry: Be 0.6667, Mo 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2342.91 K, x(Mo) 0.33333–0.33333
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:be2mo-c14)

Names (5): _corpus: _corpus:phase:be-mo:be2mo-c14  
_mp: _mp:mp-aaaaacmn  
_oqmd: _oqmd:oqmd-10888  
_paper: _paper:10.2320/jinstmet.71.187:Be2Mo  
_tdb: _tdb:BeMo-07Nak.tdb:BE2MO_C14  


### TDB models of BE2MO_C14 (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): BE2MO_C14, type code %, sha256 `75fb8f02c9ac7f20…`

~~~~text
51: PHASE BE2MO_C14 % 2 2 1 !
52: CONST BE2MO_C14 : BE : MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase; reports values for this phase_

## BEMO3_A15 (Be–Mo)

- Id: `phase:be-mo:bemo3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Stoichiometry: Be 0.2500, Mo 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1175.9 K, x(Mo) 0.75–0.75
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:bemo3-a15)

Names (3): _corpus: _corpus:phase:be-mo:bemo3-a15  
_paper: _paper:10.2320/jinstmet.71.187:BeMo3  
_tdb: _tdb:BeMo-07Nak.tdb:BEMO3_A15  


### TDB models of BEMO3_A15 (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): BEMO3_A15, type code %, sha256 `75fb8f02c9ac7f20…`

~~~~text
56: PHASE BEMO3_A15 % 2 1 3 !
57: CONST BEMO3_A15 : BE : MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Be–Mo)

- Id: `phase:be-mo:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:fcc-a1)

Names (2): _corpus: _corpus:phase:be-mo:fcc-a1  
_tdb: _tdb:BeMo-07Nak.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): FCC_A1, type code %A, sha256 `75fb8f02c9ac7f20…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BE MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase_

## HCP_A3 (Be–Mo)

- Id: `phase:be-mo:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1527.01 K, x(Mo) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:hcp-a3)

Names (2): _corpus: _corpus:phase:be-mo:hcp-a3  
_tdb: _tdb:BeMo-07Nak.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): HCP_A3, type code %A, sha256 `75fb8f02c9ac7f20…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BE% MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
_assessment that models this phase_

## LIQUID (Be–Mo)

- Id: `phase:be-mo:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1558.26–4000 K, x(Mo) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:be-mo:liquid)

Names (2): _corpus: _corpus:phase:be-mo:liquid  
_tdb: _tdb:BeMo-07Nak.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BeMo-07Nak.tdb](https://orchid-project.org/data/databases/sgte-binary/BeMo-07Nak.tdb): LIQUID, type code %, sha256 `75fb8f02c9ac7f20…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BE MO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2320/jinstmet.71.187](https://doi.org/10.2320/jinstmet.71.187) Kazuyoshi Nakashima, Tatsuya Tokunaga, Hiroshi Ohtani, Mitsuhiro Hasebe, Thermodynamic Analysis of the Be-Mo Binary Phase Diagram, J. Japan Inst. Metals 71, 187-189 (2007).  
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
