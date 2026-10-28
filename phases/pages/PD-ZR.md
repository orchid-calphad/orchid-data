# Pd–Zr phases

> Pd–Zr system: 11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 11 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PD-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/PD-ZR.md

11 phases (tier A 6, tier C 2, liquid 1, needs_review 2); 11 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PD-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/PD-ZR.json) · [Pd–Zr system page](https://data.orchid-project.org/systems/PD-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/PD-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pd–Zr system (11)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pd-zr-bcc-a2); _phase:pd-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1033.15–3999.1 K, x(Zr) 0.88596–1 | 0 | 1 |
| [FCC_A1](#phase-pd-zr-fcc-a1); _phase:pd-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1852.81 K, x(Zr) 0–0.13582 | 0 | 1 |
| [HCP_A3](#phase-pd-zr-hcp-a3); _phase:pd-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1138.99 K, x(Zr) 0.9925–1 | 0 | 1 |
| [LIQUID](#phase-pd-zr-liquid); _phase:pd-zr:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1342.47–4000 K, x(Zr) 0–1 | 0 | 1 |
| [PD11ZR9](#phase-pd-zr-pd11zr9); _phase:pd-zr:pd11zr9_ | Ni11Zr9 · tP44 · P4/m (83) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1260 K, x(Zr) 0.45–0.45 | 0 | 1 |
| [PD3ZR_D024](#phase-pd-zr-pd3zr-d024); _phase:pd-zr:pd3zr-d024_ | Ni3Ti · D0_24 · hP16 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2162.55 K, x(Zr) 0.18311–0.27053 | 0 | 1 |
| [PD4ZR3](#phase-pd-zr-pd4zr3); _phase:pd-zr:pd4zr3_ | Pd4Pu3 · hR14 · R-3 (148) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1673.01 K, x(Zr) 0.42857–0.42857 | 0 | 1 |
| [PDZR_ALPHA](#phase-pd-zr-pdzr-alpha); _phase:pd-zr:pdzr-alpha_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–469.39 K, x(Zr) 0.5–0.5 | 0 | 1 |
| [PDZR_B2](#phase-pd-zr-pdzr-b2); _phase:pd-zr:pdzr-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1872.83 K, x(Zr) 0.46881–0.5944 | 0 | 1 |
| [PDZR_B33](#phase-pd-zr-pdzr-b33); _phase:pd-zr:pdzr-b33_ | CrB · B33 · oC8 · Cmcm (63) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 469.39–903.06 K, x(Zr) 0.5–0.5 | 0 | 1 |
| [PDZRM](#phase-pd-zr-pdzrm); _phase:pd-zr:pdzrm_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1883.16 K, x(Zr) 0.33334–0.66667 | 0 | 1 |

## BCC_A2 (Pd–Zr)

- Id: `phase:pd-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1033.15–3999.1 K, x(Zr) 0.88596–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:bcc-a2)

Names (2): _corpus: _corpus:phase:pd-zr:bcc-a2  
_tdb: _tdb:PdZr-03Du.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): BCC_A2, type code %B, sha256 `3c13287a6b36d5e1…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : PD ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## FCC_A1 (Pd–Zr)

- Id: `phase:pd-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1852.81 K, x(Zr) 0–0.13582
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:fcc-a1)

Names (2): _corpus: _corpus:phase:pd-zr:fcc-a1  
_tdb: _tdb:PdZr-03Du.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): FCC_A1, type code %A, sha256 `3c13287a6b36d5e1…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : PD% ZR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## HCP_A3 (Pd–Zr)

- Id: `phase:pd-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1138.99 K, x(Zr) 0.9925–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:hcp-a3)

Names (2): _corpus: _corpus:phase:pd-zr:hcp-a3  
_tdb: _tdb:PdZr-03Du.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): HCP_A3, type code %A, sha256 `3c13287a6b36d5e1…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : PD ZR% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## LIQUID (Pd–Zr)

- Id: `phase:pd-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1342.47–4000 K, x(Zr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:liquid)

Names (2): _corpus: _corpus:phase:pd-zr:liquid  
_tdb: _tdb:PdZr-03Du.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): LIQUID, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : PD ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PD11ZR9 (Pd–Zr)

- Id: `phase:pd-zr:pd11zr9`; status `assigned`
- Structure: Ni11Zr9 · tP44 · P4/m (83); type `st:ni11zr9-tp44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pd 0.5500, Zr 0.4500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1260 K, x(Zr) 0.45–0.45
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pd11zr9)

Names (2): _corpus: _corpus:phase:pd-zr:pd11zr9  
_tdb: _tdb:PdZr-03Du.tdb:PD11ZR9  


### TDB models of PD11ZR9 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PD11ZR9, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
66: PHASE PD11ZR9 % 2 11 9 !
67: CONST PD11ZR9 : PD : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PD3ZR_D024 (Pd–Zr)

- Id: `phase:pd-zr:pd3zr-d024`; status `assigned`
- Structure: Ni3Ti · D0_24 · hP16 · P6_3/mmc (194); type `st:d0-24-ni3ti-hp16`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PdZr-03Du.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2162.55 K, x(Zr) 0.18311–0.27053
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pd3zr-d024)

Names (2): _corpus: _corpus:phase:pd-zr:pd3zr-d024  
_tdb: _tdb:PdZr-03Du.tdb:PD3ZR_D024  


### TDB models of PD3ZR_D024 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PD3ZR_D024, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
49: PHASE PD3ZR_D024 % 2 3 1 !
50: CONST PD3ZR_D024 : PD% ZR : PD ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PD4ZR3 (Pd–Zr)

- Id: `phase:pd-zr:pd4zr3`; status `assigned`
- Structure: Pd4Pu3 · hR14 · R-3 (148); type `st:pd4pu3-hr14`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pd 0.5714, Zr 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 300–1673.01 K, x(Zr) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pd4zr3)

Names (2): _corpus: _corpus:phase:pd-zr:pd4zr3  
_tdb: _tdb:PdZr-03Du.tdb:PD4ZR3  


### TDB models of PD4ZR3 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PD4ZR3, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
61: PHASE PD4ZR3 % 2 4 3 !
62: CONST PD4ZR3 : PD : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PDZR_ALPHA (Pd–Zr)

- Id: `phase:pd-zr:pdzr-alpha`; status `needs_review`
- No structure assigned. Why: no_structure_token; polymorph_family:other phases of this system have the same composition
- Candidate (dft_mp): Cmcm (63) — on-hull MP ZrPd at x(ZR)=0.5000
- Candidate (dft_oqmd): P21/m (11) — on-hull OQMD Pd1 Zr1 at x(ZR)=0.5000
- Candidate (sgte_mmc2): (PdZr-alpha) — Hallstedt 2025 mmc2 row for PDZR_ALPHA: PdZr-alpha
- Stoichiometry: Pd 0.5000, Zr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–469.39 K, x(Zr) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pdzr-alpha)

Names (2): _corpus: _corpus:phase:pd-zr:pdzr-alpha  
_tdb: _tdb:PdZr-03Du.tdb:PDZR_ALPHA  


### TDB models of PDZR_ALPHA (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PDZR_ALPHA, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
71: PHASE PDZR_ALPHA % 2 1 1 !
72: CONST PDZR_ALPHA : PD : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PDZR_B2 (Pd–Zr)

- Id: `phase:pd-zr:pdzr-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1872.83 K, x(Zr) 0.46881–0.5944
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pdzr-b2)

Names (2): _corpus: _corpus:phase:pd-zr:pdzr-b2  
_tdb: _tdb:PdZr-03Du.tdb:PDZR_B2  


### TDB models of PDZR_B2 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PDZR_B2, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
81: PHASE PDZR_B2 % 2 1 1 !
82: CONST PDZR_B2 : PD% VA : PD ZR% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PDZR_B33 (Pd–Zr)

- Id: `phase:pd-zr:pdzr-b33`; status `assigned`
- Structure: CrB · B33 · oC8 · Cmcm (63); type `st:b33-crb-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Pd 0.5000, Zr 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 469.39–903.06 K, x(Zr) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pdzr-b33)

Names (2): _corpus: _corpus:phase:pd-zr:pdzr-b33  
_tdb: _tdb:PdZr-03Du.tdb:PDZR_B33  


### TDB models of PDZR_B33 (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PDZR_B33, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
76: PHASE PDZR_B33 % 2 1 1 !
77: CONST PDZR_B33 : PD : ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
_assessment that models this phase_

## PDZRM (Pd–Zr)

- Id: `phase:pd-zr:pdzrm`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:PDZRM; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (dft_mp): I4/mmm (139) — on-hull MP Zr2Pd at x(ZR)=0.6667
- Candidate (dft_mp): Cmcm (63) — on-hull MP ZrPd at x(ZR)=0.5000
- Candidate (dft_oqmd): P21/m (11) — on-hull OQMD Pd1 Zr1 at x(ZR)=0.5000
- Candidate (dft_oqmd): P4mm (99) — on-hull OQMD Pd1 Zr2 at x(ZR)=0.6667
- Candidate (dft_oqmd): Cmca (64) — on-hull OQMD Pd10 Zr7 at x(ZR)=0.4118
- Candidate (sgte_mmc2): MoSi2 · C11_b · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for PDZRM: Pd2Zr (see also CuZr2)
- Candidate (sgte_mmc2): CuZr2 · tI6 · I4/mmm (139) — Hallstedt 2025 mmc2 row for PDZRM: PdZr2 (see also MoSi2)
- Candidate (tdb_comment):  — PdZr-03Du.tdb: 'Prototype MoSi2, both Pd2Zr and PdZr2'
- Stability: stable in 1 of 1 calculated diagram(s): 300–1883.16 K, x(Zr) 0.33334–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pd-zr:pdzrm)

Names (2): _corpus: _corpus:phase:pd-zr:pdzrm  
_tdb: _tdb:PdZr-03Du.tdb:PDZRM  


### TDB models of PDZRM (1): PHASE and CONSTITUENT statements as written

[PdZr-03Du.tdb](https://orchid-project.org/data/databases/sgte-binary/PdZr-03Du.tdb): PDZRM, type code %, sha256 `3c13287a6b36d5e1…`

~~~~text
56: PHASE PDZRM % 3 1 1 1 !
57: CONST PDZRM : PD : ZR : PD ZR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.030864](https://doi.org/10.3139/146.030864) Z. Du, Z. Metallkd., 94, 864-70(2003).  
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
