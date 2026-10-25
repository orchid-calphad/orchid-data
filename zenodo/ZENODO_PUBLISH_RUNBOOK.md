# Runbook: publishing the ORCHID Zenodo records (v2026.10)

For the PI. Ten records: the umbrella, eight datasets and the software record `orchid-examples`. Everything that can be
prepared is prepared; what remains are actions in your Zenodo account. Nothing in this repository calls Zenodo.
Commands are run in the website repository (`orchid-project.org`) with the data repository next to it; abbreviated here as

```sh
cd ~/projects/orchid-project.org
Z="python3 tools/zenodo_release.py"          # uses ../orchid-data and ../orchid-examples
```

Zenodo's web interface changes from time to time: the button and menu names below follow its help pages of October 2026
("Get a DOI now!", "Submit for review", "Add custom" for funding); if a label differs, the step is the same.

## What cannot be undone

- **Publishing a record is permanent.** A published record cannot be deleted by you, its DOI cannot be withdrawn, and its
  **files cannot be removed or replaced**. A change to the files needs a **New version** (a new DOI; the old version stays
  visible and citable). Only metadata (title, description, related works, funding, community, keywords) stays editable.
- A reserved DOI belongs to its draft for good; an abandoned draft can be deleted, but then its DOI is simply never
  registered, and a new draft gets a new DOI. Do not delete a draft whose DOI has been written into the data.
- The community identifier `orchid-calphad` cannot be changed after the community is created.
- The DOIs are written into ~36,000 files (`writeback`); undoing that is a `git checkout` before the commit, a new
  release after it.

## Pre-publish checklist (tick every line before the first Publish)

Restricted material, secrets, licences (run on the final tree after `writeback`; all must pass):

1. `$Z plan` prints `OK` (every file of every record present and unchanged, each record below 50 GB, one zip each, far
   below the 100-file default).
2. `$Z scan` prints `SCAN OK`: no PDF, page image, office file, key file or restricted path (`private/`, handbook page or
   crop folders) and no secret pattern (AWS, GitHub, Hugging Face, PyPI, OpenAI-style keys, private keys, publisher API-key
   headers) in any file of any record. Checked 2026-10-24 on the data of branch `zenodo-prep`: clean for the nine data
   records and for the examples (fifteen of the examples' own figures and `.npz` input tables are listed for one review;
   four cached manifests in `phaseforge-structures/cached/` contain a local absolute path).
3. `$Z metadata --check` and `$Z manifest --check` pass (the text and the file lists match the data).
4. `$Z card --check`, and `--check` of the builders (writeback runs them all).
5. **Verbatim quotes** (your decision of 2026-10-24: short quotes may be published with citation and page, never whole
   paragraphs): the Parquet table holds 5,743 quotes, median 172 characters, maximum 985, **81 longer than 500
   characters**. Decide: accept, or cap/review those 81 before publishing (a published file cannot be changed).
6. Licences: records are CC BY 4.0 (`orchid-examples`: MIT for code, `LICENSE-DATA.md` for data); third-party data
   (SGTE, Materials Project, OQMD CC BY 4.0; Kim et al. 2017 values MIT; Crossref metadata CC0) are stated in
   `NOTICE.md` and `LICENSES.md`, which are in every zip. Quotes stay under the publishers' copyright and are said so in
   the licence text of each record.
7. No `grants` key in any metadata file (`grep -l '"grants"' ../orchid-data/zenodo/*.json` prints nothing) and the
   community is `orchid-calphad` everywhere (`grep -rn '"identifier": "orchid"' ../orchid-data/zenodo` prints nothing).
8. Creator order and ORCHIDs (Arróyave, Saal, Shin) are the order you want on all ten records; they come from
   `AUTHORS` in `tools/orchid_cite.py`.

## Step 0. Before anything is reserved

1. Merge or rebase branch `zenodo-prep` of `orchid-data`, `orchid-project.org` and `orchid-examples` onto the current main
   (after the other release job is committed). The formal dataset titles live in `tools/orchid_cite.py`; the data files
   embed them (`cite_as`), so the first `writeback` below (which rebuilds everything) also brings the data in line with
   the titles. Until then the builders' `--check` modes report stale `cite_as` titles: expected.
2. If the examples repository changed, re-pin it: `$Z manifest --examples-ref <tag-or-commit>`, then `$Z metadata`
   and `$Z manifest`.
