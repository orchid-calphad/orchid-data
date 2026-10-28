# Y–Zr phases

> Y–Zr system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/Y-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/Y-ZR.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=Y-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/Y-ZR.json) · [Y–Zr system page](https://data.orchid-project.org/systems/Y-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/Y-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Y–Zr system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-y-zr-bcc-a2); _phase:y-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300.26–3999.1 K, x(Zr) 0–1 | 8 | 3 |
| [FCC_A1](#phase-y-zr-fcc-a1); _phase:y-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-y-zr-hcp-a3); _phase:y-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1812.88 K, x(Zr) 0–1 | 8 | 3 |
| [LIQUID](#phase-y-zr-liquid); _phase:y-zr:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1589.25–4000 K, x(Zr) 0–1 | 5 | 3 |

## BCC_A2 (Y–Zr)

- Id: `phase:y-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300.26–3999.1 K, x(Zr) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:y-zr:bcc-a2)

Names (6): _corpus: _corpus:phase:y-zr:bcc-a2  
_paper: _paper:10.2298/jmmb1002181b:(βY), paper:10.2298/jmmb1002181b:(βZr)  
_tdb: _tdb:YZr-09He.tdb:BCC_A2, tdb:YZr-10Bu.tdb:BCC_A2, tdb:YZr-97Fla-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[YZr-09He.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-09He.tdb): BCC_A2, type code %B, sha256 `91a0a0fad9c17ef4…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : Y% ZR% : VA : !
~~~~

[YZr-10Bu.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-10Bu.tdb): BCC_A2, type code %B, sha256 `9ed09585bcfb5315…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : Y% ZR% : VA : !
~~~~

[YZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-97Fla-LB.tdb): BCC_A2, type code %B, sha256 `67e490b92eec3d7f…`

~~~~text
44: PHASE BCC_A2 %B 2 1 3 !
45: CONST BCC_A2 : Y% ZR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB1002181B](https://doi.org/10.2298/JMMB1002181B) M.J. Bu, P.S. Wang, H.H. Xu, S.H. Liu, C.S. Shu, Y. Du, F.S. Pan, A.T. Tang, J. Min. Metall. B, 46, 181-92(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.07.144](https://doi.org/10.1016/j.jallcom.2008.07.144) X.C. He, H.S. Liu, Determination of the isothermal section of the Cu–Zr–Y ternary system at 978K, Journal of Alloys and Compounds 475, 245-251 (2009).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## FCC_A1 (Y–Zr)

- Id: `phase:y-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:y-zr:fcc-a1)

Names (4): _corpus: _corpus:phase:y-zr:fcc-a1  
_tdb: _tdb:YZr-09He.tdb:FCC_A1, tdb:YZr-10Bu.tdb:FCC_A1, tdb:YZr-97Fla-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[YZr-09He.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-09He.tdb): FCC_A1, type code %A, sha256 `91a0a0fad9c17ef4…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : Y ZR : VA : !
~~~~

[YZr-10Bu.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-10Bu.tdb): FCC_A1, type code %A, sha256 `9ed09585bcfb5315…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : Y ZR : VA : !
~~~~

[YZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-97Fla-LB.tdb): FCC_A1, type code %A, sha256 `67e490b92eec3d7f…`

~~~~text
39: PHASE FCC_A1 %A 2 1 1 !
40: CONST FCC_A1 : Y ZR : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2008.07.144](https://doi.org/10.1016/j.jallcom.2008.07.144) X.C. He, H.S. Liu, Determination of the isothermal section of the Cu–Zr–Y ternary system at 978K, Journal of Alloys and Compounds 475, 245-251 (2009).  
_assessment that models this phase_
- [doi:10.2298/JMMB1002181B](https://doi.org/10.2298/JMMB1002181B) M.J. Bu, P.S. Wang, H.H. Xu, S.H. Liu, C.S. Shu, Y. Du, F.S. Pan, A.T. Tang, J. Min. Metall. B, 46, 181-92(2010).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## HCP_A3 (Y–Zr)

- Id: `phase:y-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1812.88 K, x(Zr) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:y-zr:hcp-a3)

Names (6): _corpus: _corpus:phase:y-zr:hcp-a3  
_paper: _paper:10.2298/jmmb1002181b:(αY), paper:10.2298/jmmb1002181b:(αZr)  
_tdb: _tdb:YZr-09He.tdb:HCP_A3, tdb:YZr-10Bu.tdb:HCP_A3, tdb:YZr-97Fla-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[YZr-09He.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-09He.tdb): HCP_A3, type code %, sha256 `91a0a0fad9c17ef4…`

~~~~text
46: PHASE HCP_A3 % 2 1 0.5 !
47: CONST HCP_A3 : Y% ZR% : VA : !
~~~~

[YZr-10Bu.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-10Bu.tdb): HCP_A3, type code %, sha256 `9ed09585bcfb5315…`

~~~~text
42: PHASE HCP_A3 % 2 1 0.5 !
43: CONST HCP_A3 : Y% ZR% : VA : !
~~~~

[YZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-97Fla-LB.tdb): HCP_A3, type code %, sha256 `67e490b92eec3d7f…`

~~~~text
49: PHASE HCP_A3 % 2 1 0.5 !
50: CONST HCP_A3 : Y% ZR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB1002181B](https://doi.org/10.2298/JMMB1002181B) M.J. Bu, P.S. Wang, H.H. Xu, S.H. Liu, C.S. Shu, Y. Du, F.S. Pan, A.T. Tang, J. Min. Metall. B, 46, 181-92(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.07.144](https://doi.org/10.1016/j.jallcom.2008.07.144) X.C. He, H.S. Liu, Determination of the isothermal section of the Cu–Zr–Y ternary system at 978K, Journal of Alloys and Compounds 475, 245-251 (2009).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

## LIQUID (Y–Zr)

- Id: `phase:y-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1589.25–4000 K, x(Zr) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:y-zr:liquid)

Names (5): _corpus: _corpus:phase:y-zr:liquid  
_paper: _paper:10.2298/jmmb1002181b:L  
_tdb: _tdb:YZr-09He.tdb:LIQUID, tdb:YZr-10Bu.tdb:LIQUID, tdb:YZr-97Fla-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[YZr-09He.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-09He.tdb): LIQUID, type code %, sha256 `91a0a0fad9c17ef4…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : Y ZR : !
~~~~

[YZr-10Bu.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-10Bu.tdb): LIQUID, type code %, sha256 `9ed09585bcfb5315…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : Y ZR : !
~~~~

[YZr-97Fla-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/YZr-97Fla-LB.tdb): LIQUID, type code %, sha256 `67e490b92eec3d7f…`

~~~~text
34: PHASE LIQUID:L % 1 1 !
35: CONST LIQUID:L : Y ZR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.2298/JMMB1002181B](https://doi.org/10.2298/JMMB1002181B) M.J. Bu, P.S. Wang, H.H. Xu, S.H. Liu, C.S. Shu, Y. Du, F.S. Pan, A.T. Tang, J. Min. Metall. B, 46, 181-92(2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.jallcom.2008.07.144](https://doi.org/10.1016/j.jallcom.2008.07.144) X.C. He, H.S. Liu, Determination of the isothermal section of the Cu–Zr–Y ternary system at 978K, Journal of Alloys and Compounds 475, 245-251 (2009).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0099](https://doi.org/10.3139/ijmr-1997-0099) H. Flandorfer, J. Groebner, A. Stamou, N. Hassiotis, A. Saccone, P. Rogl, R. Wouters, H. Seifert, D. Maccio, R. Ferro, G. Haidemenopoulus, L. Delaey, G. Effenberg, Z. Metallkd., 88, 529-38(1997).  
_assessment that models this phase_

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
