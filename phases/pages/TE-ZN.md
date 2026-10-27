# Te–Zn phases

> Te–Zn system: 5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/TE-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/TE-ZN.md

5 phases (tier A 3, liquid 1, gas 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=TE-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/TE-ZN.json) · [Te–Zn system page](https://data.orchid-project.org/systems/TE-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/TE-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Te–Zn system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-te-zn-a8-hexagonal); _phase:te-zn:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 1 |
| [GAS](#phase-te-zn-gas); _phase:te-zn:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 1179.76–2500 K, x(Te) 0–1 | 0 | 1 |
| [HCP_A3](#phase-te-zn-hcp-a3); _phase:te-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Te) 0–0 | 0 | 1 |
| [LIQUID](#phase-te-zn-liquid); _phase:te-zn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Te) 0–1 | 8 | 1 |
| [ZNTE_B3](#phase-te-zn-znte-b3); _phase:te-zn:znte-b3_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |

## HEXAGONAL_A8 (Te–Zn)

- Id: `phase:te-zn:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zn:a8-hexagonal)

Names (2): _corpus: _corpus:phase:te-zn:a8-hexagonal  
_tdb: _tdb:ZnTe-97Feu-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[ZnTe-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnTe-97Feu-LB.tdb): HEXAGONAL_A8, type code %, sha256 `78ae5ced43382c8d…`

~~~~text
40: PHASE HEXAGONAL_A8 % 1 1 !
41: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646758](https://doi.org/10.1007/BF02646758) Y. Feutelais, A. Haloui, B. Legendre, J. Phase Equilib., 18, 48-61(1997).  
_assessment that models this phase_

## GAS (Te–Zn)

- Id: `phase:te-zn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1179.76–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zn:gas)

Names (2): _corpus: _corpus:phase:te-zn:gas  
_tdb: _tdb:ZnTe-97Feu-LB.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[ZnTe-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnTe-97Feu-LB.tdb): GAS, type code %, sha256 `78ae5ced43382c8d…`

~~~~text
48: PHASE GAS:G % 1 1 !
49: CONST GAS:G : TE TE2 TE3 TE4 TE5 TE6 TE7 ZNTE ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646758](https://doi.org/10.1007/BF02646758) Y. Feutelais, A. Haloui, B. Legendre, J. Phase Equilib., 18, 48-61(1997).  
_assessment that models this phase_

## HCP_A3 (Te–Zn)

- Id: `phase:te-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Zn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zn:hcp-a3)

Names (2): _corpus: _corpus:phase:te-zn:hcp-a3  
_tdb: _tdb:ZnTe-97Feu-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ZnTe-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnTe-97Feu-LB.tdb): HCP_A3, type code %A, sha256 `78ae5ced43382c8d…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646758](https://doi.org/10.1007/BF02646758) Y. Feutelais, A. Haloui, B. Legendre, J. Phase Equilib., 18, 48-61(1997).  
_assessment that models this phase_

## LIQUID (Te–Zn)

- Id: `phase:te-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2498.93 K, x(Te) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zn:liquid)

Names (3): _corpus: _corpus:phase:te-zn:liquid  
_paper: _paper:10.1007/bf02646758:liquid  
_tdb: _tdb:ZnTe-97Feu-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ZnTe-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnTe-97Feu-LB.tdb): LIQUID, type code %, sha256 `78ae5ced43382c8d…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : TE ZN ZNTE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646758](https://doi.org/10.1007/BF02646758) Y. Feutelais, A. Haloui, B. Legendre, J. Phase Equilib., 18, 48-61(1997).  
_assessment that models this phase; reports values for this phase_

## ZNTE_B3 (Te–Zn)

- Id: `phase:te-zn:znte-b3`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadfs and oqmd-1277630, space group 216
- Stoichiometry: Te 0.5000, Zn 0.5000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:te-zn:znte-b3)

Names (4): _corpus: _corpus:phase:te-zn:znte-b3  
_mp: _mp:mp-aaaaadfs  
_oqmd: _oqmd:oqmd-1277630  
_tdb: _tdb:ZnTe-97Feu-LB.tdb:ZNTE_B3  


### TDB models of ZNTE_B3 (1): PHASE and CONSTITUENT statements as written

[ZnTe-97Feu-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/ZnTe-97Feu-LB.tdb): ZNTE_B3, type code %, sha256 `78ae5ced43382c8d…`

~~~~text
45: PHASE ZNTE_B3 % 2 1 1 !
46: CONST ZNTE_B3 : ZN : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/BF02646758](https://doi.org/10.1007/BF02646758) Y. Feutelais, A. Haloui, B. Legendre, J. Phase Equilib., 18, 48-61(1997).  
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
