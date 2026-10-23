# Zenodo release metadata (v2026.10)

ORCHID data release v2026.10 (Version 1, machine-extracted) is published on Zenodo as **nine records**: eight
citable datasets, each with its own DOI, and an umbrella record that links them with DataCite relations
(`hasPart` on the umbrella, `isPartOf` on each dataset).

| Record name | Title | Metadata | File list |
|---|---|---|---|
| `orchid-data` | ORCHID data (umbrella) | `orchid-data.metadata.json` | `orchid-data.files.json` |
| `literature` | ORCHID literature values | `literature.metadata.json` | `literature.files.json` |
| `phase-diagrams` | ORCHID calculated binary phase diagrams | `phase-diagrams.metadata.json` | `phase-diagrams.files.json` |
| `hulls` | ORCHID binary convex hulls (Materials Project, OQMD, assessed CALPHAD) | `hulls.metadata.json` | `hulls.files.json` |
| `dft-benchmark` | ORCHID DFT-vs-experiment formation-enthalpy benchmark | `dft-benchmark.metadata.json` | `dft-benchmark.files.json` |
| `phase-registry` | ORCHID phase registry (binary systems) | `phase-registry.metadata.json` | `phase-registry.files.json` |
| `assessed-phase-assemblages` | ORCHID assessed phase assemblages (binary systems) | `assessed-phase-assemblages.metadata.json` | `assessed-phase-assemblages.files.json` |
| `espei` | ORCHID ESPEI datasets from the literature | `espei.metadata.json` | `espei.files.json` |
| `bibliography` | ORCHID bibliography | `bibliography.metadata.json` | `bibliography.files.json` |

- `<name>.metadata.json` — Zenodo deposition metadata (`metadata` object in the legacy REST format: title,
  upload type, HTML description with what / how / limitations / how to cite, creators with ORCID and affiliation,
  keywords, licence `cc-by-4.0`, NSF grant `10.13039/100000001::2608825`, version `2026.10`, community `orchid`,
  related identifiers: `isPartOf` / `hasPart`, `isSupplementTo` https://orchid-project.org, `references` to the
  SGTE, Materials Project, OQMD and Kim et al. 2017 DOIs).
- `<name>.files.json` — the files of the record (repository paths, bytes, SHA-256), written by
  `tools/zenodo_release.py manifest` from the rules in that script.
- `dois.json` — the DOI of each record. Until DOIs are reserved they are placeholders
  `10.5281/zenodo.PENDING-<name>`; every builder reads this file (through `tools/orchid_cite.py` in the website
  repository), so the citations embedded in the data (`cite_as`, Parquet metadata, static pages) follow it.

The tools live in the website repository `orchid-calphad/orchid-project.org` (`tools/zenodo_release.py`) and expect
this repository next to it (`~/projects/orchid-data`, or pass `--data`).

## How to publish (recommended: web upload with reserved DOIs)

Nothing here calls the Zenodo API and no token is stored. The order matters because the DOIs have to be written
into the data before the bundles are built.

1. **Community.** On zenodo.org create (or open) the community `orchid` (Communities → New community).
2. **Reserve nine DOIs.** For each record: *New upload*, then in the *Digital Object Identifier* section answer
   "Do you already have a DOI?" with *No* and press **Get a DOI now!** (the older interface called it **Reserve
   DOI**). Fill at least the title from `<name>.metadata.json` and **Save draft**; do not publish yet. Note the
   nine DOIs (`10.5281/zenodo.NNNNNNN`).
3. **Write the DOIs back** (website repository):

   ```sh
   python3 tools/zenodo_release.py writeback \
     --doi orchid-data=10.5281/zenodo.AAAAAAA --doi literature=10.5281/zenodo.BBBBBBB \
     --doi phase-diagrams=10.5281/zenodo.CCCCCCC --doi hulls=10.5281/zenodo.DDDDDDD \
     --doi dft-benchmark=10.5281/zenodo.EEEEEEE --doi phase-registry=10.5281/zenodo.FFFFFFF \
     --doi assessed-phase-assemblages=10.5281/zenodo.GGGGGGG --doi espei=10.5281/zenodo.HHHHHHH \
     --doi bibliography=10.5281/zenodo.IIIIIII
   ```

   This updates `dois.json`, replaces every placeholder in both repositories (metadata here, `CITATION.cff` files,
   `DATASET_CARD.md`, `hf/README.md`, `CHANGELOG.md`, `README.md`, `llms.txt`, the website's home, dataset, about,
   explorer, DFT-parity and phase-diagram pages, `data/croissant.json`, `.zenodo.json`), reruns the builders
   (literature export, DFT parity, `add_cite_as.py`, Parquet, static pages, phase registry, ESPEI bundle, assessed
   phase assemblages, bibliography, dataset-card sizes, file manifests)
   and every `--check`, and fails if a placeholder is left. `--dry-run` lists the files first. Review `git diff` in
   both repositories and commit.
4. **Check and bundle.**

   ```sh
   python3 tools/zenodo_release.py plan      # files present and unchanged, sizes, < 50 GB per record
   python3 tools/zenodo_release.py bundle    # dist/orchid-<name>-v2026.10.zip + dist/SHA256SUMS (git-ignored)
   ```

   Each zip holds the record's files at their repository paths under one top folder plus `MANIFEST.sha256`; the
   bytes are deterministic (fixed order and timestamps), so rebuilding gives the same SHA-256.
5. **Upload and fill the drafts.** In each draft upload its single zip (one file per record stays far below
   Zenodo's 100-file limit) and copy the fields from `<name>.metadata.json`: resource type *Dataset*, title,
   creators (ORCID, affiliation), description (paste the HTML in the editor's source view), version `2026.10`,
   licence *Creative Commons Attribution 4.0 International*, keywords, funding (NSF, award 2608825, CSSI Elements:
   PhaseForge), related works (the relations listed in `related_identifiers`), community `orchid`.
6. **Publish** the eight dataset records first, then the umbrella. Check that every DOI resolves and that the
   relations show on each record page. Then tag both repositories `v2026.10`.

For a later release use **New version** on each record (Zenodo keeps a concept DOI that always points to the latest
version), set the new version string in `tools/orchid_cite.py`, and repeat steps 2–6.

## Why not the GitHub integration

Zenodo's GitHub integration archives one repository snapshot per GitHub release as one record (metadata from a
`.zenodo.json`). It cannot produce eight dataset records plus an umbrella, it would archive the generated static
pages with the data, and it mints the DOI only at publication, so the DOIs could not be written into the data
first. Use it, if at all, for the website/tooling repository (its `.zenodo.json` describes that record and points
to the umbrella DOI with `documents`). The ORCHID benchmark (`orchid-calphad/orchid-bench`) is a code repository and is archived
that way, as its own record outside this data release.
