# V–Zn phases

> V–Zn system: 8 phases (tier A 4, tier B 1, liquid 1, gas 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/V-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/V-ZN.md

8 phases (tier A 4, tier B 1, liquid 1, gas 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=V-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/V-ZN.json) · [V–Zn system page](https://data.orchid-project.org/systems/V-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/V-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the V–Zn system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-v-zn-bcc-a2); _phase:v-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2183.33 K, x(Zn) 0–0.02893 | 2 | 2 |
| [FCC_A1](#phase-v-zn-fcc-a1); _phase:v-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [GAS](#phase-v-zn-gas); _phase:v-zn:gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 1179.8–4000 K, x(Zn) 0–1 | 0 | 2 |
| [HCP_A3](#phase-v-zn-hcp-a3); _phase:v-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1177.01 K, x(Zn) 0.99975–1 | 2 | 2 |
| [LIQUID](#phase-v-zn-liquid); _phase:v-zn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 691.85–3757.28 K, x(Zn) 0–1 | 6 | 2 |
| [V4ZN5](#phase-v-zn-v4zn5); _phase:v-zn:v4zn5_ | V4Zn5 · tI18 · I4/mmm (139) | tier B: DFT-supported (unique MP + OQMD match) | stable in 2 of 2 calculated diagram(s): 300–943.15 K, x(Zn) 0.55556–0.55556 | 11 | 2 |
| [VZN16](#phase-v-zn-vzn16); _phase:v-zn:vzn16_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–700.54 K, x(Zn) 0.94118–0.94118 | 2 | 1 |
| [VZN3_L12](#phase-v-zn-vzn3-l12); _phase:v-zn:vzn3-l12_ | AuCu3 · L1_2 · cP4 · Pm-3m (221) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–896.13 K, x(Zn) 0.75–0.75 | 4 | 2 |

## BCC_A2 (V–Zn)

- Id: `phase:v-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2183.33 K, x(Zn) 0–0.02893
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:bcc-a2)

Names (4): _corpus: _corpus:phase:v-zn:bcc-a2  
_paper: _paper:10.1016/j.calphad.2009.12.003:(V)  
_tdb: _tdb:VZn-10Cha.tdb:BCC_A2, tdb:VZn-11Wu.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): BCC_A2, type code %B, sha256 `d4533862db93cd15…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : V% ZN : VA : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): BCC_A2, type code %B, sha256 `8818a90f31db3069…`

~~~~text
51: PHASE BCC_A2 %B 2 1 3 !
52: CONST BCC_A2 : V% ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase_

## FCC_A1 (V–Zn)

- Id: `phase:v-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:fcc-a1)

Names (3): _corpus: _corpus:phase:v-zn:fcc-a1  
_tdb: _tdb:VZn-10Cha.tdb:FCC_A1, tdb:VZn-11Wu.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): FCC_A1, type code %A, sha256 `d4533862db93cd15…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : V ZN : VA : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): FCC_A1, type code %A, sha256 `8818a90f31db3069…`

~~~~text
46: PHASE FCC_A1 %A 2 1 1 !
47: CONST FCC_A1 : V ZN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase_

## GAS (V–Zn)

- Id: `phase:v-zn:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1179.8–4000 K, x(Zn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:gas)

Names (3): _corpus: _corpus:phase:v-zn:gas  
_tdb: _tdb:VZn-10Cha.tdb:GAS, tdb:VZn-11Wu.tdb:GAS  


### TDB models of GAS (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): GAS, type code %, sha256 `d4533862db93cd15…`

~~~~text
63: PHASE GAS:G % 1 1 !
64: CONST GAS:G : V ZN : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): GAS, type code %, sha256 `8818a90f31db3069…`

~~~~text
74: PHASE GAS:G % 1 1 !
75: CONST GAS:G : V ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase_

## HCP_A3 (V–Zn)

- Id: `phase:v-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1177.01 K, x(Zn) 0.99975–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:hcp-a3)

Names (4): _corpus: _corpus:phase:v-zn:hcp-a3  
_paper: _paper:10.1016/j.calphad.2009.12.003:(Zn)  
_tdb: _tdb:VZn-10Cha.tdb:HCP_A3, tdb:VZn-11Wu.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): HCP_A3, type code %A, sha256 `d4533862db93cd15…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : V ZN% : VA : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): HCP_A3, type code %A, sha256 `8818a90f31db3069…`

~~~~text
56: PHASE HCP_A3 %A 2 1 0.5 !
57: CONST HCP_A3 : V ZN% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase_

## LIQUID (V–Zn)

- Id: `phase:v-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 691.85–3757.28 K, x(Zn) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:liquid)

Names (4): _corpus: _corpus:phase:v-zn:liquid  
_paper: _paper:10.1016/j.calphad.2009.12.003:L  
_tdb: _tdb:VZn-10Cha.tdb:LIQUID, tdb:VZn-11Wu.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): LIQUID, type code %, sha256 `d4533862db93cd15…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : V ZN : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): LIQUID, type code %, sha256 `8818a90f31db3069…`

~~~~text
41: PHASE LIQUID:L % 1 1 !
42: CONST LIQUID:L : V ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase_

## V4ZN5 (V–Zn)

- Id: `phase:v-zn:v4zn5`; status `assigned`
- Structure: V4Zn5 · tI18 · I4/mmm (139); type `st:v4zn5-ti18`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: V 0.4444, Zn 0.5556
- Stability: stable in 2 of 2 calculated diagram(s): 300–943.15 K, x(Zn) 0.55556–0.55556
- Literature: 11 values (11 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:v4zn5)

Names (7): _corpus: _corpus:phase:v-zn:v4zn5  
_mp: _mp:mp-aaaabtrv  
_oqmd: _oqmd:oqmd-18177  
_paper: _paper:10.1016/j.calphad.2009.12.003:V4Zn5, paper:10.1016/j.calphad.2011.05.005:V4Zn5  
_tdb: _tdb:VZn-10Cha.tdb:V4ZN5, tdb:VZn-11Wu.tdb:V4ZN5  


### TDB models of V4ZN5 (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): V4ZN5, type code %, sha256 `d4533862db93cd15…`

~~~~text
55: PHASE V4ZN5 % 2 4 5 !
56: CONST V4ZN5 : V : ZN : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): V4ZN5, type code %, sha256 `8818a90f31db3069…`

~~~~text
61: PHASE V4ZN5 % 2 4 5 !
62: CONST V4ZN5 : V : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase; reports values for this phase_

## VZN16 (V–Zn)

- Id: `phase:v-zn:vzn16`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token
- Candidate (sgte_mmc2): (VZn16) — Hallstedt 2025 mmc2 row for VZN16: VZN16
- Stoichiometry: V 0.0588, Zn 0.9412
- Stability: stable in 1 of 1 calculated diagram(s): 300–700.54 K, x(Zn) 0.94118–0.94118
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:vzn16)

Names (3): _corpus: _corpus:phase:v-zn:vzn16  
_paper: _paper:10.1016/j.calphad.2011.05.005:VZn16  
_tdb: _tdb:VZn-11Wu.tdb:VZN16  


### TDB models of VZN16 (1): PHASE and CONSTITUENT statements as written

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): VZN16, type code %, sha256 `8818a90f31db3069…`

~~~~text
71: PHASE VZN16 % 2 1 16 !
72: CONST VZN16 : V : ZN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
_assessment that models this phase; reports values for this phase_

## VZN3_L12 (V–Zn)

- Id: `phase:v-zn:vzn3-l12`; status `assigned`
- Structure: AuCu3 · L1_2 · cP4 · Pm-3m (221); type `st:l1-2-aucu3-cp4`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaardi and oqmd-18189, space group 221
- Stoichiometry: V 0.2500, Zn 0.7500
- Stability: stable in 2 of 2 calculated diagram(s): 300–896.13 K, x(Zn) 0.75–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:v-zn:vzn3-l12)

Names (6): _corpus: _corpus:phase:v-zn:vzn3-l12  
_mp: _mp:mp-aaaaardi  
_oqmd: _oqmd:oqmd-18189  
_paper: _paper:10.1016/j.calphad.2009.12.003:VZn3  
_tdb: _tdb:VZn-10Cha.tdb:VZN3_L12, tdb:VZn-11Wu.tdb:VZN3_L12  


### TDB models of VZN3_L12 (2): PHASE and CONSTITUENT statements as written

[VZn-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-10Cha.tdb): VZN3_L12, type code %, sha256 `d4533862db93cd15…`

~~~~text
60: PHASE VZN3_L12 % 2 1 3 !
61: CONST VZN3_L12 : V : ZN : !
~~~~

[VZn-11Wu.tdb](https://orchid-project.org/data/databases/sgte-binary/VZn-11Wu.tdb): VZN3_L12, type code %, sha256 `8818a90f31db3069…`

~~~~text
66: PHASE VZN3_L12 % 2 1 3 !
67: CONST VZN3_L12 : V : ZN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2009.12.003](https://doi.org/10.1016/j.calphad.2009.12.003) Keke Chang, Yong Du, Weihua Sun, Honghui Xu, LiangCai Zhou, Thermodynamic assessment of the V–Zn system supported by key experiments and first-principles calculations, Calphad 34, 75-80 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2011.05.005](https://doi.org/10.1016/j.calphad.2011.05.005) Changjun Wu, Xuping Su, Daniel Liu, Xinming Wang, Jianhua Wang, Zhi Li et al., The V–Zn binary system: New experimental results and thermodynamic assessment, Calphad 35, 403-410 (2011).  
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
