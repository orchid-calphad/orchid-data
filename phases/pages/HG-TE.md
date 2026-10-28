# Hg–Te phases

> Hg–Te system: 7 phases (tier A 5, liquid 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HG-TE.html · Markdown: https://data.orchid-project.org/phases/pages/HG-TE.md

7 phases (tier A 5, liquid 2); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HG-TE) · [full JSON](https://data.orchid-project.org/phases/systems/HG-TE.json) · [Hg–Te system page](https://data.orchid-project.org/systems/HG-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/HG-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hg–Te system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBO_A10](#phase-hg-te-a10-rhombo); _phase:hg-te:a10-rhombo_ | alpha-Hg · A10 · hR1 · R-3m (166) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 3 | 2 |
| [HEXAGONAL_A8](#phase-hg-te-a8-hexagonal); _phase:hg-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 3 | 2 |
| [ZINCBLENDE_B3](#phase-hg-te-b3-zincblende); _phase:hg-te:b3-zincblende_ | ZnS (sphalerite) · B3 · cF8 · F-43m (216) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–945.31 K, x(Te) 0.5–0.5 | 9 | 2 |
| [FCC_A1](#phase-hg-te-fcc-a1); _phase:hg-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-hg-te-hcp-a3); _phase:hg-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [ION](#phase-hg-te-ion); _phase:hg-te:ion_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Te) 0–1 | 0 | 1 |
| [LIQUID](#phase-hg-te-liquid); _phase:hg-te:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Te) 0–1 | 21 | 2 |

## RHOMBO_A10 (Hg–Te)

- Id: `phase:hg-te:a10-rhombo`; status `assigned`
- Structure: alpha-Hg · A10 · hR1 · R-3m (166); type `st:a10-alpha-hg-hr1`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:a10-rhombo)

Names (4): _corpus: _corpus:phase:hg-te:a10-rhombo  
_paper: _paper:10.1016/j.jallcom.2010.01.003:Hg  
_tdb: _tdb:HgTe-10Gie.tdb:RHOMBO_A10, tdb:HgTe-95Yan-LB.tdb:RHOMBO_A10  


### TDB models of RHOMBO_A10 (2): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): RHOMBO_A10, type code %, sha256 `c1efc80be4426d7d…`

~~~~text
55: PHASE RHOMBO_A10 % 1 1 !
56: CONST RHOMBO_A10 : HG : !
~~~~

[HgTe-95Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb): RHOMBO_A10, type code %, sha256 `d35628e6d9da010c…`

~~~~text
47: PHASE RHOMBO_A10 % 1 1 !
48: CONST RHOMBO_A10 : HG : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_

## HEXAGONAL_A8 (Hg–Te)

- Id: `phase:hg-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:a8-hexagonal)

Names (5): _corpus: _corpus:phase:hg-te:a8-hexagonal, corpus:phase:hg-te:hexagonal-a8  
_paper: _paper:10.1016/j.jallcom.2010.01.003:Te  
_tdb: _tdb:HgTe-10Gie.tdb:HEXAGONAL_A8, tdb:HgTe-95Yan-LB.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (2): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): HEXAGONAL_A8, type code %, sha256 `c1efc80be4426d7d…`

~~~~text
50: PHASE HEXAGONAL_A8 % 1 1 !
51: CONST HEXAGONAL_A8 : TE : !
~~~~

[HgTe-95Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb): HEXAGONAL_A8, type code %, sha256 `d35628e6d9da010c…`

~~~~text
42: PHASE HEXAGONAL_A8 % 1 1 !
43: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_

## ZINCBLENDE_B3 (Hg–Te)

- Id: `phase:hg-te:b3-zincblende`; status `assigned`
- Structure: ZnS (sphalerite) · B3 · cF8 · F-43m (216); type `st:b3-zns-sphalerite-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 0.5000, Te 0.5000
- Stability: stable in 2 of 2 calculated diagram(s): 300–945.31 K, x(Te) 0.5–0.5
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:b3-zincblende)

Names (5): _corpus: _corpus:phase:hg-te:b3-zincblende, corpus:phase:hg-te:zincblende-b3  
_paper: _paper:10.1016/j.jallcom.2010.01.003:HgTe  
_tdb: _tdb:HgTe-10Gie.tdb:ZINCBLENDE_B3, tdb:HgTe-95Yan-LB.tdb:ZINCBLENDE_B3  


### TDB models of ZINCBLENDE_B3 (2): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): ZINCBLENDE_B3, type code %, sha256 `c1efc80be4426d7d…`

~~~~text
60: PHASE ZINCBLENDE_B3 % 2 1 1 !
61: CONST ZINCBLENDE_B3 : HG : TE : !
~~~~

[HgTe-95Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb): ZINCBLENDE_B3, type code %, sha256 `d35628e6d9da010c…`

~~~~text
52: PHASE ZINCBLENDE_B3 % 2 1 1 !
53: CONST ZINCBLENDE_B3 : HG : TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_

## FCC_A1 (Hg–Te)

- Id: `phase:hg-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:fcc-a1)

Names (3): _corpus: _corpus:phase:hg-te:fcc-a1  
_tdb: _tdb:HgTe-10Gie.tdb:FCC_A1, tdb:HgTe-95Yan-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): FCC_A1, type code %A, sha256 `c1efc80be4426d7d…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : HG : VA : !
~~~~

[HgTe-95Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb): FCC_A1, type code %A, sha256 `d35628e6d9da010c…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : HG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase_

## HCP_A3 (Hg–Te)

- Id: `phase:hg-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Hg 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:hcp-a3)

Names (3): _corpus: _corpus:phase:hg-te:hcp-a3  
_tdb: _tdb:HgTe-10Gie.tdb:HCP_A3, tdb:HgTe-95Yan-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): HCP_A3, type code %A, sha256 `c1efc80be4426d7d…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : HG : VA : !
~~~~

[HgTe-95Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb): HCP_A3, type code %A, sha256 `d35628e6d9da010c…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : HG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase_

## ION (Hg–Te)

- Id: `phase:hg-te:ion`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:ion)

