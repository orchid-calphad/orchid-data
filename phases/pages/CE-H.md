# Ce–H phases

> Ce–H system: 6 phases (tier A 3, tier C 1, liquid 1, gas 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CE-H.html · Markdown: https://data.orchid-project.org/phases/pages/CE-H.md

6 phases (tier A 3, tier C 1, liquid 1, gas 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CE-H) · [full JSON](https://data.orchid-project.org/phases/systems/CE-H.json) · [Ce–H system page](https://data.orchid-project.org/systems/CE-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/CE-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ce–H system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ce-h-bcc-a2); _phase:ce-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1000–1308.77 K, x(H) 0–0.4418 | 0 | 2 |
| [CEH3](#phase-ce-h-ceh3); _phase:ce-h:ceh3_ | CeH3 · cF44 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1366.02 K, x(H) 0.60136–0.74999 | 0 | 2 |
| [FCC_A1](#phase-ce-h-fcc-a1); _phase:ce-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1072.54 K, x(H) 0–0.22357 | 0 | 2 |
| [GAS](#phase-ce-h-gas); _phase:ce-h:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 1–1 | 0 | 2 |
| [HCP_A3](#phase-ce-h-hcp-a3); _phase:ce-h:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ce-h-liquid); _phase:ce-h:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1047–2500 K, x(H) 0–0.37753 | 0 | 2 |

## BCC_A2 (Ce–H)

- Id: `phase:ce-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1000–1308.77 K, x(H) 0–0.4418
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-h:bcc-a2)

Names (3): _corpus: _corpus:phase:ce-h:bcc-a2  
_tdb: _tdb:CeH-24Han-mod1.tdb:BCC_A2, tdb:CeH-24Han-mod2.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CeH-24Han-mod1.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod1.tdb): BCC_A2, type code %B, sha256 `443d2f1cbbcc0a31…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : CE : H VA% : !
~~~~

[CeH-24Han-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod2.tdb): BCC_A2, type code %B, sha256 `845d0a630766ed0a…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : CE : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102701](https://doi.org/10.1016/j.calphad.2024.102701) Peter Hannappel, Ebert Alvares, Felix Heubner, Claudio Pistidda, Paul Jerabek, Thomas Weißgärber, Thermodynamic assessment of the Ce H and CeNi5 H system, Calphad 85, 102701 (2024).  
_assessment that models this phase_

## CEH3 (Ce–H)

- Id: `phase:ce-h:ceh3`; status `assigned`
- Structure: CeH3 · cF44 · Fm-3m (225); type `st:ceh3-cf44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–1366.02 K, x(H) 0.60136–0.74999
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-h:ceh3)

Names (3): _corpus: _corpus:phase:ce-h:ceh3  
_tdb: _tdb:CeH-24Han-mod1.tdb:CEH3, tdb:CeH-24Han-mod2.tdb:CEH3  


### TDB models of CEH3 (2): PHASE and CONSTITUENT statements as written

[CeH-24Han-mod1.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod1.tdb): CEH3, type code %, sha256 `443d2f1cbbcc0a31…`

~~~~text
52: PHASE CEH3 % 3 1 2 1 !
53: CONST CEH3 : CE : H% VA : H% VA : !
~~~~

[CeH-24Han-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod2.tdb): CEH3, type code %, sha256 `845d0a630766ed0a…`

~~~~text
50: PHASE CEH3 % 3 1 2 1 !
51: CONST CEH3 : CE : H% VA : H% VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102701](https://doi.org/10.1016/j.calphad.2024.102701) Peter Hannappel, Ebert Alvares, Felix Heubner, Claudio Pistidda, Paul Jerabek, Thomas Weißgärber, Thermodynamic assessment of the Ce H and CeNi5 H system, Calphad 85, 102701 (2024).  
_assessment that models this phase_

## FCC_A1 (Ce–H)

- Id: `phase:ce-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1072.54 K, x(H) 0–0.22357
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-h:fcc-a1)

Names (3): _corpus: _corpus:phase:ce-h:fcc-a1  
_tdb: _tdb:CeH-24Han-mod1.tdb:FCC_A1, tdb:CeH-24Han-mod2.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CeH-24Han-mod1.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod1.tdb): FCC_A1, type code %A, sha256 `443d2f1cbbcc0a31…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : CE : H VA% : !
~~~~

[CeH-24Han-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod2.tdb): FCC_A1, type code %A, sha256 `845d0a630766ed0a…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : CE : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102701](https://doi.org/10.1016/j.calphad.2024.102701) Peter Hannappel, Ebert Alvares, Felix Heubner, Claudio Pistidda, Paul Jerabek, Thomas Weißgärber, Thermodynamic assessment of the Ce H and CeNi5 H system, Calphad 85, 102701 (2024).  
_assessment that models this phase_

## GAS (Ce–H)

- Id: `phase:ce-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-h:gas)

Names (3): _corpus: _corpus:phase:ce-h:gas  
_tdb: _tdb:CeH-24Han-mod1.tdb:GAS, tdb:CeH-24Han-mod2.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[CeH-24Han-mod1.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod1.tdb): GAS, type code %, sha256 `443d2f1cbbcc0a31…`

~~~~text
55: PHASE GAS:G % 1 1 !
56: CONST GAS:G : H H2 : !
~~~~

[CeH-24Han-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod2.tdb): GAS, type code %, sha256 `845d0a630766ed0a…`

~~~~text
53: PHASE GAS:G % 1 1 !
54: CONST GAS:G : H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102701](https://doi.org/10.1016/j.calphad.2024.102701) Peter Hannappel, Ebert Alvares, Felix Heubner, Claudio Pistidda, Paul Jerabek, Thomas Weißgärber, Thermodynamic assessment of the Ce H and CeNi5 H system, Calphad 85, 102701 (2024).  
_assessment that models this phase_

## HCP_A3 (Ce–H)

- Id: `phase:ce-h:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Ce 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-h:hcp-a3)

Names (3): _corpus: _corpus:phase:ce-h:hcp-a3  
_tdb: _tdb:CeH-24Han-mod1.tdb:HCP_A3, tdb:CeH-24Han-mod2.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CeH-24Han-mod1.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod1.tdb): HCP_A3, type code %A, sha256 `443d2f1cbbcc0a31…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : CE : VA : !
~~~~

[CeH-24Han-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod2.tdb): HCP_A3, type code %A, sha256 `845d0a630766ed0a…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : CE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102701](https://doi.org/10.1016/j.calphad.2024.102701) Peter Hannappel, Ebert Alvares, Felix Heubner, Claudio Pistidda, Paul Jerabek, Thomas Weißgärber, Thermodynamic assessment of the Ce H and CeNi5 H system, Calphad 85, 102701 (2024).  
_assessment that models this phase_

## LIQUID (Ce–H)

- Id: `phase:ce-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1047–2500 K, x(H) 0–0.37753
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ce-h:liquid)

Names (3): _corpus: _corpus:phase:ce-h:liquid  
_tdb: _tdb:CeH-24Han-mod1.tdb:LIQUID, tdb:CeH-24Han-mod2.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CeH-24Han-mod1.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod1.tdb): LIQUID, type code %, sha256 `443d2f1cbbcc0a31…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : CE H : !
~~~~

[CeH-24Han-mod2.tdb](https://orchid-project.org/data/databases/sgte-binary/CeH-24Han-mod2.tdb): LIQUID, type code %, sha256 `845d0a630766ed0a…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : CE H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2024.102701](https://doi.org/10.1016/j.calphad.2024.102701) Peter Hannappel, Ebert Alvares, Felix Heubner, Claudio Pistidda, Paul Jerabek, Thomas Weißgärber, Thermodynamic assessment of the Ce H and CeNi5 H system, Calphad 85, 102701 (2024).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

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
