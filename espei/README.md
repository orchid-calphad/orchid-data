# ORCHID ESPEI datasets from the literature

ESPEI-format datasets built from the ORCHID literature values (Version 1, machine-extracted) and from DFT (literature, Materials Project, OQMD). Every literature value is traced to its published ORCHID observation id (`literature/`, field `id`) and the DOI of its source, passes the same inclusion rules as the published literature values, and carries its uncertainty in physical units next to the ESPEI weight derived from it.

| folder | datasets | values | systems | content |
|---|---:|---:|---:|---|
| experimental | 1012 | 3012 | 193 | experimental thermochemical tables and phase-composition (ZPF) tables |
| model | 542 | 845 | 84 | values the papers calculated with a CALPHAD model, TDB (SHA-256) named where known |
| invariants | 1673 | 5576 | 486 | ZPF datasets from experimental invariant-reaction tables |
| dft/literature | 441 | 1050 | 44 | literature DFT formation enthalpies, HM_FORM endmember datasets (`solver`) |
| dft/mp | 1218 | 1218 | 373 | Materials Project on-hull formation energies, HM_FORM endmember datasets |
| dft/oqmd | 1218 | 1218 | 373 | OQMD on-hull formation energies, HM_FORM endmember datasets |

Optional phase constraints (separate folders; never mixed with measured data; see "Phase constraints"):

| folder | datasets | ZPF points | systems | content |
|---|---:|---:|---:|---|
| assessed | 654 | 7702 | 482 | assessed (handbook) phase-field points, Dataset assessed-phase-assemblages, in the phase names of each TDB that has ZPF datasets here (tag `assessed_phase_diagram`) |
| derived/invariant-brackets | 1144 | 5659 | 401 | DERIVED: phase sets just above and below each printed invariant (tag `derived_bracket`) |
| derived/liquid-stability | 434 | 3906 | 312 | DERIVED: single-phase liquid above the highest liquidus where the sources show complete liquid miscibility (tag `derived_liquid_stability`) |

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

To restrict a fit to evidence certified against a CALPHAD prediction (`calphad_certified`: every value of the dataset is `espei_certified` in the literature release, i.e. espei_ready and its pycalphad calculation from the linked TDB agrees within 25 K / 0.05; per-value detail in `orchid_certification`):

```yaml
system:
  phase_models: my-phases.json
  datasets: orchid-espei/experimental
  tags:
    orchid: {disabled: true}             # every ORCHID dataset (literature and DFT) off ...
    calphad_certified: {disabled: false}  # ... except the certified ones (tags apply in this order)
```

(ESPEI applies `tags` before it removes disabled datasets, so the second tag re-enables.)

## Phase assignment

Physical phase rule (tools/phase_rule.py): a literature value is assigned to a phase only when the paper names that phase (printed phase label of the value; when no label is printed, a table caption that names the liquid) and the phase registry maps the label to a model phase; no default phase is assigned. A liquid assignment must be physically possible: not below the lowest liquid temperature of any calculated SGTE diagram of the system minus max(100 K, 10 %) (twice that for printed invariant and phase-composition records; no calculated diagram: not below 0.40 x the lowest element melting point). Formation enthalpies and entropies of a stoichiometric compound go to that compound's TDB endmember (ESPEI non-equilibrium dataset, `solver`); other properties of a compound are not used in ESPEI. A solution-phase assignment outside the phase's field in the calculated diagram of the target TDB is flagged (`outside_calculated_field`), not excluded. Temperatures: T <= 1 K is not a measured state; a printed phase equilibrium (invariant, phase composition, transition) below 0.25 x the lowest element melting point is a misreading. A value flagged `unsigned_in_print` / `magnitude_suspect` / `system_mismatch` / `source_disputed` is not ESPEI-ready.

