# H–La phases

> H–La system: 6 phases (tier A 3, tier C 1, liquid 1, gas 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/H-LA.html · Markdown: https://data.orchid-project.org/phases/pages/H-LA.md

6 phases (tier A 3, tier C 1, liquid 1, gas 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=H-LA) · [full JSON](https://data.orchid-project.org/phases/systems/H-LA.json) · [H–La system page](https://data.orchid-project.org/systems/H-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/H-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the H–La system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-h-la-bcc-a2); _phase:h-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1052.65–1382.5 K, x(H) 0–0.48649 | 0 | 1 |
| [DHCP](#phase-h-la-dhcp-a3); _phase:h-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1164.99 K, x(H) 0–0 | 0 | 1 |
| [FCC_A1](#phase-h-la-fcc-a1); _phase:h-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 532.94–1164.99 K, x(H) 0–0.20935 | 0 | 1 |
| [GAS](#phase-h-la-gas); _phase:h-la:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 0.99977–1 | 0 | 1 |
| [LAH2](#phase-h-la-lah2); _phase:h-la:lah2_ | CeH3 · cF44 · Fm-3m (225) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1363.04 K, x(H) 0.64536–0.74999 | 2 | 1 |
| [LIQUID](#phase-h-la-liquid); _phase:h-la:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1193.01–2500 K, x(H) 0–0.45272 | 0 | 1 |

## BCC_A2 (H–La)

- Id: `phase:h-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1052.65–1382.5 K, x(H) 0–0.48649
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-la:bcc-a2)

Names (2): _corpus: _corpus:phase:h-la:bcc-a2  
_tdb: _tdb:LaH-09Pal.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[LaH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/LaH-09Pal.tdb): BCC_A2, type code %B, sha256 `bb8224faf2d8e5ac…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : LA : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_

## DHCP (H–La)

- Id: `phase:h-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1164.99 K, x(H) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-la:dhcp-a3)

Names (2): _corpus: _corpus:phase:h-la:dhcp-a3  
_tdb: _tdb:LaH-09Pal.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[LaH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/LaH-09Pal.tdb): DHCP, type code %, sha256 `bb8224faf2d8e5ac…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_

## FCC_A1 (H–La)

- Id: `phase:h-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 532.94–1164.99 K, x(H) 0–0.20935
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-la:fcc-a1)

Names (2): _corpus: _corpus:phase:h-la:fcc-a1  
_tdb: _tdb:LaH-09Pal.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[LaH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/LaH-09Pal.tdb): FCC_A1, type code %A, sha256 `bb8224faf2d8e5ac…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : LA : H VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_

## GAS (H–La)

- Id: `phase:h-la:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 0.99977–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-la:gas)

Names (2): _corpus: _corpus:phase:h-la:gas  
_tdb: _tdb:LaH-09Pal.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[LaH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/LaH-09Pal.tdb): GAS, type code %, sha256 `bb8224faf2d8e5ac…`

~~~~text
49: PHASE GAS:G % 1 1 !
50: CONST GAS:G : LA H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase_

## LAH2 (H–La)

- Id: `phase:h-la:lah2`; status `assigned`
- Structure: CeH3 · cF44 · Fm-3m (225); type `st:ceh3-cf44`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1363.04 K, x(H) 0.64536–0.74999
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-la:lah2)

Names (3): _corpus: _corpus:phase:h-la:lah2  
_paper: _paper:10.1016/j.calphad.2008.09.003:LaH2  
_tdb: _tdb:LaH-09Pal.tdb:LAH2  


### TDB models of LAH2 (1): PHASE and CONSTITUENT statements as written

[LaH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/LaH-09Pal.tdb): LAH2, type code %, sha256 `bb8224faf2d8e5ac…`

~~~~text
46: PHASE LAH2 % 3 1 2 1 !
47: CONST LAH2 : LA : H VA : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
_assessment that models this phase; reports values for this phase_

## LIQUID (H–La)

- Id: `phase:h-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1193.01–2500 K, x(H) 0–0.45272
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:h-la:liquid)

Names (2): _corpus: _corpus:phase:h-la:liquid  
_tdb: _tdb:LaH-09Pal.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[LaH-09Pal.tdb](https://orchid-project.org/data/databases/sgte-binary/LaH-09Pal.tdb): LIQUID, type code %, sha256 `bb8224faf2d8e5ac…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : H LA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2008.09.003](https://doi.org/10.1016/j.calphad.2008.09.003) M. Palumbo, J. Urgnani, D. Baldissin, L. Battezzati, M. Baricco, Thermodynamic assessment of the H–La–Ni system, Calphad 33, 162-169 (2009).  
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
