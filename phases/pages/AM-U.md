# Am–U phases

> Am–U system: 7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AM-U.html · Markdown: https://data.orchid-project.org/phases/pages/AM-U.md

7 phases (tier A 5, liquid 1, needs_review 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AM-U) · [full JSON](https://data.orchid-project.org/phases/systems/AM-U.json) · [Am–U system page](https://data.orchid-project.org/systems/AM-U.html) · [Markdown](https://data.orchid-project.org/phases/pages/AM-U.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Am–U system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A20](#phase-am-u-a20-orthorhombic); _phase:am-u:a20-orthorhombic_ | alpha-U · A20 · oC4 · Cmcm (63) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–942.02 K, x(U) 0.9991–1 | 0 | 3 |
| [BCC_A2](#phase-am-u-bcc-a2); _phase:am-u:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 1009.45–2104.33 K, x(U) 0–1 | 0 | 3 |
| [DHCP](#phase-am-u-dhcp-a3); _phase:am-u:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1364.47 K, x(U) 0–0.00178 | 0 | 3 |
| [FCC_A1](#phase-am-u-fcc-a1); _phase:am-u:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 902.68–1400 K, x(U) 0–0.41 | 0 | 3 |
| [HCP_A3](#phase-am-u-hcp-a3); _phase:am-u:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-am-u-liquid); _phase:am-u:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1354.65–4000 K, x(U) 0–1 | 0 | 3 |
| [TETRAGONAL_U](#phase-am-u-u-tetragonal); _phase:am-u:u-tetragonal_ |  | needs_review | stable in 3 of 3 calculated diagram(s): 942.02–1406.31 K, x(U) 0.99816–1 | 0 | 3 |

## ORTHORHOMBIC_A20 (Am–U)

- Id: `phase:am-u:a20-orthorhombic`; status `assigned`
- Structure: alpha-U · A20 · oC4 · Cmcm (63); type `st:a20-alpha-u-oc4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–942.02 K, x(U) 0.9991–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:a20-orthorhombic)

Names (4): _corpus: _corpus:phase:am-u:a20-orthorhombic  
_tdb: _tdb:AmU-10Kur.tdb:ORTHORHOMBIC_A20, tdb:AmU-15Per.tdb:ORTHORHOMBIC_A20, tdb:AmU-93Oga.tdb:ORTHORHOMBIC_A20  


### TDB models of ORTHORHOMBIC_A20 (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): ORTHORHOMBIC_A20, type code %, sha256 `d0aa112b9c5e85f9…`

~~~~text
45: PHASE ORTHORHOMBIC_A20 % 1 1 !
46: CONST ORTHORHOMBIC_A20 : AM U% : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): ORTHORHOMBIC_A20, type code %, sha256 `b45bb49962d3127b…`

~~~~text
46: PHASE ORTHORHOMBIC_A20 % 1 1 !
47: CONST ORTHORHOMBIC_A20 : U : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): ORTHORHOMBIC_A20, type code %, sha256 `a402906c7e81f20b…`

~~~~text
49: PHASE ORTHORHOMBIC_A20 % 1 1 !
50: CONST ORTHORHOMBIC_A20 : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_

## BCC_A2 (Am–U)

- Id: `phase:am-u:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1009.45–2104.33 K, x(U) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:bcc-a2)

Names (4): _corpus: _corpus:phase:am-u:bcc-a2  
_tdb: _tdb:AmU-10Kur.tdb:BCC_A2, tdb:AmU-15Per.tdb:BCC_A2, tdb:AmU-93Oga.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): BCC_A2, type code %B, sha256 `d0aa112b9c5e85f9…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AM% U% : VA : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): BCC_A2, type code %B, sha256 `b45bb49962d3127b…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : AM% U% : VA : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): BCC_A2, type code %B, sha256 `a402906c7e81f20b…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : AM% U% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_

## DHCP (Am–U)

- Id: `phase:am-u:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1364.47 K, x(U) 0–0.00178
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:dhcp-a3)

Names (4): _corpus: _corpus:phase:am-u:dhcp-a3  
_tdb: _tdb:AmU-10Kur.tdb:DHCP, tdb:AmU-15Per.tdb:DHCP, tdb:AmU-93Oga.tdb:DHCP  


### TDB models of DHCP (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): DHCP, type code %, sha256 `d0aa112b9c5e85f9…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : AM% U : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): DHCP, type code %, sha256 `b45bb49962d3127b…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : AM : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): DHCP, type code %, sha256 `a402906c7e81f20b…`

~~~~text
44: PHASE DHCP % 1 1 !
45: CONST DHCP : AM : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_

## FCC_A1 (Am–U)

- Id: `phase:am-u:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 902.68–1400 K, x(U) 0–0.41
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:fcc-a1)

Names (4): _corpus: _corpus:phase:am-u:fcc-a1  
_tdb: _tdb:AmU-10Kur.tdb:FCC_A1, tdb:AmU-15Per.tdb:FCC_A1, tdb:AmU-93Oga.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): FCC_A1, type code %A, sha256 `d0aa112b9c5e85f9…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AM% U : VA : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): FCC_A1, type code %A, sha256 `b45bb49962d3127b…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : AM% U : VA : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): FCC_A1, type code %A, sha256 `a402906c7e81f20b…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : AM% U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_

## HCP_A3 (Am–U)

- Id: `phase:am-u:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:hcp-a3)

Names (4): _corpus: _corpus:phase:am-u:hcp-a3  
_tdb: _tdb:AmU-10Kur.tdb:HCP_A3, tdb:AmU-15Per.tdb:HCP_A3, tdb:AmU-93Oga.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): HCP_A3, type code %A, sha256 `d0aa112b9c5e85f9…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AM U : VA : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): HCP_A3, type code %A, sha256 `b45bb49962d3127b…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : AM U : VA : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): HCP_A3, type code %A, sha256 `a402906c7e81f20b…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : AM U : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_

