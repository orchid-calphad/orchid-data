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
- config_name: phases
  data_files:
  - split: full
    path: phases/registry.parquet
- config_name: structure_types
  data_files:
  - split: full
    path: phases/structure_types.parquet
- config_name: assessed_phase_assemblages
  data_files:
  - split: full
    path: assessed-phase-assemblages/records.parquet
- config_name: bibliography_papers
  data_files:
  - split: full
    path: bibliography/papers.parquet
- config_name: bibliography_edges
  data_files:
  - split: full
    path: bibliography/edges.parquet
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
  - name: sigma_printed
    dtype: float64
  - name: sigma_printed_kind
    dtype: string
  - name: sigma_reading
    dtype: float64
  - name: sigma_method
    dtype: float64
  - name: sigma_method_class
    dtype: string
  - name: sigma_method_basis
    dtype: string
  - name: sigma_method_n_pairs
    dtype: int32
  - name: sigma_method_floor
    dtype: float64
  - name: sigma_method_floor_unit
    dtype: string
  - name: sigma_composition
    dtype: float64
  - name: sigma_scatter
    dtype: float64
  - name: sigma_conversion
    dtype: float64
  - name: sigma_effective
    dtype: float64
  - name: sigma_unit
    dtype: string
  - name: sigma_rule
    dtype: string
  - name: uncertainty_calibration
    dtype: string
  - name: sigma_x_effective
    dtype: float64
  - name: sigma_x_method
    dtype: float64
  - name: sigma_x_method_class
    dtype: string
  - name: sigma_T_condition_effective
    dtype: float64
  - name: uncertainty_budget
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
  - name: flag_espei_certified
    dtype: bool
  - name: flag_espei_ready_upstream
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
  - name: calphad_check
    dtype: string
  - name: espei_certified_basis
    dtype: string
  - name: espei_phase_rule_result
    dtype: string
  - name: espei_phase_rule_reason
    dtype: string
  - name: espei_blocked_by
    list: string
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
  - name: reader_agreement
    dtype: string
  - name: reader_agreement_label
    dtype: string
  - name: tool_release
    dtype: string
  - name: release
    dtype: string
  - name: split
    dtype: string
  - name: chemical_system
    dtype: string
  - name: fold_lso
    dtype: int32
  - name: fold_lpo
    dtype: int32
  - name: plausibility_dx_json
    dtype: string
  - name: gate_failures
    list: string
  - name: corrections_json
    dtype: string
  - name: temperature_K_stored
    dtype: float64
  - name: system_stored
    dtype: string
  - name: evidence_class_before_gates
    dtype: string
  - name: property_code_before_gates
    dtype: string
  - name: reader_agreement_basis
    dtype: string
  - name: source_system
    dtype: string
  splits:
  - name: full
    num_examples: 73542
  download_size: 7557182
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
    num_examples: 4881
  download_size: 530861
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
  - name: chemical_system
    dtype: string
  - name: fold_lso
    dtype: int32
  - name: fold_lpo
    dtype: int32
  - name: ehull_upstream_kJ_per_mol_atom
    dtype: float64
  - name: dft_structure_match
    dtype: string
  - name: structure_designators
    list: string
  - name: dft_ground_state_id
    dtype: string
  - name: x_offset_measured
    dtype: float64
  - name: sigma_composition_kJ_per_mol_atom
    dtype: float64
  - name: excluded_from_default_by
    list: string
  splits:
  - name: full
    num_examples: 7592
  download_size: 290794
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
  - name: n_mapper_hits
    dtype: int32
  splits:
  - name: full
    num_examples: 15322
  download_size: 690948
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
  download_size: 263049
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
  download_size: 671299
- config_name: phases
  features:
  - name: id
    dtype: string
  - name: system
    dtype: string
  - name: preferred_name
    dtype: string
  - name: status
    dtype: string
  - name: structure_basis
    dtype: string
  - name: confidence
    dtype: string
  - name: structure_type
    dtype: string
  - name: prototype
    dtype: string
  - name: strukturbericht
    dtype: string
  - name: pearson
    dtype: string
  - name: space_group_number
    dtype: int32
  - name: space_group_symbol
    dtype: string
  - name: label
    dtype: string
  - name: tdb_names
    dtype: string
  - name: n_models
    dtype: int32
  - name: n_names
    dtype: int32
  - name: stoichiometry
    dtype: string
  - name: stable_T_min_K
    dtype: float64
  - name: stable_T_max_K
    dtype: float64
  - name: literature_values
    dtype: int32
  - name: literature_accepted_values
    dtype: int32
  - name: n_candidates
    dtype: int32
  - name: review_reasons
    dtype: string
  - name: references_first5
    dtype: string
  - name: total_papers
    dtype: int32
  - name: tdb_first_model
    dtype: string
  - name: tdb_phase_line
    dtype: string
  - name: tdb_constituent_line
    dtype: string
  splits:
  - name: full
    num_examples: 10430
  download_size: 452491
