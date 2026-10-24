# Cr–N phases

> Cr–N system: 5 phases (tier A 2, liquid 1, gas 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-N.html · Markdown: https://data.orchid-project.org/phases/pages/CR-N.md

5 phases (tier A 2, liquid 1, gas 1, interstitial_fcc_a1_compound 1); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-N) · [full JSON](https://data.orchid-project.org/phases/systems/CR-N.json) · [Cr–N system page](https://data.orchid-project.org/systems/CR-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–N system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-n-bcc-a2); _phase:cr-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2464.98 K, x(N) 0–0.04835 | 0 | 1 |
| [FCC_A1](#phase-cr-n-fcc-a1); _phase:cr-n:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 1 calculated diagram(s): 300–1318.13 K, x(N) 0.49571–0.5 | 3 | 1 |
| [HCP_A3](#phase-cr-n-hcp-a3); _phase:cr-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1956.58 K, x(N) 0.22559–0.33333 | 0 | 1 |
| [LIQUID](#phase-cr-n-liquid); _phase:cr-n:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1920.54–4000 K, x(N) 0–0.1814 | 0 | 1 |
| [N2GAS](#phase-cr-n-n2gas); _phase:cr-n:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–4000 K, x(N) 1–1 | 0 | 1 |

## BCC_A2 (Cr–N)

- Id: `phase:cr-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2464.98 K, x(N) 0–0.04835
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-n:bcc-a2)

Names (2): _corpus: _corpus:phase:cr-n:bcc-a2  
_tdb: _tdb:CrN-91Fri-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CrN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrN-91Fri-LB.tdb): BCC_A2, type code %B, sha256 `ca92d72cc42438d4…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : CR : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_

## FCC_A1 (Cr–N)

- Id: `phase:cr-n:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1318.13 K, x(N) 0.49571–0.5
- Literature: 3 values (3 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-n:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-n:fcc-a1  
_paper: _paper:10.1016/0364-5916(91)90028-i:CrN  
_tdb: _tdb:CrN-91Fri-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CrN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrN-91Fri-LB.tdb): FCC_A1, type code %A, sha256 `ca92d72cc42438d4…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : CR : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase; reports values for this phase_

## HCP_A3 (Cr–N)

- Id: `phase:cr-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1956.58 K, x(N) 0.22559–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-n:hcp-a3)

Names (2): _corpus: _corpus:phase:cr-n:hcp-a3  
_tdb: _tdb:CrN-91Fri-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CrN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrN-91Fri-LB.tdb): HCP_A3, type code %, sha256 `ca92d72cc42438d4…`

~~~~text
41: PHASE HCP_A3 % 2 1 0.5 !
42: CONST HCP_A3 : CR : N VA% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_

## LIQUID (Cr–N)

- Id: `phase:cr-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1920.54–4000 K, x(N) 0–0.1814
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-n:liquid)

Names (2): _corpus: _corpus:phase:cr-n:liquid  
_tdb: _tdb:CrN-91Fri-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CrN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrN-91Fri-LB.tdb): LIQUID, type code %, sha256 `ca92d72cc42438d4…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : CR N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
_assessment that models this phase_

## N2GAS (Cr–N)

- Id: `phase:cr-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–4000 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-n:n2gas)

Names (2): _corpus: _corpus:phase:cr-n:n2gas  
_tdb: _tdb:CrN-91Fri-LB.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[CrN-91Fri-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrN-91Fri-LB.tdb): N2GAS, type code %, sha256 `ca92d72cc42438d4…`

~~~~text
44: PHASE N2GAS % 1 1 !
45: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/0364-5916(91)90028-I](https://doi.org/10.1016/0364-5916%2891%2990028-I) K. Frisk, Calphad, 15, 79-106(1991).  
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
