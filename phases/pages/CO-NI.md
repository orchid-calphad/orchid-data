# Co–Ni phases

> Co–Ni system: 6 phases (tier A 4, liquid 1, unresolved_no_candidates 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-NI.html · Markdown: https://data.orchid-project.org/phases/pages/CO-NI.md

6 phases (tier A 4, liquid 1, unresolved_no_candidates 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-NI) · [full JSON](https://data.orchid-project.org/phases/systems/CO-NI.json) · [Co–Ni system page](https://data.orchid-project.org/systems/CO-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Ni system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-co-ni-bcc-a2); _phase:co-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [SIGMA_D8B](#phase-co-ni-d8b-sigma); _phase:co-ni:d8b-sigma_ | sigma-CrFe · D8_b · tP30 · P4_2/mnm (136) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [DIS_SIG](#phase-co-ni-dis-sig); _phase:co-ni:dis-sig_ |  | unresolved_no_candidates | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-co-ni-fcc-a1); _phase:co-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1767.99 K, x(Ni) 0–1 | 0 | 2 |
| [HCP_A3](#phase-co-ni-hcp-a3); _phase:co-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–695.44 K, x(Ni) 0–0.29141 | 0 | 2 |
| [LIQUID](#phase-co-ni-liquid); _phase:co-ni:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1728.25–2500 K, x(Ni) 0–1 | 0 | 2 |

## BCC_A2 (Co–Ni)

- Id: `phase:co-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ni:bcc-a2)

Names (3): _corpus: _corpus:phase:co-ni:bcc-a2  
_tdb: _tdb:CoNi-24Per.tdb:BCC_A2, tdb:CoNi-87Fer-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CoNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb): BCC_A2, type code %B, sha256 `969df9adb5e23ceb…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO NI : VA : !
~~~~

[CoNi-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-87Fer-LB.tdb): BCC_A2, type code %B, sha256 `b0243f66a4c704e5…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CO NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1987-780905](https://doi.org/10.1515/ijmr-1987-780905) A. Fernandez Guillermet, Z. Metallkd., 78, 639-47(1987).  
_assessment that models this phase_

## SIGMA_D8B (Co–Ni)

- Id: `phase:co-ni:d8b-sigma`; status `assigned`
- Structure: sigma-CrFe · D8_b · tP30 · P4_2/mnm (136); type `st:d8-b-sigma-crfe-tp30`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in CoNi-24Per.tdb also describes the disordered state
- Caveat: partitioned order/disorder model in CoNi-87Fer-LB.tdb also describes the disordered state
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ni:d8b-sigma)

Names (3): _corpus: _corpus:phase:co-ni:d8b-sigma  
_tdb: _tdb:CoNi-24Per.tdb:SIGMA_D8B, tdb:CoNi-87Fer-LB.tdb:SIGMA_D8B  


### TDB models of SIGMA_D8B (2): PHASE and CONSTITUENT statements as written

[CoNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb): SIGMA_D8B, type code %AS, sha256 `969df9adb5e23ceb…`

~~~~text
48: PHASE SIGMA_D8B %AS 5 2 4 8 8 8 !
49: CONST SIGMA_D8B : CO NI : CO NI : CO NI : CO NI : CO NI : !
~~~~

[CoNi-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-87Fer-LB.tdb): SIGMA_D8B, type code %, sha256 `b0243f66a4c704e5…`

~~~~text
42: PHASE SIGMA_D8B % 3 10 4 16 !
43: CONST SIGMA_D8B : CO NI : CO NI : CO NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1987-780905](https://doi.org/10.1515/ijmr-1987-780905) A. Fernandez Guillermet, Z. Metallkd., 78, 639-47(1987).  
_assessment that models this phase_

## DIS_SIG (Co–Ni)

- Id: `phase:co-ni:dis-sig`; status `unresolved_no_candidates`
- No structure assigned. Why: name_has_descriptive_tokens:DIS,SIG; no_structure_token
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ni:dis-sig)

Names (2): _corpus: _corpus:phase:co-ni:dis-sig  
_tdb: _tdb:CoNi-24Per.tdb:DIS_SIG  


### TDB models of DIS_SIG (1): PHASE and CONSTITUENT statements as written

[CoNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb): DIS_SIG, type code %A, sha256 `969df9adb5e23ceb…`

~~~~text
43: PHASE DIS_SIG %A 1 1 !
44: CONST DIS_SIG : CO NI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_

## FCC_A1 (Co–Ni)

- Id: `phase:co-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1767.99 K, x(Ni) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ni:fcc-a1)

Names (3): _corpus: _corpus:phase:co-ni:fcc-a1  
_tdb: _tdb:CoNi-24Per.tdb:FCC_A1, tdb:CoNi-87Fer-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CoNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb): FCC_A1, type code %A, sha256 `969df9adb5e23ceb…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% NI% : VA : !
~~~~

[CoNi-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-87Fer-LB.tdb): FCC_A1, type code %A, sha256 `b0243f66a4c704e5…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CO% NI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1987-780905](https://doi.org/10.1515/ijmr-1987-780905) A. Fernandez Guillermet, Z. Metallkd., 78, 639-47(1987).  
_assessment that models this phase_

## HCP_A3 (Co–Ni)

- Id: `phase:co-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–695.44 K, x(Ni) 0–0.29141
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ni:hcp-a3)

Names (3): _corpus: _corpus:phase:co-ni:hcp-a3  
_tdb: _tdb:CoNi-24Per.tdb:HCP_A3, tdb:CoNi-87Fer-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CoNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb): HCP_A3, type code %A, sha256 `969df9adb5e23ceb…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% NI : VA : !
~~~~

[CoNi-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-87Fer-LB.tdb): HCP_A3, type code %A, sha256 `b0243f66a4c704e5…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CO% NI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1987-780905](https://doi.org/10.1515/ijmr-1987-780905) A. Fernandez Guillermet, Z. Metallkd., 78, 639-47(1987).  
_assessment that models this phase_

## LIQUID (Co–Ni)

- Id: `phase:co-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1728.25–2500 K, x(Ni) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ni:liquid)

Names (3): _corpus: _corpus:phase:co-ni:liquid  
_tdb: _tdb:CoNi-24Per.tdb:LIQUID, tdb:CoNi-87Fer-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CoNi-24Per.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-24Per.tdb): LIQUID, type code %, sha256 `969df9adb5e23ceb…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO NI : !
~~~~

[CoNi-87Fer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoNi-87Fer-LB.tdb): LIQUID, type code %, sha256 `b0243f66a4c704e5…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CO NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-023-01079-3](https://doi.org/10.1007/s11669-023-01079-3) Júlio César Pereira dos Santos, Sean Griesemer, Nathalie Dupin, Ursula R. Kattner, Chuan Liu, Daniela Ivanova et al., Applying the Effective Bond Energy Formalism (EBEF) to Describe the Sigma (σ) Phase in the Co-Cr-Ni-Re System, J. Phase Equilib. Diffus. 45, 330-357 (2024).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1987-780905](https://doi.org/10.1515/ijmr-1987-780905) A. Fernandez Guillermet, Z. Metallkd., 78, 639-47(1987).  
_assessment that models this phase_

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
