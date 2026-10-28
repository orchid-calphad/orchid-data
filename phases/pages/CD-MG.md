# Cd–Mg phases

> Cd–Mg system: 5 phases (tier A 3, liquid 1, needs_review 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-MG.html · Markdown: https://data.orchid-project.org/phases/pages/CD-MG.md

5 phases (tier A 3, liquid 1, needs_review 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-MG) · [full JSON](https://data.orchid-project.org/phases/systems/CD-MG.json) · [Cd–Mg system page](https://data.orchid-project.org/systems/CD-MG.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-MG.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Mg system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cd-mg-bcc-a2); _phase:cd-mg:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [FCC_A1](#phase-cd-mg-fcc-a1); _phase:cd-mg:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_4SL](#phase-cd-mg-hcp-4sl); _phase:cd-mg:hcp-4sl_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 300–920 K, x(Mg) 0.01–1 | 13 | 1 |
| [HCP_A3](#phase-cd-mg-hcp-a3); _phase:cd-mg:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–923 K, x(Mg) 0–1 | 6 | 2 |
| [LIQUID](#phase-cd-mg-liquid); _phase:cd-mg:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 594.22–2500 K, x(Mg) 0–1 | 0 | 1 |

## BCC_A2 (Cd–Mg)

- Id: `phase:cd-mg:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mg:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-mg:bcc-a2  
_tdb: _tdb:CdMg-12Ren.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdMg-12Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb): BCC_A2, type code %B, sha256 `2a1ea62b541b4fa1…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CD MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012).  
_assessment that models this phase_

## FCC_A1 (Cd–Mg)

- Id: `phase:cd-mg:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mg:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-mg:fcc-a1  
_tdb: _tdb:CdMg-12Ren.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdMg-12Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb): FCC_A1, type code %A, sha256 `2a1ea62b541b4fa1…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CD MG : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012).  
_assessment that models this phase_

## HCP_4SL (Cd–Mg)

- Id: `phase:cd-mg:hcp-4sl`; status `needs_review`
- No structure assigned. Why: order_disorder_ambiguity:CdMg-12Ren.tdb_model_is_partitioned; sgte_mmc2_row_disagrees_with_name:HCP_4SL; sgte_mmc2_rows_disagree; unrecognised_name_tokens:4SL
- Candidate (dft_mp): P-6m2 (187) — on-hull MP Mg149Cd at x(MG)=0.9933
- Candidate (dft_mp): Cmcm (63) — on-hull MP Mg2Cd at x(MG)=0.6667
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP Mg3Cd at x(MG)=0.7500
- Candidate (dft_mp): Amm2 (38) — on-hull MP MgCd at x(MG)=0.5000
- Candidate (dft_mp): Cmcm (63) — on-hull MP MgCd2 at x(MG)=0.3333
- Candidate (dft_mp): P6_3/mmc (194) — on-hull MP MgCd3 at x(MG)=0.2500
- Candidate (dft_oqmd): Pmma (51) — on-hull OQMD Cd1 Mg1 at x(MG)=0.5000
- Candidate (dft_oqmd): Cmcm (63) — on-hull OQMD Cd1 Mg3 at x(MG)=0.7500
- Stability: stable in 1 of 1 calculated diagram(s): 300–920 K, x(Mg) 0.01–1
- Literature: 13 values (13 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mg:hcp-4sl)

Names (6): _corpus: _corpus:phase:cd-mg:hcp-4sl  
_paper: _paper:10.1016/j.tca.2012.01.016:AB3, paper:10.1016/j.tca.2012.01.016:Cd3Mg, paper:10.1016/j.tca.2012.01.016:CdMg, paper:10.1016/j.tca.2012.01.016:CdMg3  
_tdb: _tdb:CdMg-12Ren.tdb:HCP_4SL  


### TDB models of HCP_4SL (1): PHASE and CONSTITUENT statements as written

[CdMg-12Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb): HCP_4SL, type code %AZ, sha256 `2a1ea62b541b4fa1…`

~~~~text
48: PHASE HCP_4SL %AZ 5 0.25 0.25 0.25 0.25 0.5 !
49: CONST HCP_4SL : CD MG : CD MG : CD MG : CD MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868720](https://doi.org/10.1007/bf02868720) Z. Moser, W. Gasior, J. Wypartowicz, L. Zabdyr, The Cd–Mg (Cadmium–Magnesium) system, Bull. Alloy Phase Diagrams 5 (1984) 23–30.  
_cited as the source of values for this phase_

## HCP_A3 (Cd–Mg)

- Id: `phase:cd-mg:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–923 K, x(Mg) 0–1
- Literature: 6 values (6 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mg:hcp-a3)

Names (4): _corpus: _corpus:phase:cd-mg:hcp-a3  
_paper: _paper:10.1016/j.tca.2012.01.016:Hcp_A3  
_tdb: _tdb:CdMg-12Ren.tdb:A3_HCP, tdb:CdMg-12Ren.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[CdMg-12Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb): A3_HCP, type code %A, sha256 `2a1ea62b541b4fa1…`

~~~~text
43: PHASE A3_HCP %A 2 1 0.5 !
44: CONST A3_HCP : CD MG : VA : !
~~~~

[CdMg-12Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb): HCP_A3, type code %A, sha256 `2a1ea62b541b4fa1…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CD MG : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1007/bf02868720](https://doi.org/10.1007/bf02868720) Z. Moser, W. Gasior, J. Wypartowicz, L. Zabdyr, The Cd–Mg (Cadmium–Magnesium) system, Bull. Alloy Phase Diagrams 5 (1984) 23–30.  
_cited as the source of values for this phase_

## LIQUID (Cd–Mg)

- Id: `phase:cd-mg:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 594.22–2500 K, x(Mg) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-mg:liquid)

Names (2): _corpus: _corpus:phase:cd-mg:liquid  
_tdb: _tdb:CdMg-12Ren.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdMg-12Ren.tdb](https://orchid-project.org/data/databases/sgte-binary/CdMg-12Ren.tdb): LIQUID, type code %, sha256 `2a1ea62b541b4fa1…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CD MG : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.tca.2012.01.016](https://doi.org/10.1016/j.tca.2012.01.016) Xin Ren, Changrong Li, Cuiping Guo, Zhenmin Du, A thermodynamic assessment of the Cd–Mg system, Thermochimica Acta 534, 1-8 (2012).  
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
