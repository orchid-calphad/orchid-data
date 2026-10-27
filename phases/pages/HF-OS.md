# Hf–Os phases

> Hf–Os system: 7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-OS.html · Markdown: https://data.orchid-project.org/phases/pages/HF-OS.md

7 phases (tier A 5, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-OS) · [full JSON](https://data.orchid-project.org/phases/systems/HF-OS.json) · [Hf–Os system page](https://data.orchid-project.org/systems/HF-OS.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-OS.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–Os system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-os-bcc-a2); _phase:hf-os:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1500–2450 K, x(Os) 0–0.13 | 4 | 2 |
| [B2_BCC](#phase-hf-os-bcc-b2); _phase:hf-os:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2867.72 K, x(Os) 0–0.5 | 6 | 1 |
| [FCC_A1](#phase-hf-os-fcc-a1); _phase:hf-os:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-hf-os-hcp-a3); _phase:hf-os:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.74 K, x(Os) 0–1 | 4 | 1 |
| [HF54OS17](#phase-hf-os-hf54os17); _phase:hf-os:hf54os17_ | Hf54Os17 · oI142 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1893.22 K, x(Os) 0.23944–0.23944 | 6 | 1 |
| [HFOS2_C14](#phase-hf-os-hfos2-c14); _phase:hf-os:hfos2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2952.94 K, x(Os) 0.6516–0.6723 | 6 | 1 |
| [LIQUID](#phase-hf-os-liquid); _phase:hf-os:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1872.91–4000 K, x(Os) 0–1 | 12 | 1 |

## BCC_A2 (Hf–Os)

- Id: `phase:hf-os:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1500–2450 K, x(Os) 0–0.13
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:bcc-a2)

Names (4): _corpus: _corpus:phase:hf-os:bcc-a2  
_paper: _paper:10.1016/j.jallcom.2005.06.034:bcc(Hf)  
_tdb: _tdb:HfOs-06Guo.tdb:A2_BCC, tdb:HfOs-06Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): A2_BCC, type code %B, sha256 `a62b29616d7b4270…`

~~~~text
35: PHASE A2_BCC %B 2 1 3 !
36: CONST A2_BCC : HF% OS : VA : !
~~~~

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): BCC_A2, type code %B, sha256 `a62b29616d7b4270…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : HF% OS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
_assessment that models this phase; reports values for this phase_

## B2_BCC (Hf–Os)

- Id: `phase:hf-os:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: HfOs-06Guo.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in HfOs-06Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2867.72 K, x(Os) 0–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:bcc-b2)

Names (4): _corpus: _corpus:phase:hf-os:bcc-b2, corpus:phase:hf-os:b2-bcc  
_paper: _paper:10.1016/j.jallcom.2005.06.034:HfOs  
_tdb: _tdb:HfOs-06Guo.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): B2_BCC, type code %BO, sha256 `a62b29616d7b4270…`

~~~~text
40: PHASE B2_BCC %BO 3 0.5 0.5 3 !
41: CONST B2_BCC : HF% OS : HF OS% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Hf–Os)

- Id: `phase:hf-os:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:fcc-a1)

Names (2): _corpus: _corpus:phase:hf-os:fcc-a1  
_tdb: _tdb:HfOs-06Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): FCC_A1, type code %A, sha256 `a62b29616d7b4270…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : HF OS : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
_assessment that models this phase_

## HCP_A3 (Hf–Os)

- Id: `phase:hf-os:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.74 K, x(Os) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:hcp-a3)

Names (4): _corpus: _corpus:phase:hf-os:hcp-a3  
_paper: _paper:10.1016/j.jallcom.2005.06.034:hcp(Hf), paper:10.1016/j.jallcom.2005.06.034:hcp(Os)  
_tdb: _tdb:HfOs-06Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): HCP_A3, type code %A, sha256 `a62b29616d7b4270…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : HF% OS% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
_assessment that models this phase; reports values for this phase_

## HF54OS17 (Hf–Os)

- Id: `phase:hf-os:hf54os17`; status `assigned`
- Structure: Hf54Os17 · oI142 · Immm (71); type `st:hf54os17-oi142`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hf 0.7606, Os 0.2394
- Stability: stable in 1 of 1 calculated diagram(s): 300–1893.22 K, x(Os) 0.23944–0.23944
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:hf54os17)

Names (3): _corpus: _corpus:phase:hf-os:hf54os17  
_paper: _paper:10.1016/j.jallcom.2005.06.034:Hf54Os17  
_tdb: _tdb:HfOs-06Guo.tdb:HF54OS17  


### TDB models of HF54OS17 (1): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): HF54OS17, type code %, sha256 `a62b29616d7b4270…`

~~~~text
50: PHASE HF54OS17 % 2 54 17 !
51: CONST HF54OS17 : HF : OS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
_assessment that models this phase; reports values for this phase_

## HFOS2_C14 (Hf–Os)

- Id: `phase:hf-os:hfos2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfOs-06Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2952.94 K, x(Os) 0.6516–0.6723
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:hfos2-c14)

Names (3): _corpus: _corpus:phase:hf-os:hfos2-c14  
_paper: _paper:10.1016/j.jallcom.2005.06.034:HfOs2  
_tdb: _tdb:HfOs-06Guo.tdb:HFOS2_C14  


### TDB models of HFOS2_C14 (1): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): HFOS2_C14, type code %, sha256 `a62b29616d7b4270…`

~~~~text
55: PHASE HFOS2_C14 % 2 1 2 !
56: CONST HFOS2_C14 : HF% OS : HF OS% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Hf–Os)

- Id: `phase:hf-os:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1872.91–4000 K, x(Os) 0–1
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-os:liquid)

Names (3): _corpus: _corpus:phase:hf-os:liquid  
_paper: _paper:10.1016/j.jallcom.2005.06.034:L  
_tdb: _tdb:HfOs-06Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HfOs-06Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/HfOs-06Guo.tdb): LIQUID, type code %, sha256 `a62b29616d7b4270…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : HF OS : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2005.06.034](https://doi.org/10.1016/j.jallcom.2005.06.034) Cuiping Guo, Zhenmin Du, Thermodynamic assessment of the Hf–Os system, Journal of Alloys and Compounds 407, 188-192 (2006).  
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
