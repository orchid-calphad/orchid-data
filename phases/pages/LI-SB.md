# Li–Sb phases

> Li–Sb system: 8 phases (tier A 6, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/LI-SB.html · Markdown: https://data.orchid-project.org/phases/pages/LI-SB.md

8 phases (tier A 6, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=LI-SB) · [full JSON](https://data.orchid-project.org/phases/systems/LI-SB.json) · [Li–Sb system page](https://data.orchid-project.org/systems/LI-SB.html) · [Markdown](https://data.orchid-project.org/phases/pages/LI-SB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Li–Sb system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-li-sb-a7-rhombohedral); _phase:li-sb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Sb) 1–1 | 7 | 2 |
| [BCC_A2](#phase-li-sb-bcc-a2); _phase:li-sb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–453.6 K, x(Sb) 0–0 | 9 | 2 |
| [FCC_A1](#phase-li-sb-fcc-a1); _phase:li-sb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-li-sb-hcp-a3); _phase:li-sb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LI2SB](#phase-li-sb-li2sb); _phase:li-sb:li2sb_ | GaMg2 · hP18 · P-62c (190) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–864.15 K, x(Sb) 0.33333–0.33333 | 32 | 2 |
| [LI3SB_D018](#phase-li-sb-li3sb-d018); _phase:li-sb:li3sb-d018_ | Na3As · D0_18 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1580.27 K, x(Sb) 0.25–0.25 | 7 | 2 |
| [LI3SB_D03](#phase-li-sb-li3sb-d03); _phase:li-sb:li3sb-d03_ | BiF3 · D0_3 · cF16 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1160.49 K, x(Sb) 0.25–0.25 | 7 | 1 |
| [LIQUID](#phase-li-sb-liquid); _phase:li-sb:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 441.35–2500 K, x(Sb) 0–1 | 197 | 2 |

## RHOMBOHEDRAL_A7 (Li–Sb)

- Id: `phase:li-sb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Sb) 1–1
- Literature: 7 values (7 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:a7-rhombohedral)

Names (6): _corpus: _corpus:phase:li-sb:a7-rhombohedral, corpus:phase:li-sb:rhombohedral-a7  
_paper: _paper:10.1016/j.calphad.2017.01.005:(Sb), paper:10.1016/j.jallcom.2016.12.399:(Sb)  
_tdb: _tdb:LiSb-17Li.tdb:RHOMBOHEDRAL_A7, tdb:LiSb-17Zha.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `3680314cebef8591…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `69f9831503080727…`

~~~~text
49: PHASE RHOMBOHEDRAL_A7 % 1 1 !
50: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Li–Sb)

- Id: `phase:li-sb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–453.6 K, x(Sb) 0–0
- Literature: 9 values (9 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:bcc-a2)

Names (6): _corpus: _corpus:phase:li-sb:bcc-a2  
_paper: _paper:10.1016/j.calphad.2017.01.005:(Li), paper:10.1016/j.calphad.2017.01.005:βLi3Sb, paper:10.1016/j.jallcom.2016.12.399:(Li)  
_tdb: _tdb:LiSb-17Li.tdb:BCC_A2, tdb:LiSb-17Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): BCC_A2, type code %B, sha256 `3680314cebef8591…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : LI% SB : VA : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): BCC_A2, type code %B, sha256 `69f9831503080727…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : LI% SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Li–Sb)

- Id: `phase:li-sb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:fcc-a1)

Names (3): _corpus: _corpus:phase:li-sb:fcc-a1  
_tdb: _tdb:LiSb-17Li.tdb:FCC_A1, tdb:LiSb-17Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): FCC_A1, type code %A, sha256 `3680314cebef8591…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : LI SB : VA : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): FCC_A1, type code %A, sha256 `69f9831503080727…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : LI SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase_

## HCP_A3 (Li–Sb)

- Id: `phase:li-sb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:hcp-a3)

Names (3): _corpus: _corpus:phase:li-sb:hcp-a3  
_tdb: _tdb:LiSb-17Li.tdb:HCP_A3, tdb:LiSb-17Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): HCP_A3, type code %A, sha256 `3680314cebef8591…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : LI SB : VA : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): HCP_A3, type code %A, sha256 `69f9831503080727…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : LI SB : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase_

## LI2SB (Li–Sb)

- Id: `phase:li-sb:li2sb`; status `assigned`
- Structure: GaMg2 · hP18 · P-62c (190); type `st:gamg2-hp18`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (mp_oqmd_space_groups_differ, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Li 0.6667, Sb 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–864.15 K, x(Sb) 0.33333–0.33333
- Literature: 32 values (32 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:li2sb)

Names (5): _corpus: _corpus:phase:li-sb:li2sb  
_paper: _paper:10.1016/j.calphad.2017.01.005:Li2Sb, paper:10.1016/j.jallcom.2016.12.399:Li2Sb  
_tdb: _tdb:LiSb-17Li.tdb:LI2SB, tdb:LiSb-17Zha.tdb:LI2SB  


### TDB models of LI2SB (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): LI2SB, type code %, sha256 `3680314cebef8591…`

~~~~text
57: PHASE LI2SB % 2 2 1 !
58: CONST LI2SB : LI : SB : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): LI2SB, type code %, sha256 `69f9831503080727…`

~~~~text
64: PHASE LI2SB % 2 2 1 !
65: CONST LI2SB : LI : SB : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2016.02.235](https://doi.org/10.1016/j.jallcom.2016.02.235) Sylwia Terlicka, Adam Dębski, Przemyslaw Fima, Enthalpy of formation of Li2Sb and Li3Sb and mixing enthalpy of liquid Li–Sb alloys, Journal of Alloys and Compounds 673, 272-277 (2016).  
_cited as the source of values for this phase_

## LI3SB_D018 (Li–Sb)

- Id: `phase:li-sb:li3sb-d018`; status `assigned`
- Structure: Na3As · D0_18 · hP8 · P6_3/mmc (194); type `st:d0-18-na3as-hp8`; tier A: standard phase name; confidence high
- Stoichiometry: Li 0.7500, Sb 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1580.27 K, x(Sb) 0.25–0.25
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:li3sb-d018)

Names (4): _corpus: _corpus:phase:li-sb:li3sb-d018  
_paper: _paper:10.1016/j.jallcom.2016.12.399:Li3Sb  
_tdb: _tdb:LiSb-17Li.tdb:LI3SB_D018, tdb:LiSb-17Zha.tdb:LI3SB_D018  


### TDB models of LI3SB_D018 (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): LI3SB_D018, type code %, sha256 `3680314cebef8591…`

~~~~text
52: PHASE LI3SB_D018 % 2 3 1 !
53: CONST LI3SB_D018 : LI : SB : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): LI3SB_D018, type code %, sha256 `69f9831503080727…`

~~~~text
59: PHASE LI3SB_D018 % 2 3 1 !
60: CONST LI3SB_D018 : LI : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase_

## LI3SB_D03 (Li–Sb)

- Id: `phase:li-sb:li3sb-d03`; status `assigned`
- Structure: BiF3 · D0_3 · cF16 · Fm-3m (225); type `st:d0-3-bif3-cf16`; tier A: standard phase name; confidence high
- Stoichiometry: Li 0.7500, Sb 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1160.49 K, x(Sb) 0.25–0.25
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:li3sb-d03)

Names (3): _corpus: _corpus:phase:li-sb:li3sb-d03  
_paper: _paper:10.1016/j.calphad.2017.01.005:αLi3Sb  
_tdb: _tdb:LiSb-17Zha.tdb:LI3SB_D03  


### TDB models of LI3SB_D03 (1): PHASE and CONSTITUENT statements as written

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): LI3SB_D03, type code %, sha256 `69f9831503080727…`

~~~~text
54: PHASE LI3SB_D03 % 2 3 1 !
55: CONST LI3SB_D03 : LI : SB : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Li–Sb)

- Id: `phase:li-sb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 441.35–2500 K, x(Sb) 0–1
- Literature: 197 values (197 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:li-sb:liquid)

Names (6): _corpus: _corpus:phase:li-sb:liquid  
_paper: _paper:10.1016/j.calphad.2017.01.005:Liquid, paper:10.1016/j.jallcom.2016.12.399:L, paper:10.1016/j.jallcom.2016.12.399:liquid  
_tdb: _tdb:LiSb-17Li.tdb:LIQUID, tdb:LiSb-17Zha.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[LiSb-17Li.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Li.tdb): LIQUID, type code %, sha256 `3680314cebef8591…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : LI LI3SB SB : !
~~~~

[LiSb-17Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/LiSb-17Zha.tdb): LIQUID, type code %, sha256 `69f9831503080727…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : LI LI3SB SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2016.12.399](https://doi.org/10.1016/j.jallcom.2016.12.399) D. Li, A. Beutl, H. Flandorfer, D.M. Cupid, The Li-Sb phase diagram part II: Calorimetry and thermodynamic assessment, Journal of Alloys and Compounds 701, 186-199 (2017).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2017.01.005](https://doi.org/10.1016/j.calphad.2017.01.005) Fan Zhang, Shuhong Liu, Jianchuan Wang, Yong Du, Lixian Sun, Experimental investigation and thermodynamic assessment of the Li-Sb system, Calphad 57, 28-36 (2017).  
_assessment that models this phase; reports values for this phase_

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
