# Contributing to ORCHID data

ORCHID gets better when the people who use it tell us where it is wrong and what it is missing. Every contribution
is checked against its source before it reaches a release, and every accepted contribution is credited.

## Ways to help

**Report a wrong value.** Every value on [data.orchid-project.org](https://data.orchid-project.org) has a
**report** link that opens a pre-filled issue ([Report an error in a value](https://github.com/orchid-calphad/orchid-data/issues/new?template=report-value-error.yml)).
Tell us what the paper prints, on which page, and copy the one sentence or table row that shows it (at most 240
characters). AI assistants using the ORCHID MCP server get the same link as `report_issue_url` with every value.

**Suggest a paper or assessment.** Use [Suggest a paper or assessment](https://github.com/orchid-calphad/orchid-data/issues/new?template=suggest-paper.yml)
with the DOI(s), the system and the kind of data, or add a line to `contributions/papers/queue.jsonl` (type A).
Please send DOIs, never PDFs.

**Correct many values at once.** Add a file to `contributions/corrections/` (one JSON line per correction: record
id, field, old value, new value, page and quote, your name and optional ORCID, licence consent).

**Contribute data** by pull request to `contributions/` (copy the templates in `contributions/data/`):

| type | what | needs |
|---|---|---|
| B | values you read from a published paper | DOI, printed page, quote |
| C | your own new measurements | a citable DOI: the paper, or a deposited dataset (deposit unpublished data first, e.g. on Zenodo) |
| D | calculated data (DFT, CALPHAD, ...) | DOI and method metadata (code, functional; software, TDB); evidence class `dft` or `model` |
| E | a CALPHAD assessment (TDB file) | `contributions/tdb/<name>/`: the file, the assessment DOI and an open licence |

Every value is an observation of an equilibrium state, not a bare number: give its phases, temperature, pressure,
composition and (for formation and mixing quantities) reference state, its evidence class (experimental, model or
DFT; never mixed), its source, and its uncertainty as separate components (printed, method, composition, scatter,
conversion). The field reference and every check are in [contributions/SCHEMA.md](contributions/SCHEMA.md).

Before opening the pull request, run the same check that CI runs:

```sh
python3 contributions/tools/orchid_contrib.py validate contributions/data/my-values.json
python3 -m pytest -q contributions/tests          # if you changed the tools
```

## What happens next

1. CI validates the files (units and ranges, elements of the system, the physical phase rule of the release,
   phase names of the system's TDB, duplicates, page and quote, DOI, ORCID, licence consent) and checks the DCO
   sign-off.
2. A maintainer checks the page of the paper (or the dataset) and records the check.
3. The pull request is merged; accepted corrections and values appear in the **next release**. A corrected value
   keeps its old value in its history, with your name; a contributed value starts as `contributed_unverified` and
   becomes `verified` after an independent check. Contributions never overwrite released values silently.

## Licences

- **Data** you contribute (values, corrections, metadata) are released under
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with credit to you. Each line or value carries
  `licence_consent: "CC-BY-4.0"`. Quotes are single sentences or table rows, reproduced under fair use so the value
  can be checked; do not add PDFs, page images or longer text.
- **TDB files** keep their own open licence, which you state in `metadata.json`; you confirm that you may release
  the file under it.
- **Code** (`contributions/tools/`) is under the MIT licence of the ORCHID tools. Sign off every commit
  (`git commit -s`) to certify the [Developer Certificate of Origin](https://developercertificate.org/).

## Credit

Accepted contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md). If you opt in (a checkbox in the issue form
or the pull request), you are also listed as a contributor in the Zenodo record of the release. A corrected or
verified value names you in its own `contributors` field.

## Privacy

We ask only for a name to credit (a GitHub handle is fine) and, optionally, an ORCID iD and affiliation. Do not put
e-mail addresses or other personal data in issues or files. The **report** links carry only the record id, DOI,
page and value, never anything about you.

## Conduct and governance

Everyone follows the [Code of Conduct](CODE_OF_CONDUCT.md) (Contributor Covenant 2.1). Maintainers and how
decisions are made: [GOVERNANCE.md](GOVERNANCE.md). Questions: open an issue with the
[Contribute data](https://github.com/orchid-calphad/orchid-data/issues/new?template=contribute-data.yml) form.

Classroom use: a pilot in which students check ORCHID values against their papers as a course exercise is planned;
it will use the same issue forms and pull requests, and no student data are collected.
