# Runbook: publishing the ORCHID Zenodo records (v2026.10)

For the PI. Ten records: the umbrella, eight datasets and the software record `orchid-examples`. Everything that can be
prepared is prepared; what remains are actions in your Zenodo account. Nothing in this repository calls Zenodo.
Commands are run in the website repository (`orchid-project.org`) with the data repository next to it. Run commands
through `z() { python3 -B tools/zenodo_release.py "$@"; }` and use `z plan`, `z metadata --check`, and the corresponding
subcommands below (a shell variable holding the command and its arguments does not split into words in default zsh):

```sh
cd ~/projects/orchid-project.org
z() { python3 -B tools/zenodo_release.py "$@"; }   # uses ../orchid-data and ../orchid-examples
```

Use the tested Python environment for the release tool and its Parquet builders, configuring `--parquet-python` where
required (on the Studio: `~/orchid-py313/bin/python`, which has pandas, pyarrow and ESPEI); record that environment with
the release.

Revised 2026-10-27 after Codex's X4 review of the ten records and of this runbook
(`~/projects/orchid-review-analysis-20261026/codex-round3-20261027/X4_report.md`).

Zenodo's web interface changes from time to time: the button and menu names below follow its help pages of October 2026
("Get a DOI now!", "Submit for review", "Add custom" for funding); if a label differs, the step is the same.

## What cannot be undone

- **Publishing a record is permanent.** A published record cannot be deleted by you and its DOI cannot be withdrawn.
  For ORCHID scientific changes, preserve the frozen release and publish a new version. Zenodo permits minor file
  corrections within 30 days of publication, with the amended draft republished within 45 days of the original
  publication; this platform capability does not replace ORCHID's versioning policy. Metadata (title, description,
  related works, funding, community, keywords) stays editable.
- A reserved DOI belongs to its draft for good; an abandoned draft can be deleted, but then its DOI is simply never
  registered, and a new draft gets a new DOI. Do not delete a draft whose DOI has been written into the data.
- The community identifier `orchid-calphad` cannot be changed after the community is created.
- The DOIs are written into ~36,000 files (`writeback`). A failed writeback can leave partial changes, and metadata
  alone is not a consistency check. Keep an untouched candidate snapshot and inspect the full writeback diff; after all
  rebuilds, run the builder checks, record-level cross-format checks, ESPEI membership checks and restricted-file
  checks, then regenerate and verify archive manifests. Never undo by resetting or checking out over the shared trees:
  discard the staged candidate instead (Step 3). After publication a correction is a new release.

## Pre-publish checklist (tick every line before the first Publish)

Restricted material, secrets, licences (run on the final tree after `writeback`; all must pass):

1. `z plan` prints `OK` (every file of every record present and unchanged, each record below 50 GB, one zip each, far
   below the 100-file default).
2. `z scan` prints `SCAN OK`: no PDF, page image, office file, key file or restricted path (`private/`, handbook page or
   crop folders) and no secret pattern (AWS, GitHub, Hugging Face, PyPI, OpenAI-style keys, private keys, publisher API-key
   headers) in any file of any record. Checked 2026-10-24 on the data of branch `zenodo-prep`: clean for the nine data
   records and for the examples (fifteen of the examples' own figures and `.npz` input tables are listed for one review;
   four cached manifests in `phaseforge-structures/cached/` contain a local absolute path).
3. `z metadata --check` and `z manifest --check` pass (the text and the file lists match the data).
4. `z card --check`, and `--check` of every builder on the staged candidate (Step 3).
5. **Verbatim quotes** (your decision of 2026-10-24: short quotes may be published with citation and page, never whole
   paragraphs): **resolved at export.** No released quote is longer than 500 characters (Parquet `literature_values`:
   5,743 quotes, median 172, maximum 500; `experimental_context`: 1,504, maximum 500). The 81 literature quotes (maximum
   985 characters before) and 55 context quotes (maximum 1,743) that were longer are clipped to a contiguous part of the
   original that keeps the printed value (word boundaries, no ellipsis added); `flags.quote_clipped` /
   `flag_quote_clipped` / `quote_clipped` mark them, `quote_page` is unchanged, the record store keeps the full quote.
   Permanent test: `tools/tests/test_release_integrity.py` (section 11) and `tools/tests/test_quote_clip.py`.
