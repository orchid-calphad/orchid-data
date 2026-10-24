# Contributing data to ORCHID

This folder holds contributions that are waiting for review or that were accepted for the next release. You do not
need to use it to help: the quickest ways are on GitHub's issue forms.

| I want to... | do this |
|---|---|
| report a wrong value | click **report** next to the value on its data page (it opens a pre-filled issue), or open the issue form [Report an error in a value](https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml) |
| suggest a paper or an assessment | issue form [Suggest a paper or assessment](https://github.com/orchid-calphad/orchid-data/issues/new?template=suggest-paper.yml), or add a line to `papers/queue.jsonl` |
| fix several values at once | a pull request adding a file to `corrections/` |
| add values I read from a paper | a pull request adding a file to `data/` (copy `data/TEMPLATE.json` or `data/TEMPLATE.csv`; type B) |
| add my own measurements | deposit them first with a DOI (e.g. Zenodo), then a pull request to `data/` (type C) |
| add calculated data (DFT, CALPHAD) | a pull request to `data/` with the method metadata (type D) |
| add an assessment (TDB file) | a pull request adding `tdb/<name>/` with the file and `metadata.json` (type E) |

Every value is an observation of an equilibrium state: give its phases, temperature, pressure, composition and, for
formation and mixing quantities, the reference state, together with the evidence class (experimental, model or DFT),
the source (a DOI) and, for values read from a paper, the printed page and the sentence or table row that states it
(at most 240 characters). Uncertainties are given as separate components (printed, method, composition, scatter,
conversion), as in the release.

Check your file before you open the pull request:

```sh
python3 contributions/tools/orchid_contrib.py validate contributions/data/my-values.json
```

The same check runs on every pull request. Field reference, all checks and the maintainers' acceptance procedure:
[SCHEMA.md](SCHEMA.md). Contributions are released under CC BY 4.0 with credit to you; see
[CONTRIBUTING.md](../CONTRIBUTING.md) for credit, licences and the code of conduct.

`examples/` holds three synthetic pull-request payloads used by the tests (one valid correction, one invalid, one
data contribution); they are not contributions.
