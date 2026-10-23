# ORCHID ESPEI bundle: schema

## Layout

- `experimental/<SYS>/<source>.<file>.json`, `model/<SYS>/...`, `invariants/<SYS>/...`: corpus datasets.
  `<SYS>`: elements sorted, uppercase, joined by `-` (as in `literature/`); `<source>`: the corpus folder the dataset
  was written in (the assessment / TDB it was mapped through); `<file>`: the corpus file name.
- `dft/<literature|mp|oqmd>/<SYS>/<TDB stem>.<PHASE>.json`: DFT formation enthalpies of endmembers of one phase of one
  TDB file (`solver` datasets, output `HM_FORM`, T = 298.15 K, P = 101325 Pa).
- `dft/CALIBRATION.json|md`: DFT sigma calibration.

## Dataset files (ESPEI 0.9.1 format)

ESPEI-native keys: `components`, `phases`, `conditions` (`P` Pa, `T` K, `X_<EL>` mole fractions), `output`, `values`
(J/mol-atom, J/mol-atom/K, activities; ZPF: `[phase, [components], [mole fractions]]` per vertex, `null` where not
printed), `reference_states` (or `reference_state` for activities), `solver` (DFT: `mode`, `sublattice_site_ratios`
and `sublattice_configurations` exactly as in the TDB phase model), `tags`, `weight` (scalar for equilibrium and
activity datasets; one per value for DFT `solver` datasets; absent = 1). Values removed by the inclusion gate are cut
from `values` and the matching `conditions` entries.

| key | meaning |
|---|---|
| `reference` | source paper(s) of the values (where measured / calculated): `Author Year, doi:...`; DFT databases by name and release |
| `bibtex` | BibTeX key(s) in `references.bib` (space-separated when several) |
| `comment` | literature: `ORCHID literature values, Version 1, machine-extracted. Evidence class: <class>. ORCHID observation ids (...): ORC-...`; DFT: `0 K DFT used as 298.15 K enthalpy. ...` with TDB, SHA-256, phase, ids and the eV conversion |
| `orchid.evidence_class` | `experimental`, `model` or `dft` |
| `orchid.observations[]` | per value, in order: `id` (ORCHID literature id), `reader_agreement` (`multi_reader`, `single_reader`, `single_reader_text_layer`; absent when not classified), `paper`, `measured_in`, `caveats` |
| `orchid.papers`, `orchid.dois` | paper ids (`literature/papers.json`) and DOIs involved: source, containing paper, printed cited works |
| `orchid.source_dataset`, `orchid.values_dropped`, `orchid.espei_evaluation` | corpus file; values removed by the gate; invariant ZPF driving forces against the assessment |
| `orchid.dft_source`, `orchid.tdb`, `orchid.registry_phase`, `orchid.mapping[]` | DFT: source; TDB file (name, path, SHA-256, phase); phase-registry id; per value: id (MP / OQMD entry or ORCHID id), compound, mapping basis, space group, match quality |
| `orchid_value_bases` | ZPF from ranges / central values: how a temperature was derived, keyed by ORCHID id |
| `orchid_model_evidence` | model datasets: `tdb` (name, path, SHA-256, catalog entry), `link_basis`, `model_citation`, `model_reproduction` |
| `orchid_uncertainty` | see below |

## Uncertainties (`orchid_uncertainty`)

`{unit, default_sigma {value, name}, weight_rule, values[]}`, one entry per value in value order:

| field | meaning |
|---|---|
| `sigma` | the value's standard uncertainty in the dataset's units (`unit`), or `null` when none is available (never invented) |
| `sigma_basis` | `printed`; `dft_calibrated`; `espei_default_experimental (assumed, not printed)`; `none (...)` with the reason (model-calculated; no ESPEI default); `zpf (...)` |
| `printed` | `{value, unit, interval, coverage, lower?, upper?, note?}`: printed uncertainty as published (`coverage`: `1sigma_assumed` for a bare ±x, `range_half_width` for a printed range) |
| `sigma_printed`, `sigma_assumed` | for experimental values without a printed uncertainty: `null` and ESPEI's experimental default (or `null` where ESPEI has none) |
| `sigma_mu_J_per_mol` | activities: R T sigma_a / a, the chemical-potential sigma ESPEI's activity residual uses |
| `calibration` | DFT: `{source, stratum, used (stratum or source_level), leave_system_out, system_left_out, n, sigma_robust_kJ, bias_median_kJ_not_applied, ci95_sigma_robust_kJ_full_stratum, n_full_stratum}` |
| `temperature_sigma_K`, `temperature_sigma_basis` | ZPF: printed temperature uncertainty |
| `weight_used` | the ESPEI weight that applies to this value; `weight_per_value_equivalent` = default sigma / this value's sigma |
| `printed_uncertainty_not_used` | model-calculated values: a printed uncertainty kept as printed, not used |

Caveat codes (published flags of the value): `magnitude_suspect`, `system_mismatch`, `source_disputed`,
`dft_outlier_unexplained`, `basis_inferred_from_magnitude`, `basis_corrected_from_formula`, `sign_from_heading`,
`unsigned_in_print`, `judge_adjudicated`, `page_unreadable`, `plausibility_fail`, `energy_basis_unstated`.

## index.json / index.csv

One row per dataset: `path`, `folder`, `system`, `components`, `output`, `phases`, `n_values`, `n_values_dropped`,
`T_min_K`, `T_max_K`, `evidence_class`, `reference`, `bibtex`, `dois`, `papers`, `observation_ids`, `reader_agreement`
(counts by code; `not_classified` where the record builder did not classify), `reader_agreement_source`, `caveats`,
`tags`, `weight` (`per_value` for DFT), `sigma_unit`, `sigma_min`, `sigma_median`, `sigma_max` (over printed or
calibrated sigmas), `sigma_basis_counts`, `dft_calibration_stratum`, `tdb`, `tdb_sha256`, `model_link_basis`,
`espei_median_abs_driving_force_J`, `source_dataset`. CSV: lists joined with `;`, objects as compact JSON.

## validation.json

`espei_version`; `folders` (files and datasets loaded per folder); `invalid_final` (empty); `excluded` (rejected by
ESPEI, with reason code); `dropped_datasets`; `dropped_values`; `dft_excluded` (compound or compound x TDB model, with
reason); `summary`.
