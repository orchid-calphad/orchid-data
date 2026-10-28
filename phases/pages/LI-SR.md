# Li–Sr phases

> Li–Sr system: 6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-SR.html · Markdown: https://data.orchid-project.org/phases/pages/LI-SR.md

6 phases (tier A 4, tier C 1, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-SR) · [full JSON](https://data.orchid-project.org/phases/systems/LI-SR.json) · [Li–Sr system page](https://data.orchid-project.org/systems/LI-SR.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-SR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–Sr system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-li-sr-bcc-a2); _phase:li-sr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Sr) 0–1 | 0 | 1 |
| [FCC_A1](#phase-li-sr-fcc-a1); _phase:li-sr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–820 K, x(Sr) 0.99602–1 | 0 | 1 |
| [HCP_A3](#phase-li-sr-hcp-a3); _phase:li-sr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LI23SR6_D8A](#phase-li-sr-li23sr6-d8a); _phase:li-sr:li23sr6-d8a_ | Mn23Th6 · D8_a · cF116 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–422.43 K, x(Sr) 0.2069–0.2069 | 0 | 1 |
| [LI2SR3](#phase-li-sr-li2sr3); _phase:li-sr:li2sr3_ | Li2Sr3 · tP20 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–470 K, x(Sr) 0.6–0.6 | 0 | 1 |
| [LIQUID](#phase-li-sr-liquid); _phase:li-sr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 408.84–2500 K, x(Sr) 0–1 | 0 | 1 |

## BCC_A2 (Li–Sr)

- Id: `phase:li-sr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Sr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sr:bcc-a2)

Names (2): _corpus: _corpus:phase:li-sr:bcc-a2  
_tdb: _tdb:LiSr-12Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LiSr-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSr-12Che.tdb): BCC_A2, type code %B, sha256 `0f37c0f21b298d84…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : LI SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.001](https://doi.org/10.1016/j.calphad.2012.03.001) Chong Chen, Man Wang, Yong Du, Qiannan Gao, Biao Hu, Shuhong Liu, Thermodynamic modeling of the Sr–X (X=H, Li, Na, Sc) systems, Calphad 38, 17-22 (2012).  
_assessment that models this phase_

## FCC_A1 (Li–Sr)

- Id: `phase:li-sr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–820 K, x(Sr) 0.99602–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sr:fcc-a1)

Names (2): _corpus: _corpus:phase:li-sr:fcc-a1  
_tdb: _tdb:LiSr-12Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LiSr-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSr-12Che.tdb): FCC_A1, type code %A, sha256 `0f37c0f21b298d84…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : LI SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.001](https://doi.org/10.1016/j.calphad.2012.03.001) Chong Chen, Man Wang, Yong Du, Qiannan Gao, Biao Hu, Shuhong Liu, Thermodynamic modeling of the Sr–X (X=H, Li, Na, Sc) systems, Calphad 38, 17-22 (2012).  
_assessment that models this phase_

## HCP_A3 (Li–Sr)

- Id: `phase:li-sr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sr:hcp-a3)

Names (2): _corpus: _corpus:phase:li-sr:hcp-a3  
_tdb: _tdb:LiSr-12Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[LiSr-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSr-12Che.tdb): HCP_A3, type code %A, sha256 `0f37c0f21b298d84…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : LI SR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.001](https://doi.org/10.1016/j.calphad.2012.03.001) Chong Chen, Man Wang, Yong Du, Qiannan Gao, Biao Hu, Shuhong Liu, Thermodynamic modeling of the Sr–X (X=H, Li, Na, Sc) systems, Calphad 38, 17-22 (2012).  
_assessment that models this phase_

## LI23SR6_D8A (Li–Sr)

- Id: `phase:li-sr:li23sr6-d8a`; status `assigned`
- Structure: Mn23Th6 · D8_a · cF116 · Fm-3m (225); type `st:d8-a-mn23th6-cf116`; tier A: standard phase name; confidence high
- Stoichiometry: Li 0.7931, Sr 0.2069
- Stability: stable in 1 of 1 calculated diagram(s): 300–422.43 K, x(Sr) 0.2069–0.2069
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sr:li23sr6-d8a)

Names (2): _corpus: _corpus:phase:li-sr:li23sr6-d8a  
_tdb: _tdb:LiSr-12Che.tdb:LI23SR6_D8A  


### TDB models of LI23SR6_D8A (1): PHASE and CONSTITUENT statements as written

[LiSr-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSr-12Che.tdb): LI23SR6_D8A, type code %, sha256 `0f37c0f21b298d84…`

~~~~text
40: PHASE LI23SR6_D8A % 2 23 6 !
41: CONST LI23SR6_D8A : LI : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.001](https://doi.org/10.1016/j.calphad.2012.03.001) Chong Chen, Man Wang, Yong Du, Qiannan Gao, Biao Hu, Shuhong Liu, Thermodynamic modeling of the Sr–X (X=H, Li, Na, Sc) systems, Calphad 38, 17-22 (2012).  
_assessment that models this phase_

## LI2SR3 (Li–Sr)

- Id: `phase:li-sr:li2sr3`; status `assigned`
- Structure: Li2Sr3 · tP20 · P4_2/mnm (136); type `st:li2sr3-tp20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Li 0.4000, Sr 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–470 K, x(Sr) 0.6–0.6
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sr:li2sr3)

Names (2): _corpus: _corpus:phase:li-sr:li2sr3  
_tdb: _tdb:LiSr-12Che.tdb:LI2SR3  


### TDB models of LI2SR3 (1): PHASE and CONSTITUENT statements as written

[LiSr-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSr-12Che.tdb): LI2SR3, type code %, sha256 `0f37c0f21b298d84…`

~~~~text
45: PHASE LI2SR3 % 2 2 3 !
46: CONST LI2SR3 : LI : SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.001](https://doi.org/10.1016/j.calphad.2012.03.001) Chong Chen, Man Wang, Yong Du, Qiannan Gao, Biao Hu, Shuhong Liu, Thermodynamic modeling of the Sr–X (X=H, Li, Na, Sc) systems, Calphad 38, 17-22 (2012).  
_assessment that models this phase_

## LIQUID (Li–Sr)

- Id: `phase:li-sr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 408.84–2500 K, x(Sr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sr:liquid)

Names (2): _corpus: _corpus:phase:li-sr:liquid  
_tdb: _tdb:LiSr-12Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LiSr-12Che.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSr-12Che.tdb): LIQUID, type code %, sha256 `0f37c0f21b298d84…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : LI SR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.03.001](https://doi.org/10.1016/j.calphad.2012.03.001) Chong Chen, Man Wang, Yong Du, Qiannan Gao, Biao Hu, Shuhong Liu, Thermodynamic modeling of the Sr–X (X=H, Li, Na, Sc) systems, Calphad 38, 17-22 (2012).  
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
