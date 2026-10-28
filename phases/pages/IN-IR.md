# In–Ir phases

> In–Ir system: 8 phases (tier A 6, tier C 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/IN-IR.html · Markdown: https://data.orchid-project.org/phases/pages/IN-IR.md

8 phases (tier A 6, tier C 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=IN-IR) · [full JSON](https://data.orchid-project.org/phases/systems/IN-IR.json) · [In–Ir system page](https://data.orchid-project.org/systems/IN-IR.html) · [Markdown](https://data.orchid-project.org/phases/pages/IN-IR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the In–Ir system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-in-ir-a6-tetragonal); _phase:in-ir:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Ir) 0–0 | 6 | 1 |
| [BCC_A2](#phase-in-ir-bcc-a2); _phase:in-ir:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-in-ir-fcc-a1); _phase:in-ir:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3998.99 K, x(Ir) 0.96261–1 | 6 | 1 |
| [HCP_A3](#phase-in-ir-hcp-a3); _phase:in-ir:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [IN2IR_CB](#phase-in-ir-in2ir-cb); _phase:in-ir:in2ir-cb_ | CuMg2 · C_b · oF48 · Fddd (70) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1461.07 K, x(Ir) 0.30808–0.38395 | 17 | 1 |
| [IN3IR_HT](#phase-in-ir-in3ir); _phase:in-ir:in3ir_ | In3Ir · tP16 · P4_2/mnm (136) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 620.57–1254.08 K, x(Ir) 0.23657–0.24999 | 15 | 1 |
| [IN3IR_D011](#phase-in-ir-in3ir-d011); _phase:in-ir:in3ir-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–634 K, x(Ir) 0.23822–0.25 | 15 | 1 |
| [LIQUID](#phase-in-ir-liquid); _phase:in-ir:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 429.75–4000 K, x(Ir) 0–1 | 26 | 1 |

## TETRAGONAL_A6 (In–Ir)

- Id: `phase:in-ir:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stoichiometry: In 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–429.75 K, x(Ir) 0–0
- Literature: 6 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:a6-tetragonal)

Names (4): _corpus: _corpus:phase:in-ir:a6-tetragonal, corpus:phase:in-ir:tetragonal-a6  
_paper: _paper:10.1016/j.tca.2010.12.019:In  
_tdb: _tdb:InIr-11Ser.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): TETRAGONAL_A6, type code %, sha256 `08d4e25130797918…`

~~~~text
45: PHASE TETRAGONAL_A6 % 1 1 !
46: CONST TETRAGONAL_A6 : IN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00287-6](https://doi.org/10.1016/s0925-8388%2802%2900287-6) Hans Flandorfer, Klaus W Richter, Erhard Hayer, Herbert Ipser, Gabriella Borzone, Jean-Pierre Bros, The binary system In–Ir: a new investigation of phase relationships, crystal structures, and enthalpies of mixing, Journal of Alloys and Compounds 345, 130-139 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00507-1](https://doi.org/10.1016/s0925-8388%2899%2900507-1) P. Anres, P. Fossati, K. Richter, M. Gambino, M. Gaune-Escard, J.-P. Bros, Thermodynamics of the \[Ir–In\] system, Journal of Alloys and Compounds 296, 119-127 (2000).  
_cited as the source of values for this phase_

## BCC_A2 (In–Ir)

- Id: `phase:in-ir:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:bcc-a2)

Names (2): _corpus: _corpus:phase:in-ir:bcc-a2  
_tdb: _tdb:InIr-11Ser.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): BCC_A2, type code %B, sha256 `08d4e25130797918…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : IN IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase_

## FCC_A1 (In–Ir)

- Id: `phase:in-ir:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3998.99 K, x(Ir) 0.96261–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:fcc-a1)

Names (3): _corpus: _corpus:phase:in-ir:fcc-a1  
_paper: _paper:10.1016/j.tca.2010.12.019:(Ir)  
_tdb: _tdb:InIr-11Ser.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): FCC_A1, type code %A, sha256 `08d4e25130797918…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : IN IR% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00287-6](https://doi.org/10.1016/s0925-8388%2802%2900287-6) Hans Flandorfer, Klaus W Richter, Erhard Hayer, Herbert Ipser, Gabriella Borzone, Jean-Pierre Bros, The binary system In–Ir: a new investigation of phase relationships, crystal structures, and enthalpies of mixing, Journal of Alloys and Compounds 345, 130-139 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00507-1](https://doi.org/10.1016/s0925-8388%2899%2900507-1) P. Anres, P. Fossati, K. Richter, M. Gambino, M. Gaune-Escard, J.-P. Bros, Thermodynamics of the \[Ir–In\] system, Journal of Alloys and Compounds 296, 119-127 (2000).  
_cited as the source of values for this phase_

## HCP_A3 (In–Ir)

- Id: `phase:in-ir:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:hcp-a3)

Names (2): _corpus: _corpus:phase:in-ir:hcp-a3  
_tdb: _tdb:InIr-11Ser.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): HCP_A3, type code %A, sha256 `08d4e25130797918…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : IN IR : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase_

## IN2IR_CB (In–Ir)

- Id: `phase:in-ir:in2ir-cb`; status `assigned`
- Structure: CuMg2 · C_b · oF48 · Fddd (70); type `st:c-b-cumg2-of48`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in InIr-11Ser.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1461.07 K, x(Ir) 0.30808–0.38395
- Literature: 17 values (17 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:in2ir-cb)

Names (4): _corpus: _corpus:phase:in-ir:in2ir-cb  
_paper: _paper:10.1016/j.tca.2010.12.019:In2 Ir, paper:10.1016/j.tca.2010.12.019:In2Ir  
_tdb: _tdb:InIr-11Ser.tdb:IN2IR_CB  


### TDB models of IN2IR_CB (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): IN2IR_CB, type code %, sha256 `08d4e25130797918…`

~~~~text
60: PHASE IN2IR_CB % 2 2 1 !
61: CONST IN2IR_CB : IN% IR : IN IR% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00287-6](https://doi.org/10.1016/s0925-8388%2802%2900287-6) Hans Flandorfer, Klaus W Richter, Erhard Hayer, Herbert Ipser, Gabriella Borzone, Jean-Pierre Bros, The binary system In–Ir: a new investigation of phase relationships, crystal structures, and enthalpies of mixing, Journal of Alloys and Compounds 345, 130-139 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00507-1](https://doi.org/10.1016/s0925-8388%2899%2900507-1) P. Anres, P. Fossati, K. Richter, M. Gambino, M. Gaune-Escard, J.-P. Bros, Thermodynamics of the \[Ir–In\] system, Journal of Alloys and Compounds 296, 119-127 (2000).  
_cited as the source of values for this phase_

## IN3IR_HT (In–Ir)

- Id: `phase:in-ir:in3ir`; status `assigned`
- Structure: In3Ir · tP16 · P4_2/mnm (136); type `st:in3ir-tp16`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 620.57–1254.08 K, x(Ir) 0.23657–0.24999
- Literature: 15 values (14 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:in3ir)

Names (7): _corpus: _corpus:phase:in-ir:in3ir, corpus:phase:in-ir:in3ir-ht  
_paper: _paper:10.1016/j.tca.2010.12.019:In3 Ir-HT, paper:10.1016/j.tca.2010.12.019:In3 Ir_HT, paper:10.1016/j.tca.2010.12.019:In3Ir-HT, paper:10.1016/j.tca.2010.12.019:In3Ir_HT  
_tdb: _tdb:InIr-11Ser.tdb:IN3IR_HT  


### TDB models of IN3IR_HT (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): IN3IR_HT, type code %, sha256 `08d4e25130797918…`

~~~~text
55: PHASE IN3IR_HT % 2 3 1 !
56: CONST IN3IR_HT : IN : IN IR% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00287-6](https://doi.org/10.1016/s0925-8388%2802%2900287-6) Hans Flandorfer, Klaus W Richter, Erhard Hayer, Herbert Ipser, Gabriella Borzone, Jean-Pierre Bros, The binary system In–Ir: a new investigation of phase relationships, crystal structures, and enthalpies of mixing, Journal of Alloys and Compounds 345, 130-139 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00507-1](https://doi.org/10.1016/s0925-8388%2899%2900507-1) P. Anres, P. Fossati, K. Richter, M. Gambino, M. Gaune-Escard, J.-P. Bros, Thermodynamics of the \[Ir–In\] system, Journal of Alloys and Compounds 296, 119-127 (2000).  
_cited as the source of values for this phase_

## IN3IR_D011 (In–Ir)

- Id: `phase:in-ir:in3ir-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–634 K, x(Ir) 0.23822–0.25
- Literature: 15 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:in3ir-d011)

