# Re–Y phases

> Re–Y system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-Y.html · Markdown: https://data.orchid-project.org/phases/pages/RE-Y.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-Y) · [full JSON](https://data.orchid-project.org/phases/systems/RE-Y.json) · [Re–Y system page](https://data.orchid-project.org/systems/RE-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–Y system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-re-y-bcc-a2); _phase:re-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1751.15–3999.9 K, x(Y) 1–1 | 0 | 1 |
| [FCC_A1](#phase-re-y-fcc-a1); _phase:re-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-re-y-hcp-a3); _phase:re-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3557.12 K, x(Y) 0–1 | 0 | 1 |
| [LIQUID](#phase-re-y-liquid); _phase:re-y:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1721.23–4000 K, x(Y) 0–1 | 0 | 1 |
| [RE2Y_C14](#phase-re-y-re2y-c14); _phase:re-y:re2y-c14_ | MgZn2 · C14 · hP12 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2793.37 K, x(Y) 0.33333–0.33333 | 4 | 1 |

## BCC_A2 (Re–Y)

- Id: `phase:re-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1751.15–3999.9 K, x(Y) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-y:bcc-a2)

Names (2): _corpus: _corpus:phase:re-y:bcc-a2  
_tdb: _tdb:ReY-10Zac.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ReY-10Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReY-10Zac.tdb): BCC_A2, type code %B, sha256 `43f0c18d9a96533e…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : RE Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032) C. Zacherl, J. Saal, Y. Wang, Z.K. Liu, First-principles calculations and thermodynamic modeling of the Re–Y system with extension to the Ni–Re–Y system, Intermetallics 18, 2412-2418 (2010).  
_assessment that models this phase_

## FCC_A1 (Re–Y)

- Id: `phase:re-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-y:fcc-a1)

Names (2): _corpus: _corpus:phase:re-y:fcc-a1  
_tdb: _tdb:ReY-10Zac.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ReY-10Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReY-10Zac.tdb): FCC_A1, type code %A, sha256 `43f0c18d9a96533e…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : RE Y : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032) C. Zacherl, J. Saal, Y. Wang, Z.K. Liu, First-principles calculations and thermodynamic modeling of the Re–Y system with extension to the Ni–Re–Y system, Intermetallics 18, 2412-2418 (2010).  
_assessment that models this phase_

## HCP_A3 (Re–Y)

- Id: `phase:re-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3557.12 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-y:hcp-a3)

Names (2): _corpus: _corpus:phase:re-y:hcp-a3  
_tdb: _tdb:ReY-10Zac.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ReY-10Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReY-10Zac.tdb): HCP_A3, type code %A, sha256 `43f0c18d9a96533e…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : RE% Y% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032) C. Zacherl, J. Saal, Y. Wang, Z.K. Liu, First-principles calculations and thermodynamic modeling of the Re–Y system with extension to the Ni–Re–Y system, Intermetallics 18, 2412-2418 (2010).  
_assessment that models this phase_

## LIQUID (Re–Y)

- Id: `phase:re-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1721.23–4000 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-y:liquid)

Names (2): _corpus: _corpus:phase:re-y:liquid  
_tdb: _tdb:ReY-10Zac.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ReY-10Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReY-10Zac.tdb): LIQUID, type code %, sha256 `43f0c18d9a96533e…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : RE Y : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032) C. Zacherl, J. Saal, Y. Wang, Z.K. Liu, First-principles calculations and thermodynamic modeling of the Re–Y system with extension to the Ni–Re–Y system, Intermetallics 18, 2412-2418 (2010).  
_assessment that models this phase_

## RE2Y_C14 (Re–Y)

- Id: `phase:re-y:re2y-c14`; status `assigned`
- Structure: MgZn2 · C14 · hP12 · P6_3/mmc (194); type `st:c14-mgzn2-hp12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaabgmop and oqmd-19317, space group 194
- Stoichiometry: Re 0.6667, Y 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–2793.37 K, x(Y) 0.33333–0.33333
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-y:re2y-c14)

Names (5): _corpus: _corpus:phase:re-y:re2y-c14  
_mp: _mp:mp-aaabgmop  
_oqmd: _oqmd:oqmd-19317  
_paper: _paper:10.1016/j.intermet.2010.08.032:Re2Y  
_tdb: _tdb:ReY-10Zac.tdb:RE2Y_C14  


### TDB models of RE2Y_C14 (1): PHASE and CONSTITUENT statements as written

[ReY-10Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReY-10Zac.tdb): RE2Y_C14, type code %, sha256 `43f0c18d9a96533e…`

~~~~text
40: PHASE RE2Y_C14 % 2 2 1 !
41: CONST RE2Y_C14 : RE : Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.intermet.2010.08.032](https://doi.org/10.1016/j.intermet.2010.08.032) C. Zacherl, J. Saal, Y. Wang, Z.K. Liu, First-principles calculations and thermodynamic modeling of the Re–Y system with extension to the Ni–Re–Y system, Intermetallics 18, 2412-2418 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1107/s0365110x59001918](https://doi.org/10.1107/s0365110x59001918) V. B. Compton, B. T. Matthias, Laves phase compounds of rare earths and hafnium with noble metals, Acta Cryst 12, 651-654 (1959).  
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
