# Pb–U phases

> Pb–U system: 8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-U.html · Markdown: https://data.orchid-project.org/phases/pages/PB-U.md

8 phases (tier A 5, tier C 1, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-U) · [full JSON](https://data.orchid-project.org/phases/systems/PB-U.json) · [Pb–U system page](https://data.orchid-project.org/systems/PB-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–U system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-pb-u-a20-orthorhombic); _phase:pb-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–948.3 K, x(U) 0.99909–1 | 2 | 2 |
| [BCC_A2](#phase-pb-u-bcc-a2); _phase:pb-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1015.66–3999.24 K, x(U) 0.96035–1 | 4 | 2 |
| [FCC_A1](#phase-pb-u-fcc-a1); _phase:pb-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–600.61 K, x(U) 0–0 | 2 | 2 |
| [HCP_A3](#phase-pb-u-hcp-a3); _phase:pb-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-pb-u-liquid); _phase:pb-u:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 600.61–4000 K, x(U) 0–1 | 11 | 2 |
| [PB3U_L12](#phase-pb-u-pb3u-l12); _phase:pb-u:pb3u-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1490.37 K, x(U) 0.25–0.25 | 6 | 2 |
| [PBU](#phase-pb-u-pbu); _phase:pb-u:pbu_ | PbU · tI8 · I4_1/amd (141) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1557.76 K, x(U) 0.5–0.5 | 10 | 2 |
| [TETRAGONAL_U](#phase-pb-u-u-tetragonal); _phase:pb-u:u-tetragonal_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 923.3–1052.18 K, x(U) 0.99207–1 | 4 | 2 |

## ORTHORHOMBIC_A20 (Pb–U)

- Id: `phase:pb-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–948.3 K, x(U) 0.99909–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:a20-orthorhombic)

Names (5): _corpus: _corpus:phase:pb-u:a20-orthorhombic, corpus:phase:pb-u:orthorhombic-a20  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:αU  
_tdb: _tdb:PbU-10Li.tdb:ORTHORHOMBIC_A20, tdb:PbU-21Aga.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): ORTHORHOMBIC_A20, type code %, sha256 `d7e91ddbf663d2cb…`

~~~~text
41: PHASE ORTHORHOMBIC_A20 % 1 1 !
42: CONST ORTHORHOMBIC_A20 : PB U% : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): ORTHORHOMBIC_A20, type code %, sha256 `acb4f2362054d048…`

~~~~text
42: PHASE ORTHORHOMBIC_A20 % 1 1 !
43: CONST ORTHORHOMBIC_A20 : PB U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## BCC_A2 (Pb–U)

- Id: `phase:pb-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1015.66–3999.24 K, x(U) 0.96035–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:bcc-a2)

Names (4): _corpus: _corpus:phase:pb-u:bcc-a2  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:γU  
_tdb: _tdb:PbU-10Li.tdb:BCC_A2, tdb:PbU-21Aga.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): BCC_A2, type code %B, sha256 `d7e91ddbf663d2cb…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : PB U% : VA : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): BCC_A2, type code %B, sha256 `acb4f2362054d048…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PB U% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## FCC_A1 (Pb–U)

- Id: `phase:pb-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–600.61 K, x(U) 0–0
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:fcc-a1)

Names (4): _corpus: _corpus:phase:pb-u:fcc-a1  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:(Pb)  
_tdb: _tdb:PbU-10Li.tdb:FCC_A1, tdb:PbU-21Aga.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): FCC_A1, type code %A, sha256 `d7e91ddbf663d2cb…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : PB% U : VA : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): FCC_A1, type code %A, sha256 `acb4f2362054d048…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PB% U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## HCP_A3 (Pb–U)

- Id: `phase:pb-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:hcp-a3)

Names (3): _corpus: _corpus:phase:pb-u:hcp-a3  
_tdb: _tdb:PbU-10Li.tdb:HCP_A3, tdb:PbU-21Aga.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): HCP_A3, type code %A, sha256 `d7e91ddbf663d2cb…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : PB U : VA: !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): HCP_A3, type code %A, sha256 `acb4f2362054d048…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : PB U : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## LIQUID (Pb–U)

- Id: `phase:pb-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 600.61–4000 K, x(U) 0–1
- Literature: 11 values (11 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:liquid)

Names (5): _corpus: _corpus:phase:pb-u:liquid  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:L, paper:10.1016/j.jnucmat.2010.02.002:L2  
_tdb: _tdb:PbU-10Li.tdb:LIQUID, tdb:PbU-21Aga.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): LIQUID, type code %, sha256 `d7e91ddbf663d2cb…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : PB U : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): LIQUID, type code %, sha256 `acb4f2362054d048…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PB U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## PB3U_L12 (Pb–U)

- Id: `phase:pb-u:pb3u-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.7500, U 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1490.37 K, x(U) 0.25–0.25
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:pb3u-l12)

