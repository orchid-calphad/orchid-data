# Mo–V phases

> Mo–V system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-V.html · Markdown: https://data.orchid-project.org/phases/pages/MO-V.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-V) · [full JSON](https://data.orchid-project.org/phases/systems/MO-V.json) · [Mo–V system page](https://data.orchid-project.org/systems/MO-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–V system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-v-bcc-a2); _phase:mo-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2950.5 K, x(V) 0–1 | 0 | 3 |
| [FCC_A1](#phase-mo-v-fcc-a1); _phase:mo-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-mo-v-hcp-a3); _phase:mo-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-mo-v-liquid); _phase:mo-v:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 300.5–4000 K, x(V) 0–1 | 0 | 3 |

## BCC_A2 (Mo–V)

- Id: `phase:mo-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2950.5 K, x(V) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-v:bcc-a2)

Names (4): _corpus: _corpus:phase:mo-v:bcc-a2  
_tdb: _tdb:MoV-02Bra-LB.tdb:BCC_A2, tdb:MoV-21Yan.tdb:BCC_A2, tdb:MoV-99Zhe.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[MoV-02Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-02Bra-LB.tdb): BCC_A2, type code %B, sha256 `135f4ef0257cd1b9…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MO V : VA : !
~~~~

[MoV-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-21Yan.tdb): BCC_A2, type code %B, sha256 `6712991e1b1c94fe…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : MO V : VA : !
~~~~

[MoV-99Zhe.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-99Zhe.tdb): BCC_A2, type code %B, sha256 `60f985a4117e3d9a…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : MO V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2020.157509](https://doi.org/10.1016/j.jallcom.2020.157509) Wenkui Yang, Zhikui Gao, Changrong Li, Cuiping Guo, Zhenmin Du, Experimental measurement and thermodynamic optimization on the solidus miscibility gap of the Mo-V binary and the Mo-Nb-V ternary systems, Journal of Alloys and Compounds 857, 157509 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(02)00057-3](https://doi.org/10.1016/S0364-5916%2802%2900057-3) J. Bratberg, K. Frisk, Calphad, 26, 459-76(2002).  
_assessment that models this phase_
- [doi:10.1361/105497199770340897](https://doi.org/10.1361/105497199770340897) F. Zheng, B. B. Argent, J. F. Smith, Thermodynamic computation of the Mo-V binary phase diagram, JPE 20, 370-372 (1999).  
_assessment that models this phase_

## FCC_A1 (Mo–V)

- Id: `phase:mo-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-v:fcc-a1)

Names (4): _corpus: _corpus:phase:mo-v:fcc-a1  
_tdb: _tdb:MoV-02Bra-LB.tdb:FCC_A1, tdb:MoV-21Yan.tdb:FCC_A1, tdb:MoV-99Zhe.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[MoV-02Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-02Bra-LB.tdb): FCC_A1, type code %A, sha256 `135f4ef0257cd1b9…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MO V : VA : !
~~~~

[MoV-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-21Yan.tdb): FCC_A1, type code %A, sha256 `6712991e1b1c94fe…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : MO V : VA : !
~~~~

[MoV-99Zhe.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-99Zhe.tdb): FCC_A1, type code %A, sha256 `60f985a4117e3d9a…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : MO V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2020.157509](https://doi.org/10.1016/j.jallcom.2020.157509) Wenkui Yang, Zhikui Gao, Changrong Li, Cuiping Guo, Zhenmin Du, Experimental measurement and thermodynamic optimization on the solidus miscibility gap of the Mo-V binary and the Mo-Nb-V ternary systems, Journal of Alloys and Compounds 857, 157509 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(02)00057-3](https://doi.org/10.1016/S0364-5916%2802%2900057-3) J. Bratberg, K. Frisk, Calphad, 26, 459-76(2002).  
_assessment that models this phase_
- [doi:10.1361/105497199770340897](https://doi.org/10.1361/105497199770340897) F. Zheng, B. B. Argent, J. F. Smith, Thermodynamic computation of the Mo-V binary phase diagram, JPE 20, 370-372 (1999).  
_assessment that models this phase_

## HCP_A3 (Mo–V)

- Id: `phase:mo-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-v:hcp-a3)

Names (4): _corpus: _corpus:phase:mo-v:hcp-a3  
_tdb: _tdb:MoV-02Bra-LB.tdb:HCP_A3, tdb:MoV-21Yan.tdb:HCP_A3, tdb:MoV-99Zhe.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[MoV-02Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-02Bra-LB.tdb): HCP_A3, type code %A, sha256 `135f4ef0257cd1b9…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MO V : VA : !
~~~~

[MoV-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-21Yan.tdb): HCP_A3, type code %A, sha256 `6712991e1b1c94fe…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : MO V : VA : !
~~~~

[MoV-99Zhe.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-99Zhe.tdb): HCP_A3, type code %A, sha256 `60f985a4117e3d9a…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : MO V : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2020.157509](https://doi.org/10.1016/j.jallcom.2020.157509) Wenkui Yang, Zhikui Gao, Changrong Li, Cuiping Guo, Zhenmin Du, Experimental measurement and thermodynamic optimization on the solidus miscibility gap of the Mo-V binary and the Mo-Nb-V ternary systems, Journal of Alloys and Compounds 857, 157509 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(02)00057-3](https://doi.org/10.1016/S0364-5916%2802%2900057-3) J. Bratberg, K. Frisk, Calphad, 26, 459-76(2002).  
_assessment that models this phase_
- [doi:10.1361/105497199770340897](https://doi.org/10.1361/105497199770340897) F. Zheng, B. B. Argent, J. F. Smith, Thermodynamic computation of the Mo-V binary phase diagram, JPE 20, 370-372 (1999).  
_assessment that models this phase_

## LIQUID (Mo–V)

- Id: `phase:mo-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300.5–4000 K, x(V) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-v:liquid)

Names (4): _corpus: _corpus:phase:mo-v:liquid  
_tdb: _tdb:MoV-02Bra-LB.tdb:LIQUID, tdb:MoV-21Yan.tdb:LIQUID, tdb:MoV-99Zhe.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[MoV-02Bra-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-02Bra-LB.tdb): LIQUID, type code %, sha256 `135f4ef0257cd1b9…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MO V : !
~~~~

[MoV-21Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-21Yan.tdb): LIQUID, type code %, sha256 `6712991e1b1c94fe…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : MO V : !
~~~~

[MoV-99Zhe.tdb](https://orchid-project.org/data/databases/sgte-binary/MoV-99Zhe.tdb): LIQUID, type code %, sha256 `60f985a4117e3d9a…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : MO V : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.jallcom.2020.157509](https://doi.org/10.1016/j.jallcom.2020.157509) Wenkui Yang, Zhikui Gao, Changrong Li, Cuiping Guo, Zhenmin Du, Experimental measurement and thermodynamic optimization on the solidus miscibility gap of the Mo-V binary and the Mo-Nb-V ternary systems, Journal of Alloys and Compounds 857, 157509 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(02)00057-3](https://doi.org/10.1016/S0364-5916%2802%2900057-3) J. Bratberg, K. Frisk, Calphad, 26, 459-76(2002).  
_assessment that models this phase_
- [doi:10.1361/105497199770340897](https://doi.org/10.1361/105497199770340897) F. Zheng, B. B. Argent, J. F. Smith, Thermodynamic computation of the Mo-V binary phase diagram, JPE 20, 370-372 (1999).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
