# B–Co phases

> B–Co system: 8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/B-CO.html · Markdown: https://data.orchid-project.org/phases/pages/B-CO.md

8 phases (tier A 4, tier C 2, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=B-CO) · [full JSON](https://data.orchid-project.org/phases/systems/B-CO.json) · [B–Co system page](https://data.orchid-project.org/systems/B-CO.html) · [Markdown](https://data.orchid-project.org/phases/pages/B-CO.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the B–Co system (8)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BETA_RHOMBO_B](#phase-b-co-b-beta-rhombo); _phase:b-co:b-beta-rhombo_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–2353.52 K, x(B) 1–1 | 0 | 1 |
| [MB_B27](#phase-b-co-b27-mb); _phase:b-co:b27-mb_ | FeB · B27 · oP8 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1735.07 K, x(B) 0.5–0.5 | 0 | 1 |
| [BCC_A2](#phase-b-co-bcc-a2); _phase:b-co:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [M2B_C16](#phase-b-co-c16-m2b); _phase:b-co:c16-m2b_ | Al2Cu · C16 · tI12 · I4/mcm (140) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1548.65 K, x(B) 0.33333–0.33333 | 0 | 1 |
| [CO3B_D011](#phase-b-co-co3b-d011); _phase:b-co:co3b-d011_ | Fe3C · D0_11 · oP16 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1115.91–1431.15 K, x(B) 0.25–0.25 | 0 | 1 |
| [FCC_A1](#phase-b-co-fcc-a1); _phase:b-co:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 694.99–2741.34 K, x(B) 0–0.00222 | 0 | 1 |
| [HCP_A3](#phase-b-co-hcp-a3); _phase:b-co:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1759.99 K, x(B) 0–0 | 0 | 1 |
| [LIQUID](#phase-b-co-liquid); _phase:b-co:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1406.34–4000 K, x(B) 0–1 | 0 | 1 |

## BETA_RHOMBO_B (B–Co)

- Id: `phase:b-co:b-beta-rhombo`; status `needs_review`
- No structure assigned. Why: name_has_descriptive_tokens:RHOMBO; no_structure_token
- Candidate (sgte_mmc2): beta-B · hR105 · R-3m (166) — Hallstedt 2025 mmc2 row for BETA_RHOMBO_B: beta-B
- Candidate (tdb_comment): beta-B · hR105 · R-3m — CoB-02Du-LB.tdb: 'Prototype beta-B (hR105, R-3m)'
- Stoichiometry: B 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–2353.52 K, x(B) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:b-beta-rhombo)

Names (2): _corpus: _corpus:phase:b-co:b-beta-rhombo  
_tdb: _tdb:CoB-02Du-LB.tdb:BETA_RHOMBO_B  


### TDB models of BETA_RHOMBO_B (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): BETA_RHOMBO_B, type code %, sha256 `936043c413bb18ac…`

~~~~text
49: PHASE BETA_RHOMBO_B % 1 1 !
50: CONST BETA_RHOMBO_B : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## MB_B27 (B–Co)

- Id: `phase:b-co:b27-mb`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (name_has_descriptive_tokens:MB, no_structure_token, structure_token_is_also_a_formula); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.5000, Co 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1735.07 K, x(B) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:b27-mb)

Names (2): _corpus: _corpus:phase:b-co:b27-mb  
_tdb: _tdb:CoB-02Du-LB.tdb:MB_B27  


### TDB models of MB_B27 (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): MB_B27, type code %, sha256 `936043c413bb18ac…`

~~~~text
64: PHASE MB_B27 % 2 1 1 !
65: CONST MB_B27 : CO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## BCC_A2 (B–Co)

- Id: `phase:b-co:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:bcc-a2)

Names (2): _corpus: _corpus:phase:b-co:bcc-a2  
_tdb: _tdb:CoB-02Du-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): BCC_A2, type code %B, sha256 `936043c413bb18ac…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : B CO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## M2B_C16 (B–Co)

- Id: `phase:b-co:c16-m2b`; status `assigned`
- Structure: Al2Cu · C16 · tI12 · I4/mcm (140); type `st:c16-al2cu-ti12`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (unrecognised_name_tokens:M2B); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: B 0.3333, Co 0.6667
- Stability: stable in 1 of 1 calculated diagram(s): 300–1548.65 K, x(B) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:c16-m2b)

Names (2): _corpus: _corpus:phase:b-co:c16-m2b  
_tdb: _tdb:CoB-02Du-LB.tdb:M2B_C16  


### TDB models of M2B_C16 (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): M2B_C16, type code %, sha256 `936043c413bb18ac…`

~~~~text
59: PHASE M2B_C16 % 2 2 1 !
60: CONST M2B_C16 : CO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## CO3B_D011 (B–Co)

- Id: `phase:b-co:co3b-d011`; status `assigned`
- Structure: Fe3C · D0_11 · oP16 · Pnma (62); type `st:d0-11-fe3c-op16`; tier A: standard phase name; confidence high
- Stoichiometry: B 0.2500, Co 0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 1115.91–1431.15 K, x(B) 0.25–0.25
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:co3b-d011)

Names (2): _corpus: _corpus:phase:b-co:co3b-d011  
_tdb: _tdb:CoB-02Du-LB.tdb:CO3B_D011  


### TDB models of CO3B_D011 (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): CO3B_D011, type code %, sha256 `936043c413bb18ac…`

~~~~text
54: PHASE CO3B_D011 % 2 3 1 !
55: CONST CO3B_D011 : CO : B : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## FCC_A1 (B–Co)

- Id: `phase:b-co:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 694.99–2741.34 K, x(B) 0–0.00222
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:fcc-a1)

Names (2): _corpus: _corpus:phase:b-co:fcc-a1  
_tdb: _tdb:CoB-02Du-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): FCC_A1, type code %A, sha256 `936043c413bb18ac…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : B CO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## HCP_A3 (B–Co)

- Id: `phase:b-co:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–1759.99 K, x(B) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:hcp-a3)

Names (2): _corpus: _corpus:phase:b-co:hcp-a3  
_tdb: _tdb:CoB-02Du-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): HCP_A3, type code %A, sha256 `936043c413bb18ac…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : B CO% : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
_assessment that models this phase_

## LIQUID (B–Co)

- Id: `phase:b-co:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1406.34–4000 K, x(B) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:b-co:liquid)

Names (2): _corpus: _corpus:phase:b-co:liquid  
_tdb: _tdb:CoB-02Du-LB.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CoB-02Du-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CoB-02Du-LB.tdb): LIQUID, type code %, sha256 `936043c413bb18ac…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : B CO : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.3139/146.021157](https://doi.org/10.3139/146.021157) Y. Du, J.C. Schuster, Y.A. Chang, Z. Jin, B. Huang, Z. Metallkd., 93 ,1157-63(2002).  
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
