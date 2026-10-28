# Changelog

## v2026.10 — Version 1, first public release (28 October 2026)

ORCHID's first public release. It gathers openly available CALPHAD thermodynamic databases and the evidence behind them, with every value stored as an observation of an equilibrium state: the phases, temperature, pressure, compositions and reference state, together with the source, the page, the quoted sentence or table row, and an evidence class (experimental, model, DFT, assessed phase diagram, unspecified) that is never mixed.

**Version 1 is machine-extracted.** Values were read from papers by language-model readers that had to quote their source, checked automatically, and then audited against the printed pages by independent AI reviewers; people have reviewed samples only. The flags `accepted`, `espei_ready` and `espei_certified` record the outcome of screening rules. They do not certify that a value is correct.

### What is released

| Dataset | DOI | Content |
|---|---|---|
| ORCHID-Values | 10.5281/zenodo.23735569 | 73,542 literature values from 1,321 papers; 66,551 accepted; 11,161 ESPEI-ready; 1,892 certified |
| ORCHID ESPEI datasets | 10.5281/zenodo.23735788 | 8,589 datasets: 6,452 from literature values and DFT (12,512 values) and 2,137 optional phase constraints |
| ORCHID-Diagrams | 10.5281/zenodo.23735859 | binary phase diagrams calculated from open TDB files, each tied to its file by SHA-256 |
| ORCHID-Hulls | 10.5281/zenodo.23735891 | binary DFT convex hulls (Materials Project, OQMD) and assessed CALPHAD hulls |
| ORCHID-Parity | 10.5281/zenodo.23735943 | literature formation enthalpies against DFT, structure-matched, with error statistics |
| ORCHID-Registry | 10.5281/zenodo.23735970 | 10,430 binary phases with their names, TDB models and structures |
| ORCHID-Assemblages | 10.5281/zenodo.23735996 | 23,129 points inside the named fields of 2,178 assessed (handbook) binary diagrams |
| ORCHID-Bibliography | 10.5281/zenodo.23736021 | 9,570 papers with their roles and typed citation relations |
| ORCHID examples | 10.5281/zenodo.23736043 | runnable workflows (Cu–Zr with PhaseForge+ and ESPEI, one-shot MLIP phase diagrams, MLIP formation enthalpies, quickstart) |
| ORCHID data (umbrella) | 10.5281/zenodo.23736065 | links all of the above |

All datasets are released under CC BY 4.0 and the code under MIT. Upstream data keep their own terms, listed in `LICENSES.md`.

### How the release was checked

- **Automatic gates** on every value: the quote must be found on the page, fields must sit where the table prints them, signs are checked against the printed page, the Gibbs phase rule and the law of adjacent phase regions are enforced, and formation enthalpies are compared with DFT and with Kim et al. (2017).
- **Adversarial audits** of random samples against the printed pages, repeated after each round of fixes.
- **An independent second review** of the records that feed CALPHAD fits.
- **A preliminary human review** of a frozen sample of 300 records, of which 210 were assessed: the numerical value was right in 95.6 % of the assessable responses, and all reviewed fields together in 81.5 %. It was followed by an AI-assisted adjudication of the 81 records the reviewers questioned.
- **A measured precision of the fit-facing data:** in a blind random sample of 200 ESPEI-ready records, 189 were safe to fit (94.5 %, 95 % interval 90.4–96.9 %). Value, composition, phases, property and evidence class were right in all 200. The 11 problems found (9 molar bases, 2 temperatures) are fixed or flagged in this release.

### Changes made before release (27–28 October)

- **A state needs real phases.** Invariant, transition and phase-composition values are accepted only when the record names at least one real phase; placeholder labels such as "unknown", "other" or "?" do not count. Where the page prints the phase for the row or for its table group, it was recovered (1,267 records), and those records are accepted again; they stay out of ESPEI until revalidated.
- **Page-checked corrections, all guarded:**
  - 301 from an independent second review;
  - 2,971 records from 287 table pages, where continuation rows had lost the phase or structure printed for their group;
  - 688 corrections and 503 flags for defects seen on those pages (wrong phase labels, entropies of melting stored as entropies, Cp coefficients stored as Cp, annealing temperatures stored as measurement temperatures, nm/Å mix-ups, duplicate readings);
  - 287 more from a final round (records moved to the chemical system of their state, page mismatches, duplicate readings, temperatures).
  - 15 more for property series that cross a phase transition (see Known issues).

  Each correction keeps the value before, the value after and the page evidence. Records named by a correction are filed under the chemical system of their own state.
- **Duplicates:** readings of the same printed row are linked with `duplicate_of`, which is also a Parquet column; exclude them before fitting. Where a table prints a value both per formula unit and per atom, the per-atom record is kept.
- **Exclusions from fitting:** 692 records named by the independent review (for example Ga–Pb compositions inside the miscibility gap) are kept, flagged and excluded from ESPEI and from the DFT calibration. Records whose molar basis or attribution could not be confirmed on the page are also out of ESPEI.
- **Uncertainty calibration** was recomputed without the excluded records. The ESPEI weights of about 1,000 datasets moved, by a median of about 2 %.

### Known issues

- **Values printed only in figures are not included.** A pilot for reading points from figures is under way.
- **Placeholder phases:** 1,687 records still lack a real phase. A blind check found a phase printed on the page for only about 5 % of them (95 % interval 1.7–13.7 %), so most cannot be recovered from the page.
- **Table rows that continue a group:** the accepted records were checked table by table. Candidates among the non-accepted records are not yet checked.
- **Two Ni–Te records** (Table 5 of one paper) are filed under the wrong system. The correction was held back because the page does not support the proposed move.
- **Properties across a phase transition:** heat-capacity, heat-content and lattice-parameter series that span a recorded transition were audited on the page; 15 records were assigned to the phase on their side of the transition and 110 records whose side could not be resolved are flagged and excluded from fitting.
- **Higher-order systems:** the phase registry covers binary phases only, so ternary phase names are not yet mapped to one identity.
- **A few individual records:**
  - some Ga–Sn records lack the measurement method, which is printed only on the previous page;
  - two Ga–Sn values are misprinted in the source;
  - three Fe–Y values printed in the paper have no record;
  - Ga–Pb mixture compositions inside the gap are excluded but not relabelled.