Names (5): _corpus: _corpus:phase:in-ir:in3ir-d011  
_paper: _paper:10.1016/j.tca.2010.12.019:In3 Ir-LT, paper:10.1016/j.tca.2010.12.019:In3Ir-LT, paper:10.1016/j.tca.2010.12.019:In3Ir_LT  
_tdb: _tdb:InIr-11Ser.tdb:IN3IR_D011  


### TDB models of IN3IR_D011 (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): IN3IR_D011, type code %, sha256 `08d4e25130797918…`

~~~~text
50: PHASE IN3IR_D011 % 2 3 1 !
51: CONST IN3IR_D011 : IN : IN IR% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00287-6](https://doi.org/10.1016/s0925-8388%2802%2900287-6) Hans Flandorfer, Klaus W Richter, Erhard Hayer, Herbert Ipser, Gabriella Borzone, Jean-Pierre Bros, The binary system In–Ir: a new investigation of phase relationships, crystal structures, and enthalpies of mixing, Journal of Alloys and Compounds 345, 130-139 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00507-1](https://doi.org/10.1016/s0925-8388%2899%2900507-1) P. Anres, P. Fossati, K. Richter, M. Gambino, M. Gaune-Escard, J.-P. Bros, Thermodynamics of the \[Ir–In\] system, Journal of Alloys and Compounds 296, 119-127 (2000).  
_cited as the source of values for this phase_

## LIQUID (In–Ir)

- Id: `phase:in-ir:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 429.75–4000 K, x(Ir) 0–1
- Literature: 26 values (23 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:in-ir:liquid)

Names (4): _corpus: _corpus:phase:in-ir:liquid  
_paper: _paper:10.1016/j.tca.2010.12.019:Liq, paper:10.1016/j.tca.2010.12.019:liquid  
_tdb: _tdb:InIr-11Ser.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[InIr-11Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/InIr-11Ser.tdb): LIQUID, type code %, sha256 `08d4e25130797918…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : IN IR : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.tca.2010.12.019](https://doi.org/10.1016/j.tca.2010.12.019) Colette Servant, Mohamed Idbenali, Thermodynamic assessment of the In–Ir system in the In rich part, Thermochimica Acta 517, 1-8 (2011).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/s0925-8388(02)00287-6](https://doi.org/10.1016/s0925-8388%2802%2900287-6) Hans Flandorfer, Klaus W Richter, Erhard Hayer, Herbert Ipser, Gabriella Borzone, Jean-Pierre Bros, The binary system In–Ir: a new investigation of phase relationships, crystal structures, and enthalpies of mixing, Journal of Alloys and Compounds 345, 130-139 (2002).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(99)00507-1](https://doi.org/10.1016/s0925-8388%2899%2900507-1) P. Anres, P. Fossati, K. Richter, M. Gambino, M. Gaune-Escard, J.-P. Bros, Thermodynamics of the \[Ir–In\] system, Journal of Alloys and Compounds 296, 119-127 (2000).  
_cited as the source of values for this phase_

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
