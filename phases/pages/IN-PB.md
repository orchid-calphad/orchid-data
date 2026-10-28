# In–Pb phases

> In–Pb system: 6 phases (tier A 4, tier C 1, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-PB.html · Markdown: https://data.orchid-project.org/phases/pages/IN-PB.md

6 phases (tier A 4, tier C 1, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-PB) · [full JSON](https://data.orchid-project.org/phases/systems/IN-PB.json) · [In–Pb system page](https://data.orchid-project.org/systems/IN-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Pb system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-pb-a6-tetragonal); _phase:in-pb:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 299.48–434.61 K, x(Pb) 0–0.21183 | 3 | 3 |
| [BCC_A2](#phase-in-pb-bcc-a2); _phase:in-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-in-pb-fcc-a1); _phase:in-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 299.22–600.61 K, x(Pb) 0.29005–1 | 2 | 3 |
| [HCP_A3](#phase-in-pb-hcp-a3); _phase:in-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-in-pb-liquid); _phase:in-pb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 429.38–2500 K, x(Pb) 0–1 | 5 | 3 |
| [TET_ALPHA1_A6](#phase-in-pb-tet-a6-alpha1); _phase:in-pb:tet-a6-alpha1_ | In · A6 · tI2 · I4/mmm (139) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 3 of 3 calculated diagram(s): 299.22–449.42 K, x(Pb) 0.11316–0.33307 | 0 | 3 |

## TETRAGONAL_A6 (In–Pb)

- Id: `phase:in-pb:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 299.48–434.61 K, x(Pb) 0–0.21183
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-pb:a6-tetragonal)

Names (6): _corpus: _corpus:phase:in-pb:a6-tetragonal, corpus:phase:in-pb:tetragonal-a6  
_paper: _paper:10.1016/j.tca.2003.10.020:(In)  
_tdb: _tdb:InPb-04Dav.tdb:TETRAGONAL_A6, tdb:InPb-86Nab.tdb:TETRAGONAL_A6, tdb:InPb-98Boa-LB.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (3): PHASE and CONSTITUENT statements as written

[InPb-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb): TETRAGONAL_A6, type code %, sha256 `fa3de4d2af4fda20…`

~~~~text
42: PHASE TETRAGONAL_A6 % 1 1 !
43: CONST TETRAGONAL_A6 : IN% PB : !
~~~~

[InPb-86Nab.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb): TETRAGONAL_A6, type code %, sha256 `df14085f845d9d70…`

~~~~text
40: PHASE TETRAGONAL_A6 % 1 1 !
41: CONST TETRAGONAL_A6 : IN% PB : !
~~~~

[InPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb): TETRAGONAL_A6, type code %, sha256 `f26e4bea07c1978f…`

~~~~text
45: PHASE TETRAGONAL_A6 % 1 1 !
46: CONST TETRAGONAL_A6 : IN% PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998).  
_assessment that models this phase_

## BCC_A2 (In–Pb)

- Id: `phase:in-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-pb:bcc-a2)

Names (4): _corpus: _corpus:phase:in-pb:bcc-a2  
_tdb: _tdb:InPb-04Dav.tdb:BCC_A2, tdb:InPb-86Nab.tdb:BCC_A2, tdb:InPb-98Boa-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[InPb-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb): BCC_A2, type code %B, sha256 `fa3de4d2af4fda20…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : IN PB : VA : !
~~~~

[InPb-86Nab.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb): BCC_A2, type code %B, sha256 `df14085f845d9d70…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : IN PB : VA : !
~~~~

[InPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb): BCC_A2, type code %B, sha256 `f26e4bea07c1978f…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : IN PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998).  
_assessment that models this phase_

## FCC_A1 (In–Pb)

- Id: `phase:in-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 299.22–600.61 K, x(Pb) 0.29005–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-pb:fcc-a1)

Names (5): _corpus: _corpus:phase:in-pb:fcc-a1  
_paper: _paper:10.1016/j.tca.2003.10.020:(Pb)  
_tdb: _tdb:InPb-04Dav.tdb:FCC_A1, tdb:InPb-86Nab.tdb:FCC_A1, tdb:InPb-98Boa-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[InPb-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb): FCC_A1, type code %A, sha256 `fa3de4d2af4fda20…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : IN PB : VA : !
~~~~

[InPb-86Nab.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb): FCC_A1, type code %A, sha256 `df14085f845d9d70…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : IN PB : VA : !
~~~~

[InPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb): FCC_A1, type code %A, sha256 `f26e4bea07c1978f…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : IN PB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998).  
_assessment that models this phase_

## HCP_A3 (In–Pb)

- Id: `phase:in-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-pb:hcp-a3)

Names (4): _corpus: _corpus:phase:in-pb:hcp-a3  
_tdb: _tdb:InPb-04Dav.tdb:HCP_A3, tdb:InPb-86Nab.tdb:HCP_A3, tdb:InPb-98Boa-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[InPb-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb): HCP_A3, type code %A, sha256 `fa3de4d2af4fda20…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : IN PB : VA: !
~~~~

[InPb-86Nab.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb): HCP_A3, type code %A, sha256 `df14085f845d9d70…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : IN PB : VA: !
~~~~

[InPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb): HCP_A3, type code %A, sha256 `f26e4bea07c1978f…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : IN PB : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998).  
_assessment that models this phase_

## LIQUID (In–Pb)

- Id: `phase:in-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 429.38–2500 K, x(Pb) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-pb:liquid)

Names (5): _corpus: _corpus:phase:in-pb:liquid  
_paper: _paper:10.1016/j.tca.2003.10.020:L  
_tdb: _tdb:InPb-04Dav.tdb:LIQUID, tdb:InPb-86Nab.tdb:LIQUID, tdb:InPb-98Boa-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[InPb-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb): LIQUID, type code %, sha256 `fa3de4d2af4fda20…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : IN PB : !
~~~~

[InPb-86Nab.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb): LIQUID, type code %, sha256 `df14085f845d9d70…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : IN PB : !
~~~~

[InPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb): LIQUID, type code %, sha256 `f26e4bea07c1978f…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : IN PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998).  
_assessment that models this phase_

## TET_ALPHA1_A6 (In–Pb)

- Id: `phase:in-pb:tet-a6-alpha1`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:ALPHA1); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 3 of 3 calculated diagram(s): 299.22–449.42 K, x(Pb) 0.11316–0.33307
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-pb:tet-a6-alpha1)

Names (4): _corpus: _corpus:phase:in-pb:tet-a6-alpha1  
_tdb: _tdb:InPb-04Dav.tdb:TET_ALPHA1_A6, tdb:InPb-86Nab.tdb:TET_ALPHA1_A6, tdb:InPb-98Boa-LB.tdb:TET_ALPHA1_A6  


### TDB models of TET_ALPHA1_A6 (3): PHASE and CONSTITUENT statements as written

[InPb-04Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-04Dav.tdb): TET_ALPHA1_A6, type code %, sha256 `fa3de4d2af4fda20…`

~~~~text
47: PHASE TET_ALPHA1_A6 % 1 1 !
48: CONST TET_ALPHA1_A6 : IN PB : !
~~~~

[InPb-86Nab.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-86Nab.tdb): TET_ALPHA1_A6, type code %, sha256 `df14085f845d9d70…`

~~~~text
45: PHASE TET_ALPHA1_A6 % 1 1 !
46: CONST TET_ALPHA1_A6 : IN PB : !
~~~~

[InPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/InPb-98Boa-LB.tdb): TET_ALPHA1_A6, type code %, sha256 `f26e4bea07c1978f…`

~~~~text
50: PHASE TET_ALPHA1_A6 % 1 1 !
51: CONST TET_ALPHA1_A6 : IN PB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2003.10.020](https://doi.org/10.1016/j.tca.2003.10.020) N David, Khadija El Aissaoui, J.M Fiorani, J Hertz, M Vilasi, Thermodynamic optimization of the In–Pb–Sn system based on new evaluations of the binary borders In–Pb and In–Sn, Thermochimica Acta 413, 127-137 (2004).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86 (1998).  
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