Report problems through `CONTRIBUTING.md` or the issue tracker. Each report is checked on the page before a correction is made.

### Coming next (2026.10.1)

The remaining fixes listed above, and the first results of the figure-reading pilot. Further ahead are a state registry and evidence graph linking every observation to the state it describes, and assembled ternary databases tested against ORCHID's ternary data.

## Pre-release development — ESPEI datasets, bibliography, literature re-export (2026-10-23)

**Audit round 2 fixes A1-A4 (2026-10-24, PI "fix all").** Ledger: `~/projects/ORCHID_AUDIT_2026-10-24/FIXES_R2.md`
(finding, fix, evidence, test). Page checks 1,251 -> 1,534 in `tools/literature_visual_checks.json` (rendered pages
viewed by AI agents; hashes only). (A1, compositions and systems) fractions printed under an at.% header and divided
by 100 twice, corrected per page-checked table (20 tables plus 26 stray cells; ZPF values were 100x too small);
composition axes that contradict the printed header flipped where the page confirms it; compositions assigned to the
wrong phase re-assigned by stoichiometry within the row (page-checked), remaining conflicts flagged
`label_conflicts_composition` (184, flag precision 75 % on 20 page checks); every record is filed under the system
of its own state (7,863 records moved to their binary or unary subsystem; the paper's system in `source_system`;
folds recomputed; 1,400 -> 1,475 systems); element-symbol errors (Ta-N, cement notation Ca-Fe-O, S for Si, stale
zero entries); accepted compositions outside [0, 1] not accepted. (A3, units and conditions) per-formula / per-atom
basis and sign decided once per printed column on the page (Mg2Si, CuO, TaB2, HfB, Co17Y2 / Co5Y, ...); the
DFT-driven conversion rule ("accept a conversion only if it lands near DFT") withdrawn; absolute entropies labelled
SM_FORM relabelled SM (116); H(T)-H(298) at the row temperature (747); A + B.T coefficients stored as expression terms
without a single temperature (623); 298-subscript, direct-synthesis and 0 K experimental temperatures corrected;
printed sigma rescaled with its converted value (165); formation from compounds and energies referred to another
phase (Ti-Ni martensites vs B2) are not _FORM; reading resolution counts printed decimals. Method classes: Knudsen
cell -> KEMS (before EMF), evaluated compilations never paired; calibration pairs keyed on phase and reference
state, per-formula / per-atom duplicates of one source screened, sources identified by (first author, year).
Floors recalibrated after the cleaning; classes below the >= 20 pairs / >= 10 states rule with >= 5 independent pairs
from >= 3 states take max(documented prior, cleaned robust sigma) (`cleaned_below_threshold`): formation enthalpy
EMF 8.1 -> 4.6, KEMS 3.0 -> 5.6, method not printed 4.1 -> 3.5 kJ/mol-atom, calorimetry 3.5, unspecified 3.8;
T_invariant 10 -> 11 K (table in `literature/UNCERTAINTY_CALIBRATION.md`). (A4, DFT) DFT entries matched within the
printed structure (CuZr B2, NiTi B2, Fe2Ti C14, Mg2Sr C14; `dft_structure_match`, unmatched outside the default);
`ehull` from ORCHID's own hulls for MP and OQMD (OQMD mismatches 364 -> 0; provider value in `ehull_upstream`);
`NiSi_2` parsed as NiSi2; off-stoichiometric measurements carry |dx| x hull-slope sigma and leave the default beyond
0.02; liquid / amorphous states never paired; non-integer formulas unified; parity folds equal the literature
record's; hull catalogs `correction_model` MP2020 / OQMD fit-partial, `source_release` (was `mp_release`), exact
unary ties resolved to known structures (`degenerate_endpoints` separate); calibration CIs also by system-cluster
bootstrap (`ci95_cluster_system`; MP sigma 8.9 [7.1, 11.1], OQMD 7.5 [6.4, 9.3], literature DFT 7.1 [5.3, 9.8]).
(A2, phases) literature model phases are no longer assigned from a bare Greek letter (eps / beta-compound -> BCC_A2,
C-U phi -> GRAPHITE_A9; 3,706 mappings withdrawn, kept in `model_phase_rejected`; printed-structure fields carry
`structure_basis`); `phase_mapper.py` under version control in orchid-project.org/tools (git blob in
`assessed-phase-assemblages/summary.json`) with the polymorph, Greek-table, element-of-solution, '?' and ION-liquid
fixes; registry: one-letter first sublattice kept (301 models), interstitial FCC_A1 carbides / nitrides as B1 (ZrH2
and dihydrides C1), ordered phases over disordered ranges caveated, DIS_PART names never preferred, 66 orphan ids
merged as aliases, liquid classes, NiTi B19', Al4C3 hR7. Dataset 6: unbounded schematic fields below 0 K excluded,
BaH2 and (gamma Fe,Pt) names from the handbook pages, order/disorder partners agree in the SGTE cross-check (83.0 ->
83.2 % of comparable comparisons). Counts: records 73,538 -> 73,550; accepted 72,359 -> 72,291; espei_ready 11,928
-> 11,858; DFT parity points 7,696 -> 7,546 (default MP 1,199 -> 1,181, MAE 10.8 -> 10.4; OQMD 1,251 -> 1,222,
9.4 -> 9.1 kJ/mol-atom); ESPEI datasets 6,044 -> 6,244 (experimental 984 -> 947, model 527 -> 486, invariants
1,656 -> 1,535, DFT literature 441 -> 774, MP / OQMD 1,218 -> 1,251); ESPEI 0.9.1 likelihood of all 8,353 evaluated
datasets finite. Permanent invariant tests: `tools/tests/test_r2_{compositions,thermo,dft,phases}.py`.

