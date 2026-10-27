# Ba–Ga phases

> Ba–Ga system: 10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BA-GA.html · Markdown: https://data.orchid-project.org/phases/pages/BA-GA.md

10 phases (tier A 6, tier B 1, tier C 1, liquid 1, needs_review 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BA-GA) · [full JSON](https://data.orchid-project.org/phases/systems/BA-GA.json) · [Ba–Ga system page](https://data.orchid-project.org/systems/BA-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/BA-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ba–Ga system (10)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-ba-ga-a11-orthorhombic); _phase:ba-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Ga) 1–1 | 0 | 1 |
| [BA10GA](#phase-ba-ga-ba10ga); _phase:ba-ga:ba10ga_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–730.01 K, x(Ga) 0.09091–0.09091 | 0 | 1 |
| [BA5GA6](#phase-ba-ga-ba5ga6); _phase:ba-ga:ba5ga6_ | Ba5Ga6 · hP24 · P-6c2 (188) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–859.7 K, x(Ga) 0.54545–0.54545 | 0 | 1 |
| [BA8GA7](#phase-ba-ga-ba8ga7); _phase:ba-ga:ba8ga7_ | Ba8Ga7 · cP60 · P2_13 (198) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–830.03 K, x(Ga) 0.46667–0.46667 | 1 | 1 |
| [BAGA2_C32](#phase-ba-ga-baga2-c32); _phase:ba-ga:baga2-c32_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1153.55 K, x(Ga) 0.66667–0.66667 | 0 | 1 |
| [BAGA4_D13](#phase-ba-ga-baga4-d13); _phase:ba-ga:baga4-d13_ | Al4Ba · D1_3 · tI10 · I4/mmm (139) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1297.22 K, x(Ga) 0.8–0.8 | 0 | 1 |
| [BCC_A2](#phase-ba-ga-bcc-a2); _phase:ba-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Ga) 0–1e-05 | 0 | 1 |
| [FCC_A1](#phase-ba-ga-fcc-a1); _phase:ba-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-ba-ga-hcp-a3); _phase:ba-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ba-ga-liquid); _phase:ba-ga:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Ga) 0–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (Ba–Ga)

- Id: `phase:ba-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(Ga) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:ba-ga:a11-orthorhombic  
_tdb: _tdb:BaGa-13Li.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): ORTHORHOMBIC_A11, type code %, sha256 `b2225c3190b4435f…`

~~~~text
41: PHASE ORTHORHOMBIC_A11 % 1 1 !
42: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BA10GA (Ba–Ga)

- Id: `phase:ba-ga:ba10ga`; status `needs_review`
- No structure assigned. Why: assessment_declared_compound_differs_from_model_composition; no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): Al10V · cF176 · Fd-3m (227) — Hallstedt 2025 mmc2 row for BA10GA: Ba19Ga
- Candidate (tdb_comment): Al10V · cF176 · Fd-3m — BaGa-13Li.tdb: 'Prototype Al10V (cF176, Fd-3m)'
- Stoichiometry: Ba 0.9091, Ga 0.0909
- Stability: stable in 1 of 1 calculated diagram(s): 300–730.01 K, x(Ga) 0.09091–0.09091
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:ba10ga)

Names (2): _corpus: _corpus:phase:ba-ga:ba10ga  
_tdb: _tdb:BaGa-13Li.tdb:BA10GA  


### TDB models of BA10GA (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): BA10GA, type code %, sha256 `b2225c3190b4435f…`

~~~~text
46: PHASE BA10GA % 2 10 1 !
47: CONST BA10GA : BA : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BA5GA6 (Ba–Ga)

- Id: `phase:ba-ga:ba5ga6`; status `assigned`
- Structure: Ba5Ga6 · hP24 · P-6c2 (188); type `st:ba5ga6-hp24`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_oqmd, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Ba 0.4545, Ga 0.5455
- Stability: stable in 1 of 1 calculated diagram(s): 300–859.7 K, x(Ga) 0.54545–0.54545
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:ba5ga6)

Names (2): _corpus: _corpus:phase:ba-ga:ba5ga6  
_tdb: _tdb:BaGa-13Li.tdb:BA5GA6  


### TDB models of BA5GA6 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): BA5GA6, type code %, sha256 `b2225c3190b4435f…`

~~~~text
56: PHASE BA5GA6 % 2 5 6 !
57: CONST BA5GA6 : BA : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BA8GA7 (Ba–Ga)

- Id: `phase:ba-ga:ba8ga7`; status `assigned`
- Structure: Ba8Ga7 · cP60 · P2_13 (198); type `st:ba8ga7-cp60`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Ba 0.5333, Ga 0.4667
- Stability: stable in 1 of 1 calculated diagram(s): 300–830.03 K, x(Ga) 0.46667–0.46667
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:ba8ga7)

Names (5): _corpus: _corpus:phase:ba-ga:ba8ga7  
_mp: _mp:mp-aaaabtaj  
_oqmd: _oqmd:oqmd-55151  
_paper: _paper:10.1016/j.calphad.2013.09.002:Ba8Ga7  
_tdb: _tdb:BaGa-13Li.tdb:BA8GA7  


### TDB models of BA8GA7 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): BA8GA7, type code %, sha256 `b2225c3190b4435f…`

~~~~text
51: PHASE BA8GA7 % 2 8 7 !
52: CONST BA8GA7 : BA : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase; reports values for this phase_

## BAGA2_C32 (Ba–Ga)

- Id: `phase:ba-ga:baga2-c32`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaabux and oqmd-94273, space group 191
- Stoichiometry: Ba 0.3333, Ga 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1153.55 K, x(Ga) 0.66667–0.66667
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:baga2-c32)

Names (4): _corpus: _corpus:phase:ba-ga:baga2-c32  
_mp: _mp:mp-aaaaabux  
_oqmd: _oqmd:oqmd-94273  
_tdb: _tdb:BaGa-13Li.tdb:BAGA2_C32  


### TDB models of BAGA2_C32 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): BAGA2_C32, type code %, sha256 `b2225c3190b4435f…`

~~~~text
61: PHASE BAGA2_C32 % 2 1 2 !
62: CONST BAGA2_C32 : BA : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BAGA4_D13 (Ba–Ga)

- Id: `phase:ba-ga:baga4-d13`; status `assigned`
- Structure: Al4Ba · D1_3 · tI10 · I4/mmm (139); type `st:d1-3-al4ba-ti10`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaamx and oqmd-9950, space group 139
- Stoichiometry: Ba 0.2000, Ga 0.8000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1297.22 K, x(Ga) 0.8–0.8
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:baga4-d13)

Names (4): _corpus: _corpus:phase:ba-ga:baga4-d13  
_mp: _mp:mp-aaaaaamx  
_oqmd: _oqmd:oqmd-9950  
_tdb: _tdb:BaGa-13Li.tdb:BAGA4_D13  


### TDB models of BAGA4_D13 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): BAGA4_D13, type code %, sha256 `b2225c3190b4435f…`

~~~~text
66: PHASE BAGA4_D13 % 2 1 4 !
67: CONST BAGA4_D13 : BA : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BCC_A2 (Ba–Ga)

- Id: `phase:ba-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1000 K, x(Ga) 0–1e-05
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:bcc-a2)

Names (2): _corpus: _corpus:phase:ba-ga:bcc-a2  
_tdb: _tdb:BaGa-13Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): BCC_A2, type code %B, sha256 `b2225c3190b4435f…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : BA% GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## FCC_A1 (Ba–Ga)

- Id: `phase:ba-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:fcc-a1)

Names (2): _corpus: _corpus:phase:ba-ga:fcc-a1  
_tdb: _tdb:BaGa-13Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): FCC_A1, type code %A, sha256 `b2225c3190b4435f…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : BA GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## HCP_A3 (Ba–Ga)

- Id: `phase:ba-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:hcp-a3)

Names (2): _corpus: _corpus:phase:ba-ga:hcp-a3  
_tdb: _tdb:BaGa-13Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): HCP_A3, type code %A, sha256 `b2225c3190b4435f…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : BA GA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## LIQUID (Ba–Ga)

- Id: `phase:ba-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–2500 K, x(Ga) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ba-ga:liquid)

Names (2): _corpus: _corpus:phase:ba-ga:liquid  
_tdb: _tdb:BaGa-13Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[BaGa-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/BaGa-13Li.tdb): LIQUID, type code %, sha256 `b2225c3190b4435f…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : BA GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

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
