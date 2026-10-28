# Ga–V phases

> Ga–V system: 10 phases (tier A 6, tier B 2, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-V.html · Markdown: https://data.orchid-project.org/phases/pages/GA-V.md

10 phases (tier A 6, tier B 2, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-V) · [full JSON](https://data.orchid-project.org/phases/systems/GA-V.json) · [Ga–V system page](https://data.orchid-project.org/systems/GA-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–V system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-v-a11-orthorhombic); _phase:ga-v:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(V) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ga-v-bcc-a2); _phase:ga-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2478 K, x(V) 0.591–1 | 0 | 1 |
| [FCC_A1](#phase-ga-v-fcc-a1); _phase:ga-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [GA41V8](#phase-ga-v-ga41v8); _phase:ga-v:ga41v8_ | Ga41V8 · hR49 · R-3 (148) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–773.29 K, x(V) 0.16327–0.16327 | 0 | 1 |
| [GA5V2](#phase-ga-v-ga5v2); _phase:ga-v:ga5v2_ | Hg5Mn2 · tP14 · P4/mbm (127) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1351.47 K, x(V) 0.28571–0.28571 | 0 | 1 |
| [GA5V6](#phase-ga-v-ga5v6); _phase:ga-v:ga5v6_ | Sn5Ti6-beta · hP22 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1386.7 K, x(V) 0.53539–0.55567 | 0 | 1 |
| [GA7V6_D82](#phase-ga-v-ga7v6-d82); _phase:ga-v:ga7v6-d82_ | Cu5Zn8 · D8_2 · cI52 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1266.99–1417.55 K, x(V) 0.44921–0.46782 | 0 | 1 |
| [GAV3_A15](#phase-ga-v-gav3-a15); _phase:ga-v:gav3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1568.31 K, x(V) 0.69261–0.82282 | 0 | 1 |
| [HCP_A3](#phase-ga-v-hcp-a3); _phase:ga-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ga-v-liquid); _phase:ga-v:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–4000 K, x(V) 0–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (Ga–V)

- Id: `phase:ga-v:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(V) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:ga-v:a11-orthorhombic  
_tdb: _tdb:GaV-15Lin.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): ORTHORHOMBIC_A11, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
40: PHASE ORTHORHOMBIC_A11 % 1 1 !
41: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## BCC_A2 (Ga–V)

- Id: `phase:ga-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2478 K, x(V) 0.591–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-v:bcc-a2  
_tdb: _tdb:GaV-15Lin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): BCC_A2, type code %B, sha256 `e0ba36a5e34dfeb7…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : GA V% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## FCC_A1 (Ga–V)

- Id: `phase:ga-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-v:fcc-a1  
_tdb: _tdb:GaV-15Lin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): FCC_A1, type code %A, sha256 `e0ba36a5e34dfeb7…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : GA V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## GA41V8 (Ga–V)

- Id: `phase:ga-v:ga41v8`; status `assigned`
- Structure: Ga41V8 · hR49 · R-3 (148); type `st:ga41v8-hr49`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ga 0.8367, V 0.1633
- Stability: stable in 1 of 1 calculated diagram(s): 300–773.29 K, x(V) 0.16327–0.16327
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:ga41v8)

Names (4): _corpus: _corpus:phase:ga-v:ga41v8  
_mp: _mp:mp-aaaabgmv  
_oqmd: _oqmd:oqmd-32812  
_tdb: _tdb:GaV-15Lin.tdb:GA41V8  


### TDB models of GA41V8 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): GA41V8, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
45: PHASE GA41V8 % 2 41 8 !
46: CONST GA41V8 : GA : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## GA5V2 (Ga–V)

- Id: `phase:ga-v:ga5v2`; status `assigned`
- Structure: Hg5Mn2 · tP14 · P4/mbm (127); type `st:hg5mn2-tp14`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ga 0.7143, V 0.2857
- Stability: stable in 1 of 1 calculated diagram(s): 300–1351.47 K, x(V) 0.28571–0.28571
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:ga5v2)

Names (4): _corpus: _corpus:phase:ga-v:ga5v2  
_mp: _mp:mp-aaaabeev  
_oqmd: _oqmd:oqmd-19440  
_tdb: _tdb:GaV-15Lin.tdb:GA5V2  


### TDB models of GA5V2 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): GA5V2, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
50: PHASE GA5V2 % 2 5 2 !
51: CONST GA5V2 : GA : V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## GA5V6 (Ga–V)

- Id: `phase:ga-v:ga5v6`; status `assigned`
- Structure: Sn5Ti6-beta · hP22 · P6_3/mmc (194); type `st:sn5ti6-beta-hp22`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1386.7 K, x(V) 0.53539–0.55567
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:ga5v6)

Names (2): _corpus: _corpus:phase:ga-v:ga5v6  
_tdb: _tdb:GaV-15Lin.tdb:GA5V6  


### TDB models of GA5V6 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): GA5V6, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
60: PHASE GA5V6 % 2 5 6 !
61: CONST GA5V6 : GA% V : GA V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## GA7V6_D82 (Ga–V)

- Id: `phase:ga-v:ga7v6-d82`; status `assigned`
- Structure: Cu5Zn8 · D8_2 · cI52 · I-43m (217); type `st:d8-2-cu5zn8-ci52`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GaV-15Lin.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1266.99–1417.55 K, x(V) 0.44921–0.46782
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:ga7v6-d82)

Names (2): _corpus: _corpus:phase:ga-v:ga7v6-d82  
_tdb: _tdb:GaV-15Lin.tdb:GA7V6_D82  


### TDB models of GA7V6_D82 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): GA7V6_D82, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
55: PHASE GA7V6_D82 % 4 2 3 2 6 !
56: CONST GA7V6_D82 : V : V : GA V : GA% V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## GAV3_A15 (Ga–V)

- Id: `phase:ga-v:gav3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in GaV-15Lin.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1568.31 K, x(V) 0.69261–0.82282
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:gav3-a15)

Names (2): _corpus: _corpus:phase:ga-v:gav3-a15  
_tdb: _tdb:GaV-15Lin.tdb:GAV3_A15  


### TDB models of GAV3_A15 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): GAV3_A15, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
65: PHASE GAV3_A15 % 2 1 3 !
66: CONST GAV3_A15 : GA% V : GA V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## HCP_A3 (Ga–V)

- Id: `phase:ga-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:hcp-a3)

Names (2): _corpus: _corpus:phase:ga-v:hcp-a3  
_tdb: _tdb:GaV-15Lin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): HCP_A3, type code %A, sha256 `e0ba36a5e34dfeb7…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : GA V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
_assessment that models this phase_

## LIQUID (Ga–V)

- Id: `phase:ga-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–4000 K, x(V) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-v:liquid)

Names (2): _corpus: _corpus:phase:ga-v:liquid  
_tdb: _tdb:GaV-15Lin.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaV-15Lin.tdb](https://orchid-project.org/data/databases/sgte-binary/GaV-15Lin.tdb): LIQUID, type code %, sha256 `e0ba36a5e34dfeb7…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : GA V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2015.08.007](https://doi.org/10.1016/j.calphad.2015.08.007) D. Ling, S. Liu, X. Lu, C. Zhang, Y. Du, Calphad, 51, 125-32(2015).  
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
