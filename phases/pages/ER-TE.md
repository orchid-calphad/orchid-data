# Er–Te phases

> Er–Te system: 8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ER-TE.html · Markdown: https://data.orchid-project.org/phases/pages/ER-TE.md

8 phases (tier A 5, tier B 1, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ER-TE) · [full JSON](https://data.orchid-project.org/phases/systems/ER-TE.json) · [Er–Te system page](https://data.orchid-project.org/systems/ER-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/ER-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Er–Te system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-er-te-a8-hexagonal); _phase:er-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 3 | 1 |
| [BCC_A2](#phase-er-te-bcc-a2); _phase:er-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [ER2TE3](#phase-er-te-er2te3); _phase:er-te:er2te3_ | Sc2S3 · oF80 · Fddd (70) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1470 K, x(Te) 0.6–0.6 | 24 | 1 |
| [ERTE_B1](#phase-er-te-erte-b1); _phase:er-te:erte-b1_ | NaCl · B1 · cF8 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1800 K, x(Te) 0.5–0.5 | 10 | 1 |
| [ERTE3](#phase-er-te-erte3); _phase:er-te:erte3_ | NdTe3 · oC16 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–953.4 K, x(Te) 0.75–0.75 | 18 | 1 |
| [FCC_A1](#phase-er-te-fcc-a1); _phase:er-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-er-te-hcp-a3); _phase:er-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1802 K, x(Te) 0–0 | 3 | 1 |
| [LIQUID](#phase-er-te-liquid); _phase:er-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 722.66–2500 K, x(Te) 0–1 | 22 | 1 |

## HEXAGONAL_A8 (Er–Te)

- Id: `phase:er-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:a8-hexagonal)

Names (4): _corpus: _corpus:phase:er-te:a8-hexagonal, corpus:phase:er-te:hexagonal-a8  
_paper: _paper:10.1007/s11669-022-00947-8:(Te)  
_tdb: _tdb:ErTe-22Ben.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): HEXAGONAL_A8, type code %, sha256 `f2f2246d321ba2f9…`

~~~~text
47: PHASE HEXAGONAL_A8 % 1 1 !
48: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_

## BCC_A2 (Er–Te)

- Id: `phase:er-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Er 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:bcc-a2)

Names (2): _corpus: _corpus:phase:er-te:bcc-a2  
_tdb: _tdb:ErTe-22Ben.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): BCC_A2, type code %B, sha256 `f2f2246d321ba2f9…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase_

## ER2TE3 (Er–Te)

- Id: `phase:er-te:er2te3`; status `assigned`
- Structure: Sc2S3 · oF80 · Fddd (70); type `st:sc2s3-of80`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Er 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1470 K, x(Te) 0.6–0.6
- Literature: 24 values (24 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:er2te3)

Names (5): _corpus: _corpus:phase:er-te:er2te3  
_mp: _mp:mp-aaaaavrf  
_oqmd: _oqmd:oqmd-665800  
_paper: _paper:10.1007/s11669-022-00947-8:Er2Te3  
_tdb: _tdb:ErTe-22Ben.tdb:ER2TE3  


### TDB models of ER2TE3 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): ER2TE3, type code %, sha256 `f2f2246d321ba2f9…`

~~~~text
57: PHASE ER2TE3 % 2 2 3 !
58: CONST ER2TE3 : ER : TE : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.electacta.2016.11.075](https://doi.org/10.1016/j.electacta.2016.11.075) V.P. Vassiliev, V.A. Lysenko, A New Approach for the Study of Thermodynamic Properties of Lanthanide Compounds, Electrochimica Acta 222, 1770-1777 (2016).  
_cited as the source of values for this phase_
- [doi:10.1021/ic50026a021](https://doi.org/10.1021/ic50026a021) D. J. Haase, H. Steinfink, E. J. Weiss, The Phase Equilibria and Crystal Chemistry of the Rare Earth Group VI Systems. II. Erbium-Tellurium, Inorg. Chem. 4, 541-543 (1965).  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_
- [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013).  
_cited as the source of values for this phase_
- [doi:10.15330/pcss.21.2.312-318](https://doi.org/10.15330/pcss.21.2.312-318) S. Z. Imamaliyeva, I. F. Mehdiyeva, D. B. Taghiyev, M. B. Babanly, Thermodynamic investigations of the erbium tellurides by EMF method, PCSS 21, 312-318 (2020).  
_cited as the source of values for this phase_

## ERTE_B1 (Er–Te)

- Id: `phase:er-te:erte-b1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Er 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1800 K, x(Te) 0.5–0.5
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:erte-b1)

Names (3): _corpus: _corpus:phase:er-te:erte-b1  
_paper: _paper:10.1007/s11669-022-00947-8:ErTe  
_tdb: _tdb:ErTe-22Ben.tdb:ERTE_B1  


### TDB models of ERTE_B1 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): ERTE_B1, type code %, sha256 `f2f2246d321ba2f9…`

~~~~text
52: PHASE ERTE_B1 % 2 1 1 !
53: CONST ERTE_B1 : ER : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50026a021](https://doi.org/10.1021/ic50026a021) D. J. Haase, H. Steinfink, E. J. Weiss, The Phase Equilibria and Crystal Chemistry of the Rare Earth Group VI Systems. II. Erbium-Tellurium, Inorg. Chem. 4, 541-543 (1965).  
_cited as the source of values for this phase_

## ERTE3 (Er–Te)

- Id: `phase:er-te:erte3`; status `assigned`
- Structure: NdTe3 · oC16 · Cmcm (63); type `st:ndte3-oc16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_63_matches_6_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Er 0.2500, Te 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–953.4 K, x(Te) 0.75–0.75
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:erte3)

Names (3): _corpus: _corpus:phase:er-te:erte3  
_paper: _paper:10.1007/s11669-022-00947-8:ErTe3  
_tdb: _tdb:ErTe-22Ben.tdb:ERTE3  


### TDB models of ERTE3 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): ERTE3, type code %, sha256 `f2f2246d321ba2f9…`

~~~~text
62: PHASE ERTE3 % 2 1 3 !
63: CONST ERTE3 : ER : TE : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50026a021](https://doi.org/10.1021/ic50026a021) D. J. Haase, H. Steinfink, E. J. Weiss, The Phase Equilibria and Crystal Chemistry of the Rare Earth Group VI Systems. II. Erbium-Tellurium, Inorg. Chem. 4, 541-543 (1965).  
_cited as the source of values for this phase_
- [doi:10.1038/npjcompumats.2015.10](https://doi.org/10.1038/npjcompumats.2015.10) Scott Kirklin, James E Saal, Bryce Meredig, Alex Thompson, Jeff W Doak, Muratahan Aykol et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput Mater 1 (2015).  
_cited as the source of values for this phase_
- [doi:10.1063/1.4812323](https://doi.org/10.1063/1.4812323) Anubhav Jain, Shyue Ping Ong, Geoffroy Hautier, Wei Chen, William Davidson Richards, Stephen Dacek et al., Commentary: The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013).  
_cited as the source of values for this phase_
- [doi:10.15330/pcss.21.2.312-318](https://doi.org/10.15330/pcss.21.2.312-318) S. Z. Imamaliyeva, I. F. Mehdiyeva, D. B. Taghiyev, M. B. Babanly, Thermodynamic investigations of the erbium tellurides by EMF method, PCSS 21, 312-318 (2020).  
_cited as the source of values for this phase_

## FCC_A1 (Er–Te)

- Id: `phase:er-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Er 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:fcc-a1)

Names (2): _corpus: _corpus:phase:er-te:fcc-a1  
_tdb: _tdb:ErTe-22Ben.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): FCC_A1, type code %A, sha256 `f2f2246d321ba2f9…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase_

## HCP_A3 (Er–Te)

- Id: `phase:er-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Er 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1802 K, x(Te) 0–0
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:hcp-a3)