- config_name: structure_types
  features:
  - name: id
    dtype: string
  - name: prototype
    dtype: string
  - name: prototype_spellings
    dtype: string
  - name: strukturbericht
    dtype: string
  - name: pearson
    dtype: string
  - name: space_group_number
    dtype: int32
  - name: space_group_symbol
    dtype: string
  - name: stoichiometry
    dtype: string
  - name: verification
    dtype: string
  - name: registry_phases
    dtype: int32
  - name: n_sources
    dtype: int32
  - name: source_citations
    dtype: string
  - name: source_dois
    dtype: string
  splits:
  - name: full
    num_examples: 1563
  download_size: 53103
- config_name: assessed_phase_assemblages
  features:
  - name: id
    dtype: string
  - name: system
    dtype: string
  - name: diagram
    dtype: string
  - name: field
    dtype: int32
  - name: assemblage_label
    dtype: string
  - name: n_phases
    dtype: int32
  - name: phase_labels
    dtype: string
  - name: canonical_names
    dtype: string
  - name: phase_ids
    dtype: string
  - name: T_K
    dtype: float64
  - name: T_C
    dtype: float64
  - name: x
    dtype: float64
  - name: x_component
    dtype: string
  - name: P_Pa
    dtype: float64
  - name: u_T_K
    dtype: float64
  - name: u_x
    dtype: float64
  - name: point_method
    dtype: string
  - name: margin_normalized
    dtype: float64
  - name: margin_isotherm_x
    dtype: float64
  - name: margin_isopleth_K
    dtype: float64
  - name: boundary_basis
    dtype: string
  - name: basis
    dtype: string
  - name: chemical_system
    dtype: string
  - name: paper_id
    dtype: string
  - name: fold_lso
    dtype: int32
  - name: fold_lpo
    dtype: int32
  - name: confidence
    dtype: string
  - name: review_state
    dtype: string
  - name: flags
    dtype: string
  - name: tie_line_x_left
    dtype: float64
  - name: tie_line_phase_left
    dtype: string
  - name: tie_line_x_right
    dtype: float64
  - name: tie_line_phase_right
    dtype: string
  - name: tie_line_omitted
    dtype: string
  - name: sgte_n
    dtype: int32
  - name: sgte_agrees
    dtype: int32
  - name: sgte_disagrees
    dtype: int32
  - name: sgte_not_comparable
    dtype: int32
  - name: sgte_results
    dtype: string
  - name: original_citation
    dtype: string
  - name: original_doi
    dtype: string
  - name: handbook_page_pdf
    dtype: int32
  - name: evidence_class
    dtype: string
  - name: sigma_T_reading_K
    dtype: float64
  - name: sigma_x_reading
    dtype: float64
  - name: sigma_T_method_K
    dtype: float64
  - name: sigma_x_method
    dtype: float64
  - name: sigma_T_effective_K
    dtype: float64
  - name: sigma_x_effective
    dtype: float64
  splits:
  - name: full
    num_examples: 23129
  download_size: 1721874
