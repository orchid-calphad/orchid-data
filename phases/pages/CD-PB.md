# Cd–Pb phases

> Cd–Pb system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-PB.html · Markdown: https://data.orchid-project.org/phases/pages/CD-PB.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-PB) · [full JSON](https://data.orchid-project.org/phases/systems/CD-PB.json) · [Cd–Pb system page](https://data.orchid-project.org/systems/CD-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Pb system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-pb-bcc-a2); _phase:cd-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [FCC_A1](#phase-cd-pb-fcc-a1); _phase:cd-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–600.61 K, x(Pb) 0.937–1 | 8 | 3 |
| [HCP_A3](#phase-cd-pb-hcp-a3); _phase:cd-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–594.22 K, x(Pb) 0–0.00096 | 8 | 3 |
| [LIQUID](#phase-cd-pb-liquid); _phase:cd-pb:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 519.41–2500 K, x(Pb) 0–1 | 28 | 3 |

## BCC_A2 (Cd–Pb)

- Id: `phase:cd-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pb:bcc-a2)

Names (4): _corpus: _corpus:phase:cd-pb:bcc-a2  
_tdb: _tdb:CdPb-09Liu.tdb:BCC_A2, tdb:CdPb-13Chu.tdb:BCC_A2, tdb:CdPb-95Zak-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CdPb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-09Liu.tdb): BCC_A2, type code %B, sha256 `fd9f4bfb9f06e5d0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CD PB : VA : !
~~~~

[CdPb-13Chu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-13Chu.tdb): BCC_A2, type code %B, sha256 `e09248547e361e2b…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CD PB : VA : !
~~~~

[CdPb-95Zak-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-95Zak-LB.tdb): BCC_A2, type code %B, sha256 `38bd375c9b9bc555…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : CD PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/BF02667308](https://doi.org/10.1007/BF02667308) W. Zakulski, Z. Moser, J. Phase Equilib., 16, 239-42(1995).  
_assessment that models this phase_
- [doi:10.1007/s11661-013-1652-8](https://doi.org/10.1007/s11661-013-1652-8) Ying-Yu Chuang, J.-S. Paik, C. Zhang, J. H. Perepezko, Y. A. Chang, Stable and Metastable Equilibria in the Pb-Cd System, Metall Mater Trans A 44, 3004-3013 (2013).  
_assessment that models this phase_
- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase_

## FCC_A1 (Cd–Pb)

- Id: `phase:cd-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–600.61 K, x(Pb) 0.937–1
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pb:fcc-a1)

Names (6): _corpus: _corpus:phase:cd-pb:fcc-a1  
_paper: _paper:10.1007/s11661-013-1652-8:fcc, paper:10.1007/s11664-009-0875-3:fcc  
_tdb: _tdb:CdPb-09Liu.tdb:FCC_A1, tdb:CdPb-13Chu.tdb:FCC_A1, tdb:CdPb-95Zak-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CdPb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-09Liu.tdb): FCC_A1, type code %A, sha256 `fd9f4bfb9f06e5d0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CD PB% : VA : !
~~~~

[CdPb-13Chu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-13Chu.tdb): FCC_A1, type code %A, sha256 `e09248547e361e2b…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CD PB% : VA : !
~~~~

[CdPb-95Zak-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-95Zak-LB.tdb): FCC_A1, type code %A, sha256 `38bd375c9b9bc555…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : CD PB% : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-013-1652-8](https://doi.org/10.1007/s11661-013-1652-8) Ying-Yu Chuang, J.-S. Paik, C. Zhang, J. H. Perepezko, Y. A. Chang, Stable and Metastable Equilibria in the Pb-Cd System, Metall Mater Trans A 44, 3004-3013 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667308](https://doi.org/10.1007/BF02667308) W. Zakulski, Z. Moser, J. Phase Equilib., 16, 239-42(1995).  
_assessment that models this phase_
- [doi:10.1007/bf02670872](https://doi.org/10.1007/bf02670872) Christopher W. Bale, A. D. Pelton, Optimization of binary thermodynamic and phase diagram data, Metall Trans B 14, 77-83 (1983).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02873710](https://doi.org/10.1007/bf02873710) S. Ashtakala, A.D. Pelton, and C.W. Bale: Bull. Alloy Phase Diagrams, 1981, vol. 2, pp. 83–86.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(80)87151-6](https://doi.org/10.1016/0040-6031%2880%2987151-6) Louis Schuffenecker, Daniel Balesdent, Jacques Houriez, Diagramme de phases et proprietes thermodynamiques du systeme cadmium—plomb, Thermochimica Acta 38, 89-96 (1980).  
_cited as the source of values for this phase_

## HCP_A3 (Cd–Pb)

- Id: `phase:cd-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–594.22 K, x(Pb) 0–0.00096
- Literature: 8 values (8 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pb:hcp-a3)

Names (6): _corpus: _corpus:phase:cd-pb:hcp-a3  
_paper: _paper:10.1007/s11661-013-1652-8:hcp, paper:10.1007/s11664-009-0875-3:hcp  
_tdb: _tdb:CdPb-09Liu.tdb:HCP_A3, tdb:CdPb-13Chu.tdb:HCP_A3, tdb:CdPb-95Zak-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CdPb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-09Liu.tdb): HCP_A3, type code %A, sha256 `fd9f4bfb9f06e5d0…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CD% PB : VA : !
~~~~

[CdPb-13Chu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-13Chu.tdb): HCP_A3, type code %A, sha256 `e09248547e361e2b…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CD% PB : VA : !
~~~~

[CdPb-95Zak-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-95Zak-LB.tdb): HCP_A3, type code %A, sha256 `38bd375c9b9bc555…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : CD% PB : VA : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-013-1652-8](https://doi.org/10.1007/s11661-013-1652-8) Ying-Yu Chuang, J.-S. Paik, C. Zhang, J. H. Perepezko, Y. A. Chang, Stable and Metastable Equilibria in the Pb-Cd System, Metall Mater Trans A 44, 3004-3013 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667308](https://doi.org/10.1007/BF02667308) W. Zakulski, Z. Moser, J. Phase Equilib., 16, 239-42(1995).  
_assessment that models this phase_
- [doi:10.1007/bf02670872](https://doi.org/10.1007/bf02670872) Christopher W. Bale, A. D. Pelton, Optimization of binary thermodynamic and phase diagram data, Metall Trans B 14, 77-83 (1983).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02873710](https://doi.org/10.1007/bf02873710) S. Ashtakala, A.D. Pelton, and C.W. Bale: Bull. Alloy Phase Diagrams, 1981, vol. 2, pp. 83–86.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(80)87151-6](https://doi.org/10.1016/0040-6031%2880%2987151-6) Louis Schuffenecker, Daniel Balesdent, Jacques Houriez, Diagramme de phases et proprietes thermodynamiques du systeme cadmium—plomb, Thermochimica Acta 38, 89-96 (1980).  
_cited as the source of values for this phase_

## LIQUID (Cd–Pb)

- Id: `phase:cd-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 519.41–2500 K, x(Pb) 0–1
- Literature: 28 values (28 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-pb:liquid)

Names (8): _corpus: _corpus:phase:cd-pb:liquid  
_paper: _paper:10.1007/s11661-013-1652-8:L, paper:10.1007/s11661-013-1652-8:L2, paper:10.1007/s11661-013-1652-8:liquid, paper:10.1007/s11664-009-0875-3:liq  
_tdb: _tdb:CdPb-09Liu.tdb:LIQUID, tdb:CdPb-13Chu.tdb:LIQUID, tdb:CdPb-95Zak-LB.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CdPb-09Liu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-09Liu.tdb): LIQUID, type code %, sha256 `fd9f4bfb9f06e5d0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CD PB : !
~~~~

[CdPb-13Chu.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-13Chu.tdb): LIQUID, type code %, sha256 `e09248547e361e2b…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CD PB : !
~~~~

[CdPb-95Zak-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdPb-95Zak-LB.tdb): LIQUID, type code %, sha256 `38bd375c9b9bc555…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : CD PB : !
~~~~

Example references (6 of 6; assessments first): 

- [doi:10.1007/s11661-013-1652-8](https://doi.org/10.1007/s11661-013-1652-8) Ying-Yu Chuang, J.-S. Paik, C. Zhang, J. H. Perepezko, Y. A. Chang, Stable and Metastable Equilibria in the Pb-Cd System, Metall Mater Trans A 44, 3004-3013 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11664-009-0875-3](https://doi.org/10.1007/s11664-009-0875-3) Yajun Liu, Lijun Zhang, Di Yu, Thermodynamic Descriptions for the Cd-Te, Pb-Te, Cd-Pb and Cd-Pb-Te Systems, Journal of Elec Materi 38, 2033-2045 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/BF02667308](https://doi.org/10.1007/BF02667308) W. Zakulski, Z. Moser, J. Phase Equilib., 16, 239-42(1995).  
_assessment that models this phase_
- [doi:10.1007/bf02670872](https://doi.org/10.1007/bf02670872) Christopher W. Bale, A. D. Pelton, Optimization of binary thermodynamic and phase diagram data, Metall Trans B 14, 77-83 (1983).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02873710](https://doi.org/10.1007/bf02873710) S. Ashtakala, A.D. Pelton, and C.W. Bale: Bull. Alloy Phase Diagrams, 1981, vol. 2, pp. 83–86.  
_cited as the source of values for this phase_
- [doi:10.1016/0040-6031(80)87151-6](https://doi.org/10.1016/0040-6031%2880%2987151-6) Louis Schuffenecker, Daniel Balesdent, Jacques Houriez, Diagramme de phases et proprietes thermodynamiques du systeme cadmium—plomb, Thermochimica Acta 38, 89-96 (1980).  
_cited as the source of values for this phase_

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
