# Ga–N phases

> Ga–N system: 5 phases (tier A 2, liquid 1, gas 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-N.html · Markdown: https://data.orchid-project.org/phases/pages/GA-N.md

5 phases (tier A 2, liquid 1, gas 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-N) · [full JSON](https://data.orchid-project.org/phases/systems/GA-N.json) · [Ga–N system page](https://data.orchid-project.org/systems/GA-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–N system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-n-a11-orthorhombic); _phase:ga-n:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(N) 0–0 | 1 | 2 |
| [GAN_B4](#phase-ga-n-gan-b4); _phase:ga-n:gan-b4_ | ZnS (wurtzite) · B4 · hP4 · P6_3mc (186) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1117.53 K, x(N) 0.5–0.5 | 4 | 2 |
| [GAS](#phase-ga-n-gas); _phase:ga-n:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300.03–2500 K, x(N) 0–1 | 0 | 2 |
| [LIQUID](#phase-ga-n-liquid); _phase:ga-n:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 302.91–2473.18 K, x(N) 0–2e-05 | 1 | 2 |
| [N2GAS](#phase-ga-n-n2gas); _phase:ga-n:n2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–1065 K, x(N) 1–1 | 0 | 2 |

## ORTHORHOMBIC_A11 (Ga–N)

- Id: `phase:ga-n:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–302.91 K, x(N) 0–0
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-n:a11-orthorhombic)

Names (4): _corpus: _corpus:phase:ga-n:a11-orthorhombic  
_paper: _paper:10.1016/s0022-0248(03)01352-6:Ga  
_tdb: _tdb:GaN-03Unl.tdb:ORTHORHOMBIC_A11, tdb:GaN-98Dav.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (2): PHASE and CONSTITUENT statements as written

[GaN-03Unl.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-03Unl.tdb): ORTHORHOMBIC_A11, type code %, sha256 `eb023f7ceb4ad845…`

~~~~text
34: PHASE ORTHORHOMBIC_A11 % 1 1 !
35: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[GaN-98Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-98Dav.tdb): ORTHORHOMBIC_A11, type code %, sha256 `879d60b9d25803c8…`

~~~~text
34: PHASE ORTHORHOMBIC_A11 % 1 1 !
35: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-0248(03)01352-6](https://doi.org/10.1016/S0022-0248%2803%2901352-6) J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, J. Cryst. Growth, 256, 33-51(2003).  
_assessment that models this phase; reports values for this phase_

## GAN_B4 (Ga–N)

- Id: `phase:ga-n:gan-b4`; status `assigned`
- Structure: ZnS (wurtzite) · B4 · hP4 · P6_3mc (186); type `st:b4-zns-wurtzite-hp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabey and oqmd-6450, space group 186
- Stoichiometry: Ga 0.5000, N 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1117.53 K, x(N) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-n:gan-b4)

Names (6): _corpus: _corpus:phase:ga-n:gan-b4  
_mp: _mp:mp-aaaaabey  
_oqmd: _oqmd:oqmd-6450  
_paper: _paper:10.1016/s0022-0248(03)01352-6:GaN  
_tdb: _tdb:GaN-03Unl.tdb:GAN_B4, tdb:GaN-98Dav.tdb:GAN_B4  


### TDB models of GAN_B4 (2): PHASE and CONSTITUENT statements as written

[GaN-03Unl.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-03Unl.tdb): GAN_B4, type code %, sha256 `eb023f7ceb4ad845…`

~~~~text
39: PHASE GAN_B4 % 2 1 1 !
40: CONST GAN_B4 : GA : N : !
~~~~

[GaN-98Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-98Dav.tdb): GAN_B4, type code %, sha256 `879d60b9d25803c8…`

~~~~text
39: PHASE GAN_B4 % 2 1 1 !
40: CONST GAN_B4 : GA : N : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0022-0248(03)01352-6](https://doi.org/10.1016/S0022-0248%2803%2901352-6) J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, J. Cryst. Growth, 256, 33-51(2003).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/zaac.19402440203](https://doi.org/10.1002/zaac.19402440203) Harry Hahn, Robert Juza, Untersuchungen über die Nitride von Cadmium, Gallium, Indium und Germanium. Metallamide und Metallnitride. VIII. Mitteilung, Z. Anorg. Allg. Chem. 244, 111-124 (1940).  
_cited as the source of values for this phase_

## GAS (Ga–N)

- Id: `phase:ga-n:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300.03–2500 K, x(N) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-n:gas)

Names (3): _corpus: _corpus:phase:ga-n:gas  
_tdb: _tdb:GaN-03Unl.tdb:GAS, tdb:GaN-98Dav.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[GaN-03Unl.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-03Unl.tdb): GAS, type code %, sha256 `eb023f7ceb4ad845…`

~~~~text
45: PHASE GAS:G % 1 1 !
46: CONST GAS:G : GA GA2 N N2 N3 : !
~~~~

[GaN-98Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-98Dav.tdb): GAS, type code %, sha256 `879d60b9d25803c8…`

~~~~text
45: PHASE GAS:G % 1 1 !
46: CONST GAS:G : GA GA2 N N2 N3 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-0248(03)01352-6](https://doi.org/10.1016/S0022-0248%2803%2901352-6) J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, J. Cryst. Growth, 256, 33-51(2003).  
_assessment that models this phase_

## LIQUID (Ga–N)

- Id: `phase:ga-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 302.91–2473.18 K, x(N) 0–2e-05
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-n:liquid)

Names (4): _corpus: _corpus:phase:ga-n:liquid  
_paper: _paper:10.1016/s0022-0248(03)01352-6:liquid  
_tdb: _tdb:GaN-03Unl.tdb:LIQUID, tdb:GaN-98Dav.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GaN-03Unl.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-03Unl.tdb): LIQUID, type code %, sha256 `eb023f7ceb4ad845…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : GA N : !
~~~~

[GaN-98Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-98Dav.tdb): LIQUID, type code %, sha256 `879d60b9d25803c8…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : GA N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-0248(03)01352-6](https://doi.org/10.1016/S0022-0248%2803%2901352-6) J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, J. Cryst. Growth, 256, 33-51(2003).  
_assessment that models this phase; reports values for this phase_

## N2GAS (Ga–N)

- Id: `phase:ga-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1065 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-n:n2gas)

Names (3): _corpus: _corpus:phase:ga-n:n2gas  
_tdb: _tdb:GaN-03Unl.tdb:N2GAS, tdb:GaN-98Dav.tdb:N2GAS  


### TDB models of N2GAS (2): PHASE and CONSTITUENT statements as written

[GaN-03Unl.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-03Unl.tdb): N2GAS, type code %, sha256 `eb023f7ceb4ad845…`

~~~~text
42: PHASE N2GAS % 1 1 !
43: CONST N2GAS : N2 : !
~~~~

[GaN-98Dav.tdb](https://orchid-project.org/data/databases/sgte-binary/GaN-98Dav.tdb): N2GAS, type code %, sha256 `879d60b9d25803c8…`

~~~~text
42: PHASE N2GAS % 1 1 !
43: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0022-0248(03)01352-6](https://doi.org/10.1016/S0022-0248%2803%2901352-6) J. Unland, B. Onderka, A. Davydov, R. Schmid-Fetzer, J. Cryst. Growth, 256, 33-51(2003).  
_assessment that models this phase_

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
