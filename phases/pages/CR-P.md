# Cr–P phases

> Cr–P system: 8 phases (tier A 3, tier C 2, liquid 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-P.html · Markdown: https://data.orchid-project.org/phases/pages/CR-P.md

8 phases (tier A 3, tier C 2, liquid 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-P) · [full JSON](https://data.orchid-project.org/phases/systems/CR-P.json) · [Cr–P system page](https://data.orchid-project.org/systems/CR-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–P system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-p-bcc-a2); _phase:cr-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2238.74 K, x(P) 0–0.0001 | 0 | 2 |
| [M2P_C22](#phase-cr-p-c22-m2p); _phase:cr-p:c22-m2p_ | Fe2P · C22 · hP9 · P-62m (189) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1920.62 K, x(P) 0.33333–0.33333 | 0 | 2 |
| [M3P_D0E](#phase-cr-p-d0e-m3p); _phase:cr-p:d0e-m3p_ | Ni3P · D0_e · tI32 · I-4 (82) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 2 of 2 calculated diagram(s): 300–1784.51 K, x(P) 0.25–0.25 | 0 | 2 |
| [FCC_A1](#phase-cr-p-fcc-a1); _phase:cr-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cr-p-hcp-a3); _phase:cr-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cr-p-liquid); _phase:cr-p:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(P) 0–1 | 0 | 2 |
| [RED_P](#phase-cr-p-p-red); _phase:cr-p:p-red_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 300–915 K, x(P) 1–1 | 0 | 2 |
| [WHITE_P](#phase-cr-p-p-white); _phase:cr-p:p-white_ |  | needs_review | not stable in 2 calculated diagram(s) | 0 | 2 |

## BCC_A2 (Cr–P)

- Id: `phase:cr-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2238.74 K, x(P) 0–0.0001
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:bcc-a2)

Names (3): _corpus: _corpus:phase:cr-p:bcc-a2  
_tdb: _tdb:CrP-14Mie.tdb:BCC_A2, tdb:CrP-99Mie-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): BCC_A2, type code %B, sha256 `13fd479377120522…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR% P : VA : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): BCC_A2, type code %B, sha256 `372cae8e610e58d4…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## M2P_C22 (Cr–P)

- Id: `phase:cr-p:c22-m2p`; status `assigned`
- Structure: Fe2P · C22 · hP9 · P-62m (189); type `st:c22-fe2p-hp9`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M2P); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cr 0.6667, P 0.3333
- Stability: stable in 2 of 2 calculated diagram(s): 300–1920.62 K, x(P) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:c22-m2p)

Names (3): _corpus: _corpus:phase:cr-p:c22-m2p  
_tdb: _tdb:CrP-14Mie.tdb:M2P_C22, tdb:CrP-99Mie-LB.tdb:M2P_C22  


### TDB models of M2P_C22 (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): M2P_C22, type code %, sha256 `13fd479377120522…`

~~~~text
59: PHASE M2P_C22 % 2 2 1 !
60: CONST M2P_C22 : CR : P : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): M2P_C22, type code %, sha256 `372cae8e610e58d4…`

~~~~text
61: PHASE M2P_C22 % 2 2 1 !
62: CONST M2P_C22 : CR : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## M3P_D0E (Cr–P)

- Id: `phase:cr-p:d0e-m3p`; status `assigned`
- Structure: Ni3P · D0_e · tI32 · I-4 (82); type `st:d0-e-ni3p-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: DFT agrees: on-hull mp-aaaaalog and oqmd-4349, space group 82
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M3P); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Cr 0.7500, P 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 300–1784.51 K, x(P) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:d0e-m3p)

Names (5): _corpus: _corpus:phase:cr-p:d0e-m3p  
_mp: _mp:mp-aaaaalog  
_oqmd: _oqmd:oqmd-4349  
_tdb: _tdb:CrP-14Mie.tdb:M3P_D0E, tdb:CrP-99Mie-LB.tdb:M3P_D0E  


### TDB models of M3P_D0E (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): M3P_D0E, type code %, sha256 `13fd479377120522…`

~~~~text
53: PHASE M3P_D0E % 2 3 1 !
54: CONST M3P_D0E : CR : P : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): M3P_D0E, type code %, sha256 `372cae8e610e58d4…`

~~~~text
55: PHASE M3P_D0E % 2 3 1 !
56: CONST M3P_D0E : CR : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## FCC_A1 (Cr–P)

- Id: `phase:cr-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-p:fcc-a1  
_tdb: _tdb:CrP-14Mie.tdb:FCC_A1, tdb:CrP-99Mie-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): FCC_A1, type code %A, sha256 `13fd479377120522…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR P : VA : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): FCC_A1, type code %A, sha256 `372cae8e610e58d4…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR P : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## HCP_A3 (Cr–P)

- Id: `phase:cr-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cr 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:hcp-a3)

Names (3): _corpus: _corpus:phase:cr-p:hcp-a3  
_tdb: _tdb:CrP-14Mie.tdb:HCP_A3, tdb:CrP-99Mie-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): HCP_A3, type code %A, sha256 `13fd479377120522…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR : VA : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): HCP_A3, type code %A, sha256 `372cae8e610e58d4…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## LIQUID (Cr–P)

- Id: `phase:cr-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:liquid)

Names (3): _corpus: _corpus:phase:cr-p:liquid  
_tdb: _tdb:CrP-14Mie.tdb:LIQUID, tdb:CrP-99Mie-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): LIQUID, type code %, sha256 `13fd479377120522…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR P : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): LIQUID, type code %, sha256 `372cae8e610e58d4…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## RED_P (Cr–P)

- Id: `phase:cr-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–915 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:p-red)

Names (3): _corpus: _corpus:phase:cr-p:p-red  
_tdb: _tdb:CrP-14Mie.tdb:RED_P, tdb:CrP-99Mie-LB.tdb:RED_P  


### TDB models of RED_P (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): RED_P, type code %, sha256 `13fd479377120522…`

~~~~text
48: PHASE RED_P % 1 1 !
49: CONST RED_P : P : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): RED_P, type code %, sha256 `372cae8e610e58d4…`

~~~~text
50: PHASE RED_P % 1 1 !
51: CONST RED_P : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
_assessment that models this phase_

## WHITE_P (Cr–P)

- Id: `phase:cr-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-p:p-white)

Names (3): _corpus: _corpus:phase:cr-p:p-white  
_tdb: _tdb:CrP-14Mie.tdb:WHITE_P, tdb:CrP-99Mie-LB.tdb:WHITE_P  


### TDB models of WHITE_P (2): PHASE and CONSTITUENT statements as written

[CrP-14Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-14Mie.tdb): WHITE_P, type code %, sha256 `13fd479377120522…`

~~~~text
43: PHASE WHITE_P % 1 1 !
44: CONST WHITE_P : P : !
~~~~

[CrP-99Mie-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrP-99Mie-LB.tdb): WHITE_P, type code %, sha256 `372cae8e610e58d4…`

~~~~text
45: PHASE WHITE_P % 1 1 !
46: CONST WHITE_P : P : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0314-x](https://doi.org/10.1007/s11669-014-0314-x) J. Miettinen, G. Vassilev, J. Phase Equilib. Diffus., 35, 458-68(2014).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(99)00019-X](https://doi.org/10.1016/S0364-5916%2899%2900019-X) J. Miettinen, Calphad, 23, 191-99(1999).  
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
