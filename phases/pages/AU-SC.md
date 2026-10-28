# Au–Sc phases

> Au–Sc system: 10 phases (tier A 8, tier C 1, liquid 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-SC.html · Markdown: https://data.orchid-project.org/phases/pages/AU-SC.md

10 phases (tier A 8, tier C 1, liquid 1); 10 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-SC) · [full JSON](https://data.orchid-project.org/phases/systems/AU-SC.json) · [Au–Sc system page](https://data.orchid-project.org/systems/AU-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Sc system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [AU2SC_C11B](#phase-au-sc-au2sc-c11b); _phase:au-sc:au2sc-c11b_ | MoSi2 · C11_b · tI6 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1885.59 K, x(Sc) 0.33333–0.33333 | 0 | 1 |
| [AU2SC7](#phase-au-sc-au2sc7); _phase:au-sc:au2sc7_ | Au2Sc7 · oI142 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1406.89 K, x(Sc) 0.77778–0.77778 | 0 | 1 |
| [AU3SC_D0A](#phase-au-sc-au3sc-d0a); _phase:au-sc:au3sc-d0a_ | beta-Cu3Ti · D0_a · oP8 · Pmmn (59) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1580.33 K, x(Sc) 0.25–0.25 | 0 | 1 |
| [AU4SC_D1A](#phase-au-sc-au4sc-d1a); _phase:au-sc:au4sc-d1a_ | MoNi4 · D1_a · tI10 · I4/m (87) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1498.03 K, x(Sc) 0.2–0.2 | 0 | 1 |
| [AUSC_B2](#phase-au-sc-ausc-b2); _phase:au-sc:ausc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1973.08 K, x(Sc) 0.5–0.5 | 0 | 1 |
| [AUSC2_C37](#phase-au-sc-ausc2-c37); _phase:au-sc:ausc2-c37_ | Co2Si · C37 · oP12 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1546.78 K, x(Sc) 0.66667–0.66667 | 0 | 1 |
| [BCC_A2](#phase-au-sc-bcc-a2); _phase:au-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1607.99–2499.82 K, x(Sc) 1–1 | 0 | 1 |
| [FCC_A1](#phase-au-sc-fcc-a1); _phase:au-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1338.65 K, x(Sc) 0–0.09369 | 0 | 1 |
| [HCP_A3](#phase-au-sc-hcp-a3); _phase:au-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Sc) 1–1 | 0 | 1 |
| [LIQUID](#phase-au-sc-liquid); _phase:au-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1305.94–2500 K, x(Sc) 0–1 | 0 | 1 |

## AU2SC_C11B (Au–Sc)

- Id: `phase:au-sc:au2sc-c11b`; status `assigned`
- Structure: MoSi2 · C11_b · tI6 · I4/mmm (139); type `st:c11-b-mosi2-ti6`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacfydo and oqmd-28211, space group 139
- Stoichiometry: Au 0.6667, Sc 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1885.59 K, x(Sc) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:au2sc-c11b)

Names (4): _corpus: _corpus:phase:au-sc:au2sc-c11b  
_mp: _mp:mp-aaacfydo  
_oqmd: _oqmd:oqmd-28211  
_tdb: _tdb:AuSc-16Xu.tdb:AU2SC_C11B  


### TDB models of AU2SC_C11B (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): AU2SC_C11B, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
50: PHASE AU2SC_C11B % 2 2 1 !
51: CONST AU2SC_C11B : AU : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## AU2SC7 (Au–Sc)

- Id: `phase:au-sc:au2sc7`; status `assigned`
- Structure: Au2Sc7 · oI142 · Immm (71); type `st:au2sc7-oi142`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Au 0.2222, Sc 0.7778
- Stability: stable in 1 of 1 calculated diagram(s): 300–1406.89 K, x(Sc) 0.77778–0.77778
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:au2sc7)

Names (2): _corpus: _corpus:phase:au-sc:au2sc7  
_tdb: _tdb:AuSc-16Xu.tdb:AU2SC7  


### TDB models of AU2SC7 (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): AU2SC7, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
65: PHASE AU2SC7 % 2 2 7 !
66: CONST AU2SC7 : AU : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## AU3SC_D0A (Au–Sc)

- Id: `phase:au-sc:au3sc-d0a`; status `assigned`
- Structure: beta-Cu3Ti · D0_a · oP8 · Pmmn (59); type `st:d0-a-beta-cu3ti-op8`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.7500, Sc 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1580.33 K, x(Sc) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:au3sc-d0a)

Names (2): _corpus: _corpus:phase:au-sc:au3sc-d0a  
_tdb: _tdb:AuSc-16Xu.tdb:AU3SC_D0A  


### TDB models of AU3SC_D0A (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): AU3SC_D0A, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
45: PHASE AU3SC_D0A % 2 3 1 !
46: CONST AU3SC_D0A : AU : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## AU4SC_D1A (Au–Sc)

- Id: `phase:au-sc:au4sc-d1a`; status `assigned`
- Structure: MoNi4 · D1_a · tI10 · I4/m (87); type `st:d1-a-moni4-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaciuoc and oqmd-28212, space group 87
- Stoichiometry: Au 0.8000, Sc 0.2000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1498.03 K, x(Sc) 0.2–0.2
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:au4sc-d1a)

Names (4): _corpus: _corpus:phase:au-sc:au4sc-d1a  
_mp: _mp:mp-aaaciuoc  
_oqmd: _oqmd:oqmd-28212  
_tdb: _tdb:AuSc-16Xu.tdb:AU4SC_D1A  


### TDB models of AU4SC_D1A (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): AU4SC_D1A, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
40: PHASE AU4SC_D1A % 2 4 1 !
41: CONST AU4SC_D1A : AU : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## AUSC_B2 (Au–Sc)

- Id: `phase:au-sc:ausc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Au 0.5000, Sc 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1973.08 K, x(Sc) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:ausc-b2)

Names (2): _corpus: _corpus:phase:au-sc:ausc-b2  
_tdb: _tdb:AuSc-16Xu.tdb:AUSC_B2  


### TDB models of AUSC_B2 (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): AUSC_B2, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
55: PHASE AUSC_B2 % 2 1 1 !
56: CONST AUSC_B2 : AU : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## AUSC2_C37 (Au–Sc)

- Id: `phase:au-sc:ausc2-c37`; status `assigned`
- Structure: Co2Si · C37 · oP12 · Pnma (62); type `st:c37-co2si-op12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaacquof and oqmd-1376725, space group 62
- Stoichiometry: Au 0.3333, Sc 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1546.78 K, x(Sc) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:ausc2-c37)

Names (4): _corpus: _corpus:phase:au-sc:ausc2-c37  
_mp: _mp:mp-aaacquof  
_oqmd: _oqmd:oqmd-1376725  
_tdb: _tdb:AuSc-16Xu.tdb:AUSC2_C37  


### TDB models of AUSC2_C37 (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): AUSC2_C37, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
60: PHASE AUSC2_C37 % 2 1 2 !
61: CONST AUSC2_C37 : AU : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## BCC_A2 (Au–Sc)

- Id: `phase:au-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1607.99–2499.82 K, x(Sc) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:bcc-a2)

Names (2): _corpus: _corpus:phase:au-sc:bcc-a2  
_tdb: _tdb:AuSc-16Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): BCC_A2, type code %B, sha256 `f1e86fcfc0683af1…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AU SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## FCC_A1 (Au–Sc)

- Id: `phase:au-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1338.65 K, x(Sc) 0–0.09369
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:fcc-a1)

Names (2): _corpus: _corpus:phase:au-sc:fcc-a1  
_tdb: _tdb:AuSc-16Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): FCC_A1, type code %A, sha256 `f1e86fcfc0683af1…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AU% SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## HCP_A3 (Au–Sc)

- Id: `phase:au-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Sc) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:hcp-a3)

Names (2): _corpus: _corpus:phase:au-sc:hcp-a3  
_tdb: _tdb:AuSc-16Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): HCP_A3, type code %A, sha256 `f1e86fcfc0683af1…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AU SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
_assessment that models this phase_

## LIQUID (Au–Sc)

- Id: `phase:au-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1305.94–2500 K, x(Sc) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-sc:liquid)

Names (2): _corpus: _corpus:phase:au-sc:liquid  
_tdb: _tdb:AuSc-16Xu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[AuSc-16Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/AuSc-16Xu.tdb): LIQUID, type code %, sha256 `f1e86fcfc0683af1…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AU SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2016.07.002](https://doi.org/10.1016/j.calphad.2016.07.002) K. Xu, S. Liu, F. Zhang, Y. Du, Z. Jin, Calphad, 54, 158-64(2016).  
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