- config_name: bibliography_papers
  features:
  - name: id
    dtype: string
  - name: key
    dtype: string
  - name: doi
    dtype: string
  - name: no_doi
    dtype: bool
  - name: title
    dtype: string
  - name: authors
    dtype: string
  - name: orcids
    dtype: string
  - name: container_title
    dtype: string
  - name: volume
    dtype: string
  - name: issue
    dtype: string
  - name: pages
    dtype: string
  - name: year
    dtype: int64
  - name: publisher
    dtype: string
  - name: type
    dtype: string
  - name: metadata_source
    dtype: string
  - name: citation
    dtype: string
  - name: systems
    dtype: string
  - name: roles
    dtype: string
  - name: tdb_files
    dtype: string
  - name: handbook_systems
    dtype: string
  - name: discovery_rank
    dtype: int64
  - name: values_reported
    dtype: int64
  - name: values_reported_accepted
    dtype: int64
  - name: values_reported_experimental
    dtype: int64
  - name: values_reported_model
    dtype: int64
  - name: values_reported_dft
    dtype: int64
  - name: values_reported_unspecified
    dtype: int64
  - name: values_cited
    dtype: int64
  - name: values_cited_accepted
    dtype: int64
  - name: property_groups
    dtype: string
  - name: properties
    dtype: string
  - name: n_tables
    dtype: int64
  - name: n_text_passages
    dtype: int64
  - name: n_espei_datasets
    dtype: int64
  - name: n_phase_registry_phases
    dtype: int64
  - name: n_assessed_assemblage_records
    dtype: int64
  - name: open_access_license
    dtype: string
  - name: license_urls
    dtype: string
  - name: is_referenced_by_count
    dtype: int64
  - name: is_referenced_by_count_retrieved
    dtype: string
  - name: crossref_status
    dtype: string
  - name: doi_match
    dtype: string
  - name: read_by_orchid
    dtype: string
  - name: edges_out
    dtype: int64
  - name: edges_in
    dtype: int64
  - name: json_url
    dtype: string
  - name: html_url
    dtype: string
  splits:
  - name: full
    num_examples: 9569
  download_size: 1539815
- config_name: bibliography_edges
  features:
  - name: id
    dtype: string
  - name: type
    dtype: string
  - name: src
    dtype: string
  - name: dst
    dtype: string
  - name: src_kind
    dtype: string
  - name: dst_kind
    dtype: string
  - name: count
    dtype: int64
  - name: provenance_source
    dtype: string
  - name: provenance_dataset
    dtype: string
  - name: provenance_method
    dtype: string
  - name: systems
    dtype: string
  - name: attrs
    dtype: string
  splits:
  - name: full
    num_examples: 60231
  download_size: 1084933
---

# ORCHID data: analysis-ready tables

**ORCHID** (Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery) publishes thermodynamic and
phase-equilibrium values read from published papers, binary phase diagrams calculated from assessed CALPHAD
databases, binary convex hulls from two DFT databases, and a registry of the phases of every binary system. This card
describes the Parquet tables in `parquet/` and `phases/`. They are derived from the JSON files in `literature/`,
`phase-diagrams/`, `hulls/` and `phases/` of the same release and add nothing to them; the JSON stays the reference
format.

- Release: **v2026.10** (version 2026.10; literature record store `orchid-literature 2026-10-23 (record store db-v2.1: invariant/general v2.1.19r, text+context fixup-20261022)`)
- Status: **Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.**
- Zenodo: eight citable datasets plus the umbrella record *ORCHID data* (doi:10.5281/zenodo.PENDING-orchid-data): literature values (doi:10.5281/zenodo.PENDING-literature),
  calculated binary phase diagrams (doi:10.5281/zenodo.PENDING-phase-diagrams), binary convex hulls (doi:10.5281/zenodo.PENDING-hulls), DFT-vs-experiment formation-enthalpy
  benchmark (doi:10.5281/zenodo.PENDING-dft-benchmark), phase registry (binary systems)
  (doi:10.5281/zenodo.PENDING-phase-registry), assessed phase assemblages (binary systems)
  (doi:10.5281/zenodo.PENDING-assessed-phase-assemblages), ESPEI datasets from the literature
  (doi:10.5281/zenodo.PENDING-espei), bibliography (doi:10.5281/zenodo.PENDING-bibliography)
- Homepage: <https://orchid-project.org> · data: <https://data.orchid-project.org>
- Field reference: `literature/SCHEMA.md`, hull format: `hulls/` (interval schema v1)
- Builder: `tools/build_parquet.py` in the `orchid-project.org` repository (deterministic, `--check`); the
  `phases` and `structure_types` tables: `tools/build_phase_registry.py` (deterministic, `--check`; field reference
  `phases/SCHEMA.md`); the `assessed_phase_assemblages` table: `tools/build_assessed_assemblages.py` (deterministic,
  `--check`; field reference `assessed-phase-assemblages/SCHEMA.md`); the `bibliography_papers` and
  `bibliography_edges` tables: `tools/build_bibliography.py` (deterministic, `--check`; field reference
  `bibliography/SCHEMA.md`)

