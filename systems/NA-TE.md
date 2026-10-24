# Na–Te system

> Na–Te system: 27 accepted literature values (invariant reaction 20, formation 6, phase transition 1) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/NA-TE.html · Markdown: https://data.orchid-project.org/systems/NA-TE.md

27 accepted literature values from 1 paper(s) (experimental 20, model 7); 1 calculated phase diagram(s).

Data: [JSON](https://data.orchid-project.org/literature/systems/NA-TE.json) · [CSV](https://data.orchid-project.org/systems/NA-TE.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#NA-TE) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#NA-TE/NaTe-14Che.json) · [phases (8)](https://data.orchid-project.org/phases/pages/NA-TE.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/NA-TE.html) · [Markdown](https://data.orchid-project.org/systems/NA-TE.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| experimental | 20 |
| model | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 20 |
| phase transition | 1 |
| formation | 6 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| NaTe-14Che.tdb | Y. Chen, Y. Liu, M. Chu, L. Wang, J. Alloys Compd., 588, 605-10(2014). [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094) | `345a0a074cafc669931dd4287c8fab592be447108b75b5510ce532b185f26c9f` | [viewer](https://orchid-project.org/phase-diagrams/#NA-TE/NaTe-14Che.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/NaTe-14Che.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/NaTe-14Che.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| NaTe-14Che.tdb | 694.51 | NATE3 (x(Te) 0.75) + LIQUID (x(Te) 0.88769) + HEXAGONAL_A8 (x(Te) 1) |
| NaTe-14Che.tdb | 628.27 | NA2TE_C1 (x(Te) 0.33333) + NATE (x(Te) 0.5) + LIQUID (x(Te) 0.51707) |
| NaTe-14Che.tdb | 605.99 | NATE (x(Te) 0.5) + LIQUID (x(Te) 0.56548) + NATE3 (x(Te) 0.75) |
| NaTe-14Che.tdb | 370.87 | BCC_A2 (x(Te) 0) + LIQUID (x(Te) 0) + NA2TE_C1 (x(Te) 0.33333) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/NA/NA-TE.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/NA/NA-TE.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Na–Te system (20)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 676 | eutectic |  | experimental | [1] Chen 2014; _cites Pellini 1910_ | p. 1; `ORC-ALVSKBJBYC` | “The eutectic temperature for the invariant reaction involving Na-Te melts, Te and NaTe3 was identified at 676 K by Pellini and Quercigh \[7\] and Kraus and Glass \[9\].” |
| 676 | liq -> NaTe3 + Te | NaTe3: Te 0.75; Te: Te 1 | experimental | [1] Chen 2014; _cites Pellini 1910_ | Table 3, p. 4, row 12; `ORC-W5Q7T3MLB3` |  |
| 673 | liq -> NaTe3 + Te | liq: Te 0.87; NaTe3: Te 0.75; Te: Te 1 | model | [1] Chen 2014 | Table 3, p. 4, row 11; `ORC-TUHPNLZWHI` |  |
| 628 | liq + Na2Te -> NaTe | Na2Te: Te 0.333333; NaTe: Te 0.5 | experimental | [1] Chen 2014; _cites Kraus 1929_ [doi](https://doi.org/10.1021/j150301a004) | Table 3, p. 4, row 5; `ORC-2XI6LLN33J` |  |
| 628 | liq + Na2Te -> NaTe | liq: Te 0.53; Na2Te: Te 0.333333; NaTe: Te 0.5 | model | [1] Chen 2014 | Table 3, p. 4, row 3; `ORC-BPFMLIXWCD` |  |
| 628 | peritectic |  | experimental | [1] Chen 2014; _cites Kraus 1929_ [doi](https://doi.org/10.1021/j150301a004) | p. 1; `ORC-GB2GA4EIV5.0b6885` | “The peritectic temperature for the invariant reaction involving Na-Te melts, Na2Te and NaTe was identified at 621 K by Pellini and Quercigh \[7\], 628 K by Kraus and Glass \[9\], and 622 K by Petric and Pelton \[10\].” |
| 622 | peritectic |  | experimental | [1] Chen 2014; _cites Petric 1989_ [doi](https://doi.org/10.1002/bbpc.19890930105) | p. 1; `ORC-GB2GA4EIV5.b47e33` | “The peritectic temperature for the invariant reaction involving Na-Te melts, Na2Te and NaTe was identified at 621 K by Pellini and Quercigh \[7\], 628 K by Kraus and Glass \[9\], and 622 K by Petric and Pelton \[10\].” |
| 622 | liq + Na2Te -> NaTe | Na2Te: Te 0.333333; NaTe: Te 0.5 | experimental | [1] Chen 2014; _cites Petric 1989_ [doi](https://doi.org/10.1002/bbpc.19890930105) | Table 3, p. 4, row 6; `ORC-W2456QYIK4` |  |
| 621 | peritectic |  | experimental | [1] Chen 2014; _cites Pellini 1910_ | p. 1; `ORC-GB2GA4EIV5.c52e8c` | “The peritectic temperature for the invariant reaction involving Na-Te melts, Na2Te and NaTe was identified at 621 K by Pellini and Quercigh \[7\], 628 K by Kraus and Glass \[9\], and 622 K by Petric and Pelton \[10\].” |
| 621 | liq + Na2Te -> NaTe | Na2Te: Te 0.333333; NaTe: Te 0.5 | experimental | [1] Chen 2014; _cites Pellini 1910_ | Table 3, p. 4, row 4; `ORC-PILYUS57G3` |  |
| 600 | liq -> NaTe3 + NaTe | liq: Te 0.58; NaTe3: Te 0.75; NaTe: Te 0.5 | model | [1] Chen 2014 | Table 3, p. 4, row 7; `ORC-TPSVAQPATR` |  |
| 592 | liq -> NaTe3 + NaTe | NaTe3: Te 0.75; NaTe: Te 0.5 | experimental | [1] Chen 2014; _cites Kraus 1929_ [doi](https://doi.org/10.1021/j150301a004) | Table 3, p. 4, row 9; `ORC-BBCVKNYBIN` |  |
| 592 | eutectic |  | experimental | [1] Chen 2014; _cites Kraus 1929_ [doi](https://doi.org/10.1021/j150301a004) | p. 1; `ORC-E55RUDEPIH.21001a` | “The eutectic temperature for the invariant reaction involving Na-Te melts, NaTe and NaTe3 was identified at 590 K by Pellini and Quercigh \[7\], at 592 K by Kraus and Glass \[9\], and at 591 K by Petric and Pelton \[10\].” |
| 591 | eutectic |  | experimental | [1] Chen 2014; _cites Petric 1989_ [doi](https://doi.org/10.1002/bbpc.19890930105) | p. 1; `ORC-E55RUDEPIH.4c3b11` | “The eutectic temperature for the invariant reaction involving Na-Te melts, NaTe and NaTe3 was identified at 590 K by Pellini and Quercigh \[7\], at 592 K by Kraus and Glass \[9\], and at 591 K by Petric and Pelton \[10\].” |
| 591 | liq -> NaTe3 + NaTe | NaTe3: Te 0.75; NaTe: Te 0.5 | experimental | [1] Chen 2014; _cites Petric 1989_ [doi](https://doi.org/10.1002/bbpc.19890930105) | Table 3, p. 4, row 10; `ORC-NSN6UL3NYA` |  |
| 590 | liq -> NaTe3 + NaTe | NaTe3: Te 0.75; NaTe: Te 0.5 | experimental | [1] Chen 2014; _cites Pellini 1910_ | Table 3, p. 4, row 8; `ORC-AHSHBC6H2X` |  |
| 590 | eutectic |  | experimental | [1] Chen 2014; _cites Pellini 1910_ | p. 1; `ORC-E55RUDEPIH.7e511e` | “The eutectic temperature for the invariant reaction involving Na-Te melts, NaTe and NaTe3 was identified at 590 K by Pellini and Quercigh \[7\], at 592 K by Kraus and Glass \[9\], and at 591 K by Petric and Pelton \[10\].” |
| 370.8 | eutectic |  | experimental | [1] Chen 2014; _cites Pellini 1910_ | p. 1; `ORC-5QY22QNZ3Q` | “The eutectic temperature for the invariant reaction involving Na-Te melts, NaTe and bcc Na was identified at 370.8 K by Pellini and Quercigh \[7\].” |
| 370.8 | liq -> Na + Na2Te | Na: Te 0; Na2Te: Te 0.333333 | experimental | [1] Chen 2014; _cites Pellini 1910_ | Table 3, p. 4, row 2; `ORC-GXDS4XESA5` |  |
| 370 | liq -> Na + Na2Te | Na: Te 1.000e-4; Na2Te: Te 0.333333 | model | [1] Chen 2014 | Table 3, p. 4, row 1; `ORC-77GSLBGDM6` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Na–Te system (6)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| Na2Te |  | -334.7 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Chen 2014; _cites Morachevskii 1982_ | Table 2, p. 4, row 2; `ORC-35NFM3LGWI.b422b2` |  |
| Na2Te |  | -330 kJ/mol (basis unstated) |  | model |  |  | [1] Chen 2014 | Table 2, p. 4, row 1; `ORC-5X6PWFQ3DG.f0834d` |  |
| NaTe |  | -175 kJ/mol (basis unstated) |  | model |  |  | [1] Chen 2014 | Table 2, p. 4, row 3; `ORC-4LAJOTPUWU.7503a8` |  |
| NaTe |  | -167.5 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Chen 2014; _cites Morachevskii 1982_ | Table 2, p. 4, row 4; `ORC-OO6FMFVXP3.cb02b8` |  |
| NaTe3 |  | -180 kJ/mol (basis unstated) |  | model |  |  | [1] Chen 2014 | Table 2, p. 4, row 5; `ORC-RU3TVFWBLE.8b916f` |  |
| NaTe3 |  | -167.4 kJ/mol (basis unstated) | 298.15 | experimental |  |  | [1] Chen 2014; _cites Morachevskii 1982_ | Table 2, p. 4, row 6; `ORC-JPKWKV7D7J.9fab5f` |  |

## Other properties

### Phase transition (1)

Table: Phase transition, Na–Te system

| Property | Value | T (K) | Phases / composition | Class | Source | Location | Quote |
|---|---:|---:|---|---|---|---|---|
| Phase transition | 709 K | 709 | congruent transformation | experimental | [1] Chen 2014; _cites Kraus 1929_ [doi](https://doi.org/10.1021/j150301a004) | p. 1; `ORC-A2AMQCM5L4` | “In addition, the congruent melting temperature of NaTe3 was reported to be 709 K with resistometric by Kraus and Glass \[8\] and thermal analysis by Kraus and Glass \[9\].” |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Yang Chen, Yajun Liu, Maoyou Chu, Lijun Wang, Phase diagrams and thermodynamic descriptions for Na–Te and K–Te binary systems, Journal of Alloys and Compounds 588, 605-610 (2014). [doi:10.1016/j.jallcom.2013.11.094](https://doi.org/10.1016/j.jallcom.2013.11.094)

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID literature values (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-literature
- R. Arróyave, J. Saal, D. Shin, ORCHID calculated binary phase diagrams (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-diagrams
- R. Arróyave, J. Saal, D. Shin, ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) (version 2026.10), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-hulls
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work); B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_literature_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID literature values}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-literature},
  url       = {https://doi.org/10.5281/zenodo.PENDING-literature},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_phase_diagrams_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID calculated binary phase diagrams}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-diagrams},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-diagrams}
}

@misc{orchid_hulls_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-hulls},
  url       = {https://doi.org/10.5281/zenodo.PENDING-hulls}
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

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite ORCHID ([CITATION.cff](https://data.orchid-project.org/CITATION.cff)) and the original sources. Quotes are short excerpts kept so that each value can be checked; they remain under the publishers' copyright and are not relicensed. Source papers, page images and full text are not redistributed. Field reference: [SCHEMA.md](https://data.orchid-project.org/literature/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt). Found an error? The report link of a value (Markdown: its id, ORC-..., in the Location column) opens a pre-filled GitHub issue, https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml&record_id=\<id>, carrying only the record id, source and value; [how to contribute](https://orchid-project.org/contribute/).
