# Pt–V phases

> Pt–V system: 8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PT-V.html · Markdown: https://data.orchid-project.org/phases/pages/PT-V.md

8 phases (tier A 6, tier C 1, liquid 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PT-V) · [full JSON](https://data.orchid-project.org/phases/systems/PT-V.json) · [Pt–V system page](https://data.orchid-project.org/systems/PT-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/PT-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pt–V system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-pt-v-bcc-a2); _phase:pt-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2187.75 K, x(V) 0.89535–1 | 4 | 1 |
| [FCC_A1](#phase-pt-v-fcc-a1); _phase:pt-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2076.05 K, x(V) 0–0.56405 | 16 | 1 |
| [HCP_A3](#phase-pt-v-hcp-a3); _phase:pt-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pt-v-liquid); _phase:pt-v:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 300.5–4000 K, x(V) 0–1 | 8 | 1 |
| [PT2V](#phase-pt-v-pt2v); _phase:pt-v:pt2v_ | MoPt2 · oI6 · Immm (71) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1372.35 K, x(V) 0.31971–0.33579 | 6 | 1 |
| [PT3V_D022](#phase-pt-v-pt3v-d022); _phase:pt-v:pt3v-d022_ | Al3Ti · D0_22 · tI8 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1286.39 K, x(V) 0.20991–0.2555 | 4 | 1 |
| [PTV_B19](#phase-pt-v-ptv-b19); _phase:pt-v:ptv-b19_ | AuCd · B19 · oP4 · Pmma (51) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1777.74 K, x(V) 0.49963–0.51893 | 6 | 1 |
| [PTV3_A15](#phase-pt-v-ptv3-a15); _phase:pt-v:ptv3-a15_ | Cr3Si · A15 · cP8 · Pm-3n (223) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2079.92 K, x(V) 0.67354–0.82049 | 6 | 1 |

## BCC_A2 (Pt–V)

- Id: `phase:pt-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2187.75 K, x(V) 0.89535–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:bcc-a2)

Names (3): _corpus: _corpus:phase:pt-v:bcc-a2  
_paper: _paper:10.1016/j.intermet.2008.01.002:(V)  
_tdb: _tdb:PtV-08Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): BCC_A2, type code %B, sha256 `8cbc6690005d46d1…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : PT V% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Pt–V)

- Id: `phase:pt-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2076.05 K, x(V) 0–0.56405
- Literature: 16 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:fcc-a1)

Names (3): _corpus: _corpus:phase:pt-v:fcc-a1  
_paper: _paper:10.1016/j.intermet.2008.01.002:(Pt)  
_tdb: _tdb:PtV-08Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): FCC_A1, type code %A, sha256 `8cbc6690005d46d1…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : PT% V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Pt–V)

- Id: `phase:pt-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:hcp-a3)

Names (2): _corpus: _corpus:phase:pt-v:hcp-a3  
_tdb: _tdb:PtV-08Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): HCP_A3, type code %, sha256 `8cbc6690005d46d1…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : PT V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase_

## LIQUID (Pt–V)

- Id: `phase:pt-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.5–4000 K, x(V) 0–1
- Literature: 8 values (8 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:liquid)

Names (3): _corpus: _corpus:phase:pt-v:liquid  
_paper: _paper:10.1016/j.intermet.2008.01.002:L  
_tdb: _tdb:PtV-08Wan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): LIQUID, type code %, sha256 `8cbc6690005d46d1…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : PT V : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## PT2V (Pt–V)

- Id: `phase:pt-v:pt2v`; status `assigned`
- Structure: MoPt2 · oI6 · Immm (71); type `st:mopt2-oi6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, off_stoichiometric_model); structure as stated in the SGTE crystallographic table for this phase name and system
- Stability: stable in 1 of 1 calculated diagram(s): 300–1372.35 K, x(V) 0.31971–0.33579
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:pt2v)

Names (3): _corpus: _corpus:phase:pt-v:pt2v  
_paper: _paper:10.1016/j.intermet.2008.01.002:Pt2V  
_tdb: _tdb:PtV-08Wan.tdb:PT2V  


### TDB models of PT2V (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): PT2V, type code %, sha256 `8cbc6690005d46d1…`

~~~~text
47: PHASE PT2V % 2 2 1 !
48: CONST PT2V : PT% V : PT V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## PT3V_D022 (Pt–V)

- Id: `phase:pt-v:pt3v-d022`; status `assigned`
- Structure: Al3Ti · D0_22 · tI8 · I4/mmm (139); type `st:d0-22-al3ti-ti8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtV-08Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1286.39 K, x(V) 0.20991–0.2555
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:pt3v-d022)

Names (3): _corpus: _corpus:phase:pt-v:pt3v-d022  
_paper: _paper:10.1016/j.intermet.2008.01.002:Pt3V  
_tdb: _tdb:PtV-08Wan.tdb:PT3V_D022  


### TDB models of PT3V_D022 (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): PT3V_D022, type code %, sha256 `8cbc6690005d46d1…`

~~~~text
42: PHASE PT3V_D022 % 2 3 1 !
43: CONST PT3V_D022 : PT% V : PT V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## PTV_B19 (Pt–V)

- Id: `phase:pt-v:ptv-b19`; status `assigned`
- Structure: AuCd · B19 · oP4 · Pmma (51); type `st:b19-aucd-op4`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtV-08Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1777.74 K, x(V) 0.49963–0.51893
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:ptv-b19)

Names (3): _corpus: _corpus:phase:pt-v:ptv-b19  
_paper: _paper:10.1016/j.intermet.2008.01.002:PtV  
_tdb: _tdb:PtV-08Wan.tdb:PTV_B19  


### TDB models of PTV_B19 (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): PTV_B19, type code %, sha256 `8cbc6690005d46d1…`

~~~~text
52: PHASE PTV_B19 % 2 1 1 !
53: CONST PTV_B19 : PT% V : PT V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## PTV3_A15 (Pt–V)

- Id: `phase:pt-v:ptv3-a15`; status `assigned`
- Structure: Cr3Si · A15 · cP8 · Pm-3n (223); type `st:a15-cr3si-cp8`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in PtV-08Wan.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–2079.92 K, x(V) 0.67354–0.82049
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pt-v:ptv3-a15)

Names (3): _corpus: _corpus:phase:pt-v:ptv3-a15  
_paper: _paper:10.1016/j.intermet.2008.01.002:PtV3  
_tdb: _tdb:PtV-08Wan.tdb:PTV3_A15  


### TDB models of PTV3_A15 (1): PHASE and CONSTITUENT statements as written

[PtV-08Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/PtV-08Wan.tdb): PTV3_A15, type code %, sha256 `8cbc6690005d46d1…`

~~~~text
57: PHASE PTV3_A15 % 2 1 3 !
58: CONST PTV3_A15 : PT% V : PT V% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.intermet.2008.01.002](https://doi.org/10.1016/j.intermet.2008.01.002) C.P. Wang, A.Q. Zheng, X.J. Liu, Thermodynamic assessments of the V–Ge and V–Pt systems, Intermetallics 16, 544-549 (2008).  
_assessment that models this phase; reports values for this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
