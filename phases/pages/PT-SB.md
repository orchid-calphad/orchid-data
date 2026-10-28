# Pt–Sb phases

> Pt–Sb system: 11 phases (tier A 8, tier B 1, tier C 1, liquid 1); 9 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PT-SB.html · Markdown: https://data.orchid-project.org/phases/pages/PT-SB.md

11 phases (tier A 8, tier B 1, tier C 1, liquid 1); 9 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PT-SB) · [full JSON](https://data.orchid-project.org/phases/systems/PT-SB.json) · [Pt–Sb system page](https://data.orchid-project.org/systems/PT-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/PT-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pt–Sb system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-pt-sb-a7-rhombohedral); _phase:pt-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 0 | 1 |
| [BCC_A2](#phase-pt-sb-bcc-a2); _phase:pt-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-pt-sb-fcc-a1); _phase:pt-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2041.5 K, x(Sb) 0–0.104 | 0 | 1 |
| [HCP_A3](#phase-pt-sb-hcp-a3); _phase:pt-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pt-sb-liquid); _phase:pt-sb:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 899.48–2500 K, x(Sb) 0–1 | 0 | 1 |
| [PT3SB_D023](#phase-pt-sb-pt3sb-d023); _phase:pt-sb:pt3sb-d023_ | Al3Zr · D0_23 · tI16 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–947.85 K, x(Sb) 0.25–0.25 | 0 | 1 |
| [PT3SB2](#phase-pt-sb-pt3sb2); _phase:pt-sb:pt3sb2_ | Pt3Sb2 · oI20 · Ibam (72) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1012.04 K, x(Sb) 0.4–0.4 | 0 | 1 |
| [PT5SB_L12](#phase-pt-sb-pt5sb-l12); _phase:pt-sb:pt5sb-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 832.97–1020.89 K, x(Sb) 0.15292–0.18524 | 0 | 1 |
| [PT7SB](#phase-pt-sb-pt7sb); _phase:pt-sb:pt7sb_ | CuPt7 · cF32 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–898.06 K, x(Sb) 0.125–0.125 | 0 | 1 |
| [PTSB_B81](#phase-pt-sb-ptsb-b81); _phase:pt-sb:ptsb-b81_ | NiAs · B8_1 · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1319.01 K, x(Sb) 0.5–0.5 | 0 | 1 |
| [PTSB2_C2](#phase-pt-sb-ptsb2-c2); _phase:pt-sb:ptsb2-c2_ | beta-FeS2 · C2 · cP12 · Pa-3 (205) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1497.58 K, x(Sb) 0.66667–0.66667 | 0 | 1 |

## RHOMBOHEDRAL_A7 (Pt–Sb)

- Id: `phase:pt-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:a7-rhombohedral)

Names (2): _corpus: _corpus:phase:pt-sb:a7-rhombohedral  
_tdb: _tdb:PtSb-14Guo.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : PT SB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## BCC_A2 (Pt–Sb)

- Id: `phase:pt-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:bcc-a2)

Names (2): _corpus: _corpus:phase:pt-sb:bcc-a2  
_tdb: _tdb:PtSb-14Guo.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): BCC_A2, type code %B, sha256 `e4786997c3df9ae3…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PT SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## FCC_A1 (Pt–Sb)

- Id: `phase:pt-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2041.5 K, x(Sb) 0–0.104
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:fcc-a1)

Names (2): _corpus: _corpus:phase:pt-sb:fcc-a1  
_tdb: _tdb:PtSb-14Guo.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): FCC_A1, type code %A, sha256 `e4786997c3df9ae3…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PT% SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## HCP_A3 (Pt–Sb)

- Id: `phase:pt-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:hcp-a3)

Names (2): _corpus: _corpus:phase:pt-sb:hcp-a3  
_tdb: _tdb:PtSb-14Guo.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): HCP_A3, type code %A, sha256 `e4786997c3df9ae3…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PT SB : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## LIQUID (Pt–Sb)

- Id: `phase:pt-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 899.48–2500 K, x(Sb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:liquid)

Names (2): _corpus: _corpus:phase:pt-sb:liquid  
_tdb: _tdb:PtSb-14Guo.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): LIQUID, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PT SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## PT3SB_D023 (Pt–Sb)

- Id: `phase:pt-sb:pt3sb-d023`; status `assigned`
- Structure: Al3Zr · D0_23 · tI16 · I4/mmm (139); type `st:d0-23-al3zr-ti16`; tier A: standard phase name; confidence high
- Stoichiometry: Pt 0.7500, Sb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–947.85 K, x(Sb) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:pt3sb-d023)

Names (2): _corpus: _corpus:phase:pt-sb:pt3sb-d023  
_tdb: _tdb:PtSb-14Guo.tdb:PT3SB_D023  


### TDB models of PT3SB_D023 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): PT3SB_D023, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
57: PHASE PT3SB_D023 % 2 3 1 !
58: CONST PT3SB_D023 : PT : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## PT3SB2 (Pt–Sb)

- Id: `phase:pt-sb:pt3sb2`; status `assigned`
- Structure: Pt3Sb2 · oI20 · Ibam (72); type `st:pt3sb2-oi20`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Pt 0.6000, Sb 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1012.04 K, x(Sb) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:pt3sb2)

