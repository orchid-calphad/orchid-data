# Fe–Pd phases

> Fe–Pd system: 6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/FE-PD.html · Markdown: https://data.orchid-project.org/phases/pages/FE-PD.md

6 phases (tier A 5, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=FE-PD) · [full JSON](https://data.orchid-project.org/phases/systems/FE-PD.json) · [Fe–Pd system page](https://data.orchid-project.org/systems/FE-PD.html) · [Markdown](https://data.orchid-project.org/phases/pages/FE-PD.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Fe–Pd system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-fe-pd-bcc-a2); _phase:fe-pd:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1815.95 K, x(Pd) 0–0.03877 | 8 | 1 |
| [FCC_A1](#phase-fe-pd-fcc-a1); _phase:fe-pd:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2499.24 K, x(Pd) 0–1 | 18 | 1 |
| [FEPD_L10](#phase-fe-pd-fepd-l10); _phase:fe-pd:fepd-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1061.42 K, x(Pd) 0.48925–0.62224 | 10 | 1 |
| [FEPD3_L12](#phase-fe-pd-fepd3-l12); _phase:fe-pd:fepd3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1093.95 K, x(Pd) 0.66672–0.88493 | 8 | 1 |
| [HCP_A3](#phase-fe-pd-hcp-a3); _phase:fe-pd:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-fe-pd-liquid); _phase:fe-pd:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1581.68–2500 K, x(Pd) 0–1 | 4 | 1 |

## BCC_A2 (Fe–Pd)

- Id: `phase:fe-pd:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1815.95 K, x(Pd) 0–0.03877
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pd:bcc-a2)

Names (4): _corpus: _corpus:phase:fe-pd:bcc-a2  
_paper: _paper:10.1361/105497199770335811:(αFe), paper:10.1361/105497199770335811:(δFe)  
_tdb: _tdb:FePd-99Gho-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[FePd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb): BCC_A2, type code %B, sha256 `44714d50700b1a28…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : FE% PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Fe–Pd)

- Id: `phase:fe-pd:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499.24 K, x(Pd) 0–1
- Literature: 18 values (18 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pd:fcc-a1)

Names (4): _corpus: _corpus:phase:fe-pd:fcc-a1  
_paper: _paper:10.1361/105497199770335811:(γFe), paper:10.1361/105497199770335811:γ  
_tdb: _tdb:FePd-99Gho-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[FePd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb): FCC_A1, type code %A, sha256 `44714d50700b1a28…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : FE% PD% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.51.4_285](https://doi.org/10.2320/jinstmet1952.51.4_285) Takasi Takezawa, Takashi Miwa, Toru Yokoyama, Increase of Electrical Resistivity with Ordering of Fe-(50-80 at%)Pd Alloys, J.Japan Inst.Metals 51, 285-291 (1987).  
_cited as the source of values for this phase_

## FEPD_L10 (Fe–Pd)

- Id: `phase:fe-pd:fepd-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FePd-99Gho-LB.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1061.42 K, x(Pd) 0.48925–0.62224
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pd:fepd-l10)

Names (3): _corpus: _corpus:phase:fe-pd:fepd-l10  
_paper: _paper:10.1361/105497199770335811:FePd  
_tdb: _tdb:FePd-99Gho-LB.tdb:FEPD_L10  


### TDB models of FEPD_L10 (1): PHASE and CONSTITUENT statements as written

[FePd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb): FEPD_L10, type code %A, sha256 `44714d50700b1a28…`

~~~~text
46: PHASE FEPD_L10 %A 2 0.5 0.5 !
47: CONST FEPD_L10 : FE% PD : FE PD% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.51.4_285](https://doi.org/10.2320/jinstmet1952.51.4_285) Takasi Takezawa, Takashi Miwa, Toru Yokoyama, Increase of Electrical Resistivity with Ordering of Fe-(50-80 at%)Pd Alloys, J.Japan Inst.Metals 51, 285-291 (1987).  
_cited as the source of values for this phase_

## FEPD3_L12 (Fe–Pd)

- Id: `phase:fe-pd:fepd3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in FePd-99Gho-LB.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1093.95 K, x(Pd) 0.66672–0.88493
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pd:fepd3-l12)

Names (3): _corpus: _corpus:phase:fe-pd:fepd3-l12  
_paper: _paper:10.1361/105497199770335811:FePd3  
_tdb: _tdb:FePd-99Gho-LB.tdb:FEPD3_L12  


### TDB models of FEPD3_L12 (1): PHASE and CONSTITUENT statements as written

[FePd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb): FEPD3_L12, type code %A, sha256 `44714d50700b1a28…`

~~~~text
51: PHASE FEPD3_L12 %A 2 0.25 0.75 !
52: CONST FEPD3_L12 : FE% PD : FE PD% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.2320/jinstmet1952.51.4_285](https://doi.org/10.2320/jinstmet1952.51.4_285) Takasi Takezawa, Takashi Miwa, Toru Yokoyama, Increase of Electrical Resistivity with Ordering of Fe-(50-80 at%)Pd Alloys, J.Japan Inst.Metals 51, 285-291 (1987).  
_cited as the source of values for this phase_

## HCP_A3 (Fe–Pd)

- Id: `phase:fe-pd:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pd:hcp-a3)

Names (2): _corpus: _corpus:phase:fe-pd:hcp-a3  
_tdb: _tdb:FePd-99Gho-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[FePd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb): HCP_A3, type code %A, sha256 `44714d50700b1a28…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : FE PD : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999).  
_assessment that models this phase_

## LIQUID (Fe–Pd)

- Id: `phase:fe-pd:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1581.68–2500 K, x(Pd) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:fe-pd:liquid)

Names (3): _corpus: _corpus:phase:fe-pd:liquid  
_paper: _paper:10.1361/105497199770335811:L  
_tdb: _tdb:FePd-99Gho-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[FePd-99Gho-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/FePd-99Gho-LB.tdb): LIQUID, type code %, sha256 `44714d50700b1a28…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : FE PD : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/105497199770335811](https://doi.org/10.1361/105497199770335811) G. Ghosh, C. Kantner, G. B. Olson, Thermodynamic modeling of the Pd-X (X=Ag, Co, Fe, Ni) systems, JPE 20, 295-308 (1999).  
_assessment that models this phase; reports values for this phase_

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
