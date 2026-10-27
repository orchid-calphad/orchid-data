# Cd–Zn phases

> Cd–Zn system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-ZN.html · Markdown: https://data.orchid-project.org/phases/pages/CD-ZN.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-ZN) · [full JSON](https://data.orchid-project.org/phases/systems/CD-ZN.json) · [Cd–Zn system page](https://data.orchid-project.org/systems/CD-ZN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-ZN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Zn system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-zn-bcc-a2); _phase:cd-zn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-cd-zn-fcc-a1); _phase:cd-zn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-cd-zn-hcp-a3); _phase:cd-zn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–692.68 K, x(Zn) 0–1 | 0 | 2 |
| [LIQUID](#phase-cd-zn-liquid); _phase:cd-zn:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 538.16–2500 K, x(Zn) 0–1 | 1 | 2 |

## BCC_A2 (Cd–Zn)

- Id: `phase:cd-zn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-zn:bcc-a2)

Names (3): _corpus: _corpus:phase:cd-zn:bcc-a2  
_tdb: _tdb:CdZn-93Zab.tdb:BCC_A2, tdb:CdZn-97Zab-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[CdZn-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-93Zab.tdb): BCC_A2, type code %B, sha256 `dfa8770557cf58af…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CD ZN : VA : !
~~~~

[CdZn-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-97Zab-LB.tdb): BCC_A2, type code %B, sha256 `be5c0e38c1191905…`

~~~~text
37: PHASE BCC_A2 %B 2 1 3 !
38: CONST BCC_A2 : CD ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_

## FCC_A1 (Cd–Zn)

- Id: `phase:cd-zn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-zn:fcc-a1)

Names (3): _corpus: _corpus:phase:cd-zn:fcc-a1  
_tdb: _tdb:CdZn-93Zab.tdb:FCC_A1, tdb:CdZn-97Zab-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[CdZn-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-93Zab.tdb): FCC_A1, type code %A, sha256 `dfa8770557cf58af…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CD ZN : VA : !
~~~~

[CdZn-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-97Zab-LB.tdb): FCC_A1, type code %A, sha256 `be5c0e38c1191905…`

~~~~text
32: PHASE FCC_A1 %A 2 1 1 !
33: CONST FCC_A1 : CD ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_

## HCP_A3 (Cd–Zn)

- Id: `phase:cd-zn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–692.68 K, x(Zn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-zn:hcp-a3)

Names (3): _corpus: _corpus:phase:cd-zn:hcp-a3  
_tdb: _tdb:CdZn-93Zab.tdb:HCP_A3, tdb:CdZn-97Zab-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CdZn-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-93Zab.tdb): HCP_A3, type code %A, sha256 `dfa8770557cf58af…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CD ZN : VA : !
~~~~

[CdZn-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-97Zab-LB.tdb): HCP_A3, type code %A, sha256 `be5c0e38c1191905…`

~~~~text
42: PHASE HCP_A3 %A 2 1 0.5 !
43: CONST HCP_A3 : CD ZN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_

## LIQUID (Cd–Zn)

- Id: `phase:cd-zn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 538.16–2500 K, x(Zn) 0–1
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-zn:liquid)

Names (4): _corpus: _corpus:phase:cd-zn:liquid  
_paper: _paper:10.1016/j.calphad.2009.08.006:L  
_tdb: _tdb:CdZn-93Zab.tdb:LIQUID, tdb:CdZn-97Zab-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[CdZn-93Zab.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-93Zab.tdb): LIQUID, type code %, sha256 `dfa8770557cf58af…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CD ZN : !
~~~~

[CdZn-97Zab-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CdZn-97Zab-LB.tdb): LIQUID, type code %, sha256 `be5c0e38c1191905…`

~~~~text
27: PHASE LIQUID:L % 1 1 !
28: CONST LIQUID:L : CD ZN : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/S0364-5916(97)00036-9](https://doi.org/10.1016/S0364-5916%2897%2900036-9) L.A. Zabdyr, Calphad, 21, 349-58(1997).  
_assessment that models this phase_
- [doi:10.1016/j.calphad.2009.08.006](https://doi.org/10.1016/j.calphad.2009.08.006) Ya Liu, Jean-Claude Tedenac, Thermodynamic modeling of the Cd–Sb–Zn ternary system, Calphad 33, 684-694 (2009).  
_reports values for this phase_
- [doi:10.1016/j.jallcom.2006.04.051](https://doi.org/10.1016/j.jallcom.2006.04.051) Fouzia Adjadj, El-djemai Belbacha, Malek Bouharkat, Differential calorimetric analysis of the binary system Sb–Zn, Journal of Alloys and Compounds 430, 85-91 (2007).  
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
