# ORCHID bibliography

Every paper ORCHID knows about — the assessments and data papers it read, the original sources its values cite, the
assessments behind its TDB files, the original evaluations behind the assessed (handbook) diagrams, and discovery
leads — with Crossref bibliographic metadata, the role each paper plays in ORCHID, counts of the evidence ORCHID
released from it, and typed relations between papers, TDB files and handbook diagrams.

Release `v2026.10` (bibliography 0.1). Built by `tools/build_bibliography.py` (orchid-project.org;
deterministic, offline from a Crossref response cache; `--check` verifies these files).

## Counts

| | papers | with DOI |
|---|---:|---:|
| all | 9568 | 7812 |
| `corpus_assessment_read` | 1426 | 1411 |
| `cited_original_source` | 3576 | 3013 |
| `tdb_source_assessment` | 1886 | 1686 |
| `tdb_compilation` | 1 | 1 |
| `handbook_diagram_source` | 2283 | 1290 |
| `discovery_lead` | 2806 | 2806 |
| `context_source` | 0 | 0 |
| `espei_reference` | 1 | 1 |

Papers without a DOI: 1756 (ids derived from first author, year and title, flagged `no_doi`).
Crossref records: 7784 found, 28 DOIs unknown to Crossref (404),
0 not fetched; retrieved 2026-10-23 to 2026-10-23.
DOIs matched from a printed reference, checked against Crossref (first author, year +-1, title, journal):
5385 verified, 104 weak (kept, flagged),
23 unverifiable (no Crossref record); 19 mismatched
DOIs (22 matches) were dropped: those works are kept as no-DOI records with the
printed reference (`DOI_MISMATCHES.md`). The same scoped corrections are applied by every ORCHID exporter that emits
DOIs, from one versioned table (`doi_corrections.json`, v1.0.0).
Open-access licence deposited with Crossref: 326 papers. Chemical systems: 4126.

| edge type | edges |
|---|---:|
| `cites` | 3793 |
| `used_in_assessment` | 3793 |
| `models_system_in_tdb` | 3757 |
| `reassesses` | 1536 |
| `handbook_reproduces` | 2466 |
| `cited_by_crossref` | 44888 |

## Files

| file | content |
|---|---|
| `papers.jsonl` | one full record per paper (fields in SCHEMA.md) |
| `papers.csv`, `papers.parquet` | flat table, one row per paper (stable `id`) |
| `edges.jsonl`, `edges.csv`, `edges.parquet` | typed relations with provenance (stable `id`) |
| `papers/<key>.json` | one small JSON per paper: record + its relations (resolvable URL) |
| `index.json` | release info, counts, input hashes, id rule, URL templates and a compact search table (`columns`, `rows`) |
| `systems_index.json` | system -> role -> paper ids |
| `systems/<SYS>.json` | one system: papers by role, assessments with the data papers they used (and counts) |
| `orchid-bibliography.bib`, `orchid-bibliography.csl.json` | BibTeX and CSL-JSON generated from Crossref metadata (Crossref-backed records only) |
| `papers.jsonld`, `context.jsonld` | schema.org ScholarlyArticle graph (ORCID author ids, isPartOf journal, schema:citation edges, roles / evidence as additionalProperty) |
| `pages/` | static HTML pages per paper and per system (no JavaScript; JSON-LD and COinS embedded) |
| `parquet.json` | row counts, content hashes and Croissant field descriptions of the Parquet tables |
| `SCHEMA.md`, `CITATION.cff` | field reference; how to cite |

## How to use

```python
import pandas as pd
papers = pd.read_parquet("https://data.orchid-project.org/bibliography/papers.parquet")
edges = pd.read_parquet("https://data.orchid-project.org/bibliography/edges.parquet")
# original data papers used by the assessments of Al-Ni
import json, urllib.request
doc = json.load(urllib.request.urlopen("https://data.orchid-project.org/bibliography/systems/AL-NI.json"))
for a in doc["assessments"]:
    print(a["year"], a["title"], a["n_data_papers_used"])
```

One record: `https://data.orchid-project.org/bibliography/papers/<key>.json` with `key = "p" + sha256(id)[:16]`
(look up `key` by DOI in `index.json`). The ORCHID MCP server (`orchid-mcp`) exposes `get_paper`,
`search_papers`, `get_paper_relations` and `get_assessment_evidence` over these files.

## What is and is not here

- Bibliographic metadata only (no abstracts, no full text, no PDFs, no local paths). Crossref metadata is used as
  deposited. A DOI that an upstream matcher found for a printed reference is kept only when its Crossref record agrees
  with the printed reference (`doi_match`: verified or weak); mismatches are dropped and listed in `DOI_MISMATCHES.md`;
  `doi_corrections.json` is the shared correction table (context, scope, reason, printed citation) the other datasets
  apply, so a dropped DOI is null with `doi_status: dropped_mismatch` there too.
- Roles and evidence counts are derived from the ORCHID release files (literature values, ESPEI bundle, phase
  registry, assessed phase assemblages) and from the SGTE-corpus link tables; see `provenance` in each record.
- Edges are never inferred: `cites` / `used_in_assessment` come from the citation printed for each value ORCHID
  extracted; `cited_by_crossref` only from reference lists publishers deposited openly with Crossref, kept
  separate from ORCHID's own extraction and restricted to works in this bibliography; `reassesses` only when the
  later assessment cites the earlier one and both model the same exact system in a TDB file (method
  `citation+same-system`, never from dates alone). `supersedes` is not emitted (no source states supersession);
  `same_system` is not emitted as edges (use `systems_index.json`). No `context_source` papers yet: no same-system
  context manifest exists in the ORCHID sources.
- `discovery_lead` papers were found by the Crossref higher-order assessment discovery and were not read; their
  `candidate_systems_inferred` (citation closures) are hypotheses, only title-named systems enter `systems`.
- Open-access status is taken only from the Crossref `license` field.

## Licence

Crossref bibliographic metadata: CC0 (as distributed by Crossref). ORCHID-derived fields (roles, evidence counts,
relations, systems, checks): CC BY 4.0 — cite this bibliography: R. Arróyave, J. Saal, D. Shin, ORCHID bibliography (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-bibliography.
