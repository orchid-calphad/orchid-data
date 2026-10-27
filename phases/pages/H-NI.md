# H–Ni phases

> H–Ni system: 5 phases (tier A 3, liquid 1, gas 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-NI.html · Markdown: https://data.orchid-project.org/phases/pages/H-NI.md

5 phases (tier A 3, liquid 1, gas 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-NI) · [full JSON](https://data.orchid-project.org/phases/systems/H-NI.json) · [H–Ni system page](https://data.orchid-project.org/systems/H-NI.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-NI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–Ni system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-ni-bcc-a2); _phase:h-ni:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-h-ni-fcc-a1); _phase:h-ni:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1728.24 K, x(H) 0–0.00087 | 6 | 2 |
| [GAS](#phase-h-ni-gas); _phase:h-ni:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0.98558–1 | 6 | 2 |
| [HCP_A3](#phase-h-ni-hcp-a3); _phase:h-ni:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-h-ni-liquid); _phase:h-ni:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1726.03–2500 K, x(H) 0–0.00424 | 6 | 2 |

## BCC_A2 (H–Ni)

- Id: `phase:h-ni:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ni:bcc-a2)

Names (3): _corpus: _corpus:phase:h-ni:bcc-a2  
_tdb: _tdb:NiH-09Pal.tdb:BCC_A2, tdb:NiH-99Zen.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NiH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-09Pal.tdb): BCC_A2, type code %B, sha256 `436418f01844f2fd…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI : H VA% : !
~~~~

[NiH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-99Zen.tdb): BCC_A2, type code %B, sha256 `d480b20f77444466…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00857-3](https://doi.org/10.1016/S0925-8388%2898%2900857-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, J. Alloys Compd., 283, 151-61(1999).  
_assessment that models this phase_

## FCC_A1 (H–Ni)

- Id: `phase:h-ni:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1728.24 K, x(H) 0–0.00087
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ni:fcc-a1)

Names (4): _corpus: _corpus:phase:h-ni:fcc-a1  
_paper: _paper:10.1016/s0925-8388(98)00857-3:(Ni)  
_tdb: _tdb:NiH-09Pal.tdb:FCC_A1, tdb:NiH-99Zen.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NiH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-09Pal.tdb): FCC_A1, type code %A, sha256 `436418f01844f2fd…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI : H VA% : !
~~~~

[NiH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-99Zen.tdb): FCC_A1, type code %A, sha256 `d480b20f77444466…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(98)00857-3](https://doi.org/10.1016/S0925-8388%2898%2900857-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, J. Alloys Compd., 283, 151-61(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_

## GAS (H–Ni)

- Id: `phase:h-ni:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(H) 0.98558–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ni:gas)

Names (4): _corpus: _corpus:phase:h-ni:gas  
_paper: _paper:10.1016/s0925-8388(98)00857-3:gas  
_tdb: _tdb:NiH-09Pal.tdb:GAS, tdb:NiH-99Zen.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[NiH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-09Pal.tdb): GAS, type code %, sha256 `436418f01844f2fd…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : NI NI2 H H2 : !
~~~~

[NiH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-99Zen.tdb): GAS, type code %, sha256 `d480b20f77444466…`

~~~~text
44: PHASE GAS:G % 1 1 !
45: CONST GAS:G : NI NI2 H H2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(98)00857-3](https://doi.org/10.1016/S0925-8388%2898%2900857-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, J. Alloys Compd., 283, 151-61(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_

## HCP_A3 (H–Ni)

- Id: `phase:h-ni:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ni:hcp-a3)

Names (3): _corpus: _corpus:phase:h-ni:hcp-a3  
_tdb: _tdb:NiH-09Pal.tdb:HCP_A3, tdb:NiH-99Zen.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NiH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-09Pal.tdb): HCP_A3, type code %A, sha256 `436418f01844f2fd…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI : H VA% : !
~~~~

[NiH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-99Zen.tdb): HCP_A3, type code %A, sha256 `d480b20f77444466…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI : H VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_
- [doi:10.1016/S0925-8388(98)00857-3](https://doi.org/10.1016/S0925-8388%2898%2900857-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, J. Alloys Compd., 283, 151-61(1999).  
_assessment that models this phase_

## LIQUID (H–Ni)

- Id: `phase:h-ni:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1726.03–2500 K, x(H) 0–0.00424
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-ni:liquid)

Names (4): _corpus: _corpus:phase:h-ni:liquid  
_paper: _paper:10.1016/s0925-8388(98)00857-3:L  
_tdb: _tdb:NiH-09Pal.tdb:LIQUID, tdb:NiH-99Zen.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NiH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-09Pal.tdb): LIQUID, type code %, sha256 `436418f01844f2fd…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : H NI : !
~~~~

[NiH-99Zen.tdb](https://orchid-project.org/data/databases/sgte-binary/NiH-99Zen.tdb): LIQUID, type code %, sha256 `d480b20f77444466…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : H NI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/S0925-8388(98)00857-3](https://doi.org/10.1016/S0925-8388%2898%2900857-3) K. Zeng, T. Klassen, W. Oelerich, R. Bormann, J. Alloys Compd., 283, 151-61(1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
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
