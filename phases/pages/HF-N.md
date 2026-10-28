# Hf–N phases

> Hf–N system: 8 phases (tier A 2, tier C 2, liquid 1, gas 2, interstitial_fcc_a1_compound 1); 8 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/HF-N.html · Markdown: https://data.orchid-project.org/phases/pages/HF-N.md

8 phases (tier A 2, tier C 2, liquid 1, gas 2, interstitial_fcc_a1_compound 1); 8 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=HF-N) · [full JSON](https://data.orchid-project.org/phases/systems/HF-N.json) · [Hf–N system page](https://data.orchid-project.org/systems/HF-N.html) · [Markdown](https://data.orchid-project.org/phases/pages/HF-N.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Hf–N system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-hf-n-bcc-a2); _phase:hf-n:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 2016.03–3999.75 K, x(N) 0–0 | 0 | 1 |
| [FCC_A1](#phase-hf-n-fcc-a1); _phase:hf-n:fcc-a1_ | NaCl · B1 · cF8 · Fm-3m (225) | assigned | stable in 1 of 1 calculated diagram(s): 300–3650.81 K, x(N) 0.37756–0.52058 | 0 | 1 |
| [GAS](#phase-hf-n-gas); _phase:hf-n:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300.72–4000 K, x(N) 0.99285–1 | 0 | 1 |
| [HCP_A3](#phase-hf-n-hcp-a3); _phase:hf-n:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3187.99 K, x(N) 0–0.31441 | 0 | 1 |
| [HF3N2](#phase-hf-n-hf3n2); _phase:hf-n:hf3n2_ | TiS-9R · hR6 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–2245.01 K, x(N) 0.4–0.4 | 0 | 1 |
| [HF4N3](#phase-hf-n-hf4n3); _phase:hf-n:hf4n3_ | Sc2Te3 · hR8 · R-3m (166) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 353.56–2592.71 K, x(N) 0.42857–0.42857 | 0 | 1 |
| [LIQUID](#phase-hf-n-liquid); _phase:hf-n:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 2478.01–4000 K, x(N) 0–0.26474 | 0 | 1 |
| [N2GAS](#phase-hf-n-n2gas); _phase:hf-n:n2gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2185 K, x(N) 1–1 | 0 | 1 |

## BCC_A2 (Hf–N)

- Id: `phase:hf-n:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2016.03–3999.75 K, x(N) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:bcc-a2)

Names (2): _corpus: _corpus:phase:hf-n:bcc-a2  
_tdb: _tdb:HfN-18Pan.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): BCC_A2, type code %B, sha256 `e62247a157b146a1…`

~~~~text
45: PHASE BCC_A2 %B 2 1 3 !
46: CONST BCC_A2 : HF : VA% N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## FCC_A1 (Hf–N)

- Id: `phase:hf-n:fcc-a1`; status `assigned`
- Structure: NaCl · B1 · cF8 · Fm-3m (225); type `st:b1-nacl-cf8`; interstitial_fcc_a1_compound; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3650.81 K, x(N) 0.37756–0.52058
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:fcc-a1)

Names (2): _corpus: _corpus:phase:hf-n:fcc-a1  
_tdb: _tdb:HfN-18Pan.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): FCC_A1, type code %A, sha256 `e62247a157b146a1…`

~~~~text
40: PHASE FCC_A1 %A 2 1 1 !
41: CONST FCC_A1 : HF% VA : VA N% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## GAS (Hf–N)

- Id: `phase:hf-n:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300.72–4000 K, x(N) 0.99285–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:gas)

Names (2): _corpus: _corpus:phase:hf-n:gas  
_tdb: _tdb:HfN-18Pan.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): GAS, type code %, sha256 `e62247a157b146a1…`

~~~~text
66: PHASE GAS:G % 1 1 !
67: CONST GAS:G : N N2 N3 HF : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## HCP_A3 (Hf–N)

- Id: `phase:hf-n:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3187.99 K, x(N) 0–0.31441
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:hcp-a3)

Names (2): _corpus: _corpus:phase:hf-n:hcp-a3  
_tdb: _tdb:HfN-18Pan.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): HCP_A3, type code %A, sha256 `e62247a157b146a1…`

~~~~text
50: PHASE HCP_A3 %A 2 1 0.5 !
51: CONST HCP_A3 : HF : VA% N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## HF3N2 (Hf–N)

- Id: `phase:hf-n:hf3n2`; status `assigned`
- Structure: TiS-9R · hR6 · R-3m (166); type `st:tis-9r-hr6`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_166_matches_3_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hf 0.6000, N 0.4000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2245.01 K, x(N) 0.4–0.4
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:hf3n2)

Names (2): _corpus: _corpus:phase:hf-n:hf3n2  
_tdb: _tdb:HfN-18Pan.tdb:HF3N2  


### TDB models of HF3N2 (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): HF3N2, type code %, sha256 `e62247a157b146a1…`

~~~~text
55: PHASE HF3N2 % 2 3 2 !
56: CONST HF3N2 : HF : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## HF4N3 (Hf–N)

- Id: `phase:hf-n:hf4n3`; status `assigned`
- Structure: Sc2Te3 · hR8 · R-3m (166); type `st:sc2te3-hr8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Hf 0.5714, N 0.4286
- Stability: stable in 1 of 1 calculated diagram(s): 353.56–2592.71 K, x(N) 0.42857–0.42857
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:hf4n3)

Names (2): _corpus: _corpus:phase:hf-n:hf4n3  
_tdb: _tdb:HfN-18Pan.tdb:HF4N3  


### TDB models of HF4N3 (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): HF4N3, type code %, sha256 `e62247a157b146a1…`

~~~~text
60: PHASE HF4N3 % 2 4 3 !
61: CONST HF4N3 : HF : N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## LIQUID (Hf–N)

- Id: `phase:hf-n:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 2478.01–4000 K, x(N) 0–0.26474
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:liquid)

Names (2): _corpus: _corpus:phase:hf-n:liquid  
_tdb: _tdb:HfN-18Pan.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): LIQUID, type code %, sha256 `e62247a157b146a1…`

~~~~text
35: PHASE LIQUID:L % 1 1 !
36: CONST LIQUID:L : HF N : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
_assessment that models this phase_

## N2GAS (Hf–N)

- Id: `phase:hf-n:n2gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2185 K, x(N) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:hf-n:n2gas)

Names (2): _corpus: _corpus:phase:hf-n:n2gas  
_tdb: _tdb:HfN-18Pan.tdb:N2GAS  


### TDB models of N2GAS (1): PHASE and CONSTITUENT statements as written

[HfN-18Pan.tdb](https://orchid-project.org/data/databases/sgte-binary/HfN-18Pan.tdb): N2GAS, type code %, sha256 `e62247a157b146a1…`

~~~~text
63: PHASE N2GAS % 1 1 !
64: CONST N2GAS : N2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.2298/JMMB170520055P](https://doi.org/10.2298/JMMB170520055P) M. Pang, Y. Peng, P. Zhou, Y. Du, J. Mining Metall. B, 54B, 111-18(2018).  
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
