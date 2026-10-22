---
license: cc-by-4.0
pretty_name: "ORCHID: literature thermodynamic data, calculated phase diagrams and DFT hulls"
language:
- en
task_categories:
- tabular-regression
- table-question-answering
- question-answering
- text-retrieval
tags:
- calphad
- thermodynamics
- materials-science
- phase-diagrams
- dft
- alloys
- formation-enthalpy
- information-extraction
- scientific-literature
size_categories:
- 10K<n<100K
configs:
- config_name: literature_values
  data_files:
  - split: full
    path: parquet/literature_values.parquet
  default: true
- config_name: papers
  data_files:
  - split: full
    path: parquet/papers.parquet
- config_name: experimental_context
  data_files:
  - split: full
    path: parquet/experimental_context.parquet
- config_name: dft_parity
  data_files:
  - split: full
    path: parquet/dft_parity.parquet
- config_name: phase_diagram_invariants
  data_files:
  - split: full
    path: parquet/phase_diagram_invariants.parquet
- config_name: phase_diagram_index
  data_files:
  - split: full
    path: parquet/phase_diagram_index.parquet
- config_name: hull_vertices
  data_files:
  - split: full
    path: parquet/hull_vertices.parquet
dataset_info:
- config_name: literature_values
  features:
  - name: id
    dtype: string
  - name: pid
    dtype: string
  - name: system
    dtype: string
  - name: elements
    list: string
  - name: n_elements
    dtype: int32
  - name: record_kind
    dtype: string
  - name: observation_type
    dtype: string
  - name: property
    dtype: string
  - name: property_group
    dtype: string
  - name: property_printed
    dtype: string
  - name: value
    dtype: float64
  - name: value_min
    dtype: float64
  - name: value_max
    dtype: float64
  - name: value_expression
    dtype: string
  - name: unit
    dtype: string
  - name: value_stored
    dtype: float64
  - name: unit_stored
    dtype: string
  - name: value_printed
    dtype: float64
  - name: unit_printed
    dtype: string
  - name: uncertainty_value
    dtype: float64
  - name: uncertainty_basis
    dtype: string
  - name: uncertainty_note
    dtype: string
  - name: bound
    dtype: string
  - name: temperature_bound_K
    dtype: float64
  - name: temperature_K
    dtype: float64
  - name: temperature_min_K
    dtype: float64
  - name: temperature_max_K
    dtype: float64
  - name: temperature_printed
    dtype: string
  - name: temperature_basis
    dtype: string
  - name: temperature_approximate
    dtype: bool
  - name: temperature_uncertainty_value
    dtype: float64
  - name: temperature_uncertainty_basis
    dtype: string
  - name: pressure_Pa
    dtype: float64
  - name: pressure_basis
    dtype: string
  - name: phases
    list: string
  - name: model_phases
    list: string
  - name: phase_details
    list:
    - name: label
      dtype: string
    - name: model_phase
      dtype: string
    - name: mapping_confidence
      dtype: string
    - name: pearson_symbol
      dtype: string
    - name: prototype
      dtype: string
  - name: reaction
    dtype: string
  - name: reaction_type
    dtype: string
  - name: transition_kind
    dtype: string
  - name: transition_kind_printed
    dtype: string
  - name: property_code_raw
    dtype: string
  - name: unit_basis
    dtype: string
  - name: per_formula_unit_divisor
    dtype: float64
  - name: value_before_quality_fix
    dtype: float64
  - name: merged_ids
    list: string
  - name: compositions
    list:
    - name: phase
      dtype: string
    - name: element
      dtype: string
    - name: value
      dtype: float64
    - name: basis
      dtype: string
    - name: source
      dtype: string
  - name: overall_composition
    list:
    - name: element
      dtype: string
    - name: value
      dtype: float64
  - name: overall_composition_basis
    dtype: string
  - name: reference_state_json
    dtype: string
  - name: component
    dtype: string
  - name: structure_pearson_symbol
    dtype: string
  - name: structure_prototype
    dtype: string
  - name: structure_strukturbericht
    dtype: string
  - name: structure_space_group
    dtype: string
  - name: structure_space_group_number
    dtype: int32
  - name: evidence_class
    dtype: string
  - name: origin
    dtype: string
  - name: origin_class
    dtype: string
  - name: origin_measured_in
    dtype: string
  - name: origin_own_work_of_paper
    dtype: bool
  - name: accepted
    dtype: bool
  - name: flag_espei_ready
    dtype: bool
  - name: flag_judge_adjudicated
    dtype: bool
  - name: flag_magnitude_suspect
    dtype: bool
  - name: flag_source_disputed
    dtype: bool
  - name: flag_system_mismatch
    dtype: bool
  - name: flag_unsigned_in_print
    dtype: bool
  - name: flag_sign_pdf_page_verified
    dtype: bool
  - name: flag_has_dropped_fields
    dtype: bool
  - name: flag_composition_conflict_between_readers
    dtype: bool
  - name: flag_unit_conflict_between_readers
    dtype: bool
  - name: flag_page_unreadable
    dtype: bool
  - name: flag_basis_inferred_from_magnitude
    dtype: bool
  - name: flag_basis_corrected_from_formula
    dtype: bool
  - name: flag_sign_from_heading
    dtype: bool
  - name: flag_dft_outlier_unexplained
    dtype: bool
  - name: flag_reference_state_dropped_not_in_quote
    dtype: bool
  - name: flag_state_fully_specified
    dtype: bool
  - name: flag_value_in_quote
    dtype: bool
  - name: dropped_field_count
    dtype: int32
  - name: review_state
    dtype: string
  - name: row_state
    dtype: string
  - name: review_flags
    list: string
  - name: specification_gaps
    list: string
  - name: plausibility_result
    dtype: string
  - name: plausibility_dT_K
    dtype: float64
  - name: plausibility_model
    dtype: string
  - name: method
    dtype: string
  - name: method_basis
    dtype: string
  - name: conditions_kind
    dtype: string
  - name: conditions_paper
    dtype: string
  - name: paper_id
    dtype: string
  - name: paper_doi
    dtype: string
  - name: paper_citation
    dtype: string
  - name: paper_year
    dtype: int32
  - name: cited_dois
    list: string
  - name: cited_labels
    list: string
  - name: quote
    dtype: string
  - name: quote_page
    dtype: int32
  - name: link_rule
    dtype: string
  - name: artifact
    dtype: string
  - name: artifact_label
    dtype: string
  - name: artifact_caption
    dtype: string
  - name: page
    dtype: int32
  - name: table_row
    dtype: int32
  - name: model_tdb
    dtype: string
  - name: model_tdb_path
    dtype: string
  - name: model_tdb_sha256
    dtype: string
  - name: model_doi
    dtype: string
  - name: model_reproduced_by_calculation
    dtype: bool
  - name: model_unlinked_reason
    dtype: string
  - name: readers
    list: string
  - name: reader_tier
    dtype: string
  - name: tool_release
    dtype: string
  - name: release
    dtype: string
  - name: split
    dtype: string
  splits:
  - name: full
    num_examples: 76432
  download_size: 6067938
