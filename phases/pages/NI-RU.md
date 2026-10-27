# Ni–Ru phases

> Ni–Ru system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-RU.html · Markdown: https://data.orchid-project.org/phases/pages/NI-RU.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-RU) · [full JSON](https://data.orchid-project.org/phases/systems/NI-RU.json) · [Ni–Ru system page](https://data.orchid-project.org/systems/NI-RU.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-RU.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Ru system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ni-ru-bcc-a2); _phase:ni-ru:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-ni-ru-fcc-a1); _phase:ni-ru:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1836.9 K, x(Ru) 0–0.34142 | 0 | 3 |
| [HCP_A3](#phase-ni-ru-hcp-a3); _phase:ni-ru:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–3999.5 K, x(Ru) 0.5053–1 | 0 | 3 |
| [LIQUID](#phase-ni-ru-liquid); _phase:ni-ru:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 1728.25–4000 K, x(Ru) 0–1 | 0 | 3 |

## BCC_A2 (Ni–Ru)

- Id: `phase:ni-ru:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ru:bcc-a2)

Names (4): _corpus: _corpus:phase:ni-ru:bcc-a2  
_tdb: _tdb:NiRu-01Che-LB.tdb:BCC_A2, tdb:NiRu-04Hal.tdb:BCC_A2, tdb:NiRu-08Hal.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[NiRu-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-01Che-LB.tdb): BCC_A2, type code %B, sha256 `cfb9ea78cdca6ee2…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NI RU : VA : !
~~~~

[NiRu-04Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-04Hal.tdb): BCC_A2, type code %B, sha256 `d86ac6781c062de7…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : NI RU : VA : !
~~~~

[NiRu-08Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-08Hal.tdb): BCC_A2, type code %B, sha256 `b00a907636215ffe…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NI RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028) Samuel Hallström, David Andersson, Andrei Ruban, John Ågren, Thermodynamic reassessment of the Ni–Ru system and assessment of the Al–Ni–Ru system at 1273–1523 K using ab initio calculations, Acta Materialia 56, 4062-4069 (2008).  
_assessment that models this phase_
- [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504) Samuel Hallström, Thermodynamic Assessment of the Ni-Ru System, Journal of Phase Equilibria &amp; Diffusion 25, 252-254 (2004).  
_assessment that models this phase_

## FCC_A1 (Ni–Ru)

- Id: `phase:ni-ru:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1836.9 K, x(Ru) 0–0.34142
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ru:fcc-a1)

Names (4): _corpus: _corpus:phase:ni-ru:fcc-a1  
_tdb: _tdb:NiRu-01Che-LB.tdb:FCC_A1, tdb:NiRu-04Hal.tdb:FCC_A1, tdb:NiRu-08Hal.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[NiRu-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-01Che-LB.tdb): FCC_A1, type code %A, sha256 `cfb9ea78cdca6ee2…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NI% RU : VA : !
~~~~

[NiRu-04Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-04Hal.tdb): FCC_A1, type code %A, sha256 `d86ac6781c062de7…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NI% RU : VA : !
~~~~

[NiRu-08Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-08Hal.tdb): FCC_A1, type code %A, sha256 `b00a907636215ffe…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NI% RU : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028) Samuel Hallström, David Andersson, Andrei Ruban, John Ågren, Thermodynamic reassessment of the Ni–Ru system and assessment of the Al–Ni–Ru system at 1273–1523 K using ab initio calculations, Acta Materialia 56, 4062-4069 (2008).  
_assessment that models this phase_
- [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504) Samuel Hallström, Thermodynamic Assessment of the Ni-Ru System, Journal of Phase Equilibria &amp; Diffusion 25, 252-254 (2004).  
_assessment that models this phase_

## HCP_A3 (Ni–Ru)

- Id: `phase:ni-ru:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–3999.5 K, x(Ru) 0.5053–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ru:hcp-a3)

Names (4): _corpus: _corpus:phase:ni-ru:hcp-a3  
_tdb: _tdb:NiRu-01Che-LB.tdb:HCP_A3, tdb:NiRu-04Hal.tdb:HCP_A3, tdb:NiRu-08Hal.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[NiRu-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-01Che-LB.tdb): HCP_A3, type code %A, sha256 `cfb9ea78cdca6ee2…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NI RU% : VA : !
~~~~

[NiRu-04Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-04Hal.tdb): HCP_A3, type code %A, sha256 `d86ac6781c062de7…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : NI RU% : VA : !
~~~~

[NiRu-08Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-08Hal.tdb): HCP_A3, type code %A, sha256 `b00a907636215ffe…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NI RU% : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028) Samuel Hallström, David Andersson, Andrei Ruban, John Ågren, Thermodynamic reassessment of the Ni–Ru system and assessment of the Al–Ni–Ru system at 1273–1523 K using ab initio calculations, Acta Materialia 56, 4062-4069 (2008).  
_assessment that models this phase_
- [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504) Samuel Hallström, Thermodynamic Assessment of the Ni-Ru System, Journal of Phase Equilibria &amp; Diffusion 25, 252-254 (2004).  
_assessment that models this phase_

## LIQUID (Ni–Ru)

- Id: `phase:ni-ru:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 1728.25–4000 K, x(Ru) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-ru:liquid)

Names (4): _corpus: _corpus:phase:ni-ru:liquid  
_tdb: _tdb:NiRu-01Che-LB.tdb:LIQUID, tdb:NiRu-04Hal.tdb:LIQUID, tdb:NiRu-08Hal.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[NiRu-01Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-01Che-LB.tdb): LIQUID, type code %, sha256 `cfb9ea78cdca6ee2…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NI RU : !
~~~~

[NiRu-04Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-04Hal.tdb): LIQUID, type code %, sha256 `d86ac6781c062de7…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NI RU : !
~~~~

[NiRu-08Hal.tdb](https://orchid-project.org/data/databases/sgte-binary/NiRu-08Hal.tdb): LIQUID, type code %, sha256 `b00a907636215ffe…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NI RU : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.actamat.2008.04.028](https://doi.org/10.1016/j.actamat.2008.04.028) Samuel Hallström, David Andersson, Andrei Ruban, John Ågren, Thermodynamic reassessment of the Ni–Ru system and assessment of the Al–Ni–Ru system at 1273–1523 K using ab initio calculations, Acta Materialia 56, 4062-4069 (2008).  
_assessment that models this phase_
- [doi:10.1361/15477030419504](https://doi.org/10.1361/15477030419504) Samuel Hallström, Thermodynamic Assessment of the Ni-Ru System, Journal of Phase Equilibria &amp; Diffusion 25, 252-254 (2004).  
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