Names (3): _corpus: _corpus:phase:er-te:hcp-a3  
_paper: _paper:10.1007/s11669-022-00947-8:(Er)  
_tdb: _tdb:ErTe-22Ben.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): HCP_A3, type code %A, sha256 `f2f2246d321ba2f9…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : ER : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50026a021](https://doi.org/10.1021/ic50026a021) D. J. Haase, H. Steinfink, E. J. Weiss, The Phase Equilibria and Crystal Chemistry of the Rare Earth Group VI Systems. II. Erbium-Tellurium, Inorg. Chem. 4, 541-543 (1965).  
_cited as the source of values for this phase_

## LIQUID (Er–Te)

- Id: `phase:er-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 722.66–2500 K, x(Te) 0–1
- Literature: 22 values (22 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-te:liquid)

Names (4): _corpus: _corpus:phase:er-te:liquid  
_paper: _paper:10.1007/s11669-022-00947-8:L, paper:10.1007/s11669-022-00947-8:liquid  
_tdb: _tdb:ErTe-22Ben.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ErTe-22Ben.tdb](https://orchid-project.org/data/databases/sgte-binary/ErTe-22Ben.tdb): LIQUID, type code %, sha256 `f2f2246d321ba2f9…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : ER ERTE ER2TE3 TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-022-00947-8](https://doi.org/10.1007/s11669-022-00947-8) S. Bennoui, Y. Djaballah, V. Vassiliev, A. Belgacem-Bouzida, Thermodynamic Study of Er-Bi and Er-Te Systems by Combination of First-Principles Calculations and the CALPHAD Method, J. Phase Equilib. Diffus. 43, 126-138 (2022).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1021/ic50026a021](https://doi.org/10.1021/ic50026a021) D. J. Haase, H. Steinfink, E. J. Weiss, The Phase Equilibria and Crystal Chemistry of the Rare Earth Group VI Systems. II. Erbium-Tellurium, Inorg. Chem. 4, 541-543 (1965).  
_cited as the source of values for this phase_

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
