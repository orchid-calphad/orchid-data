# Nb–Ta phases

> Nb–Ta system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NB-TA.html · Markdown: https://data.orchid-project.org/phases/pages/NB-TA.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NB-TA) · [full JSON](https://data.orchid-project.org/phases/systems/NB-TA.json) · [Nb–Ta system page](https://data.orchid-project.org/systems/NB-TA.html) · [Markdown](https://data.orchid-project.org/phases/pages/NB-TA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nb–Ta system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nb-ta-bcc-a2); _phase:nb-ta:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–4000 K, x(Ta) 0–1 | 0 | 4 |
| [B2_BCC](#phase-nb-ta-bcc-b2); _phase:nb-ta:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 2780–2910 K | 0 | 1 |
| [FCC_A1](#phase-nb-ta-fcc-a1); _phase:nb-ta:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-nb-ta-hcp-a3); _phase:nb-ta:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-nb-ta-liquid); _phase:nb-ta:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 2733.4–4000 K, x(Ta) 0–1 | 0 | 3 |

## BCC_A2 (Nb–Ta)

- Id: `phase:nb-ta:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–4000 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ta:bcc-a2)

Names (5): _corpus: _corpus:phase:nb-ta:bcc-a2  
_tdb: _tdb:NbTa-02Har.tdb:BCC_A2, tdb:NbTa-04Xio-LB.tdb:BCC_A2, tdb:NbTa-22Zha.tdb:A2_BCC, tdb:NbTa-22Zha.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NbTa-02Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-02Har.tdb): BCC_A2, type code %B, sha256 `ca67283e79b7fafa…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NB% TA% : VA : !
~~~~

[NbTa-04Xio-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-04Xio-LB.tdb): BCC_A2, type code %B, sha256 `849d2204e0561aeb…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NB% TA% : VA : !
~~~~

[NbTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-22Zha.tdb): A2_BCC, type code %B, sha256 `5229418c54024a1d…`

~~~~text
42: PHASE A2_BCC %B 2 1 3 !
43: CONST A2_BCC : NB TA : VA : !
~~~~

[NbTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-22Zha.tdb): BCC_A2, type code %B, sha256 `5229418c54024a1d…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : NB% TA% : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Li, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2002-0196](https://doi.org/10.1515/ijmr-2002-0196) K.C. Hari Kumar, T. Van Rompaey, P. Wollants, Z. Metallkd., 93, 1146-53(2002).  
_assessment that models this phase_

## B2_BCC (Nb–Ta)

- Id: `phase:nb-ta:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: NbTa-22Zha.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in NbTa-22Zha.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 2780–2910 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ta:bcc-b2)

Names (2): _corpus: _corpus:phase:nb-ta:bcc-b2  
_tdb: _tdb:NbTa-22Zha.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[NbTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-22Zha.tdb): B2_BCC, type code %BO, sha256 `5229418c54024a1d…`

~~~~text
47: PHASE B2_BCC %BO 3 0.5 0.5 3 !
48: CONST B2_BCC : NB TA : NB TA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_

## FCC_A1 (Nb–Ta)

- Id: `phase:nb-ta:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ta:fcc-a1)

Names (4): _corpus: _corpus:phase:nb-ta:fcc-a1  
_tdb: _tdb:NbTa-02Har.tdb:FCC_A1, tdb:NbTa-04Xio-LB.tdb:FCC_A1, tdb:NbTa-22Zha.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[NbTa-02Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-02Har.tdb): FCC_A1, type code %A, sha256 `ca67283e79b7fafa…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NB TA : VA : !
~~~~

[NbTa-04Xio-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-04Xio-LB.tdb): FCC_A1, type code %A, sha256 `849d2204e0561aeb…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NB TA : VA : !
~~~~

[NbTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-22Zha.tdb): FCC_A1, type code %A, sha256 `5229418c54024a1d…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : NB TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Li, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2002-0196](https://doi.org/10.1515/ijmr-2002-0196) K.C. Hari Kumar, T. Van Rompaey, P. Wollants, Z. Metallkd., 93, 1146-53(2002).  
_assessment that models this phase_

## HCP_A3 (Nb–Ta)

- Id: `phase:nb-ta:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ta:hcp-a3)

Names (4): _corpus: _corpus:phase:nb-ta:hcp-a3  
_tdb: _tdb:NbTa-02Har.tdb:HCP_A3, tdb:NbTa-04Xio-LB.tdb:HCP_A3, tdb:NbTa-22Zha.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[NbTa-02Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-02Har.tdb): HCP_A3, type code %A, sha256 `ca67283e79b7fafa…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NB TA : VA : !
~~~~

[NbTa-04Xio-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-04Xio-LB.tdb): HCP_A3, type code %A, sha256 `849d2204e0561aeb…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NB TA : VA : !
~~~~

[NbTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-22Zha.tdb): HCP_A3, type code %A, sha256 `5229418c54024a1d…`

~~~~text
52: PHASE HCP_A3 %A 2 1 0.5 !
53: CONST HCP_A3 : NB TA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Li, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2002-0196](https://doi.org/10.1515/ijmr-2002-0196) K.C. Hari Kumar, T. Van Rompaey, P. Wollants, Z. Metallkd., 93, 1146-53(2002).  
_assessment that models this phase_

## LIQUID (Nb–Ta)

- Id: `phase:nb-ta:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 2733.4–4000 K, x(Ta) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nb-ta:liquid)

Names (4): _corpus: _corpus:phase:nb-ta:liquid  
_tdb: _tdb:NbTa-02Har.tdb:LIQUID, tdb:NbTa-04Xio-LB.tdb:LIQUID, tdb:NbTa-22Zha.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[NbTa-02Har.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-02Har.tdb): LIQUID, type code %, sha256 `ca67283e79b7fafa…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NB TA : !
~~~~

[NbTa-04Xio-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-04Xio-LB.tdb): LIQUID, type code %, sha256 `849d2204e0561aeb…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NB TA : !
~~~~

[NbTa-22Zha.tdb](https://orchid-project.org/data/databases/sgte-binary/NbTa-22Zha.tdb): LIQUID, type code %, sha256 `5229418c54024a1d…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : NB TA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2004.07.002](https://doi.org/10.1016/j.calphad.2004.07.002) W. Xiong, Y. Du, Y. Li, B.Y. Huang, H.H. Xu, H.L. Chen, Z. Pan, Calphad, 28, 133-40(2004).  
_assessment that models this phase_
- [doi:10.1016/j.ijrmhm.2022.105780](https://doi.org/10.1016/j.ijrmhm.2022.105780) Enkuan Zhang, Ying Tang, Mingwen Wen, Abdulmonem Obaied, Irina Roslyakova, Lijun Zhang, On phase stability of Mo-Nb-Ta-W refractory high entropy alloys, International Journal of Refractory Metals and Hard Materials 103, 105780 (2022).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2002-0196](https://doi.org/10.1515/ijmr-2002-0196) K.C. Hari Kumar, T. Van Rompaey, P. Wollants, Z. Metallkd., 93, 1146-53(2002).  
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
