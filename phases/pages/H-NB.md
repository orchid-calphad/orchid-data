# H–Nb phases

> H–Nb system: 8 phases (tier A 4, tier C 1, liquid 1, gas 2); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-NB.html · Markdown: https://data.orchid-project.org/phases/pages/H-NB.md

8 phases (tier A 4, tier C 1, liquid 1, gas 2); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-NB) · [full JSON](https://data.orchid-project.org/phases/systems/H-NB.json) · [H–Nb system page](https://data.orchid-project.org/systems/H-NB.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-NB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Nb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-nb-bcc-a2); _phase:h-nb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2750 K, x(H) 0–0.5104 | 0 | 2 |
| [FCC_A1](#phase-h-nb-fcc-a1); _phase:h-nb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-h-nb-gas); _phase:h-nb:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(H) 0.98989–1 | 0 | 2 |
| [H2GAS](#phase-h-nb-h2gas); _phase:h-nb:h2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1220 K, x(H) 1–1 | 0 | 2 |
| [HCP_A3](#phase-h-nb-hcp-a3); _phase:h-nb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-h-nb-liquid); _phase:h-nb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2748.56–4000 K, x(H) 0–0.00504 | 0 | 2 |
| [NBH](#phase-h-nb-nbh); _phase:h-nb:nbh_ | NbH · oP8 · Pnnn (48) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–429.33 K, x(H) 0.40775–0.5 | 0 | 2 |
| [NBH2_C1](#phase-h-nb-nbh2-c1); _phase:h-nb:nbh2-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 300–430.66 K, x(H) 0.66285–0.66662 | 0 | 2 |

## BCC_A2 (H–Nb)

- Id: `phase:h-nb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2750 K, x(H) 0–0.5104
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:bcc-a2)

Names (3): _corpus: _corpus:phase:h-nb:bcc-a2  
_tdb: _tdb:NbH-23Dot.tdb:BCC_A2, tdb:NbH-97Ans-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): BCC_A2, type code %B, sha256 `79b1cf5db71443aa…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : NB% : H VA% : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): BCC_A2, type code %B, sha256 `5f71226cd001bd44…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : NB% : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## FCC_A1 (H–Nb)

- Id: `phase:h-nb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:fcc-a1)

Names (3): _corpus: _corpus:phase:h-nb:fcc-a1  
_tdb: _tdb:NbH-23Dot.tdb:FCC_A1, tdb:NbH-97Ans-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): FCC_A1, type code %A, sha256 `79b1cf5db71443aa…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : NB : H VA% : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): FCC_A1, type code %A, sha256 `5f71226cd001bd44…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : NB : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## GAS (H–Nb)

- Id: `phase:h-nb:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(H) 0.98989–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:gas)

Names (3): _corpus: _corpus:phase:h-nb:gas  
_tdb: _tdb:NbH-23Dot.tdb:GAS, tdb:NbH-97Ans-LB.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): GAS, type code %, sha256 `79b1cf5db71443aa…`

~~~~text
54: PHASE GAS:G % 1 1 !
55: CONST GAS:G : NB H H2 : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): GAS, type code %, sha256 `5f71226cd001bd44…`

~~~~text
53: PHASE GAS:G % 1 1 !
54: CONST GAS:G : H H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## H2GAS (H–Nb)

- Id: `phase:h-nb:h2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1220 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:h2gas)

Names (3): _corpus: _corpus:phase:h-nb:h2gas  
_tdb: _tdb:NbH-23Dot.tdb:H2GAS, tdb:NbH-97Ans-LB.tdb:H2GAS  


### TDB models of H2GAS (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): H2GAS, type code %, sha256 `79b1cf5db71443aa…`

~~~~text
57: PHASE H2GAS % 1 1 !
58: CONST H2GAS : H2 : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): H2GAS, type code %, sha256 `5f71226cd001bd44…`

~~~~text
56: PHASE H2GAS % 1 1 !
57: CONST H2GAS : H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## HCP_A3 (H–Nb)

- Id: `phase:h-nb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:hcp-a3)

Names (3): _corpus: _corpus:phase:h-nb:hcp-a3  
_tdb: _tdb:NbH-23Dot.tdb:HCP_A3, tdb:NbH-97Ans-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): HCP_A3, type code %A, sha256 `79b1cf5db71443aa…`

~~~~text
40: PHASE HCP_A3 %A 2 1 2 !
41: CONST HCP_A3 : NB : H VA% : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): HCP_A3, type code %A, sha256 `5f71226cd001bd44…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : NB : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## LIQUID (H–Nb)

- Id: `phase:h-nb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2748.56–4000 K, x(H) 0–0.00504
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:liquid)

Names (3): _corpus: _corpus:phase:h-nb:liquid  
_tdb: _tdb:NbH-23Dot.tdb:LIQUID, tdb:NbH-97Ans-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): LIQUID, type code %, sha256 `79b1cf5db71443aa…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : H NB : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): LIQUID, type code %, sha256 `5f71226cd001bd44…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : H NB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## NBH (H–Nb)

- Id: `phase:h-nb:nbh`; status `assigned`
- Structure: NbH · oP8 · Pnnn (48); type `st:nbh-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 2 of 2 calculated diagram(s): 300–429.33 K, x(H) 0.40775–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:nbh)

Names (3): _corpus: _corpus:phase:h-nb:nbh  
_tdb: _tdb:NbH-23Dot.tdb:NBH, tdb:NbH-97Ans-LB.tdb:NBH  


### TDB models of NBH (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): NBH, type code %, sha256 `79b1cf5db71443aa…`

~~~~text
46: PHASE NBH % 2 1 1 !
47: CONST NBH : NB : H% VA : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): NBH, type code %, sha256 `5f71226cd001bd44…`

~~~~text
45: PHASE NBH % 2 1 1 !
46: CONST NBH : NB : H% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
_assessment that models this phase_

## NBH2_C1 (H–Nb)

- Id: `phase:h-nb:nbh2-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–430.66 K, x(H) 0.66285–0.66662
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-nb:nbh2-c1)

Names (3): _corpus: _corpus:phase:h-nb:nbh2-c1  
_tdb: _tdb:NbH-23Dot.tdb:NBH2_C1, tdb:NbH-97Ans-LB.tdb:NBH2_C1  


### TDB models of NBH2_C1 (2): PHASE and CONSTITUENT statements as written

[NbH-23Dot.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-23Dot.tdb): NBH2_C1, type code %, sha256 `79b1cf5db71443aa…`

~~~~text
51: PHASE NBH2_C1 % 2 1 2 !
52: CONST NBH2_C1 : NB : H% VA : !
~~~~

[NbH-97Ans-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbH-97Ans-LB.tdb): NBH2_C1, type code %, sha256 `5f71226cd001bd44…`

~~~~text
50: PHASE NBH2_C1 % 2 1 2 !
51: CONST NBH2_C1 : NB : H% VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2023.102617](https://doi.org/10.1016/j.calphad.2023.102617) Maxime Dottor, Jean-Claude Crivello, Jean-Marc Joubert, Critical reassessment of the H–Nb system and experimental investigation and thermodynamic modeling of the H–Nb–Zr system, Calphad 83, 102617 (2023).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(96)02652-7](https://doi.org/10.1016/S0925-8388%2896%2902652-7) I. Ansara, N. Dupin, unpublished, 1997.  
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