- config_name: papers
  features:
  - name: id
    dtype: string
  - name: doi
    dtype: string
  - name: doi_url
    dtype: string
  - name: citation
    dtype: string
  - name: title
    dtype: string
  - name: authors
    list: string
  - name: year
    dtype: int32
  - name: container
    dtype: string
  - name: kind
    dtype: string
  - name: roles
    list: string
  - name: source_kinds
    list: string
  - name: systems
    list: string
  - name: metadata_source
    dtype: string
  - name: pdf_sha256_prefix
    dtype: string
  - name: n_values
    dtype: int32
  splits:
  - name: full
    num_examples: 4877
  download_size: 529209
- config_name: experimental_context
  features:
  - name: paper_id
    dtype: string
  - name: context_id
    dtype: string
  - name: section_basis
    dtype: string
  - name: context_reader_tier
    dtype: string
  - name: context_readers
    list: string
  - name: item_id
    dtype: string
  - name: type
    dtype: string
  - name: label
    dtype: string
  - name: purity
    dtype: string
  - name: starting_materials
    dtype: string
  - name: synthesis
    dtype: string
  - name: nominal_composition
    dtype: string
  - name: composition_basis
    dtype: string
  - name: measured_composition
    dtype: string
  - name: temperature_printed
    dtype: string
  - name: temperature_status
    dtype: string
  - name: duration
    dtype: string
  - name: atmosphere_or_container
    dtype: string
  - name: cooling
    dtype: string
  - name: purpose
    dtype: string
  - name: method
    dtype: string
  - name: instrument
    dtype: string
  - name: heating_or_cooling_rate
    dtype: string
  - name: atmosphere
    dtype: string
  - name: crucible
    dtype: string
  - name: calibration
    dtype: string
  - name: stated_uncertainty
    dtype: string
  - name: applies_to
    dtype: string
  - name: temperature_K
    dtype: float64
  - name: duration_hours
    dtype: float64
  - name: quote
    dtype: string
  - name: page
    dtype: int32
  - name: extraction_accepted
    dtype: bool
  - name: second_reader_agrees
    dtype: bool
  - name: has_dropped_fields
    dtype: bool
  - name: review_flags
    list: string
  splits:
  - name: full
    num_examples: 1504
  download_size: 161785
