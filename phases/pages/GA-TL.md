# Ga–Tl phases

> Ga–Tl system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GA-TL.html · Markdown: https://data.orchid-project.org/phases/pages/GA-TL.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GA-TL) · [full JSON](https://data.orchid-project.org/phases/systems/GA-TL.json) · [Ga–Tl system page](https://data.orchid-project.org/systems/GA-TL.html) · [Markdown](https://data.orchid-project.org/phases/pages/GA-TL.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ga–Tl system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ga-tl-a11-orthorhombic); _phase:ga-tl:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.88 K, x(Tl) 0–0 | 0 | 1 |
| [BCC_A2](#phase-ga-tl-bcc-a2); _phase:ga-tl:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 506.99–2499.5 K, x(Tl) 0.99999–1 | 0 | 1 |
| [FCC_A1](#phase-ga-tl-fcc-a1); _phase:ga-tl:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ga-tl-hcp-a3); _phase:ga-tl:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–572 K, x(Tl) 1–1 | 0 | 1 |
| [LIQUID](#phase-ga-tl-liquid); _phase:ga-tl:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.88–2500 K, x(Tl) 0–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (Ga–Tl)

- Id: `phase:ga-tl:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.88 K, x(Tl) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tl:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:ga-tl:a11-orthorhombic  
_tdb: _tdb:GaTl-17Kim.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaTl-17Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTl-17Kim.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d3153766bf3da028…`

~~~~text
44: PHASE ORTHORHOMBIC_A11 % 1 1 !
45: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11661-017-4075-0](https://doi.org/10.1007/s11661-017-4075-0) Yunkyum Kim, Han Gyeol Kim, Youn-Bae Kang, George Kaptay, Joonho Lee, Prediction of Phase Separation of Immiscible Ga-Tl Alloys, Metall Mater Trans A 48, 3130-3136 (2017).  
_assessment that models this phase_

## BCC_A2 (Ga–Tl)

- Id: `phase:ga-tl:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 506.99–2499.5 K, x(Tl) 0.99999–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tl:bcc-a2)

Names (2): _corpus: _corpus:phase:ga-tl:bcc-a2  
_tdb: _tdb:GaTl-17Kim.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaTl-17Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTl-17Kim.tdb): BCC_A2, type code %B, sha256 `d3153766bf3da028…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : GA TL% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11661-017-4075-0](https://doi.org/10.1007/s11661-017-4075-0) Yunkyum Kim, Han Gyeol Kim, Youn-Bae Kang, George Kaptay, Joonho Lee, Prediction of Phase Separation of Immiscible Ga-Tl Alloys, Metall Mater Trans A 48, 3130-3136 (2017).  
_assessment that models this phase_

## FCC_A1 (Ga–Tl)

- Id: `phase:ga-tl:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tl:fcc-a1)

Names (2): _corpus: _corpus:phase:ga-tl:fcc-a1  
_tdb: _tdb:GaTl-17Kim.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaTl-17Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTl-17Kim.tdb): FCC_A1, type code %A, sha256 `d3153766bf3da028…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : GA TL : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11661-017-4075-0](https://doi.org/10.1007/s11661-017-4075-0) Yunkyum Kim, Han Gyeol Kim, Youn-Bae Kang, George Kaptay, Joonho Lee, Prediction of Phase Separation of Immiscible Ga-Tl Alloys, Metall Mater Trans A 48, 3130-3136 (2017).  
_assessment that models this phase_

## HCP_A3 (Ga–Tl)

- Id: `phase:ga-tl:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–572 K, x(Tl) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tl:hcp-a3)

Names (2): _corpus: _corpus:phase:ga-tl:hcp-a3  
_tdb: _tdb:GaTl-17Kim.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaTl-17Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTl-17Kim.tdb): HCP_A3, type code %A, sha256 `d3153766bf3da028…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : GA TL% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11661-017-4075-0](https://doi.org/10.1007/s11661-017-4075-0) Yunkyum Kim, Han Gyeol Kim, Youn-Bae Kang, George Kaptay, Joonho Lee, Prediction of Phase Separation of Immiscible Ga-Tl Alloys, Metall Mater Trans A 48, 3130-3136 (2017).  
_assessment that models this phase_

## LIQUID (Ga–Tl)

- Id: `phase:ga-tl:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.88–2500 K, x(Tl) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ga-tl:liquid)

Names (2): _corpus: _corpus:phase:ga-tl:liquid  
_tdb: _tdb:GaTl-17Kim.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaTl-17Kim.tdb](https://orchid-project.org/data/databases/sgte-binary/GaTl-17Kim.tdb): LIQUID, type code %, sha256 `d3153766bf3da028…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : GA TL : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11661-017-4075-0](https://doi.org/10.1007/s11661-017-4075-0) Yunkyum Kim, Han Gyeol Kim, Youn-Bae Kang, George Kaptay, Joonho Lee, Prediction of Phase Separation of Immiscible Ga-Tl Alloys, Metall Mater Trans A 48, 3130-3136 (2017).  
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
