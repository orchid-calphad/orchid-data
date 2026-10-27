# Co–Re phases

> Co–Re system: 6 phases (tier A 4, liquid 1, unresolved_no_candidates 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-RE.html · Markdown: https://data.orchid-project.org/phases/pages/CO-RE.md

6 phases (tier A 4, liquid 1, unresolved_no_candidates 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-RE) · [full JSON](https://data.orchid-project.org/phases/systems/CO-RE.json) · [Co–Re system page](https://data.orchid-project.org/systems/CO-RE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-RE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Re system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-re-bcc-a2); _phase:co-re:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [SIGMA_D8B](#phase-co-re-d8b-sigma); _phase:co-re:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [DIS_SIG](#phase-co-re-dis-sig); _phase:co-re:dis-sig_ |  | unresolved_no_candidates | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-co-re-fcc-a1); _phase:co-re:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 383.75–1887.35 K, x(Re) 0–0.19403 | 0 | 4 |
| [HCP_A3](#phase-co-re-hcp-a3); _phase:co-re:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 299.59–3999.25 K, x(Re) 0–1 | 0 | 4 |
| [LIQUID](#phase-co-re-liquid); _phase:co-re:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 1760.99–4000 K, x(Re) 0–1 | 0 | 4 |

## BCC_A2 (Co–Re)

- Id: `phase:co-re:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-re:bcc-a2)

Names (5): _corpus: _corpus:phase:co-re:bcc-a2  
_tdb: _tdb:CoRe-14Liu.tdb:BCC_A2, tdb:CoRe-18Guo.tdb:BCC_A2, tdb:CoRe-24Per.tdb:BCC_A2, tdb:CoRe-24Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CoRe-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-14Liu.tdb): BCC_A2, type code %B, sha256 `9022ff2a486be381…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CO RE : VA : !
~~~~

[CoRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-18Guo.tdb): BCC_A2, type code %B, sha256 `bcd125e1e2f5a714…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CO RE : VA : !
~~~~

[CoRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Per.tdb): BCC_A2, type code %B, sha256 `88a3581d7a2f62a0…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO RE : VA : !
~~~~

[CoRe-24Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Shi.tdb): BCC_A2, type code %B, sha256 `abf52118bf771eb7…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : CO RE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.12.003](https://doi.org/10.1016/j.calphad.2013.12.003) X.J. Liu, J.Y. Lin, Y. Lu, Y.H. Guo, C.P. Wang, Calphad, 45, 138-44(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102688](https://doi.org/10.1016/j.calphad.2024.102688) Z. Shi, G. Shang, X.-G. Lu, Calphad, 85, 102688(2024).  
_assessment that models this phase_

## SIGMA_D8B (Co–Re)

- Id: `phase:co-re:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoRe-24Per.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-re:d8b-sigma)

Names (2): _corpus: _corpus:phase:co-re:d8b-sigma  
_tdb: _tdb:CoRe-24Per.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (1): PHASE and CONSTITUENT statements as written

[CoRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Per.tdb): SIGMA_D8B, type code %AS, sha256 `88a3581d7a2f62a0…`

~~~~text
48: PHASE SIGMA_D8B %AS 5 2 4 8 8 8 !
49: CONST SIGMA_D8B : CO RE : CO RE : CO RE : CO RE : CO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_

## DIS_SIG (Co–Re)

- Id: `phase:co-re:dis-sig`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:DIS,SIG; no_structure_token
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-re:dis-sig)

Names (2): _corpus: _corpus:phase:co-re:dis-sig  
_tdb: _tdb:CoRe-24Per.tdb:DIS_SIG  


### TDB models of DIS_SIG (1): PHASE and CONSTITUENT statements as written

[CoRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Per.tdb): DIS_SIG, type code %A, sha256 `88a3581d7a2f62a0…`

~~~~text
43: PHASE DIS_SIG %A 1 1 !
44: CONST DIS_SIG : CO RE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_

## FCC_A1 (Co–Re)

- Id: `phase:co-re:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 383.75–1887.35 K, x(Re) 0–0.19403
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-re:fcc-a1)

Names (5): _corpus: _corpus:phase:co-re:fcc-a1  
_tdb: _tdb:CoRe-14Liu.tdb:FCC_A1, tdb:CoRe-18Guo.tdb:FCC_A1, tdb:CoRe-24Per.tdb:FCC_A1, tdb:CoRe-24Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CoRe-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-14Liu.tdb): FCC_A1, type code %A, sha256 `9022ff2a486be381…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CO% RE : VA : !
~~~~

[CoRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-18Guo.tdb): FCC_A1, type code %A, sha256 `bcd125e1e2f5a714…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CO% RE : VA : !
~~~~

[CoRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Per.tdb): FCC_A1, type code %A, sha256 `88a3581d7a2f62a0…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% RE : VA : !
~~~~

[CoRe-24Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Shi.tdb): FCC_A1, type code %A, sha256 `abf52118bf771eb7…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : CO% RE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.12.003](https://doi.org/10.1016/j.calphad.2013.12.003) X.J. Liu, J.Y. Lin, Y. Lu, Y.H. Guo, C.P. Wang, Calphad, 45, 138-44(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102688](https://doi.org/10.1016/j.calphad.2024.102688) Z. Shi, G. Shang, X.-G. Lu, Calphad, 85, 102688(2024).  
_assessment that models this phase_

## HCP_A3 (Co–Re)

- Id: `phase:co-re:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 299.59–3999.25 K, x(Re) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-re:hcp-a3)

Names (5): _corpus: _corpus:phase:co-re:hcp-a3  
_tdb: _tdb:CoRe-14Liu.tdb:HCP_A3, tdb:CoRe-18Guo.tdb:HCP_A3, tdb:CoRe-24Per.tdb:HCP_A3, tdb:CoRe-24Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CoRe-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-14Liu.tdb): HCP_A3, type code %A, sha256 `9022ff2a486be381…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CO% RE% : VA : !
~~~~

[CoRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-18Guo.tdb): HCP_A3, type code %A, sha256 `bcd125e1e2f5a714…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CO% RE% : VA : !
~~~~

[CoRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Per.tdb): HCP_A3, type code %A, sha256 `88a3581d7a2f62a0…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% RE% : VA : !
~~~~

[CoRe-24Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Shi.tdb): HCP_A3, type code %A, sha256 `abf52118bf771eb7…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : CO% RE% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.12.003](https://doi.org/10.1016/j.calphad.2013.12.003) X.J. Liu, J.Y. Lin, Y. Lu, Y.H. Guo, C.P. Wang, Calphad, 45, 138-44(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102688](https://doi.org/10.1016/j.calphad.2024.102688) Z. Shi, G. Shang, X.-G. Lu, Calphad, 85, 102688(2024).  
_assessment that models this phase_

## LIQUID (Co–Re)

- Id: `phase:co-re:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 1760.99–4000 K, x(Re) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-re:liquid)

Names (5): _corpus: _corpus:phase:co-re:liquid  
_tdb: _tdb:CoRe-14Liu.tdb:LIQUID, tdb:CoRe-18Guo.tdb:LIQUID, tdb:CoRe-24Per.tdb:LIQUID, tdb:CoRe-24Shi.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CoRe-14Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-14Liu.tdb): LIQUID, type code %, sha256 `9022ff2a486be381…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CO RE : !
~~~~

[CoRe-18Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-18Guo.tdb): LIQUID, type code %, sha256 `bcd125e1e2f5a714…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CO RE : !
~~~~

[CoRe-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Per.tdb): LIQUID, type code %, sha256 `88a3581d7a2f62a0…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO RE : !
~~~~

[CoRe-24Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/CoRe-24Shi.tdb): LIQUID, type code %, sha256 `abf52118bf771eb7…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : CO RE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.12.003](https://doi.org/10.1016/j.calphad.2013.12.003) X.J. Liu, J.Y. Lin, Y. Lu, Y.H. Guo, C.P. Wang, Calphad, 45, 138-44(2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.01.005](https://doi.org/10.1016/j.calphad.2018.01.005) C. Guo, T. Wu, C. Li, Z. Du, Calphad, 61, 33-40(2018).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2024.102688](https://doi.org/10.1016/j.calphad.2024.102688) Z. Shi, G. Shang, X.-G. Lu, Calphad, 85, 102688(2024).  
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
