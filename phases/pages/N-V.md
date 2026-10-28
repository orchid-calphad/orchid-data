# N–V phases

> N–V system: 5 phases (tier A 2, liquid 1, gas 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/N-V.html · Markdown: https://data.orchid-project.org/phases/pages/N-V.md

5 phases (tier A 2, liquid 1, gas 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=N-V) · [full JSON](https://data.orchid-project.org/phases/systems/N-V.json) · [N–V system page](https://data.orchid-project.org/systems/N-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/N-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the N–V system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-n-v-bcc-a2); _phase:n-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2198.52 K, x(N) 0–0.14936 | 0 | 2 |
| [FCC_A1](#phase-n-v-fcc-a1); _phase:n-v:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 2 of 2 calculated diagram(s): 300–2393.43 K, x(N) 0.37866–0.5 | 0 | 2 |
| [HCP_A3](#phase-n-v-hcp-a3); _phase:n-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–2682.63 K, x(N) 0.24214–0.33333 | 0 | 2 |
| [LIQUID](#phase-n-v-liquid); _phase:n-v:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 2110–4000 K, x(N) 0–0.23338 | 0 | 2 |
| [N2GAS](#phase-n-v-n2gas); _phase:n-v:n2gas_ | gas | gas | stable in 2 of 2 calculated diagram(s): 300–4000 K, x(N) 1–1 | 0 | 2 |

## BCC_A2 (N–V)

- Id: `phase:n-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2198.52 K, x(N) 0–0.14936
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-v:bcc-a2)

Names (3): _corpus: _corpus:phase:n-v:bcc-a2  
_tdb: _tdb:VN-91Oht-LB.tdb:BCC_A2, tdb:VN-97Du.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[VN-91Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-91Oht-LB.tdb): BCC_A2, type code %B, sha256 `2acab6ca1bd63897…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : V% : N VA% : !
~~~~

[VN-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-97Du.tdb): BCC_A2, type code %B, sha256 `4add1267df6db927…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : V% : N VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90022-C](https://doi.org/10.1016/0364-5916%2891%2990022-C) H. Ohtani, M. Hillert, Calphad, 15, 11-24(1991).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0101](https://doi.org/10.3139/ijmr-1997-0101) Y. Du, R. Schmid-Fetzer, H. Ohtani, Z. Metallkd., 88, 545-56(1997).  
_assessment that models this phase_

## FCC_A1 (N–V)

- Id: `phase:n-v:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2393.43 K, x(N) 0.37866–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-v:fcc-a1)

Names (3): _corpus: _corpus:phase:n-v:fcc-a1  
_tdb: _tdb:VN-91Oht-LB.tdb:FCC_A1, tdb:VN-97Du.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[VN-91Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-91Oht-LB.tdb): FCC_A1, type code %A, sha256 `2acab6ca1bd63897…`

~~~~text
37: PHASE FCC_A1 %A 2 1 1 !
38: CONST FCC_A1 : V : N VA% : !
~~~~

[VN-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-97Du.tdb): FCC_A1, type code %A, sha256 `4add1267df6db927…`

~~~~text
36: PHASE FCC_A1 %A 2 1 1 !
37: CONST FCC_A1 : V : N VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90022-C](https://doi.org/10.1016/0364-5916%2891%2990022-C) H. Ohtani, M. Hillert, Calphad, 15, 11-24(1991).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0101](https://doi.org/10.3139/ijmr-1997-0101) Y. Du, R. Schmid-Fetzer, H. Ohtani, Z. Metallkd., 88, 545-56(1997).  
_assessment that models this phase_

## HCP_A3 (N–V)

- Id: `phase:n-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–2682.63 K, x(N) 0.24214–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-v:hcp-a3)

Names (3): _corpus: _corpus:phase:n-v:hcp-a3  
_tdb: _tdb:VN-91Oht-LB.tdb:HCP_A3, tdb:VN-97Du.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[VN-91Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-91Oht-LB.tdb): HCP_A3, type code %A, sha256 `2acab6ca1bd63897…`

~~~~text
47: PHASE HCP_A3 %A 2 1 0.5 !
48: CONST HCP_A3 : V : N VA% : !
~~~~

[VN-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-97Du.tdb): HCP_A3, type code %A, sha256 `4add1267df6db927…`

~~~~text
46: PHASE HCP_A3 %A 2 1 0.5 !
47: CONST HCP_A3 : V : N VA% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90022-C](https://doi.org/10.1016/0364-5916%2891%2990022-C) H. Ohtani, M. Hillert, Calphad, 15, 11-24(1991).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0101](https://doi.org/10.3139/ijmr-1997-0101) Y. Du, R. Schmid-Fetzer, H. Ohtani, Z. Metallkd., 88, 545-56(1997).  
_assessment that models this phase_

## LIQUID (N–V)

- Id: `phase:n-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 2110–4000 K, x(N) 0–0.23338
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-v:liquid)

Names (3): _corpus: _corpus:phase:n-v:liquid  
_tdb: _tdb:VN-91Oht-LB.tdb:LIQUID, tdb:VN-97Du.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[VN-91Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-91Oht-LB.tdb): LIQUID, type code %, sha256 `2acab6ca1bd63897…`

~~~~text
32: PHASE LIQUID:L % 1 1 !
33: CONST LIQUID:L : N V : !
~~~~

[VN-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-97Du.tdb): LIQUID, type code %, sha256 `4add1267df6db927…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : N V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90022-C](https://doi.org/10.1016/0364-5916%2891%2990022-C) H. Ohtani, M. Hillert, Calphad, 15, 11-24(1991).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0101](https://doi.org/10.3139/ijmr-1997-0101) Y. Du, R. Schmid-Fetzer, H. Ohtani, Z. Metallkd., 88, 545-56(1997).  
_assessment that models this phase_

## N2GAS (N–V)

- Id: `phase:n-v:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–4000 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:n-v:n2gas)

Names (3): _corpus: _corpus:phase:n-v:n2gas  
_tdb: _tdb:VN-91Oht-LB.tdb:N2GAS, tdb:VN-97Du.tdb:N2GAS  


### TDB models of N2GAS (2): PHASE and CONSTITUENT statements as written

[VN-91Oht-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-91Oht-LB.tdb): N2GAS, type code %, sha256 `2acab6ca1bd63897…`

~~~~text
50: PHASE N2GAS % 1 1 !
51: CONST N2GAS : N2 : !
~~~~

[VN-97Du.tdb](https://orchid-project.org/data/databases/sgte-binary/VN-97Du.tdb): N2GAS, type code %, sha256 `4add1267df6db927…`

~~~~text
49: PHASE N2GAS % 1 1 !
50: CONST N2GAS : N2 : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0364-5916(91)90022-C](https://doi.org/10.1016/0364-5916%2891%2990022-C) H. Ohtani, M. Hillert, Calphad, 15, 11-24(1991).  
_assessment that models this phase_
- [doi:10.3139/ijmr-1997-0101](https://doi.org/10.3139/ijmr-1997-0101) Y. Du, R. Schmid-Fetzer, H. Ohtani, Z. Metallkd., 88, 545-56(1997).  
_assessment that models this phase_

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
