# Eu–Mg phases

> Eu–Mg system: 8 phases (tier A 4, tier C 3, liquid 1); 0 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/EU-MG.html · Markdown: https://data.orchid-project.org/phases/pages/EU-MG.md

8 phases (tier A 4, tier C 3, liquid 1); 0 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=EU-MG) · [full JSON](https://data.orchid-project.org/phases/systems/EU-MG.json) · [Eu–Mg system page](https://data.orchid-project.org/systems/EU-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/EU-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Eu–Mg system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-eu-mg-bcc-a2); _phase:eu-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [EU2MG17](#phase-eu-mg-eu2mg17); _phase:eu-mg:eu2mg17_ | Ni17Th2 · hP38 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | no calculated diagram | 0 | 1 |
| [EUMG_B2](#phase-eu-mg-eumg-b2); _phase:eu-mg:eumg-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [EUMG2_C14](#phase-eu-mg-eumg2-c14); _phase:eu-mg:eumg2-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [EUMG4](#phase-eu-mg-eumg4); _phase:eu-mg:eumg4_ | Mg4Sr · hP90 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | no calculated diagram | 0 | 1 |
| [EUMG5](#phase-eu-mg-eumg5); _phase:eu-mg:eumg5_ | EuMg5 · hP42 · P6_3/mmc (194) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | no calculated diagram | 0 | 1 |
| [HCP_A3](#phase-eu-mg-hcp-a3); _phase:eu-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | no calculated diagram | 0 | 1 |
| [LIQUID](#phase-eu-mg-liquid); _phase:eu-mg:liquid_ | liquid | liquid | no calculated diagram | 4 | 1 |

## BCC_A2 (Eu–Mg)

- Id: `phase:eu-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:bcc-a2)

Names (2): _corpus: _corpus:phase:eu-mg:bcc-a2  
_tdb: _tdb:EuMg-08Tao.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): BCC_A2, type code %B, sha256 `8aec385f6e458adc…`

~~~~text
28: PHASE BCC_A2 %B 2 1 3 !
29: CONST BCC_A2 : EU : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## EU2MG17 (Eu–Mg)

- Id: `phase:eu-mg:eu2mg17`; status `assigned`
- Structure: Ni17Th2 · hP38 · P6_3/mmc (194); type `st:ni17th2-hp38`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_mp, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.1053, Mg 0.8947
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:eu2mg17)

Names (2): _corpus: _corpus:phase:eu-mg:eu2mg17  
_tdb: _tdb:EuMg-08Tao.tdb:EU2MG17  


### TDB models of EU2MG17 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): EU2MG17, type code %, sha256 `8aec385f6e458adc…`

~~~~text
60: PHASE EU2MG17 % 2 2 17 !
61: CONST EU2MG17 : EU : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## EUMG_B2 (Eu–Mg)

- Id: `phase:eu-mg:eumg-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.5000, Mg 0.5000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:eumg-b2)

Names (2): _corpus: _corpus:phase:eu-mg:eumg-b2  
_tdb: _tdb:EuMg-08Tao.tdb:EUMG_B2  


### TDB models of EUMG_B2 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): EUMG_B2, type code %, sha256 `8aec385f6e458adc…`

~~~~text
38: PHASE EUMG_B2 % 2 1 1 !
39: CONST EUMG_B2 : EU : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## EUMG2_C14 (Eu–Mg)

- Id: `phase:eu-mg:eumg2-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Stoichiometry: Eu 0.3333, Mg 0.6667
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:eumg2-c14)

Names (2): _corpus: _corpus:phase:eu-mg:eumg2-c14  
_tdb: _tdb:EuMg-08Tao.tdb:EUMG2_C14  


### TDB models of EUMG2_C14 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): EUMG2_C14, type code %, sha256 `8aec385f6e458adc…`

~~~~text
43: PHASE EUMG2_C14 % 2 1 2 !
44: CONST EUMG2_C14 : EU : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## EUMG4 (Eu–Mg)

- Id: `phase:eu-mg:eumg4`; status `assigned`
- Structure: Mg4Sr · hP90 · P6_3/mmc (194); type `st:mg4sr-hp90`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.2000, Mg 0.8000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:eumg4)

Names (2): _corpus: _corpus:phase:eu-mg:eumg4  
_tdb: _tdb:EuMg-08Tao.tdb:EUMG4  


### TDB models of EUMG4 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): EUMG4, type code %, sha256 `8aec385f6e458adc…`

~~~~text
48: PHASE EUMG4 % 2 1 4 !
49: CONST EUMG4 : EU : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## EUMG5 (Eu–Mg)

- Id: `phase:eu-mg:eumg5`; status `assigned`
- Structure: EuMg5 · hP42 · P6_3/mmc (194); type `st:eumg5-hp42`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Eu 0.1667, Mg 0.8333
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:eumg5)

Names (2): _corpus: _corpus:phase:eu-mg:eumg5  
_tdb: _tdb:EuMg-08Tao.tdb:EUMG5  


### TDB models of EUMG5 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): EUMG5, type code %, sha256 `8aec385f6e458adc…`

~~~~text
55: PHASE EUMG5 % 2 1 5 !
56: CONST EUMG5 : EU : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## HCP_A3 (Eu–Mg)

- Id: `phase:eu-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mg 1.0000
- Stability: no calculated diagram
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:hcp-a3)

Names (2): _corpus: _corpus:phase:eu-mg:hcp-a3  
_tdb: _tdb:EuMg-08Tao.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): HCP_A3, type code %A, sha256 `8aec385f6e458adc…`

~~~~text
33: PHASE HCP_A3 %A 2 1 0.5 !
34: CONST HCP_A3 : MG% : VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase_

## LIQUID (Eu–Mg)

- Id: `phase:eu-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: no calculated diagram
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:eu-mg:liquid)

Names (3): _corpus: _corpus:phase:eu-mg:liquid  
_paper: _paper:10.1016/j.calphad.2008.07.003:L  
_tdb: _tdb:EuMg-08Tao.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[EuMg-08Tao.tdb](https://orchid-project.org/data/databases/sgte-binary/EuMg-08Tao.tdb): LIQUID, type code %, sha256 `8aec385f6e458adc…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : EU MG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.07.003](https://doi.org/10.1016/j.calphad.2008.07.003) X.M. Tao, H. Wang, W.J. Zhu, H.S. Liu, Y.F. Ouyang, Z.P. Jin, Thermodynamic description of the Mg–Eu binary system, Calphad 32, 462-465 (2008).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(69)90045-9](https://doi.org/10.1016/0022-5088%2869%2990045-9) Werner Mühlpfordt, Wilhelm Klemm, Zur Kenntnis des systems Magnesium-Europium III. Das Zustandsdiagramm des systems MgEu, Journal of the Less Common Metals 17, 127-129 (1969).  
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