3. Optional: check whether NSF award 2608825 has appeared in Zenodo's database (it was absent on 2026-10-24):
   `curl -s 'https://zenodo.org/api/awards?q=2608825' | head -c 300`. If it has, use it instead of the custom award
   (`ZENODO_FUNDING_MANUAL.md`).

## Step 1. Create the community (once)

zenodo.org, Communities, New community. Identifier `orchid-calphad` (**permanent**; `orchid` and `orchid-project` belong to
other projects), title "ORCHID: Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery", public, a short
description with <https://orchid-project.org>, optional logo (`assets/logo/` in the website repository). Look at the
community's Settings: if you, as owner, can publish into your community without review, records go straight to
published when you press Publish; otherwise the button reads **Submit for review**, the record stays unpublished until
you **accept** it under the community's Requests (Step 6).

## Step 2. Reserve ten DOIs (Zenodo web, no files yet)

For each of the ten records (any order): *New upload*, resource type (Dataset; **Software** for `orchid-examples`), the
**title** from the table below, then in *Digital Object Identifier* answer "Do you already have a DOI?" with **No** and
press **Get a DOI now!** (save the draft first if the button is inactive), then **Save draft**. Do **not** publish. Do
not attach the community yet. Copy the DOI of each draft into the table and send it to Claude.

| # | record name | title (paste) | resource type | DOI (`10.5281/zenodo.`) |
|---|---|---|---|---|
| 1 | `literature` | ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature | Dataset | |
| 2 | `espei` | ORCHID-Values ESPEI datasets: ESPEI-format datasets built from the literature values | Dataset | |
| 3 | `phase-diagrams` | ORCHID-Diagrams: calculated binary phase diagrams | Dataset | |
| 4 | `hulls` | ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) | Dataset | |
| 5 | `dft-benchmark` | ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark | Dataset | |
| 6 | `phase-registry` | ORCHID-Registry: phase registry of binary systems | Dataset | |
| 7 | `assessed-phase-assemblages` | ORCHID-Assemblages: assessed phase assemblages of binary systems | Dataset | |
| 8 | `bibliography` | ORCHID-Bibliography: papers and typed citation relations | Dataset | |
| 9 | `orchid-examples` | ORCHID examples: runnable workflows on the ORCHID data (PhaseForge+, ESPEI, one-shot MLIP phase diagrams, MLIP formation enthalpies, quickstart) | Software | |
| 10 | `orchid-data` | ORCHID data: umbrella record of the ORCHID datasets | Dataset | |

## Step 3. Write the DOIs into the release (Claude; the DOIs must be in the data before the zips are built)

```sh
$Z writeback --dry-run --doi literature=10.5281/zenodo.AAAAAAA --doi espei=... --doi phase-diagrams=... --doi hulls=... \
   --doi dft-benchmark=... --doi phase-registry=... --doi assessed-phase-assemblages=... --doi bibliography=... \
   --doi orchid-examples=... --doi orchid-data=...           # lists the files that would change; then without --dry-run
```

`writeback` replaces every `10.5281/zenodo.PENDING-<name>` in the data repository, the website repository and the
examples repository (README and CITATION.cff only), updates `zenodo/dois.json`, reruns all builders (this also brings
the formal titles into the data), regenerates the metadata and file lists, and fails if a placeholder is left. Then:

1. In `orchid-examples` commit the DOI change (README, CITATION.cff) and **re-pin**: `$Z manifest --examples-ref HEAD`,
   then `$Z metadata`, `$Z manifest`, `$Z metadata --check`, `$Z manifest --check`.
2. Review `git diff` in the three repositories; commit (never `git commit -a` across unrelated work); tag later (Step 7).
3. `$Z plan`, `$Z scan`, `$Z card --check` all green.
4. `$Z bundle` writes `dist/orchid-<name>-v2026.10.zip` (ten zips, about 190 MB in all; deterministic: a rebuild gives the
   same bytes), `dist/SHA256SUMS` and `dist/MD5SUMS` (Zenodo shows the MD5 of an uploaded file).
5. `$Z metadata --export dist/forms` writes one sheet per record (`dist/forms/<name>.form.html`) with every form field
   and the description as rich text to copy.
6. Paper (Claude): `python3 scripts/make_numbers.py --data ~/projects/orchid-data`, then rebuild (Step 7 lists the
   sentences). The `make_numbers.py` patch for the tenth record is `scripts/make_numbers_zenodo.patch` in the paper
   working copy.

