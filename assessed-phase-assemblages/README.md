# ORCHID assessed phase assemblages (binary systems)

Status: **Version 1, machine-extracted.** Release v2026.10. Licence CC BY 4.0 (derived data and citations).

One record per named phase field of the expert-drawn (assessed) binary phase diagrams compiled in H. Okamoto,
*Desk Handbook: Phase Diagrams for Binary Alloys*, 2nd ed. (ASM International, 2010): the thermodynamic coordinate
(T, x, P) of a point deep inside the field and the phase assemblage present there. Evidence class
`assessed_phase_diagram`: an expert drew the diagram from experimental evidence without a CALPHAD model; these are
neither raw measurements nor model values, and they are kept separable at fitting time.

## Counts (this build)

| | |
|---|---|
| diagrams with points | 2,178 |
| fields seen | 27,118 |
| points | 23,131 (centroid 21,618, pole of inaccessibility 1,513) |
| points by number of phases | 1-phase 4,639, 2-phase 18,492 |
| two-phase points with / without a tie_line block | 11,962 / 6,530 |
| SGTE cross-check (point x assessment) | 30,769 comparisons: 23,087 comparable (19,160 agree, 3,927 disagree; agreement 0.8299 of comparable), 7,682 not comparable (counted separately, reasons in `sgte_not_comparable.csv`) |
| SGTE cross-check (points) | 10,362 points with a comparable assessment; 9,184 (0.8863) agree with at least one SGTE assessment; median system agreement 0.8889 (892 systems with >= 5 comparable comparisons) |
| boundary basis (lines bounding the point's field along its isotherm and isopleth) | printed_solid 20,784, mixed 1,292, dashed_estimated 1,028, none 27 |
| ESPEI datasets (one per diagram) | 1,070 default, 1,070 with tie-lines; 10,874 points exported, 12,257 excluded (phase without TDB name) |

Points by basis:

| basis | points |
|---|---|
| deterministic_adjacency | 8,035 |
| reader_consensus | 6,794 |
| deterministic_printed_label | 3,206 |
| adjudicator | 2,803 |
| deterministic_phase_rules | 2,186 |
| expert_reviewed | 87 |
| dft_hull_corroborated | 20 |

Fields without a point, by reason:

| reason | fields |
|---|---|
| too_thin_for_margin | 2,047 |
| tracing_fault | 740 |
| partly_drawn_truncated_edge | 482 |
| undetermined_in_source | 255 |
| awaiting_expert | 172 |
| diagram_tracing_suspect | 123 |
| axis_component_not_in_system | 89 |
| open | 70 |
| more_than_two_phases | 5 |
| cannot_tell | 4 |

## Why one point deep inside each field

The PI's guidance (2026-10-23): the positions of drawn boundaries and tie-lines deserve little credence; the
thermodynamic coordinates of the assemblage are what matters. Each field therefore gives exactly one point: the area
centroid of the field (in the diagram's T and composition axes) when it lies inside the field at least 0.006
(frame-normalised) from every drawn line, otherwise the pole of inaccessibility (the interior point farthest from all
lines). Fields too thin for that margin have no point (listed in `exclusions.jsonl`). The claim "this assemblage is
stable at (T, x, 1 atm)" then does not depend on where exactly the expert drew the boundaries. Coordinate uncertainty
comes from the axis calibration (printed tick labels vs the fitted axis) plus half a raster cell.

Each record carries an `uncertainty_budget` with the components kept separate, in the same structure as the ORCHID
literature release (PI decision 2026-10-24): digitisation (`sigma_reading`, the coordinate uncertainty above), a
handbook-class prior (`sigma_method`: 10 K and 0.02 mole fraction for an expert-drawn assessed diagram; an ORCHID
assumption, the same as the release's model / assessment priors, not fitted) and the distance to the nearest drawn
boundary (`sigma_boundary_margin`, reported but not combined, since boundary positions carry low credence);
`sigma_effective` = max(reading, handbook prior). The ESPEI datasets carry the per-point components and the
`boundary_basis` in `orchid_uncertainty_budget` (ZPF data are not weighted by a sigma in ESPEI).

## Solid and dashed (estimated) boundaries

Handbook diagrams draw boundaries that the evaluator could not fix from measurements as dashed lines. The tracer joins
the dashes of such a line into a chain and uses it as a field boundary like a solid line (dashed Curie-temperature
lines, cooling curves and the dashed second assessment of an overlay are not boundaries and are dropped). Each point
records `boundary_basis` for the lines that bound its field along its isotherm and isopleth, i.e. the lines that set
its positional margin: `printed_solid`, `dashed_estimated` or `mixed` (null when only frame edges bound it), with the
counts in `boundary_lines`. The dash chains are re-derived from the traced lines with the tracer's own rule
(`tools/dashed_boundaries.py`; the build fails if the number of dash joins differs from the tracer's count in any
diagram). For points bounded by dashed lines the reading component of the budget is enlarged (ORCHID assumption, not
fitted): 2x the handbook-class prior (20 K, 0.04) for `dashed_estimated` and 1.5x (15 K, 0.03) for `mixed`.

## SGTE cross-check: metric definitions

A comparison is one point against one SGTE assessment of its system (the phase set at the nearest cell of the
calculated 10 K x 0.01 grid). It is comparable when every phase of the point maps to a registry phase and the cell
has an equilibrium; the result is then agrees or disagrees. Rates are computed over comparable comparisons only:
`agreement_rate_of_comparable` = agrees / (agrees + disagrees) over all comparable comparisons (an aggregate, not a
per-system mean); `points_agreeing_with_at_least_one_rate` = share of the points with at least one comparable
comparison that agree with at least one SGTE assessment of their system (systems have up to 16 assessments, and an
older assessment that differs still counts); `median_system_rate` over systems with at least 5 comparable
comparisons. Non-comparable comparisons are never part of a rate; they are counted by reason in `summary.json` and
listed one per row in `sgte_not_comparable.csv`.

Two-phase points carry the two phases with **unknown compositions** (`phase_compositions: null`; ESPEI null vertices
with a `__HYPERPLANE__` vertex at the point's overall composition). A separate `tie_line` block gives the isotherm
through the point intersected with the drawn boundaries, with the caveat that it is drawing-based and of low credence
(weak/soft constraint); it is left out with a reason when the isotherm does not meet two clean, unambiguous boundaries.

## Files

`records.jsonl.gz` (full records, gzip JSON Lines), `records.csv` / `records.parquet` (flat), `exclusions.jsonl` / `.csv` (fields and
diagrams without points, with reasons), `espei-zpf/<diagram>.json` (ESPEI ZPF datasets, null endpoints),
`espei-zpf-with-tie-lines/<diagram>.json` (variant using tie_line endpoints where present), `espei_exclusions.jsonl`,
`sgte_not_comparable.csv` (each non-comparable SGTE comparison with its reason),
`summary.json`, `parquet.json`, `SCHEMA.md`, `CITATION.cff`. ESPEI datasets were validated with
`espei.datasets.check_dataset` and `load_datasets` (ESPEI 0.9.1).

## Not included (licence)

No page images, crops, renders, paths to page images, or handbook text beyond phase names and citations. The build
fails if any output key or string looks like such content (forbidden keys, image/PDF paths, base64, long free text).
Traced boundary geometry, reader/adjudicator reasons and review pages are not part of this dataset.

## Citation

Cite this dataset, the umbrella ORCHID data record, and, for every diagram you use, its **original evaluation**
(`citations[role=original_evaluation]`, DOI where matched) followed by the Okamoto handbook as the compilation.

R. Arróyave, J. Saal, D. Shin, ORCHID assessed phase assemblages (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-assessed-phase-assemblages

Part of: R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data