## LIQUID (Am–U)

- Id: `phase:am-u:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1354.65–4000 K, x(U) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:liquid)

Names (4): _corpus: _corpus:phase:am-u:liquid  
_tdb: _tdb:AmU-10Kur.tdb:LIQUID, tdb:AmU-15Per.tdb:LIQUID, tdb:AmU-93Oga.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): LIQUID, type code %, sha256 `d0aa112b9c5e85f9…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AM U : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): LIQUID, type code %, sha256 `b45bb49962d3127b…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : AM U : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): LIQUID, type code %, sha256 `a402906c7e81f20b…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : AM U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
_assessment that models this phase_

## TETRAGONAL_U (Am–U)

- Id: `phase:am-u:u-tetragonal`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:TETRAGONAL; no_structure_token
- Candidate (sgte_mmc2): beta-U · A_b · tP30 · P4_2/mnm (136) — Hallstedt 2025 mmc2 row for TETRAGONAL_U: beta-U
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — AmU-10Kur.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — AmU-15Per.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Candidate (tdb_comment): beta-U · tP30 · P4_2/mnm, SB: A_b — AmU-93Oga.tdb: 'Prototype beta-U (tP30, P4_2/mnm, SB: A_b)'
- Stability: stable in 3 of 3 calculated diagram(s): 942.02–1406.31 K, x(U) 0.99816–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-u:u-tetragonal)

Names (4): _corpus: _corpus:phase:am-u:u-tetragonal  
_tdb: _tdb:AmU-10Kur.tdb:TETRAGONAL_U, tdb:AmU-15Per.tdb:TETRAGONAL_U, tdb:AmU-93Oga.tdb:TETRAGONAL_U  


### TDB models of TETRAGONAL_U (3): PHASE and CONSTITUENT statements as written

[AmU-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-10Kur.tdb): TETRAGONAL_U, type code %, sha256 `d0aa112b9c5e85f9…`

~~~~text
50: PHASE TETRAGONAL_U % 1 1 !
51: CONST TETRAGONAL_U : AM U% : !
~~~~

[AmU-15Per.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-15Per.tdb): TETRAGONAL_U, type code %, sha256 `b45bb49962d3127b…`

~~~~text
51: PHASE TETRAGONAL_U % 1 1 !
52: CONST TETRAGONAL_U : U : !
~~~~

[AmU-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmU-93Oga.tdb): TETRAGONAL_U, type code %, sha256 `a402906c7e81f20b…`

~~~~text
54: PHASE TETRAGONAL_U % 1 1 !
55: CONST TETRAGONAL_U : U : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_
- [doi:10.1016/j.jnucmat.2014.12.101](https://doi.org/10.1016/j.jnucmat.2014.12.101) A. Perron, P.E.A. Turchi, A. Landa, P. Söderlind, B. Ravat, B. Oudot et al., The Pu–U–Am system: An ab initio informed CALPHAD thermodynamic study, Journal of Nuclear Materials 458, 425-441 (2015).  
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
