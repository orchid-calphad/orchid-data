# Assessed phase assemblages: schema (assessed-phase-assemblage-v1)

Builder: `tools/build_assessed_assemblages.py` (orchid-project.org; deterministic, `--check`). Source annotation run:
`run-20261021h-full`. Evidence class of every record: `assessed_phase_diagram`.

## Record (`records.jsonl.gz`, gzip-compressed JSON Lines, one object per line)

| field | meaning |
|---|---|
| `id` | `aspa-` + first 16 hex of SHA-256 of `system|diagram|field|0` (stable across rebuilds) |
| `record_type`, `evidence_class` | `assessed_phase_assemblage`, `assessed_phase_diagram` (never `experimental`, never a model value) |
| `system`, `elements` | binary system (upper-case elements, sorted, `-`-joined; the phase-registry key) |
| `diagram`, `field` | diagram id `<SYSTEM>-p<PDF page>` and field id of the annotation run |
| `assemblage[]` | phases present: `label` (handbook label as printed, with the annotation conventions: `L#2` second liquid, `δ#2` second composition of one phase, `G` gas), `canonical_name` (registry preferred name when mapped, else the label), `phase_id` (phase-registry id or `null`; never invented), `mapping_basis`, and phase metadata from the diagram's phase table (`pearson_symbol`, `strukturbericht`, `prototype`, `space_group_printed`, `composition_range_at_pct`) |
| `assemblage_label`, `n_phases` | `+`-joined labels; 1 or 2 (three-phase invariants are other records) |
| `T_K`, `T_C`, `temperature_axis` | temperature of the point; the diagram axis is in °C |
| `x`, `x_component`, `composition_axis`, `composition_basis` | mole fraction of `x_component`; every diagram here is drawn in at.% (no wt.% conversion) |
| `P_Pa`, `pressure_basis` | 101325; 1 atm assumed |
| `coordinate_uncertainty` | `{T_K, x}` bounds = max axis-calibration residual + half a raster cell; also the residuals and number of calibration pairs per axis |
| `uncertainty_budget` | `{calibration, sigma_rule, quantities{temperature_K, composition}}`, the same separate-component structure as the literature release (PI decision 2026-10-24). Per quantity (`unit` K / mole fraction, `value_type` `T_ASSESSED` / `X_ASSESSED`): `sigma_printed` null (the handbook prints no uncertainty); `sigma_reading` = digitisation, i.e. the `coordinate_uncertainty` bound (max axis-calibration residual + half a raster cell); `sigma_method` = handbook-class prior `{class: assessed_phase_diagram, value, floor, basis: prior, n_pairs: 0, entry, prior_source: orchid_assumed}`, 10 K and 0.02 mole fraction: ORCHID assumption, not fitted: an expert-drawn assessed diagram reproduces its experimental evidence to about 10 K and 0.02 mole fraction, the priors the literature release uses for model / assessment values; `sigma_composition`, `sigma_scatter`, `sigma_conversion` null (do not apply); `sigma_boundary_margin` = `positional_margin` isopleth_K / isotherm_mole_fraction (drawing-based, reported, **not** combined); `sigma_effective` = max(sigma_reading, sigma_method). Rule: `max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter); boundary margin reported, not combined`. Flat columns: `sigma_T_reading_K`, `sigma_x_reading`, `sigma_T_method_K`, `sigma_x_method`, `sigma_T_effective_K`, `sigma_x_effective`. Tie-line endpoints keep their own `x_uncertainty` (drawing-based, not part of the budget) |
| `point_method` | `centroid` or `pole_of_inaccessibility`; for the fallback `centroid` gives the centroid, whether it was inside, and its clearance |
| `positional_margin` | `{normalized, isotherm_mole_fraction, isopleth_K}`: distance to the nearest drawn line or frame edge (frame-normalised; along the isotherm; along the isopleth). Drawing-based, low credence: describes placement only, not an uncertainty of any phase composition |
| `phase_compositions` | always `null`: the record does not claim phase compositions |
| `tie_line` | two-phase points only, or `null`: `{T_K, endpoints[{phase, x, x_uncertainty, side, kind, line_compound?, x_drawn?}], method, caveat}`. Isotherm through the point intersected with the field's drawn boundaries; each endpoint belongs to the phase whose single-phase field lies on that side, a line compound (composition from the printed phase table, `x_drawn` the drawn line), or a pure-element frame edge. Caveat: drawing-based, weak/soft constraint |
| `tie_line_omitted` | reason when a two-phase point has no tie_line: `neighbour_field_unnamed`, `side_assignment_ambiguous`, `boundary_not_a_single_clean_line`, `isotherm_reaches_cut_off_frame_edge`, `frame_edge_phase_ambiguous`, `endpoints_do_not_cover_the_two_phases`, `point_outside_endpoints` |
| `basis`, `basis_description` | how the field was named: `deterministic_printed_label`, `deterministic_phase_rules`, `deterministic_adjacency`, `reader_consensus`, `adjudicator`, `dft_hull_corroborated` (adjudicator + Materials Project/OQMD hulls; not handbook evidence), `expert_reviewed` |
| `confidence` | `high` / `medium` / `low` (blind-audit defaults per basis; hull rule: both hulls agree high, disagree low; `local_conflict` low; `carried_against_rules` capped at medium) |
| `review_state` | `expert decision (tier 5)`, `expert-reviewed (tier 5)`, or `not reviewed by the expert` |
| `name_history`, `expert_review` | only where the expert corrected the machine name (tools/assessed_expert_corrections.json): the superseded machine name with its basis, and the reviewer, review time and source of the decision |
| `flags` | `local_conflict`, `carried_against_rules`, `phase_not_in_table`, `hull_support:<both|disagree|mp_only|oqmd_only|none>`, `partly_drawn_dft_corroborated` |
| `sgte_crosscheck[]` | per calculated SGTE diagram of the system: `{tdb, tdb_sha256, cell{T_K, x}, calculated (TDB phase set at the nearest grid cell), result: agrees / disagrees / not_comparable, reason}`. Phase sets compared as registry ids. Never changes the assessed record |
| `citations[]` | original evaluation(s) first (`citation`, `doi`, `doi_matched_by`, `kind`; `doi` null with `doi_status: dropped_mismatch` and `doi_correction` when the DOI matched to the printed source line describes a different work, `tools/doi_corrections.json`), then the handbook (`role: compilation`, `page_pdf`, `locator`) |
| `method` | builder, version, annotation run, tool hashes |