6. Licences: records are CC BY 4.0 (`orchid-examples`: MIT for code, `LICENSE-DATA.md` for data); third-party data
   (SGTE, Materials Project, OQMD CC BY 4.0; Kim et al. 2017 values MIT; Crossref metadata CC0) are stated in
   `NOTICE.md` and `LICENSES.md`, which are in every zip. Quotes stay under the publishers' copyright and are said so in
   the licence text of each record. Every dataset record also states the licence scope: "The stated licence covers the
   ORCHID-produced content in this deposit; upstream data and software retain their documented terms and attribution
   requirements, and no publisher pages, handbook drawings or restricted TDB source files are included." This is a scope
   correction, not a fresh legal clearance of every upstream asset: check the actual archive contents before publication
   (`z scan`, and the restricted-file checks of Step 3).
7. No `grants` key in any metadata file (`grep -l '"grants"' ../orchid-data/zenodo/*.json` prints nothing) and the
   community is `orchid-calphad` everywhere (`grep -rn '"identifier": "orchid"' ../orchid-data/zenodo` prints nothing).
8. Creator order and ORCHIDs (Arróyave, Saal, Shin) are the order you want on all ten records; they come from
   `AUTHORS` in `tools/orchid_cite.py`.

## Step 0. Before anything is reserved

1. The lock owner (`~/projects/ORCHID_COORDINATION.md`) first preserves the current work and prepares an isolated release
   candidate; reconcile the intended changes there, without resetting, cleaning, stashing or overwriting another agent's
   work. Do not rebase, reset or check out over the shared `orchid-data` and `orchid-project.org` trees. The formal
   dataset titles live in `tools/orchid_cite.py`; the data files embed them (`cite_as`), so the staged rebuild of Step 3
   also brings the data in line with the titles. Until then the builders' `--check` modes report stale `cite_as`
   titles: expected.
2. Choose the intended immutable examples commit, test its cached quick paths from that commit, and regenerate the
   manifest and metadata with that exact reference before proceeding: `z manifest --examples-ref <commit>`, then
   `z metadata`, `z manifest`, `z metadata --check`, `z plan`. Reproduction results apply only to the tested commit.
3. Optional: check whether NSF award 2608825 has appeared in Zenodo's database (it was absent on 2026-10-24):
   `curl -s 'https://zenodo.org/api/awards?q=2608825' | head -c 300`. If it has, use it instead of the custom award
   (`ZENODO_FUNDING_MANUAL.md`). Do the same for 2534344. An earlier dated lookup is not evidence of current indexing.

## Step 1. Create the community (once)

zenodo.org, Communities, New community. Identifier `orchid-calphad` (**permanent**; `orchid` and `orchid-project` belong to
other projects), title "ORCHID: Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery", public, a short
description with <https://orchid-project.org>, optional logo (`assets/logo/` in the website repository). Look at the
community's Settings: if you, as owner, can publish into your community without review, records go straight to
published when you press Publish; otherwise the button reads **Submit for review**, the record stays unpublished until
you **accept** it under the community's Requests (Step 6).

For every draft, enter both NSF awards 2608825 and 2534344 in the Funding section;
see `ZENODO_FUNDING_MANUAL.md` for indexed/custom award selection and the verified ARM-MIP title.

## Step 2. Reserve ten DOIs (Zenodo web, no files yet)

For each of the ten records (any order): *New upload*, resource type (Dataset; **Software** for `orchid-examples`), the
**title** from the table below, then in *Digital Object Identifier* answer "Do you already have a DOI?" with **No** and
press **Get a DOI now!** (save the draft first if the button is inactive), then **Save draft**. Do **not** publish. Do
not attach the community yet. Copy the DOI of each draft into the table and send it to Claude.

