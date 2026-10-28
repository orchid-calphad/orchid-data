# Gd–Y phases

> Gd–Y system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/GD-Y.html · Markdown: https://data.orchid-project.org/phases/pages/GD-Y.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=GD-Y) · [full JSON](https://data.orchid-project.org/phases/systems/GD-Y.json) · [Gd–Y system page](https://data.orchid-project.org/systems/GD-Y.html) · [Markdown](https://data.orchid-project.org/phases/pages/GD-Y.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Gd–Y system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-gd-y-bcc-a2); _phase:gd-y:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 1508.16–1795.15 K, x(Y) 0–1 | 0 | 2 |
| [FCC_A1](#phase-gd-y-fcc-a1); _phase:gd-y:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-gd-y-hcp-a3); _phase:gd-y:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1751.15 K, x(Y) 0–1 | 0 | 2 |
| [LIQUID](#phase-gd-y-liquid); _phase:gd-y:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1586.12–2500 K, x(Y) 0–1 | 0 | 2 |

## BCC_A2 (Gd–Y)

- Id: `phase:gd-y:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1508.16–1795.15 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-y:bcc-a2)

Names (3): _corpus: _corpus:phase:gd-y:bcc-a2  
_tdb: _tdb:GdY-07Guo.tdb:BCC_A2, tdb:GdY-10Gro.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[GdY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-07Guo.tdb): BCC_A2, type code %B, sha256 `9c12c34c0087a00b…`

~~~~text
32: PHASE BCC_A2 %B 2 1 3 !
33: CONST BCC_A2 : GD Y : VA : !
~~~~

[GdY-10Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-10Gro.tdb): BCC_A2, type code %B, sha256 `6d17a3ebf8a18005…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GD Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.scriptamat.2010.01.035](https://doi.org/10.1016/j.scriptamat.2010.01.035) Joachim Gröbner, Rainer Schmid-Fetzer, Thermodynamic modeling of the Mg–Ce–Gd–Y system, Scripta Materialia 63, 674-679 (2010).  
_assessment that models this phase_

## FCC_A1 (Gd–Y)

- Id: `phase:gd-y:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-y:fcc-a1)

Names (3): _corpus: _corpus:phase:gd-y:fcc-a1  
_tdb: _tdb:GdY-07Guo.tdb:FCC_A1, tdb:GdY-10Gro.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[GdY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-07Guo.tdb): FCC_A1, type code %A, sha256 `9c12c34c0087a00b…`

~~~~text
27: PHASE FCC_A1 %A 2 1 1 !
28: CONST FCC_A1 : GD Y : VA : !
~~~~

[GdY-10Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-10Gro.tdb): FCC_A1, type code %A, sha256 `6d17a3ebf8a18005…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GD Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.scriptamat.2010.01.035](https://doi.org/10.1016/j.scriptamat.2010.01.035) Joachim Gröbner, Rainer Schmid-Fetzer, Thermodynamic modeling of the Mg–Ce–Gd–Y system, Scripta Materialia 63, 674-679 (2010).  
_assessment that models this phase_

## HCP_A3 (Gd–Y)

- Id: `phase:gd-y:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1751.15 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-y:hcp-a3)

Names (3): _corpus: _corpus:phase:gd-y:hcp-a3  
_tdb: _tdb:GdY-07Guo.tdb:HCP_A3, tdb:GdY-10Gro.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[GdY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-07Guo.tdb): HCP_A3, type code %A, sha256 `9c12c34c0087a00b…`

~~~~text
37: PHASE HCP_A3 %A 2 1 0.5 !
38: CONST HCP_A3 : GD Y : VA : !
~~~~

[GdY-10Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-10Gro.tdb): HCP_A3, type code %A, sha256 `6d17a3ebf8a18005…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GD Y : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.scriptamat.2010.01.035](https://doi.org/10.1016/j.scriptamat.2010.01.035) Joachim Gröbner, Rainer Schmid-Fetzer, Thermodynamic modeling of the Mg–Ce–Gd–Y system, Scripta Materialia 63, 674-679 (2010).  
_assessment that models this phase_

## LIQUID (Gd–Y)

- Id: `phase:gd-y:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1586.12–2500 K, x(Y) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:gd-y:liquid)

Names (3): _corpus: _corpus:phase:gd-y:liquid  
_tdb: _tdb:GdY-07Guo.tdb:LIQUID, tdb:GdY-10Gro.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[GdY-07Guo.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-07Guo.tdb): LIQUID, type code %, sha256 `9c12c34c0087a00b…`

~~~~text
22: PHASE LIQUID:L % 1 1 !
23: CONST LIQUID:L : GD Y : !
~~~~

[GdY-10Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/GdY-10Gro.tdb): LIQUID, type code %, sha256 `6d17a3ebf8a18005…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : GD Y : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.calphad.2006.10.004](https://doi.org/10.1016/j.calphad.2006.10.004) Cuiping Guo, Zhenmin Du, Changrong Li, A thermodynamic description of the Gd–Mg–Y system, Calphad 31, 75-88 (2007).  
_assessment that models this phase_
- [doi:10.1016/j.scriptamat.2010.01.035](https://doi.org/10.1016/j.scriptamat.2010.01.035) Joachim Gröbner, Rainer Schmid-Fetzer, Thermodynamic modeling of the Mg–Ce–Gd–Y system, Scripta Materialia 63, 674-679 (2010).  
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
