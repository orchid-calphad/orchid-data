# Ag–Cr phases

> Ag–Cr system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-CR.html · Markdown: https://data.orchid-project.org/phases/pages/AG-CR.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-CR) · [full JSON](https://data.orchid-project.org/phases/systems/AG-CR.json) · [Ag–Cr system page](https://data.orchid-project.org/systems/AG-CR.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-CR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Cr system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ag-cr-bcc-a2); _phase:ag-cr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.98 K, x(Cr) 0.99836–1 | 0 | 3 |
| [FCC_A1](#phase-ag-cr-fcc-a1); _phase:ag-cr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1235.54 K, x(Cr) 0–0.00251 | 0 | 3 |
| [HCP_A3](#phase-ag-cr-hcp-a3); _phase:ag-cr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-ag-cr-liquid); _phase:ag-cr:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1210.54–4000 K, x(Cr) 0–1 | 0 | 3 |

## BCC_A2 (Ag–Cr)

- Id: `phase:ag-cr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.98 K, x(Cr) 0.99836–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cr:bcc-a2)

Names (4): _corpus: _corpus:phase:ag-cr:bcc-a2  
_tdb: _tdb:AgCr-04Kor-LB.tdb:BCC_A2, tdb:AgCr-20Qiu.tdb:BCC_A2, tdb:AgCr-21Shi.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[AgCr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-04Kor-LB.tdb): BCC_A2, type code %B, sha256 `a2433be47f9079dd…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG CR% : VA : !
~~~~

[AgCr-20Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-20Qiu.tdb): BCC_A2, type code %B, sha256 `ea4cb56095aea45a…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : AG CR% : VA : !
~~~~

[AgCr-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-21Shi.tdb): BCC_A2, type code %B, sha256 `20f97ab537bb5c2a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AG CR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101734](https://doi.org/10.1016/j.calphad.2019.101734) C. Qiu, B. Hu, J. Zhou, P. Wu, Y. Liu, C. Wang, Y. Du, Calphad, 68, 101734(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158618](https://doi.org/10.1016/j.jallcom.2021.158618) Chenying Shi, Yuling Liu, Biaobiao Yang, Bo Jin, Biao Hu, V.B. Rajkumar et al., Phase equilibria thermodynamics and solidified microstructure in the Ag-Cr-Zr system, Journal of Alloys and Compounds 863, 158618 (2021).  
_assessment that models this phase_

## FCC_A1 (Ag–Cr)

- Id: `phase:ag-cr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1235.54 K, x(Cr) 0–0.00251
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cr:fcc-a1)

Names (4): _corpus: _corpus:phase:ag-cr:fcc-a1  
_tdb: _tdb:AgCr-04Kor-LB.tdb:FCC_A1, tdb:AgCr-20Qiu.tdb:FCC_A1, tdb:AgCr-21Shi.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[AgCr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-04Kor-LB.tdb): FCC_A1, type code %A, sha256 `a2433be47f9079dd…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% CR : VA : !
~~~~

[AgCr-20Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-20Qiu.tdb): FCC_A1, type code %A, sha256 `ea4cb56095aea45a…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : AG% CR : VA : !
~~~~

[AgCr-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-21Shi.tdb): FCC_A1, type code %A, sha256 `20f97ab537bb5c2a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AG% CR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101734](https://doi.org/10.1016/j.calphad.2019.101734) C. Qiu, B. Hu, J. Zhou, P. Wu, Y. Liu, C. Wang, Y. Du, Calphad, 68, 101734(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158618](https://doi.org/10.1016/j.jallcom.2021.158618) Chenying Shi, Yuling Liu, Biaobiao Yang, Bo Jin, Biao Hu, V.B. Rajkumar et al., Phase equilibria thermodynamics and solidified microstructure in the Ag-Cr-Zr system, Journal of Alloys and Compounds 863, 158618 (2021).  
_assessment that models this phase_

## HCP_A3 (Ag–Cr)

- Id: `phase:ag-cr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cr:hcp-a3)

Names (4): _corpus: _corpus:phase:ag-cr:hcp-a3  
_tdb: _tdb:AgCr-04Kor-LB.tdb:HCP_A3, tdb:AgCr-20Qiu.tdb:HCP_A3, tdb:AgCr-21Shi.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[AgCr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-04Kor-LB.tdb): HCP_A3, type code %A, sha256 `a2433be47f9079dd…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG CR : VA : !
~~~~

[AgCr-20Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-20Qiu.tdb): HCP_A3, type code %A, sha256 `ea4cb56095aea45a…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : AG CR : VA : !
~~~~

[AgCr-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-21Shi.tdb): HCP_A3, type code %A, sha256 `20f97ab537bb5c2a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AG CR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101734](https://doi.org/10.1016/j.calphad.2019.101734) C. Qiu, B. Hu, J. Zhou, P. Wu, Y. Liu, C. Wang, Y. Du, Calphad, 68, 101734(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158618](https://doi.org/10.1016/j.jallcom.2021.158618) Chenying Shi, Yuling Liu, Biaobiao Yang, Bo Jin, Biao Hu, V.B. Rajkumar et al., Phase equilibria thermodynamics and solidified microstructure in the Ag-Cr-Zr system, Journal of Alloys and Compounds 863, 158618 (2021).  
_assessment that models this phase_

## LIQUID (Ag–Cr)

- Id: `phase:ag-cr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1210.54–4000 K, x(Cr) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-cr:liquid)

Names (4): _corpus: _corpus:phase:ag-cr:liquid  
_tdb: _tdb:AgCr-04Kor-LB.tdb:LIQUID, tdb:AgCr-20Qiu.tdb:LIQUID, tdb:AgCr-21Shi.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[AgCr-04Kor-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-04Kor-LB.tdb): LIQUID, type code %, sha256 `a2433be47f9079dd…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG CR : !
~~~~

[AgCr-20Qiu.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-20Qiu.tdb): LIQUID, type code %, sha256 `ea4cb56095aea45a…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : AG CR : !
~~~~

[AgCr-21Shi.tdb](https://orchid-project.org/data/databases/sgte-binary/AgCr-21Shi.tdb): LIQUID, type code %, sha256 `20f97ab537bb5c2a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AG CR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2019.101734](https://doi.org/10.1016/j.calphad.2019.101734) C. Qiu, B. Hu, J. Zhou, P. Wu, Y. Liu, C. Wang, Y. Du, Calphad, 68, 101734(2020).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2021.158618](https://doi.org/10.1016/j.jallcom.2021.158618) Chenying Shi, Yuling Liu, Biaobiao Yang, Bo Jin, Biao Hu, V.B. Rajkumar et al., Phase equilibria thermodynamics and solidified microstructure in the Ag-Cr-Zr system, Journal of Alloys and Compounds 863, 158618 (2021).  
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