## Tables

| config | rows | content |
|---|---:|---|
| `literature_values` | 73,538 | one row per value read from a paper: property, value and unit, temperature, pressure, phases, compositions, reaction, evidence class, origin, flags, method, conditions, paper, cited sources, quote, model TDB link, uncertainty budget (`sigma_*` columns), ML split |
| `papers` | 4,880 | corpus papers (values were read from them) and cited works (a value was attributed to them) |
| `experimental_context` | 1,504 | samples, heat treatments and measurements of 225 papers, each with its quote and page |
| `dft_parity` | 7,696 | literature formation enthalpy × lowest-energy DFT entry at the same composition, one row per record and DFT source |
| `phase_diagram_invariants` | 15,322 | distinct invariant equilibria of 2,720 calculated SGTE binary phase diagrams: T, phases, phase compositions; `n_mapper_hits` = how often the mapper found it (the JSON files list all 24,828 hits) |
| `phase_diagram_index` | 2,774 | one row per calculated diagram (2,720 `ok`, 54 `failed`), TDB file, SHA-256, citation |
| `hull_vertices` | 28,143 | binary convex-hull vertices: 12,829 Materials Project (v2026.04.13), 15,314 OQMD (v1.8) |
| `phases` | 10,496 | phase registry: one row per phase of each of 1,241 binary systems (`phases/registry.parquet`) |
| `assessed_phase_assemblages` | 23,131 | one (T, x, P) point deep inside each named phase field of the expert-drawn (assessed) binary diagrams compiled in Okamoto's Desk Handbook, with the assemblage, registry ids, basis, confidence and SGTE cross-check (`assessed-phase-assemblages/records.parquet`) |
| `bibliography_papers` | 9,569 | every paper ORCHID knows: Crossref metadata, roles, value counts, DOI check (`bibliography/papers.parquet`) |
| `bibliography_edges` | 60,231 | typed relations between papers, TDB files and handbook diagrams, with provenance (`bibliography/edges.parquet`) |
| `structure_types` | 1,563 | structure types used by the registry: prototype, Strukturbericht, Pearson symbol, space group, sources (`phases/structure_types.parquet`) |

### Uncertainty budget (`literature_values.sigma_*`, `uncertainty_budget`)

Every value carries an uncertainty budget (PI decision 2026-10-24), with the components kept separate so that
users can recombine them; printed values and printed uncertainties are never altered. In the literature JSON
(`literature/SCHEMA.md`, field `uncertainty_budget`) each record has one budget per measured quantity (`value`; the
printed phase `composition`; the equilibration `temperature_K` of phase-composition / assemblage observations);
the Parquet table flattens the value quantity into typed columns and keeps the full budget as JSON:

