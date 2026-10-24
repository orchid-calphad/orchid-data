# B–Ga phases

> B–Ga system: 7 phases (tier A 4, liquid 1, needs_review 2); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-GA.html · Markdown: https://data.orchid-project.org/phases/pages/B-GA.md

7 phases (tier A 4, liquid 1, needs_review 2); 4 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-GA) · [full JSON](https://data.orchid-project.org/phases/systems/B-GA.json) · [Markdown](https://data.orchid-project.org/phases/pages/B-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Ga system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-b-ga-a11-orthorhombic); _phase:b-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(B) 0–0 | 0 | 1 |
| [ALPHA_RHOMBO_B](#phase-b-ga-b-alpha-rhombo); _phase:b-ga:b-alpha-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1 | 0 | 1 |
| [BETA_RHOMBO_B](#phase-b-ga-b-beta-rhombo); _phase:b-ga:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 1388–2348 K, x(B) 1–1 | 0 | 1 |
| [BCC_A2](#phase-b-ga-bcc-a2); _phase:b-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-b-ga-fcc-a1); _phase:b-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-b-ga-hcp-a3); _phase:b-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-b-ga-liquid); _phase:b-ga:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 302.91–4000 K, x(B) 0–1 | 0 | 1 |

## ORTHORHOMBIC_A11 (B–Ga)

- Id: `phase:b-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–302.91 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:a11-orthorhombic)

Names (2): _corpus: _corpus:phase:b-ga:a11-orthorhombic  
_tdb: _tdb:GaB-13Li.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): ORTHORHOMBIC_A11, type code %, sha256 `60b4bb3e27dc1490…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## ALPHA_RHOMBO_B (B–Ga)

- Id: `phase:b-ga:b-alpha-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): alpha-B · hR12 · R-3m (166) — Hallstedt 2025 mmc2 row for ALPHA_RHOMBO_B: Si_nB
- Candidate (tdb_comment): alpha-B · hR12 · R-3m — GaB-13Li.tdb: 'Prototype alpha-B (hR12, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1388 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:b-alpha-rhombo)

Names (2): _corpus: _corpus:phase:b-ga:b-alpha-rhombo  
_tdb: _tdb:GaB-13Li.tdb:ALPHA_RHOMBO_B  


### TDB models of ALPHA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): ALPHA_RHOMBO_B, type code %, sha256 `60b4bb3e27dc1490…`

~~~~text
48: PHASE ALPHA_RHOMBO_B % 1 1 !
49: CONST ALPHA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BETA_RHOMBO_B (B–Ga)

- Id: `phase:b-ga:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — GaB-13Li.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 1388–2348 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-ga:b-beta-rhombo  
_tdb: _tdb:GaB-13Li.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): BETA_RHOMBO_B, type code %, sha256 `60b4bb3e27dc1490…`

~~~~text
53: PHASE BETA_RHOMBO_B % 1 1 !
54: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## BCC_A2 (B–Ga)

- Id: `phase:b-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:bcc-a2)

Names (2): _corpus: _corpus:phase:b-ga:bcc-a2  
_tdb: _tdb:GaB-13Li.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): BCC_A2, type code %B, sha256 `60b4bb3e27dc1490…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : GA : B VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## FCC_A1 (B–Ga)

- Id: `phase:b-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:fcc-a1)

Names (2): _corpus: _corpus:phase:b-ga:fcc-a1  
_tdb: _tdb:GaB-13Li.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): FCC_A1, type code %A, sha256 `60b4bb3e27dc1490…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : GA : B VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## HCP_A3 (B–Ga)

- Id: `phase:b-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:hcp-a3)

Names (2): _corpus: _corpus:phase:b-ga:hcp-a3  
_tdb: _tdb:GaB-13Li.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): HCP_A3, type code %A, sha256 `60b4bb3e27dc1490…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : GA : B VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
_assessment that models this phase_

## LIQUID (B–Ga)

- Id: `phase:b-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 302.91–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-ga:liquid)

Names (2): _corpus: _corpus:phase:b-ga:liquid  
_tdb: _tdb:GaB-13Li.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[GaB-13Li.tdb](https://orchid-project.org/data/databases/sgte-binary/GaB-13Li.tdb): LIQUID, type code %, sha256 `60b4bb3e27dc1490…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : B GA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2013.09.002](https://doi.org/10.1016/j.calphad.2013.09.002) Xi Li, Kaiming Cheng, Xiaoming Yuan, Dongdong Zhao, Jinghua Xin, Weiwei Wang et al., Thermodynamic assessment of the Ga–X (X=B, Ca, Sr, Ba) systems supported by first-principles calculations, Calphad 43, 52-60 (2013).  
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