Names (4): _corpus: _corpus:phase:pt-sb:pt3sb2  
_mp: _mp:mp-aaaaaxeh  
_oqmd: _oqmd:oqmd-7877  
_tdb: _tdb:PtSb-14Guo.tdb:PT3SB2  


### TDB models of PT3SB2 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): PT3SB2, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
62: PHASE PT3SB2 % 2 3 2 !
63: CONST PT3SB2 : PT : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## PT5SB_L12 (Pt–Sb)

- Id: `phase:pt-sb:pt5sb-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtSb-14Guo.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 832.97–1020.89 K, x(Sb) 0.15292–0.18524
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:pt5sb-l12)

Names (2): _corpus: _corpus:phase:pt-sb:pt5sb-l12  
_tdb: _tdb:PtSb-14Guo.tdb:PT5SB_L12  


### TDB models of PT5SB_L12 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): PT5SB_L12, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
52: PHASE PT5SB_L12 % 2 5 1 !
53: CONST PT5SB_L12 : PT% SB : PT SB% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## PT7SB (Pt–Sb)

- Id: `phase:pt-sb:pt7sb`; status `assigned`
- Structure: CuPt7 · cF32 · Fm-3m (225); type `st:cupt7-cf32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pt 0.8750, Sb 0.1250
- Stability: stable in 1 of 1 calculated diagram(s): 300–898.06 K, x(Sb) 0.125–0.125
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:pt7sb)

Names (2): _corpus: _corpus:phase:pt-sb:pt7sb  
_tdb: _tdb:PtSb-14Guo.tdb:PT7SB  


### TDB models of PT7SB (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): PT7SB, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
47: PHASE PT7SB % 2 7 1 !
48: CONST PT7SB : PT : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## PTSB_B81 (Pt–Sb)

- Id: `phase:pt-sb:ptsb-b81`; status `assigned`
- Structure: NiAs · B8_1 · hP4 · P6_3/mmc (194); type `st:b8-1-nias-hp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaefl and oqmd-3649, space group 194
- Stoichiometry: Pt 0.5000, Sb 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1319.01 K, x(Sb) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:ptsb-b81)

Names (4): _corpus: _corpus:phase:pt-sb:ptsb-b81  
_mp: _mp:mp-aaaaaefl  
_oqmd: _oqmd:oqmd-3649  
_tdb: _tdb:PtSb-14Guo.tdb:PTSB_B81  


### TDB models of PTSB_B81 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): PTSB_B81, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
67: PHASE PTSB_B81 % 2 1 1 !
68: CONST PTSB_B81 : PT : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
_assessment that models this phase_

## PTSB2_C2 (Pt–Sb)

- Id: `phase:pt-sb:ptsb2-c2`; status `assigned`
- Structure: beta-FeS2 · C2 · cP12 · Pa-3 (205); type `st:c2-beta-fes2-cp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaavq and oqmd-7991, space group 205
- Stoichiometry: Pt 0.3333, Sb 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1497.58 K, x(Sb) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-sb:ptsb2-c2)

Names (4): _corpus: _corpus:phase:pt-sb:ptsb2-c2  
_mp: _mp:mp-aaaaaavq  
_oqmd: _oqmd:oqmd-7991  
_tdb: _tdb:PtSb-14Guo.tdb:PTSB2_C2  


### TDB models of PTSB2_C2 (1): PHASE and CONSTITUENT statements as written

[PtSb-14Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/PtSb-14Guo.tdb): PTSB2_C2, type code %, sha256 `e4786997c3df9ae3…`

~~~~text
72: PHASE PTSB2_C2 % 2 1 2 !
73: CONST PTSB2_C2 : PT : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.111072](https://doi.org/10.3139/146.111072) C. Guo, C. Li, S. Shang, Z. Du, Int. J. Mater. Res, 105, 525-36(2014).  
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