| column | meaning (unit: `sigma_unit`, the value's unit) |
|---|---|
| `sigma_printed`, `sigma_printed_kind` | uncertainty as printed by the source (null if none; ORCHID placeholders `stated_default` / `reading_resolution` are not printed sigmas); kind: `plus_minus_coverage_not_stated` (taken as 1 sigma), `range_half_width`, `standard_deviation`, `standard_error` |
| `sigma_reading` | half of the last printed digit |
| `sigma_method`, `sigma_method_class`, `sigma_method_basis`, `sigma_method_n_pairs`, `sigma_method_floor`, `sigma_method_floor_unit` | method-class systematic component: the robust between-study scatter of independent measurements of the same state by the same method class in ORCHID (`calibrated`, n pairs), , max(prior, cleaned robust sigma) below the calibration threshold (`cleaned_below_threshold`), or a documented prior (`prior`); DFT values: the calibrated sigma_DFT; model-calculated values: the model class's robust deviation from experiment (`calibrated`) or a prior. `sigma_method_floor` is in the calibration's canonical unit (`sigma_method_floor_unit`, e.g. kJ/mol-atom, K, mole fraction, or relative) |
| `sigma_composition` | attribution / composition offset (value measured at a historical formula of the phase: \|dx\| x hull slope) |
| `sigma_scatter` | between-study scatter of a page-checked mutually inconsistent group |
| `sigma_conversion` | reference-state / unit conversion contribution (e.g. a lattice-stability conversion) |
| `sigma_effective` | max( sqrt( max(printed, reading, method)^2 + composition^2 + conversion^2 ), scatter ): the recommended sigma (`sigma_rule`) |
| `uncertainty_calibration` | calibration version and SHA-256 prefix of `literature/UNCERTAINTY_CALIBRATION.json` |
| `sigma_x_effective`, `sigma_x_method`, `sigma_x_method_class` | the same for the row's phase compositions (mole fraction) |
| `sigma_T_condition_effective` | the same for the equilibration temperature of a phase-composition / assemblage row (K) |
| `uncertainty_budget` | the full budget (JSON string) |

Rule: the method floor is a between-study scatter and already contains each study's statistical error, so it is
not added to the printed sigma in quadrature (no double counting); the larger is used. Composition offset and
conversion are independent and added in quadrature; a group scatter replaces the result when larger. Method floors
(`literature/UNCERTAINTY_CALIBRATION.md`): for each value type and method class, independent measurements of the
same state from different primary sources (one value per source, re-listings counted once), robust sigma =
1.4826 x state-weighted median |d| / sqrt(2), 95 % bootstrap CI over states; floor = that sigma rounded up and never
below ESPEI's experimental default for energies, entropies and activities (0.5 kJ/mol, 0.2 J/K/mol); classes with
fewer than 20 pairs or 10 states but at least 5 independent pairs from 3 states take max(documented prior, cleaned
robust sigma) (`cleaned_below_threshold`, n and CI recorded); the others use a documented prior. The ESPEI bundle (`espei/`) weights its datasets by
`sigma_effective` by default and carries the components per value (`orchid_uncertainty.values[].budget`;
calibration copy `espei/experimental/CALIBRATION_EXPERIMENT.json`).

### Phase registry tables (`phases`, `structure_types`)

A structure type is given only when certain:

- **Tier A** (`structure_basis = standard_name`): the TDB phase name encodes one structure (FCC_A1, BCC_B2, L12_FCC,
  SIGMA, ...), and the model's stoichiometry and sublattices and the DFT ground state do not contradict it.
- **Tier B** (`dft_unique_match`, "DFT-supported"): a stoichiometric compound whose composition matches exactly one
  on-hull entry in both Materials Project and OQMD, with the same space group, one structure type for that space group
  and stoichiometry, and no other phase of the system at that composition.
- **Tier C** (`assessment_declared`, confidence `assessor-stated`): the Hallstedt 2025 crystallographic table of the
  SGTE collection (CC BY 4.0) gives exactly one structure for this phase name and system, tiers A/B do not contradict
  it, and every model's composition or site ratio equals the listed compound.
- `liquid`, `gas`: no prototype. Everything else has `status = needs_review` with candidates (in the JSON), or
  `unresolved_no_candidates`.

`phases` columns: `id` (`phase:<sorted lower-case elements>:<slug>`), `system`, `preferred_name` (TDB name used by most
assessments), `status`, `structure_basis` (tier, above), `confidence`, `structure_type` (id in `structure_types`),
`prototype`, `strukturbericht`, `pearson`, `space_group_number`, `space_group_symbol`, `label`, `tdb_names`
(`;`-joined TDB phase names), `n_models` (TDB phase declarations), `n_names` (names in all namespaces: TDB, paper
labels, corpus ids, MP, OQMD), `stoichiometry` (`EL:x;...` when every model is stoichiometric and they agree),
`stable_T_min_K` / `stable_T_max_K` (range over the calculated diagrams where the phase is stable), `literature_values`,
`literature_accepted_values`, `n_candidates`, `review_reasons` (`;`-joined), `references_first5` (DOIs, assessments
first), `total_papers`, `tdb_first_model`, `tdb_phase_line`, `tdb_constituent_line` (file and verbatim PHASE /
CONSTITUENT statements of the first model). The complete records (every name, every model with its verbatim TDB
definition, stability per diagram, references) are in `phases/systems/<SYS>.json`.

### Assessed phase assemblages (`assessed_phase_assemblages`)

Evidence class `assessed_phase_diagram`: an expert drew the diagram from experimental evidence without a CALPHAD
model; these rows are neither measurements nor model values. One row per named phase field: the field's area centroid
(or its pole of inaccessibility when the centroid is not safely inside), so the assemblage claim does not depend on
exactly where the boundaries were drawn. `T_K`, `x` (mole fraction of `x_component`), `P_Pa` (1 atm assumed),
`u_T_K` / `u_x` (bounds from the axis calibration), `phase_labels` (as printed), `canonical_names`, `phase_ids`
(phase-registry ids; empty when unmapped), `basis`, `confidence`, `review_state`, `margin_*` (distance to the nearest
drawn line: drawing-based, low credence), `tie_line_*` (two-phase rows only, drawing-based, weak constraint),
`sgte_*` (agreement with the calculated SGTE diagrams of the system), `original_citation` / `original_doi` (cite
first) and `handbook_page_pdf`. Full records, exclusions and ESPEI ZPF datasets are in `assessed-phase-assemblages/`
(field reference `SCHEMA.md` there).

### Bibliography tables (`bibliography_papers`, `bibliography_edges`)

`bibliography_papers`: one row per paper (stable `id`: `doi:<doi>` or `nodoi:<hash>`), Crossref metadata, roles,
value counts; `bibliography_edges`: one row per typed relation (stable `id`), `src`/`dst` paper ids, provenance.
Join edges to papers on `src`/`dst` = `id`. `doi_match` grades DOIs that upstream matchers found for printed
references (`verified`, `weak`, `unverifiable`); mismatched DOIs were dropped and are listed in
`bibliography/DOI_MISMATCHES.md`. Licence: Crossref metadata CC0, ORCHID fields CC BY 4.0. Column descriptions:
`bibliography/SCHEMA.md` and `bibliography/parquet.json`.

`structure_types` columns: `id`, `prototype`, `prototype_spellings` (`;`), `strukturbericht`, `pearson`,
`space_group_number`, `space_group_symbol`, `stoichiometry`, `verification` (which source confirms the row),
`registry_phases` (phases assigned this type), `n_sources`, `source_citations` (` | `-joined), `source_dois` (`;`).

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
`{phase, element, value, basis, source}`), and the reaction for invariants. There are 73,538 values from 1,321
papers covering 1,405 chemical systems (by number of elements: 792 unary, 53,378 binary, 16,342 ternary and
3,026 higher-order values), after merging 3,550 exact duplicates and 4,002 cosmetic duplicates (an UNKNOWN or
missing phase beside a named one, the liquid printed as L or liquid, glyph variants; `merged_ids`; see
`literature/QUALITY_FIXES.md` sections 1 and 7). 72,359 values are accepted. The literature-level consistency gates
(`literature/QUALITY_FIXES.md` section 7) corrected 4,060 values (2,303 of them only to the standard reference temperature: a printed 298 K is
stored as 298.15 K) where the evidence was printed and confirmed on the PDF page (table temperature units, J/kJ scales, signs under printed headings, system assignment, property codes;
the stored value is kept and `corrections` names the rule and the visual check) and demoted or flagged 1,988
(`gate_failures`).