## Step 4. Fill each draft (Zenodo web, ten times)

Order: as in Step 5 below. For each draft open its form sheet and:

1. **Files**: upload `dist/orchid-<name>-v2026.10.zip` (one file). Compare the MD5 Zenodo shows with `dist/MD5SUMS`.
2. Resource type, title, **creators** (the sheet lists name, ORCID, affiliation; this order), **description** (select the
   blue box on the sheet, copy, paste into the editor; if the editor drops headings or the BibTeX block, tell Claude: the
   text is regenerated), **publication date** (**TODO: set it on the day you publish**), **version** `2026.10`,
   **licence** (Creative Commons Attribution 4.0; MIT for the examples), keywords, language, access *Open*.
3. **Related works**: one row per line of the sheet (relation type, identifier, resource type). The reserved DOIs of the
   other records are valid identifiers although they do not resolve until published.
4. **Funding**: *Add custom*, as in `ZENODO_FUNDING_MANUAL.md` (NSF, 2608825, title, URL).
5. **Community**: select `orchid-calphad` (only one community can be chosen at first submission).
6. **Save draft**, then *Preview*: title, creators, DOI (must equal the reserved one), licence, funding chip, related
   works, description, one file.
7. Show it to Claude if you want a second pair of eyes (the previous dry run asked for this on every draft: this is the
   highest-stakes step).

## Step 5. Publish, in this order

1. Datasets: `literature`, `espei`, `phase-diagrams`, `hulls`, `dft-benchmark`, `phase-registry`,
   `assessed-phase-assemblages`, `bibliography` (the first two are the sources of the others).
2. `orchid-examples`.
3. `orchid-data` (umbrella) **last**, because it links to all of them.

After each publish: open `https://doi.org/10.5281/zenodo.N` (resolves within minutes; before that the record page
`zenodo.org/records/N` works), check that licence, funding, related works and the single file are as previewed.

## Step 6. Community acceptance

If the button read *Submit for review*, each record is now a pending request: community `orchid-calphad`, Requests (or the
notification), open each, **Accept**. The record becomes public on acceptance, so accept in the Step 5 order. A record
that is declined can be resubmitted or published without the community. Records already published can be added to the
community afterwards with *Submit to community* on the record page.
The GitHub-integration records (`orchid-project.org`, `orchid-pipeline`, `orchid-mcp`, `orchid-bench`; their
`.zenodo.json` name the same community) will also appear as requests after each GitHub release. Keep the Zenodo GitHub
toggle **off** for `orchid-data` and `orchid-examples` (deposited here; a release would archive them twice).

## Step 7. After publishing

1. Check that `zenodo/dois.json` holds the ten published DOIs (it already does, from Step 3), and rerun
   `$Z plan`, `$Z metadata --check`, `$Z manifest --check` and the builders' `--check` modes (writeback ran them once).
   Tag the repositories `v2026.10` (data, website, examples), push (needs your approval).
2. Paper (Claude): rerun `make_numbers.py` (macros `\doiUmbrella` ... `\doiExamples`, `\nZenodoRecords`=10,
   `\nZenodoDataRecords`=8, `\nZenodoSoftwareRecords`=1), rebuild `main.tex`, `main_arxiv.tex`, `si.tex`; fill the
   `orchid_data_2026` entry in `references.bib` with the umbrella DOI; replace `\doiPlaceholder{...}` for the code and
   the benchmark after their GitHub releases.
3. When the paper has an arXiv id or DOI: set `PAPER` in `tools/orchid_cite.py`, run `$Z metadata`, and on each published
   record press *Edit* and add *Related works*: "is supplement to" the paper (metadata edits do not need a new
   version). The Hugging Face card and the websites cite the same DOIs (writeback did that).
4. If something in a file is wrong: do not edit files in place; make a **New version** of that record (new DOI), then
   update `dois.json` and the paper macros.

## Not covered

- orchid-bench, orchid-pipeline, orchid-project.org and orchid-mcp are archived by the GitHub integration at their releases
  (`.zenodo.json` in each; no `grants` entry; the NSF funding is in the notes and, by hand, as a custom award).
- `ZENODO_LARGE_FILES.md` in the examples repository lists about 200 MB of raw outputs (MLIP runs, MCMC chains) that are
  meant for a further Zenodo record. It is not prepared here (the one-shot job is still running); it would be an eleventh
  record, deposited after this one and linked with `isSupplementTo` to `orchid-examples`.
