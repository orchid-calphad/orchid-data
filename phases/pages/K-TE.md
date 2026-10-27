# K–Te phases

> K–Te system: 9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 7 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/K-TE.html · Markdown: https://data.orchid-project.org/phases/pages/K-TE.md

9 phases (tier A 5, tier C 2, liquid 1, needs_review 1); 7 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=K-TE) · [full JSON](https://data.orchid-project.org/phases/systems/K-TE.json) · [K–Te system page](https://data.orchid-project.org/systems/K-TE.html) · [Markdown](https://data.orchid-project.org/phases/pages/K-TE.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the K–Te system (9)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [HEXAGONAL_A8](#phase-k-te-a8-hexagonal); _phase:k-te:a8-hexagonal_ | gamma-Se · A8 · hP3 · P3_121 (152) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1 | 0 | 1 |
| [BCC_A2](#phase-k-te-bcc-a2); _phase:k-te:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(Te) 0–0 | 0 | 1 |
| [FCC_A1](#phase-k-te-fcc-a1); _phase:k-te:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-k-te-hcp-a3); _phase:k-te:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [K2TE_C1](#phase-k-te-k2te-c1); _phase:k-te:k2te-c1_ | CaF2 · C1 · cF12 · Fm-3m (225) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1199.75 K, x(Te) 0.33333–0.33333 | 0 | 1 |
| [K2TE3](#phase-k-te-k2te3); _phase:k-te:k2te3_ | K2Te3 · oP20 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–696.91 K, x(Te) 0.6–0.6 | 4 | 1 |
| [K5TE3](#phase-k-te-k5te3); _phase:k-te:k5te3_ | K5Te3 · tI32 · I4/m (87) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–914.75 K, x(Te) 0.375–0.375 | 2 | 1 |
| [KTE](#phase-k-te-kte); _phase:k-te:kte_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–684.65 K, x(Te) 0.5–0.5 | 4 | 1 |
| [LIQUID](#phase-k-te-liquid); _phase:k-te:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 336.53–2500 K, x(Te) 0–1 | 0 | 1 |

## HEXAGONAL_A8 (K–Te)

- Id: `phase:k-te:a8-hexagonal`; status `assigned`
- Structure: gamma-Se · A8 · hP3 · P3_121 (152); type `st:a8-gamma-se-hp3`; tier A: standard phase name; confidence high
- Stoichiometry: Te 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–722.66 K, x(Te) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:a8-hexagonal)

Names (2): _corpus: _corpus:phase:k-te:a8-hexagonal  
_tdb: _tdb:KTe-14Che.tdb:HEXAGONAL_A8  


### TDB models of HEXAGONAL_A8 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): HEXAGONAL_A8, type code %, sha256 `1493e709e213dad3…`

~~~~text
50: PHASE HEXAGONAL_A8 % 1 1 !
51: CONST HEXAGONAL_A8 : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## BCC_A2 (K–Te)

- Id: `phase:k-te:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stoichiometry: K 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–336.53 K, x(Te) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:bcc-a2)

Names (2): _corpus: _corpus:phase:k-te:bcc-a2  
_tdb: _tdb:KTe-14Che.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): BCC_A2, type code %B, sha256 `1493e709e213dad3…`

~~~~text
40: PHASE BCC_A2 %B 2 1 3 !
41: CONST BCC_A2 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## FCC_A1 (K–Te)

- Id: `phase:k-te:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: K 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:fcc-a1)

Names (2): _corpus: _corpus:phase:k-te:fcc-a1  
_tdb: _tdb:KTe-14Che.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): FCC_A1, type code %A, sha256 `1493e709e213dad3…`

~~~~text
35: PHASE FCC_A1 %A 2 1 1 !
36: CONST FCC_A1 : K : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## HCP_A3 (K–Te)

- Id: `phase:k-te:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: K 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:hcp-a3)

Names (2): _corpus: _corpus:phase:k-te:hcp-a3  
_tdb: _tdb:KTe-14Che.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): HCP_A3, type code %A, sha256 `1493e709e213dad3…`

~~~~text
45: PHASE HCP_A3 %A 2 1 0.5 !
46: CONST HCP_A3 : K : VA: !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## K2TE_C1 (K–Te)

- Id: `phase:k-te:k2te-c1`; status `assigned`
- Structure: CaF2 · C1 · cF12 · Fm-3m (225); type `st:c1-caf2-cf12`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaacpf and oqmd-11320, space group 225
- Stoichiometry: K 0.6667, Te 0.3333
- Stability: stable in 1 of 1 calculated diagram(s): 300–1199.75 K, x(Te) 0.33333–0.33333
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:k2te-c1)

Names (4): _corpus: _corpus:phase:k-te:k2te-c1  
_mp: _mp:mp-aaaaacpf  
_oqmd: _oqmd:oqmd-11320  
_tdb: _tdb:KTe-14Che.tdb:K2TE_C1  


### TDB models of K2TE_C1 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): K2TE_C1, type code %, sha256 `1493e709e213dad3…`

~~~~text
55: PHASE K2TE_C1 % 2 2 1 !
56: CONST K2TE_C1 : K : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase_

## K2TE3 (K–Te)

- Id: `phase:k-te:k2te3`; status `assigned`
- Structure: K2Te3 · oP20 · Pnma (62); type `st:k2te3-op20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (dft_space_group_62_matches_7_structure_types, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: K 0.4000, Te 0.6000
- Stability: stable in 1 of 1 calculated diagram(s): 300–696.91 K, x(Te) 0.6–0.6
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:k2te3)

Names (3): _corpus: _corpus:phase:k-te:k2te3  
_paper: _paper:10.1016/j.jallcom.2013.11.094:K2Te3  
_tdb: _tdb:KTe-14Che.tdb:K2TE3  


### TDB models of K2TE3 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): K2TE3, type code %, sha256 `1493e709e213dad3…`

~~~~text
70: PHASE K2TE3 % 2 2 3 !
71: CONST K2TE3 : K : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_

## K5TE3 (K–Te)

- Id: `phase:k-te:k5te3`; status `assigned`
- Structure: K5Te3 · tI32 · I4/m (87); type `st:k5te3-ti32`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: K 0.6250, Te 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–914.75 K, x(Te) 0.375–0.375
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:k5te3)

Names (3): _corpus: _corpus:phase:k-te:k5te3  
_paper: _paper:10.1016/j.jallcom.2013.11.094:K5Te3  
_tdb: _tdb:KTe-14Che.tdb:K5TE3  


### TDB models of K5TE3 (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): K5TE3, type code %, sha256 `1493e709e213dad3…`

~~~~text
60: PHASE K5TE3 % 2 5 3 !
61: CONST K5TE3 : K : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_

## KTE (K–Te)

- Id: `phase:k-te:kte`; status `needs_review`
- No structure assigned. Why: mp_oqmd_space_groups_differ; no_structure_token; sgte_mmc2_rows_disagree
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP KTe at x(TE)=0.5000
- Candidate (dft_oqmd): P-62m (189) — on-hull OQMD K1 Te1 at x(TE)=0.5000
- Candidate (sgte_mmc2): Li2O2 · hP8 · P6_3/mmc (194) — Hallstedt 2025 mmc2 row for KTE: KTe (high T)
- Candidate (sgte_mmc2): Na2O2 · hP12 · P-62m (189) — Hallstedt 2025 mmc2 row for KTE: KTe (low T)
- Candidate (tdb_comment): Na2O2 · hP12 · P-62m — KTe-14Che.tdb: 'Prototype Na2O2 (hP12, P-62m), low T; Li2O2 (hP8, P6_3/mmc), high T'
- Stoichiometry: K 0.5000, Te 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–684.65 K, x(Te) 0.5–0.5
- Literature: 4 values (4 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:kte)

Names (3): _corpus: _corpus:phase:k-te:kte  
_paper: _paper:10.1016/j.jallcom.2013.11.094:KTe  
_tdb: _tdb:KTe-14Che.tdb:KTE  


### TDB models of KTE (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): KTE, type code %, sha256 `1493e709e213dad3…`

~~~~text
65: PHASE KTE % 2 1 1 !
66: CONST KTE : K : TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
_assessment that models this phase; reports values for this phase_

## LIQUID (K–Te)

- Id: `phase:k-te:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 336.53–2500 K, x(Te) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:k-te:liquid)

Names (2): _corpus: _corpus:phase:k-te:liquid  
_tdb: _tdb:KTe-14Che.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[KTe-14Che.tdb](https://orchid-project.org/data/databases/sgte-binary/KTe-14Che.tdb): LIQUID, type code %, sha256 `1493e709e213dad3…`

~~~~text
30: PHASE LIQUID:L % 1 1 !
31: CONST LIQUID:L : K K2TE K2TE3 TE : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014).  
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