- config_name: dft_parity
  features:
  - name: record_id
    dtype: string
  - name: dft_source
    dtype: string
  - name: system
    dtype: string
  - name: elements
    list: string
  - name: formula
    dtype: string
  - name: phase_label
    dtype: string
  - name: composition
    list:
    - name: element
      dtype: string
    - name: x
      dtype: float64
  - name: formula_match
    dtype: string
  - name: match_note
    dtype: string
  - name: lit_kJ_per_mol_atom
    dtype: float64
  - name: dft_kJ_per_mol_atom
    dtype: float64
  - name: dft_eV_per_atom
    dtype: float64
  - name: residual_kJ_per_mol_atom
    dtype: float64
  - name: ehull_kJ_per_mol_atom
    dtype: float64
  - name: dft_material_id
    dtype: string
  - name: dft_spacegroup
    dtype: string
  - name: dft_theoretical
    dtype: bool
  - name: dft_n_polymorphs
    dtype: int32
  - name: evidence_class
    dtype: string
  - name: accepted
    dtype: bool
  - name: own_work_of_paper
    dtype: bool
  - name: unsigned
    dtype: bool
  - name: sign_lost
    dtype: bool
  - name: sign_verified
    dtype: bool
  - name: sign_check
    dtype: string
  - name: suspect
    list: string
  - name: chem_class
    dtype: string
  - name: method_class
    dtype: string
  - name: method
    dtype: string
  - name: temperature_K
    dtype: float64
  - name: record_kind
    dtype: string
  - name: paper_id
    dtype: string
  - name: page
    dtype: int32
  - name: table
    dtype: string
  - name: quote
    dtype: string
  - name: cited_dois
    list: string
  - name: default_subset
    dtype: bool
  - name: dft_release
    dtype: string
  - name: quality_fix
    dtype: string
  - name: unit_basis
    dtype: string
  - name: basis_inferred_from_magnitude
    dtype: bool
  splits:
  - name: full
    num_examples: 7826
  download_size: 270741
- config_name: phase_diagram_invariants
  features:
  - name: system
    dtype: string
  - name: file
    dtype: string
  - name: tdb
    dtype: string
  - name: tdb_sha256
    dtype: string
  - name: x_component
    dtype: string
  - name: invariant_index
    dtype: int32
  - name: T_K
    dtype: float64
  - name: n_phases
    dtype: int32
  - name: phases
    list: string
  - name: compositions
    list:
    - name: phase
      dtype: string
    - name: x
      dtype: float64
  - name: x_min
    dtype: float64
  - name: x_max
    dtype: float64
  - name: engine
    dtype: string
  - name: citation
    dtype: string
  - name: doi
    dtype: string
  splits:
  - name: full
    num_examples: 24828
  download_size: 850031
- config_name: phase_diagram_index
  features:
  - name: system
    dtype: string
  - name: elements
    list: string
  - name: file
    dtype: string
  - name: tdb
    dtype: string
  - name: tdb_sha256
    dtype: string
  - name: status
    dtype: string
  - name: listed_in_index
    dtype: bool
  - name: has_grid
    dtype: bool
  - name: x_component
    dtype: string
  - name: T_min_K
    dtype: float64
  - name: T_max_K
    dtype: float64
  - name: phases
    list: string
  - name: n_invariants
    dtype: int32
  - name: engine
    dtype: string
  - name: citation
    dtype: string
  - name: doi
    dtype: string
  splits:
  - name: full
    num_examples: 2774
  download_size: 263411