| # | record name | title (paste) | resource type | DOI (`10.5281/zenodo.`) |
|---|---|---|---|---|
| 1 | `literature` | ORCHID-Values: thermodynamic and phase-equilibrium values read from the literature | Dataset | |
| 2 | `espei` | ORCHID ESPEI datasets: literature and database-derived thermodynamic fitting inputs | Dataset | |
| 3 | `phase-diagrams` | ORCHID-Diagrams: calculated binary phase diagrams | Dataset | |
| 4 | `hulls` | ORCHID-Hulls: binary convex hulls (Materials Project, OQMD, assessed CALPHAD) | Dataset | |
| 5 | `dft-benchmark` | ORCHID-Parity: DFT-vs-experiment formation-enthalpy benchmark | Dataset | |
| 6 | `phase-registry` | ORCHID-Registry: phase registry of binary systems | Dataset | |
| 7 | `assessed-phase-assemblages` | ORCHID-Assemblages: assessed phase assemblages of binary systems | Dataset | |
| 8 | `bibliography` | ORCHID-Bibliography: papers and typed citation relations | Dataset | |
| 9 | `orchid-examples` | ORCHID examples: runnable workflows on the ORCHID data (PhaseForge+, ESPEI, one-shot MLIP phase diagrams, MLIP formation enthalpies, quickstart) | Software | |
| 10 | `orchid-data` | ORCHID data: umbrella record of the ORCHID datasets | Dataset | |

## Step 3. Write the DOIs into the release (Claude; the DOIs must be in the data before the zips are built)

Replace all ten placeholder DOIs and verify the reciprocal umbrella/component relations and version-specific archive
references before publication; add the paper identifier only when it exists, and test the advertised data endpoint
after hosting is explicitly approved and connected.

Require all ten distinct real DOI mappings before writeback, then search the complete release candidate and archive
contents for every `PENDING-` placeholder, including identifiers not present in the supplied map. `writeback` enforces
both (since 2026-10-27): it refuses a map that lacks any of the ten records, repeats a DOI or contains a placeholder,
and after substitution it searches every file of the candidate trees (text, binary, and `.gz` decompressed; `tools/`
code excepted) for `unassigned DOI marker` and fails if one remains.

**Do not run writeback against the shared live trees.** Its literature synchronization no longer deletes: a file present
only in `orchid-data/literature/` is moved to `~/projects/orchid-superseded/<date>-zenodo-writeback/<path>` and listed in
that folder's `README.md`. Its built-in rebuild, however, runs export → parity → sync once, without the calibrated
multi-pass sequence used for this release. Use a staged copy approved by the lock owner instead:

1. Prepare the staged candidate as in `~/data/private/orchid-ic3-fix-20261027/run_fix.sh` (rsync of the rebuilt folders
   into `<work>/staged-data/`, symlinks for the rest; the live tree is read only), and keep an untouched copy of it.
2. Substitute the DOIs in the staged candidate with `--no-rebuild` (all ten `--doi`; `--data <staged-data>`, and
   `--site`/`--examples` pointing at staged copies of those repositories):

   ```sh
   z --data <staged-data> --examples <staged-examples> writeback --site <staged-site> --dry-run \
      --doi literature=10.5281/zenodo.AAAAAAA --doi espei=... --doi phase-diagrams=... --doi hulls=... \
      --doi dft-benchmark=... --doi phase-registry=... --doi assessed-phase-assemblages=... --doi bibliography=... \
      --doi orchid-examples=... --doi orchid-data=...    # lists the files that would change; then without --dry-run,
                                                         # with --no-rebuild
   ```

   With `--no-rebuild` it reports the binary files (Parquet, `.gz`) that still carry placeholders: the rebuild below
   regenerates them, and the final search must be empty.
3. After DOI substitution, run the documented staged export, parity, calibration, re-export and bundle sequence until
   the derived outputs are stable (the order of `run_fix.sh`: export, parity, calibration rebuild, export, parity, ESPEI
   bundle, index, registry, TDB provenance, bibliography, Parquet, Zenodo metadata, card; then assessed assemblages,
   static pages and `add_cite_as` where their inputs changed); rebuild the Kim cross-check and other stale consumers
   before generating manifests.