**Evidence classes.** Every value carries one `evidence_class`, never mixed or averaged:
`experimental` (36,268), `model` (26,214: computed from a CALPHAD or other thermodynamic model), `dft` (5,807:
first-principles), `unspecified` (5,249: the paper does not let the origin be settled). `origin` records how the
class was decided; `origin_measured_in` the paper the value was measured or calculated in, which is often not the
paper it was read from (34,988 values are cited from another work; `conditions_kind = cited_source`).

**Labels and flags.** `accepted` (72,359 true) means the readers agreed and the deterministic checks passed.
`flag_*` columns are booleans (absent in the source = false; `flag_state_fully_specified` and
`flag_value_in_quote` are null where not evaluated). `review_flags` and `specification_gaps` list codes.
`plausibility_*` is a cross-check against a calculated phase diagram where one exists.

**Model links.** 12,832 `model` values are linked unambiguously to a TDB file of the ORCHID catalog
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
198 cases. `readers` records which readings agree; `reader_tier` is the pipeline status of the table or passage (which reader
passes ran), not an agreement claim: `preliminary_flash+claude` (59,431),
`confirmed_pro` (8,053), `preliminary_flash` (5,856 running text, with the second reader's verdict in
`flag_value_in_quote` / `second_reader`), `preliminary_flash+claude+fable_judge` (198). A value is accepted only
on reader agreement plus deterministic checks; `review_flags` lists the codes of checks that fired.