- config_name: hull_vertices
  features:
  - name: system
    dtype: string
  - name: source
    dtype: string
  - name: a_element
    dtype: string
  - name: x_element
    dtype: string
  - name: formula
    dtype: string
  - name: x
    dtype: float64
  - name: formation_energy_eV_per_atom
    dtype: float64
  - name: formation_energy_kJ_per_mol_atom
    dtype: float64
  - name: energy_per_atom_eV
    dtype: float64
  - name: material_id
    dtype: string
  - name: spacegroup_symbol
    dtype: string
  - name: spacegroup_number
    dtype: int32
  - name: theoretical
    dtype: bool
  - name: collinear
    dtype: bool
  - name: degenerate_ids
    list: string
  - name: is_endpoint
    dtype: bool
  - name: reference_kind
    dtype: string
  - name: release
    dtype: string
  - name: thermo_type
    dtype: string
  - name: entry_pool
    dtype: string
  - name: snapshot_sha256
    dtype: string
  splits:
  - name: full
    num_examples: 28143
  download_size: 679954
---

# ORCHID data: analysis-ready tables

**ORCHID** (Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery) publishes thermodynamic and
phase-equilibrium values read from published papers, binary phase diagrams calculated from assessed CALPHAD
databases, and binary convex hulls from two DFT databases. This card describes the Parquet tables in `parquet/`.
They are derived from the JSON files in `literature/`, `phase-diagrams/` and `hulls/` of the same release and add
nothing to them; the JSON stays the reference format.

- Release: **v2026.10** (version 2026.10; literature record store `orchid-literature 2026-10-22 (record store db-v2.1: invariant/general v2.1.19p, text+context fixup-20261022)`)
- Status: **Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.**
- Zenodo: four citable datasets plus the umbrella record *ORCHID data* (doi:10.5281/zenodo.PENDING-orchid-data): literature values (doi:10.5281/zenodo.PENDING-literature),
  calculated binary phase diagrams (doi:10.5281/zenodo.PENDING-phase-diagrams), binary convex hulls (doi:10.5281/zenodo.PENDING-hulls), DFT-vs-experiment formation-enthalpy
  benchmark (doi:10.5281/zenodo.PENDING-dft-benchmark)
- Homepage: <https://orchid-project.org> · data: <https://data.orchid-project.org>
- Field reference: `literature/SCHEMA.md`, hull format: `hulls/` (interval schema v1)
- Builder: `tools/build_parquet.py` in the `orchid-project.org` repository (deterministic, `--check`)

## Tables

| config | rows | content |
|---|---:|---|
| `literature_values` | 76,432 | one row per value read from a paper: property, value and unit, temperature, pressure, phases, compositions, reaction, evidence class, origin, flags, method, conditions, paper, cited sources, quote, model TDB link, ML split |
| `papers` | 4,877 | corpus papers (values were read from them) and cited works (a value was attributed to them) |
| `experimental_context` | 1,504 | samples, heat treatments and measurements of 225 papers, each with its quote and page |
| `dft_parity` | 7,826 | literature formation enthalpy × lowest-energy DFT entry at the same composition, one row per record and DFT source |
| `phase_diagram_invariants` | 24,828 | invariant equilibria of 2,720 calculated SGTE binary phase diagrams: T, phases, phase compositions |
| `phase_diagram_index` | 2,774 | one row per calculated diagram (2,720 `ok`, 54 `failed`), TDB file, SHA-256, citation |
| `hull_vertices` | 28,143 | binary convex-hull vertices: 12,829 Materials Project (v2026.04.13), 15,314 OQMD (v1.8) |

`parquet/MANIFEST.json` records for each table the row count, the Arrow schema, a content hash (SHA-256 of the
rows as canonical JSON, independent of the Parquet encoder) and the SHA-256 of every input file. All files are
zstd-compressed; `literature_values` is sorted by `system` (then `id`) in row groups of 8,192 rows, so a filter on
`system` reads only the row groups that hold it.

Units: temperatures in K, pressures in Pa, formation enthalpies and Gibbs energies of formation in kJ/mol-atom
(or `kJ/mol (basis unstated)`, see Limitations), DFT energies in eV/atom with a kJ/mol-atom column
(1 eV/atom = 96.485 kJ/mol-atom, the factor used throughout ORCHID). Compositions are mole fractions.

