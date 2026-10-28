# Nd–Zr phases

> Nd–Zr system: 5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ND-ZR.html · Markdown: https://data.orchid-project.org/phases/pages/ND-ZR.md

5 phases (tier A 4, liquid 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ND-ZR) · [full JSON](https://data.orchid-project.org/phases/systems/ND-ZR.json) · [Nd–Zr system page](https://data.orchid-project.org/systems/ND-ZR.html) · [Markdown](https://data.orchid-project.org/phases/pages/ND-ZR.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Nd–Zr system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-nd-zr-bcc-a2); _phase:nd-zr:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 944–3999.1 K, x(Zr) 0–1 | 4 | 2 |
| [DHCP](#phase-nd-zr-dhcp-a3); _phase:nd-zr:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1267.2 K, x(Zr) 0–0.05141 | 2 | 2 |
| [FCC_A1](#phase-nd-zr-fcc-a1); _phase:nd-zr:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 820–1090 K | 0 | 2 |
| [HCP_A3](#phase-nd-zr-hcp-a3); _phase:nd-zr:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1283.99 K, x(Zr) 0.96568–1 | 2 | 2 |
| [LIQUID](#phase-nd-zr-liquid); _phase:nd-zr:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1258.1–4000 K, x(Zr) 0–1 | 14 | 2 |

## BCC_A2 (Nd–Zr)

- Id: `phase:nd-zr:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 944–3999.1 K, x(Zr) 0–1
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-zr:bcc-a2)

Names (5): _corpus: _corpus:phase:nd-zr:bcc-a2  
_paper: _paper:10.1016/j.calphad.2014.02.008:bcc-Nd, paper:10.1016/j.calphad.2014.02.008:bcc-Zr  
_tdb: _tdb:NdZr-14Che.tdb:BCC_A2, tdb:NdZr-14Mat.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[NdZr-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Che.tdb): BCC_A2, type code %B, sha256 `5b20a92a0ab14f26…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : ND ZR : VA : !
~~~~

[NdZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Mat.tdb): BCC_A2, type code %B, sha256 `3f1e2816e533b3fb…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : ND ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Zr system, Calphad 46, 103-107 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1) Kaiming Cheng, Hua Zhou, Biao Hu, Yong Du, Lijun Zhang, Shuhong Liu et al., Experimental Investigation and Thermodynamic Modeling of the Nd-Zr and the Mg-Nd-Zr Systems, Metall Mater Trans A 45, 2708-2718 (2014).  
_assessment that models this phase_

## DHCP (Nd–Zr)

- Id: `phase:nd-zr:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1267.2 K, x(Zr) 0–0.05141
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-zr:dhcp-a3)

Names (5): _corpus: _corpus:phase:nd-zr:dhcp-a3, corpus:phase:nd-zr:dhcp  
_paper: _paper:10.1016/j.calphad.2014.02.008:dhcp-Nd  
_tdb: _tdb:NdZr-14Che.tdb:DHCP, tdb:NdZr-14Mat.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[NdZr-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Che.tdb): DHCP, type code %, sha256 `5b20a92a0ab14f26…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : ND% ZR : !
~~~~

[NdZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Mat.tdb): DHCP, type code %, sha256 `3f1e2816e533b3fb…`

~~~~text
41: PHASE DHCP % 1 1 !
42: CONST DHCP : ND% ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Zr system, Calphad 46, 103-107 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1) Kaiming Cheng, Hua Zhou, Biao Hu, Yong Du, Lijun Zhang, Shuhong Liu et al., Experimental Investigation and Thermodynamic Modeling of the Nd-Zr and the Mg-Nd-Zr Systems, Metall Mater Trans A 45, 2708-2718 (2014).  
_assessment that models this phase_

## FCC_A1 (Nd–Zr)

- Id: `phase:nd-zr:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 820–1090 K
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-zr:fcc-a1)

Names (3): _corpus: _corpus:phase:nd-zr:fcc-a1  
_tdb: _tdb:NdZr-14Che.tdb:FCC_A1, tdb:NdZr-14Mat.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[NdZr-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Che.tdb): FCC_A1, type code %A, sha256 `5b20a92a0ab14f26…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : ND ZR : VA : !
~~~~

[NdZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Mat.tdb): FCC_A1, type code %A, sha256 `3f1e2816e533b3fb…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : ND ZR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1) Kaiming Cheng, Hua Zhou, Biao Hu, Yong Du, Lijun Zhang, Shuhong Liu et al., Experimental Investigation and Thermodynamic Modeling of the Nd-Zr and the Mg-Nd-Zr Systems, Metall Mater Trans A 45, 2708-2718 (2014).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Zr system, Calphad 46, 103-107 (2014).  
_assessment that models this phase_

## HCP_A3 (Nd–Zr)

- Id: `phase:nd-zr:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1283.99 K, x(Zr) 0.96568–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-zr:hcp-a3)

Names (4): _corpus: _corpus:phase:nd-zr:hcp-a3  
_paper: _paper:10.1016/j.calphad.2014.02.008:hcp-Zr  
_tdb: _tdb:NdZr-14Che.tdb:HCP_A3, tdb:NdZr-14Mat.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[NdZr-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Che.tdb): HCP_A3, type code %A, sha256 `5b20a92a0ab14f26…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : ND ZR% : VA : !
~~~~

[NdZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Mat.tdb): HCP_A3, type code %A, sha256 `3f1e2816e533b3fb…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : ND ZR% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Zr system, Calphad 46, 103-107 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1) Kaiming Cheng, Hua Zhou, Biao Hu, Yong Du, Lijun Zhang, Shuhong Liu et al., Experimental Investigation and Thermodynamic Modeling of the Nd-Zr and the Mg-Nd-Zr Systems, Metall Mater Trans A 45, 2708-2718 (2014).  
_assessment that models this phase_

## LIQUID (Nd–Zr)

- Id: `phase:nd-zr:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1258.1–4000 K, x(Zr) 0–1
- Literature: 14 values (14 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:nd-zr:liquid)

Names (5): _corpus: _corpus:phase:nd-zr:liquid  
_paper: _paper:10.1007/s11661-014-2209-1:Liquid, paper:10.1016/j.calphad.2014.02.008:L  
_tdb: _tdb:NdZr-14Che.tdb:LIQUID, tdb:NdZr-14Mat.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[NdZr-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Che.tdb): LIQUID, type code %, sha256 `5b20a92a0ab14f26…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : ND ZR : !
~~~~

[NdZr-14Mat.tdb](https://orchid-project.org/data/databases/sgte-binary/NdZr-14Mat.tdb): LIQUID, type code %, sha256 `3f1e2816e533b3fb…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : ND ZR : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11661-014-2209-1](https://doi.org/10.1007/s11661-014-2209-1) Kaiming Cheng, Hua Zhou, Biao Hu, Yong Du, Lijun Zhang, Shuhong Liu et al., Experimental Investigation and Thermodynamic Modeling of the Nd-Zr and the Mg-Nd-Zr Systems, Metall Mater Trans A 45, 2708-2718 (2014).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2014.02.008](https://doi.org/10.1016/j.calphad.2014.02.008) N. Mattern, Y. Yokoyama, A. Mizuno, J.H. Han, O. Fabrichnaya, T. Harada et al., Experimental and thermodynamic assessment of the Nd–Zr system, Calphad 46, 103-107 (2014).  
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
