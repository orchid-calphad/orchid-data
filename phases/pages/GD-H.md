# Gd–H phases

> Gd–H system: 5 phases (tier A 1, liquid 1, gas 1, needs_review 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-H.html · Markdown: https://data.orchid-project.org/phases/pages/GD-H.md

5 phases (tier A 1, liquid 1, gas 1, needs_review 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-H) · [full JSON](https://data.orchid-project.org/phases/systems/GD-H.json) · [Gd–H system page](https://data.orchid-project.org/systems/GD-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–H system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-gd-h-bcc-a2); _phase:gd-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1221.91–1586.6 K, x(H) 0–0.00033 | 0 | 1 |
| [FCC_A1](#phase-gd-h-fcc-a1); _phase:gd-h:fcc-a1_ | CaF2 · C1 · cF12 · Fm-3m (225) | assigned | stable in 1 of 1 calculated diagram(s): 300–1468.03 K, x(H) 0.52934–0.70081 | 0 | 1 |
| [GAS](#phase-gd-h-gas); _phase:gd-h:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 1–1 | 2 | 1 |
| [HCP_A3](#phase-gd-h-hcp-a3); _phase:gd-h:hcp-a3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1916.51 K, x(H) 0–0.75 | 1 | 1 |
| [LIQUID](#phase-gd-h-liquid); _phase:gd-h:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1586.6–2500 K, x(H) 0–0.00509 | 0 | 1 |

## BCC_A2 (Gd–H)

- Id: `phase:gd-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1221.91–1586.6 K, x(H) 0–0.00033
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-h:bcc-a2)

Names (2): _corpus: _corpus:phase:gd-h:bcc-a2  
_tdb: _tdb:GdH-16Fu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GdH-16Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/GdH-16Fu.tdb): BCC_A2, type code %B, sha256 `aaac49e5806f315d…`

~~~~text
41: PHASE BCC_A2 %B 2 1 1 !
42: CONST BCC_A2 : GD : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201) Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Jie Zheng et al., Study on the thermodynamics of the gadolinium-hydrogen binary system (H/Gd = 0.0–2.0) and implications to metallic gadolinium purification, Journal of Alloys and Compounds 673, 131-137 (2016).  
_assessment that models this phase_

## FCC_A1 (Gd–H)

- Id: `phase:gd-h:fcc-a1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1468.03 K, x(H) 0.52934–0.70081
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-h:fcc-a1)

Names (2): _corpus: _corpus:phase:gd-h:fcc-a1  
_tdb: _tdb:GdH-16Fu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GdH-16Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/GdH-16Fu.tdb): FCC_A1, type code %A, sha256 `aaac49e5806f315d…`

~~~~text
36: PHASE FCC_A1 %A 3 1 1 2 !
37: CONST FCC_A1 : GD : H VA : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201) Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Jie Zheng et al., Study on the thermodynamics of the gadolinium-hydrogen binary system (H/Gd = 0.0–2.0) and implications to metallic gadolinium purification, Journal of Alloys and Compounds 673, 131-137 (2016).  
_assessment that models this phase_

## GAS (Gd–H)

- Id: `phase:gd-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-h:gas)

Names (3): _corpus: _corpus:phase:gd-h:gas  
_paper: _paper:10.1016/j.jallcom.2016.02.201:Gas(H2)  
_tdb: _tdb:GdH-16Fu.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[GdH-16Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/GdH-16Fu.tdb): GAS, type code %, sha256 `aaac49e5806f315d…`

~~~~text
50: PHASE GAS:G % 1 1 !
51: CONST GAS:G : H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201) Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Jie Zheng et al., Study on the thermodynamics of the gadolinium-hydrogen binary system (H/Gd = 0.0–2.0) and implications to metallic gadolinium purification, Journal of Alloys and Compounds 673, 131-137 (2016).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Gd–H)

- Id: `phase:gd-h:hcp-a3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:HCP_A3
- Candidate (dft_mp): Fm-3m (225) — on-hull MP GdH2 at x(H)=0.6667
- Candidate (dft_mp): P-3c1 (165) — on-hull MP GdH3 at x(H)=0.7500
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Gd1 H2 at x(H)=0.6667
- Candidate (dft_oqmd): P-3c1 (165) — on-hull OQMD Gd1 H3 at x(H)=0.7500
- Candidate (literature_printed): HoH3 · hP24 — printed with a label mapped to this phase
- Candidate (name_token): Mg · A3 · hP2 · P6_3/mmc (194) — Strukturbericht/word 'A3' in the TDB name
- Candidate (sgte_mmc2): HoH3 · hP24 · P-3c1 (165) — Hallstedt 2025 mmc2 row for HCP_A3: DyH3, ErH3, GdH3, YH3
- Stability: stable in 1 of 1 calculated diagram(s): 300–1916.51 K, x(H) 0–0.75
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-h:hcp-a3)

Names (3): _corpus: _corpus:phase:gd-h:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2016.02.201:Hcp(Gd)  
_tdb: _tdb:GdH-16Fu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GdH-16Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/GdH-16Fu.tdb): HCP_A3, type code %A, sha256 `aaac49e5806f315d…`

~~~~text
47: PHASE HCP_A3 %A 3 1 1 2 !
48: CONST HCP_A3 : GD : H VA : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201) Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Jie Zheng et al., Study on the thermodynamics of the gadolinium-hydrogen binary system (H/Gd = 0.0–2.0) and implications to metallic gadolinium purification, Journal of Alloys and Compounds 673, 131-137 (2016).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Gd–H)

- Id: `phase:gd-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1586.6–2500 K, x(H) 0–0.00509
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-h:liquid)

Names (2): _corpus: _corpus:phase:gd-h:liquid  
_tdb: _tdb:GdH-16Fu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GdH-16Fu.tdb](https://orchid-project.org/data/databases/sgte-binary/GdH-16Fu.tdb): LIQUID, type code %, sha256 `aaac49e5806f315d…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : GD H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2016.02.201](https://doi.org/10.1016/j.jallcom.2016.02.201) Kai Fu, Guoling Li, Jigang Li, Yang Liu, Wenhuai Tian, Jie Zheng et al., Study on the thermodynamics of the gadolinium-hydrogen binary system (H/Gd = 0.0–2.0) and implications to metallic gadolinium purification, Journal of Alloys and Compounds 673, 131-137 (2016).  
_assessment that models this phase_

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
