# Mn–W phases

> Mn–W system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MN-W.html · Markdown: https://data.orchid-project.org/phases/pages/MN-W.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MN-W) · [full JSON](https://data.orchid-project.org/phases/systems/MN-W.json) · [Mn–W system page](https://data.orchid-project.org/systems/MN-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/MN-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mn–W system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mn-w-bcc-a2); _phase:mn-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0–1 | 0 | 2 |
| [CBCC_A12](#phase-mn-w-cbcc-a12); _phase:mn-w:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–981.81 K, x(W) 0–0.00178 | 0 | 2 |
| [CUB_A13](#phase-mn-w-cub-a13); _phase:mn-w:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 980–1474.99 K, x(W) 0–0.00603 | 0 | 2 |
| [FCC_A1](#phase-mn-w-fcc-a1); _phase:mn-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1329.47–1508.44 K, x(W) 0–0.00609 | 0 | 2 |
| [HCP_A3](#phase-mn-w-hcp-a3); _phase:mn-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-mn-w-liquid); _phase:mn-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1508.44–4000 K, x(W) 0–1 | 0 | 2 |

## BCC_A2 (Mn–W)

- Id: `phase:mn-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.9 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-w:bcc-a2)

Names (3): _corpus: _corpus:phase:mn-w:bcc-a2  
_tdb: _tdb:MnW-08Fra.tdb:BCC_A2, tdb:MnW-18Els.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[MnW-08Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-08Fra.tdb): BCC_A2, type code %B, sha256 `73c9fe1bb2c5b04f…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MN W : VA : !
~~~~

[MnW-18Els.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-18Els.tdb): BCC_A2, type code %B, sha256 `4dc5d2756f97b600…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : MN W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2018.01.006](https://doi.org/10.1016/j.ijrmhm.2018.01.006) Ossama Elsebaie, Kevin M. Jaansalu, A study of the manganese–tungsten binary phase diagram, International Journal of Refractory Metals and Hard Materials 72, 332-340 (2018).  
_assessment that models this phase_

## CBCC_A12 (Mn–W)

- Id: `phase:mn-w:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–981.81 K, x(W) 0–0.00178
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-w:cbcc-a12)

Names (3): _corpus: _corpus:phase:mn-w:cbcc-a12  
_tdb: _tdb:MnW-08Fra.tdb:CBCC_A12, tdb:MnW-18Els.tdb:CBCC_A12  


### TDB models of CBCC_A12 (2): PHASE and CONSTITUENT statements as written

[MnW-08Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-08Fra.tdb): CBCC_A12, type code %A, sha256 `73c9fe1bb2c5b04f…`

~~~~text
43: PHASE CBCC_A12 %A 2 1 1 !
44: CONST CBCC_A12 : MN : VA : !
~~~~

[MnW-18Els.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-18Els.tdb): CBCC_A12, type code %A, sha256 `4dc5d2756f97b600…`

~~~~text
39: PHASE CBCC_A12 %A 2 1 1 !
40: CONST CBCC_A12 : MN% W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2018.01.006](https://doi.org/10.1016/j.ijrmhm.2018.01.006) Ossama Elsebaie, Kevin M. Jaansalu, A study of the manganese–tungsten binary phase diagram, International Journal of Refractory Metals and Hard Materials 72, 332-340 (2018).  
_assessment that models this phase_

## CUB_A13 (Mn–W)

- Id: `phase:mn-w:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 980–1474.99 K, x(W) 0–0.00603
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-w:cub-a13)

Names (3): _corpus: _corpus:phase:mn-w:cub-a13  
_tdb: _tdb:MnW-08Fra.tdb:CUB_A13, tdb:MnW-18Els.tdb:CUB_A13  


### TDB models of CUB_A13 (2): PHASE and CONSTITUENT statements as written

[MnW-08Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-08Fra.tdb): CUB_A13, type code %, sha256 `73c9fe1bb2c5b04f…`

~~~~text
48: PHASE CUB_A13 % 2 1 1 !
49: CONST CUB_A13 : MN : VA : !
~~~~

[MnW-18Els.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-18Els.tdb): CUB_A13, type code %, sha256 `4dc5d2756f97b600…`

~~~~text
44: PHASE CUB_A13 % 2 1 1 !
45: CONST CUB_A13 : MN% W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2018.01.006](https://doi.org/10.1016/j.ijrmhm.2018.01.006) Ossama Elsebaie, Kevin M. Jaansalu, A study of the manganese–tungsten binary phase diagram, International Journal of Refractory Metals and Hard Materials 72, 332-340 (2018).  
_assessment that models this phase_

## FCC_A1 (Mn–W)

- Id: `phase:mn-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1329.47–1508.44 K, x(W) 0–0.00609
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-w:fcc-a1)

Names (3): _corpus: _corpus:phase:mn-w:fcc-a1  
_tdb: _tdb:MnW-08Fra.tdb:FCC_A1, tdb:MnW-18Els.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[MnW-08Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-08Fra.tdb): FCC_A1, type code %A, sha256 `73c9fe1bb2c5b04f…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MN% W : VA : !
~~~~

[MnW-18Els.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-18Els.tdb): FCC_A1, type code %A, sha256 `4dc5d2756f97b600…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : MN% W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2018.01.006](https://doi.org/10.1016/j.ijrmhm.2018.01.006) Ossama Elsebaie, Kevin M. Jaansalu, A study of the manganese–tungsten binary phase diagram, International Journal of Refractory Metals and Hard Materials 72, 332-340 (2018).  
_assessment that models this phase_

## HCP_A3 (Mn–W)

- Id: `phase:mn-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-w:hcp-a3)

Names (3): _corpus: _corpus:phase:mn-w:hcp-a3  
_tdb: _tdb:MnW-08Fra.tdb:HCP_A3, tdb:MnW-18Els.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[MnW-08Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-08Fra.tdb): HCP_A3, type code %A, sha256 `73c9fe1bb2c5b04f…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MN W : VA : !
~~~~

[MnW-18Els.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-18Els.tdb): HCP_A3, type code %A, sha256 `4dc5d2756f97b600…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : MN W : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2018.01.006](https://doi.org/10.1016/j.ijrmhm.2018.01.006) Ossama Elsebaie, Kevin M. Jaansalu, A study of the manganese–tungsten binary phase diagram, International Journal of Refractory Metals and Hard Materials 72, 332-340 (2018).  
_assessment that models this phase_

## LIQUID (Mn–W)

- Id: `phase:mn-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1508.44–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mn-w:liquid)

Names (3): _corpus: _corpus:phase:mn-w:liquid  
_tdb: _tdb:MnW-08Fra.tdb:LIQUID, tdb:MnW-18Els.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[MnW-08Fra.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-08Fra.tdb): LIQUID, type code %, sha256 `73c9fe1bb2c5b04f…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MN W : !
~~~~

[MnW-18Els.tdb](https://orchid-project.org/data/databases/sgte-binary/MnW-18Els.tdb): LIQUID, type code %, sha256 `4dc5d2756f97b600…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : MN W : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2018.01.006](https://doi.org/10.1016/j.ijrmhm.2018.01.006) Ossama Elsebaie, Kevin M. Jaansalu, A study of the manganese–tungsten binary phase diagram, International Journal of Refractory Metals and Hard Materials 72, 332-340 (2018).  
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