## Point placement

Exactly one point per named field. The field is the set of raster cells of the traced field (drawn lines are not part
of any field). Distances use frame-normalised axes (each axis scaled to the drawn frame). The area centroid (mean T
and x of the field's cells) is used when it lies inside the field with clearance >= 0.006; otherwise the pole of
inaccessibility (the cell of maximum clearance; first in row-major order on ties). If even that is < 0.006 the field
gets no point (`too_thin_for_margin`). Points are never placed on invariant lines or line compounds (both are lines,
not fields). Rationale: an interior point makes the assemblage claim independent of the exact boundary positions,
which in an assessed diagram carry little credence.

## Exclusions (`exclusions.jsonl`)

`{diagram, field, reason, detail, assemblage?}`. Reasons: `tracing_fault`, `open`, `awaiting_expert` (tier-5
pending), `undetermined_in_source` (source_undetermined, e.g. printed '?', drawing ends), `cannot_tell`,
`partly_drawn_truncated_edge` (the field reaches a cut-off composition edge of the drawing; included instead when
DFT-hull corroborated), `too_thin_for_margin`, `diagram_tracing_suspect` (whole diagram), `more_than_two_phases` (a binary field named with three or more phases), `axis_component_not_in_system` (the composition axis was read as an element outside the system; whole diagram), `diagram_not_annotated`
(field null: calibration failed, overlay of several assessments, no axis title).

## ESPEI (`espei-zpf/`, `espei-zpf-with-tie-lines/`)

One ZPF dataset per diagram: `components` (upper case, `VA` when a model of an included phase has vacancies),
`phases` (TDB phase names: the registry preferred name, i.e. the SGTE name used by most assessments of the system),
`conditions {P: 101325, T: [K...]}`, `values` aligned with `T`. Single-phase point: `[[PHASE, [X], [x]]]`. Two-phase
point (default): `[[P1, [X], [null]], [P2, [X], [null]], ["__HYPERPLANE__", [X], [x]]]` -- phases present,
compositions unknown, the target hyperplane at the point's overall composition. The tie-line variant uses
`[[P1, [X], [x1]], [P2, [X], [x2]]]` where a `tie_line` block exists, else the default form; a line-compound endpoint
is written with composition null (ESPEI 0.9.1 / pycalphad 0.11.2 return NaN for a line compound at a fixed composition),
and where both endpoints are line compounds the hyperplane is set at the point. `tags`: `assessed_phase_diagram`,
`orchid` (+ `tie_line_variant`). `reference`: original evaluation(s) and the handbook; `comment`: evidence class, point
method and (variant) the caveat; `orchid`: record ids; `orchid_uncertainty_budget`: `{sigma_rule, calibration,
points[{record_id, temperature_K, composition_mole_fraction}]}` with the budget component values of each point (value
order); ESPEI weighs ZPF by its driving-force tolerance, so the budget is information, not a weight. Points whose phases do not all map to a registry phase with a TDB
name are left out (`espei_exclusions.jsonl`) but stay in `records.*`. The ESPEI bundle (`espei/assessed/`) carries the
same points in the phase names of each assessment (TDB) that has ESPEI ZPF datasets, for use together with them.

## CSV / Parquet columns

`id`, `system`, `diagram`, `field`, `assemblage_label`, `n_phases`, `phase_labels`, `canonical_names`, `phase_ids`, `T_K`, `T_C`, `x`, `x_component`, `P_Pa`, `u_T_K`, `u_x`, `sigma_T_reading_K`, `sigma_x_reading`, `sigma_T_method_K`, `sigma_x_method`, `sigma_T_effective_K`, `sigma_x_effective`, `point_method`, `margin_normalized`, `margin_isotherm_x`, `margin_isopleth_K`, `basis`, `confidence`, `review_state`, `flags`, `tie_line_x_left`, `tie_line_phase_left`, `tie_line_x_right`, `tie_line_phase_right`, `tie_line_omitted`, `sgte_n`, `sgte_agrees`, `sgte_disagrees`, `sgte_not_comparable`, `sgte_results`, `original_citation`, `original_doi`, `handbook_page_pdf`, `evidence_class`. Lists are `;`-joined. `sgte_results`: `tdb=result` per assessment.
