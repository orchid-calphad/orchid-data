# Cr–La phases

> Cr–La system: 5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-LA.html · Markdown: https://data.orchid-project.org/phases/pages/CR-LA.md

5 phases (tier A 4, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-LA) · [full JSON](https://data.orchid-project.org/phases/systems/CR-LA.json) · [Cr–La system page](https://data.orchid-project.org/systems/CR-LA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-LA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–La system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-la-bcc-a2); _phase:cr-la:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.16 K, x(La) 0–1 | 10 | 2 |
| [DHCP](#phase-cr-la-dhcp-a3); _phase:cr-la:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1125 K, x(La) 1–1 | 1 | 2 |
| [FCC_A1](#phase-cr-la-fcc-a1); _phase:cr-la:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 549.93–1189 K, x(La) 0.99553–1 | 0 | 2 |
| [HCP_A3](#phase-cr-la-hcp-a3); _phase:cr-la:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-cr-la-liquid); _phase:cr-la:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1126.03–4000 K, x(La) 0–1 | 12 | 2 |

## BCC_A2 (Cr–La)

- Id: `phase:cr-la:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.16 K, x(La) 0–1
- Literature: 10 values (10 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-la:bcc-a2)

Names (4): _corpus: _corpus:phase:cr-la:bcc-a2  
_paper: _paper:10.1007/s11669-009-9581-3:Cr  
_tdb: _tdb:CrLa-09Cha.tdb:BCC_A2, tdb:CrLa-09Pov.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CrLa-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb): BCC_A2, type code %B, sha256 `7eae47ddc2ae31ca…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : CR LA : VA : !
~~~~

[CrLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb): BCC_A2, type code %B, sha256 `af1685101b0145ad…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009).  
_assessment that models this phase_

## DHCP (Cr–La)

- Id: `phase:cr-la:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: La 1.0000
- Stability: stable in 2 of 2 calculated diagram(s): 300–1125 K, x(La) 1–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-la:dhcp-a3)

Names (5): _corpus: _corpus:phase:cr-la:dhcp-a3, corpus:phase:cr-la:dhcp  
_paper: _paper:10.1007/s11669-009-9581-3:αLa  
_tdb: _tdb:CrLa-09Cha.tdb:DHCP, tdb:CrLa-09Pov.tdb:DHCP  


### TDB models of DHCP (2): PHASE and CONSTITUENT statements as written

[CrLa-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb): DHCP, type code %, sha256 `7eae47ddc2ae31ca…`

~~~~text
41: PHASE DHCP % 2 1 0.5 !
42: CONST DHCP : LA : VA : !
~~~~

[CrLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb): DHCP, type code %, sha256 `af1685101b0145ad…`

~~~~text
43: PHASE DHCP % 2 1 0.5 !
44: CONST DHCP : LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009).  
_assessment that models this phase_

## FCC_A1 (Cr–La)

- Id: `phase:cr-la:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 549.93–1189 K, x(La) 0.99553–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-la:fcc-a1)

Names (3): _corpus: _corpus:phase:cr-la:fcc-a1  
_tdb: _tdb:CrLa-09Cha.tdb:FCC_A1, tdb:CrLa-09Pov.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CrLa-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb): FCC_A1, type code %A, sha256 `7eae47ddc2ae31ca…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : CR LA : VA : !
~~~~

[CrLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb): FCC_A1, type code %A, sha256 `af1685101b0145ad…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR LA : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase_

## HCP_A3 (Cr–La)

- Id: `phase:cr-la:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Cr 1.0000
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-la:hcp-a3)

Names (3): _corpus: _corpus:phase:cr-la:hcp-a3  
_tdb: _tdb:CrLa-09Cha.tdb:HCP_A3, tdb:CrLa-09Pov.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CrLa-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb): HCP_A3, type code %A, sha256 `7eae47ddc2ae31ca…`

~~~~text
36: PHASE HCP_A3 %A 2 1 0.5 !
37: CONST HCP_A3 : CR : VA : !
~~~~

[CrLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb): HCP_A3, type code %A, sha256 `af1685101b0145ad…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009).  
_assessment that models this phase_
- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase_

## LIQUID (Cr–La)

- Id: `phase:cr-la:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1126.03–4000 K, x(La) 0–1
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-la:liquid)

Names (6): _corpus: _corpus:phase:cr-la:liquid  
_paper: _paper:10.1007/s11669-008-9463-0:liquid, paper:10.1007/s11669-009-9581-3:L1, paper:10.1007/s11669-009-9581-3:L2  
_tdb: _tdb:CrLa-09Cha.tdb:LIQUID, tdb:CrLa-09Pov.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CrLa-09Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Cha.tdb): LIQUID, type code %, sha256 `7eae47ddc2ae31ca…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : CR LA : !
~~~~

[CrLa-09Pov.tdb](https://orchid-project.org/data/databases/sgte-binary/CrLa-09Pov.tdb): LIQUID, type code %, sha256 `af1685101b0145ad…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR LA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1007/s11669-009-9581-3](https://doi.org/10.1007/s11669-009-9581-3) Wren Chan, Michael C. Gao, Ömer N. Doğan, Paul King, Anthony D. Rollett, Thermodynamic Assessment of Cr-Rare Earth Systems, J. Phase Equilib. Diffus. 30, 578-586 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/s11669-008-9463-0](https://doi.org/10.1007/s11669-008-9463-0) E. Povoden, M. Chen, A.N. Grundy, T. Ivas, L.J. Gauckler, Thermodynamic Assessment of the La-Cr-O System, J. Phase Equilib. Diffus. 30, 12-27 (2009).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(91)90030-n](https://doi.org/10.1016/0364-5916%2891%2990030-n) A.T. Dinsdale, SGTE data for pure elements, Calphad 15, 317-425 (1991).  
_cited as the source of values for this phase_

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