**Reader agreement (tables).** `reader_agreement` says how many independent visual readers carry a table value:
`multi_reader` ("confirmed (two or more readers)"), `single_reader` ("unconfirmed (single reader)": one visual reader
read the row and no second reader has confirmed it yet; the data explorer shows a "single reader" badge) or
`single_reader_text_layer` (one visual reader, every value also printed in the PDF text layer); the human label is in
`reader_agreement_label`. A blind, independent second Claude read is listed as `claude-opus-5.5#2` in `readers` and
counts as a second reader. Treat `single_reader` values as unconfirmed. Where the record builder did not classify a value (invariant tables, running text), `reader_agreement` is derived from `readers` (`reader_agreement_basis = derived_from_readers`, settled rows only): multi_reader 69,249, single_reader_text_layer 2,547, single_reader 1,342, not classified 400.

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
Project and in OQMD, separately; the two are never averaged. When the record names a structure (Strukturbericht
designator or prototype in the printed label, or the mapped model phase of the same compound), the lowest entry of
that space group is used (`dft_structure_match` = exact; `dft_ground_state_id` when it is not the ground state), and
a record whose structure has no entry is `structure_unmatched` (paired with the ground state, outside the default).
`ehull_kJ_per_mol_atom` is computed from ORCHID's own released hull (`hulls/dft-*`); the provider's value is kept in
`ehull_upstream_kJ_per_mol_atom`. A measured composition off the compound (`x_offset_measured`) adds
`sigma_composition_kJ_per_mol_atom` = |dx| x hull slope, and |dx| > 0.02 leaves the default subset
(`excluded_from_default_by`). `residual = DFT − literature`. `default_subset` (experimental, accepted, not unsigned,
no sign loss, not magnitude-suspect, structure matched or not named, on-stoichiometry): MAE 10.4 kJ/mol-atom over
1,181 MP pairs (median 6.2, Spearman 0.85) and 9.1 over 1,222 OQMD pairs (median 5.3, Spearman 0.90). Per-formula vs
per-atom bases are decided from the printed column or caption only (audit round 2; the earlier conversion that was
accepted when the converted value agreed with DFT is withdrawn). `chemical_system`, `fold_lso` and `fold_lpo` are
those of the literature record with the same `record_id`.

**Kim et al. 2017 cross-check.** Accepted experimental formation enthalpies (kJ/mol-atom, signed) were compared per
formula with the experimental compilation of Kim, Meschel, Nash and Chen (Scientific Data 4 (2017) 170162):
162 formulas in common, MAE 3.87 kJ/mol-atom, median absolute difference 1.19, sign agreement 100 %, 19 formulas
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
`< 90` validation, else test. No paper spans two splits. This release: train 57,933 values (1,052 papers),
validation 7,133 (124 papers), test 8,472 (145 papers). Because many values are reprinted from earlier work,
the same measurement can appear under several papers; for strict leakage control also group by
`origin_measured_in` (or by `system` for extrapolation to unseen chemistries).

**Fine-tuning.** For extraction tasks, pair `quote` (running text) or `artifact_caption` + `table_row` with the
structured target (`property`, `value`, `unit`, `temperature_K`, `phases`, `compositions`), and restrict to
`accepted` rows. For regression, filter on `evidence_class` and `unit`, drop placeholder uncertainties
(below) and weight by `sigma_effective`.

**Uses to avoid.** Do not treat `model` or `unspecified` values as measurements, do not average across evidence
classes, and do not feed values to an optimizer (ESPEI etc.) without review: `flag_espei_ready`
(11,928 true) means the value can be used in ESPEI: the pipeline's completeness and format checks plus the physical
phase rule (printed phase mapped to a model phase, physically possible at its temperature; literature/QUALITY_FIXES.md
section 6). `flag_espei_certified` (1,917 true) adds agreement with a pycalphad calculation from the linked TDB
(`calphad_check`: agrees / disagrees / not_available; 323 ready values disagree, 9,679 have no prediction). Neither
is a review verdict.

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

- **Per-formula vs per-atom.** 2,494 formation values have unit `kJ/mol (basis unstated)`: the paper does not say
  whether they are per mole of atoms or per formula unit, and they are not converted. Exclude them from per-atom
  analyses (`dft_parity` already does). A further 2,238 formation values are per atom only by the record builder's
  magnitude heuristic (`unit_basis = magnitude_heuristic`, `flag_basis_inferred_from_magnitude`).
- **Unsigned magnitudes.** Some papers print formation enthalpies without a minus sign by convention
  (`flag_unsigned_in_print`, 44 values; more found by the sign check in `dft_parity.sign_check`). The value is
  stored as printed.
