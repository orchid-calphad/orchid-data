# Sc–W phases

> Sc–W system: 4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/SC-W.html · Markdown: https://data.orchid-project.org/phases/pages/SC-W.md

4 phases (tier A 3, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=SC-W) · [full JSON](https://data.orchid-project.org/phases/systems/SC-W.json) · [Sc–W system page](https://data.orchid-project.org/systems/SC-W.html) · [Markdown](https://data.orchid-project.org/phases/pages/SC-W.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Sc–W system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-sc-w-bcc-a2); _phase:sc-w:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–3999.88 K, x(W) 0–1 | 0 | 2 |
| [FCC_A1](#phase-sc-w-fcc-a1); _phase:sc-w:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [HCP_A3](#phase-sc-w-hcp-a3); _phase:sc-w:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1615.99 K, x(W) 0–0.00093 | 0 | 2 |
| [LIQUID](#phase-sc-w-liquid); _phase:sc-w:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1783.59–4000 K, x(W) 0–1 | 0 | 2 |

## BCC_A2 (Sc–W)

- Id: `phase:sc-w:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–3999.88 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-w:bcc-a2)

Names (3): _corpus: _corpus:phase:sc-w:bcc-a2  
_tdb: _tdb:ScW-00Kri.tdb:BCC_A2, tdb:ScW-15Wan.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[ScW-00Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-00Kri.tdb): BCC_A2, type code %B, sha256 `e3aea447947d7bfa…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : SC W : VA : !
~~~~

[ScW-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-15Wan.tdb): BCC_A2, type code %B, sha256 `478e3612800b19c0…`

~~~~text
31: PHASE BCC_A2 %B 2 1 3 !
32: CONST BCC_A2 : SC W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910311](https://doi.org/10.1515/ijmr-2000-910311) N. Krishnamurthy, T. Kundu, A. Awasthi, S.P. Garg, Z. Metallkd., 91, 234-40(2000).  
_assessment that models this phase_

## FCC_A1 (Sc–W)

- Id: `phase:sc-w:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-w:fcc-a1)

Names (3): _corpus: _corpus:phase:sc-w:fcc-a1  
_tdb: _tdb:ScW-00Kri.tdb:FCC_A1, tdb:ScW-15Wan.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[ScW-00Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-00Kri.tdb): FCC_A1, type code %A, sha256 `e3aea447947d7bfa…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : SC W : VA : !
~~~~

[ScW-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-15Wan.tdb): FCC_A1, type code %A, sha256 `478e3612800b19c0…`

~~~~text
26: PHASE FCC_A1 %A 2 1 1 !
27: CONST FCC_A1 : SC W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910311](https://doi.org/10.1515/ijmr-2000-910311) N. Krishnamurthy, T. Kundu, A. Awasthi, S.P. Garg, Z. Metallkd., 91, 234-40(2000).  
_assessment that models this phase_

## HCP_A3 (Sc–W)

- Id: `phase:sc-w:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1615.99 K, x(W) 0–0.00093
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-w:hcp-a3)

Names (3): _corpus: _corpus:phase:sc-w:hcp-a3  
_tdb: _tdb:ScW-00Kri.tdb:HCP_A3, tdb:ScW-15Wan.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[ScW-00Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-00Kri.tdb): HCP_A3, type code %, sha256 `e3aea447947d7bfa…`

~~~~text
38: PHASE HCP_A3 % 2 1 0.5 !
39: CONST HCP_A3 : SC% W : VA : !
~~~~

[ScW-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-15Wan.tdb): HCP_A3, type code %, sha256 `478e3612800b19c0…`

~~~~text
36: PHASE HCP_A3 % 2 1 0.5 !
37: CONST HCP_A3 : SC% W : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910311](https://doi.org/10.1515/ijmr-2000-910311) N. Krishnamurthy, T. Kundu, A. Awasthi, S.P. Garg, Z. Metallkd., 91, 234-40(2000).  
_assessment that models this phase_

## LIQUID (Sc–W)

- Id: `phase:sc-w:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1783.59–4000 K, x(W) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:sc-w:liquid)

Names (3): _corpus: _corpus:phase:sc-w:liquid  
_tdb: _tdb:ScW-00Kri.tdb:LIQUID, tdb:ScW-15Wan.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[ScW-00Kri.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-00Kri.tdb): LIQUID, type code %, sha256 `e3aea447947d7bfa…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : SC W : !
~~~~

[ScW-15Wan.tdb](https://orchid-project.org/data/databases/sgte-binary/ScW-15Wan.tdb): LIQUID, type code %, sha256 `478e3612800b19c0…`

~~~~text
21: PHASE LIQUID:L % 1 1 !
22: CONST LIQUID:L : SC W : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1007/s11669-014-0340-8](https://doi.org/10.1007/s11669-014-0340-8) S. L. Wang, L. J. Zhou, Y. Ye, X. H. Wang, Y. H. Lin, C. P. Wang et al., Thermodynamic Assessments of the Sc-M (M: Cr, Gd, Mo, W and Zr) Systems, J. Phase Equilib. Diffus. 36, 3-9 (2015).  
_assessment that models this phase_
- [doi:10.1515/ijmr-2000-910311](https://doi.org/10.1515/ijmr-2000-910311) N. Krishnamurthy, T. Kundu, A. Awasthi, S.P. Garg, Z. Metallkd., 91, 234-40(2000).  
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
