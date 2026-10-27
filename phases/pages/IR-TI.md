# Ir–Ti phases

> Ir–Ti system: 8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IR-TI.html · Markdown: https://data.orchid-project.org/phases/pages/IR-TI.md

8 phases (tier A 7, liquid 1); 8 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IR-TI) · [full JSON](https://data.orchid-project.org/phases/systems/IR-TI.json) · [Ir–Ti system page](https://data.orchid-project.org/systems/IR-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/IR-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ir–Ti system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ir-ti-bcc-a2); _phase:ir-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 990–1940.98 K, x(Ti) 0.82957–1 | 9 | 1 |
| [FCC_A1](#phase-ir-ti-fcc-a1); _phase:ir-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2725 K, x(Ti) 0–0.09969 | 4 | 1 |
| [HCP_A3](#phase-ir-ti-hcp-a3); _phase:ir-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1939.99 K, x(Ti) 0.99558–1 | 5 | 1 |
| [IR3TI_L12](#phase-ir-ti-ir3ti-l12); _phase:ir-ti:ir3ti-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2387.95 K, x(Ti) 0.2238–0.27814 | 12 | 1 |
| [IRTI_B2](#phase-ir-ti-irti-b2); _phase:ir-ti:irti-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2402.98 K, x(Ti) 0.42736–0.64635 | 16 | 1 |
| [IRTI_L10](#phase-ir-ti-irti-l10); _phase:ir-ti:irti-l10_ | AuCu · L1_0 · tP4 · P4/mmm (123) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2023.98 K, x(Ti) 0.41624–0.56398 | 0 | 1 |
| [IRTI3_A15](#phase-ir-ti-irti3-a15); _phase:ir-ti:irti3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1789.1 K, x(Ti) 0.72966–0.76187 | 13 | 1 |
| [LIQUID](#phase-ir-ti-liquid); _phase:ir-ti:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1740.19–4000 K, x(Ti) 0–1 | 20 | 1 |

## BCC_A2 (Ir–Ti)

- Id: `phase:ir-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 990–1940.98 K, x(Ti) 0.82957–1
- Literature: 9 values (9 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:bcc-a2)

Names (3): _corpus: _corpus:phase:ir-ti:bcc-a2  
_paper: _paper:10.1007/s11669-014-0302-1:(βTi)  
_tdb: _tdb:IrTi-14Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): BCC_A2, type code %B, sha256 `b451b67f1b3cf0c9…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : IR TI% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
_cited as the source of values for this phase_

## FCC_A1 (Ir–Ti)

- Id: `phase:ir-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2725 K, x(Ti) 0–0.09969
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:fcc-a1)

Names (3): _corpus: _corpus:phase:ir-ti:fcc-a1  
_paper: _paper:10.1007/s11669-014-0302-1:(Ir)  
_tdb: _tdb:IrTi-14Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): FCC_A1, type code %A, sha256 `b451b67f1b3cf0c9…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : IR% TI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
_cited as the source of values for this phase_

## HCP_A3 (Ir–Ti)

- Id: `phase:ir-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1939.99 K, x(Ti) 0.99558–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:hcp-a3)

Names (3): _corpus: _corpus:phase:ir-ti:hcp-a3  
_paper: _paper:10.1007/s11669-014-0302-1:(αTi)  
_tdb: _tdb:IrTi-14Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): HCP_A3, type code %A, sha256 `b451b67f1b3cf0c9…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : IR TI% : VA: !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
_cited as the source of values for this phase_

## IR3TI_L12 (Ir–Ti)

- Id: `phase:ir-ti:ir3ti-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in IrTi-14Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2387.95 K, x(Ti) 0.2238–0.27814
- Literature: 12 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:ir3ti-l12)

Names (3): _corpus: _corpus:phase:ir-ti:ir3ti-l12  
_paper: _paper:10.1007/s11669-014-0302-1:TiIr3  
_tdb: _tdb:IrTi-14Wan.tdb:IR3TI_L12  


### TDB models of IR3TI_L12 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): IR3TI_L12, type code %, sha256 `b451b67f1b3cf0c9…`

~~~~text
46: PHASE IR3TI_L12 %  2 3 1 !
47: CONST IR3TI_L12 : IR% TI : IR TI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
_cited as the source of values for this phase_

## IRTI_B2 (Ir–Ti)

- Id: `phase:ir-ti:irti-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in IrTi-14Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2402.98 K, x(Ti) 0.42736–0.64635
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:irti-b2)

Names (3): _corpus: _corpus:phase:ir-ti:irti-b2  
_paper: _paper:10.1007/s11669-014-0302-1:γTiIr  
_tdb: _tdb:IrTi-14Wan.tdb:IRTI_B2  


### TDB models of IRTI_B2 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): IRTI_B2, type code %, sha256 `b451b67f1b3cf0c9…`

~~~~text
56: PHASE IRTI_B2 %  2 1 1 !
57: CONST IRTI_B2 : IR% TI : IR TI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
_cited as the source of values for this phase_

## IRTI_L10 (Ir–Ti)

- Id: `phase:ir-ti:irti-l10`; status `assigned`
- Structure: AuCu · L1_0 · tP4 · P4/mmm (123); type `st:l1-0-aucu-tp4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in IrTi-14Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2023.98 K, x(Ti) 0.41624–0.56398
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:irti-l10)

Names (2): _corpus: _corpus:phase:ir-ti:irti-l10  
_tdb: _tdb:IrTi-14Wan.tdb:IRTI_L10  


### TDB models of IRTI_L10 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): IRTI_L10, type code %, sha256 `b451b67f1b3cf0c9…`

~~~~text
51: PHASE IRTI_L10 %  2 1 1 !
52: CONST IRTI_L10 : IR% TI : IR TI% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase_

## IRTI3_A15 (Ir–Ti)

- Id: `phase:ir-ti:irti3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in IrTi-14Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1789.1 K, x(Ti) 0.72966–0.76187
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:irti3-a15)

Names (3): _corpus: _corpus:phase:ir-ti:irti3-a15  
_paper: _paper:10.1007/s11669-014-0302-1:Ti3Ir  
_tdb: _tdb:IrTi-14Wan.tdb:IRTI3_A15  


### TDB models of IRTI3_A15 (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): IRTI3_A15, type code %, sha256 `b451b67f1b3cf0c9…`

~~~~text
61: PHASE IRTI3_A15 %  2 1 3 !
62: CONST IRTI3_A15 : IR% TI : IR TI% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
_cited as the source of values for this phase_

## LIQUID (Ir–Ti)

- Id: `phase:ir-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1740.19–4000 K, x(Ti) 0–1
- Literature: 20 values (20 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ir-ti:liquid)

Names (3): _corpus: _corpus:phase:ir-ti:liquid  
_paper: _paper:10.1007/s11669-014-0302-1:L  
_tdb: _tdb:IrTi-14Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[IrTi-14Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/IrTi-14Wan.tdb): LIQUID, type code %, sha256 `b451b67f1b3cf0c9…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : IR TI : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0302-1](https://doi.org/10.1007/s11669-014-0302-1) Cuiping Wang, Yihui Guo, Yong Lu, Xingjun Liu, Thermodynamic Assessment of the Ti-Ir System, J. Phase Equilib. Diffus. 35, 269-275 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02667568](https://doi.org/10.1007/bf02667568) H. Okamoto, Ir-Ti (Iridium-Titanium), J. Phase Equilib., 1992, 13, p 329-331  
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