- **Placeholder uncertainties.** Only `uncertainty_basis = printed` (3,306) or `printed_range` (16) is the
  source's own uncertainty. `stated_default` (20,874; e.g. "5% default") and `reading_resolution` (7,480) are ORCHID
  placeholders, not measured uncertainties. Most values have none. Use `sigma_effective` (uncertainty budget, above): it is defined for
  every value with a convertible unit, never uses a placeholder, and is never below the method-class floor.
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

## Machine-learning use

Every literature value (`literature_values`), every DFT parity row (`dft_parity`) and every assessed phase-assemblage
point (`assessed_phase_assemblages`) carries two deterministic 5-fold assignments, as columns (the Hugging Face configs
keep a single `full` split; select folds with a filter):

- `fold_lso` (leave-chemical-system-out) = int(sha256(`chemical_system`), 16) mod 5, where `chemical_system` is the
  sorted, upper-case, `-`-joined element string (e.g. `AL-NI`) of the record's own state: a binary compound or a pure
  element reported in a ternary paper is filed under its binary or unary system, and the paper's system is kept in
  `source_system` (audit round 2);
- `fold_lpo` (leave-paper-out) = int(sha256(`paper_id`), 16) mod 5, where `paper_id` is the stable source id
  (`doi:<doi>` or `sha256:<pdf prefix>`; assessed points: the original evaluation, else `handbook:<diagram>`).

```python
from datasets import load_dataset
ds = load_dataset("<this repo>", "literature_values", split="full")
test = ds.filter(lambda r: r["fold_lso"] == 0)          # unseen chemical systems
train = ds.filter(lambda r: r["fold_lso"] != 0)
```

**Leakage.** A random row split leaks: values from one table, one paper or one system are strongly correlated, and
many values are re-listed by several papers from the same original measurement (`cited_dois`). Use `fold_lpo` to test
on unseen papers and `fold_lso` to test on unseen chemistry. The system fold is keyed on the exact system: unary and
lower-order subsystems are systems of their own, so a held-out ternary A-B-C may have its A-B binary in training; for
strict extrapolation drop from training every record whose system is a subsystem of a held-out system. Even
`fold_lpo` does not separate re-listed measurements: drop training rows that share a `cited_dois` entry with a test
row when that matters. The older `split` column (train / validation / test by paper, 80/10/10) is kept unchanged.

## Licence and citation

ORCHID's data are released under **CC BY 4.0**, as are the SGTE (Hallstedt 2025), Materials Project and OQMD data
from which they are derived. Cite the ORCHID dataset you use and the umbrella record (DOIs below), and the original
source of each value (`paper_citation`, `paper_doi`, `cited_dois`). The quotations from papers (`quote`) are short
excerpts kept for verification; they remain under the publishers' copyright and are not relicensed. The source
papers, page images and full texts are not redistributed. The assessed phase-assemblage points are ORCHID's own
measurements of where the phase fields of the handbook diagrams lie (T, x, P and phase names, with citations); no
handbook drawing or text is included. Third-party sources, citations and statements of changes are in `NOTICE.md`,
the licence of each folder in `LICENSES.md`: SGTE binary collection, Hallstedt, Calphad 89 (2025) 102833 (CC BY 4.0);
Materials Project, Jain et al., APL Materials 1 (2013) 011002 (CC BY 4.0); OQMD, Saal et al., JOM 65 (2013) 1501 and
Kirklin et al., npj Comput. Mater. 1 (2015) 15010 (CC BY 4.0); Kim et al. 2017 experimental formation enthalpies
(Figshare 10.6084/m9.figshare.7289723, MIT; used in the DFT benchmark cross-check); Crossref bibliographic metadata
CC0; ORCHID-derived bibliography fields CC BY 4.0.

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
| ORCHID phase registry (binary systems) | `phases`, `structure_types` | 10.5281/zenodo.PENDING-phase-registry |
| ORCHID assessed phase assemblages (binary systems) | `assessed_phase_assemblages` | 10.5281/zenodo.PENDING-assessed-phase-assemblages |
| ORCHID ESPEI datasets from the literature | (ESPEI JSON in `espei/`; no Parquet table) | 10.5281/zenodo.PENDING-espei |
| ORCHID bibliography | `bibliography_papers`, `bibliography_edges` | 10.5281/zenodo.PENDING-bibliography |
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
