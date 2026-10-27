# Hf–Ir phases

> Hf–Ir system: 10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-IR.html · Markdown: https://data.orchid-project.org/phases/pages/HF-IR.md

10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-IR) · [full JSON](https://data.orchid-project.org/phases/systems/HF-IR.json) · [Hf–Ir system page](https://data.orchid-project.org/systems/HF-IR.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-IR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Ir system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-ir-bcc-a2); _phase:hf-ir:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1674.39–2506 K, x(Ir) 0–0.0617 | 0 | 1 |
| [FCC_A1](#phase-hf-ir-fcc-a1); _phase:hf-ir:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2724.52 K, x(Ir) 0.92834–1 | 0 | 1 |
| [HCP_A3](#phase-hf-ir-hcp-a3); _phase:hf-ir:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2016.02 K, x(Ir) 0–0.01304 | 0 | 1 |
| [HF2IR](#phase-hf-ir-hf2ir); _phase:hf-ir:hf2ir_ | NiTi2 · cF96 · Fd-3m (227) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1997.83 K, x(Ir) 0.28359–0.33333 | 0 | 1 |
| [HF5IR3](#phase-hf-ir-hf5ir3); _phase:hf-ir:hf5ir3_ | Ir3Zr5 · hP48 · P6_122 (178) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2193.99 K, x(Ir) 0.375–0.375 | 0 | 1 |
| [HFIR_ALPHA](#phase-hf-ir-hfir-alpha); _phase:hf-ir:hfir-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1237.16 K, x(Ir) 0.47983–0.48001 | 0 | 1 |
| [HFIR_B2](#phase-hf-ir-hfir-b2); _phase:hf-ir:hfir-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1219.38–2707.64 K, x(Ir) 0.48762–0.5063 | 0 | 1 |
| [HFIR_L10](#phase-hf-ir-hfir-l10); _phase:hf-ir:hfir-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 917.21–1219.51 K, x(Ir) 0.49998–0.50013 | 0 | 1 |
| [HFIR3_L12](#phase-hf-ir-hfir3-l12); _phase:hf-ir:hfir3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2738.88 K, x(Ir) 0.74997–0.81062 | 0 | 1 |
| [LIQUID](#phase-hf-ir-liquid); _phase:hf-ir:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1735.4–4000 K, x(Ir) 0–1 | 0 | 1 |

## BCC_A2 (Hf–Ir)

- Id: `phase:hf-ir:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1674.39–2506 K, x(Ir) 0–0.0617
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:bcc-a2)

Names (2): _corpus: _corpus:phase:hf-ir:bcc-a2  
_tdb: _tdb:HfIr-18Idb.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): BCC_A2, type code %B, sha256 `37ce1bf38cdad3fb…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : HF% IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## FCC_A1 (Hf–Ir)

- Id: `phase:hf-ir:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2724.52 K, x(Ir) 0.92834–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:fcc-a1)

Names (2): _corpus: _corpus:phase:hf-ir:fcc-a1  
_tdb: _tdb:HfIr-18Idb.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): FCC_A1, type code %A, sha256 `37ce1bf38cdad3fb…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : HF IR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HCP_A3 (Hf–Ir)

- Id: `phase:hf-ir:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2016.02 K, x(Ir) 0–0.01304
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hcp-a3)

Names (2): _corpus: _corpus:phase:hf-ir:hcp-a3  
_tdb: _tdb:HfIr-18Idb.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HCP_A3, type code %A, sha256 `37ce1bf38cdad3fb…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : HF% IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HF2IR (Hf–Ir)

- Id: `phase:hf-ir:hf2ir`; status `assigned`
- Structure: NiTi2 · cF96 · Fd-3m (227); type `st:niti2-cf96`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1997.83 K, x(Ir) 0.28359–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hf2ir)

Names (2): _corpus: _corpus:phase:hf-ir:hf2ir  
_tdb: _tdb:HfIr-18Idb.tdb:HF2IR  


### TDB models of HF2IR (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HF2IR, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
46: PHASE HF2IR % 2 2 1 !
47: CONST HF2IR : HF : HF IR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HF5IR3 (Hf–Ir)

- Id: `phase:hf-ir:hf5ir3`; status `assigned`
- Structure: Ir3Zr5 · hP48 · P6_122 (178); type `st:ir3zr5-hp48`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Hf 0.6250, Ir 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–2193.99 K, x(Ir) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hf5ir3)

Names (4): _corpus: _corpus:phase:hf-ir:hf5ir3  
_mp: _mp:mp-aaacqzqp  
_oqmd: _oqmd:oqmd-2052706  
_tdb: _tdb:HfIr-18Idb.tdb:HF5IR3  


### TDB models of HF5IR3 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HF5IR3, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
51: PHASE HF5IR3 % 2 5 3 !
52: CONST HF5IR3 : HF : IR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HFIR_ALPHA (Hf–Ir)

- Id: `phase:hf-ir:hfir-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; off_stoichiometric_model
- Candidate (sgte_mmc2): (HfIr) · Pmma (51) — Hallstedt 2025 mmc2 row for HFIR_ALPHA: HfIr-alpha
- Stability: stable in 1 of 1 calculated diagram(s): 300–1237.16 K, x(Ir) 0.47983–0.48001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hfir-alpha)

Names (2): _corpus: _corpus:phase:hf-ir:hfir-alpha  
_tdb: _tdb:HfIr-18Idb.tdb:HFIR_ALPHA  


### TDB models of HFIR_ALPHA (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HFIR_ALPHA, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
56: PHASE HFIR_ALPHA % 2 0.52 0.48 !
57: CONST HFIR_ALPHA : HF% IR : HF IR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HFIR_B2 (Hf–Ir)

- Id: `phase:hf-ir:hfir-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfIr-18Idb.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1219.38–2707.64 K, x(Ir) 0.48762–0.5063
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hfir-b2)

Names (2): _corpus: _corpus:phase:hf-ir:hfir-b2  
_tdb: _tdb:HfIr-18Idb.tdb:HFIR_B2  


### TDB models of HFIR_B2 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HFIR_B2, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
66: PHASE HFIR_B2 % 2 1 1 !
67: CONST HFIR_B2 : HF% IR : HF IR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HFIR_L10 (Hf–Ir)

- Id: `phase:hf-ir:hfir-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfIr-18Idb.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 917.21–1219.51 K, x(Ir) 0.49998–0.50013
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hfir-l10)

Names (2): _corpus: _corpus:phase:hf-ir:hfir-l10  
_tdb: _tdb:HfIr-18Idb.tdb:HFIR_L10  


### TDB models of HFIR_L10 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HFIR_L10, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
61: PHASE HFIR_L10 % 2 1 1 !
62: CONST HFIR_L10 : HF% IR : HF IR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## HFIR3_L12 (Hf–Ir)

- Id: `phase:hf-ir:hfir3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfIr-18Idb.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2738.88 K, x(Ir) 0.74997–0.81062
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:hfir3-l12)

Names (2): _corpus: _corpus:phase:hf-ir:hfir3-l12  
_tdb: _tdb:HfIr-18Idb.tdb:HFIR3_L12  


### TDB models of HFIR3_L12 (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): HFIR3_L12, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
71: PHASE HFIR3_L12 % 2 1 3 !
72: CONST HFIR3_L12 : HF% IR : HF IR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
_assessment that models this phase_

## LIQUID (Hf–Ir)

- Id: `phase:hf-ir:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1735.4–4000 K, x(Ir) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-ir:liquid)

Names (2): _corpus: _corpus:phase:hf-ir:liquid  
_tdb: _tdb:HfIr-18Idb.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HfIr-18Idb.tdb](https://orchid-project.org/data/databases/sgte-binary/HfIr-18Idb.tdb): LIQUID, type code %, sha256 `37ce1bf38cdad3fb…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : HF IR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1051/metal/2018001](https://doi.org/10.1051/metal/2018001) M. Idbenali, C. Servant, M. Feddaoui, Metall. Res. Technol., 115, 503(2018).  
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