# Datasheet

Following *Datasheets for Datasets* (Gebru et al., 2021).

## Motivation

**Why was the dataset created?** CALPHAD assessments are fitted to experimental phase-equilibrium and
thermochemical data that are scattered across decades of papers, mostly in tables and sentences that no machine
reads. ORCHID collects those values with their full state (phases, temperature, pressure, composition, reference
state) and their provenance (paper, page, table row or sentence, cited original), so they can be found, compared
with models, and reused for assessment, benchmarking and machine learning. The calculated phase diagrams and DFT
hulls are published beside them as model and first-principles references for the same systems.

**Who created it and who funded it?** R. Arróyave (Texas A&M University), J. Saal (Citrine Informatics) and
D. Shin (Oak Ridge National Laboratory), as part of the ORCHID project.

## Composition

**What do the instances represent?** A row of `literature_values` is one value as an observation of an
equilibrium state: a quantity (`property`, e.g. `INVARIANT_TEMPERATURE`, `TRANSITION_TEMPERATURE`,
`PHASE_COMPOSITION`, `HM_FORM`, `CPM`, `LATTICE_A`) of a chemical `system`, with the phases involved, the
temperature and pressure at which it holds, phase compositions (`compositions`, a list of
`{phase, element, value, basis, source}`), and the reaction for invariants. There are 76,432 values from 1,322
papers covering 1,390 chemical systems (by number of elements: 519 unary, 55,884 binary, 16,578 ternary and
3,451 higher-order values), after merging 3,510 exact duplicates (`merged_ids`; see `literature/QUALITY_FIXES.md`).

**Evidence classes.** Every value carries one `evidence_class`, never mixed or averaged:
`experimental` (36,918), `model` (28,148: computed from a CALPHAD or other thermodynamic model), `dft` (6,162:
first-principles), `unspecified` (5,204: the paper does not let the origin be settled). `origin` records how the
class was decided; `origin_measured_in` the paper the value was measured or calculated in, which is often not the
paper it was read from (36,506 values are cited from another work; `conditions_kind = cited_source`).

**Labels and flags.** `accepted` (75,491 true) means the readers agreed and the deterministic checks passed.
`flag_*` columns are booleans (absent in the source = false; `flag_state_fully_specified` and
`flag_value_in_quote` are null where not evaluated). `review_flags` and `specification_gaps` list codes.
`plausibility_*` is a cross-check against a calculated phase diagram where one exists.

**Model links.** 13,586 `model` values are linked unambiguously to a TDB file of the ORCHID catalog
(`model_tdb`, `model_tdb_path`, `model_tdb_sha256`); `model_unlinked_reason` says why the others are not.

**Other tables.** `papers` is the bibliography for `paper_id`, `origin_measured_in` and `cited_dois`.
`experimental_context` lists sample preparation, heat treatments and measurement methods with their quotes; it
applies only to values whose origin is the paper's own experimental work (`conditions_kind = paper_context`).
`phase_diagram_*` are pycalphad 0.11.2 calculations from the SGTE binary collection (Hallstedt 2025), each tied to
its TDB by SHA-256; `x` is the mole fraction of `x_component`. `hull_vertices` are the stable phases of each binary
at 0 K; `x` is the mole fraction of `x_element`, `formation_energy_*` is relative to the source's elemental
references (`reference_kind`).

**Is anything missing?** The corpus is the set of papers that could be read, not all papers on a system;
coverage is uneven across systems. Values in figures are not included (tables and running text only). Fields not
printed in a value's quote were removed (`flag_has_dropped_fields`) rather than guessed.

**Confidential or personal data?** None. Author names appear only as bibliographic metadata.

## Collection process

**Readers.** Each table and passage was read independently by machine readers: the PDF text layer, Gemini Flash,
Claude Opus and, for confirmation or disagreement, Gemini Pro; a judge model chose between disagreeing readers in
198 cases. `reader_tier` and `readers` record which readings agreed: `preliminary_flash+claude` (62,292),
`confirmed_pro` (8,070), `preliminary_flash` (5,872, running text, with the second reader's verdict in
`flag_value_in_quote` / `second_reader`), `preliminary_flash+claude+fable_judge` (198). A value is accepted only
on reader agreement plus deterministic checks; `review_flags` lists the codes of checks that fired.

