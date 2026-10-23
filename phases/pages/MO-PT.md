# Mo–Pt phases

> Mo–Pt system: 8 phases (tier A 6, tier C 1, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-PT.html · Markdown: https://data.orchid-project.org/phases/pages/MO-PT.md

8 phases (tier A 6, tier C 1, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-PT) · [full JSON](https://data.orchid-project.org/phases/systems/MO-PT.json) · [Mo–Pt system page](https://data.orchid-project.org/systems/MO-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–Pt system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-pt-bcc-a2); _phase:mo-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2900.01 K, x(Pt) 0–0.14368 | 12 | 1 |
| [FCC_A1](#phase-mo-pt-fcc-a1); _phase:mo-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2296.51 K, x(Pt) 0.58668–1 | 6 | 1 |
| [HCP_A3](#phase-mo-pt-hcp-a3); _phase:mo-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1738.7–2450 K, x(Pt) 0.32857–0.58024 | 12 | 1 |
| [LIQUID](#phase-mo-pt-liquid); _phase:mo-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2041.5–4000 K, x(Pt) 0–1 | 6 | 1 |
| [MO6PT_A15](#phase-mo-pt-mo6pt-a15); _phase:mo-pt:mo6pt-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1550–2060 K, x(Pt) 0.18326–0.18901 | 18 | 1 |
| [MOPT_B19](#phase-mo-pt-mopt-b19); _phase:mo-pt:mopt-b19_ | AuCd · B19 · oP4 · Pmma (51) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2320 K, x(Pt) 0.36–0.5065 | 15 | 1 |
| [MOPT_D019](#phase-mo-pt-mopt-d019); _phase:mo-pt:mopt-d019_ | Ni3Sn · D0_19 · hP8 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1260–2430 K, x(Pt) 0.3318–0.52577 | 12 | 1 |
| [MOPT2](#phase-mo-pt-mopt2); _phase:mo-pt:mopt2_ | MoPt2 · oI6 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2210 K, x(Pt) 0.61354–0.99 | 31 | 1 |

## BCC_A2 (Mo–Pt)

- Id: `phase:mo-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2900.01 K, x(Pt) 0–0.14368
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:bcc-a2)

Names (3): _corpus: _corpus:phase:mo-pt:bcc-a2  
_paper: _paper:10.1016/j.calphad.2024.102665:A2  
_tdb: _tdb:MoPt-24Fio.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): BCC_A2, type code %B, sha256 `e0c202c305972988…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : MO% PT : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_

## FCC_A1 (Mo–Pt)

- Id: `phase:mo-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2296.51 K, x(Pt) 0.58668–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:fcc-a1)

Names (3): _corpus: _corpus:phase:mo-pt:fcc-a1  
_paper: _paper:10.1016/j.calphad.2024.102665:A1  
_tdb: _tdb:MoPt-24Fio.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): FCC_A1, type code %A, sha256 `e0c202c305972988…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : MO PT% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_

## HCP_A3 (Mo–Pt)

- Id: `phase:mo-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1738.7–2450 K, x(Pt) 0.32857–0.58024
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:hcp-a3)

Names (3): _corpus: _corpus:phase:mo-pt:hcp-a3  
_paper: _paper:10.1016/j.calphad.2024.102665:A3  
_tdb: _tdb:MoPt-24Fio.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): HCP_A3, type code %A, sha256 `e0c202c305972988…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : MO PT : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_

## LIQUID (Mo–Pt)

- Id: `phase:mo-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2041.5–4000 K, x(Pt) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:liquid)

Names (3): _corpus: _corpus:phase:mo-pt:liquid  
_paper: _paper:10.1016/j.calphad.2024.102665:L  
_tdb: _tdb:MoPt-24Fio.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): LIQUID, type code %, sha256 `e0c202c305972988…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : MO PT : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_

## MO6PT_A15 (Mo–Pt)

- Id: `phase:mo-pt:mo6pt-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoPt-24Fio.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1550–2060 K, x(Pt) 0.18326–0.18901
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:mo6pt-a15)

Names (3): _corpus: _corpus:phase:mo-pt:mo6pt-a15  
_paper: _paper:10.1016/j.calphad.2024.102665:A15  
_tdb: _tdb:MoPt-24Fio.tdb:MO6PT_A15  


### TDB models of MO6PT_A15 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): MO6PT_A15, type code %, sha256 `e0c202c305972988…`

~~~~text
46: PHASE MO6PT_A15 % 2 3 1 !
47: CONST MO6PT_A15 : MO% PT : MO PT% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_

## MOPT_B19 (Mo–Pt)

- Id: `phase:mo-pt:mopt-b19`; status `assigned`
- Structure: AuCd · B19 · oP4 · Pmma (51); type `st:b19-aucd-op4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoPt-24Fio.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2320 K, x(Pt) 0.36–0.5065
- Literature: 15 values (15 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:mopt-b19)

Names (3): _corpus: _corpus:phase:mo-pt:mopt-b19  
_paper: _paper:10.1016/j.calphad.2024.102665:B19  
_tdb: _tdb:MoPt-24Fio.tdb:MOPT_B19  


### TDB models of MOPT_B19 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): MOPT_B19, type code %, sha256 `e0c202c305972988…`

~~~~text
56: PHASE MOPT_B19 % 2 1 1 !
57: CONST MOPT_B19 : MO% PT : MO PT% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.50.5962](https://doi.org/10.1103/physrevb.50.5962) Z. W. Lu, Barry M. Klein, Theoretical studies of the stability of ordered\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="italic">A\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>8\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>\<i>B\</i>compounds, Phys. Rev. B 50, 5962-5970 (1994).  
_cited as the source of values for this phase_

## MOPT_D019 (Mo–Pt)

- Id: `phase:mo-pt:mopt-d019`; status `assigned`
- Structure: Ni3Sn · D0_19 · hP8 · P6_3/mmc (194); type `st:d0-19-ni3sn-hp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in MoPt-24Fio.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 1260–2430 K, x(Pt) 0.3318–0.52577
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:mopt-d019)

Names (3): _corpus: _corpus:phase:mo-pt:mopt-d019  
_paper: _paper:10.1016/j.calphad.2024.102665:D019  
_tdb: _tdb:MoPt-24Fio.tdb:MOPT_D019  


### TDB models of MOPT_D019 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): MOPT_D019, type code %, sha256 `e0c202c305972988…`

~~~~text
51: PHASE MOPT_D019 % 2 3 1 !
52: CONST MOPT_D019 : MO% PT : MO PT% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_

## MOPT2 (Mo–Pt)

- Id: `phase:mo-pt:mopt2`; status `assigned`
- Structure: MoPt2 · oI6 · Immm (71); type `st:mopt2-oi6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–2210 K, x(Pt) 0.61354–0.99
- Literature: 31 values (31 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-pt:mopt2)

Names (3): _corpus: _corpus:phase:mo-pt:mopt2  
_paper: _paper:10.1016/j.calphad.2024.102665:MoPt2  
_tdb: _tdb:MoPt-24Fio.tdb:MOPT2  


### TDB models of MOPT2 (1): PHASE and CONSTITUENT statements as written

[MoPt-24Fio.tdb](https://orchid-project.org/data/databases/sgte-binary/MoPt-24Fio.tdb): MOPT2, type code %, sha256 `e0c202c305972988…`

~~~~text
61: PHASE MOPT2 % 2 2 1 !
62: CONST MOPT2 : MO PT% : MO% PT : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2024.102665](https://doi.org/10.1016/j.calphad.2024.102665) J.-M. Fiorani, M. Siblani, J.-M. Joubert, C. Barreteau, J.-C. Crivello, N. David et al., Thermodynamic modeling of the Mo–Pt system based on the NACEF approach, Calphad 84, 102665 (2024).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02881200](https://doi.org/10.1007/bf02881200) L. Brewer, R.H. Lamoreaux, Bull. Alloy Phase Diagrams, 1 (1980) 89-91.  
_cited as the source of values for this phase_
- [doi:10.1016/j.calphad.2005.01.002](https://doi.org/10.1016/j.calphad.2005.01.002) Stefano Curtarolo A, Accuracy of ab initio methods in predicting the crystal structures of metals: A review of 80 binary alloys, Calphad (2005).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.50.5962](https://doi.org/10.1103/physrevb.50.5962) Z. W. Lu, Barry M. Klein, Theoretical studies of the stability of ordered\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mi mathvariant="italic">A\</mml:mi>\</mml:mrow>\<mml:mrow>\<mml:mn>8\</mml:mn>\</mml:mrow>\</mml:msub>\</mml:mrow>\</mml:math>\<i>B\</i>compounds, Phys. Rev. B 50, 5962-5970 (1994).  
_cited as the source of values for this phase_
- [doi:10.1103/physrevb.77.193111](https://doi.org/10.1103/physrevb.77.193111) M. Stojković, V. Koteski, J. Belošević-Čavor, B. Cekić, D. Stojić, V. Ivanovski, Structure and electronic properties of\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mtext>Mo\</mml:mtext>\</mml:mrow>\<mml:mn>3\</mml:mn>\</mml:msub>\<mml:mtext>Pt\</mml:mtext>\</mml:mrow>\</mml:math>,\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mtext>MoPt\</mml:mtext>\</mml:mrow>\<mml:mn>2\</mml:mn>\</mml:msub>\</mml:mrow>\</mml:math>, and\<mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" display="inline">\<mml:mrow>\<mml:msub>\<mml:mrow>\<mml:mtext>MoPt\</mml:mtext>\</mml:mrow>\<mml:mn>3\</mml:mn>\</mml:msub>\</mml:mrow>\</mml:math>: First-principles calculations, Phys. Rev. B 77 (2008).  
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
