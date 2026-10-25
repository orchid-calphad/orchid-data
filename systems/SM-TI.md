# Sm–Ti system

> Sm–Ti system: 33 accepted literature values (formation 28, invariant reaction 5) and 1 calculated phase diagram(s) from ORCHID, each value with evidence class, source, page and quote.

HTML: https://data.orchid-project.org/systems/SM-TI.html · Markdown: https://data.orchid-project.org/systems/SM-TI.md

33 accepted literature values from 1 paper(s) (model 5, DFT 21, unspecified 7); 1 calculated phase diagram(s). 1 further extracted value(s) not accepted by the reader-agreement checks are only in the JSON/CSV.

Data: [JSON](https://data.orchid-project.org/literature/systems/SM-TI.json) · [CSV](https://data.orchid-project.org/systems/SM-TI.csv) · [interactive explorer](https://orchid-project.org/data-explorer/#SM-TI) · [interactive phase diagram](https://orchid-project.org/phase-diagrams/#SM-TI/SmTi-21Sae.json) · [phases (5)](https://data.orchid-project.org/phases/pages/SM-TI.html) · [papers (bibliography)](https://data.orchid-project.org/bibliography/pages/systems/SM-TI.html) · [Markdown](https://data.orchid-project.org/systems/SM-TI.md)

Table: Accepted values by evidence class

| Evidence class | Values |
|---|---:|
| model | 5 |
| DFT | 21 |
| unspecified | 7 |

Table: Accepted values by property group

| Property group | Values |
|---|---:|
| invariant reaction | 5 |
| formation | 28 |

## Calculated phase diagrams

Binary phase diagrams calculated with pycalphad 0.11.2 from the SGTE binary collection (Hallstedt 2025, CC BY 4.0). Evidence class: model.

Table: Assessments with a calculated phase diagram

| TDB file | Assessment | SHA-256 | Links |
|---|---|---|---|
| SmTi-21Sae.tdb | A. Saengdeejing, Y. Chen, O. Takeda, M. Enoki, S. Sugimoto, H. Ohtani, A. Taichi, Calphad, 75, 102357(2021). [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357) | `d33873229a2fab02cbcc8211cb768befce817608ae4bcb86ba52477d8e3b419a` | [viewer](https://orchid-project.org/phase-diagrams/#SM-TI/SmTi-21Sae.json) · [TDB](https://orchid-project.org/data/databases/sgte-binary/SmTi-21Sae.tdb) · [JSON](https://data.orchid-project.org/phase-diagrams/sgte/SmTi-21Sae.json) |

Table: Calculated three-phase invariants (model, mole fraction of the second component)

| TDB file | T (K) | Phases at the invariant |
|---|---:|---|
| SmTi-21Sae.tdb | 1877.72 | LIQUID (x(Ti) 0.129) + LIQUID#2 (x(Ti) 0.95271) + BCC_A2 (x(Ti) 0.98951) |
| SmTi-21Sae.tdb | 1309.39 | BCC_A2 (x(Ti) 7.300e-4) + LIQUID (x(Ti) 0.02162) + BCC_A2#2 (x(Ti) 0.99426) |
| SmTi-21Sae.tdb | 1193.54 | HCP_A3 (x(Ti) 4.000e-5) + BCC_A2#2 (x(Ti) 4.100e-4) + BCC_A2 (x(Ti) 0.99576) |
| SmTi-21Sae.tdb | 1193.54 | HCP_A3 (x(Ti) 4.000e-5) + BCC_A2 (x(Ti) 4.100e-4) + BCC_A2#2 (x(Ti) 0.99576) |
| SmTi-21Sae.tdb | 1146.55 | HCP_A3#2 (x(Ti) 2.000e-5) + BCC_A2 (x(Ti) 0.99636) + HCP_A3 (x(Ti) 0.99961) |
| SmTi-21Sae.tdb | 1146.55 | HCP_A3 (x(Ti) 2.000e-5) + BCC_A2 (x(Ti) 0.99636) + HCP_A3#2 (x(Ti) 0.99961) |
| SmTi-21Sae.tdb | 1013.24 | HCP_A3 (x(Ti) 1.000e-5) + RHOMB_C19 (x(Ti) 6.000e-5) + HCP_A3#2 (x(Ti) 0.99987) |
| SmTi-21Sae.tdb | 1013.24 | HCP_A3 (x(Ti) 1.000e-5) + RHOMB_C19 (x(Ti) 6.000e-5) + HCP_A3#2 (x(Ti) 0.99987) |
| SmTi-21Sae.tdb | 1013.24 | HCP_A3 (x(Ti) 1.000e-5) + RHOMB_C19 (x(Ti) 6.000e-5) + HCP_A3#2 (x(Ti) 0.99987) |
| SmTi-21Sae.tdb | 1013.24 | HCP_A3#2 (x(Ti) 1.000e-5) + RHOMB_C19 (x(Ti) 6.000e-5) + HCP_A3 (x(Ti) 0.99987) |

Convex hulls: [Materials Project DFT hull](https://data.orchid-project.org/hulls/dft-mp/SM/SM-TI.json) · [OQMD DFT hull](https://data.orchid-project.org/hulls/dft-oqmd/SM/SM-TI.json)

## Invariant reactions (literature)

Table: Invariant reactions reported in the literature for the Sm–Ti system (5)

| T (K) | Reaction / phases | Compositions (mole fraction) | Class | Source | Location | Quote |
|---:|---|---|---|---|---|---|
| 1878 | Liquid \<-> Liquid + bcc | Liquid: Ti 0.129; bcc: Ti 0.9895 | model | [1] Saengdeejing 2021 | Table 4, p. 25, row 1; `ORC-QV5XJV36CW` |  |
| 1309 | Liquid \<-> bcc#1 + bcc#2 | Liquid: Ti 0.02162; bcc#1: Ti 7.300e-4; bcc#2: Ti 0.9942 | model | [1] Saengdeejing 2021 | Table 4, p. 25, row 2; `ORC-5HQQTQ72KI` |  |
| 1194 | bcc \<-> hcp + bcc | bcc: Ti 0.9958; hcp: Ti 3.900e-5 | model | [1] Saengdeejing 2021 | Table 4, p. 25, row 3; `ORC-ZVPY4KI6CZ` |  |
| 1147 | bcc \<-> hcp#1 + hcp#2 | bcc: Ti 0.9964; hcp#1: Ti 2.500e-5; hcp#2: Ti 0.9996 | model | [1] Saengdeejing 2021 | Table 4, p. 25, row 4; `ORC-4EBA4ZZDUK` |  |
| 1013 | hcp#1 + hcp#2 \<-> Rhombohedral | hcp#1: Ti 5.000e-6; hcp#2: Ti 0.9998; Rhombohedral: Ti 5.700e-5 | model | [1] Saengdeejing 2021 | Table 4, p. 25, row 5; `ORC-D7FFQBIQJ2` |  |

## Formation enthalpies

Literature values in kJ/mol-atom where the per-atom basis is known. DFT columns: the lowest-energy entry at the same composition (Materials Project 2026.04.13, OQMD v1.8; different energy references, never averaged), from [dft_parity.json](https://data.orchid-project.org/literature/dft_parity.json).

Table: Enthalpies of formation, Sm–Ti system (28)

| Phase | Compound | Value | T (K) | Class | MP DFT (kJ/mol-atom) | OQMD DFT (kJ/mol-atom) | Source | Location | Quote |
|---|---|---:|---:|---|---:|---:|---|---|---|
| B2 SmTi |  | 35.3329 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 31; `ORC-RQG34AA5CY.af9d92` |  |
| B32 SmTi |  | 38.3143 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 32; `ORC-MMSPFYT2UT.0b4edf` |  |
| Bᵢ SmTi-1 |  | 69.4501 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 39; `ORC-BDSE2MZC4B.09621a` |  |
| Bᵢ SmTi-2 |  | 34.069 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 40; `ORC-7CMDCBLR4F.64e707` |  |
| D0₂₂ SmTi₃ |  | 28.1351 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 25; `ORC-OI5IS6J7DQ.2b29d1` |  |
| D0₂₂ Sm₃Ti |  | 22.2109 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 26; `ORC-MCXQCN3TBN.cac024` |  |
| D0₂₃ SmTi₃ |  | 30.1903 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 27; `ORC-WKV6UNUJYK.7f6124` |  |
| D0₂₃ Sm₃Ti |  | 28.4149 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 28; `ORC-TETM5CEMUD.e69090` |  |
| D0₃ SmTi₃ |  | 32.5542 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 33; `ORC-YRNZYP6N7L.b8998e` |  |
| D0₃ Sm₃Ti |  | 31.5121 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 34; `ORC-OOAY3V37FF.1f1d52` |  |
| I4/mmm SmTi₃ |  | 28.1448 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 35; `ORC-2QESSNROE3.a3c2e1` |  |
| I4/mmm Sm₃Ti |  | 22.2013 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 36; `ORC-OZUBC3I53K.274f07` |  |
| L1₀ SmTi |  | 35.3426 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 22; `ORC-LSK2PKCFHD.9e5a95` |  |
| L1₂ SmTi₃ |  | 29.3026 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 23; `ORC-V3VNCQJIIK.77be28` |  |
| L1₂ Sm₃Ti |  | 21.825 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 24; `ORC-ZWYNIDBB5Q.96b0bb` |  |
| SmTi | [SmTi](https://data.orchid-project.org/compounds/SmTi.html) | 16.1709 kJ/mol-atom | 0 | unspecified |  | 8.737 (oqmd-755584) | [1] Saengdeejing 2021 | Table 2, p. 13, row 3; `ORC-KOJE4OLBR6` |  |
| SmTi₆ |  | 8.50036 kJ/mol-atom | 0 | unspecified |  |  | [1] Saengdeejing 2021 | Table 2, p. 13, row 7; `ORC-MRLXOQYJ3E` |  |
| Sm₁₁Ti₈ |  | 13.0062 kJ/mol-atom | 0 | unspecified |  |  | [1] Saengdeejing 2021 | Table 2, p. 13, row 2; `ORC-XDY6RRFUIN` |  |
| Sm₂Ti₃ | [Sm2Ti3](https://data.orchid-project.org/compounds/Sm2Ti3.html) | 12.6685 kJ/mol-atom | 0 | unspecified |  | 65.771 (oqmd-428705) | [1] Saengdeejing 2021 | Table 2, p. 13, row 4; `ORC-XH7E5G77IP` |  |
| Sm₃Ti | [Sm3Ti](https://data.orchid-project.org/compounds/Sm3Ti.html) | 12.7457 kJ/mol-atom | 0 | unspecified | 23.099 (mp-aaacdipi) | 19.47 (oqmd-320604) | [1] Saengdeejing 2021 | Table 2, p. 13, row 1; `ORC-IRDKSBDPTQ` |  |
| Sm₄Ti₁₅ |  | 9.69678 kJ/mol-atom | 0 | unspecified |  |  | [1] Saengdeejing 2021 | Table 2, p. 13, row 6; `ORC-GPTQP2UGIS` |  |
| Sm₆Ti₁₃ |  | 11.858 kJ/mol-atom | 0 | unspecified |  |  | [1] Saengdeejing 2021 | Table 2, p. 13, row 5; `ORC-YNZ3UOEEA7` |  |
| cF12 SmTi₂ |  | 121.224 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 29; `ORC-XL3YUSSYHB.8985be` |  |
| cF12 Sm₂Ti |  | 70.9843 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 30; `ORC-BNXXK5TP26.2d318e` |  |
| hP5 Sm₂Ti₃ |  | 87.242 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 41; `ORC-FMNT73JAZA.75a0c3` |  |
| hP5 Sm₃Ti₂ |  | 40.0607 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 42; `ORC-2HXDZABP4Z.098561` |  |
| hR SmTi₂ |  | 27.3632 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 37; `ORC-4LYRMDI33R.7e837a` |  |
| hR Sm₂Ti |  | 26.3791 kJ/mol-atom | 0 | DFT |  |  | [1] Saengdeejing 2021 | Table 1, p. 5, row 38; `ORC-DF7YVVIKAK.d24e0b` |  |

## Sources

Reporting papers the values were read from (a value cited from another work names that work in its row).

1. Arkapol Saengdeejing, Ying Chen, Osamu Takeda, Masanori Enoki, Satoshi Sugimoto, Hiroshi Ohtani et al., Sm–Ti binary thermodynamic database and phase diagram, Calphad 75, 102357 (2021). [doi:10.1016/j.calphad.2021.102357](https://doi.org/10.1016/j.calphad.2021.102357)

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