**Audit fixes A5 (figures) and A6 (paper numbers and claims) (2026-10-24, PI-approved).** (1) Calculated invariants:
`parquet/phase_diagram_invariants.parquet` has one row per distinct invariant (tools/calc_invariants.py: same phases
with the mapper's `#n` suffix ignored, T within 0.1 K, sorted phase compositions within 0.01; 24,828 mapper hits ->
15,322 invariants, new column `n_mapper_hits`; the JSON files keep all hits). (2) Cited-source years re-derived from
the printed reference (a parenthesised year first, never a page number; `year_read` / `year_basis` kept where the
year changed; 359 cited sources). (3) Lattice lengths a, b, c in angstrom where a unit was printed (nm x 10, pm / 100;
`value_stored` / `unit_stored` kept; units not printed are not converted; flag `lattice_length_outside_typical_range`).
(4) The 5 values whose page prints a pressure other than 1 atm no longer carry the assumed 101,325 Pa
(`pressure_basis = printed_not_1_atm_see_gate_failures`, `pressure_Pa_stored`). (5) Signs read on the page by gate G3
set `flag_sign_pdf_page_verified` (12). (6) The two running-text values whose page had been nulled were read again on
the rendered page (page 4 each; ledger entries `page_fix:ORC-O4DJJCAHLH`, `page_fix:ORC-A7W44LTTFR`). (7)
quality_fixes.json: the gate-level `espei_ready_after` is labelled (before the ESPEI phase rule; the released count is
`espei.espei_ready`) and the page-check ledger entries (`visual_check_entries`) are counted apart from the keys the
gates look up; the ledger states that the pages were inspected by AI agents, not by a person. (8) Hull catalogs and
documents state the energy corrections applied upstream (`correction_model: upstream_only`,
`upstream_energy_corrections`: MP2020 for the Materials Project GGA_GGA+U snapshot, the OQMD standard fit for OQMD);
energies unchanged. (9) Licence wording: quotes are short excerpts kept for verification under the publishers'
copyright (no "fair use" / "single sentence" claims). Tests: tools/tests/test_release_integrity.py.

**Co-author review fixes (2026-10-24, J. Saal).** (1) Assessed phase assemblages: rock-salt (B1) carbides and nitrides,
sphalerite SiC and FeSi-type silicides were named DIAMOND_A4 because the Pearson symbol cF8 alone selected it (84 phase
occurrences); they now map to the phase each SGTE file defines (FCC_A1 (M)(C,VA) for HfC, NbC, TaC, TiC, VC, ZrC,
beta-WC, the nitrides; own B1 / B3 / B20 phases otherwise), and the ESPEI ZPF files follow. SGTE cross-check: 19,160
of 23,087 comparable comparisons agree (83.0 %), 9,184 of 10,362 comparable points agree with at least one
assessment; metric definitions in the README and `summary.json`, non-comparable comparisons listed with reasons in
`sgte_not_comparable.csv`. (2) New per-point `boundary_basis` (printed_solid / dashed_estimated / mixed) for the lines
bounding each field; points bounded by dashed (estimated) lines get a larger reading component (2x / 1.5x the handbook
prior). (3) Literature: 30 records whose chemical system took an element from a pressure unit (Pa), a cover gas (Ar),
a garbled phase prefix (H-CuTe), a prototype / phase designation (CaF2, C, F) or a polymorph letter (B-, C-type
sesquioxides) were reassigned after viewing the pages (ledger `tools/literature_visual_checks.json`); a new gate
rejects units and gases as elements. 79 elements, 930 binary systems. (4) DFT calibration: energies within 1 meV/atom
of the hull (the numerical precision of the DFT energies) count as on the hull. (5) Machine-learning folds
`fold_lso` / `fold_lpo` (5-fold, sha256) on literature values, DFT parity rows and assessed points. (6) LICENSE,
LICENSES.md and NOTICE.md rewritten for this repository (CC BY 4.0 ORCHID data; SGTE, Materials Project, OQMD CC BY 4.0;
Kim et al. 2017 MIT; Crossref CC0; quotations remain the publishers' copyright; handbook-derived points are ORCHID's
own measurements, no handbook drawing or text).

