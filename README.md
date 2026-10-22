# ORCHID data

Open data of the **ORCHID** project (Open Repository for CALPHAD Hypotheses, Intelligence, and Discovery),
served at <https://data.orchid-project.org> and browsable at <https://orchid-project.org>.

| Folder | Content |
|---|---|
| `literature/` | Thermodynamic and phase-equilibrium values read from published papers: one JSON per chemical system (`systems/`), full dumps (`orchid-literature.csv.gz`, `orchid-literature.jsonl.gz`), papers, experimental contexts, DFT-vs-experiment parity data. Fields are documented in `literature/SCHEMA.md`. |
| `phase-diagrams/` | Binary phase diagrams calculated with pycalphad from the SGTE binary collection (Hallstedt 2025, CC BY 4.0), each tied to its TDB file by SHA-256. |
| `hulls/` | Binary convex hulls from the Materials Project and OQMD (CC BY 4.0) and assessed CALPHAD isotherms. |

## Licence and attribution
Derived data: **CC BY 4.0** — cite ORCHID and the original sources. Each literature value carries its citation, DOI,
page and the one sentence it was read from (quoted under fair use). Source papers, page images and full texts are not
redistributed. Third-party data (SGTE, Materials Project, OQMD) keep their own licences and citations: see `NOTICE.md`
and `LICENSES.md`.

## Citing
See `CITATION.cff`. Versioned releases are archived on Zenodo with a DOI.

Authors: R. Arróyave (Texas A&M University), J. Saal (Citrine Informatics), D. Shin (Oak Ridge National Laboratory).
