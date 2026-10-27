# Cd–In phases

> Cd–In system: 6 phases (tier A 4, liquid 1, needs_review 1); 5 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-IN.html · Markdown: https://data.orchid-project.org/phases/pages/CD-IN.md

6 phases (tier A 4, liquid 1, needs_review 1); 5 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-IN) · [full JSON](https://data.orchid-project.org/phases/systems/CD-IN.json) · [Cd–In system page](https://data.orchid-project.org/systems/CD-IN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-IN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–In system (6)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [TETRAGONAL_A6](#phase-cd-in-a6-tetragonal); _phase:cd-in:a6-tetragonal_ | In · A6 · tI2 · I4/mmm (139) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–429.75 K, x(In) 0.93611–1 | 0 | 2 |
| [BCC_A2](#phase-cd-in-bcc-a2); _phase:cd-in:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [CD3IN](#phase-cd-in-cd3in); _phase:cd-in:cd3in_ |  | needs_review | stable in 2 of 2 calculated diagram(s): 398.06–468.5 K, x(In) 0.25–0.25 | 0 | 2 |
| [FCC_A1](#phase-cd-in-fcc-a1); _phase:cd-in:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–420.3 K, x(In) 0.79957–0.96269 | 0 | 2 |
| [HCP_A3](#phase-cd-in-hcp-a3); _phase:cd-in:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–594.22 K, x(In) 0–0.01774 | 0 | 2 |
| [LIQUID](#phase-cd-in-liquid); _phase:cd-in:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 399.26–2500 K, x(In) 0–1 | 0 | 2 |

## TETRAGONAL_A6 (Cd–In)

- Id: `phase:cd-in:a6-tetragonal`; status `assigned`
- Structure: In · A6 · tI2 · I4/mmm (139); type `st:a6-in-ti2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–429.75 K, x(In) 0.93611–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-in:a6-tetragonal)

Names (3): _corpus: _corpus:phase:cd-in:a6-tetragonal  
_tdb: _tdb:CdIn-19Fis.tdb:TETRAGONAL_A6, tdb:CdIn-93Zak.tdb:TETRAGONAL_A6  


### TDB models of TETRAGONAL_A6 (2): PHASE and CONSTITUENT statements as written

[CdIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-19Fis.tdb): TETRAGONAL_A6, type code %, sha256 `1f440c073b0db984…`

~~~~text
43: PHASE TETRAGONAL_A6 % 1 1 !
44: CONST TETRAGONAL_A6 : CD IN% : !
~~~~

[CdIn-93Zak.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-93Zak.tdb): TETRAGONAL_A6, type code %, sha256 `bf71d09111ca9904…`

~~~~text
48: PHASE TETRAGONAL_A6 % 1 1 !
49: CONST TETRAGONAL_A6 : CD IN% : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667807](https://doi.org/10.1007/BF02667807) W. Zakulski, Z. Moser, K. Rzyman, H.L. Lukas, S.G. Fries, M. Sukiennik, R. Kaczmarczyk, R. Castanet, J. Phase Equilib., 14, 184-96(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## BCC_A2 (Cd–In)

- Id: `phase:cd-in:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-in:bcc-a2)

Names (3): _corpus: _corpus:phase:cd-in:bcc-a2  
_tdb: _tdb:CdIn-19Fis.tdb:BCC_A2, tdb:CdIn-93Zak.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CdIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-19Fis.tdb): BCC_A2, type code %B, sha256 `1f440c073b0db984…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CD IN : VA : !
~~~~

[CdIn-93Zak.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-93Zak.tdb): BCC_A2, type code %B, sha256 `bf71d09111ca9904…`

~~~~text
38: PHASE BCC_A2 %B 2 1 3 !
39: CONST BCC_A2 : CD IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667807](https://doi.org/10.1007/BF02667807) W. Zakulski, Z. Moser, K. Rzyman, H.L. Lukas, S.G. Fries, M. Sukiennik, R. Kaczmarczyk, R. Castanet, J. Phase Equilib., 14, 184-96(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## CD3IN (Cd–In)

- Id: `phase:cd-in:cd3in`; status `needs_review`
- No structure assigned. Why: no_on_hull_entry_in_both; no_structure_token; sgte_mmc2_row_incomplete
- Candidate (sgte_mmc2): (Cd3In) — Hallstedt 2025 mmc2 row for CD3IN: Cd3In
- Stoichiometry: Cd 0.7500, In 0.2500
- Stability: stable in 2 of 2 calculated diagram(s): 398.06–468.5 K, x(In) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-in:cd3in)

Names (3): _corpus: _corpus:phase:cd-in:cd3in  
_tdb: _tdb:CdIn-19Fis.tdb:CD3IN, tdb:CdIn-93Zak.tdb:CD3IN  


### TDB models of CD3IN (2): PHASE and CONSTITUENT statements as written

[CdIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-19Fis.tdb): CD3IN, type code %, sha256 `1f440c073b0db984…`

~~~~text
48: PHASE CD3IN % 2 3 1 !
49: CONST CD3IN : CD : IN : !
~~~~

[CdIn-93Zak.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-93Zak.tdb): CD3IN, type code %, sha256 `bf71d09111ca9904…`

~~~~text
53: PHASE CD3IN % 2 3 1 !
54: CONST CD3IN : CD : IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667807](https://doi.org/10.1007/BF02667807) W. Zakulski, Z. Moser, K. Rzyman, H.L. Lukas, S.G. Fries, M. Sukiennik, R. Kaczmarczyk, R. Castanet, J. Phase Equilib., 14, 184-96(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## FCC_A1 (Cd–In)

- Id: `phase:cd-in:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–420.3 K, x(In) 0.79957–0.96269
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-in:fcc-a1)

Names (3): _corpus: _corpus:phase:cd-in:fcc-a1  
_tdb: _tdb:CdIn-19Fis.tdb:FCC_A1, tdb:CdIn-93Zak.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CdIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-19Fis.tdb): FCC_A1, type code %A, sha256 `1f440c073b0db984…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CD IN : VA : !
~~~~

[CdIn-93Zak.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-93Zak.tdb): FCC_A1, type code %A, sha256 `bf71d09111ca9904…`

~~~~text
33: PHASE FCC_A1 %A 2 1 1 !
34: CONST FCC_A1 : CD IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667807](https://doi.org/10.1007/BF02667807) W. Zakulski, Z. Moser, K. Rzyman, H.L. Lukas, S.G. Fries, M. Sukiennik, R. Kaczmarczyk, R. Castanet, J. Phase Equilib., 14, 184-96(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## HCP_A3 (Cd–In)

- Id: `phase:cd-in:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–594.22 K, x(In) 0–0.01774
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-in:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-in:hcp-a3  
_tdb: _tdb:CdIn-19Fis.tdb:HCP_A3, tdb:CdIn-93Zak.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CdIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-19Fis.tdb): HCP_A3, type code %A, sha256 `1f440c073b0db984…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CD% IN : VA : !
~~~~

[CdIn-93Zak.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-93Zak.tdb): HCP_A3, type code %A, sha256 `bf71d09111ca9904…`

~~~~text
43: PHASE HCP_A3 %A 2 1 0.5 !
44: CONST HCP_A3 : CD% IN : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667807](https://doi.org/10.1007/BF02667807) W. Zakulski, Z. Moser, K. Rzyman, H.L. Lukas, S.G. Fries, M. Sukiennik, R. Kaczmarczyk, R. Castanet, J. Phase Equilib., 14, 184-96(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## LIQUID (Cd–In)

- Id: `phase:cd-in:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 399.26–2500 K, x(In) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-in:liquid)