**Method-based uncertainty floors and per-value uncertainty budgets (2026-10-24, PI decision).** Printed
uncertainties often reflect statistical precision only (e.g. Knudsen-effusion formation enthalpies printed with
+-0.08 kJ/mol-atom that differ from calorimetry by 6-8 kJ/mol-atom). Every literature record now carries
`uncertainty_budget` (tools/uncertainty_budget.py) with the components kept separate per measured quantity (value;
printed phase compositions; equilibration temperature): `sigma_printed` (as printed), `sigma_reading` (half of the
last printed digit), `sigma_method` (method-class floor), `sigma_composition` (historical-formula offset),
`sigma_scatter` (page-checked mutually inconsistent group), `sigma_conversion` (reference-state conversion) and
`sigma_effective` = max(sqrt(max(printed, reading, method)^2 + composition^2 + conversion^2), scatter). Method
floors are calibrated from ORCHID's own independent measurements of the same state (one value per primary source,
re-listings once, per-formula / per-atom basis-error pairs left out; 1.4826 x state-weighted median|d| / sqrt 2,
bootstrap 95 % CI over states; >= 20 pairs and >= 10 states, else a documented prior; never below ESPEI's default):
formation enthalpies 3.5 kJ/mol-atom for solution / reaction calorimetry (74 pairs, CI 1.9-5.9), 8.1 for EMF (32,
3.9-14.4), 3.8 for 'experimental' unspecified (35, 1.6-5.0), 4.1 for method not printed (312, 2.6-4.4); invariant
temperatures 10 K (4,981 pairs, 8.4-10.5); phase compositions 0.011 (3,139 pairs); lattice parameters 0.23 %
(0.11 % XRD); model-calculated values vs experiment 3.3 kJ/mol-atom, 4 K, 0.005; DFT values take the calibrated
sigma_DFT. All floors: `literature/UNCERTAINTY_CALIBRATION.md` (copied to
`espei/experimental/CALIBRATION_EXPERIMENT.json|md`). Printed values and printed uncertainties are unchanged.
102,170 quantities of 73,538 records have a budget (100,926 with sigma_effective; the rest carry the reason, e.g.
a mass-basis unit); of 6,087 with a printed sigma, 3,512 have sigma_effective above it. ESPEI bundle: weights use
sigma_effective by default (the opt-in `orchid_weight_floor.suggested_weight` is kept, marked superseded); 1,404
thermochemical datasets, weight lower than before in 1,297 (747 experimental, 550 model), unchanged in 107;
experimental HM_FORM sigma larger than before for 373 of 437 values; every value carries its budget in
`orchid_uncertainty.values[].budget`; ZPF regions carry temperature and composition budgets; invariant-temperature
brackets use u = sigma_effective (1,141 -> 1,114 datasets, 5,612 -> 5,090 points); one model dataset
(`model/C-TI/TiC-03Fri.sm-model-01.json`) now evaluates finite and is written (527 model datasets). Assessed
phase assemblages: budget with digitisation (`sigma_reading`), handbook-class prior 10 K / 0.02 (`sigma_method`)
and the boundary margin reported, not combined. Cu-Zr: the ESPEI-ready measured formation enthalpies now have
sigma_effective 4.1-8.7 kJ/mol-atom (before 0.08-8.7), above the 3 kJ/mol-atom floor of the Cu-Zr PhaseForge+ fit.
Budgets also in Parquet (`literature_values` sigma_* columns), compound pages (budget table), the MCP server and
the dataset card. ESPEI 0.9.1 likelihood of all 8,239 datasets finite.

**Cu-Zr compound formation enthalpies: over-exclusion fixed (2026-10-24, PI).** After the targeted cleanup no
measured formation enthalpy of Cu5Zr, Cu51Zr14, Cu8Zr3 or Cu10Zr7 was ESPEI-ready. Rechecked on the rendered pages of
Turchanin 2008 (Table 3 p. 437, text p. 435, Fig. 4 p. 436, references pp. 444-445) and Zeng 1994 (Table 1):
(1) Cu4Zr / Cu9Zr2, Cu3Zr and Cu3Zr2 are the historical formulas of Cu5Zr, Cu51Zr14 and Cu10Zr7, which the table
note itself attributes to the modern phases: `stoichiometry_mismatch` is now flag-only and the value is used for the
modern phase with sigma = sqrt(sigma_printed^2 + (|dx| x local hull slope)^2) (`uncertainty.basis =
printed_with_composition_offset`; slope = median of the 298.15 K lower-hull segment in nine Cu-Zr assessments:
49.7 / 51.8 / 40.1 / 40.1 kJ/mol per unit x; sigma_comp 1.66 / 0.78 / 1.39 / 0.47 kJ/mol-atom). (2) The [46]
values (Zaitsev and Zaitseva 2003) are enthalpies at 1123 K from fcc-Cu and bcc-Zr (text p. 435; Fig. 4 replots them
for fcc-Cu / hcp-Zr): converted to fcc-Cu / hcp-Zr at 1123 K with the SGTE unary lattice stability H(BCC_A2,Zr) -
H(HCP_A3,Zr) = 4206.77 J/mol at 1123 K, x_Zr-weighted (conversion in the record's `corrections`, printed value
kept; T stays 1123 K, which is how ESPEI 0.9.1 evaluates _FORM data; its format has no per-dataset reference phase).
(3) Cu10Zr7 [33] and converted [46] disagree by 8 kJ/mol-atom (13 sigma): `mutually_inconsistent` (not certified),
scatter sigma 5.63 kJ/mol-atom; converted [46] CuZr / CuZr2 take their group sigmas (8.75 / 3.48). (4) Primary works
linked in `cited_sources` (Kleppa-Watanabe 1982, Ansara 1982, Sommer-Choi 1989, Yamaguchi 2008, Zaitsev 2003; Sidorov
1989 has no DOI). espei_ready 11,919 -> 11,928 (9 Cu-Zr values); ESPEI experimental datasets 975 -> 984
(2,932 -> 2,941 values); all Cu-Zr datasets give finite ESPEI likelihoods.

