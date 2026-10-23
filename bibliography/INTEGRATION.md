# Bibliography: integration notes (for the owners of the shared generators)

Written 2026-10-23 by the bibliography build. The bibliography is built by `orchid-project.org/tools/build_bibliography.py`
(offline, deterministic, `--check`) into `orchid-data/bibliography/`. The shared generators (`build_static_pages.py`,
`zenodo_release.py manifest/card`) were **not** run, and `orchid_cite.py` / `zenodo_release.py` were **not** edited: at the
start of this work they (and `orchid-data/zenodo/`) had uncommitted edits by another agent (committed at 09:32 as ebd83a20 /
b3b20af4), and registering a dataset in `orchid_cite.DATASETS` changes the umbrella pages of `build_static_pages.py` and the
Zenodo manifests, whose `--check`s would then fail until their owner reruns them. Until then `build_bibliography.py`
registers the dataset at run time (`cite_module()`, the pattern of `build_espei_bundle.py`), so its `cite_as` blocks already
have the standard form. The changes the shared generators need are listed here.

Rebuild:

```bash
cd ~/projects/orchid-project.org
~/orchid-py313/bin/python tools/build_bibliography.py fetch     # only if new DOIs: network, read-only Crossref, cached
~/orchid-py313/bin/python tools/build_bibliography.py build     # offline from build-cache/crossref (git-ignored)
~/orchid-py313/bin/python tools/build_bibliography.py build --check
~/orchid-py313/bin/python tools/tests/test_bibliography.py
```

Inputs are hashed in `index.json` -> `inputs`. Rebuild after any of them changes, in particular:
- `assessed-phase-assemblages/records.csv` (the per-paper `assessed_assemblage_records` counts come from it; built from
  the version committed in b3b20af4);
- the discovery leads are read with `git show` from the open-tdb branch `discovery/forward-citations` (commit 9578e363),
  file `catalog/discovery/higher-order-assessment-targets.json`; rebuild if that branch moves or is merged (then point
  `DISCOVERY_REF` at master).

## 1. orchid_cite.py (dataset registry)

Make the run-time registration of `build_bibliography.cite_module()` permanent:

```python
THIRD_PARTY["papers_bibliography"] = "the papers themselves when you use their data (doi / citation of each bibliography record)"
DATASETS["bibliography"] = ("ORCHID bibliography", "orchid_bibliography_2026", ["papers_bibliography"])
EXTRACTED.add("bibliography")
STATUS_BY["bibliography"] = ("Version 1, machine-extracted: roles and evidence counts derive from machine-extracted literature "
                             "values and link tables; bibliographic fields are Crossref metadata as deposited (DOI mismatches "
                             "flagged in doi_check).")
ABSTRACT["bibliography"] = ("Every paper ORCHID knows about: Crossref bibliographic metadata (CC0), the role of each paper in "
                            "ORCHID, counts of the evidence released from it, and typed relations with provenance (citations of "
                            "values, TDB files, reassessments, handbook diagrams, Crossref reference lists).")
```

(`cite_module()` is a no-op once the name exists, so the bibliography output does not change.) Then rerun
`build_static_pages.py` (umbrella pages list the datasets) and the Zenodo `manifest`/`card` steps.

Licence note for `LICENSES.md` / `NOTICE.md`: Crossref bibliographic metadata is CC0 (Crossref metadata licence);
ORCHID-derived bibliography fields are CC BY 4.0.

## 2. zenodo_release.py and zenodo/

- `zenodo/dois.json`: add `"bibliography": "10.5281/zenodo.PENDING-bibliography"`.
- `RECORDS["bibliography"] = (DOCS + ["zenodo/bibliography.metadata.json", "bibliography/**"], ["bibliography/pages/**"])`
  (pages are a website view, as for `phases/pages/**`; `INTEGRATION.md` may also be excluded).
- `DATA_DIRS += ("bibliography",)`.
- In the Parquet verification step, read `bibliography/parquet.json` like `assessed-phase-assemblages/parquet.json`:
  two tables (`papers`, `edges`), each with `rows`, `csv_sha256`, `content_sha256` (sha256 of the canonical JSON rows,
  sorted keys, joined by `\n`).
- `zenodo/bibliography.metadata.json`: the draft below (same layout as `phase-registry.metadata.json`).

## 3. build_static_pages.py (pages, sitemap, llms.txt)

The per-paper and per-system pages are already written by `build_bibliography.py` (into `bibliography/pages/`,
covered by its `--check`). `tools/bibliography_pages.py` is the hook if the shared generator should own them:

```python
import bibliography_pages
out.update(bibliography_pages.pages_from_files(DATA))   # {"bibliography/pages/...": html}; identical bytes
```

