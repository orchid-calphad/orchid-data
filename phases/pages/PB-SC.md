# Pb–Sc phases

> Pb–Sc system: 6 phases (tier A 4, tier B 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PB-SC.html · Markdown: https://data.orchid-project.org/phases/pages/PB-SC.md

6 phases (tier A 4, tier B 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PB-SC) · [full JSON](https://data.orchid-project.org/phases/systems/PB-SC.json) · [Pb–Sc system page](https://data.orchid-project.org/systems/PB-SC.html) · [Markdown](https://data.orchid-project.org/phases/pages/PB-SC.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pb–Sc system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pb-sc-bcc-a2); _phase:pb-sc:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1544.86–2498.99 K, x(Sc) 0.98191–1 | 0 | 1 |
| [FCC_A1](#phase-pb-sc-fcc-a1); _phase:pb-sc:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–601.54 K, x(Sc) 0–0 | 0 | 1 |
| [HCP_A3](#phase-pb-sc-hcp-a3); _phase:pb-sc:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Sc) 0.98998–1 | 0 | 1 |
| [LIQUID](#phase-pb-sc-liquid); _phase:pb-sc:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 600.54–2500 K, x(Sc) 0–1 | 0 | 1 |
| [PB3SC5_D88](#phase-pb-sc-pb3sc5-d88); _phase:pb-sc:pb3sc5-d88_ | Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1970.15 K, x(Sc) 0.625–0.625 | 0 | 1 |
| [PB5SC6](#phase-pb-sc-pb5sc6); _phase:pb-sc:pb5sc6_ | Si5V6 · oI44 · Ibam (72) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1561.98 K, x(Sc) 0.54545–0.54545 | 0 | 1 |

## BCC_A2 (Pb–Sc)

- Id: `phase:pb-sc:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1544.86–2498.99 K, x(Sc) 0.98191–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sc:bcc-a2)

Names (2): _corpus: _corpus:phase:pb-sc:bcc-a2  
_tdb: _tdb:PbSc-14Idd.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PbSc-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb): BCC_A2, type code %B, sha256 `f09786a7a2f576ea…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : PB SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_

## FCC_A1 (Pb–Sc)

- Id: `phase:pb-sc:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–601.54 K, x(Sc) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sc:fcc-a1)

Names (2): _corpus: _corpus:phase:pb-sc:fcc-a1  
_tdb: _tdb:PbSc-14Idd.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PbSc-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb): FCC_A1, type code %A, sha256 `f09786a7a2f576ea…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : PB% SC : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_

## HCP_A3 (Pb–Sc)

- Id: `phase:pb-sc:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1607.99 K, x(Sc) 0.98998–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sc:hcp-a3)

Names (2): _corpus: _corpus:phase:pb-sc:hcp-a3  
_tdb: _tdb:PbSc-14Idd.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PbSc-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb): HCP_A3, type code %A, sha256 `f09786a7a2f576ea…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : PB SC% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_

## LIQUID (Pb–Sc)

- Id: `phase:pb-sc:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 600.54–2500 K, x(Sc) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sc:liquid)

Names (2): _corpus: _corpus:phase:pb-sc:liquid  
_tdb: _tdb:PbSc-14Idd.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PbSc-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb): LIQUID, type code %, sha256 `f09786a7a2f576ea…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : PB SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_

## PB3SC5_D88 (Pb–Sc)

- Id: `phase:pb-sc:pb3sc5-d88`; status `assigned`
- Structure: Mn5Si3 · D8_8 · hP16 · P6_3/mcm (193); type `st:d8-8-mn5si3-hp16`; tier A: standard phase name; confidence high
- Stoichiometry: Pb 0.3750, Sc 0.6250
- Stability: stable in 1 of 1 calculated diagram(s): 300–1970.15 K, x(Sc) 0.625–0.625
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sc:pb3sc5-d88)

Names (2): _corpus: _corpus:phase:pb-sc:pb3sc5-d88  
_tdb: _tdb:PbSc-14Idd.tdb:PB3SC5_D88  


### TDB models of PB3SC5_D88 (1): PHASE and CONSTITUENT statements as written

[PbSc-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb): PB3SC5_D88, type code %, sha256 `f09786a7a2f576ea…`

~~~~text
48: PHASE PB3SC5_D88 % 2 3 5 !
49: CONST PB3SC5_D88 : PB : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
_assessment that models this phase_

## PB5SC6 (Pb–Sc)

- Id: `phase:pb-sc:pb5sc6`; status `assigned`
- Structure: Si5V6 · oI44 · Ibam (72); type `st:si5v6-oi44`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Pb 0.4545, Sc 0.5455
- Stability: stable in 1 of 1 calculated diagram(s): 300–1561.98 K, x(Sc) 0.54545–0.54545
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pb-sc:pb5sc6)

Names (4): _corpus: _corpus:phase:pb-sc:pb5sc6  
_mp: _mp:mp-aaabmgof  
_oqmd: _oqmd:oqmd-21582  
_tdb: _tdb:PbSc-14Idd.tdb:PB5SC6  


### TDB models of PB5SC6 (1): PHASE and CONSTITUENT statements as written

[PbSc-14Idd.tdb](https://orchid-project.org/data/databases/sgte-binary/PbSc-14Idd.tdb): PB5SC6, type code %, sha256 `f09786a7a2f576ea…`

~~~~text
43: PHASE PB5SC6 % 2 5 6 !
44: CONST PB5SC6 : PB : SC : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.131](https://doi.org/10.1016/j.jallcom.2013.11.131) A. Iddaoudi, C. Servant, N. Selhaoui, S. Kardellass, K. Mahdouk, L. Bouirden, Thermodynamic modeling of the RE–Pb (RE=Sc, Dy, Gd) systems, Journal of Alloys and Compounds 589, 192-199 (2014).  
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
