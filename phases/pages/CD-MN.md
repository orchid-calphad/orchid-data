# Cd–Mn phases

> Cd–Mn system: 6 phases (tier A 5, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-MN.html · Markdown: https://data.orchid-project.org/phases/pages/CD-MN.md

6 phases (tier A 5, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-MN) · [full JSON](https://data.orchid-project.org/phases/systems/CD-MN.json) · [Cd–Mn system page](https://data.orchid-project.org/systems/CD-MN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-MN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Mn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-mn-bcc-a2); _phase:cd-mn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1400–2498.96 K, x(Mn) 0.99759–1 | 0 | 1 |
| [CBCC_A12](#phase-cd-mn-cbcc-a12); _phase:cd-mn:cbcc-a12_ | alpha-Mn · A12 · cI58 · I-43m (217) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–980 K, x(Mn) 1–1 | 0 | 1 |
| [CUB_A13](#phase-cd-mn-cub-a13); _phase:cd-mn:cub-a13_ | beta-Mn · A13 · cP20 · P4_132 (213) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 980–1407.96 K, x(Mn) 1–1 | 0 | 1 |
| [FCC_A1](#phase-cd-mn-fcc-a1); _phase:cd-mn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1332.96–1413.68 K, x(Mn) 0.99605–1 | 0 | 1 |
| [HCP_A3](#phase-cd-mn-hcp-a3); _phase:cd-mn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–593.61 K, x(Mn) 0–0.00027 | 0 | 1 |
| [LIQUID](#phase-cd-mn-liquid); _phase:cd-mn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 593.61–2500 K, x(Mn) 0–1 | 0 | 1 |

## BCC_A2 (Cd–Mn)

- Id: `phase:cd-mn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1400–2498.96 K, x(Mn) 0.99759–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mn:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-mn:bcc-a2  
_tdb: _tdb:CdMn-14Qin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdMn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb): BCC_A2, type code %B, sha256 `9925fc3a837c19be…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CD MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## CBCC_A12 (Cd–Mn)

- Id: `phase:cd-mn:cbcc-a12`; status `assigned`
- Structure: alpha-Mn · A12 · cI58 · I-43m (217); type `st:a12-alpha-mn-ci58`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–980 K, x(Mn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mn:cbcc-a12)

Names (2): _corpus: _corpus:phase:cd-mn:cbcc-a12  
_tdb: _tdb:CdMn-14Qin.tdb:CBCC_A12  


### TDB models of CBCC_A12 (1): PHASE and CONSTITUENT statements as written

[CdMn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb): CBCC_A12, type code %A, sha256 `9925fc3a837c19be…`

~~~~text
41: PHASE CBCC_A12 %A 2 1 1 !
42: CONST CBCC_A12 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## CUB_A13 (Cd–Mn)

- Id: `phase:cd-mn:cub-a13`; status `assigned`
- Structure: beta-Mn · A13 · cP20 · P4_132 (213); type `st:a13-beta-mn-cp20`; tier A: standard phase name; confidence high
- Stoichiometry: Mn 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 980–1407.96 K, x(Mn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mn:cub-a13)

Names (2): _corpus: _corpus:phase:cd-mn:cub-a13  
_tdb: _tdb:CdMn-14Qin.tdb:CUB_A13  


### TDB models of CUB_A13 (1): PHASE and CONSTITUENT statements as written

[CdMn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb): CUB_A13, type code %, sha256 `9925fc3a837c19be…`

~~~~text
46: PHASE CUB_A13 % 2 1 1 !
47: CONST CUB_A13 : MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## FCC_A1 (Cd–Mn)

- Id: `phase:cd-mn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1332.96–1413.68 K, x(Mn) 0.99605–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mn:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-mn:fcc-a1  
_tdb: _tdb:CdMn-14Qin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdMn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb): FCC_A1, type code %A, sha256 `9925fc3a837c19be…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CD MN% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## HCP_A3 (Cd–Mn)

- Id: `phase:cd-mn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–593.61 K, x(Mn) 0–0.00027
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mn:hcp-a3)

Names (2): _corpus: _corpus:phase:cd-mn:hcp-a3  
_tdb: _tdb:CdMn-14Qin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdMn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb): HCP_A3, type code %A, sha256 `9925fc3a837c19be…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CD% MN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## LIQUID (Cd–Mn)

- Id: `phase:cd-mn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 593.61–2500 K, x(Mn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mn:liquid)

Names (2): _corpus: _corpus:phase:cd-mn:liquid  
_tdb: _tdb:CdMn-14Qin.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdMn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMn-14Qin.tdb): LIQUID, type code %, sha256 `9925fc3a837c19be…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CD MN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
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
