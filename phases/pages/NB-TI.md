# Nb–Ti phases

> Nb–Ti system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-TI.html · Markdown: https://data.orchid-project.org/phases/pages/NB-TI.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-TI) · [full JSON](https://data.orchid-project.org/phases/systems/NB-TI.json) · [Nb–Ti system page](https://data.orchid-project.org/systems/NB-TI.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-TI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Ti system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-ti-bcc-a2); _phase:nb-ti:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2765.99 K, x(Ti) 0–1 | 0 | 5 |
| [OMEGA_C32](#phase-nb-ti-c32-omega); _phase:nb-ti:c32-omega_ | AlB2 · C32 · hP3 · P6/mmm (191) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-nb-ti-fcc-a1); _phase:nb-ti:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 5 calculated diagram(s) | 0 | 5 |
| [HCP_A3](#phase-nb-ti-hcp-a3); _phase:nb-ti:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 5 of 5 calculated diagram(s): 300–2746.9 K, x(Ti) 0.96931–1 | 0 | 5 |
| [LIQUID](#phase-nb-ti-liquid); _phase:nb-ti:liquid_ | liquid | liquid | stable in 5 of 5 calculated diagram(s): 1155–4000 K, x(Ti) 0–1 | 0 | 5 |

## BCC_A2 (Nb–Ti)

- Id: `phase:nb-ti:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2765.99 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ti:bcc-a2)

Names (6): _corpus: _corpus:phase:nb-ti:bcc-a2  
_tdb: _tdb:NbTi-01Zha-LB.tdb:BCC_A2, tdb:NbTi-16Yan.tdb:BCC_A2, tdb:NbTi-18Hu.tdb:BCC_A2, tdb:NbTi-94Har.tdb:BCC_A2, tdb:NbTi-98Sau.tdb:BCC_A2  


### TDB models of BCC_A2 (5): PHASE and CONSTITUENT statements as written

[NbTi-01Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-01Zha-LB.tdb): BCC_A2, type code %B, sha256 `cc166cb688a0d62e…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% TI% : VA : !
~~~~

[NbTi-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-16Yan.tdb): BCC_A2, type code %B, sha256 `334018575c889441…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NB% TI% : VA : !
~~~~

[NbTi-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-18Hu.tdb): BCC_A2, type code %B, sha256 `b7a98bf27255bfc2…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NB% TI% : VA : !
~~~~

[NbTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-94Har.tdb): BCC_A2, type code %B, sha256 `09901ed78b749997…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NB% TI% : VA : !
~~~~

[NbTi-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-98Sau.tdb): BCC_A2, type code %B, sha256 `7e8f7395e69fa0a0…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NB% TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(94)90008-6](https://doi.org/10.1016/0364-5916%2894%2990008-6) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00051-7](https://doi.org/10.1016/S0364-5916%2801%2900051-7) Y. Zhang, H. Liu, Z. Jin, Calphad, 25, 305-17(2001).  
_assessment that models this phase_

## OMEGA_C32 (Nb–Ti)

- Id: `phase:nb-ti:c32-omega`; status `assigned`
- Structure: AlB2 · C32 · hP3 · P6/mmm (191); type `st:c32-alb2-hp3`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ti:c32-omega)

Names (4): _corpus: _corpus:phase:nb-ti:c32-omega  
_tdb: _tdb:NbTi-01Zha-LB.tdb:OMEGA_C32, tdb:NbTi-16Yan.tdb:OMEGA_C32, tdb:NbTi-18Hu.tdb:OMEGA_C32  


### TDB models of OMEGA_C32 (3): PHASE and CONSTITUENT statements as written

[NbTi-01Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-01Zha-LB.tdb): OMEGA_C32, type code %, sha256 `cc166cb688a0d62e…`

~~~~text
42: PHASE OMEGA_C32 % 1 1 !
43: CONST OMEGA_C32 : NB TI% : !
~~~~

[NbTi-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-16Yan.tdb): OMEGA_C32, type code %, sha256 `334018575c889441…`

~~~~text
41: PHASE OMEGA_C32 % 1 1 !
42: CONST OMEGA_C32 : NB TI : !
~~~~

[NbTi-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-18Hu.tdb): OMEGA_C32, type code %, sha256 `b7a98bf27255bfc2…`

~~~~text
41: PHASE OMEGA_C32 % 1 1 !
42: CONST OMEGA_C32 : NB TI% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00051-7](https://doi.org/10.1016/S0364-5916%2801%2900051-7) Y. Zhang, H. Liu, Z. Jin, Calphad, 25, 305-17(2001).  
_assessment that models this phase_

## FCC_A1 (Nb–Ti)

- Id: `phase:nb-ti:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 5 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ti:fcc-a1)

Names (6): _corpus: _corpus:phase:nb-ti:fcc-a1  
_tdb: _tdb:NbTi-01Zha-LB.tdb:FCC_A1, tdb:NbTi-16Yan.tdb:FCC_A1, tdb:NbTi-18Hu.tdb:FCC_A1, tdb:NbTi-94Har.tdb:FCC_A1, tdb:NbTi-98Sau.tdb:FCC_A1  


### TDB models of FCC_A1 (5): PHASE and CONSTITUENT statements as written

[NbTi-01Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-01Zha-LB.tdb): FCC_A1, type code %A, sha256 `cc166cb688a0d62e…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB TI : VA : !
~~~~

[NbTi-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-16Yan.tdb): FCC_A1, type code %A, sha256 `334018575c889441…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NB TI : VA : !
~~~~

[NbTi-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-18Hu.tdb): FCC_A1, type code %A, sha256 `b7a98bf27255bfc2…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NB TI : VA : !
~~~~

[NbTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-94Har.tdb): FCC_A1, type code %A, sha256 `09901ed78b749997…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NB TI : VA : !
~~~~

[NbTi-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-98Sau.tdb): FCC_A1, type code %A, sha256 `7e8f7395e69fa0a0…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NB TI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(94)90008-6](https://doi.org/10.1016/0364-5916%2894%2990008-6) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00051-7](https://doi.org/10.1016/S0364-5916%2801%2900051-7) Y. Zhang, H. Liu, Z. Jin, Calphad, 25, 305-17(2001).  
_assessment that models this phase_

## HCP_A3 (Nb–Ti)

- Id: `phase:nb-ti:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 300–2746.9 K, x(Ti) 0.96931–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ti:hcp-a3)

Names (6): _corpus: _corpus:phase:nb-ti:hcp-a3  
_tdb: _tdb:NbTi-01Zha-LB.tdb:HCP_A3, tdb:NbTi-16Yan.tdb:HCP_A3, tdb:NbTi-18Hu.tdb:HCP_A3, tdb:NbTi-94Har.tdb:HCP_A3, tdb:NbTi-98Sau.tdb:HCP_A3  


### TDB models of HCP_A3 (5): PHASE and CONSTITUENT statements as written

[NbTi-01Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-01Zha-LB.tdb): HCP_A3, type code %A, sha256 `cc166cb688a0d62e…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB TI% : VA : !
~~~~

[NbTi-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-16Yan.tdb): HCP_A3, type code %A, sha256 `334018575c889441…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NB TI% : VA : !
~~~~

[NbTi-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-18Hu.tdb): HCP_A3, type code %A, sha256 `b7a98bf27255bfc2…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NB TI% : VA : !
~~~~

[NbTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-94Har.tdb): HCP_A3, type code %A, sha256 `09901ed78b749997…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NB TI% : VA : !
~~~~

[NbTi-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-98Sau.tdb): HCP_A3, type code %A, sha256 `7e8f7395e69fa0a0…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NB TI% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(94)90008-6](https://doi.org/10.1016/0364-5916%2894%2990008-6) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00051-7](https://doi.org/10.1016/S0364-5916%2801%2900051-7) Y. Zhang, H. Liu, Z. Jin, Calphad, 25, 305-17(2001).  
_assessment that models this phase_

## LIQUID (Nb–Ti)

- Id: `phase:nb-ti:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 5 of 5 calculated diagram(s): 1155–4000 K, x(Ti) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ti:liquid)

Names (6): _corpus: _corpus:phase:nb-ti:liquid  
_tdb: _tdb:NbTi-01Zha-LB.tdb:LIQUID, tdb:NbTi-16Yan.tdb:LIQUID, tdb:NbTi-18Hu.tdb:LIQUID, tdb:NbTi-94Har.tdb:LIQUID, tdb:NbTi-98Sau.tdb:LIQUID  


### TDB models of LIQUID (5): PHASE and CONSTITUENT statements as written

[NbTi-01Zha-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-01Zha-LB.tdb): LIQUID, type code %, sha256 `cc166cb688a0d62e…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB TI : !
~~~~

[NbTi-16Yan.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-16Yan.tdb): LIQUID, type code %, sha256 `334018575c889441…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NB TI : !
~~~~

[NbTi-18Hu.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-18Hu.tdb): LIQUID, type code %, sha256 `b7a98bf27255bfc2…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NB TI : !
~~~~

[NbTi-94Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-94Har.tdb): LIQUID, type code %, sha256 `09901ed78b749997…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NB TI : !
~~~~

[NbTi-98Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTi-98Sau.tdb): LIQUID, type code %, sha256 `7e8f7395e69fa0a0…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NB TI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0364-5916(94)90008-6](https://doi.org/10.1016/0364-5916%2894%2990008-6) K.C. Hari Kumar, P. Wollants, L. Delaey, Calphad, 18, 71-79(1994).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.05.007](https://doi.org/10.1016/j.calphad.2018.05.007) B. Hu, Y. Jiang, J. Wang, B. Yao, F. Min, Y. Du, Calphad, 62, 75-82(2018).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2016.02.251](https://doi.org/10.1016/j.jallcom.2016.02.251) Jia-Yi Yan, G.B. Olson, Computational thermodynamics and kinetics of displacive transformations in titanium-based alloys, Journal of Alloys and Compounds 673, 441-454 (2016).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00051-7](https://doi.org/10.1016/S0364-5916%2801%2900051-7) Y. Zhang, H. Liu, Z. Jin, Calphad, 25, 305-17(2001).  
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
