# Os–Pt phases

> Os–Pt system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/OS-PT.html · Markdown: https://data.orchid-project.org/phases/pages/OS-PT.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=OS-PT) · [full JSON](https://data.orchid-project.org/phases/systems/OS-PT.json) · [Os–Pt system page](https://data.orchid-project.org/systems/OS-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/OS-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Os–Pt system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-os-pt-bcc-a2); _phase:os-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-os-pt-fcc-a1); _phase:os-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2234.17 K, x(Pt) 0.70252–1 | 0 | 1 |
| [HCP_A3](#phase-os-pt-hcp-a3); _phase:os-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–3307 K, x(Pt) 0–0.09013 | 0 | 1 |
| [LIQUID](#phase-os-pt-liquid); _phase:os-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1116.5–4000 K, x(Pt) 0–1 | 0 | 1 |

## BCC_A2 (Os–Pt)

- Id: `phase:os-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-pt:bcc-a2)

Names (2): _corpus: _corpus:phase:os-pt:bcc-a2  
_tdb: _tdb:OsPt-21Jou.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[OsPt-21Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/OsPt-21Jou.tdb): BCC_A2, type code %B, sha256 `eb70102a6e4a5bc9…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : OS PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102311](https://doi.org/10.1016/j.calphad.2021.102311) Jean-Marc Joubert, Jean-Claude Crivello, Kirill V. Yusenko, Modification of Lu's (2005) high pressure model for improved high pressure/high temperature extrapolations. Part II: Modeling of osmium–platinum system at high pressure/high temperature, Calphad 74, 102311 (2021).  
_assessment that models this phase_

## FCC_A1 (Os–Pt)

- Id: `phase:os-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2234.17 K, x(Pt) 0.70252–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-pt:fcc-a1)

Names (2): _corpus: _corpus:phase:os-pt:fcc-a1  
_tdb: _tdb:OsPt-21Jou.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[OsPt-21Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/OsPt-21Jou.tdb): FCC_A1, type code %A, sha256 `eb70102a6e4a5bc9…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : OS PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102311](https://doi.org/10.1016/j.calphad.2021.102311) Jean-Marc Joubert, Jean-Claude Crivello, Kirill V. Yusenko, Modification of Lu's (2005) high pressure model for improved high pressure/high temperature extrapolations. Part II: Modeling of osmium–platinum system at high pressure/high temperature, Calphad 74, 102311 (2021).  
_assessment that models this phase_

## HCP_A3 (Os–Pt)

- Id: `phase:os-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–3307 K, x(Pt) 0–0.09013
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:os-pt:hcp-a3  
_tdb: _tdb:OsPt-21Jou.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[OsPt-21Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/OsPt-21Jou.tdb): HCP_A3, type code %, sha256 `eb70102a6e4a5bc9…`

~~~~text
37: PHASE HCP_A3 % 2 1 0.5 !
38: CONST HCP_A3 : OS% PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102311](https://doi.org/10.1016/j.calphad.2021.102311) Jean-Marc Joubert, Jean-Claude Crivello, Kirill V. Yusenko, Modification of Lu's (2005) high pressure model for improved high pressure/high temperature extrapolations. Part II: Modeling of osmium–platinum system at high pressure/high temperature, Calphad 74, 102311 (2021).  
_assessment that models this phase_

## LIQUID (Os–Pt)

- Id: `phase:os-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1116.5–4000 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:os-pt:liquid)

Names (2): _corpus: _corpus:phase:os-pt:liquid  
_tdb: _tdb:OsPt-21Jou.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[OsPt-21Jou.tdb](https://orchid-project.org/data/databases/sgte-binary/OsPt-21Jou.tdb): LIQUID, type code %, sha256 `eb70102a6e4a5bc9…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : OS PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2021.102311](https://doi.org/10.1016/j.calphad.2021.102311) Jean-Marc Joubert, Jean-Claude Crivello, Kirill V. Yusenko, Modification of Lu's (2005) high pressure model for improved high pressure/high temperature extrapolations. Part II: Modeling of osmium–platinum system at high pressure/high temperature, Calphad 74, 102311 (2021).  
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
