# ORCHID ESPEI datasets from the literature

ESPEI-format datasets built from the ORCHID literature values (Version 1, machine-extracted) and from DFT (literature, Materials Project, OQMD). Every literature value is traced to its published ORCHID observation id (`literature/`, field `id`) and the DOI of its source, passes the same inclusion rules as the published literature values, and carries its uncertainty in physical units next to the ESPEI weight derived from it.

| folder | datasets | values | systems | content |
|---|---:|---:|---:|---|
| experimental | 1641 | 5435 | 246 | experimental thermochemical tables and phase-composition (ZPF) tables |
| model | 754 | 2304 | 126 | values the papers calculated with a CALPHAD model, TDB (SHA-256) named where known |
| invariants | 2143 | 7888 | 537 | ZPF datasets from experimental invariant-reaction tables |
| dft/literature | 473 | 1080 | 48 | literature DFT formation enthalpies, HM_FORM endmember datasets (`solver`) |
| dft/mp | 1290 | 1290 | 399 | Materials Project on-hull formation energies, HM_FORM endmember datasets |
| dft/oqmd | 1290 | 1290 | 399 | OQMD on-hull formation energies, HM_FORM endmember datasets |

## Use with ESPEI

Point ESPEI at one evidence class at a time; classes are never mixed in a folder, and for DFT use **one** of `dft/mp`, `dft/oqmd`, `dft/literature` per fit (MP uses corrected, OQMD fitted elemental references).

```yaml
# espei-in.yaml
system:
  phase_models: my-phases.json
  datasets: orchid-espei/experimental      # or invariants/, dft/mp/, ... (separately, by choice)
generate_parameters:
  excess_model: linear
  ref_state: SGTE91
```

```
espei --input espei-in.yaml
```

or in Python (ESPEI 0.9.1):

```python
from espei.datasets import load_datasets, recursive_glob, apply_tags
ds = load_datasets(recursive_glob('espei/experimental/AG-AL') + recursive_glob('espei/invariants/AG-AL'))
# your choices, e.g. halve the weight of single-reader values, drop model values:
apply_tags(ds, {'single_reader': {'weight': 0.5}, 'model': {'disabled': True}})
```

`apply_tags` replaces the dataset's `weight`; to scale the weight derived from the printed sigma, read `orchid_uncertainty` and set `weight` yourself. `index.csv` / `index.json` list every dataset (system, output, phases, values, temperature range, evidence class, DOIs, observation ids, reader agreement, sigma summary, weight).

Tags: evidence class (`experimental`, `model`, `dft_literature`, `dft_mp`, `dft_oqmd`), quality (`single_reader`, `single_reader_text_layer`, `no_printed_uncertainty`, `polymorph_ambiguous`, `above_hull`, `orchid_caveat`), plus the corpus tags (`thermochemical_table`, `invariant_table`, `via_assessment`, ...).

## Uncertainties

ESPEI 0.9.1 has no per-value uncertainty field: the sigma it uses is a reference sigma divided by the dataset's `weight` (500 J/mol for HM, 0.2 J/K/mol for SM and CPM, 500 J/mol on the chemical potential for activities; ESPEI: "estimated from NIST TRC uncertainties", i.e. for experiments). Every value carries its sigma in physical units in `orchid_uncertainty.values[]` (`sigma`, `sigma_basis`, printed text and coverage or calibration provenance, `weight_used`). **Weights are derived from these sigmas; you can recompute your own weights from them.**

Which sigma applies to which data:

| data | sigma | ESPEI weight |
|---|---|---|
| experimental, uncertainty printed | printed (±x taken as 1 sigma: coverage is not printed with the values; a printed range gives sigma = half-width, bounds kept) | ESPEI default / median sigma of the dataset (one weight per equilibrium dataset in ESPEI 0.9.1); per-value equivalents recorded |
| experimental, nothing printed | `sigma_printed` null; `sigma_assumed` = ESPEI's experimental default (500 J/mol, 0.2 J/K/mol), basis `espei_default_experimental (assumed, not printed)`; GM has no default (null) | 1 (tag `no_printed_uncertainty`) |
| DFT (literature, MP, OQMD) | calibrated against experiment (dft/CALIBRATION.md): robust sigma of the value's stratum, leave-system-out; bias recorded, not applied | 500 J/mol / sigma_DFT per value (a conversion, not a claim that DFT is accurate to 500 J/mol) |
| model-calculated (model/) | none (model-calculated; no measurement uncertainty) | 1 only because ESPEI needs a value: **choose your own weight** or exclude with the `model` tag |
| ZPF (experimental/ ZPF, invariants/) | none on the value; printed temperature uncertainty kept where printed; ESPEI weighs ZPF by a driving-force tolerance | 1 (not set) |

Per folder and output: UNCERTAINTY_SUMMARY.md.

## What each dataset carries

ESPEI-native content (`components`, `phases`, `conditions`, `output`, `values`, `reference_states` / `reference_state`, `solver` for DFT endmembers, `tags`, `weight`), plus `reference` (source paper, DOI), `bibtex` (key in `references.bib`), a `comment` with the ORCHID observation ids, the evidence class and "Version 1, machine-extracted", an `orchid` block (ids, reader agreement, caveats, papers, DOIs, source) and `orchid_uncertainty`. Model datasets keep `orchid_model_evidence` (TDB name, SHA-256, link basis). DFT datasets name the TDB file (SHA-256), phase and endmember they map to (see SCHEMA.md).

## Caveats

- **Machine-extracted (Version 1).** Literature values were read by language-model readers and accepted on reader agreement plus deterministic checks; a hand-checked precision sample is in progress. Check a value against its paper (DOI) before relying on it.
- **Single reader.** Values read by one visual reader carry `reader_agreement: single_reader` in `orchid.observations` and the tag `single_reader`. Reader agreement is taken from the record store (the published literature release predates the field).
- **Weights are your choice.** The weights written follow the rules above; tags and `orchid_uncertainty` let you set your own.
- **DFT.** 0 K energies used as 298.15 K enthalpies; one DFT source per fit; a value is written only where the compound maps to exactly one TDB phase (phase registry: DFT entry id or paper label) and exactly one endmember of that TDB model at the compound's composition (one dataset per system, TDB file and phase; `solver` site ratios and configurations as in the TDB). Excluded compounds are listed in validation.json with reasons. ESPEI 0.9.1 evaluates HM_FORM against each element's SER phase named on the TDB's ELEMENT line, which must exist as a phase in the TDB; in some binary TDB files it does not (e.g. GRAPHITE, ORTHORHOMBIC_GA, 1/2_MOLE_O2(G)), and ESPEI then stops with a KeyError: add the element phase to your working TDB or fit those datasets with another.
- **Energy basis.** ESPEI reads energies per mole of atoms. Literature values whose per-atom basis was not printed carry the caveat `energy_basis_unstated`.
- **ZPF encoding.** Phase labels are mapped to the model phases of the assessment the source folder is named after (tag `via_assessment`); a printed compound composition that is its formula rounded is written at the exact formula value; a `__HYPERPLANE__` vertex is added only where every known composition comes from stoichiometry. Range temperatures are written at the midpoint (`orchid_value_bases`).
- Values removed by the inclusion gate and datasets ESPEI rejects are listed in VALIDATION.md.

## Citation

R. Arróyave, J. Saal, D. Shin, ORCHID ESPEI datasets from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-espei

Part of: R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (each dataset's `reference` / `bibtex`, references.bib; index.csv lists the DOIs); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Licence: CC BY 4.0 (derived data; MP and OQMD data CC BY 4.0). The source papers are not redistributed; only their citations and DOIs.
