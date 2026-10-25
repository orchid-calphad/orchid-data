# Re–Ti phases

> Re–Ti system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/RE-TI.html · Markdown: https://data.orchid-project.org/phases/pages/RE-TI.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=RE-TI) · [full JSON](https://data.orchid-project.org/phases/systems/RE-TI.json) · [Re–Ti system page](https://data.orchid-project.org/systems/RE-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/RE-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Re–Ti system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-re-ti-bcc-a2); _phase:re-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2040.61 K, x(Ti) 0.63644–1 | 0 | 1 |
| [FCC_A1](#phase-re-ti-fcc-a1); _phase:re-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-re-ti-hcp-a3); _phase:re-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3475.5 K, x(Ti) 0–1 | 0 | 1 |
| [LIQUID](#phase-re-ti-liquid); _phase:re-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1155.99–4000 K, x(Ti) 0–1 | 1 | 1 |
| [RE24TI5_A12](#phase-re-ti-re24ti5-a12); _phase:re-ti:re24ti5-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3068 K, x(Ti) 0.17241–0.17241 | 1 | 1 |
| [RETI_B2](#phase-re-ti-reti-b2); _phase:re-ti:reti-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3171.51 K, x(Ti) 0.5–0.5 | 1 | 1 |

## BCC_A2 (Re–Ti)

- Id: `phase:re-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2040.61 K, x(Ti) 0.63644–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ti:bcc-a2)

Names (2): _corpus: _corpus:phase:re-ti:bcc-a2  
_tdb: _tdb:ReTi-12Zac.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ReTi-12Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTi-12Zac.tdb): BCC_A2, type code %B, sha256 `c87d1fee31a160f8…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : RE TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.05.001](https://doi.org/10.1016/j.calphad.2012.05.001) Chelsey L. Zacherl, Shun-Li Shang, Arkapol Saengdeejing, Zi-Kui Liu, Phase stability and thermodynamic modeling of the Re–Ti system supplemented by first-principles calculations, Calphad 38, 71-80 (2012).  
_assessment that models this phase_

## FCC_A1 (Re–Ti)

- Id: `phase:re-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ti:fcc-a1)

Names (2): _corpus: _corpus:phase:re-ti:fcc-a1  
_tdb: _tdb:ReTi-12Zac.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ReTi-12Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTi-12Zac.tdb): FCC_A1, type code %A, sha256 `c87d1fee31a160f8…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : RE TI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.05.001](https://doi.org/10.1016/j.calphad.2012.05.001) Chelsey L. Zacherl, Shun-Li Shang, Arkapol Saengdeejing, Zi-Kui Liu, Phase stability and thermodynamic modeling of the Re–Ti system supplemented by first-principles calculations, Calphad 38, 71-80 (2012).  
_assessment that models this phase_

## HCP_A3 (Re–Ti)

- Id: `phase:re-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3475.5 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ti:hcp-a3)

Names (2): _corpus: _corpus:phase:re-ti:hcp-a3  
_tdb: _tdb:ReTi-12Zac.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ReTi-12Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTi-12Zac.tdb): HCP_A3, type code %A, sha256 `c87d1fee31a160f8…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : RE% TI% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.05.001](https://doi.org/10.1016/j.calphad.2012.05.001) Chelsey L. Zacherl, Shun-Li Shang, Arkapol Saengdeejing, Zi-Kui Liu, Phase stability and thermodynamic modeling of the Re–Ti system supplemented by first-principles calculations, Calphad 38, 71-80 (2012).  
_assessment that models this phase_

## LIQUID (Re–Ti)

- Id: `phase:re-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1155.99–4000 K, x(Ti) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ti:liquid)

Names (3): _corpus: _corpus:phase:re-ti:liquid  
_paper: _paper:10.1016/j.calphad.2012.05.001:liquid  
_tdb: _tdb:ReTi-12Zac.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ReTi-12Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTi-12Zac.tdb): LIQUID, type code %, sha256 `c87d1fee31a160f8…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : RE TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.05.001](https://doi.org/10.1016/j.calphad.2012.05.001) Chelsey L. Zacherl, Shun-Li Shang, Arkapol Saengdeejing, Zi-Kui Liu, Phase stability and thermodynamic modeling of the Re–Ti system supplemented by first-principles calculations, Calphad 38, 71-80 (2012).  
_assessment that models this phase; reports values for this phase_

## RE24TI5_A12 (Re–Ti)

- Id: `phase:re-ti:re24ti5-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaaty and oqmd-19420, space group 217
- Stoichiometry: Re 0.8276, Ti 0.1724
- Stability: stable in 1 of 1 calculated diagram(s): 300–3068 K, x(Ti) 0.17241–0.17241
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ti:re24ti5-a12)

Names (5): _corpus: _corpus:phase:re-ti:re24ti5-a12  
_mp: _mp:mp-aaaaaaty  
_oqmd: _oqmd:oqmd-19420  
_paper: _paper:10.1016/j.calphad.2012.05.001:χ-Re24Ti5  
_tdb: _tdb:ReTi-12Zac.tdb:RE24TI5_A12  


### TDB models of RE24TI5_A12 (1): PHASE and CONSTITUENT statements as written

[ReTi-12Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTi-12Zac.tdb): RE24TI5_A12, type code %, sha256 `c87d1fee31a160f8…`

~~~~text
50: PHASE RE24TI5_A12 % 2 24 5 !
51: CONST RE24TI5_A12 : RE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.05.001](https://doi.org/10.1016/j.calphad.2012.05.001) Chelsey L. Zacherl, Shun-Li Shang, Arkapol Saengdeejing, Zi-Kui Liu, Phase stability and thermodynamic modeling of the Re–Ti system supplemented by first-principles calculations, Calphad 38, 71-80 (2012).  
_assessment that models this phase; reports values for this phase_

## RETI_B2 (Re–Ti)

- Id: `phase:re-ti:reti-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaadfv and oqmd-18050, space group 221
- Stoichiometry: Re 0.5000, Ti 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–3171.51 K, x(Ti) 0.5–0.5
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:re-ti:reti-b2)

Names (5): _corpus: _corpus:phase:re-ti:reti-b2  
_mp: _mp:mp-aaaaadfv  
_oqmd: _oqmd:oqmd-18050  
_paper: _paper:10.1016/j.calphad.2012.05.001:B2–ReTi  
_tdb: _tdb:ReTi-12Zac.tdb:RETI_B2  


### TDB models of RETI_B2 (1): PHASE and CONSTITUENT statements as written

[ReTi-12Zac.tdb](https://orchid-project.org/data/databases/sgte-binary/ReTi-12Zac.tdb): RETI_B2, type code %, sha256 `c87d1fee31a160f8…`

~~~~text
55: PHASE RETI_B2 % 2 1 1 !
56: CONST RETI_B2 : RE : TI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2012.05.001](https://doi.org/10.1016/j.calphad.2012.05.001) Chelsey L. Zacherl, Shun-Li Shang, Arkapol Saengdeejing, Zi-Kui Liu, Phase stability and thermodynamic modeling of the Re–Ti system supplemented by first-principles calculations, Calphad 38, 71-80 (2012).  
_assessment that models this phase; reports values for this phase_

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
