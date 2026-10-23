# ESPEI bundle: integration steps (for the PI; not part of the release)

The bundle is written by `tools/build_espei_bundle.py` (orchid-project.org) into `<orchid-data>/espei/`. Nothing
below has been run: no shared generator, manifest or Zenodo file was touched. Exclude this file from the record
(pattern below) or delete it after integration.

## 1. `tools/orchid_cite.py`: register the record

The builder registers exactly this entry at run time when it is missing, so its outputs do not change when the
patch lands (README, CITATION.cff and `index.json` `cite_as` stay byte-identical).

```python
THIRD_PARTY["papers_espei"] = ("the original source of every value you use (each dataset's `reference` / `bibtex`, "
                               "references.bib; index.csv lists the DOIs)")
EXTRACTED |= {"espei"}
ABSTRACT["espei"] = ("ESPEI-format datasets (thermochemical, phase-equilibrium ZPF and invariant-reaction ZPF) built from "
                     "the ORCHID literature values, one folder per evidence class (experimental, model, DFT: literature, "
                     "Materials Project, OQMD), every value traced to its published ORCHID observation id and source DOI, "
                     "with its uncertainty in physical units (printed, ESPEI's experimental default, or calibrated for "
                     "DFT against experiment) and the ESPEI weight derived from it.")
DATASETS["espei"] = ("ORCHID ESPEI datasets from the literature", "orchid_espei_2026", ["papers_espei", "mp", "oqmd"])
```

(put the entries in the literal dicts; `NAMES = tuple(DATASETS)` then includes `espei`; `zenodo/dois.json` gets the
placeholder `10.5281/zenodo.PENDING-espei` from `dois()` until writeback.)

## 2. `tools/zenodo_release.py`

```python
# module docstring, record list:
#   espei   ORCHID ESPEI datasets from the literature   espei/ (ESPEI JSON per evidence class, index, calibration)
RECORDS["espei"] = (DOCS + ["zenodo/espei.metadata.json", "espei/**"], ["espei/INTEGRATION.md"])
DATA_DIRS = (..., "espei")
# cmd_writeback: steps, after "sync" and after build_phase_registry (reads literature/, phases/, hulls/,
# literature/dft_parity.json):
[py, "tools/build_espei_bundle.py", "--data", a.data]          # needs ~/.venvs/espei/bin/python (--espei-python)
# checks:
[py, "tools/build_espei_bundle.py", "--data", a.data, "--check"]
```

`assert set(RECORDS) == set(orchid_cite.NAMES)` holds once both edits are in.

## 3. `zenodo/espei.metadata.json` (draft; same format as the other records)

