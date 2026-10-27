# Funding: what to enter by hand in the Zenodo form

## Both awards must be entered on every record

The acknowledgment covers NSF awards **2608825** (PhaseForge) and **2534344** (ARM-MIP).
For each award, first search the Funding selector by number. Choose the indexed award
when available; otherwise create a separate custom award under National Science Foundation.
The earlier database lookup below applies only to 2608825 and does not establish whether
2534344 is indexed. Save both funding entries on each of the ten drafts.

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

## Text to enter (every one of the ten records, and any later GitHub-integration record)

In the upload form, section **Funding**, button **Add custom** (not "Add"):

| field | value |
|---|---|
| Funder | `National Science Foundation` (pick the entry whose ROR id is `021nxhr62`, DOI `10.13039/100000001`; the funder must be found by name because custom awards need a funder registered in ROR) |
| Number | `2608825` |
| Title | `CSSI Elements: PhaseForge` |
| URL | `https://www.nsf.gov/awardsearch/showAward?AWD_ID=2608825` |

**TODO for the PI:** `CSSI Elements: PhaseForge` is the only title found in our files (CITATION.cff of
`orchid-pipeline`, `orchid-data/GOVERNANCE.md`, the website's funding section, the paper). Open the URL above, compare
with the official award title shown by NSF, and use that title if it differs (NSF titles are usually longer, for
example "Elements: ..."). The acknowledgement sentence used everywhere is: "This work was supported by the U.S.
National Science Foundation under awards OAC-2608825 (CSSI Elements: PhaseForge) and 2534344
(Autonomous Robotic Metallurgist: An NSF Materials Innovation Platform, ARM-MIP)." (`OAC` is the NSF division; the
award number proper is 2608825).

## Before you enter a custom award

1. In the same section press **Add**, type `2608825`, and see whether the award has appeared in the database since
   2026-10-24 (the standard entry would show as National Science Foundation, 2608825). If it is there, choose it
   instead (its identifier is `021nxhr62::2608825`) and skip the custom entry. The runbook has a one-line check.
2. Otherwise use **Add custom** with the table above.

## After you save the draft

The funding appears as a chip under the funding section and, after publication, on the record page under "Funding".
It can be edited after publication (it is metadata, not a file). Do the same in each of the ten drafts; there is no
bulk edit.
