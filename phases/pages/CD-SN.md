# Cd–Sn phases

> Cd–Sn system: 7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when the stored evidence supports an assignment under the stated tier rules, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CD-SN.html · Markdown: https://data.orchid-project.org/phases/pages/CD-SN.md

7 phases (tier A 6, liquid 1); 4 stable in a calculated diagram. Structure types are assigned only when the stored evidence supports an assignment under the stated tier rules (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CD-SN) · [full JSON](https://data.orchid-project.org/phases/systems/CD-SN.json) · [Cd–Sn system page](https://data.orchid-project.org/systems/CD-SN.html) · [Markdown](https://data.orchid-project.org/phases/pages/CD-SN.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cd–Sn system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-cd-sn-a4-diamond); _phase:cd-sn:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [BCT_A5](#phase-cd-sn-a5-bct); _phase:cd-sn:a5-bct_ | beta-Sn · A5 · tI4 · I4_1/amd (141) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–505.08 K, x(Sn) 0.9889–1 | 0 | 1 |
| [BCC_A2](#phase-cd-sn-bcc-a2); _phase:cd-sn:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3_CDSN](#phase-cd-sn-cdsn-hcp-a3); _phase:cd-sn:cdsn-hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 404.58–495.32 K, x(Sn) 0.94185–0.98234 | 0 | 1 |
| [FCC_A1](#phase-cd-sn-fcc-a1); _phase:cd-sn:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-cd-sn-hcp-a3); _phase:cd-sn:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–594.22 K, x(Sn) 0–0.00262 | 0 | 1 |
| [LIQUID](#phase-cd-sn-liquid); _phase:cd-sn:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 444.95–2500 K, x(Sn) 0–1 | 0 | 1 |

## DIAMOND_A4 (Cd–Sn)

- Id: `phase:cd-sn:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Sn 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:a4-diamond)

Names (2): _corpus: _corpus:phase:cd-sn:a4-diamond  
_tdb: _tdb:CdSn-14Qin.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): DIAMOND_A4, type code %, sha256 `0131d993398b6ba2…`

~~~~text
50: PHASE DIAMOND_A4 % 1 1 !
51: CONST DIAMOND_A4 : SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## BCT_A5 (Cd–Sn)

- Id: `phase:cd-sn:a5-bct`; status `assigned`
- Structure: beta-Sn · A5 · tI4 · I4_1/amd (141); type `st:a5-beta-sn-ti4`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–505.08 K, x(Sn) 0.9889–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:a5-bct)

Names (2): _corpus: _corpus:phase:cd-sn:a5-bct  
_tdb: _tdb:CdSn-14Qin.tdb:BCT_A5  


### TDB models of BCT_A5 (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): BCT_A5, type code %, sha256 `0131d993398b6ba2…`

~~~~text
55: PHASE BCT_A5 % 1 1 !
56: CONST BCT_A5 : CD SN% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## BCC_A2 (Cd–Sn)

- Id: `phase:cd-sn:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:bcc-a2)

Names (2): _corpus: _corpus:phase:cd-sn:bcc-a2  
_tdb: _tdb:CdSn-14Qin.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): BCC_A2, type code %B, sha256 `0131d993398b6ba2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CD SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## HCP_A3_CDSN (Cd–Sn)

- Id: `phase:cd-sn:cdsn-hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 404.58–495.32 K, x(Sn) 0.94185–0.98234
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:cdsn-hcp-a3)

Names (2): _corpus: _corpus:phase:cd-sn:cdsn-hcp-a3  
_tdb: _tdb:CdSn-14Qin.tdb:HCP_A3_CDSN  


### TDB models of HCP_A3_CDSN (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): HCP_A3_CDSN, type code %, sha256 `0131d993398b6ba2…`

~~~~text
45: PHASE HCP_A3_CDSN % 1 1 !
46: CONST HCP_A3_CDSN : CD SN% : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## FCC_A1 (Cd–Sn)

- Id: `phase:cd-sn:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:fcc-a1)

Names (2): _corpus: _corpus:phase:cd-sn:fcc-a1  
_tdb: _tdb:CdSn-14Qin.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): FCC_A1, type code %A, sha256 `0131d993398b6ba2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CD SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## HCP_A3 (Cd–Sn)

- Id: `phase:cd-sn:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 300–594.22 K, x(Sn) 0–0.00262
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:hcp-a3)

Names (2): _corpus: _corpus:phase:cd-sn:hcp-a3  
_tdb: _tdb:CdSn-14Qin.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): HCP_A3, type code %A, sha256 `0131d993398b6ba2…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CD% SN : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
_assessment that models this phase_

## LIQUID (Cd–Sn)

- Id: `phase:cd-sn:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 444.95–2500 K, x(Sn) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cd-sn:liquid)

Names (2): _corpus: _corpus:phase:cd-sn:liquid  
_tdb: _tdb:CdSn-14Qin.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[CdSn-14Qin.tdb](https://orchid-project.org/data/databases/sgte-binary/CdSn-14Qin.tdb): LIQUID, type code %, sha256 `0131d993398b6ba2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CD SN : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1016/j.calphad.2014.06.006](https://doi.org/10.1016/j.calphad.2014.06.006) Aning Qin, Rong Wang, Yaru Wang, Jiong Wang, Shuhong Liu, Kaiming Cheng et al., Thermodynamic assessment of the Cd–X (X=Sn, Mn, Fe) systems, Calphad 47, 83-91 (2014).  
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
