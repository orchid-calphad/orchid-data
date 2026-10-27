# Au–Ge phases

> Au–Ge system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AU-GE.html · Markdown: https://data.orchid-project.org/phases/pages/AU-GE.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AU-GE) · [full JSON](https://data.orchid-project.org/phases/systems/AU-GE.json) · [Au–Ge system page](https://data.orchid-project.org/systems/AU-GE.html) · [Markdown](https://data.orchid-project.org/phases/pages/AU-GE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Au–Ge system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-au-ge-a4-diamond); _phase:au-ge:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1 | 6 | 2 |
| [BCC_A2](#phase-au-ge-bcc-a2); _phase:au-ge:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-au-ge-fcc-a1); _phase:au-ge:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1361.58 K, x(Ge) 0–0.03309 | 6 | 2 |
| [HCP_A3](#phase-au-ge-hcp-a3); _phase:au-ge:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-au-ge-liquid); _phase:au-ge:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 630.2–2500 K, x(Ge) 0–1 | 6 | 2 |

## DIAMOND_A4 (Au–Ge)

- Id: `phase:au-ge:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Ge 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1211.4 K, x(Ge) 1–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ge:a4-diamond)

Names (4): _corpus: _corpus:phase:au-ge:a4-diamond  
_paper: _paper:10.1016/j.jallcom.2009.03.114:diamond_A4  
_tdb: _tdb:AuGe-09Wan.tdb:DIAMOND_A4, tdb:AuGe-89Che-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[AuGe-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-09Wan.tdb): DIAMOND_A4, type code %, sha256 `8bbcae88b81042e5…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : GE : !
~~~~

[AuGe-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-89Che-LB.tdb): DIAMOND_A4, type code %, sha256 `a6d58cb0d20f1858…`

~~~~text
43: PHASE DIAMOND_A4 % 1 1 !
44: CONST DIAMOND_A4 : GE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114) J. Wang, C. Leinenbach, M. Roth, Thermodynamic modeling of the Au–Ge–Sn ternary system, Journal of Alloys and Compounds 481, 830-836 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254) S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (Au–Ge)

- Id: `phase:au-ge:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ge:bcc-a2)

Names (3): _corpus: _corpus:phase:au-ge:bcc-a2  
_tdb: _tdb:AuGe-09Wan.tdb:BCC_A2, tdb:AuGe-89Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AuGe-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-09Wan.tdb): BCC_A2, type code %B, sha256 `8bbcae88b81042e5…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : AU GE : VA : !
~~~~

[AuGe-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-89Che-LB.tdb): BCC_A2, type code %B, sha256 `a6d58cb0d20f1858…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AU GE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114) J. Wang, C. Leinenbach, M. Roth, Thermodynamic modeling of the Au–Ge–Sn ternary system, Journal of Alloys and Compounds 481, 830-836 (2009).  
_assessment that models this phase_

## FCC_A1 (Au–Ge)

- Id: `phase:au-ge:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1361.58 K, x(Ge) 0–0.03309
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ge:fcc-a1)

Names (4): _corpus: _corpus:phase:au-ge:fcc-a1  
_paper: _paper:10.1016/j.jallcom.2009.03.114:fcc_A1  
_tdb: _tdb:AuGe-09Wan.tdb:FCC_A1, tdb:AuGe-89Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AuGe-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-09Wan.tdb): FCC_A1, type code %A, sha256 `8bbcae88b81042e5…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : AU% GE : VA : !
~~~~

[AuGe-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-89Che-LB.tdb): FCC_A1, type code %A, sha256 `a6d58cb0d20f1858…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AU% GE : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114) J. Wang, C. Leinenbach, M. Roth, Thermodynamic modeling of the Au–Ge–Sn ternary system, Journal of Alloys and Compounds 481, 830-836 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254) S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_

## HCP_A3 (Au–Ge)

- Id: `phase:au-ge:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ge:hcp-a3)

Names (3): _corpus: _corpus:phase:au-ge:hcp-a3  
_tdb: _tdb:AuGe-09Wan.tdb:HCP_A3, tdb:AuGe-89Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AuGe-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-09Wan.tdb): HCP_A3, type code %A, sha256 `8bbcae88b81042e5…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : AU GE : VA : !
~~~~

[AuGe-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-89Che-LB.tdb): HCP_A3, type code %A, sha256 `a6d58cb0d20f1858…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AU GE : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114) J. Wang, C. Leinenbach, M. Roth, Thermodynamic modeling of the Au–Ge–Sn ternary system, Journal of Alloys and Compounds 481, 830-836 (2009).  
_assessment that models this phase_

## LIQUID (Au–Ge)

- Id: `phase:au-ge:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 630.2–2500 K, x(Ge) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:au-ge:liquid)

Names (4): _corpus: _corpus:phase:au-ge:liquid  
_paper: _paper:10.1016/j.jallcom.2009.03.114:L  
_tdb: _tdb:AuGe-09Wan.tdb:LIQUID, tdb:AuGe-89Che-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AuGe-09Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-09Wan.tdb): LIQUID, type code %, sha256 `8bbcae88b81042e5…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : AU GE : !
~~~~

[AuGe-89Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AuGe-89Che-LB.tdb): LIQUID, type code %, sha256 `a6d58cb0d20f1858…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AU GE : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/j.jallcom.2009.03.114](https://doi.org/10.1016/j.jallcom.2009.03.114) J. Wang, C. Leinenbach, M. Roth, Thermodynamic modeling of the Au–Ge–Sn ternary system, Journal of Alloys and Compounds 481, 830-836 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(89)87056-X](https://doi.org/10.1016/0040-6031%2889%2987056-X) P.-Y. Chevalier, Thermochim. Acta, 141, 217-26(1989).  
_assessment that models this phase; cited as the source of values for this phase_
- [doi:10.1007/bf02649254](https://doi.org/10.1007/bf02649254) S. Hassam, M. Gambino, M. Gaune-escard, J.P. Bros, J. ågren, Experimental and Calculated Ag + Au + Ge Phase Diagram, Metall Trans A 19, 409-416 (1988).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
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
