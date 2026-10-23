# Ni–Pt phases

> Ni–Pt system: 6 phases (tier A 4, liquid 1, needs_review 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/NI-PT.html · Markdown: https://data.orchid-project.org/phases/pages/NI-PT.md

6 phases (tier A 4, liquid 1, needs_review 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=NI-PT) · [full JSON](https://data.orchid-project.org/phases/systems/NI-PT.json) · [Ni–Pt system page](https://data.orchid-project.org/systems/NI-PT.html) · [Markdown](https://data.orchid-project.org/phases/pages/NI-PT.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ni–Pt system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [A2_BCC](#phase-ni-pt-bcc-a2); _phase:ni-pt:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [B2_BCC](#phase-ni-pt-bcc-b2); _phase:ni-pt:bcc-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_4SL](#phase-ni-pt-fcc-4sl); _phase:ni-pt:fcc-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2499 K, x(Pt) 0–1 | 0 | 1 |
| [A1_FCC](#phase-ni-pt-fcc-a1); _phase:ni-pt:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 2 calculated diagram(s): 300–2020 K, x(Pt) 0–0.99 | 0 | 2 |
| [HCP_A3](#phase-ni-pt-hcp-a3); _phase:ni-pt:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-ni-pt-liquid); _phase:ni-pt:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1707.92–2500 K, x(Pt) 0–1 | 0 | 1 |

## A2_BCC (Ni–Pt)

- Id: `phase:ni-pt:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pt:bcc-a2)

Names (3): _corpus: _corpus:phase:ni-pt:bcc-a2  
_tdb: _tdb:NiPt-09Lu.tdb:A2_BCC, tdb:NiPt-09Lu.tdb:BCC_A2  


### TDB models of A2_BCC (2): PHASE and CONSTITUENT statements as written

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): A2_BCC, type code %B, sha256 `fe66306490091640…`

~~~~text
47: PHASE A2_BCC %B 2 1 3 !
48: CONST A2_BCC : NI PT VA : VA : !
~~~~

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): BCC_A2, type code %B, sha256 `fe66306490091640…`

~~~~text
42: PHASE BCC_A2 %B 2 1 3 !
43: CONST BCC_A2 : NI PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009).  
_assessment that models this phase_

## B2_BCC (Ni–Pt)

- Id: `phase:ni-pt:bcc-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Caveat: NiPt-09Lu.tdb: ordered phase with disordered part A2_BCC (order/disorder model)
- Caveat: partitioned order/disorder model in NiPt-09Lu.tdb also describes the disordered state
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pt:bcc-b2)

Names (2): _corpus: _corpus:phase:ni-pt:bcc-b2  
_tdb: _tdb:NiPt-09Lu.tdb:B2_BCC  


### TDB models of B2_BCC (1): PHASE and CONSTITUENT statements as written

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): B2_BCC, type code %BO, sha256 `fe66306490091640…`

~~~~text
52: PHASE B2_BCC %BO 3 0.5 0.5 3 !
53: CONST B2_BCC : NI PT VA : NI PT VA : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009).  
_assessment that models this phase_

## FCC_4SL (Ni–Pt)

- Id: `phase:ni-pt:fcc-4sl`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:order_disorder_ambiguity; order_disorder_ambiguity:NiPt-09Lu.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:FCC_4SL; unrecognised_name_tokens:4SL
- Candidate (dft_mp): Pm-3m (221) — on-hull MP Ni3Pt at x(PT)=0.2500
- Candidate (dft_mp): P4/mmm (123) — on-hull MP NiPt at x(PT)=0.5000
- Candidate (dft_mp): Pm-3m (221) — on-hull MP NiPt3 at x(PT)=0.7500
- Candidate (dft_oqmd): P4/mmm (123) — on-hull OQMD Ni1 Pt1 at x(PT)=0.5000
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Ni1 Pt3 at x(PT)=0.7500
- Candidate (dft_oqmd): Pm-3m (221) — on-hull OQMD Ni3 Pt1 at x(PT)=0.2500
- Candidate (name_token): Cu · A1 · cF4 · Fm-3m (225) — Strukturbericht/word 'A1' in the TDB name
- Candidate (sgte_mmc2): AuCu3 · L1_2 · cP4 · Pm-3m (221) — Hallstedt 2025 mmc2 row for FCC_4SL: Ag3Mg, Al3Li, AlNi3, AlPt3, Au3Cu, AuCu3, Co3Pt, CoPt3, Cr3Pt, CrPt3, Cu3Pt, FeNi3, Fe3Pt, FePt3, MnNi3, Ni3Pt, NiPt3, Ni3Si (beta-1)
- Stability: stable in 1 of 1 calculated diagram(s): 300–2499 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pt:fcc-4sl)

Names (2): _corpus: _corpus:phase:ni-pt:fcc-4sl  
_tdb: _tdb:NiPt-09Lu.tdb:FCC_4SL  


### TDB models of FCC_4SL (1): PHASE and CONSTITUENT statements as written

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): FCC_4SL, type code %AY, sha256 `fe66306490091640…`

~~~~text
37: PHASE FCC_4SL %AY 5 0.25 0.25 0.25 0.25 1 !
38: CONST FCC_4SL : NI PT : NI PT : NI PT : NI PT : VA :  !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009).  
_assessment that models this phase_

## A1_FCC (Ni–Pt)

- Id: `phase:ni-pt:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 2 calculated diagram(s): 300–2020 K, x(Pt) 0–0.99
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pt:fcc-a1)

Names (3): _corpus: _corpus:phase:ni-pt:fcc-a1  
_tdb: _tdb:NiPt-09Lu.tdb:A1_FCC, tdb:NiPt-09Lu.tdb:FCC_A1  


### TDB models of A1_FCC (2): PHASE and CONSTITUENT statements as written

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): A1_FCC, type code %A, sha256 `fe66306490091640…`

~~~~text
32: PHASE A1_FCC %A 2 1 1 !
33: CONST A1_FCC : NI PT : VA : !
~~~~

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): FCC_A1, type code %A, sha256 `fe66306490091640…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : NI% PT% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009).  
_assessment that models this phase_

## HCP_A3 (Ni–Pt)

- Id: `phase:ni-pt:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pt:hcp-a3)

Names (2): _corpus: _corpus:phase:ni-pt:hcp-a3  
_tdb: _tdb:NiPt-09Lu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): HCP_A3, type code %A, sha256 `fe66306490091640…`

~~~~text
57: PHASE HCP_A3 %A 2 1 0.5 !
58: CONST HCP_A3 : NI PT : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009).  
_assessment that models this phase_

## LIQUID (Ni–Pt)

- Id: `phase:ni-pt:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1707.92–2500 K, x(Pt) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ni-pt:liquid)

Names (2): _corpus: _corpus:phase:ni-pt:liquid  
_tdb: _tdb:NiPt-09Lu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[NiPt-09Lu.tdb](https://orchid-project.org/data/databases/sgte-binary/NiPt-09Lu.tdb): LIQUID, type code %, sha256 `fe66306490091640…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : NI PT : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2009.06.002](https://doi.org/10.1016/j.calphad.2009.06.002) Xiao-Gang Lu, Bo Sundman, John A˚gren, Thermodynamic assessments of the Ni–Pt and Al–Ni–Pt systems, Calphad 33, 450-456 (2009).  
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
