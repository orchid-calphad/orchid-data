# Mo–P phases

> Mo–P system: 8 phases (tier A 4, tier B 1, liquid 1, needs_review 2); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/MO-P.html · Markdown: https://data.orchid-project.org/phases/pages/MO-P.md

8 phases (tier A 4, tier B 1, liquid 1, needs_review 2); 5 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=MO-P) · [full JSON](https://data.orchid-project.org/phases/systems/MO-P.json) · [Mo–P system page](https://data.orchid-project.org/systems/MO-P.html) · [Markdown](https://data.orchid-project.org/phases/pages/MO-P.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Mo–P system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-mo-p-bcc-a2); _phase:mo-p:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2904.15 K, x(P) 0–0.149 | 0 | 1 |
| [FCC_A1](#phase-mo-p-fcc-a1); _phase:mo-p:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-mo-p-hcp-a3); _phase:mo-p:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-mo-p-liquid); _phase:mo-p:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 821.01–4000 K, x(P) 0–1 | 0 | 1 |
| [MO3P](#phase-mo-p-mo3p); _phase:mo-p:mo3p_ | V3S · tI32 · I-42m (121) | tier B: DFT-supported (unique MP + OQMD match) | stable in 1 of 1 calculated diagram(s): 300–1974.15 K, x(P) 0.25–0.25 | 0 | 1 |
| [MOP_BH](#phase-mo-p-mop-bh); _phase:mo-p:mop-bh_ | WC · B_h · hP2 · P-6m2 (187) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–2154.05 K, x(P) 0.5–0.5 | 0 | 1 |
| [RED_P](#phase-mo-p-p-red); _phase:mo-p:p-red_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–916.01 K, x(P) 1–1 | 0 | 1 |
| [WHITE_P](#phase-mo-p-p-white); _phase:mo-p:p-white_ |  | needs_review | not stable in 1 calculated diagram(s) | 0 | 1 |

## BCC_A2 (Mo–P)

- Id: `phase:mo-p:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2904.15 K, x(P) 0–0.149
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:bcc-a2)

Names (2): _corpus: _corpus:phase:mo-p:bcc-a2  
_tdb: _tdb:MoP-15Mie.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): BCC_A2, type code %B, sha256 `680d0f91cc7104fb…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : MO% P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## FCC_A1 (Mo–P)

- Id: `phase:mo-p:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:fcc-a1)

Names (2): _corpus: _corpus:phase:mo-p:fcc-a1  
_tdb: _tdb:MoP-15Mie.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): FCC_A1, type code %A, sha256 `680d0f91cc7104fb…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : MO P : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## HCP_A3 (Mo–P)

- Id: `phase:mo-p:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Mo 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:hcp-a3)

Names (2): _corpus: _corpus:phase:mo-p:hcp-a3  
_tdb: _tdb:MoP-15Mie.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): HCP_A3, type code %A, sha256 `680d0f91cc7104fb…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : MO : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## LIQUID (Mo–P)

- Id: `phase:mo-p:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 821.01–4000 K, x(P) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:liquid)

Names (2): _corpus: _corpus:phase:mo-p:liquid  
_tdb: _tdb:MoP-15Mie.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): LIQUID, type code %, sha256 `680d0f91cc7104fb…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : MO P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## MO3P (Mo–P)

- Id: `phase:mo-p:mo3p`; status `assigned`
- Structure: V3S · tI32 · I-42m (121); type `st:v3s-ti32`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Mo 0.7500, P 0.2500
- Stability: stable in 1 of 1 calculated diagram(s): 300–1974.15 K, x(P) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:mo3p)

Names (4): _corpus: _corpus:phase:mo-p:mo3p  
_mp: _mp:mp-aaaaaouu  
_oqmd: _oqmd:oqmd-8015  
_tdb: _tdb:MoP-15Mie.tdb:MO3P  


### TDB models of MO3P (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): MO3P, type code %, sha256 `680d0f91cc7104fb…`

~~~~text
53: PHASE MO3P % 2 3 1 !
54: CONST MO3P : MO : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## MOP_BH (Mo–P)

- Id: `phase:mo-p:mop-bh`; status `assigned`
- Structure: WC · B_h · hP2 · P-6m2 (187); type `st:b-h-wc-hp2`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaail and oqmd-13741, space group 187
- Stoichiometry: Mo 0.5000, P 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2154.05 K, x(P) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:mop-bh)

Names (4): _corpus: _corpus:phase:mo-p:mop-bh  
_mp: _mp:mp-aaaaaail  
_oqmd: _oqmd:oqmd-13741  
_tdb: _tdb:MoP-15Mie.tdb:MOP_BH  


### TDB models of MOP_BH (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): MOP_BH, type code %, sha256 `680d0f91cc7104fb…`

~~~~text
58: PHASE MOP_BH % 2 1 1 !
59: CONST MOP_BH : MO : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## RED_P (Mo–P)

- Id: `phase:mo-p:p-red`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RED; no_structure_token
- Candidate (sgte_mmc2): (Red P) — Hallstedt 2025 mmc2 row for RED_P: Red P
- Stoichiometry: P 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–916.01 K, x(P) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:p-red)

Names (2): _corpus: _corpus:phase:mo-p:p-red  
_tdb: _tdb:MoP-15Mie.tdb:RED_P  


### TDB models of RED_P (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): RED_P, type code %, sha256 `680d0f91cc7104fb…`

~~~~text
48: PHASE RED_P % 1 1 !
49: CONST RED_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
_assessment that models this phase_

## WHITE_P (Mo–P)

- Id: `phase:mo-p:p-white`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:WHITE; no_structure_token
- Candidate (sgte_mmc2): (White P) — Hallstedt 2025 mmc2 row for WHITE_P: White P
- Stoichiometry: P 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:mo-p:p-white)

Names (2): _corpus: _corpus:phase:mo-p:p-white  
_tdb: _tdb:MoP-15Mie.tdb:WHITE_P  


### TDB models of WHITE_P (1): PHASE and CONSTITUENT statements as written

[MoP-15Mie.tdb](https://orchid-project.org/data/databases/sgte-binary/MoP-15Mie.tdb): WHITE_P, type code %, sha256 `680d0f91cc7104fb…`

~~~~text
43: PHASE WHITE_P % 1 1 !
44: CONST WHITE_P : P : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1007/s11669-014-0357-z](https://doi.org/10.1007/s11669-014-0357-z) J. Miettinen, A. Pashkova, G. Vassilev, Thermodynamic Description of Ternary FE-X-P Systems. Part 4: FE-MO-P, J. Phase Equilib. Diffus. 36, 60-67 (2015).  
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
