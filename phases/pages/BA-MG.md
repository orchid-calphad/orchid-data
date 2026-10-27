# Ba–Mg phases

> Ba–Mg system: 7 phases (tier A 3, liquid 1, needs_review 3); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-MG.html · Markdown: https://data.orchid-project.org/phases/pages/BA-MG.md

7 phases (tier A 3, liquid 1, needs_review 3); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-MG) · [full JSON](https://data.orchid-project.org/phases/systems/BA-MG.json) · [Ba–Mg system page](https://data.orchid-project.org/systems/BA-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Mg system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BA2MG17](#phase-ba-mg-ba2mg17); _phase:ba-mg:ba2mg17_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–977.54 K, x(Mg) 0.895–0.895 | 0 | 1 |
| [BA6MG23_D8A](#phase-ba-mg-ba6mg23-d8a); _phase:ba-mg:ba6mg23-d8a_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–873.33 K, x(Mg) 0.793–0.793 | 0 | 1 |
| [BAMG2_C14](#phase-ba-mg-bamg2-c14); _phase:ba-mg:bamg2-c14_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–885.49 K, x(Mg) 0.667–0.667 | 0 | 1 |
| [BCC_A2](#phase-ba-mg-bcc-a2); _phase:ba-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1002.17 K, x(Mg) 0–2e-05 | 0 | 1 |
| [FCC_A1](#phase-ba-mg-fcc-a1); _phase:ba-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ba-mg-hcp-a3); _phase:ba-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.95 K, x(Mg) 0.99998–1 | 0 | 1 |
| [LIQUID](#phase-ba-mg-liquid); _phase:ba-mg:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 637.17–2500 K, x(Mg) 0–1 | 0 | 1 |

## BA2MG17 (Ba–Mg)

- Id: `phase:ba-mg:ba2mg17`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): Th2Zn17 · hR19 · R-3m (166) — Hallstedt 2025 mmc2 row for BA2MG17: Ba2Mg17
- Candidate (tdb_comment): Th2Zn17 · hR19 · R-3m — BaMg-13Ren.tdb: 'Prototype Th2Zn17 (hR19, R-3m)'
- Stoichiometry: Ba 0.1050, Mg 0.8950
- Stability: stable in 1 of 1 calculated diagram(s): 300–977.54 K, x(Mg) 0.895–0.895
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:ba2mg17)

Names (2): _corpus: _corpus:phase:ba-mg:ba2mg17  
_tdb: _tdb:BaMg-13Ren.tdb:BA2MG17  


### TDB models of BA2MG17 (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): BA2MG17, type code %, sha256 `f30cb2ae71edd422…`

~~~~text
51: PHASE BA2MG17 % 2 0.105 0.895 !
52: CONST BA2MG17 : BA : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
_assessment that models this phase_

## BA6MG23_D8A (Ba–Mg)

- Id: `phase:ba-mg:ba6mg23-d8a`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_D8_a; stoichiometry_contradicts_D8_a:BaMg-13Ren.tdb
- Candidate (name_token): Mn23Th6 · D8_a · cF116 · Fm-3m (225) — Strukturbericht/word 'D8A' in the TDB name
- Candidate (sgte_mmc2): Mn23Th6 · D8_a · cF116 · Fm-3m (225) — Hallstedt 2025 mmc2 row for BA6MG23_D8A: Ba6Mg23
- Candidate (tdb_comment): Mn23Th6 · cF116 · Fm-3m — BaMg-13Ren.tdb: 'Prototype Mn23Th6 (cF116, Fm-3m)'
- Stoichiometry: Ba 0.2070, Mg 0.7930
- Stability: stable in 1 of 1 calculated diagram(s): 300–873.33 K, x(Mg) 0.793–0.793
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:ba6mg23-d8a)

Names (2): _corpus: _corpus:phase:ba-mg:ba6mg23-d8a  
_tdb: _tdb:BaMg-13Ren.tdb:BA6MG23_D8A  


### TDB models of BA6MG23_D8A (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): BA6MG23_D8A, type code %, sha256 `f30cb2ae71edd422…`

~~~~text
46: PHASE BA6MG23_D8A % 2 0.207 0.793 !
47: CONST BA6MG23_D8A : BA : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
_assessment that models this phase_

## BAMG2_C14 (Ba–Mg)

- Id: `phase:ba-mg:bamg2-c14`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C14; stoichiometry_contradicts_C14:BaMg-13Ren.tdb
- Candidate (name_token): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Strukturbericht/word 'C14' in the TDB name
- Candidate (sgte_mmc2): MgZn2 · C14 · hP12 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for BAMG2_C14: BaMg2
- Candidate (tdb_comment): MgZn2 · hP12 · P6_3/mmc — BaMg-13Ren.tdb: 'Prototype MgZn2 (hP12, P6_3/mmc)'
- Stoichiometry: Ba 0.3330, Mg 0.6670
- Stability: stable in 1 of 1 calculated diagram(s): 300–885.49 K, x(Mg) 0.667–0.667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:bamg2-c14)

Names (2): _corpus: _corpus:phase:ba-mg:bamg2-c14  
_tdb: _tdb:BaMg-13Ren.tdb:BAMG2_C14  


### TDB models of BAMG2_C14 (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): BAMG2_C14, type code %, sha256 `f30cb2ae71edd422…`

~~~~text
41: PHASE BAMG2_C14 % 2 0.333 0.667 !
42: CONST BAMG2_C14 : BA : MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
_assessment that models this phase_

## BCC_A2 (Ba–Mg)

- Id: `phase:ba-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1002.17 K, x(Mg) 0–2e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:bcc-a2)

Names (2): _corpus: _corpus:phase:ba-mg:bcc-a2  
_tdb: _tdb:BaMg-13Ren.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): BCC_A2, type code %B, sha256 `f30cb2ae71edd422…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BA% MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
_assessment that models this phase_

## FCC_A1 (Ba–Mg)

- Id: `phase:ba-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:fcc-a1)

Names (2): _corpus: _corpus:phase:ba-mg:fcc-a1  
_tdb: _tdb:BaMg-13Ren.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): FCC_A1, type code %A, sha256 `f30cb2ae71edd422…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BA MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
_assessment that models this phase_

## HCP_A3 (Ba–Mg)

- Id: `phase:ba-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.95 K, x(Mg) 0.99998–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:hcp-a3)

Names (2): _corpus: _corpus:phase:ba-mg:hcp-a3  
_tdb: _tdb:BaMg-13Ren.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): HCP_A3, type code %A, sha256 `f30cb2ae71edd422…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BA MG% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
_assessment that models this phase_

## LIQUID (Ba–Mg)

- Id: `phase:ba-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 637.17–2500 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-mg:liquid)

Names (2): _corpus: _corpus:phase:ba-mg:liquid  
_tdb: _tdb:BaMg-13Ren.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaMg-13Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/BaMg-13Ren.tdb): LIQUID, type code %, sha256 `f30cb2ae71edd422…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BA MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.110870](https://doi.org/10.3139/146.110870) X. Ren, C. Li, Z. Du, C. Guo, S. Chen, Int. J. Mater. Res., 104, 358-363(2013).  
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
