# Cr–Sn phases

> Cr–Sn system: 6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-SN.html · Markdown: https://data.orchid-project.org/phases/pages/CR-SN.md

6 phases (tier A 5, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-SN) · [full JSON](https://data.orchid-project.org/phases/systems/CR-SN.json) · [Cr–Sn system page](https://data.orchid-project.org/systems/CR-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–Sn system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-cr-sn-a4-diamond); _phase:cr-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [BCT_A5](#phase-cr-sn-a5-bct); _phase:cr-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 1–1 | 0 | 3 |
| [BCC_A2](#phase-cr-sn-bcc-a2); _phase:cr-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2244.98 K, x(Sn) 0–0.03738 | 0 | 3 |
| [FCC_A1](#phase-cr-sn-fcc-a1); _phase:cr-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [HCP_A3](#phase-cr-sn-hcp-a3); _phase:cr-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [LIQUID](#phase-cr-sn-liquid); _phase:cr-sn:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1 | 0 | 3 |

## DIAMOND_A4 (Cr–Sn)

- Id: `phase:cr-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-sn:a4-diamond)

Names (4): _corpus: _corpus:phase:cr-sn:a4-diamond  
_tdb: _tdb:CrSn-01Jer-LB.tdb:DIAMOND_A4, tdb:CrSn-17Laf.tdb:DIAMOND_A4, tdb:CrSn-19Laf.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (3): PHASE and CONSTITUENT statements as written

[CrSn-01Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-01Jer-LB.tdb): DIAMOND_A4, type code %, sha256 `6f7f02f10b4fae0a…`

~~~~text
41: PHASE DIAMOND_A4 % 1 1 !
42: CONST DIAMOND_A4 : SN : !
~~~~

[CrSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-17Laf.tdb): DIAMOND_A4, type code %, sha256 `0faaac76d7589256…`

~~~~text
42: PHASE DIAMOND_A4 % 1 1 !
43: CONST DIAMOND_A4 : SN : !
~~~~

[CrSn-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-19Laf.tdb): DIAMOND_A4, type code %, sha256 `ceeba14a417d8d83…`

~~~~text
46: PHASE DIAMOND_A4 % 1 1 !
47: CONST DIAMOND_A4 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00030-X](https://doi.org/10.1016/S0364-5916%2801%2900030-X) R. Jerlerud Perez, B. Sundman, Calphad, 25, 59-66(2001).  
_assessment that models this phase_

## BCT_A5 (Cr–Sn)

- Id: `phase:cr-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–505.08 K, x(Sn) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-sn:a5-bct)

Names (4): _corpus: _corpus:phase:cr-sn:a5-bct  
_tdb: _tdb:CrSn-01Jer-LB.tdb:BCT_A5, tdb:CrSn-17Laf.tdb:BCT_A5, tdb:CrSn-19Laf.tdb:BCT_A5  


### TDB models of BCT_A5 (3): PHASE and CONSTITUENT statements as written

[CrSn-01Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-01Jer-LB.tdb): BCT_A5, type code %, sha256 `6f7f02f10b4fae0a…`

~~~~text
46: PHASE BCT_A5 % 1 1 !
47: CONST BCT_A5 : SN : !
~~~~

[CrSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-17Laf.tdb): BCT_A5, type code %, sha256 `0faaac76d7589256…`

~~~~text
47: PHASE BCT_A5 % 1 1 !
48: CONST BCT_A5 : SN : !
~~~~

[CrSn-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-19Laf.tdb): BCT_A5, type code %, sha256 `ceeba14a417d8d83…`

~~~~text
51: PHASE BCT_A5 % 1 1 !
52: CONST BCT_A5 : SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00030-X](https://doi.org/10.1016/S0364-5916%2801%2900030-X) R. Jerlerud Perez, B. Sundman, Calphad, 25, 59-66(2001).  
_assessment that models this phase_

## BCC_A2 (Cr–Sn)

- Id: `phase:cr-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2244.98 K, x(Sn) 0–0.03738
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-sn:bcc-a2)

Names (4): _corpus: _corpus:phase:cr-sn:bcc-a2  
_tdb: _tdb:CrSn-01Jer-LB.tdb:BCC_A2, tdb:CrSn-17Laf.tdb:BCC_A2, tdb:CrSn-19Laf.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CrSn-01Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-01Jer-LB.tdb): BCC_A2, type code %B, sha256 `6f7f02f10b4fae0a…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR% SN : VA : !
~~~~

[CrSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-17Laf.tdb): BCC_A2, type code %B, sha256 `0faaac76d7589256…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CR% SN : VA : !
~~~~

[CrSn-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-19Laf.tdb): BCC_A2, type code %B, sha256 `ceeba14a417d8d83…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CR% SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00030-X](https://doi.org/10.1016/S0364-5916%2801%2900030-X) R. Jerlerud Perez, B. Sundman, Calphad, 25, 59-66(2001).  
_assessment that models this phase_

## FCC_A1 (Cr–Sn)

- Id: `phase:cr-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-sn:fcc-a1)

Names (4): _corpus: _corpus:phase:cr-sn:fcc-a1  
_tdb: _tdb:CrSn-01Jer-LB.tdb:FCC_A1, tdb:CrSn-17Laf.tdb:FCC_A1, tdb:CrSn-19Laf.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CrSn-01Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-01Jer-LB.tdb): FCC_A1, type code %A, sha256 `6f7f02f10b4fae0a…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR SN : VA : !
~~~~

[CrSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-17Laf.tdb): FCC_A1, type code %A, sha256 `0faaac76d7589256…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CR SN : VA : !
~~~~

[CrSn-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-19Laf.tdb): FCC_A1, type code %A, sha256 `ceeba14a417d8d83…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CR SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00030-X](https://doi.org/10.1016/S0364-5916%2801%2900030-X) R. Jerlerud Perez, B. Sundman, Calphad, 25, 59-66(2001).  
_assessment that models this phase_

## HCP_A3 (Cr–Sn)

- Id: `phase:cr-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-sn:hcp-a3)

Names (4): _corpus: _corpus:phase:cr-sn:hcp-a3  
_tdb: _tdb:CrSn-01Jer-LB.tdb:HCP_A3, tdb:CrSn-17Laf.tdb:HCP_A3, tdb:CrSn-19Laf.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CrSn-01Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-01Jer-LB.tdb): HCP_A3, type code %A, sha256 `6f7f02f10b4fae0a…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR SN : VA : !
~~~~

[CrSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-17Laf.tdb): HCP_A3, type code %A, sha256 `0faaac76d7589256…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CR SN : VA : !
~~~~

[CrSn-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-19Laf.tdb): HCP_A3, type code %A, sha256 `ceeba14a417d8d83…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : CR SN : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00030-X](https://doi.org/10.1016/S0364-5916%2801%2900030-X) R. Jerlerud Perez, B. Sundman, Calphad, 25, 59-66(2001).  
_assessment that models this phase_

## LIQUID (Cr–Sn)

- Id: `phase:cr-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 505.08–4000 K, x(Sn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-sn:liquid)

Names (4): _corpus: _corpus:phase:cr-sn:liquid  
_tdb: _tdb:CrSn-01Jer-LB.tdb:LIQUID, tdb:CrSn-17Laf.tdb:LIQUID, tdb:CrSn-19Laf.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CrSn-01Jer-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-01Jer-LB.tdb): LIQUID, type code %, sha256 `6f7f02f10b4fae0a…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR SN : !
~~~~

[CrSn-17Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-17Laf.tdb): LIQUID, type code %, sha256 `0faaac76d7589256…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CR SN : !
~~~~

[CrSn-19Laf.tdb](https://orchid-project.org/data/databases/sgte-binary/CrSn-19Laf.tdb): LIQUID, type code %, sha256 `ceeba14a417d8d83…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CR SN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2017.02.003](https://doi.org/10.1016/j.calphad.2017.02.003) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 57, 37-45(2017).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2018.11.002](https://doi.org/10.1016/j.calphad.2018.11.002) P. Lafaye, C. Toffolon-Masclet, J.-C. Crivello, J.-M. Joubert, Calphad, 64, 43-54(2019).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(01)00030-X](https://doi.org/10.1016/S0364-5916%2801%2900030-X) R. Jerlerud Perez, B. Sundman, Calphad, 25, 59-66(2001).  
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