Every value's phase comes from its published literature record (printed label -> phase registry -> the target TDB's phase name), never from a default. Values with different phases in one source table are written as separate datasets (`<TDB>.<file>-<PHASES>.json`). Formation enthalpies / entropies of a phase that is stoichiometric in the target TDB are written as ESPEI non-equilibrium datasets (`solver`, the compound's endmember, output `HM_FORM` / `SM_FORM`, tag `compound_formation_endmember`) when the printed composition matches the formula and the printed reference state is the TDB's SER; other properties of compounds are not written. `orchid_phase_assignment` gives the phases, the basis (printed labels or caption) and, flag only, values outside the phase's field in the calculated diagram of the target TDB (`outside_calculated_field`). Also excluded (VALIDATION.md, `drop_reasons`): activities outside (0, 1], negative absolute entropies, increments printed as absolute values, per-gram heat capacities, formation / mixing values outside physical ranges, values flagged unsigned_in_print / magnitude_suspect / system_mismatch / source_disputed, reference phases that the TDB does not have, binary three-phase ZPF regions away from every calculated invariant, ZPF regions with a gas and no printed pressure, and ZPF regions that carry no composition and no hyperplane (zero driving force in ESPEI 0.9.1).

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
- **Single reader.** Values read by one visual reader carry `reader_agreement: single_reader` in `orchid.observations` and the tag `single_reader`. Reader agreement is taken from the literature release.
- **Weights are your choice.** The weights written follow the rules above; tags and `orchid_uncertainty` let you set your own.
- **DFT.** 0 K energies used as 298.15 K enthalpies; one DFT source per fit; a value is written only where the compound maps to exactly one TDB phase (phase registry: DFT entry id or paper label) and exactly one endmember of that TDB model at the compound's composition (one dataset per system, TDB file and phase; `solver` site ratios and configurations as in the TDB). Excluded compounds are listed in validation.json with reasons. ESPEI 0.9.1 evaluates HM_FORM against each element's SER phase named on the TDB's ELEMENT line, which must exist as a phase in the TDB; in some binary TDB files it does not (e.g. GRAPHITE, ORTHORHOMBIC_GA, 1/2_MOLE_O2(G)), and ESPEI then stops with a KeyError. Such datasets are not written (likelihood evaluation gate, VALIDATION.md); to use those values, add the element phase to your working TDB and rebuild from the literature release.
- **Energy basis.** ESPEI reads energies per mole of atoms. Literature values whose per-atom basis was not printed carry the caveat `energy_basis_unstated`.
- **ZPF encoding.** Phase labels are mapped to the model phases of the assessment the source folder is named after (tag `via_assessment`); a printed compound composition that is its formula rounded is written at the exact formula value; a `__HYPERPLANE__` vertex is added only where every known composition comes from stoichiometry. Range temperatures are written at the midpoint (`orchid_value_bases`).
- **Line compounds (E2).** A ZPF vertex of a phase that is stoichiometric in the target TDB is written with composition null: ESPEI 0.9.1 / pycalphad 0.11.2 return NaN for a line compound at a fixed composition (one NaN makes the ZPF likelihood -inf), and with null ESPEI evaluates the compound at its formula composition. Where that leaves a region with no known composition, a `__HYPERPLANE__` is added at the mean of the compound compositions. Known limitation of ESPEI 0.9.1: a single-phase vertex at a line-compound composition gives an undefined target hyperplane (zero driving force) once the compound is stable there, so a congruent melting point constrains the model in one direction only; the invariant brackets below constrain both.
- **Duplicates (E3, E4).** Identical ZPF regions in several datasets (several assessment folders, or several papers quoting the same invariant) are written once, with every source in `orchid.observations[i].also_reported_as`; a printed row read twice (same row id, conditions and value) counts once (`also_read_as`). Records concerned are listed in UPSTREAM_CORRECTIONS.md.
- **Activity reference states (E5).** Every activity table was checked against the paper: the reference state written is the one the paper prints (or, where nothing is printed, the pure liquid of an element that is liquid at the temperature, recorded as `not_printed_implied`); `orchid_reference_state` gives the basis and the printed text. Literature records whose reference state differs are listed in UPSTREAM_CORRECTIONS.md; the published literature values are not changed here.
- Values removed by the inclusion gate and datasets ESPEI rejects are listed in VALIDATION.md.

## Optional minimum-sigma policy (E6)

Printed uncertainties are kept as printed. Some are much smaller than the scatter between independent measurements of the same quantity (e.g. formation enthalpies printed with ±80 J/mol-atom while other measurements of the same compound differ by 1-2 kJ/mol-atom); with the weight derived from such a sigma a few values can dominate a fit. Every experimental thermochemical dataset carries `orchid_weight_floor` (`suggested_weight` = min(weight, 1), i.e. sigma_eff = max(sigma, ESPEI's experimental default)). The floor changes the weight of 47 of 869 datasets. It is a suggestion, not applied: `d['weight'] = d['orchid_weight_floor']['suggested_weight']` before `load_datasets` applies it.

## Phase constraints (optional)

ZPF data alone can let a refinement misfire: ESPEI 0.9.1 penalises a phase that should be present but is not, but gives no driving force for a liquid point at a line-compound composition once the compound is stable, so a compound can melt far above its printed melting point without cost. Three optional, tagged dataset groups add phase evidence. They share the phase names of the assessment folder (TDB) they are written for, so they load together with `experimental/` and `invariants/` of that TDB. Use them by choice, never as measured data.

- `derived/invariant-brackets/<SYS>/<TDB>.<file>.json` (tags `derived`, `derived_bracket`): For each binary invariant reaction (eutectic, peritectic, monotectic, eutectoid, peritectoid, metatectic, syntectic, congruent melting or transformation, polymorphic) with printed temperature T and printed temperature uncertainty u (else u = 5 K, documented default), two ZPF points are written at the invariant composition x0: at T + max(2u, 10 K) the phase set stable above the reaction and at T - max(2u, 10 K) the set stable below. The reaction is read as printed with the cooling convention (left side = high temperature; a reaction written on heating, i.e. a single liquid formed from solids, is turned round). x0 is the composition of the phase alone on its side (eutectic: the liquid; peritectic: the product; congruent: the common composition); the other side's phases are written with their printed compositions (null where not printed or for line compounds, E2). The target hyperplane is estimated at x0 - d and x0 + d (d = min(0.01, half the distance to the nearest printed composition or to a pure element)) so that a line compound at x0 cannot make the hyperplane undefined (ESPEI 0.9.1 returns zero driving force when the equilibrium at the hyperplane composition is a single phase without internal degrees of freedom). A point is not written when another invariant of the system that shares a non-liquid phase (or a liquid within 0.05 in composition of x0) lies between T and the bracket temperature. These points encode the semantics of the printed reaction (which phases are stable on which side); they are DERIVED, not measured. Each point records its source observation, T, u and offset (`orchid.points`).
- `derived/liquid-stability/<SYS>/<TDB>.liquid-stability.json` (tags `derived`, `derived_liquid_stability`): Single-phase LIQUID points at x = 0.1 ... 0.9 at T = T_liq_max + 50 K, where T_liq_max is the highest of the melting points of the two elements (SGTE unary data), every accepted printed temperature of an experimental literature value of the system that involves the liquid (invariants, liquidus and ZPF points) and every assessed (handbook) two-phase field point that contains the liquid. Written only where the evidence shows complete liquid miscibility: the system has an assessed (handbook) diagram with a single-phase liquid field and no second liquid (no L#2 field), no literature value of the system has two liquids (monotectic, syntectic or two liquid labels), both elements are condensed liquids at 1 atm (metals and metalloids) and T stays below both normal boiling points. Purpose: forbid spurious liquid miscibility gaps (and solids stable above the liquidus) in a fit. DERIVED, not measured. `orchid.basis` gives the temperatures used.
- `assessed/<SYS>/<TDB>.<DIAGRAM>.json` (tag `assessed_phase_diagram`): the ZPF datasets of assessed-phase-assemblages (one point inside each named field of an expert-drawn handbook diagram) with the phase names of that TDB (phase registry); points with a phase that the TDB does not model, or models twice, are left out; `orchid.confidence` per point. Evidence class assessed_phase_diagram: neither experimental nor CALPHAD.

Counts (brackets written and skipped by reason, systems with liquid-stability points) are in validation.json (`phase_constraints`). Suggested use: weight each group so that it contributes comparably to the measured data (e.g. per-type weights proportional to 1/N), and check the fitted model's invariant temperatures against the printed ones after the fit.

## Citation

R. Arróyave, J. Saal, D. Shin, ORCHID ESPEI datasets from the literature (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-espei

Part of: R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite the original source of every value you use (each dataset's `reference` / `bibtex`, references.bib; index.csv lists the DOIs); A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0).

Licence: CC BY 4.0 (derived data; MP and OQMD data CC BY 4.0). The source papers are not redistributed; only their citations and DOIs.
