# TDB generation and potential provenance

`tdb_provenance.json` registers the four Cu–Zr example models by TDB SHA-256. Its JSON Schema is
`tdb_provenance.schema.json`. Artifact paths are relative to the `cuzr-phaseforgeplus/` directory of
`orchid-examples`; this registry contains metadata, not additional thermodynamic databases.
Join a phase model's `models[].sha256`, a diagram's TDB digest, or a fitting run's TDB digest to `records[].sha256`.
An unmatched digest has unknown provenance: do not classify it from the filename or copy a parent's tag.

`generation_method` is `phaseforge`, `phaseforge_plus`, `conventional_assessment`, `other`, or `unknown`.
The corresponding `tags` permit filtering; PhaseForge+ is encoded as `phaseforge_plus`.
`workflow_history` retains both stages for a PhaseForge model subsequently fitted with PhaseForge+.
`variant` distinguishes the MLIP-only description, the zero-initialized B2 temperature-term variant, and the fitted model.
These are model-provenance tags, distinct from ESPEI's evidence-selection or weight-changing tags.

`potential` records the family and model name, a version when documented, and the exact checkpoint file digests.
The Cu–Zr models use GRACE-2L-OMAT. No separate semantic version was recorded; `version` is null and the six
archived checkpoint hashes identify the model. A null potential on the conventional assessment means no MLIP
was used; for unknown provenance it means not established. Never invent a model version or checkpoint hash.
`evidence` identifies the records supporting the attribution; `parents` links unchanged source TDB bytes by hash.

The final Cu–Zr model is `phaseforge_plus`, with both generation stages in its history. Its fit records the two
ORCHID data commits, the archived weighting policy, the source run, and post-hoc selection. It remains a
review-only demonstration. The 9/13 gate result is in-sample and is not validation on independent evidence.

The workflow definition and runner are `orchid-examples/cuzr-phaseforgeplus/workflow/cuzr.json` and
`scripts/workflow.py`. They preserve the historical data pins and weighting choices. New fits using the revised
individual-uncertainty bundle require a new run manifest, and must retain its weights or document their overrides.
The historical model hashes and results are not replaced by an unexecuted plan. The runner records hashes of inputs,
software versions, commands, seeds for new MD runs, outputs, and stage receipts. The historical MD seed was not
recorded, so exact trajectory reproduction cannot be claimed.
