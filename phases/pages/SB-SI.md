# Sb–Si phases

> Sb–Si system: 3 phases (tier A 2, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SB-SI.html · Markdown: https://data.orchid-project.org/phases/pages/SB-SI.md

3 phases (tier A 2, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SB-SI) · [full JSON](https://data.orchid-project.org/phases/systems/SB-SI.json) · [Sb–Si system page](https://data.orchid-project.org/systems/SB-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/SB-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sb–Si system (3)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-sb-si-a4-diamond); _phase:sb-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1686.95 K, x(Si) 0.99896–1 | 0 | 2 |
| [RHOMBOHEDRAL_A7](#phase-sb-si-a7-rhombohedral); _phase:sb-si:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Si) 0–0 | 0 | 2 |
| [LIQUID](#phase-sb-si-liquid); _phase:sb-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 902.71–2500 K, x(Si) 0–1 | 29 | 2 |

## DIAMOND_A4 (Sb–Si)

- Id: `phase:sb-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1686.95 K, x(Si) 0.99896–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-si:a4-diamond)

Names (3): _corpus: _corpus:phase:sb-si:a4-diamond  
_tdb: _tdb:SbSi-11Wan.tdb:DIAMOND_A4, tdb:SbSi-85Ole-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[SbSi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSi-11Wan.tdb): DIAMOND_A4, type code %, sha256 `92ed80bc14bc6afe…`

~~~~text
25: PHASE DIAMOND_A4 % 1 1 !
26: CONST DIAMOND_A4 : SB SI% : !
~~~~

[SbSi-85Ole-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSi-85Ole-LB.tdb): DIAMOND_A4, type code %, sha256 `74004a1d293e3fd1…`

~~~~text
26: PHASE DIAMOND_A4 % 1 1 !
27: CONST DIAMOND_A4 : SB SI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02869508](https://doi.org/10.1007/BF02869508) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 445-48(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_

## RHOMBOHEDRAL_A7 (Sb–Si)

- Id: `phase:sb-si:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stoichiometry: Sb 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–903.78 K, x(Si) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-si:a7-rhombohedral)

Names (3): _corpus: _corpus:phase:sb-si:a7-rhombohedral  
_tdb: _tdb:SbSi-11Wan.tdb:RHOMBOHEDRAL_A7, tdb:SbSi-85Ole-LB.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (2): PHASE and CONSTITUENT statements as written

[SbSi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSi-11Wan.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `92ed80bc14bc6afe…`

~~~~text
30: PHASE RHOMBOHEDRAL_A7 % 1 1 !
31: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

[SbSi-85Ole-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSi-85Ole-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `74004a1d293e3fd1…`

~~~~text
31: PHASE RHOMBOHEDRAL_A7 % 1 1 !
32: CONST RHOMBOHEDRAL_A7 : SB : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02869508](https://doi.org/10.1007/BF02869508) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 445-48(1985).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase_

## LIQUID (Sb–Si)

- Id: `phase:sb-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 902.71–2500 K, x(Si) 0–1
- Literature: 29 values (26 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sb-si:liquid)

Names (5): _corpus: _corpus:phase:sb-si:liquid  
_paper: _paper:10.1007/bf02869508:L, paper:10.1016/j.jallcom.2010.11.199:L  
_tdb: _tdb:SbSi-11Wan.tdb:LIQUID, tdb:SbSi-85Ole-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[SbSi-11Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSi-11Wan.tdb): LIQUID, type code %, sha256 `92ed80bc14bc6afe…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : SB SI : !
~~~~

[SbSi-85Ole-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/SbSi-85Ole-LB.tdb): LIQUID, type code %, sha256 `74004a1d293e3fd1…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SB SI : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1007/BF02869508](https://doi.org/10.1007/BF02869508) R.W. Olesinski, G.J. Abbaschian, Bull. Alloy Phase Diag., 6, 445-48(1985).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.11.199](https://doi.org/10.1016/j.jallcom.2010.11.199) J. Wang, Y.J. Liu, L.B. Liu, H.Y. Zhou, Z.P. Jin, Thermodynamic modeling of the Au–Sb–Si ternary system, Journal of Alloys and Compounds 509, 3057-3064 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1002/j.1538-7305.1960.tb03927.x](https://doi.org/10.1002/j.1538-7305.1960.tb03927.x) C. D. Thurmond, M. Kowalchik, Germanium and Silicon Liquidus Curves, Bell System Technical Journal 39, 169-204 (1960).  
_cited as the source of values for this phase_
- [doi:10.1002/zaac.19070550102](https://doi.org/10.1002/zaac.19070550102) Robert S. Williams, LI. Über die Legierungen des Antimons mit Mangan, Chrom, Silicium und Zinn; des Wismuts mit Chrom und Silicium und des Mangans mit Zinn und Blei, Z. Anorg. Chem. 55, 1-33 (1907).  
_cited as the source of values for this phase_
- [doi:10.1021/j150509a019](https://doi.org/10.1021/j150509a019) Carl D. Thurmond, Equilibrium Thermochemistry of Solid and Liquid Alloys of Germanium and of Silicon. I. The Solubility of Ge and Si in Elements of Groups III, IV and V, J. Phys. Chem. 57, 827-830 (1953).  
_cited as the source of values for this phase_

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