(`OWN_DIRS` needs `"bibliography/pages"` only if the shared generator takes over writing and cleaning them.)
Pages are JavaScript-free, link `bibliography/pages/style.css` (the phase-page palette), and embed schema.org JSON-LD
(ScholarlyArticle; Dataset on system pages) plus a COinS span (Zotero / Mendeley). Highwire `citation_*` meta tags
were deliberately not added: Google Scholar reads them as "this page is the article", which these pages are not.

Links to add:
- data root `index.html` / `index.md`: a "Bibliography" entry -> `bibliography/pages/index.html` (and the files list:
  `bibliography/papers.parquet`, `edges.parquet`, `papers.jsonl`, `orchid-bibliography.bib`).
- system pages `systems/<SYS>.html`: "papers (bibliography)" -> `../bibliography/pages/systems/<SYS>.html` when that file
  exists (4,125 systems, including ternaries and higher).
- `papers/index.html`: per paper, a link to `../bibliography/pages/papers/<key>.html` with
  `key = "p" + sha256(id)[:16]` (id = `doi:<doi>`; literature `ref:` ids are listed in each record's `aliases`).

`sitemap.xml` entries (data site):

```
https://data.orchid-project.org/bibliography/pages/index.html
https://data.orchid-project.org/bibliography/pages/systems/<SYS>.html      (one per file in bibliography/pages/systems/)
https://data.orchid-project.org/bibliography/pages/papers/<key>.html       (one per file in bibliography/pages/papers/)
https://data.orchid-project.org/bibliography/README.md
https://data.orchid-project.org/bibliography/SCHEMA.md
```

`llms.txt` lines:

```
- [ORCHID bibliography](https://data.orchid-project.org/bibliography/README.md): every paper ORCHID knows (9,560; roles, evidence counts, typed relations). One paper: https://data.orchid-project.org/bibliography/papers/<key>.json (key = "p" + sha256("doi:<lowercase doi>")[:16]; lookup table in bibliography/index.json); one system: https://data.orchid-project.org/bibliography/systems/<SYS>.json (assessments and the data papers they used); tables: bibliography/papers.parquet, bibliography/edges.parquet; field reference: bibliography/SCHEMA.md
```

`llms-full.txt`: append `bibliography/README.md` and the "Ids", "Roles" and "Edges" sections of `bibliography/SCHEMA.md`.

## 4. Hugging Face card (`hf/README.md`) and Croissant

```yaml
- config_name: bibliography_papers
  data_files:
  - split: full
    path: bibliography/papers.parquet
- config_name: bibliography_edges
  data_files:
  - split: full
    path: bibliography/edges.parquet
```

Card text: "`bibliography_papers`: one row per paper (stable `id`: `doi:<doi>` or `nodoi:<hash>`), Crossref metadata,
roles, value counts; `bibliography_edges`: one row per typed relation (stable `id`), `src`/`dst` paper ids, provenance.
Join edges to papers on `src`/`dst` = `id`. Licence: Crossref metadata CC0, ORCHID fields CC BY 4.0."

Croissant (`data/croissant.json` on the website): two `cr:RecordSet`s, `bibliography_papers` and
`bibliography_edges`, `cr:FileObject` `bibliography/papers.parquet` / `edges.parquet` (sha256 of the files), keys
`id`; field names, `dataType` and descriptions are in `bibliography/parquet.json` -> `fields` (also the column tables
of `SCHEMA.md`).

## 5. orchid-mcp

Committed in `~/projects/orchid-mcp` (no version bump): `get_paper(doi, fields)` extended with the bibliography entry,
new `search_papers`, `get_paper_relations`, `get_assessment_evidence`, resource `orchid://bibliography-schema`,
OpenAPI paths under `/bibliography/`, tests with the fixture `tests/fixtures/bibliography-data` (NI-TI papers).
When a new mcp release is cut, the data site must serve `bibliography/index.json`, `bibliography/papers/<key>.json`
and `bibliography/systems/<SYS>.json`.

## 6. Zenodo record draft (`zenodo/bibliography.metadata.json`)

Not written into `zenodo/`: the umbrella record's file rules include `zenodo/*.metadata.json`, so a new file there changes
the `orchid-data` manifest (owner reruns `zenodo_release.py manifest`). Copy this JSON to `zenodo/bibliography.metadata.json`
together with the `RECORDS` change.

```json
{
 "_comment": "DRAFT (bibliography agent, 2026-10-23). Zenodo deposition metadata in the legacy REST format, same layout as zenodo/phase-registry.metadata.json; to be written to zenodo/bibliography.metadata.json by whoever owns zenodo/ (the folder had uncommitted edits by another agent).",
 "record": "bibliography",
 "doi": "10.5281/zenodo.PENDING-bibliography",
 "metadata": {
  "title": "ORCHID bibliography",
  "upload_type": "dataset",
  "version": "2026.10",
  "description": "<p><b>ORCHID bibliography</b>, version 2026.10: every paper the ORCHID CALPHAD data project knows about, with Crossref bibliographic metadata, the role each paper plays in ORCHID, counts of the evidence ORCHID released from it, and typed relations. Part of the ORCHID data release v2026.10.</p><h3>What</h3><ul><li>9,560 works (7,825 with DOI; 1,735 without, with stable ids from first author, year and title): 1,422 read by ORCHID, 3,572 cited as the original source of extracted values, 1,883 assessments behind TDB files, 2,283 original evaluations behind assessed (handbook) diagrams, 2,806 discovery leads (Crossref higher-order assessment discovery, not read).</li><li>60,239 typed edges with provenance: cites / used_in_assessment (3,784 each; from the citation printed for each extracted value), models_system_in_tdb (3,760), reassesses (1,538; citation + same exact system, never from dates), handbook_reproduces (2,466), cited_by_crossref (44,907; publisher-deposited reference lists, kept separate).</li><li>Files: papers.jsonl/.csv/.parquet, edges.jsonl/.csv/.parquet, papers/&lt;key&gt;.json (one record per paper), systems/&lt;SYS&gt;.json and systems_index.json, BibTeX and CSL-JSON (Crossref metadata), papers.jsonld (schema.org ScholarlyArticle), SCHEMA.md, CITATION.cff.</li></ul><h3>How</h3><p>Deterministic builder (tools/build_bibliography.py) over the ORCHID release files (literature values, ESPEI bundle, phase registry, assessed phase assemblages), the SGTE-corpus link tables and handbook source lines, and a cache of Crossref REST API responses (retrieved 2026-10-23). No model calls; no abstracts, full text or PDFs.</p><h3>Limitations</h3><ul><li>Crossref metadata as deposited; doi_check flags DOIs whose Crossref record disagrees with the printed reference (mismatch suspects are kept, not removed).</li><li>Open-access status only from the Crossref license field.</li><li>Discovery leads were not read; their inferred candidate systems are hypotheses.</li><li>Version 1, machine-extracted: evidence counts derive from machine-extracted values.</li></ul><h3>Licence</h3><p>Crossref bibliographic metadata: CC0. ORCHID-derived fields (roles, evidence counts, relations, checks): CC BY 4.0.</p><h3>How to cite</h3><p>R. Arróyave, J. Saal, D. Shin, ORCHID bibliography (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-bibliography</p><p>This work was supported by the U.S. National Science Foundation under award OAC-2608825 (CSSI Elements: PhaseForge).</p>",
  "creators": [
   {
    "name": "Arróyave, Raymundo",
    "affiliation": "Texas A&M University",
    "orcid": "0000-0001-7548-8686"
   },
   {
    "name": "Saal, James",
    "affiliation": "Citrine Informatics",
    "orcid": "0000-0003-0935-158X"
   },
   {
    "name": "Shin, Dongwon",
    "affiliation": "Oak Ridge National Laboratory",
    "orcid": "0000-0002-5797-3423"
   }
  ],
  "keywords": [
   "bibliography",
   "citation graph",
   "CALPHAD",
   "thermodynamic assessment",
   "phase diagrams",
   "provenance",
   "Crossref",
   "AI-ready data"
  ],
  "license": "cc-by-4.0",
  "access_right": "open",
  "language": "eng",
  "grants": [
   {
    "id": "10.13039/100000001::2608825"
   }
  ],
  "communities": [
   {
    "identifier": "orchid"
   }
  ],
  "related_identifiers": [
   {
    "identifier": "10.5281/zenodo.PENDING-orchid-data",
    "relation": "isPartOf",
    "resource_type": "dataset",
    "scheme": "doi"
   },
   {
    "identifier": "10.5281/zenodo.PENDING-literature",
    "relation": "isDerivedFrom",
    "resource_type": "dataset",
    "scheme": "doi"
   },
   {
    "identifier": "10.5281/zenodo.PENDING-phase-registry",
    "relation": "references",
    "resource_type": "dataset",
    "scheme": "doi"
   },
   {
    "identifier": "10.1016/j.calphad.2025.102833",
    "relation": "references",
    "resource_type": "publication-article",
    "scheme": "doi"
   },
   {
    "identifier": "https://data.orchid-project.org/bibliography/",
    "relation": "isIdenticalTo",
    "resource_type": "dataset",
    "scheme": "url"
   }
  ]
 }
}
```