4. Review DOI substitutions across all affected text files in each candidate repository, including examples source and
   configuration files, rather than assuming only README and citation files change. Inspect the full diff against the
   untouched copy.
5. Run every builder `--check`, the record-level cross-format checks (JSONL, CSV, Parquet), the ESPEI membership checks
   and the restricted-file checks; search the whole candidate once more for `unassigned DOI marker`; then `z manifest`,
   `z manifest --check`, `z metadata --check`.
6. Only then does the lock owner install the candidate into the live trees (moving superseded files to
   `~/projects/orchid-superseded/`, never deleting) and log it on the coordination board.

Then:

1. In `orchid-examples` commit the DOI change and **re-pin**: `z manifest --examples-ref <commit>`, then `z metadata`,
   `z manifest`, `z metadata --check`, `z manifest --check`.
2. Review `git diff` in the three repositories; commit only the intended paths (`git add <paths>`; never
   `git commit -a` across unrelated work); tag later (Step 7).
3. `z plan`, `z scan`, `z card --check` all green.
4. `z bundle` writes `dist/orchid-<name>-v2026.10.zip` (ten zips, about 190 MB in all; deterministic: a rebuild gives the
   same bytes), `dist/SHA256SUMS` and `dist/MD5SUMS` (Zenodo shows the MD5 of an uploaded file).
5. `z metadata --export dist/forms` writes one sheet per record (`dist/forms/<name>.form.html`) with every form field
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
4. **Funding**: Enter two separate Funding entries on every draft, for National Science Foundation awards 2608825 and
   2534344. Select the indexed award when available; otherwise enter a custom award with its verified official title and
   award URL, and confirm that both entries were saved (`ZENODO_FUNDING_MANUAL.md`).
5. **Community**: select `orchid-calphad` (only one community can be chosen at first submission).
6. **Save draft**, then *Preview*: title, creators, DOI (must equal the reserved one), licence, both funding chips,
   related works, description, one file.
7. Show it to Claude if you want a second pair of eyes (the previous dry run asked for this on every draft: this is the
   highest-stakes step).

## Step 5. Publish, in this order

Only after the final candidate passes its checks should the PI review the ten concrete drafts, both funding entries,
archive checksums and related identifiers, and perform the authorized publication steps.

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
   `z plan`, `z metadata --check`, `z manifest --check` and the builders' `--check` modes.
   Tag the repositories `v2026.10` (data, website, examples), push (needs your approval).
2. Paper (Claude): rerun `make_numbers.py` (macros `\doiUmbrella` ... `\doiExamples`, `\nZenodoRecords`=10,
   `\nZenodoDataRecords`=8, `\nZenodoSoftwareRecords`=1), rebuild `main.tex`, `main_arxiv.tex`, `si.tex`; fill the
   `orchid_data_2026` entry in `references.bib` with the umbrella DOI; replace `\doiPlaceholder{...}` for the code and
   the benchmark after their GitHub releases.
3. When the paper has an arXiv id or DOI: set `PAPER` in `tools/orchid_cite.py`, run `z metadata`, and on each published
   record press *Edit* and add *Related works*: "is supplement to" the paper (metadata edits do not need a new
   version). The Hugging Face card and the websites cite the same DOIs (writeback did that).
4. If something in a file is wrong: for ORCHID scientific changes, preserve the frozen release and publish a new version
   of that record (new DOI), then update `dois.json` and the paper macros. Zenodo permits minor file corrections within 30
   days of publication, with the amended draft republished within 45 days of the original publication; this platform
   capability does not replace ORCHID's versioning policy.

## Not covered

- orchid-bench, orchid-pipeline, orchid-project.org and orchid-mcp are archived by the GitHub integration at their releases
  (`.zenodo.json` in each; no `grants` entry; the NSF funding is in the notes and, by hand, as two Funding entries).
- `ZENODO_LARGE_FILES.md` in the examples repository lists about 200 MB of raw outputs (MLIP runs, MCMC chains) that are
  meant for a further Zenodo record. It is not prepared here (the one-shot job is still running); it would be an eleventh
  record, deposited after this one and linked with `isSupplementTo` to `orchid-examples`.