Names (2): _corpus: _corpus:phase:hg-te:ion  
_tdb: _tdb:HgTe-10Gie.tdb:ION  


### TDB models of ION (1): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): ION, type code %, sha256 `c1efc80be4426d7d…`

~~~~text
33: PHASE ION:Y % 2 1 1 !
34: CONST ION:Y : HG+2 : TE-2 TE VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase_

## LIQUID (Hg–Te)

- Id: `phase:hg-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2500 K, x(Te) 0–1
- Literature: 21 values (21 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hg-te:liquid)

Names (6): _corpus: _corpus:phase:hg-te:liquid  
_paper: _paper:10.1016/0364-5916(95)00038-g:liquid, paper:10.1016/j.jallcom.2010.01.003:L, paper:10.1016/j.jallcom.2010.01.003:liquid  
_tdb: _tdb:HgTe-10Gie.tdb:LIQUID, tdb:HgTe-95Yan-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[HgTe-10Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-10Gie.tdb): LIQUID, type code %, sha256 `c1efc80be4426d7d…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : HG HGTE TE : !
~~~~

[HgTe-95Yan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/HgTe-95Yan-LB.tdb): LIQUID, type code %, sha256 `d35628e6d9da010c…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : HG HGTE TE : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(95)00038-G](https://doi.org/10.1016/0364-5916%2895%2900038-G) J. Yang, N.J. Silk, A. Watson, A.W. Bryant, B.B. Argent, Calphad, 19, 399-414(1995).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2010.01.003](https://doi.org/10.1016/j.jallcom.2010.01.003) Wojciech Gierlotka, Thermodynamic description of the Hg–Te binary system, Journal of Alloys and Compounds 494, 102-108 (2010).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23735970
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.23736065

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23735970},
  url       = {https://doi.org/10.5281/zenodo.23735970},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.23736065},
  url       = {https://doi.org/10.5281/zenodo.23736065},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
