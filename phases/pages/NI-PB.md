# Ni–Pb phases

> Ni–Pb system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-PB.html · Markdown: https://data.orchid-project.org/phases/pages/NI-PB.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-PB) · [full JSON](https://data.orchid-project.org/phases/systems/NI-PB.json) · [Ni–Pb system page](https://data.orchid-project.org/systems/NI-PB.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-PB.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Pb system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-ni-pb-bcc-a2); _phase:ni-pb:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [FCC_A1](#phase-ni-pb-fcc-a1); _phase:ni-pb:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 300–2499.4 K, x(Pb) 0–1 | 20 | 4 |
| [HCP_A3](#phase-ni-pb-hcp-a3); _phase:ni-pb:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 4 calculated diagram(s): 600–600 K, x(Pb) 0.16–0.7 | 0 | 4 |
| [LIQUID](#phase-ni-pb-liquid); _phase:ni-pb:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 598.15–2500 K, x(Pb) 0–1 | 31 | 4 |

## BCC_A2 (Ni–Pb)

- Id: `phase:ni-pb:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pb:bcc-a2)

Names (5): _corpus: _corpus:phase:ni-pb:bcc-a2  
_tdb: _tdb:NiPb-00Wan-LB.tdb:BCC_A2, tdb:NiPb-10Kai.tdb:BCC_A2, tdb:NiPb-13Vaa.tdb:BCC_A2, tdb:NiPb-99Gho.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[NiPb-00Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-00Wan-LB.tdb): BCC_A2, type code %B, sha256 `8aeb2c456644892c…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NI PB : VA : !
~~~~

[NiPb-10Kai.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-10Kai.tdb): BCC_A2, type code %B, sha256 `72882d15b39ccedf…`

~~~~text
36: PHASE BCC_A2 %B 2 1 3 !
37: CONST BCC_A2 : NI PB : VA : !
~~~~

[NiPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-13Vaa.tdb): BCC_A2, type code %B, sha256 `45da44d5203a07e7…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : NI PB : VA : !
~~~~

[NiPb-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-99Gho.tdb): BCC_A2, type code %B, sha256 `76b83859e1d1c4ef…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : NI PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.08.001](https://doi.org/10.1016/j.calphad.2010.08.001) I. Kainulainen, P. Taskinen, J. Gisby, A thermodynamic assessment of the nickel–lead system, Calphad 34, 441-445 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.06.004](https://doi.org/10.1016/j.calphad.2013.06.004) I. Vaajamo, P. Taskinen, J.A. Gisby, A solubility study and thermodynamic description of the system Fe–Ni–Pb, Calphad 42, 66-75 (2013).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase_

## FCC_A1 (Ni–Pb)

- Id: `phase:ni-pb:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 300–2499.4 K, x(Pb) 0–1
- Literature: 20 values (20 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pb:fcc-a1)

Names (11): _corpus: _corpus:phase:ni-pb:fcc-a1  
_paper: _paper:10.1016/j.calphad.2010.08.001:(Ni), paper:10.1016/j.calphad.2010.08.001:(Pb), paper:10.1016/j.calphad.2013.06.004:FCC_A1#1, paper:10.1016/j.calphad.2013.06.004:FCC_A1#2, paper:10.1016/s0364-5916(00)00020-1:(Ni), paper:10.1016/s0364-5916(00)00020-1:(Pb)  
_tdb: _tdb:NiPb-00Wan-LB.tdb:FCC_A1, tdb:NiPb-10Kai.tdb:FCC_A1, tdb:NiPb-13Vaa.tdb:FCC_A1, tdb:NiPb-99Gho.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[NiPb-00Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-00Wan-LB.tdb): FCC_A1, type code %A, sha256 `8aeb2c456644892c…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NI% PB% : VA : !
~~~~

[NiPb-10Kai.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-10Kai.tdb): FCC_A1, type code %A, sha256 `72882d15b39ccedf…`

~~~~text
31: PHASE FCC_A1 %A 2 1 1 !
32: CONST FCC_A1 : NI% PB% : VA : !
~~~~

[NiPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-13Vaa.tdb): FCC_A1, type code %A, sha256 `45da44d5203a07e7…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : NI% PB% : VA : !
~~~~

[NiPb-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-99Gho.tdb): FCC_A1, type code %A, sha256 `76b83859e1d1c4ef…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : NI% PB% : VA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.08.001](https://doi.org/10.1016/j.calphad.2010.08.001) I. Kainulainen, P. Taskinen, J. Gisby, A thermodynamic assessment of the nickel–lead system, Calphad 34, 441-445 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.06.004](https://doi.org/10.1016/j.calphad.2013.06.004) I. Vaajamo, P. Taskinen, J.A. Gisby, A solubility study and thermodynamic description of the system Fe–Ni–Pb, Calphad 42, 66-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02874918](https://doi.org/10.1007/bf02874918) P. Nash, The Ni–Pb (nickel–lead) system, Bull. Alloy Phase Diagr. 8 (3) (1987) 264–301.  
_cited as the source of values for this phase_

## HCP_A3 (Ni–Pb)

- Id: `phase:ni-pb:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 4 calculated diagram(s): 600–600 K, x(Pb) 0.16–0.7
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pb:hcp-a3)

Names (5): _corpus: _corpus:phase:ni-pb:hcp-a3  
_tdb: _tdb:NiPb-00Wan-LB.tdb:HCP_A3, tdb:NiPb-10Kai.tdb:HCP_A3, tdb:NiPb-13Vaa.tdb:HCP_A3, tdb:NiPb-99Gho.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[NiPb-00Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-00Wan-LB.tdb): HCP_A3, type code %A, sha256 `8aeb2c456644892c…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NI PB : VA : !
~~~~

[NiPb-10Kai.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-10Kai.tdb): HCP_A3, type code %A, sha256 `72882d15b39ccedf…`

~~~~text
41: PHASE HCP_A3 %A 2 1 0.5 !
42: CONST HCP_A3 : NI PB : VA : !
~~~~

[NiPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-13Vaa.tdb): HCP_A3, type code %A, sha256 `45da44d5203a07e7…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : NI PB : VA : !
~~~~

[NiPb-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-99Gho.tdb): HCP_A3, type code %A, sha256 `76b83859e1d1c4ef…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : NI PB : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.08.001](https://doi.org/10.1016/j.calphad.2010.08.001) I. Kainulainen, P. Taskinen, J. Gisby, A thermodynamic assessment of the nickel–lead system, Calphad 34, 441-445 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2013.06.004](https://doi.org/10.1016/j.calphad.2013.06.004) I. Vaajamo, P. Taskinen, J.A. Gisby, A solubility study and thermodynamic description of the system Fe–Ni–Pb, Calphad 42, 66-75 (2013).  
_assessment that models this phase_
- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase_

## LIQUID (Ni–Pb)

- Id: `phase:ni-pb:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 598.15–2500 K, x(Pb) 0–1
- Literature: 31 values (31 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pb:liquid)

Names (11): _corpus: _corpus:phase:ni-pb:liquid  
_paper: _paper:10.1016/j.calphad.2010.08.001:L, paper:10.1016/j.calphad.2010.08.001:L2, paper:10.1016/j.calphad.2013.06.004:LIQUID, paper:10.1016/j.calphad.2013.06.004:LIQUID#2, paper:10.1016/s0364-5916(00)00020-1:L, paper:10.1016/s0364-5916(00)00020-1:L2  
_tdb: _tdb:NiPb-00Wan-LB.tdb:LIQUID, tdb:NiPb-10Kai.tdb:LIQUID, tdb:NiPb-13Vaa.tdb:LIQUID, tdb:NiPb-99Gho.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[NiPb-00Wan-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-00Wan-LB.tdb): LIQUID, type code %, sha256 `8aeb2c456644892c…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NI PB : !
~~~~

[NiPb-10Kai.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-10Kai.tdb): LIQUID, type code %, sha256 `72882d15b39ccedf…`

~~~~text
26: PHASE LIQUID:L % 1 1 !
27: CONST LIQUID:L : NI PB : !
~~~~

[NiPb-13Vaa.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-13Vaa.tdb): LIQUID, type code %, sha256 `45da44d5203a07e7…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : NI PB : !
~~~~

[NiPb-99Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPb-99Gho.tdb): LIQUID, type code %, sha256 `76b83859e1d1c4ef…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : NI PB : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.08.001](https://doi.org/10.1016/j.calphad.2010.08.001) I. Kainulainen, P. Taskinen, J. Gisby, A thermodynamic assessment of the nickel–lead system, Calphad 34, 441-445 (2010).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/S0364-5916(00)00020-1](https://doi.org/10.1016/S0364-5916%2800%2900020-1) C.P. Wang, X.J. Liu, I. Ohnuma, R. Kainuma, K. Ishida, Calphad, 24, 149-67(2000).  
_assessment that models this phase; cited as the source of values for this phase; reports values for this phase_
- [doi:10.1016/j.calphad.2013.06.004](https://doi.org/10.1016/j.calphad.2013.06.004) I. Vaajamo, P. Taskinen, J.A. Gisby, A solubility study and thermodynamic description of the system Fe–Ni–Pb, Calphad 42, 66-75 (2013).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11661-999-0085-x](https://doi.org/10.1007/s11661-999-0085-x) G. Ghosh, Thermodynamic modeling of the nickel-lead-tin system, Metall Mater Trans A 30, 1481-1494 (1999).  
_cited as the source of values for this phase_
- [doi:10.1007/bf02874918](https://doi.org/10.1007/bf02874918) P. Nash, The Ni–Pb (nickel–lead) system, Bull. Alloy Phase Diagr. 8 (3) (1987) 264–301.  
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
