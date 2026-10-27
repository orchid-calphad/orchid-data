# Cd–Ge phases

> Cd–Ge system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-GE.html · Markdown: https://data.orchid-project.org/phases/pages/CD-GE.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-GE) · [full JSON](https://data.orchid-project.org/phases/systems/CD-GE.json) · [Cd–Ge system page](https://data.orchid-project.org/systems/CD-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Ge system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-cd-ge-a4-diamond); _phase:cd-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1 | 0 | 2 |
| [BCC_A2](#phase-cd-ge-bcc-a2); _phase:cd-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-cd-ge-fcc-a1); _phase:cd-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cd-ge-hcp-a3); _phase:cd-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–594.22 K, x(Ge) 0–0 | 0 | 2 |
| [LIQUID](#phase-cd-ge-liquid); _phase:cd-ge:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 592.96–2500 K, x(Ge) 0–1 | 0 | 2 |

## DIAMOND_A4 (Cd–Ge)

- Id: `phase:cd-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ge:a4-diamond)

Names (3): _corpus: _corpus:phase:cd-ge:a4-diamond  
_tdb: _tdb:CdGe-00Dic-LB.tdb:DIAMOND_A4, tdb:CdGe-01Dic.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[CdGe-00Dic-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-00Dic-LB.tdb): DIAMOND_A4, type code %, sha256 `605fc90f02aa6a6b…`

~~~~text
54: PHASE DIAMOND_A4 % 1 1 !
55: CONST DIAMOND_A4 : GE : !
~~~~

[CdGe-01Dic.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-01Dic.tdb): DIAMOND_A4, type code %, sha256 `44d7e7fbe1053a99…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-2001-0196](https://doi.org/10.3139/ijmr-2001-0196) E. Dichi, G. Morgant, B. Legendre, S.G. Fries, Z. Metallkd. 92, 1078-82(2001).  
_assessment that models this phase_

## BCC_A2 (Cd–Ge)

- Id: `phase:cd-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ge:bcc-a2)

Names (3): _corpus: _corpus:phase:cd-ge:bcc-a2  
_tdb: _tdb:CdGe-00Dic-LB.tdb:BCC_A2, tdb:CdGe-01Dic.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CdGe-00Dic-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-00Dic-LB.tdb): BCC_A2, type code %B, sha256 `605fc90f02aa6a6b…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : CD GE : VA : !
~~~~

[CdGe-01Dic.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-01Dic.tdb): BCC_A2, type code %B, sha256 `44d7e7fbe1053a99…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CD GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-2001-0196](https://doi.org/10.3139/ijmr-2001-0196) E. Dichi, G. Morgant, B. Legendre, S.G. Fries, Z. Metallkd. 92, 1078-82(2001).  
_assessment that models this phase_

## FCC_A1 (Cd–Ge)

- Id: `phase:cd-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ge:fcc-a1)

Names (3): _corpus: _corpus:phase:cd-ge:fcc-a1  
_tdb: _tdb:CdGe-00Dic-LB.tdb:FCC_A1, tdb:CdGe-01Dic.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CdGe-00Dic-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-00Dic-LB.tdb): FCC_A1, type code %A, sha256 `605fc90f02aa6a6b…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : CD GE : VA : !
~~~~

[CdGe-01Dic.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-01Dic.tdb): FCC_A1, type code %A, sha256 `44d7e7fbe1053a99…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CD GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-2001-0196](https://doi.org/10.3139/ijmr-2001-0196) E. Dichi, G. Morgant, B. Legendre, S.G. Fries, Z. Metallkd. 92, 1078-82(2001).  
_assessment that models this phase_

## HCP_A3 (Cd–Ge)

- Id: `phase:cd-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–594.22 K, x(Ge) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ge:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-ge:hcp-a3  
_tdb: _tdb:CdGe-00Dic-LB.tdb:HCP_A3, tdb:CdGe-01Dic.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CdGe-00Dic-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-00Dic-LB.tdb): HCP_A3, type code %A, sha256 `605fc90f02aa6a6b…`

~~~~text
49: PHASE HCP_A3 %A 2 1 0.5 !
50: CONST HCP_A3 : CD% GE : VA : !
~~~~

[CdGe-01Dic.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-01Dic.tdb): HCP_A3, type code %A, sha256 `44d7e7fbe1053a99…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CD% GE : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-2001-0196](https://doi.org/10.3139/ijmr-2001-0196) E. Dichi, G. Morgant, B. Legendre, S.G. Fries, Z. Metallkd. 92, 1078-82(2001).  
_assessment that models this phase_

## LIQUID (Cd–Ge)

- Id: `phase:cd-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 592.96–2500 K, x(Ge) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-ge:liquid)

Names (3): _corpus: _corpus:phase:cd-ge:liquid  
_tdb: _tdb:CdGe-00Dic-LB.tdb:LIQUID, tdb:CdGe-01Dic.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CdGe-00Dic-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-00Dic-LB.tdb): LIQUID, type code %, sha256 `605fc90f02aa6a6b…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : CD GE : !
~~~~

[CdGe-01Dic.tdb](https://orchid-project.org/data/databases/sgte-binary/CdGe-01Dic.tdb): LIQUID, type code %, sha256 `44d7e7fbe1053a99…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CD GE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/ijmr-2001-0196](https://doi.org/10.3139/ijmr-2001-0196) E. Dichi, G. Morgant, B. Legendre, S.G. Fries, Z. Metallkd. 92, 1078-82(2001).  
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
