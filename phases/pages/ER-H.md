# Er–H phases

> Er–H system: 5 phases (tier A 2, liquid 1, gas 1, needs_review 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/ER-H.html · Markdown: https://data.orchid-project.org/phases/pages/ER-H.md

5 phases (tier A 2, liquid 1, gas 1, needs_review 1); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=ER-H) · [full JSON](https://data.orchid-project.org/phases/systems/ER-H.json) · [Er–H system page](https://data.orchid-project.org/systems/ER-H.html) · [Markdown](https://data.orchid-project.org/phases/pages/ER-H.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Er–H system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-er-h-bcc-a2); _phase:er-h:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 4 | 1 |
| [FCC_A1](#phase-er-h-fcc-a1); _phase:er-h:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1494.6 K, x(H) 0.44743–0.70158 | 0 | 1 |
| [GAS](#phase-er-h-gas); _phase:er-h:gas_ | gas | gas | stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 1–1 | 0 | 1 |
| [HCP_A3](#phase-er-h-hcp-a3); _phase:er-h:hcp-a3_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2047.56 K, x(H) 0–0.75 | 4 | 1 |
| [LIQUID](#phase-er-h-liquid); _phase:er-h:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1795–2500 K, x(H) 0–0.00509 | 0 | 1 |

## BCC_A2 (Er–H)

- Id: `phase:er-h:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: Er 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-h:bcc-a2)

Names (3): _corpus: _corpus:phase:er-h:bcc-a2  
_paper: _paper:10.1016/j.calphad.2013.01.004:β-ErH2  
_tdb: _tdb:ErH-13Mas.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[ErH-13Mas.tdb](https://orchid-project.org/data/databases/sgte-binary/ErH-13Mas.tdb): BCC_A2, type code %B, sha256 `f6f27fb09e27c3aa…`

~~~~text
41: PHASE BCC_A2 %B 2 1 3 !
42: CONST BCC_A2 : ER : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.004](https://doi.org/10.1016/j.calphad.2013.01.004) Aurore Mascaro, Caroline Toffolon-Masclet, Caroline Raepsaet, Jean-Marc Joubert, Experimental study and thermodynamic assessment of the erbium–hydrogen binary system, Calphad 41, 50-59 (2013).  
_assessment that models this phase; reports values for this phase_

## FCC_A1 (Er–H)

- Id: `phase:er-h:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1494.6 K, x(H) 0.44743–0.70158
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-h:fcc-a1)

Names (2): _corpus: _corpus:phase:er-h:fcc-a1  
_tdb: _tdb:ErH-13Mas.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[ErH-13Mas.tdb](https://orchid-project.org/data/databases/sgte-binary/ErH-13Mas.tdb): FCC_A1, type code %A, sha256 `f6f27fb09e27c3aa…`

~~~~text
36: PHASE FCC_A1 %A 3 1 1 2 !
37: CONST FCC_A1 : ER : H VA : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.004](https://doi.org/10.1016/j.calphad.2013.01.004) Aurore Mascaro, Caroline Toffolon-Masclet, Caroline Raepsaet, Jean-Marc Joubert, Experimental study and thermodynamic assessment of the erbium–hydrogen binary system, Calphad 41, 50-59 (2013).  
_assessment that models this phase_

## GAS (Er–H)

- Id: `phase:er-h:gas`; status `assigned`
- Structure: gas; type `st:gas`; gas; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–2500 K, x(H) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-h:gas)

Names (2): _corpus: _corpus:phase:er-h:gas  
_tdb: _tdb:ErH-13Mas.tdb:GAS  


### TDB models of GAS (1): PHASE and CONSTITUENT statements as written

[ErH-13Mas.tdb](https://orchid-project.org/data/databases/sgte-binary/ErH-13Mas.tdb): GAS, type code %, sha256 `f6f27fb09e27c3aa…`

~~~~text
50: PHASE GAS:G % 1 1 !
51: CONST GAS:G : H H2 : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.004](https://doi.org/10.1016/j.calphad.2013.01.004) Aurore Mascaro, Caroline Toffolon-Masclet, Caroline Raepsaet, Jean-Marc Joubert, Experimental study and thermodynamic assessment of the erbium–hydrogen binary system, Calphad 41, 50-59 (2013).  
_assessment that models this phase_

## HCP_A3 (Er–H)

- Id: `phase:er-h:hcp-a3`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:sgte_mmc2_row_disagrees_with_name; sgte_mmc2_row_disagrees_with_name:HCP_A3
- Candidate (dft_mp): Fm-3m (225) — on-hull MP ErH2 at x(H)=0.6667
- Candidate (dft_mp): P-3c1 (165) — on-hull MP ErH3 at x(H)=0.7500
- Candidate (dft_oqmd): Fm-3m (225) — on-hull OQMD Er1 H2 at x(H)=0.6667
- Candidate (dft_oqmd): P-3c1 (165) — on-hull OQMD Er1 H3 at x(H)=0.7500
- Candidate (name_token): Mg · A3 · hP2 · P6_3/mmc (194) — Strukturbericht/word 'A3' in the TDB name
- Candidate (sgte_mmc2): HoH3 · hP24 · P-3c1 (165) — Hallstedt 2025 mmc2 row for HCP_A3: DyH3, ErH3, GdH3, YH3
- Stability: stable in 1 of 1 calculated diagram(s): 300–2047.56 K, x(H) 0–0.75
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-h:hcp-a3)

Names (3): _corpus: _corpus:phase:er-h:hcp-a3  
_paper: _paper:10.1016/j.calphad.2013.01.004:γ-ErH3  
_tdb: _tdb:ErH-13Mas.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[ErH-13Mas.tdb](https://orchid-project.org/data/databases/sgte-binary/ErH-13Mas.tdb): HCP_A3, type code %A, sha256 `f6f27fb09e27c3aa…`

~~~~text
47: PHASE HCP_A3 %A 3 1 1 2 !
48: CONST HCP_A3 : ER : H VA : H VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.004](https://doi.org/10.1016/j.calphad.2013.01.004) Aurore Mascaro, Caroline Toffolon-Masclet, Caroline Raepsaet, Jean-Marc Joubert, Experimental study and thermodynamic assessment of the erbium–hydrogen binary system, Calphad 41, 50-59 (2013).  
_assessment that models this phase; reports values for this phase_

## LIQUID (Er–H)

- Id: `phase:er-h:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1795–2500 K, x(H) 0–0.00509
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:er-h:liquid)

Names (2): _corpus: _corpus:phase:er-h:liquid  
_tdb: _tdb:ErH-13Mas.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[ErH-13Mas.tdb](https://orchid-project.org/data/databases/sgte-binary/ErH-13Mas.tdb): LIQUID, type code %, sha256 `f6f27fb09e27c3aa…`

~~~~text
31: PHASE LIQUID:L % 1 1 !
32: CONST LIQUID:L : ER H : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.01.004](https://doi.org/10.1016/j.calphad.2013.01.004) Aurore Mascaro, Caroline Toffolon-Masclet, Caroline Raepsaet, Jean-Marc Joubert, Experimental study and thermodynamic assessment of the erbium–hydrogen binary system, Calphad 41, 50-59 (2013).  
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