**Targeted cleanup of flagged records (2026-10-24, PI-approved).** Every remaining flagged invariant table and
value group was checked on the rendered PDF page (642 new page checks in `tools/literature_visual_checks.json`, one
per table group or record: page, image hash, verdict, what was seen; no images published). Invariant phase lists:
column headers and composition labels read as phases ('Phase 2', 'X^M', 'φ1', 'reactive phase', 'sample
(nominal)', a liquid taken from a 'composition of liquid' header) dropped on the checked rows, phases the printed
reaction names but the reading missed added, reaction types set to the printed one (e.g. EO -> eutectoid,
'Peretectic'), rows of ternary systems moved to the system the page names (Al-Mg-Zn, Cr-Ni-Ti, Al-C-Fe, Ag-Bi-Ni,
Bi-Cu-Ni, Fe-Ni-W, Al-Cr-Ni); compositions printed under a dropped label move to `phase_compositions_dropped`,
the stored list stays in `phases_stored`. Phase repeats are now found with a spelling-independent key (subscripts,
LaTeX and spelled Greek letters, ″ = two primes, separators); numbered liquids (L1, L2, Liquid#2) count as liquids
(this also restores 98 second liquids that the earlier repeat rule had dropped). Binary invariants with four or more
phases 279 -> 25 (20 of them degenerate reactions printed so: accepted, not ESPEI-ready); reaction phase / liquid
count flags 418 -> 164, of which 140 are printed so by the paper (`*_as_printed`) and 24 remain unsettled (all not
ESPEI-ready). Values (`page_fix:<id>`, applied before the other gates, stored values kept): J vs kJ and
per-formula-unit headers (Li-Sb partial enthalpies, rare-earth sesquioxides Ln2O3 per 5 atoms, U-O 'J/mol of atom',
Zn3P2, Cs5Te3, LaFe12O19 printed -5745 kJ/mol, Nb2N printed -293 kJ/mol, Nb-Re per-atom column, Ge-P entropy header
misprint, ...), Ag-Cu-Sn Table I starred rows °C -> K, binary oxide / phosphide rows of multi-element tables moved
to their binary system; values found not to be what is printed (Cp polynomial coefficients, lattice parameters
read as enthalpies, compositions read as temperatures, a transformation enthalpy stored as a formation enthalpy) not
accepted; values printed as stored but outside the physical range stay accepted and are not ESPEI-ready
(`value_outside_typical_range_as_printed`); unsigned magnitudes printed without a minus sign (Mn3O4 block, Li3Sb
ΔfG) flagged `unsigned_magnitude_in_print`. Evidence class on 'Calculated ...' tables: 199 rows confirmed as cited
or own measurements in separate experimental columns, 1 set to model, 14 values read from Okamoto-assessed
diagrams set to unspecified; the UO3 'S°_f' entropies are standard absolute entropies (unchanged).
Standard reference temperature (PI rule '298 K is 298.15 K'): 2,349 values stored at 298 K are stored at 298.15 K
(printed string kept, `standard_reference_temperature`). Duplicates: labels compared by spelling key, contained
words and formula composition; 4,002 cosmetic duplicates merged in all (936 more), two readings of one printed
value with different phases flagged `phase_label_readings_disagree` (541). Compositions printed far from a label's
formula are flag-only (`composition_label_mismatch`, 183; real solubilities as printed). Liquid / amorphous
properties at room temperature (CaO(liq-am) Cp, S) are not ESPEI-ready. Records 74,474 -> 73,538; accepted
73,165 -> 72,359; espei_ready 11,956 -> 11,919; espei_certified 1,912 -> 1,917. ESPEI bundle: every value the
release marks not ESPEI-ready is now excluded (`not_espei_ready:literature_gate`; 57 ZPF values before); dataset
temperatures of 298 K are written as 298.15 K, so ESPEI's `filter_temperatures` drops nothing (251 compound-formation
datasets contributed nothing before); one observation supplies one value per folder; ZPF duplicates are removed
again after E2; printed sigmas below 0.1 x ESPEI's default use the default in the weight (Li-Sb +-0.011 kJ);
`experimental/MG-O/MgO-18Lia.zpf-00.json` left out (pycalphad evaluation not reproducible). Datasets / values:
experimental 1,012 / 3,012 -> 975 / 2,932, model 542 / 845 -> 526 / 828, invariants 1,673 / 5,576 -> 1,656 /
5,486, assessed 654 -> 650, DFT literature 441, MP 1,218, OQMD 1,218; ESPEI 0.9.1 likelihood of all 8,256 datasets
finite, none empty; `invariants/PD-TI/PdTi-11Guo.zpf-00.json` and `invariants/AL-S/AlS-19Shi.zpf-01.json` also left
out (NaN / -inf in one of several repeated full evaluations);
a temperature corrected on the page is written into the dataset. Dataset 6: item B034 of the blind expert sample (AU-LI p123 field 15) corrected to the expert's
name β’+δ2 (`expert_reviewed`, machine name in `name_history`). Cu-Zr compound formation enthalpies (Zeng 1994 Table 1, Turchanin
2008 Table 3 and text p. 435, checked on the page): the calorimetric values are at 298 K (stored 1123 K corrected),
[46] values are derived at 1123 K from fcc-Cu and bcc-Zr (reference state corrected, not ESPEI-ready), values measured
at another stoichiometry (Cu3Zr, Cu3Zr2, Cu4Zr, Cu9Zr2) flagged `stoichiometry_mismatch`, Zeng's 'measured' columns
flagged as the same measurements Turchanin lists with printed sigmas (`related_records` both ways), CuZr and CuZr2
flagged `mutually_inconsistent` (spread 15 kJ/mol-atom; scatter-aware sigma 8.7 / 3.5 kJ/mol-atom, never
certified), 'T. p.' values `temperature_not_printed`, melting entropies recoded SM_FUSION at the printed melting
temperatures. Compound pages: the energy-above-hull column is kJ/mol-atom (it was labelled eV/atom; an eV/atom column
is added); the MCP server's `e_above_hull_eV` is converted. Merged duplicate readings keep the other spellings of a
single phase (`label_variants`, used by the DFT parity match). DFT parity 7,696 points (MAE MP 10.8, OQMD 9.4
kJ/mol-atom); Kim et al. 2017: 159 formulas, MAE 3.89.

**Literature-level consistency gates (2026-10-23).** Every literature value was checked against its table, its
paper, the physics of its quantity and the calculated SGTE diagrams of its system (12 gates, `tools/literature_gates.py`,
literature/QUALITY_FIXES.md section 7). Corrections were made only where the evidence is printed (header, caption,
heading) or follows from a whole table, and every table-level unit / sign / scale correction and every system
reassignment was confirmed on the rendered PDF page (515 page checks, `tools/literature_visual_checks.json`: page,
image hash, verdict, what was seen; no images published). Stored values are kept (`value_stored`,
`temperature_K_stored`, `system_stored`, ...) and each changed record carries `corrections`; demoted or flagged
records carry `gate_failures`. No printed value or quote changed. 77,540 -> 74,474 records (3,066 cosmetic duplicates
merged: an UNKNOWN beside a named phase, L vs liquid, glyph variants); accepted 76,600 -> 73,165; espei_ready
12,221 -> 11,956; espei_certified 1,928 -> 1,912. Corrections: 132 table temperatures (°C tables stored as K: Ag-Pt
Table 6, Ag-Cu-Sn Table I, Bi-Sb-Sn Table V, Ce-Cu-Sn Table 4, Si-Pb, SiO decomposition) plus 11 rows read on the
page (Ru-U Table 6 °C column, B-C-Si "This work" rows); 316 J-vs-kJ / x10^3 table scales (Co-Ge, Co-Zr, Cr-Si, Ni-Ti,
Fe-Ti a_Ti x10^3, Li-Sb partial enthalpies, Nb borides, rare-earth sesquioxides ...); 171 per-gram heat capacities
relabelled J/g/K; 31 values under a printed (-ΔfH) heading negated (Al-Pt); 12 signs read on the page; 177 values
moved to the system their phases and caption name (cement notation C-S -> Ca-O-Si, Al-C-Fe, Au-Sn, Gd-Si, Ce-Mg-Y,
Fe-Y, Er-Fe, Co-Mo ...); 286 "Gibbs free energy of formation" values recoded GM_MIX -> GM_FORM; fusion / lattice
stability / entropy-increment / magnetic and excess entropy codes; 619 invariant phase lists cleaned of repeated
liquids and non-phase labels. Demoted (not accepted): values outside physical ranges, Redlich-Kister parameters
and Cp polynomial coefficients stored as properties (185), compositions or dashes read as temperatures, liquids at
impossible temperatures, values the page check found misread (79) or belonging to a higher-order system (8).
Flagged (not ESPEI-ready): inconsistent reaction phase counts, binary rows with four phases, compositions not summing
to one, activities rounded to 0, evidence-class changes suggested by wording but not checked on the page.
Evidence class: 47 model -> experimental (cited) and 8 model -> dft, each confirmed on the page (31 suggestions
rejected there); values from ASM / JPE phase-diagram evaluations flagged `from_evaluation_paper`. `reader_agreement`
derived from `readers` where the record builder had not set it (`reader_agreement_basis`); `reader_tier` documented
as a pipeline status. CALPHAD cross-check now carries `dx` and `fail_reason`; the 1 atm default pressure is
`assumed_default_1_atm_not_printed`. ESPEI bundle rebuilt (experimental 1,012 datasets / 3,012 values, model 542 /
845, invariants 1,673 / 5,576, DFT literature 441, MP 1,218, OQMD 1,218, assessed 654); ESPEI 0.9.1 likelihood
evaluation of all 8,336 datasets against their TDB finite. DFT benchmark 7,745 points (MAE vs MP 11.0, OQMD 9.6
kJ/mol-atom); Kim et al. 2017 cross-check 162 formulas, MAE 3.87. Parquet columns `gate_failures`,
`corrections_json`, `temperature_K_stored`, `system_stored`, `evidence_class_before_gates`,
`property_code_before_gates`, `reader_agreement_basis`, `plausibility_dx_json`. Dataset card counts corrected
(papers 1,321, systems 1,392).

**ESPEI phase assignment fixed; ESPEI readiness split into ready / certified (2026-10-23).** Root cause: the corpus
ESPEI writer gave every thermochemical dataset the phase LIQUID when no printed label mapped to a model phase, and
added LIQUID beside every mapped phase, so compound formation enthalpies (e.g. Fe17Y2, Saenko 2017 table 5, 973 K)
were written as liquid data; the literature records themselves were correct. Each ESPEI value's phase is now taken
from its published record by a physical phase rule (`tools/phase_rule.py`; literature/QUALITY_FIXES.md section 6;
espei/README.md "Phase assignment"): printed label or caption only, never a default; liquid only where physically
possible; formation enthalpies / entropies of line compounds as `solver` endmember datasets (tag
`compound_formation_endmember`); other compound properties not used. New ESPEI gates (activities outside (0, 1],
negative absolute entropies, increments, per-gram heat capacities, implausible magnitudes, reference phases absent
from the TDB, gas without pressure, off-invariant binary three-phase regions, inert ZPF regions, duplicates) and a
likelihood evaluation of every dataset against its TDB with ESPEI 0.9.1 (all 8,156 written datasets finite).
Literature: `flags.espei_ready` now also requires the phase rule and no blocking flag (12,221 true, was 14,205);
new `espei_certified` (ready and agreeing with the pycalphad cross-check; 1,928), `espei_certified_basis`,
`calphad_check` (323 ready values disagree, 9,970 have no prediction), `espei_ready_upstream`, `espei_phase_rule`,
`espei_blocked_by`; reference phase names `1` / `A1` completed to `1/2_MOLE_X2(G)` / `FCC_A1` (1,675; section 5b).
No printed value or label changed. ESPEI bundle: experimental 909, model 464, invariants 1,672, DFT literature 442,
Materials Project 1,218, OQMD 1,218, assessed 654 datasets (VALIDATION.md). Parquet columns `flag_espei_certified`,
`flag_espei_ready_upstream`, `calphad_check`, `espei_certified_basis`, `espei_phase_rule_result/_reason`,
`espei_blocked_by`.

**Literature values re-exported** from the record store db-v2.1 v2.1.19r: 77,540 values (was 76,432; general
tables 45,088), 76,600 accepted, 1,391 systems, 4,881 papers and cited works. Every table value now carries
`reader_agreement` / `reader_agreement_label`: `multi_reader` 41,809, `single_reader_text_layer` 2,385,
`single_reader` 894 (806 accepted; the data explorer shows a "single reader" badge; treat as unconfirmed); a blind
second Claude read (`claude-opus-5.5#2`) counts as a second reader. DFT benchmark 7,888 points; Kim et al. 2017
cross-check unchanged (162 formulas, MAE 3.85 kJ/mol-atom). Phase registry, Parquet tables and static pages rebuilt.

New dataset **ORCHID ESPEI datasets from the literature** (`espei/`, Zenodo record `espei`,
10.5281/zenodo.23735788, `hasPart` of the umbrella; Version 1, machine-extracted): 7,639 ESPEI 0.9.1
datasets with 19,419 values — experimental 1,679, model
758, invariant ZPF 2,143, DFT literature
479, Materials Project 1,290, OQMD
1,290 — gated by the published literature values, each value with its observation id,
source DOI, uncertainty (printed, ESPEI default or DFT sigma calibrated against experiment) and ESPEI weight;
validated with ESPEI check_dataset / load_datasets. Built by `tools/build_espei_bundle.py` (orchid-project.org).

New dataset **ORCHID bibliography** (`bibliography/`, Zenodo record `bibliography`, 10.5281/zenodo.23736021,
`hasPart` of the umbrella; Version 1, machine-extracted): 9,568 works (7,812 with DOI),
their roles in ORCHID, evidence counts and 60,231 typed relations with provenance; Crossref metadata (CC0).
DOIs that upstream matchers found for printed references (handbook source lines, cited sources of values, TDB header
citations) are now checked against Crossref (first author, year ±1, title, journal): `doi_match` verified
5,385, weak 104 (kept, flagged), no Crossref record
23; 19 mismatched DOIs were dropped (works kept without
DOI; `bibliography/DOI_MISMATCHES.md`). Hugging Face configs `bibliography_papers`, `bibliography_edges`. Built by
`tools/build_bibliography.py` (orchid-project.org).

Release metadata: nine Zenodo records (eight datasets plus the umbrella); `zenodo/espei.metadata.json`,
`zenodo/bibliography.metadata.json`, umbrella `hasPart`, `zenodo/dois.json` placeholders.

## Pre-release development — assessed phase assemblages v1 (2026-10-23)

New dataset **ORCHID assessed phase assemblages (binary systems)** (`assessed-phase-assemblages/`, Zenodo record
`assessed-phase-assemblages`, 10.5281/zenodo.23735996, `hasPart` of the umbrella; Version 1,
machine-extracted): one (T, x, P) point deep inside each named phase field of the expert-drawn (assessed) binary
diagrams compiled in Okamoto's Desk Handbook (annotation run-20261021h-full), evidence class `assessed_phase_diagram`.
23,131 points from 2,178 diagrams (area centroid 21,618, pole of inaccessibility 1,513), with phase-registry ids,
coordinate uncertainty from the axis calibration, naming basis, confidence, review state, a cross-check against the
calculated SGTE diagrams (82.3% agreement where comparable) and citations (original evaluation first, the handbook
as compilation). Two-phase points carry phases with unknown compositions; 11,962 also carry a drawing-based tie_line
block (low credence). ESPEI ZPF datasets, one per diagram (1,070; default with null endpoints, and a tie-line
variant), validated with ESPEI 0.9.1. Data only: no page images, crops or handbook text (build-time guard). Built by
`tools/build_assessed_assemblages.py` (orchid-project.org).

## Pre-release development — phase registry v0 (2026-10-23)

New dataset **ORCHID phase registry (binary systems)** (`phases/`, Zenodo record `phase-registry`,
10.5281/zenodo.23735970, `hasPart` of the umbrella): 10,496 phases in 1,241 binary systems, 43,251 names
(TDB 22,556, paper labels 8,463, corpus 10,916, Materials Project 658, OQMD 658), 22,556 TDB phase declarations, stability from the
calculated diagrams, up to 10 example references per phase (9,927 phases with references, 3,014 distinct DOIs).
Structure types: 6,259 from the standard phase name (tier A), 150 DFT-supported (tier B: unique Materials Project +
OQMD on-hull match), 1,253 assessment-declared (tier C, assessor-stated: exactly one consistent structure in the
Hallstedt 2025 crystallographic table for that phase name and system), 1,305 liquid and 231 gas; 1,240 phases in the
review queue with candidates, 58 without candidates. Every TDB model carries `tdb_definition`: the verbatim PHASE,
CONSTITUENT and TYPE_DEFINITION statements with line numbers (8,392 distinct type definitions), a parsed view
(type codes, sublattices, site ratios, constituents with major-constituent markers, magnetic model, order/disorder
partner), parameter counts by kind and interaction order, and links to the file on orchid-project.org and in
orchid-calphad/orchid-pipeline. Built by `tools/build_phase_registry.py` (orchid-project.org).

File layout: every file stays below 45 MB (GitHub warns at 50 MB). `phases/registry.json` (7.8 MB) is a compact index
of all phases (id, system, names, structure summary with tier and prototype, counts, `detail` file); the full records,
including `models[].tdb_definition` and `references`, are in `phases/systems/<SYS>.json` (one per system, largest
0.37 MB). JSON-LD, CSV and Parquet are unchanged.

AI-ready access: `phases/structure_types.csv` and `phases/structure_types.parquet` (1,563 structure types; row counts
and content hashes in `phases/parquet.json`); Hugging Face configs `phases` (`phases/registry.parquet`) and
`structure_types` in `DATASET_CARD.md` / `hf/README.md`, with column descriptions and the tier definitions; static,
JavaScript-free pages `phases/pages/<SYS>.html|.md` for the 1,241 binary systems (every phase with id, names,
tier/basis, prototype, Strukturbericht, Pearson symbol, space group, stability summary, verbatim PHASE and
CONSTITUENT statements, example DOIs; schema.org Dataset / DefinedTerm JSON-LD) and `phases/pages/index.html|.md`,
linked from the system pages and listed in `sitemap.xml`, `llms.txt`, `llms-full.txt` and `index.md`. The static pages
are web views and not part of the Zenodo record.

## Pre-release snapshot — Version 1, machine-extracted (2026-10-22)

First citable release of the ORCHID data, archived on Zenodo as four datasets, each its own record and DOI, plus
the umbrella record *ORCHID data* that links them (DataCite `isPartOf` / `hasPart`).

**Status.** Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

### Records

| Record | DOI | Content |
|---|---|---|
| ORCHID data (umbrella) | 10.5281/zenodo.23736065 | README, CHANGELOG, DATASET_CARD, licences and attributions, Parquet manifest, Zenodo metadata |
| ORCHID literature values | 10.5281/zenodo.23735569 | `literature/` (except the DFT benchmark files); Parquet `literature_values`, `papers`, `experimental_context` |
| ORCHID calculated binary phase diagrams | 10.5281/zenodo.23735859 | `phase-diagrams/`; Parquet `phase_diagram_index`, `phase_diagram_invariants` |
| ORCHID binary convex hulls (MP, OQMD, assessed CALPHAD) | 10.5281/zenodo.23735891 | `hulls/`; Parquet `hull_vertices` |
| ORCHID DFT-vs-experiment formation-enthalpy benchmark | 10.5281/zenodo.23735943 | `literature/dft_parity.json`, `literature/kim2017_crosscheck.*`; Parquet `dft_parity` |

File lists with sizes and SHA-256: `zenodo/<record>.files.json`.

### Contents and counts

- **Literature values:** 76,432 values from 1,322 papers covering 1,390 chemical systems; 75,491 accepted
  (reader agreement plus deterministic checks). Evidence classes: experimental 36,918, model 28,148 (13,586 linked to
  the exact TDB file by SHA-256), DFT 6,162, unspecified 5,204. Record kinds: invariant-reaction tables 26,693,
  general tables 43,980, running text 5,759 (each with a verbatim quote and page). Bibliography of 4,877 reporting
  papers and cited works; experimental context of 225 papers (1,504 items).
- **Calculated binary phase diagrams:** 2,774 SGTE binary databases (Hallstedt 2025), 2,720 calculated with
  pycalphad 0.11.2 and 54 failed; 24,828 invariant equilibria.
- **Binary convex hulls:** Materials Project 2026.04.13 (3,828 systems, 12,829 vertices), OQMD v1.8 (3,916
  systems, 15,314 vertices), assessed SGTE CALPHAD isotherms at 298.15 K (2,695 assessments, 1,223 systems).
- **DFT-vs-experiment benchmark:** 7,826 literature x DFT points (3,738 Materials Project, 4,088 OQMD) from 4,188
  records and 962 compounds; default subset MAE 10.9 kJ/mol-atom (1,231 MP pairs) and 9.6 (1,294 OQMD pairs).
  Kim et al. 2017 cross-check: 162 formulas in common, MAE 3.85 kJ/mol-atom, 19 differing by more than 10.
- **Parquet:** seven tables with a by-paper train/validation/test split (59,967 / 7,527 / 8,938 values).

### Clean-up before release (details: `literature/QUALITY_FIXES.md`, `literature/quality_fixes.json`)

- **Duplicates:** 3,510 exact duplicates merged in 3,314 groups (the removed ids are listed in the surviving record's `merged_ids`).
- **Controlled vocabularies:** `transition_kind` for 21,444 records (187 printed variants, 15,910 relabelled; the
  printed form kept in `transition_kind_printed`); 504 malformed property codes mapped (raw code in
  `property_code_raw`).
- **Garbled fields:** 2 non-page `quote_page` values set to null (`page_unreadable`); `temperature_bound` and
  `reference_state` normalised to objects; 1 reader comment not printed in the quote dropped.
- **DFT-parity outliers:** 238 large residuals examined: 47 per-formula values labelled per atom converted
  (`basis_corrected_from_formula`), 31 unsigned magnitudes flagged and excluded from the default parity set
  (`unsigned_in_print`), 160 flagged `dft_outlier_unexplained` and kept.
- **Energy units:** mixing and partial quantities converted to kJ/mol-atom when the per-atom basis is explicit
  (1,132) and to `kJ/mol (basis unstated)` otherwise (1,995; 9 heuristic per-atom labels demoted); 2,680
  formation values per atom only by a magnitude heuristic are flagged `basis_inferred_from_magnitude`.
- **Field placement:** fields not printed in a value's quote or row were removed (only their existence is
  recorded, `has_dropped_fields`).
- **Website and data site:** "prototype" / "in review" labels replaced by the Version 1 status; counts in
  `DATASET_CARD.md` recomputed from the data.

### Citation metadata

- Top-level `cite_as` (text, BibTeX, DOI of the dataset and of the umbrella record, sources to cite as well) in
  `literature/index.json`, every `literature/systems/*.json`, `phase-diagrams/index.json`, the three hull catalogs,
  `literature/dft_parity.json` and `parquet/MANIFEST.json`; `orchid.cite_as`, `orchid.doi`, `orchid.citation` and
  `orchid.dataset` key-value metadata in every Parquet file; `literature/CITATION.txt` beside the CSV (a comment line
  would break CSV readers); `CITATION.cff` at the top and in `literature/`, `phase-diagrams/` and `hulls/`; a
  "Please cite" box with BibTeX on every static page.
- The hull catalogs now differ from the open-tdb copies only by the added `cite_as` key.

### Known limitations

- Version 1 is machine-extracted; a hand-checked precision sample is in progress. Values in figures are not
  included and coverage is uneven across systems.
- 2,765 formation values have a per-atom vs per-formula basis the paper does not state (`kJ/mol (basis unstated)`,
  not converted); 2,680 are per atom only by a magnitude heuristic.
- Uncertainties with basis `stated_default` (23,133) or `reading_resolution` (6,936) are placeholders; only
  `printed` (3,742) and `printed_range` (23) are the source's own.
- `experimental` values cited from older work carry the citing paper's reading; `unspecified` values may be
  experimental or calculated. `flag_source_disputed` (512), `flag_magnitude_suspect` (499) and
  `flag_system_mismatch` (495) mark values to check; 44 values are printed without a sign by the paper's
  convention (`flag_unsigned_in_print`).
- `flag_espei_ready` is an automatic completeness flag, not a review verdict; do not feed values to an optimizer
  without review.
- Calculated phase diagrams and hulls are model results, not measurements; 54 SGTE files did not calculate; DFT
  hulls are at 0 K and Materials Project and OQMD energies are not comparable with each other.
