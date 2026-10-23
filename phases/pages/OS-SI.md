# Os–Si phases

> Os–Si system: 8 phases (tier A 4, tier B 1, tier C 2, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/OS-SI.html · Markdown: https://data.orchid-project.org/phases/pages/OS-SI.md

8 phases (tier A 4, tier B 1, tier C 2, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=OS-SI) · [full JSON](https://data.orchid-project.org/phases/systems/OS-SI.json) · [Os–Si system page](https://data.orchid-project.org/systems/OS-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/OS-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Os–Si system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-os-si-a4-diamond); _phase:os-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.76 K, x(Si) 1–1 | 4 | 1 |
| [MSI_B20](#phase-os-si-b20-msi); _phase:os-si:b20-msi_ | FeSi · B20 · cP8 · P2_13 (198) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2013.01 K, x(Si) 0.5–0.5 | 4 | 1 |
| [BCC_A2](#phase-os-si-bcc-a2); _phase:os-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-os-si-fcc-a1); _phase:os-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-os-si-hcp-a3); _phase:os-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3331.55 K, x(Si) 0–0 | 2 | 1 |
| [LIQUID](#phase-os-si-liquid); _phase:os-si:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1616.01–4000 K, x(Si) 0–1 | 13 | 1 |
| [OS2SI3](#phase-os-si-os2si3); _phase:os-si:os2si3_ | Ge3Ru2 · oP40 · Pbcn (60) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–2103.93 K, x(Si) 0.6–0.6 | 6 | 1 |
| [OSSI2](#phase-os-si-ossi2); _phase:os-si:ossi2_ | FeSi2-h · oC48 · Cmce (64) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1922.11 K, x(Si) 0.66667–0.66667 | 6 | 1 |

## DIAMOND_A4 (Os–Si)

- Id: `phase:os-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.76 K, x(Si) 1–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:a4-diamond)

Names (4): _corpus: _corpus:phase:os-si:a4-diamond, corpus:phase:os-si:diamond-a4  
_paper: _paper:10.1016/s0925-8388(01)00931-8:Diamond  
_tdb: _tdb:OsSi-01Liu-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): DIAMOND_A4, type code %, sha256 `661081800c525b84…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-0248(83)90424-4](https://doi.org/10.1016/0022-0248%2883%2990424-4) K. Mason, G. Müller-Vogt, Osmium disilicide: Preparation, crystal growth, and physical properties of a new semiconducting compound, Journal of Crystal Growth 63, 34-38 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(62)90055-3](https://doi.org/10.1016/0022-5088%2862%2990055-3) Lies N Finnie, Structures and compositions of the silicides of ruthenium, osmium, rhodium and iridium, Journal of the Less Common Metals 4, 24-34 (1962).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(88)90148-8](https://doi.org/10.1016/0022-5088%2888%2990148-8) L. Schellenberg, H.F. Braun, J. Muller, The osmium-silicon phase diagram, Journal of the Less Common Metals 144, 341-350 (1988).  
_cited as the source of values for this phase_

## MSI_B20 (Os–Si)

- Id: `phase:os-si:b20-msi`; status `assigned`
- Structure: FeSi · B20 · cP8 · P2_13 (198); type `st:b20-fesi-cp8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:MSI); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Os 0.5000, Si 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2013.01 K, x(Si) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:b20-msi)

Names (4): _corpus: _corpus:phase:os-si:b20-msi, corpus:phase:os-si:msi-b20  
_paper: _paper:10.1016/s0925-8388(01)00931-8:OsSi  
_tdb: _tdb:OsSi-01Liu-LB.tdb:MSI_B20  


### TDB models of MSI_B20 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): MSI_B20, type code %, sha256 `661081800c525b84…`

~~~~text
50: PHASE MSI_B20 % 2 1 1 !
51: CONST MSI_B20 : OS : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90148-8](https://doi.org/10.1016/0022-5088%2888%2990148-8) L. Schellenberg, H.F. Braun, J. Muller, The osmium-silicon phase diagram, Journal of the Less Common Metals 144, 341-350 (1988).  
_cited as the source of values for this phase_

## BCC_A2 (Os–Si)

- Id: `phase:os-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:bcc-a2)

Names (2): _corpus: _corpus:phase:os-si:bcc-a2  
_tdb: _tdb:OsSi-01Liu-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): BCC_A2, type code %B, sha256 `661081800c525b84…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : OS SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase_

## FCC_A1 (Os–Si)

- Id: `phase:os-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:fcc-a1)

Names (2): _corpus: _corpus:phase:os-si:fcc-a1  
_tdb: _tdb:OsSi-01Liu-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): FCC_A1, type code %A, sha256 `661081800c525b84…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : OS SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase_

## HCP_A3 (Os–Si)

- Id: `phase:os-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3331.55 K, x(Si) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:hcp-a3)

Names (3): _corpus: _corpus:phase:os-si:hcp-a3  
_paper: _paper:10.1016/s0925-8388(01)00931-8:(Os)  
_tdb: _tdb:OsSi-01Liu-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): HCP_A3, type code %, sha256 `661081800c525b84…`

~~~~text
40: PHASE HCP_A3 % 2 1 0.5 !
41: CONST HCP_A3 : OS% SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90148-8](https://doi.org/10.1016/0022-5088%2888%2990148-8) L. Schellenberg, H.F. Braun, J. Muller, The osmium-silicon phase diagram, Journal of the Less Common Metals 144, 341-350 (1988).  
_cited as the source of values for this phase_

## LIQUID (Os–Si)

- Id: `phase:os-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1616.01–4000 K, x(Si) 0–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:liquid)

Names (3): _corpus: _corpus:phase:os-si:liquid  
_paper: _paper:10.1016/s0925-8388(01)00931-8:liquid  
_tdb: _tdb:OsSi-01Liu-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): LIQUID, type code %, sha256 `661081800c525b84…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : OS SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90148-8](https://doi.org/10.1016/0022-5088%2888%2990148-8) L. Schellenberg, H.F. Braun, J. Muller, The osmium-silicon phase diagram, Journal of the Less Common Metals 144, 341-350 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-0248(83)90424-4](https://doi.org/10.1016/0022-0248%2883%2990424-4) K. Mason, G. Müller-Vogt, Osmium disilicide: Preparation, crystal growth, and physical properties of a new semiconducting compound, Journal of Crystal Growth 63, 34-38 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(62)90055-3](https://doi.org/10.1016/0022-5088%2862%2990055-3) Lies N Finnie, Structures and compositions of the silicides of ruthenium, osmium, rhodium and iridium, Journal of the Less Common Metals 4, 24-34 (1962).  
_cited as the source of values for this phase_

## OS2SI3 (Os–Si)

- Id: `phase:os-si:os2si3`; status `assigned`
- Structure: Ge3Ru2 · oP40 · Pbcn (60); type `st:ge3ru2-op40`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Os 0.4000, Si 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2103.93 K, x(Si) 0.6–0.6
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:os2si3)

