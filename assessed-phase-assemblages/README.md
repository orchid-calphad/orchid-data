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
| SGTE cross-check (point x assessment) | 30,769 comparisons: 18,974 agree, 4,087 disagree, 7,708 not comparable (agreement 0.8228 of comparable) |
| ESPEI datasets (one per diagram) | 1,070 default, 1,070 with tie-lines; 10,870 points exported, 12,261 excluded (phase without TDB name) |

Points by basis:

| basis | points |
|---|---|
| deterministic_adjacency | 8,035 |
| reader_consensus | 6,795 |
| deterministic_printed_label | 3,206 |
| adjudicator | 2,803 |
| deterministic_phase_rules | 2,186 |
| expert_reviewed | 86 |
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

Two-phase points carry the two phases with **unknown compositions** (`phase_compositions: null`; ESPEI null vertices
with a `__HYPERPLANE__` vertex at the point's overall composition). A separate `tie_line` block gives the isotherm
through the point intersected with the drawn boundaries, with the caveat that it is drawing-based and of low credence
(weak/soft constraint); it is left out with a reason when the isotherm does not meet two clean, unambiguous boundaries.

## Files

`records.jsonl.gz` (full records, gzip JSON Lines), `records.csv` / `records.parquet` (flat), `exclusions.jsonl` / `.csv` (fields and
diagrams without points, with reasons), `espei-zpf/<diagram>.json` (ESPEI ZPF datasets, null endpoints),
`espei-zpf-with-tie-lines/<diagram>.json` (variant using tie_line endpoints where present), `espei_exclusions.jsonl`,
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