**Quote verification (running text).** A value read from a sentence is kept only if the sentence is verbatim on
one page of the PDF and the printed value lies inside it (`link_rule`). The sentence is stored in `quote` with
`quote_page`.

**Window rule.** Fields a reader returns that are not printed inside the quoted sentence or the table row (e.g. a
temperature or phase taken from elsewhere on the page) are dropped, counted in `dropped_field_count`, and not
published.

**PDF sign checks.** Formation enthalpies whose minus sign may have been lost in the text layer were checked
against the rendered page image. `flag_unsigned_in_print` marks values printed without a sign (magnitudes by the
paper's convention); `flag_sign_pdf_page_verified` marks a sign corrected from the page image.

**DFT parity.** `dft_parity` matches each literature `HM_FORM` in kJ/mol-atom (evidence class experimental, model
or unspecified) to the lowest-energy non-deprecated entry at exactly the same reduced composition in the Materials
Project and in OQMD, separately; the two are never averaged. `residual = DFT − literature`. `default_subset`
reproduces the published default (experimental, accepted, not unsigned, no sign loss, not magnitude-suspect):
MAE 10.9 kJ/mol-atom over 1,231 MP pairs (median 6.3, Spearman 0.83) and 9.6 over 1,294 OQMD pairs (median 5.5,
Spearman 0.88). Large residuals were classified deterministically (`quality_fix`; `literature/QUALITY_FIXES.md`):
per-formula values labelled per atom were converted (47), unsigned magnitudes flagged and excluded (31), the rest
flagged `dft_outlier_unexplained` (160) and kept.

**Kim et al. 2017 cross-check.** Accepted experimental formation enthalpies (kJ/mol-atom, signed) were compared per
formula with the experimental compilation of Kim, Meschel, Nash and Chen (Scientific Data 4 (2017) 170162):
162 formulas in common, MAE 3.85 kJ/mol-atom, median absolute difference 1.19, sign agreement 100 %, 19 formulas
differing by more than 10 kJ/mol-atom (listed with record ids in `literature/kim2017_crosscheck.md`).

**Timeframe.** Corpus papers published 1975–2025 (cited works back to the 19th century); reading done in 2026;
release v2026.10 built 2026-10-22.

## Preprocessing

Temperatures are converted to K (`temperature_printed` keeps the printed string), compositions in atomic or mass
percent to mole fraction (the `basis` of each composition says which), formation quantities to kJ/mol-atom when
the paper states the basis, and likewise mixing enthalpies, Gibbs energies of mixing and partial molar enthalpies
(kJ/mol-atom only with an explicit per-atom basis, otherwise `kJ/mol (basis unstated)`; `unit_basis` says how the
basis was established; `value_stored`/`unit_stored` and `value_printed`/`unit_printed` keep the earlier forms).
Exact duplicates are merged (`merged_ids`), reaction types and malformed property codes are mapped to controlled
vocabularies (raw values kept in `transition_kind_printed` and `property_code_raw`), and every correction is
listed with its evidence in `literature/QUALITY_FIXES.md`. For the Parquet tables only: nested JSON is flattened into typed columns; `temperature_bound` becomes
`bound` (`upper` for `<`, `lower` for `>`) and `temperature_bound_K`; `reference_state` is kept as a JSON string
(`reference_state_json`); `transition_kind` is the controlled reaction / transition class (see Known limitations); the
`split` column is added. Two corrupted `quote_page` values (non-page integers) are null with
`flag_page_unreadable`.

## Uses

**Intended uses.** Finding experimental data for a CALPHAD assessment; comparing assessed models with the data
they were fitted to; benchmarking DFT formation energies against calorimetry; training and evaluating models
for property prediction (tabular regression on formation enthalpy, invariant temperatures, phase compositions)
and for scientific information extraction (the quote, table caption and locator of each value give the
supervision signal; the source PDFs are not included).

**Recommended ML split.** `literature_values.split` assigns every paper to `train` / `validation` / `test`
deterministically: `sha256("orchid-split-v1:" + paper_id)`, first 8 bytes as an integer mod 100, `< 80` train,
`< 90` validation, else test. No paper spans two splits. This release: train 59,967 values (1,053 papers),
validation 7,527 (124 papers), test 8,938 (145 papers). Because many values are reprinted from earlier work,
the same measurement can appear under several papers; for strict leakage control also group by
`origin_measured_in` (or by `system` for extrapolation to unseen chemistries).

**Fine-tuning.** For extraction tasks, pair `quote` (running text) or `artifact_caption` + `table_row` with the
structured target (`property`, `value`, `unit`, `temperature_K`, `phases`, `compositions`), and restrict to
`accepted` rows. For regression, filter on `evidence_class` and `unit`, and drop placeholder uncertainties
(below).

**Uses to avoid.** Do not treat `model` or `unspecified` values as measurements, do not average across evidence
classes, and do not feed values to an optimizer (ESPEI etc.) without review: `flag_espei_ready`
(14,132 true, all of them accepted experimental or DFT values) comes from the extraction pipeline's automatic
completeness checks; it is not a review verdict.

## Distribution

Served at <https://data.orchid-project.org> from the `orchid-data` repository. Release v2026.10 is archived on
Zenodo as four datasets, each its own record and DOI, linked by the umbrella record *ORCHID data* (DataCite
`isPartOf` / `hasPart`); the deposition metadata and file manifests are in `zenodo/`, changes in `CHANGELOG.md`.
A Hugging Face mirror is planned (`hf/README.md` is this card in mirror form).

## Maintenance

Maintained by the ORCHID team. New releases rebuild the JSON and these tables together; `parquet/MANIFEST.json`
names the release and input hashes, and `tools/build_parquet.py --check` verifies that the Parquet files match
the JSON. Ids (`ORC-...`) are stable across releases; corrections are made in the record store and appear in the
next release. Report errors via the project website or repository issues.

## Known limitations

- **Per-formula vs per-atom.** 2,765 formation values have unit `kJ/mol (basis unstated)`: the paper does not say
  whether they are per mole of atoms or per formula unit, and they are not converted. Exclude them from per-atom
  analyses (`dft_parity` already does). A further 2,680 formation values are per atom only by the record builder's
  magnitude heuristic (`unit_basis = magnitude_heuristic`, `flag_basis_inferred_from_magnitude`).
- **Unsigned magnitudes.** Some papers print formation enthalpies without a minus sign by convention
  (`flag_unsigned_in_print`, 44 values; more found by the sign check in `dft_parity.sign_check`). The value is
  stored as printed.
- **Placeholder uncertainties.** Only `uncertainty_basis = printed` (3,742) or `printed_range` (23) is the
  source's own uncertainty. `stated_default` (23,133; e.g. "5% default") and `reading_resolution` (6,936) are ORCHID
  placeholders, not measured uncertainties. Most values have none.
- **Multi-system tables.** Some tables report many systems at once; values are assigned to the system of their
  row, and a record can carry up to 18 elements when the table's system could not be narrowed.
  `flag_system_mismatch` (495) marks rows whose phases or compositions do not fit the assigned system.
- **Evidence-class caveats.** `experimental` values cited from older work carry the citing paper's reading of
  them (`origin` says how the class was decided, e.g. `cited_work_before_1980_assumed_experimental`); `unspecified`
  values may be experimental or calculated. `flag_source_disputed` (512) and `flag_magnitude_suspect` (499) mark
  values to check before use.
- **Assumed conditions.** Pressure is usually `unstated_assumed` 1 atm; some temperatures are
  `assumed_room_temperature` or `assumed_standard_298K` (`temperature_basis`).
- **Vocabulary.** `transition_kind` (= `reaction_type`) is one of eutectic, peritectic, monotectic, syntectic,
  eutectoid, peritectoid, monotectoid, quasi-peritectic, congruent melting, congruent transformation, polymorphic,
  magnetic, order-disorder, critical point, metatectic/catatectic, other; the reading is in
  `transition_kind_printed` (187 variants). Liquidus / solidus points and ambiguous labels are `other`.
- **DFT.** MP and OQMD energies use different references and corrections and are not comparable to each other.
  OQMD formulas are written with spaces and explicit 1s (`Al3 Ni1`). Hulls are binary and at 0 K.
- **Calculated diagrams.** 54 SGTE files did not calculate (`phase_diagram_index.status = failed`); calculated
  invariants are as good as the grid and the assessment, and are model values, not measurements.

## Licence and citation

Derived data: **CC BY 4.0**. Cite the ORCHID dataset you use and the umbrella record (DOIs below), and the original
source of each value (`paper_citation`, `paper_doi`, `cited_dois`). Each `quote` is a single sentence reproduced
under fair use to make the value verifiable; the source papers, page images and full texts are not redistributed.
Third-party data keep their licences and citations (`NOTICE.md`, `LICENSES.md`): SGTE binary collection, Hallstedt
2025 (CC BY 4.0); Materials Project, Jain et al., APL Materials 1 (2013) 011002 (CC BY 4.0); OQMD, Saal et al., JOM
65 (2013) 1501 and Kirklin et al., npj Comput. Mater. 1 (2015) 15010 (CC BY 4.0).

The same citation is machine-readable everywhere: a top-level `cite_as` object (text, BibTeX, DOI) in
`literature/index.json`, every `literature/systems/*.json`, `phase-diagrams/index.json`, the hull catalogs,
`literature/dft_parity.json` and `parquet/MANIFEST.json`; `orchid.cite_as` / `orchid.doi` key-value metadata in every
Parquet file; `literature/CITATION.txt` beside the CSV; `CITATION.cff` at the top and in `literature/`,
`phase-diagrams/` and `hulls/`.

| dataset | Parquet tables | DOI |
|---|---|---|
| ORCHID literature values | `literature_values`, `papers`, `experimental_context` | 10.5281/zenodo.PENDING-literature |
| ORCHID calculated binary phase diagrams | `phase_diagram_index`, `phase_diagram_invariants` | 10.5281/zenodo.PENDING-phase-diagrams |
| ORCHID binary convex hulls (MP, OQMD, assessed CALPHAD) | `hull_vertices` | 10.5281/zenodo.PENDING-hulls |
| ORCHID DFT-vs-experiment formation-enthalpy benchmark | `dft_parity` | 10.5281/zenodo.PENDING-dft-benchmark |
| ORCHID data (umbrella) | all | 10.5281/zenodo.PENDING-orchid-data |

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

@misc{orchid_dft_benchmark_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID DFT-vs-experiment formation-enthalpy benchmark}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-dft-benchmark},
  url       = {https://doi.org/10.5281/zenodo.PENDING-dft-benchmark},
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

## How to load

Hugging Face `datasets` (from a local checkout or the mirror):

```python
from datasets import load_dataset
vals = load_dataset("parquet", data_files="parquet/literature_values.parquet", split="train")
train = vals.filter(lambda r: r["split"] == "train")
# from the mirror: load_dataset("<org>/orchid-data", "literature_values", split="full")
```

pandas:

```python
import pandas as pd
df = pd.read_parquet("parquet/literature_values.parquet",
                     filters=[("system", "==", "AL-NI")])          # row-group pruning on system
hf = df[(df.property == "HM_FORM") & (df.unit == "kJ/mol-atom")
        & (df.evidence_class == "experimental") & df.accepted & ~df.flag_unsigned_in_print]
comps = df.explode("compositions").dropna(subset=["compositions"])  # one row per phase x element
```

DuckDB SQL:

```sql
-- experimental invariant temperatures next to the calculated SGTE invariants of the same system
SELECT v.system, v.reaction, v.temperature_K AS T_lit, i.T_K AS T_calc, i.tdb
FROM 'parquet/literature_values.parquet' v
JOIN 'parquet/phase_diagram_invariants.parquet' i USING (system)
WHERE v.property = 'INVARIANT_TEMPERATURE' AND v.evidence_class = 'experimental' AND v.accepted
  AND abs(v.temperature_K - i.T_K) < 20;

-- DFT vs experiment, default subset, per source
SELECT dft_source, count(*) AS n, avg(abs(residual_kJ_per_mol_atom)) AS mae
FROM 'parquet/dft_parity.parquet' WHERE default_subset GROUP BY dft_source;

-- hull vertices of a binary from both DFT sources
SELECT source, formula, x, formation_energy_kJ_per_mol_atom, material_id
FROM 'parquet/hull_vertices.parquet' WHERE system = 'AL-NI' AND NOT is_endpoint ORDER BY source, x;

-- values with their paper's bibliographic record
SELECT v.id, v.property, v.value, v.unit, p.citation, p.year
FROM 'parquet/literature_values.parquet' v JOIN 'parquet/papers.parquet' p ON p.id = v.paper_id
WHERE v.system = 'CU-ZN' LIMIT 20;
```
