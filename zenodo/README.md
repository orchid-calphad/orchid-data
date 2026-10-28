# Zenodo release metadata (v2026.10)

ORCHID data release v2026.10 (Version 1, machine-extracted) is published on Zenodo as **ten records**: eight
citable datasets, each with its own DOI, an umbrella record that links them with DataCite relations (`hasPart` on the
umbrella, `isPartOf` on each dataset), and a software record for the runnable examples (`orchid-examples`, a git archive
of a pinned commit of the `orchid-calphad/orchid-examples` repository; it is not part of the umbrella, which only points
to it with `isReferencedBy`). The orchid-bench, orchid-pipeline, orchid-project.org and orchid-mcp software records come
from the GitHub integration and are not described here. All records go to the Zenodo community
`orchid-calphad` (a single variable, `ZENODO_COMMUNITY` in `tools/orchid_cite.py`).

**Step-by-step instructions for the PI: `ZENODO_PUBLISH_RUNBOOK.md`. Funding: `ZENODO_FUNDING_MANUAL.md`.**

| Record name | Dataset (paper) | Title | Metadata | File list |
|---|---|---|---|---|
| `orchid-data` | umbrella | ORCHID data: umbrella record of the ORCHID datasets | `orchid-data.metadata.json` | `orchid-data.files.json` |
| `literature` | Values | ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature | `literature.metadata.json` | `literature.files.json` |
| `phase-diagrams` | Diagrams | ORCHID-Diagrams: calculated binary phase diagrams | `phase-diagrams.metadata.json` | `phase-diagrams.files.json` |
| `hulls` | Hulls | ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) | `hulls.metadata.json` | `hulls.files.json` |
| `dft-benchmark` | Parity | ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark | `dft-benchmark.metadata.json` | `dft-benchmark.files.json` |
| `phase-registry` | Registry | ORCHID-Registry: phase registry of binary systems | `phase-registry.metadata.json` | `phase-registry.files.json` |
| `assessed-phase-assemblages` | Assemblages | ORCHID-Assemblages: assessed phase assemblages of binary systems | `assessed-phase-assemblages.metadata.json` | `assessed-phase-assemblages.files.json` |
| `espei` | ESPEI datasets of Values | ORCHID-Values ESPEI datasets: ESPEI-format datasets built from the literature values | `espei.metadata.json` | `espei.files.json` |
| `bibliography` | Bibliography | ORCHID-Bibliography: papers and typed citation relations | `bibliography.metadata.json` | `bibliography.files.json` |
| `orchid-examples` | software | ORCHID examples: runnable workflows on the ORCHID data (PhaseForge+, ESPEI, one-shot MLIP phase diagrams, MLIP formation enthalpies, quickstart) | `orchid-examples.metadata.json` | `orchid-examples.files.json` (pinned commit) |

- `<name>.metadata.json` — Zenodo deposition metadata (`metadata` object in the legacy REST format: title,
  upload type, HTML description with what / how / limitations / how to cite, creators with ORCID and affiliation,
  keywords, licence `cc-by-4.0` (`mit` for the examples), version `2026.10`, community `orchid-calphad`, no `grants` entry (NSF award 2608825 is not in Zenodo's awards database: enter it as a custom award, `ZENODO_FUNDING_MANUAL.md`),
  related identifiers: `isPartOf` / `hasPart`, `isDerivedFrom`, `isDocumentedBy` the websites, `references` to the
  SGTE, Materials Project, OQMD and Kim et al. 2017 DOIs, and `isSupplementTo` the paper once it has an identifier).
  Written by `tools/build_zenodo_metadata.py` (`zenodo_release.py metadata`); `metadata_numbers.json` lists every number in the
  descriptions with the release file it was read from. The record of ORCHID-Assemblages is written by
  `tools/build_assessed_assemblages.py`.
- `<name>.files.json` — the files of the record (repository paths, bytes, SHA-256), written by
  `tools/zenodo_release.py manifest` from the rules in that script.
- `dois.json` — the DOI of each record. Until DOIs are reserved they are placeholders
  `unassigned per-record DOI`; every builder reads this file (through `tools/orchid_cite.py` in the website
  repository), so the citations embedded in the data (`cite_as`, Parquet metadata, static pages) follow it.

The tools live in the website repository `orchid-calphad/orchid-project.org` (`tools/zenodo_release.py`) and expect
this repository next to it (`~/projects/orchid-data`, or pass `--data`).

## How to publish

Web upload with reserved DOIs, no Zenodo API call and no token stored by these tools. The exact steps, in order, with
the pre-publish checklist and what cannot be undone, are in **`ZENODO_PUBLISH_RUNBOOK.md`**. In short: create the
community `orchid-calphad`; reserve ten DOIs in ten draft uploads; `zenodo_release.py writeback` writes the DOIs into the
data, the metadata and the paper numbers; `bundle` builds one zip per record; upload each zip and fill the form from the
sheet that `zenodo_release.py metadata --export DIR` writes; enter the funding as a custom award
(`ZENODO_FUNDING_MANUAL.md`); publish the eight datasets, then the examples, then the umbrella; accept each submission in
the community.

Commands (website repository): `manifest`, `metadata`, `card`, `scan`, `plan`, `bundle`, `writeback`; each has `--check` or
`--dry-run` where it applies (`python3 tools/zenodo_release.py --help`).

For a later release use **New version** on each record (Zenodo keeps a concept DOI that always points to the latest
version), set the new version string in `tools/orchid_cite.py`, and repeat the runbook from the reservation of the DOIs.

## Why not the GitHub integration

Zenodo's GitHub integration archives one repository snapshot per GitHub release as one record (metadata from a
`.zenodo.json`). It cannot produce eight dataset records plus an umbrella, it would archive the generated static
pages with the data, and it mints the DOI only at publication, so the DOIs could not be written into the data
first. Use it, if at all, for the website/tooling repository (its `.zenodo.json` describes that record and points
to the umbrella DOI with `documents`). The examples record is deposited by web upload (so that its DOI is known before
it is published); keep the GitHub toggle OFF for `orchid-examples` and `orchid-data`. The ORCHID benchmark (`orchid-calphad/orchid-bench`) is a code repository and is archived
that way, as its own record outside this data release.
