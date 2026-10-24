## What this pull request contributes

- [ ] corrections (`contributions/corrections/`)
- [ ] values read from a paper (type B, `contributions/data/`)
- [ ] new measurements with a DOI (type C)
- [ ] calculated data (type D)
- [ ] an assessment / TDB file (type E, `contributions/tdb/`)
- [ ] paper suggestions (type A, `contributions/papers/queue.jsonl`)
- [ ] documentation or tools

Systems and a short description:

## Checklist

- [ ] `python3 contributions/tools/orchid_contrib.py validate <files>` passes
- [ ] every value states its source (DOI) and, for values read from a paper, the printed page and quote (at most 240 characters)
- [ ] no PDFs, page images or e-mail addresses in the files
- [ ] I agree that the contributed data are released under CC BY 4.0, and my commits are signed off (`git commit -s`, Developer Certificate of Origin)
- [ ] credit me in the Zenodo metadata of the release (opt-in; name and ORCID as in the files)