Names (4): _corpus: _corpus:phase:pb-u:pb3u-l12  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:Pb3U  
_tdb: _tdb:PbU-10Li.tdb:PB3U_L12, tdb:PbU-21Aga.tdb:PB3U_L12  


### TDB models of PB3U_L12 (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): PB3U_L12, type code %, sha256 `d7e91ddbf663d2cb…`

~~~~text
51: PHASE PB3U_L12 % 2 3 1 !
52: CONST PB3U_L12 : PB : U : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): PB3U_L12, type code %, sha256 `acb4f2362054d048…`

~~~~text
52: PHASE PB3U_L12 % 2 3 1 !
53: CONST PB3U_L12 : PB : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## PBU (Pb–U)

- Id: `phase:pb-u:pbu`; status `assigned`
- Structure: PbU · tI8 · I4_1/amd (141); type `st:pbu-ti8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pb 0.5000, U 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1557.76 K, x(U) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:pbu)

Names (5): _corpus: _corpus:phase:pb-u:pbu  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:PbU, paper:10.1016/j.jnucmat.2010.02.002:Pb–U  
_tdb: _tdb:PbU-10Li.tdb:PBU, tdb:PbU-21Aga.tdb:PBU  


### TDB models of PBU (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): PBU, type code %, sha256 `d7e91ddbf663d2cb…`

~~~~text
56: PHASE PBU % 2 1 1 !
57: CONST PBU : PB : U : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): PBU, type code %, sha256 `acb4f2362054d048…`

~~~~text
57: PHASE PBU % 2 1 1 !
58: CONST PBU : PB : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## TETRAGONAL_U (Pb–U)

- Id: `phase:pb-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — PbU-10Li.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — PbU-21Aga.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 2 of 2 calculated diagram(s): 923.3–1052.18 K, x(U) 0.99207–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-u:u-tetragonal)

Names (5): _corpus: _corpus:phase:pb-u:u-tetragonal, corpus:phase:pb-u:tetragonal-u  
_paper: _paper:10.1016/j.jnucmat.2010.02.002:βU  
_tdb: _tdb:PbU-10Li.tdb:TETRAGONAL_U, tdb:PbU-21Aga.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (2): PHASE and CONSTITUENT statements as written

[PbU-10Li.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-10Li.tdb): TETRAGONAL_U, type code %, sha256 `d7e91ddbf663d2cb…`

~~~~text
46: PHASE TETRAGONAL_U % 1 1 !
47: CONST TETRAGONAL_U : PB U% : !
~~~~

[PbU-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/PbU-21Aga.tdb): TETRAGONAL_U, type code %, sha256 `acb4f2362054d048…`

~~~~text
47: PHASE TETRAGONAL_U % 1 1 !
48: CONST TETRAGONAL_U : PB U% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jnucmat.2010.02.002](https://doi.org/10.1016/j.jnucmat.2010.02.002) Z.S. Li, X.J. Liu, C.P. Wang, Thermodynamic modeling of the Pb–U and Pb–Pu systems, Journal of Nuclear Materials 403, 1-6 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