```json
{
 "_comment": "Zenodo deposition metadata (legacy REST format). DOI placeholders 10.5281/zenodo.PENDING-<name> are replaced by tools/zenodo_release.py writeback.",
 "record": "espei",
 "doi": "10.5281/zenodo.PENDING-espei",
 "metadata": {
  "title": "ORCHID ESPEI datasets from the literature",
  "upload_type": "dataset",
  "version": "2026.10",
  "description": "<p><b>ORCHID ESPEI datasets from the literature</b>: ESPEI 0.9.1 datasets built from the ORCHID literature values and from DFT, one folder per evidence class: <code>experimental/</code> (thermochemical and phase-composition ZPF tables), <code>invariants/</code> (ZPF from invariant-reaction tables), <code>model/</code> (values the papers calculated with a CALPHAD model, TDB SHA-256), <code>dft/literature</code>, <code>dft/mp</code>, <code>dft/oqmd</code> (HM_FORM of TDB phase endmembers, mapped through the ORCHID phase registry). Every literature value carries its ORCHID observation id and source DOI and passes the inclusion rules of the published literature values; every value carries its uncertainty in physical units (printed; ESPEI's experimental default where none was printed; DFT sigma calibrated against experiment, leave-system-out) and the ESPEI weight derived from it. Validated with ESPEI 0.9.1 check_dataset and load_datasets (VALIDATION.md). Part of the ORCHID data release v2026.10.</p><h3>Limitations</h3><ul><li>Version 1, machine-extracted literature values.</li><li>Model-calculated values have no measurement uncertainty: choose your own weight.</li><li>0 K DFT energies are used as 298.15 K enthalpies; DFT residuals are heavy-tailed.</li><li>Use one DFT source per fit (different elemental references).</li></ul><h3>Licence</h3><p>Derived data CC BY 4.0; Materials Project and OQMD data CC BY 4.0. Source papers are not redistributed.</p>",
  "creators": [
   {"name": "Arróyave, Raymundo", "affiliation": "Texas A&M University", "orcid": "0000-0001-7548-8686"},
   {"name": "Saal, James", "affiliation": "Citrine Informatics", "orcid": "0000-0003-0935-158X"},
   {"name": "Shin, Dongwon", "affiliation": "Oak Ridge National Laboratory", "orcid": "0000-0002-5797-3423"}
  ],
  "keywords": ["ESPEI", "CALPHAD", "thermodynamics", "phase diagrams", "ZPF", "DFT", "formation enthalpy", "uncertainty", "AI-ready data"],
  "license": "cc-by-4.0",
  "access_right": "open",
  "language": "eng",
  "grants": [{"id": "10.13039/100000001::2608825"}],
  "communities": [{"identifier": "orchid"}],
  "related_identifiers": [
   {"identifier": "10.5281/zenodo.PENDING-orchid-data", "relation": "isPartOf", "resource_type": "dataset", "scheme": "doi"},
   {"identifier": "10.5281/zenodo.PENDING-literature", "relation": "isDerivedFrom", "resource_type": "dataset", "scheme": "doi"},
   {"identifier": "10.5281/zenodo.PENDING-hulls", "relation": "isDerivedFrom", "resource_type": "dataset", "scheme": "doi"},
   {"identifier": "10.5281/zenodo.PENDING-phase-registry", "relation": "references", "resource_type": "dataset", "scheme": "doi"},
   {"identifier": "https://orchid-project.org", "relation": "isSupplementTo", "scheme": "url"},
   {"identifier": "10.1063/1.4812323", "relation": "references", "scheme": "doi"},
   {"identifier": "10.1007/s11837-013-0755-4", "relation": "references", "scheme": "doi"},
   {"identifier": "10.1038/npjcompumats.2015.10", "relation": "references", "scheme": "doi"}
  ],
  "notes": "This work was supported by the U.S. National Science Foundation under award OAC-2608825 (CSSI Elements: PhaseForge)."
 }
}
```

The umbrella `zenodo/orchid-data.metadata.json` needs `hasPart 10.5281/zenodo.PENDING-espei` and the abstract
sentence listing the records.

## 4. Other generators / documents (inputs only; run by the PI)

- `tools/build_static_pages.py`: iterates `orchid_cite.NAMES`, so the dataset list and the record count pick up
  `espei` after step 1 (re-run; no code change needed unless a dedicated page is wanted).
- `llms.txt`, `llms-full.txt`, `sitemap.xml` / `sitemap-pages.xml`: add `espei/README.md`, `espei/index.csv`,
  `espei/VALIDATION.md`, `espei/UNCERTAINTY_SUMMARY.md`, `espei/dft/CALIBRATION.md`.
- `DATASET_CARD.md`, `README.md`, `CHANGELOG.md` of orchid-data: one section / line for the ESPEI record.
- `tools/build_parquet.py`: optional (an `espei_index.parquet` from `espei/index.csv`); not required.
- `zenodo_release.py manifest` and `card` afterwards (as usual).

## 5. Order and freshness

- Inputs: `literature/` (export + sync), `literature/dft_parity.json`, `phases/` (phase registry), `hulls/`. Run the
  builder after those, then `--check`.
- At build time the published literature release (`literature/`) predates the current record store
  (`export_literature_data.py --check` reports it out of date) and does not carry `reader_agreement`. The bundle is
  gated on the published release; reader agreement comes from the record store (`reader_agreement_source:
  record_store`). After the literature export is re-run, re-run this builder: the gate, the DFT calibration pairs
  and reader agreement then follow the new release.
