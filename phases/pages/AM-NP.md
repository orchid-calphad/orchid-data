# Am–Np phases

> Am–Np system: 7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AM-NP.html · Markdown: https://data.orchid-project.org/phases/pages/AM-NP.md

7 phases (tier A 6, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AM-NP) · [full JSON](https://data.orchid-project.org/phases/systems/AM-NP.json) · [Am–Np system page](https://data.orchid-project.org/systems/AM-NP.html) · [Markdown](https://data.orchid-project.org/phases/pages/AM-NP.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Am–Np system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAG_AD](#phase-am-np-ad-tetrag); _phase:am-np:ad-tetrag_ | beta-Np · A_d · tP4 · P4/nmm (129) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 555.03–910.95 K, x(Np) 0.99776–1 | 0 | 2 |
| [BCC_A2](#phase-am-np-bcc-a2); _phase:am-np:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 823.05–2499.34 K, x(Np) 0–1 | 0 | 2 |
| [DHCP](#phase-am-np-dhcp-a3); _phase:am-np:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1362.47 K, x(Np) 0–0.00653 | 0 | 2 |
| [FCC_A1](#phase-am-np-fcc-a1); _phase:am-np:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 787.47–1362.47 K, x(Np) 0–0.13302 | 0 | 2 |
| [HCP_A3](#phase-am-np-hcp-a3); _phase:am-np:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-am-np-liquid); _phase:am-np:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 882.99–2500 K, x(Np) 0–1 | 0 | 2 |
| [ORTHO_AC](#phase-am-np-ortho-ac); _phase:am-np:ortho-ac_ | alpha-Np · A_c · oP8 · Pnma (62) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–555.03 K, x(Np) 0.99991–1 | 0 | 2 |

## TETRAG_AD (Am–Np)

- Id: `phase:am-np:ad-tetrag`; status `assigned`
- Structure: beta-Np · A_d · tP4 · P4/nmm (129); type `st:a-d-beta-np-tp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 555.03–910.95 K, x(Np) 0.99776–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:ad-tetrag)

Names (3): _corpus: _corpus:phase:am-np:ad-tetrag  
_tdb: _tdb:AmNp-10Kur.tdb:TETRAG_AD, tdb:AmNp-93Oga.tdb:TETRAG_AD  


### TDB models of TETRAG_AD (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): TETRAG_AD, type code %, sha256 `2a5ba036840cfb6c…`

~~~~text
50: PHASE TETRAG_AD % 1 1 !
51: CONST TETRAG_AD : AM NP% : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): TETRAG_AD, type code %, sha256 `cfa44b10057e67b3…`

~~~~text
56: PHASE TETRAG_AD % 1 1 !
57: CONST TETRAG_AD : NP : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_

## BCC_A2 (Am–Np)

- Id: `phase:am-np:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 823.05–2499.34 K, x(Np) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:bcc-a2)

Names (3): _corpus: _corpus:phase:am-np:bcc-a2  
_tdb: _tdb:AmNp-10Kur.tdb:BCC_A2, tdb:AmNp-93Oga.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): BCC_A2, type code %B, sha256 `2a5ba036840cfb6c…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : AM% NP% : VA : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): BCC_A2, type code %B, sha256 `cfa44b10057e67b3…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : AM% NP% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_

## DHCP (Am–Np)

- Id: `phase:am-np:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1362.47 K, x(Np) 0–0.00653
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:dhcp-a3)

Names (3): _corpus: _corpus:phase:am-np:dhcp-a3  
_tdb: _tdb:AmNp-10Kur.tdb:DHCP, tdb:AmNp-93Oga.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): DHCP, type code %, sha256 `2a5ba036840cfb6c…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : AM% NP : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): DHCP, type code %, sha256 `cfa44b10057e67b3…`

~~~~text
46: PHASE DHCP % 1 1 !
47: CONST DHCP : AM : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_

## FCC_A1 (Am–Np)

- Id: `phase:am-np:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 787.47–1362.47 K, x(Np) 0–0.13302
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:fcc-a1)

Names (3): _corpus: _corpus:phase:am-np:fcc-a1  
_tdb: _tdb:AmNp-10Kur.tdb:FCC_A1, tdb:AmNp-93Oga.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): FCC_A1, type code %A, sha256 `2a5ba036840cfb6c…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : AM% NP : VA : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): FCC_A1, type code %A, sha256 `cfa44b10057e67b3…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : AM% NP : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_

## HCP_A3 (Am–Np)

- Id: `phase:am-np:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:hcp-a3)

Names (3): _corpus: _corpus:phase:am-np:hcp-a3  
_tdb: _tdb:AmNp-10Kur.tdb:HCP_A3, tdb:AmNp-93Oga.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): HCP_A3, type code %A, sha256 `2a5ba036840cfb6c…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : AM NP : VA : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): HCP_A3, type code %A, sha256 `cfa44b10057e67b3…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : AM NP : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_

## LIQUID (Am–Np)

- Id: `phase:am-np:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 882.99–2500 K, x(Np) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:liquid)

Names (3): _corpus: _corpus:phase:am-np:liquid  
_tdb: _tdb:AmNp-10Kur.tdb:LIQUID, tdb:AmNp-93Oga.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): LIQUID, type code %, sha256 `2a5ba036840cfb6c…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : AM NP : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): LIQUID, type code %, sha256 `cfa44b10057e67b3…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : AM NP : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
_assessment that models this phase_

## ORTHO_AC (Am–Np)

- Id: `phase:am-np:ortho-ac`; status `assigned`
- Structure: alpha-Np · A_c · oP8 · Pnma (62); type `st:a-c-alpha-np-op8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–555.03 K, x(Np) 0.99991–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:am-np:ortho-ac)

Names (3): _corpus: _corpus:phase:am-np:ortho-ac  
_tdb: _tdb:AmNp-10Kur.tdb:ORTHO_AC, tdb:AmNp-93Oga.tdb:ORTHO_AC  


### TDB models of ORTHO_AC (2): PHASE and CONSTITUENT statements as written

[AmNp-10Kur.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-10Kur.tdb): ORTHO_AC, type code %, sha256 `2a5ba036840cfb6c…`

~~~~text
45: PHASE ORTHO_AC % 1 1 !
46: CONST ORTHO_AC : AM NP% : !
~~~~

[AmNp-93Oga.tdb](https://orchid-project.org/data/databases/sgte-binary/AmNp-93Oga.tdb): ORTHO_AC, type code %, sha256 `cfa44b10057e67b3…`

~~~~text
51: PHASE ORTHO_AC % 1 1 !
52: CONST ORTHO_AC : NP : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0925-8388(93)90636-2](https://doi.org/10.1016/0925-8388%2893%2990636-2) Toru Ogawa, Alloying behaviour among U, Np, Pu and Am predicted with the Brewer valence bond model, Journal of Alloys and Compounds 194, 1-7 (1993).  
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