Names (3): _corpus: _corpus:phase:cd-in:liquid  
_tdb: _tdb:CdIn-19Fis.tdb:LIQUID, tdb:CdIn-93Zak.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CdIn-19Fis.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-19Fis.tdb): LIQUID, type code %, sha256 `1f440c073b0db984…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CD IN : !
~~~~

[CdIn-93Zak.tdb](https://orchid-project.org/data/databases/sgte-binary/CdIn-93Zak.tdb): LIQUID, type code %, sha256 `bf71d09111ca9904…`

~~~~text
28: PHASE LIQUID:L % 1 1 !
29: CONST LIQUID:L : CD IN : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/BF02667807](https://doi.org/10.1007/BF02667807) W. Zakulski, Z. Moser, K. Rzyman, H.L. Lukas, S.G. Fries, M. Sukiennik, R. Kaczmarczyk, R. Castanet, J. Phase Equilib., 14, 184-96(1993).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2019.01.001](https://doi.org/10.1016/j.calphad.2019.01.001) E. Fischer, K. Gajavalli, G. Mikaelian, P. Benigni, J. Rogez, A. Decreton et al., Experimental study and thermodynamic modelling of the Ag-Cd-In system, Calphad 64, 292-305 (2019).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read by language-model readers constrained to quote their source and checked automatically, and the release was then audited on the printed pages by adversarial audits, an independent second review of fit-facing records and a preliminary human review of a frozen sample. Flags such as accepted and ESPEI-ready record screening results, not certification; known issues are listed in the release notes.

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
