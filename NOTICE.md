# NOTICE: sources, attribution and licences of the ORCHID data release

This file names every third-party source whose data are included in, or were used to derive, the ORCHID data
release, with its licence, the citation it requires and, where CC BY 4.0 requires it, a statement of the changes made.
The licence of each folder is summarised in `LICENSES.md`. ORCHID's own data are © 2026 the ORCHID authors
(R. Arróyave, J. E. Saal, D. Shin) and licensed under CC BY 4.0 (`LICENSE`).

## ORCHID data (CC BY 4.0)

The literature values, the phase registry, the assessed phase-assemblage points, the calculated phase diagrams and
hulls, the ESPEI datasets, the DFT benchmark and the ORCHID fields of the bibliography were produced by the ORCHID
project. Cite the ORCHID release (`CITATION.cff`, DOIs in `zenodo/dois.json`) and, for each value used, its source
paper (`paper_citation`, `paper_doi`) and, for values the paper re-lists from earlier work, the cited original
(`cited_dois`, `cited_sources`).

## Quotations from published papers (publishers' copyright; not relicensed)

Each literature value carries a short verbatim excerpt of its source (one sentence of running text, or a table
caption and the row it was read from) in the `quote` field, and the static pages show these excerpts. They are kept
only so that the value can be verified against the page it came from. They remain under the copyright of their
publishers, are reproduced as short quotations, and are **not** covered by the CC BY 4.0 licence of ORCHID's data.
The source papers, page images and full texts are not redistributed.

## SGTE binary collection (CC BY 4.0)

Source and citation: B. Hallstedt, "The SGTE collection of binary datasets", *Calphad* 89 (2025) 102833,
<https://doi.org/10.1016/j.calphad.2025.102833>. The article and its supplementary TDB files are published under
CC BY 4.0 (<https://creativecommons.org/licenses/by/4.0/>; licence as deposited with Crossref for the version of
record). Each TDB file names its original assessment in its header; cite both Hallstedt (2025) and that assessment.

Used in: `phase-diagrams/` (diagrams calculated from each file), `hulls/calphad-sgte/` (isotherms), `phases/` (phase
names, models and verbatim PHASE / CONSTITUENT / TYPE_DEFINITION statements), the CALPHAD cross-checks of
`literature/` and `assessed-phase-assemblages/`, and the phase names of the ESPEI datasets.

Statement of changes: no TDB file is redistributed here. Phase equilibria were calculated from the unmodified files
with pycalphad (grids, boundaries, invariants, isotherms); the verbatim statements in `phases/` are copied unchanged
(only line breaks normalised), each with the file's path and SHA-256.

## Materials Project (CC BY 4.0)

Source: <https://materialsproject.org>, database release 2026.04.13, GGA/GGA+U energies with the MP2020 compatibility
corrections, retrieved through the Materials Project API. Licence: CC BY 4.0 (terms of use,
<https://legacy.materialsproject.org/terms>). Cite: A. Jain et al., "Commentary: The Materials Project: A materials
genome approach to accelerating materials innovation", *APL Materials* 1 (2013) 011002,
<https://doi.org/10.1063/1.4812323>, and the release identifier recorded with the data.

Used in: `hulls/dft-mp/`, `literature/dft_parity.json`, `espei/dft/mp/`, the DFT names of `phases/`.
Statement of changes: selected fields (formation energy per atom, energy above hull, structure identifiers) were
retrieved and normalised into a snapshot; ORCHID built convex hulls from it, paired the energies with literature
values (kJ/mol-atom) and wrote ESPEI datasets. Energies are not recomputed.

## OQMD (CC BY 4.0)

Source: <https://oqmd.org>, version 1.8, formation energies of the `standard` fit. Licence: CC BY 4.0 (download page,
<https://oqmd.org/download/>). Cite: J. E. Saal et al., "Materials design and discovery with high-throughput density
functional theory: the Open Quantum Materials Database (OQMD)", *JOM* 65 (2013) 1501,
<https://doi.org/10.1007/s11837-013-0755-4>; S. Kirklin et al., "The Open Quantum Materials Database (OQMD):
assessing the accuracy of DFT formation energies", *npj Comput. Mater.* 1 (2015) 15010,
<https://doi.org/10.1038/npjcompumats.2015.10>.

Used in: `hulls/dft-oqmd/`, `literature/dft_parity.json`, `espei/dft/oqmd/`, the DFT names of `phases/`.
Statement of changes: formation energies and stabilities were read from a local copy of the database into a snapshot;
ORCHID built convex hulls from it (elemental end points at zero), paired the energies with literature values and
wrote ESPEI datasets. Energies are not recomputed. OQMD and Materials Project energies use different references and
are never averaged.

## Kim et al. 2017 experimental formation enthalpies (MIT)

Source: G. Kim, S. V. Meschel, P. Nash, W. Chen, "Experimental formation enthalpies for intermetallic phases and
other inorganic compounds", *Scientific Data* 4 (2017) 170162, <https://doi.org/10.1038/sdata.2017.162> (article
CC BY 4.0). The table used is the CSV re-deposited on Figshare, "Expt Formation Enthalpy Data",
<https://doi.org/10.6084/m9.figshare.7289723> (G. Kim, S. V. Meschel, P. Nash, W. Chen, Hacking Materials, 2018),
licensed under the MIT licence (Figshare records the licence without a separate copyright line; the holders are
the authors of the Figshare item):

> Copyright (c) 2018 G. Kim, S. V. Meschel, P. Nash, W. Chen, Hacking Materials
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
> documentation files (the "Software"), to deal in the Software without restriction, including without limitation
> the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
> permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of
> the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
> WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
> COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
> OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Used in: `literature/kim2017_crosscheck.json` and `.md`, which list, for the formulas in common with ORCHID, the
median of the Kim et al. values per formula next to the ORCHID values. The full CSV is not redistributed.

## Crossref metadata (CC0)

`bibliography/` holds bibliographic metadata retrieved read-only from the Crossref REST API (titles, authors and ORCID
iDs, venues, volumes, pages, dates, licence URLs, citation counts and publisher-deposited reference lists; retrieval
dates in each record). Crossref makes this metadata available under CC0
(<https://www.crossref.org/documentation/retrieve-metadata/rest-api/>). No abstracts, full text or PDFs are kept.
The ORCHID fields of the bibliography (roles, evidence counts, typed relations, systems, DOI checks) are CC BY 4.0.

## Handbook-derived points (`assessed-phase-assemblages/`)

The assessed phase-assemblage points were obtained from the binary diagrams compiled in H. Okamoto, *Desk Handbook:
Phase Diagrams for Binary Alloys*, 2nd ed., ASM International (2010), each of which reproduces an evaluation
published earlier (cited per point as `original_citation`, with the handbook as the compilation). ORCHID traced the
printed boundary lines of each diagram, located its phase fields, and placed one point deep inside each field. The
released data are ORCHID's own measurements of where these fields lie: a temperature, a composition and a pressure
per point, the names of the phases present there, ORCHID's naming basis and confidence, a positional margin, the
cross-check against the SGTE assessments, and the citations. No drawing, page image, crop, rendering, traced line set
or text of the handbook (other than phase names and citations) is included; the build refuses any such content.
Users who need the diagrams themselves should consult the handbook or the cited evaluations.

## Software used to produce the data (not redistributed)

pycalphad (MIT), ESPEI (MIT), NumPy, SciPy and pyarrow were used to calculate and validate the data. No third-party
code is included in this repository.
