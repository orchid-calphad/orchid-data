# Sc–Zn phases

> Sc–Zn system: 9 phases (tier A 5, tier C 3, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SC-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/SC-ZN.md

9 phases (tier A 5, tier C 3, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SC-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/SC-ZN.json) · [Sc–Zn system page](https://data.orchid-project.org/systems/SC-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/SC-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sc–Zn system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-sc-zn-bcc-a2); _phase:sc-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1607.31–1817.9 K, x(Zn) 0–0.00155 | 1 | 1 |
| [FCC_A1](#phase-sc-zn-fcc-a1); _phase:sc-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-sc-zn-hcp-a3); _phase:sc-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.72 K, x(Zn) 0–1 | 5 | 1 |
| [LIQUID](#phase-sc-zn-liquid); _phase:sc-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 692.22–2500 K, x(Zn) 0–1 | 15 | 1 |
| [SC13ZN58](#phase-sc-zn-sc13zn58); _phase:sc-zn:sc13zn58_ | Gd13Zn58 · hP142 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1093.12 K, x(Zn) 0.8169–0.8169 | 8 | 1 |
| [SC3ZN17](#phase-sc-zn-sc3zn17); _phase:sc-zn:sc3zn17_ | Be17Ru3 · cI60 · Im-3 (204) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1087.76 K, x(Zn) 0.85–0.85 | 6 | 1 |
| [SCZN_B2](#phase-sc-zn-sczn-b2); _phase:sc-zn:sczn-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1502.59 K, x(Zn) 0.5–0.5 | 6 | 1 |
| [SCZN12_D2B](#phase-sc-zn-sczn12-d2b); _phase:sc-zn:sczn12-d2b_ | Mn12Th · D2_b · tI26 · I4/mmm (139) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 4 | 1 |
| [SCZN2](#phase-sc-zn-sczn2); _phase:sc-zn:sczn2_ | Hg2U · hP3 · P6/mmm (191) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1298.04 K, x(Zn) 0.66667–0.66667 | 8 | 1 |

## BCC_A2 (Sc–Zn)

- Id: `phase:sc-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1607.31–1817.9 K, x(Zn) 0–0.00155
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:sc-zn:bcc-a2  
_paper: _paper:10.2298/jmmb110909017t:βSc  
_tdb: _tdb:ScZn-12Tan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): BCC_A2, type code %B, sha256 `7b51650bade528a1…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SC% ZN : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Sc–Zn)

- Id: `phase:sc-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:fcc-a1)

Names (2): _corpus: _corpus:phase:sc-zn:fcc-a1  
_tdb: _tdb:ScZn-12Tan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): FCC_A1, type code %A, sha256 `7b51650bade528a1…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SC ZN : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase_

## HCP_A3 (Sc–Zn)

- Id: `phase:sc-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.72 K, x(Zn) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:hcp-a3)

Names (5): _corpus: _corpus:phase:sc-zn:hcp-a3  
_paper: _paper:10.2298/jmmb110909017t:(Zn), paper:10.2298/jmmb110909017t:Hcp_A3, paper:10.2298/jmmb110909017t:αSc  
_tdb: _tdb:ScZn-12Tan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): HCP_A3, type code %A, sha256 `7b51650bade528a1…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : SC% ZN% : VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

## LIQUID (Sc–Zn)

- Id: `phase:sc-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 692.22–2500 K, x(Zn) 0–1
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:liquid)

Names (3): _corpus: _corpus:phase:sc-zn:liquid  
_paper: _paper:10.2298/jmmb110909017t:L  
_tdb: _tdb:ScZn-12Tan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): LIQUID, type code %, sha256 `7b51650bade528a1…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SC ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

## SC13ZN58 (Sc–Zn)

- Id: `phase:sc-zn:sc13zn58`; status `assigned`
- Structure: Gd13Zn58 · hP142 · P6_3/mmc (194); type `st:gd13zn58-hp142`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sc 0.1831, Zn 0.8169
- Stability: stable in 1 of 1 calculated diagram(s): 300–1093.12 K, x(Zn) 0.8169–0.8169
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:sc13zn58)

Names (3): _corpus: _corpus:phase:sc-zn:sc13zn58  
_paper: _paper:10.2298/jmmb110909017t:Sc13Zn58  
_tdb: _tdb:ScZn-12Tan.tdb:SC13ZN58  


### TDB models of SC13ZN58 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): SC13ZN58, type code %, sha256 `7b51650bade528a1…`

~~~~text
51: PHASE SC13ZN58 % 2 13 58 !
52: CONST SC13ZN58 : SC : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

## SC3ZN17 (Sc–Zn)

- Id: `phase:sc-zn:sc3zn17`; status `assigned`
- Structure: Be17Ru3 · cI60 · Im-3 (204); type `st:be17ru3-ci60`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sc 0.1500, Zn 0.8500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1087.76 K, x(Zn) 0.85–0.85
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:sc3zn17)

Names (3): _corpus: _corpus:phase:sc-zn:sc3zn17  
_paper: _paper:10.2298/jmmb110909017t:Sc3Zn17  
_tdb: _tdb:ScZn-12Tan.tdb:SC3ZN17  


### TDB models of SC3ZN17 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): SC3ZN17, type code %, sha256 `7b51650bade528a1…`

~~~~text
56: PHASE SC3ZN17 % 2 3 17 !
57: CONST SC3ZN17 : SC : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

## SCZN_B2 (Sc–Zn)

- Id: `phase:sc-zn:sczn-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaarcw and oqmd-18106, space group 221
- Stoichiometry: Sc 0.5000, Zn 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1502.59 K, x(Zn) 0.5–0.5
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:sczn-b2)

Names (5): _corpus: _corpus:phase:sc-zn:sczn-b2  
_mp: _mp:mp-aaaaarcw  
_oqmd: _oqmd:oqmd-18106  
_paper: _paper:10.2298/jmmb110909017t:ScZn  
_tdb: _tdb:ScZn-12Tan.tdb:SCZN_B2  


### TDB models of SCZN_B2 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): SCZN_B2, type code %, sha256 `7b51650bade528a1…`

~~~~text
41: PHASE SCZN_B2 % 2 1 1 !
42: CONST SCZN_B2 : SC : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

## SCZN12_D2B (Sc–Zn)

- Id: `phase:sc-zn:sczn12-d2b`; status `assigned`
- Structure: Mn12Th · D2_b · tI26 · I4/mmm (139); type `st:d2-b-mn12th-ti26`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaarcx and oqmd-18107, space group 139
- Stoichiometry: Sc 0.0769, Zn 0.9231
- Stability: not stable in 1 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:sczn12-d2b)

Names (5): _corpus: _corpus:phase:sc-zn:sczn12-d2b  
_mp: _mp:mp-aaaaarcx  
_oqmd: _oqmd:oqmd-18107  
_paper: _paper:10.2298/jmmb110909017t:ScZn12  
_tdb: _tdb:ScZn-12Tan.tdb:SCZN12_D2B  


### TDB models of SCZN12_D2B (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): SCZN12_D2B, type code %, sha256 `7b51650bade528a1…`

~~~~text
61: PHASE SCZN12_D2B % 2 1 12 !
62: CONST SCZN12_D2B : SC : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

## SCZN2 (Sc–Zn)

- Id: `phase:sc-zn:sczn2`; status `assigned`
- Structure: Hg2U · hP3 · P6/mmm (191); type `st:hg2u-hp3`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Sc 0.3333, Zn 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1298.04 K, x(Zn) 0.66667–0.66667
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-zn:sczn2)

Names (3): _corpus: _corpus:phase:sc-zn:sczn2  
_paper: _paper:10.2298/jmmb110909017t:ScZn2  
_tdb: _tdb:ScZn-12Tan.tdb:SCZN2  


### TDB models of SCZN2 (1): PHASE and CONSTITUENT statements as written

[ScZn-12Tan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScZn-12Tan.tdb): SCZN2, type code %, sha256 `7b51650bade528a1…`

~~~~text
46: PHASE SCZN2 % 2 1 2 !
47: CONST SCZN2 : SC : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.2298/JMMB110909017T](https://doi.org/10.2298/JMMB110909017T) C. Tang, P. Zhou, D.D. Zhao, X.M. Yuan, Y. Tang, P.S. Wang, B. Hu, Y. Du, H.H. Xu, J. Mining Metall. B, 48, 123-30(2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(96)02576-5](https://doi.org/10.1016/s0925-8388%2896%2902576-5) A. Palenzona, P. Manfrinetti, J. Alloy. Compd.¬, 247 (1997) 195.  
_cited as the source of values for this phase_

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
