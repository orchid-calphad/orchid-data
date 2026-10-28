# Ag–Si phases

> Ag–Si system: 5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/AG-SI.html · Markdown: https://data.orchid-project.org/phases/pages/AG-SI.md

5 phases (tier A 4, liquid 1); 3 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=AG-SI) · [full JSON](https://data.orchid-project.org/phases/systems/AG-SI.json) · [Ag–Si system page](https://data.orchid-project.org/systems/AG-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/AG-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Ag–Si system (5)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-ag-si-a4-diamond); _phase:ag-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 0.99998–1 | 7 | 2 |
| [BCC_A2](#phase-ag-si-bcc-a2); _phase:ag-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [FCC_A1](#phase-ag-si-fcc-a1); _phase:ag-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 2 of 2 calculated diagram(s): 300–1248.18 K, x(Si) 0–0.00067 | 7 | 2 |
| [HCP_A3](#phase-ag-si-hcp-a3); _phase:ag-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 2 calculated diagram(s) | 0 | 2 |
| [LIQUID](#phase-ag-si-liquid); _phase:ag-si:liquid_ | liquid | liquid | stable in 2 of 2 calculated diagram(s): 1110.21–2500 K, x(Si) 0–1 | 5 | 2 |

## DIAMOND_A4 (Ag–Si)

- Id: `phase:ag-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1687 K, x(Si) 0.99998–1
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-si:a4-diamond)

Names (5): _corpus: _corpus:phase:ag-si:a4-diamond  
_paper: _paper:10.1016/0040-6031(88)87048-5:Si dia, paper:10.1016/0040-6031(88)87048-5:dia  
_tdb: _tdb:AgSi-85Sau.tdb:DIAMOND_A4, tdb:AgSi-88Che-LB.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (2): PHASE and CONSTITUENT statements as written

[AgSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-85Sau.tdb): DIAMOND_A4, type code %, sha256 `7730593a39e0f7f4…`

~~~~text
39: PHASE DIAMOND_A4 % 1 1 !
40: CONST DIAMOND_A4 : SI : !
~~~~

[AgSi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-88Che-LB.tdb): DIAMOND_A4, type code %, sha256 `97dc06551f22e1b3…`

~~~~text
49: PHASE DIAMOND_A4 % 1 1 !
50: CONST DIAMOND_A4 : AG SI% : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5) P.-Y. Chevalier, Thermodynamic evalution of the Ag-Si system, Thermochimica Acta 130, 33-41 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080600128](https://doi.org/10.1002/zaac.19080600128) G. Arrivaut, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXVIII. Über Silicium‐Silberlegierungen, Z. Anorg. Chem. 60, 436-440 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_

## BCC_A2 (Ag–Si)

- Id: `phase:ag-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-si:bcc-a2)

Names (3): _corpus: _corpus:phase:ag-si:bcc-a2  
_tdb: _tdb:AgSi-85Sau.tdb:BCC_A2, tdb:AgSi-88Che-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (2): PHASE and CONSTITUENT statements as written

[AgSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-85Sau.tdb): BCC_A2, type code %B, sha256 `7730593a39e0f7f4…`

~~~~text
29: PHASE BCC_A2 %B 2 1 3 !
30: CONST BCC_A2 : AG SI : VA : !
~~~~

[AgSi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-88Che-LB.tdb): BCC_A2, type code %B, sha256 `97dc06551f22e1b3…`

~~~~text
39: PHASE BCC_A2 %B 2 1 3 !
40: CONST BCC_A2 : AG SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5) P.-Y. Chevalier, Thermodynamic evalution of the Ag-Si system, Thermochimica Acta 130, 33-41 (1988).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## FCC_A1 (Ag–Si)

- Id: `phase:ag-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 300–1248.18 K, x(Si) 0–0.00067
- Literature: 7 values (7 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-si:fcc-a1)

Names (5): _corpus: _corpus:phase:ag-si:fcc-a1  
_paper: _paper:10.1016/0040-6031(88)87048-5:Ag f.c.c., paper:10.1016/0040-6031(88)87048-5:Ag(f.c.c.)  
_tdb: _tdb:AgSi-85Sau.tdb:FCC_A1, tdb:AgSi-88Che-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (2): PHASE and CONSTITUENT statements as written

[AgSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-85Sau.tdb): FCC_A1, type code %A, sha256 `7730593a39e0f7f4…`

~~~~text
24: PHASE FCC_A1 %A 2 1 1 !
25: CONST FCC_A1 : AG% SI : VA : !
~~~~

[AgSi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-88Che-LB.tdb): FCC_A1, type code %A, sha256 `97dc06551f22e1b3…`

~~~~text
34: PHASE FCC_A1 %A 2 1 1 !
35: CONST FCC_A1 : AG% SI : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5) P.-Y. Chevalier, Thermodynamic evalution of the Ag-Si system, Thermochimica Acta 130, 33-41 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080600128](https://doi.org/10.1002/zaac.19080600128) G. Arrivaut, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXVIII. Über Silicium‐Silberlegierungen, Z. Anorg. Chem. 60, 436-440 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_

## HCP_A3 (Ag–Si)

- Id: `phase:ag-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 2 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-si:hcp-a3)

Names (3): _corpus: _corpus:phase:ag-si:hcp-a3  
_tdb: _tdb:AgSi-85Sau.tdb:HCP_A3, tdb:AgSi-88Che-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (2): PHASE and CONSTITUENT statements as written

[AgSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-85Sau.tdb): HCP_A3, type code %A, sha256 `7730593a39e0f7f4…`

~~~~text
34: PHASE HCP_A3 %A 2 1 0.5 !
35: CONST HCP_A3 : AG SI : VA : !
~~~~

[AgSi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-88Che-LB.tdb): HCP_A3, type code %A, sha256 `97dc06551f22e1b3…`

~~~~text
44: PHASE HCP_A3 %A 2 1 0.5 !
45: CONST HCP_A3 : AG SI : VA : !
~~~~

Example references (2 of 2; assessments first): 

- [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5) P.-Y. Chevalier, Thermodynamic evalution of the Ag-Si system, Thermochimica Acta 130, 33-41 (1988).  
_assessment that models this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_

## LIQUID (Ag–Si)

- Id: `phase:ag-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 2 of 2 calculated diagram(s): 1110.21–2500 K, x(Si) 0–1
- Literature: 5 values (5 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:ag-si:liquid)

Names (4): _corpus: _corpus:phase:ag-si:liquid  
_paper: _paper:10.1016/0040-6031(88)87048-5:L  
_tdb: _tdb:AgSi-85Sau.tdb:LIQUID, tdb:AgSi-88Che-LB.tdb:LIQUID  


### TDB models of LIQUID (2): PHASE and CONSTITUENT statements as written

[AgSi-85Sau.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-85Sau.tdb): LIQUID, type code %, sha256 `7730593a39e0f7f4…`

~~~~text
19: PHASE LIQUID:L % 1 1 !
20: CONST LIQUID:L : AG SI : !
~~~~

[AgSi-88Che-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/AgSi-88Che-LB.tdb): LIQUID, type code %, sha256 `97dc06551f22e1b3…`

~~~~text
29: PHASE LIQUID:L % 1 1 !
30: CONST LIQUID:L : AG SI : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1016/0040-6031(88)87048-5](https://doi.org/10.1016/0040-6031%2888%2987048-5) P.-Y. Chevalier, Thermodynamic evalution of the Ag-Si system, Thermochimica Acta 130, 33-41 (1988).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0364-5916(85)90001-X](https://doi.org/10.1016/0364-5916%2885%2990001-X) N. Saunders, Calphad, 9, 297-309(1985).  
_assessment that models this phase_
- [doi:10.1002/zaac.19080600128](https://doi.org/10.1002/zaac.19080600128) G. Arrivaut, Metallographische Mitteilungen aus dem Institut für physikalische Chemie der Universität Göttingen. LXVIII. Über Silicium‐Silberlegierungen, Z. Anorg. Chem. 60, 436-440 (1908).  
_cited as the source of values for this phase_
- [doi:10.1016/0022-5088(75)90138-1](https://doi.org/10.1016/0022-5088%2875%2990138-1) Bruno Predel, Hanspeter Bankstahl, Beitrag zur kenntnis der thermodynamischen eigenschaften flüssiger silber-germanium-, silber-silizium-, gold-germanium- und gold-silizium-legierungen, Journal of the Less Common Metals 43, 191-203 (1975).  
_cited as the source of values for this phase_

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
