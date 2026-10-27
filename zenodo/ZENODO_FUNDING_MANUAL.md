# Funding: what to enter by hand in the Zenodo form

## Both awards must be entered on every record

Enter two separate Funding entries on every draft, for National Science Foundation awards 2608825 and 2534344. Select
the indexed award when available; otherwise enter a custom award with its verified official title and award URL, and
confirm that both entries were saved. The earlier database lookup below applies only to 2608825 and does not establish
whether 2534344 is indexed; a dated lookup is not evidence of current indexing, so search both numbers on the day.

The acknowledgment used in every record (`FUNDING_NOTE` in `tools/orchid_cite.py`, in the notes and at the end of each
description) does not depend on the award titles:

> This work was supported by the U.S. National Science Foundation under awards OAC-2608825 and 2534344.

(`OAC` is the NSF division; the award number proper is 2608825.)

ARM-MIP fields, verified against the [NSF award API](https://api.nsf.gov/services/v1/awards/2534344.json) on 2026-10-26:

| field | value |
|---|---|
| Funder | National Science Foundation |
| Number | 2534344 |
| Title | Research Infrastructure: MIP: Autonomous Robotic Metallurgist: An NSF Materials Innovation Platform (ARM-MIP) |
| URL | https://www.nsf.gov/awardsearch/showAward?AWD_ID=2534344 |

NSF award 2608825 is **not in Zenodo's awards database** (checked 2026-10-24 against the awards API: 0 hits for the
number and for "PhaseForge"; a control NSF award returned one hit). A `grants` entry such as
`10.13039/100000001::2608825` in the deposition metadata is therefore rejected, and all `grants` entries have been
removed from the ten `zenodo/*.metadata.json` files and from the `.zenodo.json` files of `orchid-data`,
`orchid-project.org`, `orchid-pipeline` and `orchid-examples`. The funding sentence stays in the `notes` field of every
record. In the web form, enter the funding yourself, once per record, as a **custom award**.

## Award 2608825: text to enter (every one of the ten records, and any later GitHub-integration record)

In the upload form, section **Funding**, button **Add custom** (not "Add"), unless the award is now indexed:

| field | value |
|---|---|
| Funder | `National Science Foundation` (pick the entry whose ROR id is `021nxhr62`, DOI `10.13039/100000001`; the funder must be found by name because custom awards need a funder registered in ROR) |
| Number | `2608825` |
| Title | the official NSF award title, verified at the URL below on the day (**not yet independently confirmed**; `CSSI Elements: PhaseForge` is the only title in our files) |
| URL | `https://www.nsf.gov/awardsearch/showAward?AWD_ID=2608825` |

**TODO for the PI:** `CSSI Elements: PhaseForge` is the only title found in our files (CITATION.cff of
`orchid-pipeline`, `orchid-data/GOVERNANCE.md`, the website's funding section, the paper). The NSF API pages could not
be reached during the X4 review of 2026-10-27, so no independent confirmation of the full title is claimed. Open the URL
above and enter the official award title shown by NSF (NSF titles are usually longer, for example "Elements: ...").

## Award 2534344

Search the Funding selector for `2534344` first; if it is indexed, choose it. Otherwise **Add custom** with the ARM-MIP
fields in the table at the top of this file (funder as for 2608825).

## Before you enter a custom award

1. In the same section press **Add**, type `2608825`, and see whether the award has appeared in the database since
   2026-10-24 (the standard entry would show as National Science Foundation, 2608825). If it is there, choose it
   instead (its identifier is `021nxhr62::2608825`) and skip the custom entry. The runbook has a one-line check.
   Do the same for `2534344`.
2. Otherwise use **Add custom** with the tables above, one entry per award.

## After you save the draft

Each award appears as a chip under the funding section and, after publication, on the record page under "Funding":
confirm that **both** chips (2608825 and 2534344) were saved. Funding can be edited after publication (it is metadata,
not a file). Do the same in each of the ten drafts; there is no bulk edit.