Names (5): _corpus: _corpus:phase:os-si:os2si3  
_mp: _mp:mp-aaaaayou  
_oqmd: _oqmd:oqmd-83466  
_paper: _paper:10.1016/s0925-8388(01)00931-8:Os2Si3  
_tdb: _tdb:OsSi-01Liu-LB.tdb:OS2SI3  


### TDB models of OS2SI3 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): OS2SI3, type code %, sha256 `661081800c525b84…`

~~~~text
55: PHASE OS2SI3 % 2 2 3 !
56: CONST OS2SI3 : OS : SI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90148-8](https://doi.org/10.1016/0022-5088%2888%2990148-8) L. Schellenberg, H.F. Braun, J. Muller, The osmium-silicon phase diagram, Journal of the Less Common Metals 144, 341-350 (1988).  
_cited as the source of values for this phase_

## OSSI2 (Os–Si)

- Id: `phase:os-si:ossi2`; status `assigned`
- Structure: FeSi2-h · oC48 · Cmce (64); type `st:fesi2-h-oc48`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_64_matches_2_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Os 0.3333, Si 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1922.11 K, x(Si) 0.66667–0.66667
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-si:ossi2)

Names (3): _corpus: _corpus:phase:os-si:ossi2  
_paper: _paper:10.1016/s0925-8388(01)00931-8:OsSi2  
_tdb: _tdb:OsSi-01Liu-LB.tdb:OSSI2  


### TDB models of OSSI2 (1): PHASE and CONSTITUENT statements as written

[OsSi-01Liu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/OsSi-01Liu-LB.tdb): OSSI2, type code %, sha256 `661081800c525b84…`

~~~~text
60: PHASE OSSI2 % 2 1 2 !
61: CONST OSSI2 : OS : SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/S0925-8388(01)00931-8](https://doi.org/10.1016/S0925-8388%2801%2900931-8) Y.Q. Liu, G. Shao, K.P. Homewood, J. Alloys Compd., 320, 72-79(2001).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(88)90148-8](https://doi.org/10.1016/0022-5088%2888%2990148-8) L. Schellenberg, H.F. Braun, J. Muller, The osmium-silicon phase diagram, Journal of the Less Common Metals 144, 341-350 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-0248(83)90424-4](https://doi.org/10.1016/0022-0248%2883%2990424-4) K. Mason, G. Müller-Vogt, Osmium disilicide: Preparation, crystal growth, and physical properties of a new semiconducting compound, Journal of Crystal Growth 63, 34-38 (1983).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(62)90055-3](https://doi.org/10.1016/0022-5088%2862%2990055-3) Lies N Finnie, Structures and compositions of the silicides of ruthenium, osmium, rhodium and iridium, Journal of the Less Common Metals 4, 24-34 (1962).  
_cited as the source of values for this phase_

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
