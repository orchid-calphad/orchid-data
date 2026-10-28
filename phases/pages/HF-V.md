# Hf–V phases

> Hf–V system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-V.html · Markdown: https://data.orchid-project.org/phases/pages/HF-V.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-V) · [full JSON](https://data.orchid-project.org/phases/systems/HF-V.json) · [Hf–V system page](https://data.orchid-project.org/systems/HF-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–V system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-v-bcc-a2); _phase:hf-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3999.24 K, x(V) 0–1 | 20 | 1 |
| [C15_LAVES](#phase-hf-v-c15-laves); _phase:hf-v:c15-laves_ | Cu2Mg · C15 · cF24 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1807.52 K, x(V) 0.64035–0.67472 | 26 | 1 |
| [FCC_A1](#phase-hf-v-fcc-a1); _phase:hf-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-hf-v-hcp-a3); _phase:hf-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2191.02 K, x(V) 0–0.02651 | 7 | 1 |
| [LIQUID](#phase-hf-v-liquid); _phase:hf-v:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1733.12–4000 K, x(V) 0–1 | 23 | 1 |

## BCC_A2 (Hf–V)

- Id: `phase:hf-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3999.24 K, x(V) 0–1
- Literature: 20 values (12 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-v:bcc-a2)

Names (3): _corpus: _corpus:phase:hf-v:bcc-a2  
_paper: _paper:10.1361/15477030522464:bcc_A2  
_tdb: _tdb:HfV-05Ser.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HfV-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/HfV-05Ser.tdb): BCC_A2, type code %B, sha256 `5eb8c7c45b64d39e…`

~~~~text
34: PHASE BCC_A2 %B 2 1 3 !
35: CONST BCC_A2 : HF% V% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(68)90003-9](https://doi.org/10.1016/0022-5088%2868%2990003-9) E. Rudy, St. Windisch, The phase diagrams hafnium-vanadium and hafnium-chromium, Journal of the Less Common Metals 15, 13-27 (1968).  
_cited as the source of values for this phase_

## C15_LAVES (Hf–V)

- Id: `phase:hf-v:c15-laves`; status `assigned`
- Structure: Cu2Mg · C15 · cF24 · Fd-3m (227); type `st:c15-cu2mg-cf24`; tier A: standard phase name; confidence high
- Caveat: partitioned order/disorder model in HfV-05Ser.tdb also describes the disordered state
- Stability: stable in 1 of 1 calculated diagram(s): 300–1807.52 K, x(V) 0.64035–0.67472
- Literature: 26 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-v:c15-laves)

Names (4): _corpus: _corpus:phase:hf-v:c15-laves  
_paper: _paper:10.1361/15477030522464:C15 Laves, paper:10.1361/15477030522464:C15-Laves  
_tdb: _tdb:HfV-05Ser.tdb:C15_LAVES  


### TDB models of C15_LAVES (1): PHASE and CONSTITUENT statements as written

[HfV-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/HfV-05Ser.tdb): C15_LAVES, type code %, sha256 `5eb8c7c45b64d39e…`

~~~~text
44: PHASE C15_LAVES % 2 2 1 !
45: CONST C15_LAVES : HF V% : HF% V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(68)90003-9](https://doi.org/10.1016/0022-5088%2868%2990003-9) E. Rudy, St. Windisch, The phase diagrams hafnium-vanadium and hafnium-chromium, Journal of the Less Common Metals 15, 13-27 (1968).  
_cited as the source of values for this phase_

## FCC_A1 (Hf–V)

- Id: `phase:hf-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-v:fcc-a1)

Names (2): _corpus: _corpus:phase:hf-v:fcc-a1  
_tdb: _tdb:HfV-05Ser.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HfV-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/HfV-05Ser.tdb): FCC_A1, type code %A, sha256 `5eb8c7c45b64d39e…`

~~~~text
29: PHASE FCC_A1 %A 2 1 1 !
30: CONST FCC_A1 : HF V : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase_

## HCP_A3 (Hf–V)

- Id: `phase:hf-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2191.02 K, x(V) 0–0.02651
- Literature: 7 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-v:hcp-a3)

Names (3): _corpus: _corpus:phase:hf-v:hcp-a3  
_paper: _paper:10.1361/15477030522464:cph_A3  
_tdb: _tdb:HfV-05Ser.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HfV-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/HfV-05Ser.tdb): HCP_A3, type code %A, sha256 `5eb8c7c45b64d39e…`

~~~~text
39: PHASE HCP_A3 %A 2 1 0.5 !
40: CONST HCP_A3 : HF% V : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(68)90003-9](https://doi.org/10.1016/0022-5088%2868%2990003-9) E. Rudy, St. Windisch, The phase diagrams hafnium-vanadium and hafnium-chromium, Journal of the Less Common Metals 15, 13-27 (1968).  
_cited as the source of values for this phase_

## LIQUID (Hf–V)

- Id: `phase:hf-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1733.12–4000 K, x(V) 0–1
- Literature: 23 values (16 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-v:liquid)

Names (5): _corpus: _corpus:phase:hf-v:liquid  
_paper: _paper:10.1361/15477030522464:L, paper:10.1361/15477030522464:Liq, paper:10.1361/15477030522464:liquid  
_tdb: _tdb:HfV-05Ser.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HfV-05Ser.tdb](https://orchid-project.org/data/databases/sgte-binary/HfV-05Ser.tdb): LIQUID, type code %, sha256 `5eb8c7c45b64d39e…`

~~~~text
24: PHASE LIQUID:L % 1 1 !
25: CONST LIQUID:L : HF V : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1361/15477030522464](https://doi.org/10.1361/15477030522464) C. Servant, Thermodynamic Assessments of the Phase Diagrams of the Hafnium-Vanadium and Vanadium-Zirconium Systems, Journal of Phase Equilibria &amp; Diffusion 26, 39-49 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0022-5088(68)90003-9](https://doi.org/10.1016/0022-5088%2868%2990003-9) E. Rudy, St. Windisch, The phase diagrams hafnium-vanadium and hafnium-chromium, Journal of the Less Common Metals 15, 13-27 (1968).  
_cited as the source of values for this phase_

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
