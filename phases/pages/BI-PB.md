# Bi–Pb phases

> Bi–Pb system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/BI-PB.html · Markdown: https://data.orchid-project.org/phases/pages/BI-PB.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=BI-PB) · [full JSON](https://data.orchid-project.org/phases/systems/BI-PB.json) · [Bi–Pb system page](https://data.orchid-project.org/systems/BI-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/BI-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Bi–Pb system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [RHOMBOHEDRAL_A7](#phase-bi-pb-a7-rhombohedral); _phase:bi-pb:a7-rhombohedral_ | alpha-As · A7 · hR2 · R-3m (166) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–544.55 K, x(Pb) 0–0.0048 | 0 | 4 |
| [BCC_A2](#phase-bi-pb-bcc-a2); _phase:bi-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-bi-pb-fcc-a1); _phase:bi-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.36 K, x(Pb) 0.76884–1 | 0 | 4 |
| [HCP_A3](#phase-bi-pb-hcp-a3); _phase:bi-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–459.3 K, x(Pb) 0.57133–0.75363 | 0 | 4 |
| [LIQUID](#phase-bi-pb-liquid); _phase:bi-pb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 398.14–2500 K, x(Pb) 0–1 | 0 | 4 |

## RHOMBOHEDRAL_A7 (Bi–Pb)

- Id: `phase:bi-pb:a7-rhombohedral`; status `assigned`
- Structure: alpha-As · A7 · hR2 · R-3m (166); type `st:a7-alpha-as-hr2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–544.55 K, x(Pb) 0–0.0048
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-pb:a7-rhombohedral)

Names (5): _corpus: _corpus:phase:bi-pb:a7-rhombohedral  
_tdb: _tdb:BiPb-17Gie.tdb:RHOMBOHEDRAL_A7, tdb:BiPb-21Aga.tdb:RHOMBOHEDRAL_A7, tdb:BiPb-98Boa-LB.tdb:RHOMBOHEDRAL_A7, tdb:BiPb-98Yoo.tdb:RHOMBOHEDRAL_A7  


### TDB models of RHOMBOHEDRAL_A7 (4): PHASE and CONSTITUENT statements as written

[BiPb-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-17Gie.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `9ba301ea84eb981a…`

~~~~text
42: PHASE RHOMBOHEDRAL_A7 % 1 1 !
43: CONST RHOMBOHEDRAL_A7 : BI% PB : !
~~~~

[BiPb-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-21Aga.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `767bd5aeaed33a7b…`

~~~~text
47: PHASE RHOMBOHEDRAL_A7 % 1 1 !
48: CONST RHOMBOHEDRAL_A7 : BI% PB : !
~~~~

[BiPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Boa-LB.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `c36b3e9ef4935609…`

~~~~text
44: PHASE RHOMBOHEDRAL_A7 % 1 1 !
45: CONST RHOMBOHEDRAL_A7 : BI% PB : !
~~~~

[BiPb-98Yoo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Yoo.tdb): RHOMBOHEDRAL_A7, type code %, sha256 `a29e66212cd9bf01…`

~~~~text
40: PHASE RHOMBOHEDRAL_A7 % 1 1 !
41: CONST RHOMBOHEDRAL_A7 : BI% PB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86(1998).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00022-4](https://doi.org/10.1016/S0364-5916%2898%2900022-4) S.W. Yoon, H.M. Lee, Calphad, 22, 167-78(1998).  
_assessment that models this phase_

## BCC_A2 (Bi–Pb)

- Id: `phase:bi-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-pb:bcc-a2)

Names (5): _corpus: _corpus:phase:bi-pb:bcc-a2  
_tdb: _tdb:BiPb-17Gie.tdb:BCC_A2, tdb:BiPb-21Aga.tdb:BCC_A2, tdb:BiPb-98Boa-LB.tdb:BCC_A2, tdb:BiPb-98Yoo.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[BiPb-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-17Gie.tdb): BCC_A2, type code %B, sha256 `9ba301ea84eb981a…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : BI PB : VA : !
~~~~

[BiPb-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-21Aga.tdb): BCC_A2, type code %B, sha256 `767bd5aeaed33a7b…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : BI PB : VA : !
~~~~

[BiPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Boa-LB.tdb): BCC_A2, type code %B, sha256 `c36b3e9ef4935609…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : BI PB : VA : !
~~~~

[BiPb-98Yoo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Yoo.tdb): BCC_A2, type code %B, sha256 `a29e66212cd9bf01…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : BI PB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86(1998).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00022-4](https://doi.org/10.1016/S0364-5916%2898%2900022-4) S.W. Yoon, H.M. Lee, Calphad, 22, 167-78(1998).  
_assessment that models this phase_

## FCC_A1 (Bi–Pb)

- Id: `phase:bi-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.36 K, x(Pb) 0.76884–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-pb:fcc-a1)

Names (5): _corpus: _corpus:phase:bi-pb:fcc-a1  
_tdb: _tdb:BiPb-17Gie.tdb:FCC_A1, tdb:BiPb-21Aga.tdb:FCC_A1, tdb:BiPb-98Boa-LB.tdb:FCC_A1, tdb:BiPb-98Yoo.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[BiPb-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-17Gie.tdb): FCC_A1, type code %A, sha256 `9ba301ea84eb981a…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : BI PB : VA : !
~~~~

[BiPb-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-21Aga.tdb): FCC_A1, type code %A, sha256 `767bd5aeaed33a7b…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : BI PB : VA : !
~~~~

[BiPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Boa-LB.tdb): FCC_A1, type code %A, sha256 `c36b3e9ef4935609…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : BI PB : VA : !
~~~~

[BiPb-98Yoo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Yoo.tdb): FCC_A1, type code %A, sha256 `a29e66212cd9bf01…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : BI PB : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86(1998).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00022-4](https://doi.org/10.1016/S0364-5916%2898%2900022-4) S.W. Yoon, H.M. Lee, Calphad, 22, 167-78(1998).  
_assessment that models this phase_

## HCP_A3 (Bi–Pb)

- Id: `phase:bi-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–459.3 K, x(Pb) 0.57133–0.75363
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-pb:hcp-a3)

Names (5): _corpus: _corpus:phase:bi-pb:hcp-a3  
_tdb: _tdb:BiPb-17Gie.tdb:HCP_A3, tdb:BiPb-21Aga.tdb:HCP_A3, tdb:BiPb-98Boa-LB.tdb:HCP_A3, tdb:BiPb-98Yoo.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[BiPb-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-17Gie.tdb): HCP_A3, type code %A, sha256 `9ba301ea84eb981a…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : BI PB : VA: !
~~~~

[BiPb-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-21Aga.tdb): HCP_A3, type code %A, sha256 `767bd5aeaed33a7b…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : BI PB : VA: !
~~~~

[BiPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Boa-LB.tdb): HCP_A3, type code %A, sha256 `c36b3e9ef4935609…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : BI PB : VA: !
~~~~

[BiPb-98Yoo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Yoo.tdb): HCP_A3, type code %A, sha256 `a29e66212cd9bf01…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : BI PB : VA: !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86(1998).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00022-4](https://doi.org/10.1016/S0364-5916%2898%2900022-4) S.W. Yoon, H.M. Lee, Calphad, 22, 167-78(1998).  
_assessment that models this phase_

## LIQUID (Bi–Pb)

- Id: `phase:bi-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 398.14–2500 K, x(Pb) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:bi-pb:liquid)

Names (5): _corpus: _corpus:phase:bi-pb:liquid  
_tdb: _tdb:BiPb-17Gie.tdb:LIQUID, tdb:BiPb-21Aga.tdb:LIQUID, tdb:BiPb-98Boa-LB.tdb:LIQUID, tdb:BiPb-98Yoo.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[BiPb-17Gie.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-17Gie.tdb): LIQUID, type code %, sha256 `9ba301ea84eb981a…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : BI PB : !
~~~~

[BiPb-21Aga.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-21Aga.tdb): LIQUID, type code %, sha256 `767bd5aeaed33a7b…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : BI PB : !
~~~~

[BiPb-98Boa-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Boa-LB.tdb): LIQUID, type code %, sha256 `c36b3e9ef4935609…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : BI PB : !
~~~~

[BiPb-98Yoo.tdb](https://orchid-project.org/data/databases/sgte-binary/BiPb-98Yoo.tdb): LIQUID, type code %, sha256 `a29e66212cd9bf01…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : BI PB : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/s11669-017-0572-5](https://doi.org/10.1007/s11669-017-0572-5) Wojciech Gierlotka, Yi-Cheng Tung, A New Thermodynamic Description of the Bi-Pb-Sn System, J. Phase Equilib. Diffus. 38, 814-828 (2017).  
_assessment that models this phase_
- [doi:10.1016/j.tca.2021.178913](https://doi.org/10.1016/j.tca.2021.178913) Renu Agarwal, Understanding uranium interactions with bismuth and lead-bismuth eutectic: Using calorimetric measurements, Thermochimica Acta 699, 178913 (2021).  
_assessment that models this phase_
- [doi:10.1016/S0040-6031(98)00237-8](https://doi.org/10.1016/S0040-6031%2898%2900237-8) D. Boa, I. Ansara, Thermochim. Acta, 314, 79-86(1998).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(98)00022-4](https://doi.org/10.1016/S0364-5916%2898%2900022-4) S.W. Yoon, H.M. Lee, Calphad, 22, 167-78(1998).  
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
