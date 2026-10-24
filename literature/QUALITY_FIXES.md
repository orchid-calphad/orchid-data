# ORCHID literature data: quality fixes

Release: `orchid-literature 2026-10-23 (record store db-v2.1: invariant/general v2.1.19r, text+context fixup-20261022)`. Written by `tools/export_literature_data.py` via `tools/literature_quality.py` (deterministic). Machine-readable copy: `quality_fixes.json`.

Every rule re-labels, normalizes, merges or flags; no value is invented. Where a value changed, the original is kept in the record (`value_before_quality_fix`, `transition_kind_printed`, `property_code_raw`, `value_stored`/`unit_stored`, `merged_ids`).

## 1. Duplicates

Records identical in paper, page, property, value, unit, temperature, phases and quote, and in every field that distinguishes two printed states (compositions, component, reference state, method, evidence class, cited sources, reaction, range, structure, bound, uncertainty), were merged into one record; the others are listed in its `merged_ids` (and `merged_pids` when they came from other rows/artifacts).

| scope | groups | records removed |
|---|---:|---:|
| same row | 2614 | 2614 |
| rows of one artifact | 561 | 757 |
| several artifacts | 155 | 179 |
| **total** | **3330** | **3550** |

## 2. Controlled vocabularies

`transition_kind` (21703 records, 187 printed variants, 15971 relabelled); raw value in `transition_kind_printed`; `reaction.type` carries the controlled term.

| transition_kind | records |
|---|---:|
| congruent melting | 2319 |
| congruent transformation | 652 |
| critical point | 80 |
| eutectic | 5625 |
| eutectoid | 1054 |
| magnetic | 252 |
| metatectic/catatectic | 183 |
| monotectic | 196 |
| monotectoid | 26 |
| order-disorder | 23 |
| other | 4004 |
| peritectic | 4467 |
| peritectoid | 783 |
| polymorphic | 828 |
| quasi-peritectic | 1202 |
| syntectic | 9 |

Mapped printed variants (all; `rule` says why):

| printed | transition_kind | rule | n |
|---|---|---|---:|
| Congruent | congruent melting | congruent_with_liquid_phase | 1456 |
| congruent | congruent melting | congruent_with_liquid_phase | 328 |
| Melting | congruent melting | keyword | 248 |
| Congruent melting | congruent melting | keyword | 64 |
| melting | congruent melting | keyword | 54 |
| congruent melting | congruent melting | keyword | 38 |
| Melting point | congruent melting | keyword | 29 |
| Congruent Melting | congruent melting | keyword | 25 |
| Congruent reaction | congruent melting | congruent_with_liquid_phase | 21 |
| Congruent point | congruent melting | congruent_with_liquid_phase | 15 |
| C.M. | congruent melting | keyword | 13 |
| melting point | congruent melting | keyword | 10 |
| Fusion | congruent melting | keyword | 4 |
| congruent melting point | congruent melting | keyword | 4 |
| fusion | congruent melting | keyword | 4 |
| Congruently melting | congruent melting | keyword | 3 |
| congruent point | congruent melting | congruent_with_liquid_phase | 3 |
| congruent | congruent transformation | congruent_without_liquid_phase | 565 |
| Congruent | congruent transformation | congruent_without_liquid_phase | 69 |
| congruent transformation | congruent transformation | keyword | 7 |
| Congruent point | congruent transformation | congruent_without_liquid_phase | 5 |
| congruent point | congruent transformation | congruent_without_liquid_phase | 4 |
| Congruent transformation | congruent transformation | keyword | 2 |
| Critical | critical point | keyword | 46 |
| Critical point | critical point | keyword | 16 |
| critical point | critical point | keyword | 13 |
| Critical pt. | critical point | keyword | 2 |
| Tricritical | critical point | keyword | 2 |
| Critical Point | critical point | keyword | 1 |
| Eutectic | eutectic | keyword | 2899 |
| eutectic | eutectic | keyword | 1764 |
| E | eutectic | letter_label | 683 |
| e | eutectic | letter_label | 170 |
| Eutectic reaction | eutectic | keyword | 68 |
| Eutectic (Degenerated invariant equilibrium) | eutectic | keyword | 12 |
| I | eutectic | letter_label | 7 |
| Eutectics | eutectic | keyword | 3 |
| Quasibinary Eutectic | eutectic | keyword | 3 |
| Ternary Eutectic | eutectic | keyword | 3 |
| eutectic 1 | eutectic | keyword | 3 |
| eutectic 2 | eutectic | keyword | 3 |
| e2, eutectic | eutectic | keyword | 2 |
| eutectic crystallization | eutectic | keyword | 2 |
| metastable eutectic | eutectic | keyword | 2 |
| Almost degenerate eutectic | eutectic | keyword | 1 |
| Eutectoid | eutectoid | keyword | 812 |
| eutectoid | eutectoid | keyword | 198 |
| Eutectoid reaction | eutectoid | keyword | 18 |
| eutectoid 1 | eutectoid | keyword | 3 |
| eutectoid 3 | eutectoid | keyword | 3 |
| eutectoid 4 | eutectoid | keyword | 3 |
| eutectoid 5 | eutectoid | keyword | 3 |
| eutectoid decomposition | eutectoid | keyword | 3 |
| Eutectiod | eutectoid | keyword | 2 |
| Eutectoid (cont.) | eutectoid | keyword | 2 |
| Eutectoidal | eutectoid | keyword | 2 |
| e1, eutectoid | eutectoid | keyword | 2 |
| eutectoid 2 | eutectoid | keyword | 2 |
| Postulated eutectoid | eutectoid | keyword | 1 |
| magnetic | magnetic | keyword | 221 |
| Double degenerated (magnetic ordering of B33) | magnetic | keyword | 10 |
| Degenerated (magnetic ordering of A2) | magnetic | keyword | 6 |
| Double degenerated (magnetic ordering of Fe2B) | magnetic | keyword | 6 |
| Double degenerated (magnetic ordering of bct-Fe3B) | magnetic | keyword | 6 |
| Degenerated (magnetic ordering A2) | magnetic | keyword | 2 |
| Magnetic transition | magnetic | keyword | 1 |
| Metatectic | metatectic/catatectic | keyword | 100 |
| Catatectic | metatectic/catatectic | keyword | 69 |
| metatectic | metatectic/catatectic | keyword | 10 |
| Catatectic reaction | metatectic/catatectic | keyword | 2 |
| Catatectic(a) | metatectic/catatectic | keyword | 1 |
| catatectic | metatectic/catatectic | keyword | 1 |
| Monotectic | monotectic | keyword | 99 |
| monotectic | monotectic | keyword | 96 |
| Metastable Monotectic | monotectic | keyword | 1 |
| monotectoid | monotectoid | keyword | 17 |
| Monotectoid | monotectoid | keyword | 8 |
| Monotectoid (a) | monotectoid | keyword | 1 |
| ordering | order-disorder | keyword | 9 |
| Order-disorder | order-disorder | keyword | 6 |
| Order–disorder | order-disorder | keyword | 4 |
| Ordering reaction fcc ↔ L12 | order-disorder | keyword | 3 |
| Ordering reaction fcc ↔ L10 | order-disorder | keyword | 1 |
| other | other | no_rule | 1608 |
| liquidus | other | no_rule | 1554 |
| solidus | other | no_rule | 418 |
| max | other | unqualified_letter_or_extremum | 101 |
| Transition | other | no_rule | 64 |
| saddle | other | no_rule | 31 |
| Degenerate | other | no_rule | 19 |
| Eutectic (or peritectic) | other | ambiguous_printed_alternative | 19 |
| invariant | other | no_rule | 19 |
| transition | other | no_rule | 12 |
| Maximum | other | unqualified_letter_or_extremum | 9 |
| min | other | no_rule | 8 |
| C | other | unqualified_letter_or_extremum | 7 |
| Incongruent m.t. | other | no_rule | 7 |
| azeotropic melting minimum | other | no_rule | 7 |
| δ/bcc_A2 phase boundary (upper) | other | no_rule | 7 |
| Degenerated | other | no_rule | 6 |
| EO | other | no_rule | 6 |
| decomposition | other | no_rule | 6 |
| incongruent | other | no_rule | 6 |
| maximum | other | unqualified_letter_or_extremum | 5 |
| Congruent formation | other | no_rule | 4 |
| P.T. | other | no_rule | 4 |
| Peretectic | other | no_rule | 4 |
| solidus or eutectic | other | ambiguous_printed_alternative | 4 |
| Congruent transition | other | no_rule | 3 |
| Eutctoid | other | no_rule | 3 |
| Remelting | other | no_rule | 3 |
| Structure transformation | other | no_rule | 3 |
| allotropic or solvus | other | ambiguous_printed_alternative | 3 |
| crystallization | other | no_rule | 3 |
| e2 | other | no_rule | 3 |
| e3 | other | no_rule | 3 |
| p1 | other | no_rule | 3 |
| p3 | other | no_rule | 3 |
| Azeotropic melting | other | no_rule | 2 |
| Boiling point | other | no_rule | 2 |
| Congruent m.t. | other | no_rule | 2 |
| Decomposition | other | no_rule | 2 |
| Dissociation | other | no_rule | 2 |
| Fe17Tm2 Metastable from154.7 to 0 °C | other | no_rule | 2 |
| Freezing point | other | no_rule | 2 |
| PO | other | no_rule | 2 |
| Peritictic | other | no_rule | 2 |
| e1 | other | no_rule | 2 |
| e4 | other | no_rule | 2 |
| eutectoïd | other | no_rule | 2 |
| minimum point | other | no_rule | 2 |
| p2 | other | no_rule | 2 |
| p4 | other | no_rule | 2 |
| ? | other | no_rule | 1 |
| Congurent | other | no_rule | 1 |
| Isomeric transition | other | no_rule | 1 |
| Metatetic | other | no_rule | 1 |
| Pertectic | other | no_rule | 1 |
| Transformation | other | no_rule | 1 |
| crystallographic | other | no_rule | 1 |
| dissociation | other | no_rule | 1 |
| second order | other | no_rule | 1 |
| Peritectic | peritectic | keyword | 2752 |
| peritectic | peritectic | keyword | 1184 |
| P | peritectic | letter_label | 369 |
| p | peritectic | letter_label | 68 |
| Peritectic reaction | peritectic | keyword | 34 |
| Peritetic reaction | peritectic | keyword | 16 |
| peritectic crystallization | peritectic | keyword | 10 |
| Peritecitc | peritectic | keyword | 6 |
| III | peritectic | letter_label | 4 |
| peritectic 1 | peritectic | keyword | 3 |
| peritectic 2 | peritectic | keyword | 3 |
| peritectic 3 | peritectic | keyword | 3 |
| peritectic decomposition | peritectic | keyword | 3 |
| Degenerate peritectic | peritectic | keyword | 2 |
| Gas-peritectic | peritectic | keyword | 2 |
| p1, peritectic | peritectic | keyword | 2 |
| p2, peritectic | peritectic | keyword | 2 |
| p3, peritectic | peritectic | keyword | 2 |
| Gas–peritectic | peritectic | keyword | 1 |
| Peritectic-like | peritectic | keyword | 1 |
| Peritectoid | peritectoid | keyword | 608 |
| peritectoid | peritectoid | keyword | 120 |
| Peritectoid reaction | peritectoid | keyword | 12 |
| Peritectiod | peritectoid | keyword | 11 |
| Perictectoid | peritectoid | keyword | 8 |
| Peritictoid | peritectoid | keyword | 8 |
| peritectoid recrystallization | peritectoid | keyword | 4 |
| peritectoid 1 | peritectoid | keyword | 3 |
| peritectoid 3 | peritectoid | keyword | 3 |
| peritectoid 4 | peritectoid | keyword | 3 |
| Gas–peritectoid | peritectoid | keyword | 2 |
| peritectoid 2 | peritectoid | keyword | 1 |
| polymorphic | polymorphic | keyword | 466 |
| Polymorphic | polymorphic | keyword | 157 |
| Allotropic | polymorphic | keyword | 135 |
| solid state transition | polymorphic | keyword | 15 |
| Allotropic transformation | polymorphic | keyword | 14 |
| Polymorphic-transformation | polymorphic | keyword | 12 |
| Polymorphic transformation | polymorphic | keyword | 8 |
| Polymorphic transition | polymorphic | keyword | 5 |
| Double degenerated (polymorphic transformation of FeB) | polymorphic | keyword | 4 |
| allotropic | polymorphic | keyword | 4 |
| Allotropic transition | polymorphic | keyword | 3 |
| Allotropy | polymorphic | keyword | 3 |
| Structural transition | polymorphic | keyword | 2 |
| U | quasi-peritectic | letter_label | 1185 |
| II | quasi-peritectic | keyword | 16 |
| Quasi-peritectic | quasi-peritectic | keyword | 1 |
| Syntectic | syntectic | keyword | 9 |

Property codes (528 records; raw code in `property_code_raw`):

| raw | clean | n |
|---|---|---:|
| `ACR_` | `ACTIVITY` | 24 |
| `LATTICE_4F_Z_1_` | `LATTICE_4F_Z_1` | 12 |
| `LATTICE_4F_Z_2_` | `LATTICE_4F_Z_2` | 12 |
| `LATTICE_4F_Z_FIRST_` | `LATTICE_4F_Z_1` | 7 |
| `LATTICE_4F_Z_SECOND_` | `LATTICE_4F_Z_2` | 7 |
| `LATTICE_A_` | `LATTICE_A` | 21 |
| `LATTICE_A_FE50NI50_` | `LATTICE_A` | 1 |
| `LATTICE_A_FE_` | `LATTICE_A` | 3 |
| `LATTICE_A_NI_` | `LATTICE_A` | 1 |
| `LATTICE_B_` | `LATTICE_B` | 10 |
| `LATTICE_COMMENTS_UNLABELLED_VALUE_` | `LATTICE_UNLABELLED_VALUE` | 3 |
| `LATTICE_C_` | `LATTICE_C` | 13 |
| `LATTICE_LATTICE_PARAMETER` | `LATTICE_UNSPECIFIED_AXIS` | 35 |
| `LATTICE_LATTICE_PARAMETERS` | `LATTICE_UNSPECIFIED_AXIS` | 12 |
| `LATTICE_LATTICE_PARAMETERS_ERROR_5_` | `LATTICE_UNSPECIFIED_AXIS` | 7 |
| `LATTICE_LATTICE_PARAMETER_A` | `LATTICE_A` | 112 |
| `LATTICE_LATTICE_PARAMETER_ALPHA` | `LATTICE_ALPHA` | 4 |
| `LATTICE_LATTICE_PARAMETER_B` | `LATTICE_B` | 27 |
| `LATTICE_LATTICE_PARAMETER_C` | `LATTICE_C` | 76 |
| `LATTICE_LATTICE_PARAMETER_DIFFERENCE_AT_AT_25_C_` | `LATTICE_DIFFERENCE_AT_AT_25_C` | 24 |
| `LATTICE_LATTICE_PARAMETER_GAMMA` | `LATTICE_GAMMA` | 2 |
| `LATTICE_VAT` | `LATTICE_V_ATOM` | 90 |
| `LATTICE_V_AT` | `LATTICE_V_ATOM` | 4 |
| `LATTICE__` | `LATTICE_UNSPECIFIED_ANGLE` | 20 |
| `LATTICE__` | `LATTICE_UNSPECIFIED_AXIS` | 1 |

## 3. Garbled fields

`quote_page` values that are not page numbers were set to null with `flags.page_unreadable` (2). `temperature_bound` is always `{op, value_K, printed}` (string forms converted, "none" removed); `reference_state` is always an object (free text becomes `{"printed": ...}`); free text not printed in the quote and longer than 300 characters (reader commentary) was dropped with `flags.reference_state_dropped_not_in_quote` (1).

| id | field | before | after | evidence |
|---|---|---|---|---|
| ORC-T3LAA67CHJ.404a18 | reference_state | pure solid elements at 298.15 K and 1 bar (heat content base definition implied by Meschel and Kleppa context for droppe... (1963 characters | None | free text of 1963 characters not printed in the quote (reader commentary) |
| ORC-O4DJJCAHLH | quote_page | 40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004 | None | not a page number (> 2000 or not a positive integer) |
| ORC-A7W44LTTFR | quote_page | 4323232323 | None | not a page number (> 2000 or not a positive integer) |

## 4. DFT parity outliers

Formation enthalpies (kJ/mol-atom, experimental / model / unspecified) whose single binary formula matches a Materials Project or OQMD entry and that differ from DFT by more than 50 kJ/mol-atom, or have the opposite sign with |DFT - lit| > 10 (238 records), classified in this order:

* `basis_corrected_from_formula` (47): a large-residual case where lit / n_atoms (or lit x n_atoms, undoing an earlier per-formula division) lies within 15 kJ/mol-atom of every matched DFT source, and the printed unit has no per-atom marker or the caption/quote says per mole of compound. Value converted; original in `value_before_quality_fix`, operation in `basis_correction`.
* `sign_from_heading` (0): printed without a minus sign, -lit within 15 of DFT, and the record's printed heading carries the minus (e.g. "-ΔfH"): sign applied, heading in `sign_heading_printed`.
* `unsigned_in_print` (31): printed without a minus sign, -lit within 15 of DFT (and lit itself more than twice that far, so small values near zero are not classified), no negated heading in the record: value kept as printed, flagged, excluded from the default parity set.
* `dft_outlier_unexplained` (160): no rule applies; flagged `flags.dft_outlier_unexplained`, value unchanged.

| id | class | formula | before | after | evidence |
|---|---|---|---:|---:|---|
| ORC-JDJTGHPS4K | basis_corrected_from_formula | HfB | -98.95 | -49.475 | printed unit 'kJ/mol' has no per-atom marker; HfB has 2 atoms per formula unit; -98.95 divided by 2 = -49.48, within 15 of DFT (MP -39.9, OQMD -40.2) |
| ORC-7BRGOIHAWY | basis_corrected_from_formula | Ta3B2 | -13.5294 | -67.647 | printed unit 'kJ/mol' has no per-atom marker; Ta3B2 has 5 atoms per formula unit; -13.5294 multiplied by 5 = -67.65, within 15 of DFT (MP -64.9, OQMD -65.0) |
| ORC-JNRM625MX5 | basis_corrected_from_formula | Ta3B4 | -10.88742857 | -76.212 | printed unit 'kJ/mol' has no per-atom marker; Ta3B4 has 7 atoms per formula unit; -10.8874 multiplied by 7 = -76.21, within 15 of DFT (MP -74.6, OQMD -74.4) |
| ORC-KM6Q5LMCOG | basis_corrected_from_formula | Ta3B4 | -11.43642857 | -80.055 | printed unit 'kJ/mol' has no per-atom marker; Ta3B4 has 7 atoms per formula unit; -11.4364 multiplied by 7 = -80.05, within 15 of DFT (MP -74.6, OQMD -74.4) |
| ORC-VGMMQLZODX | basis_corrected_from_formula | Ta3B2 | -14.26 | -71.3 | printed unit 'kJ/mol' has no per-atom marker; Ta3B2 has 5 atoms per formula unit; -14.26 multiplied by 5 = -71.30, within 15 of DFT (MP -64.9, OQMD -65.0) |
| ORC-2XXL6EGLXQ.a44990 | basis_corrected_from_formula | CaO2(cr) | -659.0 | -219.666667 | printed unit 'kJ.mol-1' has no per-atom marker; CaO2(cr) has 3 atoms per formula unit; -659 divided by 3 = -219.67, within 15 of DFT (MP -212.9, OQMD -220.0) |
| ORC-EONGZNVMF4.e5cd6e | basis_corrected_from_formula | CaO2(cr) | -648.1 | -216.033333 | printed unit 'kJ.mol-1' has no per-atom marker; CaO2(cr) has 3 atoms per formula unit; -648.1 divided by 3 = -216.03, within 15 of DFT (MP -212.9, OQMD -220.0) |
| ORC-FDK7VGPM2Z.234c60 | basis_corrected_from_formula | CaO(cr) | -635.1 | -317.55 | printed unit 'kJ.mol-1' has no per-atom marker; CaO(cr) has 2 atoms per formula unit; -635.1 divided by 2 = -317.55, within 15 of DFT (MP -319.0, OQMD -308.3) |
| ORC-IOMQXHHZHX.39b429 | basis_corrected_from_formula | CaO2(cr) | -652.7 | -217.566667 | printed unit 'kJ.mol-1' has no per-atom marker; CaO2(cr) has 3 atoms per formula unit; -652.7 divided by 3 = -217.57, within 15 of DFT (MP -212.9, OQMD -220.0) |
| ORC-MOABLTWFHR.fd3a6b | basis_corrected_from_formula | CaO(cr) | -634.0 | -317.0 | printed unit 'kJ.mol-1' has no per-atom marker; CaO(cr) has 2 atoms per formula unit; -634 divided by 2 = -317.00, within 15 of DFT (MP -319.0, OQMD -308.3) |
| ORC-N6RZ52LOV5.b9b0c1 | basis_corrected_from_formula | CaO(cr) | -634.6 | -317.3 | printed unit 'kJ.mol-1' has no per-atom marker; CaO(cr) has 2 atoms per formula unit; -634.6 divided by 2 = -317.30, within 15 of DFT (MP -319.0, OQMD -308.3) |
| ORC-XQRAM3624L | basis_corrected_from_formula | CaO(cr) | -634.0 | -317.0 | printed unit 'kJ.mol-1' has no per-atom marker; CaO(cr) has 2 atoms per formula unit; -634 divided by 2 = -317.00, within 15 of DFT (MP -319.0, OQMD -308.3) |
| ORC-YHMSI6IKE4.81e7a6 | basis_corrected_from_formula | CaO(cr) | -635.1 | -317.55 | printed unit 'kJ.mol-1' has no per-atom marker; CaO(cr) has 2 atoms per formula unit; -635.1 divided by 2 = -317.55, within 15 of DFT (MP -319.0, OQMD -308.3) |
| ORC-4TQ3RYV4BP | basis_corrected_from_formula | CuO | -152.3 | -76.15 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -152.3 divided by 2 = -76.15, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-AJGT674S4D.aad2e0 | basis_corrected_from_formula | CuO | -155.77 | -77.885 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -155.77 divided by 2 = -77.89, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-AJGT674S4D.b11196 | basis_corrected_from_formula | Cu2O | -170.83 | -56.943333 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -170.83 divided by 3 = -56.94, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-ALFTX6OZRM.1e7619 | basis_corrected_from_formula | CuO | -161.71 | -80.855 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -161.71 divided by 2 = -80.86, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-ALFTX6OZRM.279a7f | basis_corrected_from_formula | Cu2O | -173.18 | -57.726667 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -173.18 divided by 3 = -57.73, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-ALFTX6OZRM.b67909 | basis_corrected_from_formula | CuO | -157.07 | -78.535 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -157.07 divided by 2 = -78.53, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-C7MXYNKNHW | basis_corrected_from_formula | CuO | -156.06 | -78.03 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -156.06 divided by 2 = -78.03, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-GMNQNEO2HB | basis_corrected_from_formula | CuO | -155.48 | -77.74 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -155.48 divided by 2 = -77.74, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-I5UR2MQHUO | basis_corrected_from_formula | CuO | -157.07 | -78.535 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -157.07 divided by 2 = -78.53, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-J56QLHWYW7 | basis_corrected_from_formula | CuO | -161.08 | -80.54 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -161.08 divided by 2 = -80.54, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-LAWLJGIQGF | basis_corrected_from_formula | CuO | -154.03 | -77.015 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -154.03 divided by 2 = -77.02, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-LGOKEWXJHR.56dd6b | basis_corrected_from_formula | Cu2O | -164.85 | -54.95 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -164.85 divided by 3 = -54.95, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-LGOKEWXJHR.e36160 | basis_corrected_from_formula | CuO | -152.3 | -76.15 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -152.3 divided by 2 = -76.15, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-QQXJ6OCZ6G | basis_corrected_from_formula | CuO | -155.77 | -77.885 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -155.77 divided by 2 = -77.89, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-QZDH5SGEEG | basis_corrected_from_formula | CuO | -155.19 | -77.595 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -155.19 divided by 2 = -77.59, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-SNTTKLS5GR.c8b64e | basis_corrected_from_formula | Cu2O | -170.26 | -56.753333 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -170.26 divided by 3 = -56.75, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-SNTTKLS5GR.ce4045 | basis_corrected_from_formula | CuO | -155.19 | -77.595 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -155.19 divided by 2 = -77.59, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-T4WZFE2TJJ.006290 | basis_corrected_from_formula | CuO | -155.48 | -77.74 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -155.48 divided by 2 = -77.74, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-T4WZFE2TJJ.eef88f | basis_corrected_from_formula | Cu2O | -170.29 | -56.763333 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -170.29 divided by 3 = -56.76, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-UDWXTWFN6Y.049c73 | basis_corrected_from_formula | CuO | -154.03 | -77.015 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -154.03 divided by 2 = -77.02, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-UDWXTWFN6Y.223526 | basis_corrected_from_formula | Cu2O | -172.48 | -57.493333 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -172.48 divided by 3 = -57.49, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-UEENQAKLM2.5a9513 | basis_corrected_from_formula | Cu2O | -179.91 | -59.97 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -179.91 divided by 3 = -59.97, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-UQ5FDHCSKH | basis_corrected_from_formula | CuO | -161.71 | -80.855 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -161.71 divided by 2 = -80.86, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-XCCWO6H7LI.d9fe69 | basis_corrected_from_formula | Cu2O | -170.71 | -56.903333 | printed unit 'kJ/mol' has no per-atom marker; Cu2O has 3 atoms per formula unit; -170.71 divided by 3 = -56.90, within 15 of DFT (MP -62.2, OQMD -66.0) |
| ORC-XCCWO6H7LI.fa10e4 | basis_corrected_from_formula | CuO | -156.06 | -78.03 | printed unit 'kJ/mol' has no per-atom marker; CuO has 2 atoms per formula unit; -156.06 divided by 2 = -78.03, within 15 of DFT (MP -91.0, OQMD -80.2) |
| ORC-2BKKRXR33O | basis_corrected_from_formula | Li2O2 | -632.62 | -158.155 | printed unit 'kJ/mol' has no per-atom marker; Li2O2 has 4 atoms per formula unit; -632.62 divided by 4 = -158.16, within 15 of DFT (MP -159.2, OQMD -156.4) |
| ORC-6MGAPSXOS4 | basis_corrected_from_formula | Li2O | -597.0 | -199.0 | printed unit 'kJ/mol' has no per-atom marker; Li2O has 3 atoms per formula unit; -597 divided by 3 = -199.00, within 15 of DFT (MP -198.9, OQMD -191.0) |
| ORC-AKI6NGQPUL | basis_corrected_from_formula | Li2O | -598.73 | -199.576667 | printed unit 'kJ/mol' has no per-atom marker; Li2O has 3 atoms per formula unit; -598.73 divided by 3 = -199.58, within 15 of DFT (MP -198.9, OQMD -191.0) |
| ORC-AZT4WLCRAM | basis_corrected_from_formula | Li2O | -597.902 | -199.300667 | printed unit 'kJ/mol' has no per-atom marker; Li2O has 3 atoms per formula unit; -597.902 divided by 3 = -199.30, within 15 of DFT (MP -198.9, OQMD -191.0) |
| ORC-C5DY6KUUTC | basis_corrected_from_formula | Li2O2 | -644.28 | -161.07 | printed unit 'kJ/mol' has no per-atom marker; Li2O2 has 4 atoms per formula unit; -644.28 divided by 4 = -161.07, within 15 of DFT (MP -159.2, OQMD -156.4) |
| ORC-CBPWWARGVT | basis_corrected_from_formula | Li2O2 | -605.9 | -151.475 | printed unit 'kJ/mol' has no per-atom marker; Li2O2 has 4 atoms per formula unit; -605.9 divided by 4 = -151.47, within 15 of DFT (MP -159.2, OQMD -156.4) |
| ORC-CLLKMPH32B | basis_corrected_from_formula | Li2O | -597.48 | -199.16 | printed unit 'kJ/mol' has no per-atom marker; Li2O has 3 atoms per formula unit; -597.48 divided by 3 = -199.16, within 15 of DFT (MP -198.9, OQMD -191.0) |
| ORC-OCTG4OQW4X | basis_corrected_from_formula | Li2O2 | -632.62 | -158.155 | printed unit 'kJ/mol' has no per-atom marker; Li2O2 has 4 atoms per formula unit; -632.62 divided by 4 = -158.16, within 15 of DFT (MP -159.2, OQMD -156.4) |
| ORC-ZL6CQL3CB7 | basis_corrected_from_formula | Li2O | -596.5 | -198.833333 | printed unit 'kJ/mol' has no per-atom marker; Li2O has 3 atoms per formula unit; -596.5 divided by 3 = -198.83, within 15 of DFT (MP -198.9, OQMD -191.0) |
| ORC-7BHMNQTERA.e9b4e0 | dft_outlier_unexplained | AlB12 | -7.13 | -7.13 | opposite sign would match DFT but a minus sign is printed |
| ORC-7SENU32VE5.a9c6bc | dft_outlier_unexplained | AlB12 | -15.45 | -15.45 | opposite sign would match DFT but a minus sign is printed |
| ORC-BZBVIVDFD3.641832 | dft_outlier_unexplained | AlB12 | -15.253 | -15.253 | opposite sign would match DFT but a minus sign is printed |
| ORC-OFWRUQIJOX.29484e | dft_outlier_unexplained | AlB12 | -27.8 | -27.8 | opposite sign would match DFT but a minus sign is printed |
| ORC-VX6XF7LNLH.63d8b3 | dft_outlier_unexplained | AlB12 | -20.469 | -20.469 | opposite sign would match DFT but a minus sign is printed |
| ORC-PTCEOWMDSK.a5ef8d | dft_outlier_unexplained | Al11Cr2 | -15.32 | -15.32 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-R2GR6QLLKK.6b1758 | dft_outlier_unexplained | Al9Cr4 | -15.9 | -15.9 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-R2GR6QLLKK.6e2f3e | dft_outlier_unexplained | Al9Cr4 | -15.9 | -15.9 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-RL4XI5ZJPE.0dfd61 | dft_outlier_unexplained | Al11Cr2 | -15.06 | -15.06 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-WL7W6TITLB.6f9a16 | dft_outlier_unexplained | Al7Cr | -13.389 | -13.389 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-WL7W6TITLB.ba7092 | dft_outlier_unexplained | Al7Cr | -13.389 | -13.389 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-ZBKFVMQUIR.2ebec0 | dft_outlier_unexplained | Al11Cr2 | -15.062 | -15.062 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-ZBKFVMQUIR.9e4ee3 | dft_outlier_unexplained | Al11Cr2 | -15.062 | -15.062 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-IDJQ65H2VW.0cf5b6 | dft_outlier_unexplained | Al9Cr4 (h) | -12.903 | -12.903 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-SNXMEQBNRR.2f1eaf | dft_outlier_unexplained | Al11Cr2 | -15.322 | -15.322 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-CBFYDBTBRQ.96a41e | dft_outlier_unexplained | Mo5Al3-D8m | -22.0 | -22.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-KRFTD44W63.334d50 | dft_outlier_unexplained | Mo5Al3–D8m | -23.0 | -23.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-YE3UC7GJLU.3052ae | dft_outlier_unexplained | Mo5Al3–D8m | -22.0 | -22.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-EAIHRLMSOO.8f51c6 | dft_outlier_unexplained | AlTe | -87.6 | -87.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-DMIDUOBAKE | dft_outlier_unexplained | Al45V7 | 3.4272 | 3.4272 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-IBVD2A4HP4 | dft_outlier_unexplained | Al3V | 1.194 | 1.194 | no deterministic rule applies (DFT MP -27.9, OQMD -27.2) |
| ORC-6TKVKGZUN7.67693c | dft_outlier_unexplained | GeP | 1.44 | 1.44 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-GPEQGVYTET.cad93e | dft_outlier_unexplained | GeP | -11.442 | -11.442 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XUKMNJEPBE.b70504 | dft_outlier_unexplained | GeP | -11.44 | -11.44 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-N2BPBLFSN3 | dft_outlier_unexplained | Mg2B | -0.01423 | -0.01423 | no deterministic rule applies (DFT OQMD 24.1) |
| ORC-2QS3QXVB7F | dft_outlier_unexplained | Re2Si | -19.367 | -19.367 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-FLO5GRSVGD | dft_outlier_unexplained | Re2Si | -22.7 | -22.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-LUJ7XZ7YH3 | dft_outlier_unexplained | Re2Si | -22.0 | -22.0 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-QRHLTLQTBM | dft_outlier_unexplained | Re2Si | -19.7 | -19.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-TGOMFDVI6F | dft_outlier_unexplained | Re2Si | -20.0 | -20.0 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-VN47E3AARD.9cef4e | dft_outlier_unexplained | Re2Si | -12.7 | -12.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-VN47E3AARD.f5a708 | dft_outlier_unexplained | Re2Si | -12.7 | -12.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-S3AYA55WXC.5775a5 | dft_outlier_unexplained | Ti3Be(D03) | 3.6 | 3.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-S3AYA55WXC.841996 | dft_outlier_unexplained | Ti3Be(D03) | 3.6 | 3.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-EKJ27B36M7.e79e21 | dft_outlier_unexplained | ErBi2 | 15.2241 | 15.2241 | no deterministic rule applies (DFT OQMD -46.4) |
| ORC-EKJ27B36M7.ea7c62 | dft_outlier_unexplained | ErBi2 (MoS2-type) | 15.2241 | 15.2241 | no deterministic rule applies (DFT OQMD -46.4) |
| ORC-23O2KQG2NE | dft_outlier_unexplained | ErTe | -179.45 | -179.45 | no deterministic rule applies (DFT MP -136.7, OQMD -121.0) |
| ORC-FOOUUWPGJS | dft_outlier_unexplained | Bi2Se3 | 28.0 | 28.0 | no deterministic rule applies (DFT MP -64.6, OQMD -37.4) |
| ORC-JCVUNKRB5B | dft_outlier_unexplained | Bi2Se3 | -11.63 | -11.63 | no deterministic rule applies (DFT MP -64.6, OQMD -37.4) |
| ORC-UDK76LZB4Z.380313 | dft_outlier_unexplained | Bi4Te3, | 11.717 | 11.717 | no deterministic rule applies (DFT MP -34.1, OQMD -16.5) |
| ORC-I7WQ7E7CP7.8490a4 | dft_outlier_unexplained | YC | -57.0 | -57.0 | no deterministic rule applies (DFT MP 4.3, OQMD -23.9) |
| ORC-7MRHG7N6JM | dft_outlier_unexplained | ZrC3 | -53.0 | -53.0 | no deterministic rule applies (DFT OQMD 75.5) |
| ORC-PVGKDA2GYI | dft_outlier_unexplained | ZrC3 | -25.0 | -25.0 | no deterministic rule applies (DFT OQMD 75.5) |
| ORC-J4C54RBMBL.c06885 | dft_outlier_unexplained | Sr2Mg-C14 | 36.4176 | 36.4176 | no deterministic rule applies (DFT MP -3.4, OQMD -3.4) |
| ORC-OOZ4JZME4Z.5bf5d2 | dft_outlier_unexplained | Ca2Mg-C14 | 26.8549 | 26.8549 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-2RQQARKD4D.a020f1 | dft_outlier_unexplained | CaO(liq-am) | -557.3 | -557.3 | no deterministic rule applies (DFT MP -319.0, OQMD -308.3) |
| ORC-BWUGY4RCBI.19f6e9 | dft_outlier_unexplained | CaO(liq-am) | -565.6 | -565.6 | no deterministic rule applies (DFT MP -319.0, OQMD -308.3) |
| ORC-S7YOHYNZRJ.30327b | dft_outlier_unexplained | CaO(liq-am) | -600.9 | -600.9 | no deterministic rule applies (DFT MP -319.0, OQMD -308.3) |
| ORC-SAKKEEI5SE.2d0105 | dft_outlier_unexplained | CaO(liq-am) | -555.6 | -555.6 | no deterministic rule applies (DFT MP -319.0, OQMD -308.3) |
| ORC-3HYDEZEJHJ.a45823 | dft_outlier_unexplained | CaSi | -210.41 | -210.41 | no deterministic rule applies (DFT MP -48.5, OQMD -53.1) |
| ORC-3HYDEZEJHJ.ec7553 | dft_outlier_unexplained | CaSi2 | -200.34 | -200.34 | no deterministic rule applies (DFT MP -32.3, OQMD -37.6) |
| ORC-4M4CL2ZEFR.01d466 | dft_outlier_unexplained | CaSi | -151.0 | -151.0 | no deterministic rule applies (DFT MP -48.5, OQMD -53.1) |
| ORC-4M4CL2ZEFR.f6076c | dft_outlier_unexplained | Ca2Si | -209.0 | -209.0 | no deterministic rule applies (DFT MP -41.9, OQMD -45.5) |
| ORC-4M4CL2ZEFR.f95b49 | dft_outlier_unexplained | CaSi2 | -151.0 | -151.0 | no deterministic rule applies (DFT MP -32.3, OQMD -37.6) |
| ORC-5UBITMWKOB.50a5a9 | dft_outlier_unexplained | CaSi2 | -191.23 | -191.23 | no deterministic rule applies (DFT MP -32.3, OQMD -37.6) |
| ORC-5UBITMWKOB.6652b8 | dft_outlier_unexplained | Ca2Si | -254.35 | -254.35 | no deterministic rule applies (DFT MP -41.9, OQMD -45.5) |
| ORC-5UBITMWKOB.771bfa | dft_outlier_unexplained | CaSi | -180.16 | -180.16 | no deterministic rule applies (DFT MP -48.5, OQMD -53.1) |
| ORC-DSIDS2MAX2.9b2cda | dft_outlier_unexplained | Ca2Si | -209.0 | -209.0 | no deterministic rule applies (DFT MP -41.9, OQMD -45.5) |
| ORC-DSIDS2MAX2.b484d4 | dft_outlier_unexplained | CaSi | -120.64 | -120.64 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-DSIDS2MAX2.da25fb | dft_outlier_unexplained | CaSi2 | -150.4 | -150.4 | no deterministic rule applies (DFT MP -32.3, OQMD -37.6) |
| ORC-MVPCUY2QXZ.24c48a | dft_outlier_unexplained | CaSi | -120.38 | -120.38 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-MVPCUY2QXZ.509ca2 | dft_outlier_unexplained | CaSi2 | -150.4 | -150.4 | no deterministic rule applies (DFT MP -32.3, OQMD -37.6) |
| ORC-TMGYG5CRHE | dft_outlier_unexplained | CaSi2 | -153.42 | -153.42 | no deterministic rule applies (DFT MP -32.3, OQMD -37.6) |
| ORC-2BBVVIXWTO | dft_outlier_unexplained | Co17Y2 | 7.6 | 7.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-346I5F5EQH | dft_outlier_unexplained | CoY3 | 15.8 | 15.8 | no deterministic rule applies (DFT MP -13.9, OQMD -14.7) |
| ORC-57NY3YXVJ7.5ff086 | dft_outlier_unexplained | CrGe | -10.25 | -10.25 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-6HTTW5327W.8f41bd | dft_outlier_unexplained | αCr5Ge3 | -12.3 | -12.3 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-AEGTNE4V3R.c00b5c | dft_outlier_unexplained | CrGe | -13.85 | -13.85 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-DDPY5AV4XW.66798b | dft_outlier_unexplained | Cr11Ge8 | -28.6 | -28.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-DDPY5AV4XW.9b1320 | dft_outlier_unexplained | Cr11Ge8 | -30.7 | -30.7 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-P3R7LHZLX4.17f577 | dft_outlier_unexplained | αCr5Ge3 | -16.3 | -16.3 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-RRUITAEIYM.4a9907 | dft_outlier_unexplained | Cr11Ge8 | -10.92 | -10.92 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-VYDTBVQGR6.7e076a | dft_outlier_unexplained | αCr5Ge3 | -15.7 | -15.7 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-WMW5QZIUMC.fe8401 | dft_outlier_unexplained | Cr11Ge8 | -16.19 | -16.19 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-HRJTWRGIKE.c68ad1 | dft_outlier_unexplained | Cu8Hf3 | -192.72 | -192.72 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-PYVAEHKD5K | dft_outlier_unexplained | CuO | -138.16 | -138.16 | no deterministic rule applies (DFT MP -91.0, OQMD -80.2) |
| ORC-UEENQAKLM2.d6b8e9 | dft_outlier_unexplained | CuO | -138.16 | -138.16 | no deterministic rule applies (DFT MP -91.0, OQMD -80.2) |
| ORC-BUGOBEY2SA.8253a8 | dft_outlier_unexplained | L12-CuPt3 | -10.0 | -10.0 | no deterministic rule applies (DFT MP 232.8, OQMD -11.3) |
| ORC-DGXLGCDH4A.307a73 | dft_outlier_unexplained | L12-CuPt3 | -13.0 | -13.0 | no deterministic rule applies (DFT MP 232.8, OQMD -11.3) |
| ORC-X346LL47CP.06d331 | dft_outlier_unexplained | L12-CuPt3 | -8.0 | -8.0 | no deterministic rule applies (DFT MP 232.8, OQMD -11.3) |
| ORC-XOPIEWRTSO.ee7e04 | dft_outlier_unexplained | L12-CuPt3 | -14.0 | -14.0 | no deterministic rule applies (DFT MP 232.8, OQMD -11.3) |
| ORC-X2KCSO7KLU.1b7401 | dft_outlier_unexplained | ζ(Cu10Sb3) | -4.936 | -4.936 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-XLTIVDRTXK.120f23 | dft_outlier_unexplained | ε(Cu3Sb) | -4.718 | -4.718 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-FGKIBVFKMX.551bc0 | dft_outlier_unexplained | Fe2Gd | -11.6 | -11.6 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-GFLCDMFT2S.df124f | dft_outlier_unexplained | Fe23Gd6 | -6.44 | -6.44 | no deterministic rule applies (DFT MP 119.9, OQMD -1.3) |
| ORC-QHUFQDX7VW.d21cdf | dft_outlier_unexplained | Fe23Gd6 | -4.74 | -4.74 | no deterministic rule applies (DFT MP 119.9, OQMD -1.3) |
| ORC-XVCLD777MT | dft_outlier_unexplained | Fe2Gd | -11.6 | -11.6 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-I5FTFLBBH2 | dft_outlier_unexplained | Fe2Tb | -9.005 | -9.005 | opposite sign would match DFT but a minus sign is printed |
| ORC-AVMJJOFCI6.aa805e | dft_outlier_unexplained | FeTi | 16.375 | 16.375 | no deterministic rule applies (DFT MP -40.6, OQMD -43.5) |
| ORC-RQ4BFCC5WQ.beef01 | dft_outlier_unexplained | FeTi | 12.055 | 12.055 | no deterministic rule applies (DFT MP -40.6, OQMD -43.5) |
| ORC-Y5NZC5TFL6.2d4fb1 | dft_outlier_unexplained | Fe2Ti | 7.179 | 7.179 | no deterministic rule applies (DFT MP -27.3, OQMD -29.6) |
| ORC-HH35CEJQF6.c3a472 | dft_outlier_unexplained | FeY | -12.5 | -12.5 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-IIIWFVRG2N.a0809b | dft_outlier_unexplained | FeY | -9.4 | -9.4 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-DFGUHZKH5X.d5d00e | dft_outlier_unexplained | Mn2Gd | -6.4 | -6.4 | opposite sign would match DFT but a minus sign is printed |
| ORC-DFGUHZKH5X.e25286 | dft_outlier_unexplained | Mn23Gd6 | -6.4 | -6.4 | no deterministic rule applies (DFT MP 89.4, OQMD 12.2) |
| ORC-PNIDQR52CL.cf24ce | dft_outlier_unexplained | Mn23Sm6 | -3.17 | -3.17 | no deterministic rule applies (DFT MP 10.8, OQMD 18.9) |
| ORC-67FUWETMMC.0d66d3 | dft_outlier_unexplained | Ge1P1 | -13.6 | -13.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-JNA7PDKMQ2.8cc84f | dft_outlier_unexplained | Ge1P1 | -13.82 | -13.82 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-KZ6SOQYB5E | dft_outlier_unexplained | Ge1P1 | -12.56 | -12.56 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-THZKCHGMJH.5d4e3b | dft_outlier_unexplained | Ge1P1 | -10.5 | -10.5 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-4NIT2EUNUZ | dft_outlier_unexplained | Mg2Si | -63.3 | -63.3 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-4P7GS3EMYE | dft_outlier_unexplained | Mg2Si | -64.11 | -64.11 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-7UMSNJ5ULE | dft_outlier_unexplained | Mg2Si | -65.22 | -65.22 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-BQMOVUXMWI | dft_outlier_unexplained | Mg2Si | -80.01 | -80.01 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-IT4ZCWCHUS | dft_outlier_unexplained | Mg2Si | -68.97 | -68.97 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-N7FIHVHMXU | dft_outlier_unexplained | Mg2Si | -79.41 | -79.41 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-RRLRFVBSPR | dft_outlier_unexplained | Mg2Si | -78.9 | -78.9 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-WGV2LZGFYW | dft_outlier_unexplained | Mg2Si | -79.11 | -79.11 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XE6ZN6IYQS | dft_outlier_unexplained | Mg2Si | -63.03 | -63.03 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XT23ZMENP2 | dft_outlier_unexplained | Mg2Si | -66.48 | -66.48 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-YAOI6N6R5H | dft_outlier_unexplained | Mg2Si | -89.1 | -89.1 | no deterministic rule applies (DFT MP -12.4, OQMD -15.6) |
| ORC-6FVHAKNFGR | dft_outlier_unexplained | MoRe | -11.1 | -11.1 | opposite sign would match DFT but a minus sign is printed |
| ORC-EHCGQKMWEM | dft_outlier_unexplained | MoRe2 | -9.7 | -9.7 | opposite sign would match DFT but a minus sign is printed |
| ORC-RFPJQTOPP2 | dft_outlier_unexplained | MoRe5 | -7.4 | -7.4 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-RNK6KNR4U2 | dft_outlier_unexplained | Mo2Re | -10.4 | -10.4 | no deterministic rule applies (DFT OQMD 41.3) |
| ORC-ETM4B5HQ7B.8cb200 | dft_outlier_unexplained | TaN3 | 22.0 | 22.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-NXZXLEBKFD.3cb80c | dft_outlier_unexplained | TaN3 | 22.0 | 22.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-CRSOXW3NYP | dft_outlier_unexplained | NiSi3–L12 | -8.61 | -8.61 | opposite sign would match DFT but a minus sign is printed |
| ORC-BXDGYNA4FE | dft_outlier_unexplained | Tb3Ni2 | -32.5 | -32.5 | no deterministic rule applies (DFT MP -33.4, OQMD 3.4) |
| ORC-IXS6VH7K56 | dft_outlier_unexplained | Tb3Ni2 | -45.3 | -45.3 | no deterministic rule applies (DFT MP -33.4, OQMD 3.4) |
| ORC-T5FGP4HAKO | dft_outlier_unexplained | Tb3Ni | -20.2 | -20.2 | no deterministic rule applies (DFT MP -22.9, OQMD 24.4) |
| ORC-X6JDSME53M | dft_outlier_unexplained | Tb3Ni | -24.5 | -24.5 | no deterministic rule applies (DFT MP -22.9, OQMD 24.4) |
| ORC-XGJTJCDVFW | dft_outlier_unexplained | Tb3Ni | -29.3 | -29.3 | no deterministic rule applies (DFT MP -22.9, OQMD 24.4) |
| ORC-YJUTP2PTKK | dft_outlier_unexplained | Tb3Ni2 | -39.1 | -39.1 | no deterministic rule applies (DFT MP -33.4, OQMD 3.4) |
| ORC-3UQSOYYDZ5.ba5118 | dft_outlier_unexplained | PuO1,61 | -433.6 | -433.6 | no deterministic rule applies (DFT MP -270.3, OQMD -276.4) |
| ORC-BQ7EBIS6BA.4474ae | dft_outlier_unexplained | PuO1,52 | -422.5 | -422.5 | no deterministic rule applies (DFT MP -270.3, OQMD -276.4) |
| ORC-EBMTXVKTB3.dc77b1 | dft_outlier_unexplained | PuO1,52 | -419.0 | -419.0 | no deterministic rule applies (DFT MP -270.3, OQMD -276.4) |
| ORC-IW4K2IGBVB.07daca | dft_outlier_unexplained | PuO1,61 | -447.5 | -447.5 | no deterministic rule applies (DFT MP -270.3, OQMD -276.4) |
| ORC-O2MKQDICEJ.012a44 | dft_outlier_unexplained | PuO1,61 | -442.25 | -442.25 | no deterministic rule applies (DFT MP -270.3, OQMD -276.4) |
| ORC-QX5Z74ABJL.0e15ad | dft_outlier_unexplained | PuO1,61 | -437.75 | -437.75 | no deterministic rule applies (DFT MP -270.3, OQMD -276.4) |
| ORC-5H3ZBHLINP | dft_outlier_unexplained | Zr2O | -286.0 | -286.0 | no deterministic rule applies (DFT MP -192.1, OQMD -186.6) |
| ORC-5NHXC6TIGO | dft_outlier_unexplained | ZrO3 | -644.0 | -644.0 | no deterministic rule applies (DFT OQMD -240.0) |
| ORC-7W5PN7OFFN | dft_outlier_unexplained | Zr3O | -214.0 | -214.0 | no deterministic rule applies (DFT MP -149.1, OQMD -142.7) |
| ORC-B66ZOF6RPG | dft_outlier_unexplained | ZrO0.5 | -286.0 | -286.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-BQTDFV2XVC | dft_outlier_unexplained | ZrO3 | -411.0 | -411.0 | no deterministic rule applies (DFT OQMD -240.0) |
| ORC-UT4GG4A3ZU | dft_outlier_unexplained | ZrO2 | -573.0 | -573.0 | no deterministic rule applies (DFT MP -368.0, OQMD -350.5) |
| ORC-B5HZQXACR2 | dft_outlier_unexplained | Re2Si | -19.7 | -19.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-BEDS4AL56C | dft_outlier_unexplained | Re2Si | -20.0 | -20.0 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-HSMQUVTRQ5 | dft_outlier_unexplained | Re2Si | -22.7 | -22.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-RPBIKNDS4Q | dft_outlier_unexplained | Re2Si | -27.0 | -27.0 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-W7LPYQQ2OB | dft_outlier_unexplained | αSbTm | -157.0 | -157.0 | no deterministic rule applies (DFT MP -111.5, OQMD -103.1) |
| ORC-6OOPELOSIS.274e9e | dft_outlier_unexplained | ε-Sb3Zn4 | -5.28 | -5.28 | opposite sign would match DFT but a minus sign is printed |
| ORC-7A2QTKMYRH.003111 | dft_outlier_unexplained | ε-Sb3Zn4 | -9.378 | -9.378 | opposite sign would match DFT but a minus sign is printed |
| ORC-7VPUF5XRGG.2a862c | dft_outlier_unexplained | δ-Sb3Zn4 | -12.379 | -12.379 | opposite sign would match DFT but a minus sign is printed |
| ORC-E76ESIXAL7.7546d1 | dft_outlier_unexplained | ε-Sb3Zn4 | -9.378 | -9.378 | opposite sign would match DFT but a minus sign is printed |
| ORC-GEOHQLQG2H.60a4e1 | dft_outlier_unexplained | ε-Sb3Zn4 | -10.7 | -10.7 | opposite sign would match DFT but a minus sign is printed |
| ORC-I5P7YJ6ZTR.05380b | dft_outlier_unexplained | δ′-Sb3Zn4 | -16.028 | -16.028 | opposite sign would match DFT but a minus sign is printed |
| ORC-LJ7NTT3MZM.0521f9 | dft_outlier_unexplained | δ′-Sb3Zn4 | -20.551 | -20.551 | opposite sign would match DFT but a minus sign is printed |
| ORC-NZUTUZNKYH.3f1124 | dft_outlier_unexplained | δ-Sb3Zn4 | -4.35 | -4.35 | per-formula reading would match DFT but the printed unit is explicitly per atom; opposite sign would match DFT but a minus sign is printed |
| ORC-R4WK4SK6PB.425011 | dft_outlier_unexplained | δ-Sb3Zn4 | -17.878 | -17.878 | opposite sign would match DFT but a minus sign is printed |
| ORC-THQ7S4MRBN.008989 | dft_outlier_unexplained | δ-Sb3Zn4 | -10.707 | -10.707 | opposite sign would match DFT but a minus sign is printed |
| ORC-5UUHBBHP6L | dft_outlier_unexplained | Sc5Si3 | 4.236 | 4.236 | no deterministic rule applies (DFT MP -71.5, OQMD -74.2) |
| ORC-SB22WLDX3O.343415 | dft_outlier_unexplained | Sc5Si3 | -161.1 | -161.1 | no deterministic rule applies (DFT MP -71.5, OQMD -74.2) |
| ORC-2KKFN2CQ4A.44744c | dft_outlier_unexplained | Si0.75Ta0.25 | -39.0 | -39.0 | no deterministic rule applies (DFT OQMD 4.5) |
| ORC-JO4R7F2VDG.9363b1 | dft_outlier_unexplained | Si3V | 54.3 | 54.3 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XH7E5G77IP | dft_outlier_unexplained | Sm₂Ti₃ | 12.66852411 | 12.66852411 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-YTPULMUAG2.147391 | dft_outlier_unexplained | Sn5Ti6-L | -115.0 | -115.0 | no deterministic rule applies (DFT MP -35.9, OQMD -43.2) |
| ORC-YTPULMUAG2.38164d | dft_outlier_unexplained | SnTi2 | -92.0 | -92.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-YTPULMUAG2.3a933d | dft_outlier_unexplained | Sn3Ti5 | -94.0 | -94.0 | no deterministic rule applies (DFT MP -33.6, OQMD -40.3) |
| ORC-HBOMRR3WMD | dft_outlier_unexplained | USn | -88.45 | -88.45 | no deterministic rule applies (DFT MP 4.1, OQMD -2.2) |
| ORC-VEJ7ZKU7ER.7c82a9 | unsigned_in_print | Al3Zr2 | 55.0 | 55.0 | printed without a minus sign (55.0) and no negated heading in the record; -value within 15 of DFT (MP -50.3, OQMD -50.3); value kept as printed, excluded from the default parity set |
| ORC-XCKFUPBCDP.5dea3d | unsigned_in_print | Al2Zr3 | 41.929 | 41.929 | printed without a minus sign (41.929) and no negated heading in the record; -value within 15 of DFT (MP -38.8, OQMD -38.8); value kept as printed, excluded from the default parity set |
| ORC-KWPV2VO5Q6 | unsigned_in_print | Ti3Al | 30.872733 | 30.872733 | printed without a minus sign (30872.733) and no negated heading in the record; -value within 15 of DFT (MP -26.9, OQMD -31.7); value kept as printed, excluded from the default parity set |
| ORC-IYGKUG52RR.7ea5a7 | unsigned_in_print | TiBe(B32) | 28.3 | 28.3 | printed without a minus sign (28.3) and no negated heading in the record; -value within 15 of DFT (MP -13.5, OQMD -15.8); value kept as printed, excluded from the default parity set |
| ORC-IYGKUG52RR.b27a73 | unsigned_in_print | TiBe(B32) | 28.3 | 28.3 | printed without a minus sign (28.3) and no negated heading in the record; -value within 15 of DFT (MP -13.5, OQMD -15.8); value kept as printed, excluded from the default parity set |
| ORC-JGZ6JOX4UO.34eb12 | unsigned_in_print | ErBi2 | 39.6679 | 39.6679 | printed without a minus sign (39.6679) and no negated heading in the record; -value within 15 of DFT (OQMD -46.4); value kept as printed, excluded from the default parity set |
| ORC-JGZ6JOX4UO.9c10e5 | unsigned_in_print | ErBi2 (CdI2-type) | 39.6679 | 39.6679 | printed without a minus sign (39.6679) and no negated heading in the record; -value within 15 of DFT (OQMD -46.4); value kept as printed, excluded from the default parity set |
| ORC-AP6PJYWU2A.68996d | unsigned_in_print | BiK3 | 45.1 | 45.1 | printed without a minus sign (45.1) and no negated heading in the record; -value within 15 of DFT (MP -35.2, OQMD -37.5); value kept as printed, excluded from the default parity set |
| ORC-RBLTNNPVR3.7c362e | unsigned_in_print | Y2C | 31.8 | 31.8 | printed without a minus sign (31.8) and no negated heading in the record; -value within 15 of DFT (MP -28.2, OQMD -28.7); value kept as printed, excluded from the default parity set |
| ORC-3US35N57LJ.209a6e | unsigned_in_print | CoGe | 21.9 | 21.9 | printed without a minus sign (21.9) and no negated heading in the record; -value within 15 of DFT (MP -21.0, OQMD -22.3); value kept as printed, excluded from the default parity set |
| ORC-3US35N57LJ.42fca7 | unsigned_in_print | CoGe | 21.4 | 21.4 | printed without a minus sign (21.4) and no negated heading in the record; -value within 15 of DFT (MP -21.0, OQMD -22.3); value kept as printed, excluded from the default parity set |
| ORC-3US35N57LJ.4a429f | unsigned_in_print | CoGe2 | 15.3 | 15.3 | printed without a minus sign (15.3) and no negated heading in the record; -value within 15 of DFT (MP -14.8, OQMD -15.2); value kept as printed, excluded from the default parity set |
| ORC-3US35N57LJ.6eedfa | unsigned_in_print | CoGe | 21.0 | 21.0 | printed without a minus sign (21.0) and no negated heading in the record; -value within 15 of DFT (MP -21.0, OQMD -22.3); value kept as printed, excluded from the default parity set |
| ORC-3US35N57LJ.708cee | unsigned_in_print | CoGe2 | 15.5 | 15.5 | printed without a minus sign (15.5) and no negated heading in the record; -value within 15 of DFT (MP -14.8, OQMD -15.2); value kept as printed, excluded from the default parity set |
| ORC-3US35N57LJ.a784df | unsigned_in_print | CoGe2 | 15.9 | 15.9 | printed without a minus sign (15.9) and no negated heading in the record; -value within 15 of DFT (MP -14.8, OQMD -15.2); value kept as printed, excluded from the default parity set |
| ORC-S46LFTJSEB | unsigned_in_print | Co2Y | 22.76 | 22.76 | printed without a minus sign (22.76) and no negated heading in the record; -value within 15 of DFT (MP -17.1, OQMD -18.2); value kept as printed, excluded from the default parity set |
| ORC-E4DHBOCKS5 | unsigned_in_print | ε(Cr2N) | 41.8 | 41.8 | printed without a minus sign (41.8) and no negated heading in the record; -value within 15 of DFT (MP -48.8, OQMD -43.7); value kept as printed, excluded from the default parity set |
| ORC-Z7SKX53DNV | unsigned_in_print | Cu10Zr7 | 21.226 | 21.226 | printed without a minus sign (21226) and no negated heading in the record; -value within 15 of DFT (MP -15.3, OQMD -15.4); value kept as printed, excluded from the default parity set |
| ORC-3BTH25KMV7 | unsigned_in_print | Mn3O4 | 198.3971429 | 198.3971429 | printed without a minus sign (1388.78) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-IRJXYJDNH7 | unsigned_in_print | Mn3O4 | 201.2057143 | 201.2057143 | printed without a minus sign (1408.44) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-JOYPE76SKL | unsigned_in_print | Mn3O4 | 197.5342857 | 197.5342857 | printed without a minus sign (1382.74) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-NRMMC4OTJO | unsigned_in_print | Mn3O4 | 198.3642857 | 198.3642857 | printed without a minus sign (1388.55) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-O4LF5UQABA | unsigned_in_print | Mn3O4 | 206.35 | 206.35 | printed without a minus sign (1444.45) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-OF7YZ4OCHX | unsigned_in_print | Mn3O4 | 196.78 | 196.78 | printed without a minus sign (1377.46) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-OOK4XMA4V5 | unsigned_in_print | Mn3O4 | 197.9142857 | 197.9142857 | printed without a minus sign (1385.4) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-P3442DZZI6 | unsigned_in_print | Mn3O4 | 196.1814286 | 196.1814286 | printed without a minus sign (1373.27) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-QOMRTGICZ5 | unsigned_in_print | Mn3O4 | 198.1557143 | 198.1557143 | printed without a minus sign (1387.09) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-QZ2I3A6NYV | unsigned_in_print | Mn3O4 | 198.2157143 | 198.2157143 | printed without a minus sign (1387.51) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-S2J5QCW5R6 | unsigned_in_print | Mn3O4 | 198.2 | 198.2 | printed without a minus sign (1387.4) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-SJQNK6QQKR | unsigned_in_print | Mn3O4 | 198.0142857 | 198.0142857 | printed without a minus sign (1386.1) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |
| ORC-ZPFJ3SIJDS | unsigned_in_print | Mn3O4 | 201.2657143 | 201.2657143 | printed without a minus sign (1408.86) and no negated heading in the record; -value within 15 of DFT (MP -197.8, OQMD -200.1); value kept as printed, excluded from the default parity set |

## 5. Energy units

Formation enthalpies / Gibbs energies of formation, mixing enthalpies, Gibbs energies of mixing and partial molar enthalpies are given in kJ (`value`, `unit`) with the value before conversion in `value_stored`/`unit_stored` and the printed value/unit beside them. `unit_basis` records how the per-atom basis was established (printed_unit, column_header, caption, reviewer, state_completion_*, magnitude_heuristic, assumed_per_mole_of_atoms, unstated).

* mixing / partial values converted to kJ/mol-atom (explicit per-atom basis): 1132
* mixing / partial values converted to kJ/mol (basis unstated): 2166
* of these, per-atom labels from a heuristic or assumption demoted to basis unstated: 9
* formation values whose per-atom basis comes only from the record builder's magnitude heuristic (kept, flagged `flags.basis_inferred_from_magnitude`): see `index.json` totals

## 5b. Reference-state phase names

The record builder wrote the reference phase of O, N, H and F as `1` (the first character of the SGTE SER name `1/2_MOLE_O2(G)` etc. on the TDB ELEMENT line) and of some metals as the Strukturbericht symbol (`A1`, `A2`, `A3`). These names are derived, not printed; they are completed to `1/2_MOLE_X2(G)` and `FCC_A1` / `BCC_A2` / `HCP_A3`, with the written name kept in `reference_state.<EL>.phase_before_quality_fix`: 1675 reference phases (1495 SER gas names, 180 Strukturbericht symbols).

## 6. ESPEI readiness: physical phase rule; certification

Physical phase rule (tools/phase_rule.py): a literature value is assigned to a phase only when the paper names that phase (printed phase label of the value; when no label is printed, a table caption that names the liquid) and the phase registry maps the label to a model phase; no default phase is assigned. A liquid assignment must be physically possible: not below the lowest liquid temperature of any calculated SGTE diagram of the system minus max(100 K, 10 %) (twice that for printed invariant and phase-composition records; no calculated diagram: not below 0.40 x the lowest element melting point). Formation enthalpies and entropies of a stoichiometric compound go to that compound's TDB endmember (ESPEI non-equilibrium dataset, `solver`); other properties of a compound are not used in ESPEI. A solution-phase assignment outside the phase's field in the calculated diagram of the target TDB is flagged (`outside_calculated_field`), not excluded. Temperatures: T <= 1 K is not a measured state; a printed phase equilibrium (invariant, phase composition, transition) below 0.25 x the lowest element melting point is a misreading. A value flagged `unsigned_in_print` / `magnitude_suspect` / `system_mismatch` / `source_disputed` is not ESPEI-ready.

Before this rule, the corpus ESPEI export assigned every thermochemical value without a mapped model phase to LIQUID (and added LIQUID to every mapped phase set), so compound formation enthalpies at compound compositions and at temperatures where no liquid can exist were written as liquid mixing data. The printed values and labels were always correct in these records (`property`, `phases`); only `flags.espei_ready` changes: a value that fails the rule has `espei_ready` false, `espei_ready_upstream` true and `espei_phase_rule` {result, reason, detail}. No value, label or phase is altered.

`espei_certified` = `espei_ready` AND `plausibility.result` = pass (pycalphad calculation from the linked TDB agrees within the recorded tolerance, 25 K / 0.05 mole fraction); `espei_certified_basis` = `pycalphad_invariant_agreement`. `calphad_check`: agrees / disagrees / not_available.

| count | n |
|---|---:|
| blocked_by_flag | 26 |
| blocked_by_flag_magnitude_suspect | 17 |
| blocked_by_flag_unsigned_in_print | 9 |
| espei_certified | 1928 |
| espei_ready | 12221 |
| espei_ready_calphad_disagrees | 323 |
| espei_ready_no_prediction | 9970 |
| phase_rule_fail_compound_property_not_fittable | 367 |
| phase_rule_fail_liquid_impossible_at_T | 8 |
| phase_rule_fail_phase_label_ambiguous | 77 |
| phase_rule_fail_phase_label_not_mapped | 790 |
| phase_rule_fail_phase_not_printed | 710 |
| phase_rule_fail_temperature_implausible | 6 |
| phase_rule_pass | 12221 |

Values whose `espei_ready` the phase rule turned false:

| id | system | property | T (K) | printed labels | reason | detail |
|---|---|---|---:|---|---|---|
| ORC-RBLTNNPVR3.7c362e | C-SI-Y | HM_FORM | 298.15 | Y2C | blocked_by_flag | unsigned_in_print |
| ORC-S46LFTJSEB | CO-Y | HM_FORM | 298.15 | Co2Y | blocked_by_flag | unsigned_in_print |
| ORC-7CR6KUYW66 | FE-TI | ACR_TI | 1650.0 | bcc | blocked_by_flag | magnitude_suspect |
| ORC-7WSFDPW275 | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-B4QS27QZBY.818957 | FE-TI | ACR_TI | 1650.0 | Bcc | blocked_by_flag | magnitude_suspect |
| ORC-DQ3GXD66WX | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-EKYGVHERRU | FE-TI | ACR_TI | 1600.0 | bcc | blocked_by_flag | magnitude_suspect |
| ORC-HSVROZ4SVW.b0d6d4 | FE-TI | ACR_TI | 1550.0 | Bcc | blocked_by_flag | magnitude_suspect |
| ORC-N47CRZXOCP.66a9d3 | FE-TI | ACR_TI | 1550.0 | Bcc | blocked_by_flag | magnitude_suspect |
| ORC-NNRZ2XZQMO.460f91 | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-NSB7NU6SWX | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-QND2SCLWKB | FE-TI | ACR_TI | 1550.0 | bcc | blocked_by_flag | magnitude_suspect |
| ORC-RRDGITWNOH.b8c8f8 | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-SOYYFWW4R4.0c9800 | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-TX5HIWNLDH | FE-TI | ACR_TI | 1550.0 | bcc | blocked_by_flag | magnitude_suspect |
| ORC-X3O6VV33H6 | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-XH3HOVMUTJ.a7c2f4 | FE-TI | ACR_TI | 1873.0 | L | blocked_by_flag | magnitude_suspect |
| ORC-XLAOWBKMFH.3758f0 | FE-TI | ACR_TI | 1600.0 | Bcc | blocked_by_flag | magnitude_suspect |
| ORC-NRMMC4OTJO | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-O4LF5UQABA | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-OF7YZ4OCHX | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-P3442DZZI6 | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-QOMRTGICZ5 | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-QZ2I3A6NYV | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-ZPFJ3SIJDS | MN-O | HM_FORM | 298.15 | Mn3O4 | blocked_by_flag | unsigned_in_print |
| ORC-T64EA4SVSN | O-ZR | HM_FORM | 298.15 | ZrO2 | blocked_by_flag | magnitude_suspect |
| ORC-XCFMJUUOJ7.a0179c | AL-CA | GM_FORM | 800.0 | Al4Ca | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-V7YJ5MPN3I | AL-NI | SM | 298.0 | Al3Ni | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IHDYFUIRSU | B-NB | SM | 298.15 | Nb3B4 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PC4VPHHPN2 | B-NB | SM | 298.15 | Nb3B2 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KEI2TY2L4J.c69d64 | BI-K | GM_FORM | 838.0 | Bi2K | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BOPH4LJCD6 | C-SI | SM | 298.0 | αSiC(Hex) | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-67R62WBVGI.f4efec | CA-PB | HM_MIX | 1020.0 | Ca2Pb(l) | compound_property_not_fittable | HM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JR73AQEICV.511c7b | CA-PB | HM_MIX | 1020.0 | CaPb3(l) | compound_property_not_fittable | HM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4T5HFCFJIC | CE-ZN | GM_MIX | 773.15 | CeZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7IY7WMYAU7 | CE-ZN | GM_MIX | 773.15 | CeZn5 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7NGCG5VXFB | CE-ZN | GM_MIX | 773.15 | CeZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BSC7LKZPK4 | CE-ZN | GM_MIX | 773.15 | Ce13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CU7XVBQ4U7 | CE-ZN | GM_MIX | 1173.15 | Ce3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DEWQ4KPVM3 | CE-ZN | GM_MIX | 1173.15 | Ce2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EKSC43ZMMO | CE-ZN | GM_MIX | 973.15 | Ce13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-G3TRTAFB47 | CE-ZN | GM_MIX | 773.15 | CeZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-G54IYE5ICU | CE-ZN | GM_MIX | 773.15 | Ce3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GM74XWMPQ7 | CE-ZN | GM_MIX | 1173.15 | CeZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-H7ZRAAMMEB | CE-ZN | GM_MIX | 773.15 | CeZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IKJIUSYEHO | CE-ZN | GM_MIX | 773.15 | Ce2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IWY6AENSQZ | CE-ZN | GM_MIX | 773.15 | CeZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KN7WUE6X2I | CE-ZN | GM_MIX | 973.15 | Ce3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LJJ4JGFPMB | CE-ZN | GM_MIX | 1173.15 | CeZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MCEDTP4U2B | CE-ZN | GM_MIX | 973.15 | CeZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MEI23J6GDL | CE-ZN | GM_MIX | 1173.15 | CeZn5 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MFTVHE3OCF | CE-ZN | GM_MIX | 1173.15 | Ce13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MMXDAHEPYE | CE-ZN | GM_MIX | 1173.15 | CeZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NMQOH7S6Z4 | CE-ZN | GM_MIX | 1173.15 | CeZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NOZQYF5A46 | CE-ZN | GM_MIX | 973.15 | Ce3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QALMUYRVLZ | CE-ZN | GM_MIX | 973.15 | Ce2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QJSEAQ5IRX | CE-ZN | GM_MIX | 973.15 | CeZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-S763I5XRQE | CE-ZN | GM_MIX | 973.15 | CeZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SI3RIE5BNR | CE-ZN | GM_MIX | 973.15 | CeZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-USKX4LDIIG | CE-ZN | GM_MIX | 973.15 | CeZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UYVVGXTHP7 | CE-ZN | GM_MIX | 1173.15 | Ce3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VSDOYLEF2H | CE-ZN | GM_MIX | 1173.15 | CeZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WBPEYMXB56 | CE-ZN | GM_MIX | 973.15 | CeZn5 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-YC57UPTDSC | CE-ZN | GM_MIX | 773.15 | Ce3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5L35TGCFAL.ec28c3 | CR-GE | SM | 298.0 | CrGe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JJU3CGVLU7.826061 | CR-GE | SM | 298.0 | Cr11Ge19 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IDEY4NU7GH.5fcb90 | CS-O | CPM | 298.15 | Cs4O | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IDEY4NU7GH.6d36ca | CS-O | SM | 298.15 | Cs4O | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NGZLBXOCTJ.51d7f5 | CS-O | CPM | 298.15 | Cs7O | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NGZLBXOCTJ.89404d | CS-O | SM | 298.15 | Cs7O | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SWEHTSC4LB.6455b7 | CS-O | SM | 298.15 | Cs7O2 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SWEHTSC4LB.f524bc | CS-O | CPM | 298.15 | Cs7O2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSATJTWL4X.de9739 | CS-O | SM | 298.15 | Cs3O | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSATJTWL4X.f55708 | CS-O | CPM | 298.15 | Cs3O | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2T3W5BF2L4.4e597c | ER-GE | GM_MIX | 950.0 | LT_ErGe2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3Z7R6C4RJD.fc409f | ER-GE | GM_MIX | 950.0 | Er11Ge10 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AIUQQK7SCB.65be9e | ER-GE | GM_MIX | 950.0 | MT_ErGe2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CAIUJ7QU3I.af9293 | ER-GE | GM_MIX | 950.0 | Er3Ge4 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DQF45FYYVS.ab0d4a | ER-GE | GM_MIX | 950.0 | LT_Er2Ge3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EH46YZZVT7.7340ac | ER-GE | GM_MIX | 950.0 | ErGe | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LPVBNOE2IG.61f1dc | ER-GE | GM_MIX | 950.0 | HT_Er2Ge3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-O4EBHRWJPH.2ba01d | ER-GE | GM_MIX | 950.0 | Er2Ge5 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SJMNJSI46L.3a1910 | ER-GE | GM_MIX | 950.0 | Er5Ge4 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VL7CG4ITOP.fc705a | ER-GE | GM_MIX | 950.0 | HT_ErGe2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3CGZJZTPCB.875a26 | FE-GD | SM | 298.15 | Fe2Gd | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7XTBZMJVLP | FE-GD | SM | 298.0 | Fe2Gd | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XV3BI7QYUX.1323e3 | FE-GD | CPM | 298.15 | Fe2Gd | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6RGAKANZZY.b63bed | FE-LU | CPM | 300.0 | Fe2Lu | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PIU2NHVH32.18f6d2 | FE-LU | CPM | 290.0 | Fe2Lu | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3DFCHE5IR2.11713e | FE-TM | CPM | 290.0 | Fe2Tm | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NUHO6HHWO3.b76be8 | FE-TM | CPM | 300.0 | Fe2Tm | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6LBYYMRF75.603efa | FE-Y | GM_FORM | 973.0 | Fe17Y2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KU7WUHD2V2.f6b958 | FE-Y | GM_FORM | 973.0 | Fe3Y | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-YIWT6AZWC6.d0b6b1 | FE-Y | GM_FORM | 895.0 | Fe17Y2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6OSRGYMQDQ | GA-SE | SM | 298.0 | β-Ga2Se3 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HG7LOTMMDU | GA-SE | SM | 298.0 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-I4YOLNDV4S | GA-SE | SM | 298.0 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MM6PA5TXHW | GA-SE | SM | 298.0 | β-Ga2Se3 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NYI2LSUD7M | GA-SE | SM | 298.0 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-O7KYJO5SNX | GA-SE | SM | 298.0 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RHIBFFNDTR | GA-SE | SM | 298.0 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-V3JJYGH5BO | GA-SE | SM | 298.0 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B7SZWQWZ6C | GE-P | SM | 298.0 | Ge1P1 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3VTJ5UM27P | LI-SB | GM_FORM | 723.0 | Li3Sb | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BDUZKOBQSG | LI-SB | GM_FORM | 630.0 | Li3Sb | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FWLVF5XETV | LI-SB | GM_FORM | 630.0 | Li2Sb | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SGNKL2MPDJ | LI-SB | GM_FORM | 723.0 | Li2Sb | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3EP2RAVNHP.48e3a8 | MG-SI | SM | 298.0 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-45PCIV5J5E | MG-SI | CPM | 383.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4YXFQ4ZRYX.6d85ee | MG-SI | CPM | 513.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4YXFQ4ZRYX.994b18 | MG-SI | CPM | 513.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5EZRJRQ5V6 | MG-SI | CPM | 623.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5FLUIEC3GZ | MG-SI | CPM | 583.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6UMIRMG7DS | MG-SI | CPM | 543.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7G23CBNW46.74a375 | MG-SI | CPM | 553.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7G23CBNW46.88f04f | MG-SI | CPM | 553.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7UNHT7Y5ZC.004be0 | MG-SI | CPM | 773.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7UNHT7Y5ZC.d952a0 | MG-SI | CPM | 773.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-A3CSOQESVH | MG-SI | CPM | 783.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BKHQDGCW7O | MG-SI | CPM | 443.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-C5WUQTGSIS.40195d | MG-SI | CPM | 673.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-C5WUQTGSIS.495b52 | MG-SI | CPM | 673.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-C7M3WPNJL3.6d0e35 | MG-SI | CPM | 653.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-C7M3WPNJL3.f34470 | MG-SI | CPM | 653.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CN5CHCIBKV | MG-SI | CPM | 503.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-E3RXDXORFP | MG-SI | CPM | 403.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FLICYKGIIJ | MG-SI | SM | 298.0 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GH7U4XTBVB | MG-SI | CPM | 363.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GYI2XSQTVH | MG-SI | CPM | 563.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IBSFAEN5EH | MG-SI | CPM | 803.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IIVLC4GRG6.2749fa | MG-SI | CPM | 593.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IIVLC4GRG6.c0a300 | MG-SI | CPM | 593.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IYSRVYIFHF | MG-SI | CPM | 683.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JAXMQJWGAZ.56716d | MG-SI | CPM | 693.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JAXMQJWGAZ.ff4911 | MG-SI | CPM | 693.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JXU7RLOV22.589a41 | MG-SI | CPM | 573.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JXU7RLOV22.ab8442 | MG-SI | CPM | 573.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KNODUZ7WM7 | MG-SI | CPM | 743.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LD55S7QAMA | MG-SI | CPM | 703.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MMLUA4KJMN.52348e | MG-SI | CPM | 493.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MMLUA4KJMN.67a5ad | MG-SI | CPM | 493.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MNDEPH4I7O.c7dc1e | MG-SI | CPM | 733.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MNDEPH4I7O.ea2d17 | MG-SI | CPM | 733.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-N5ELPG3PEA | MG-SI | CPM | 423.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NDS7G2BINE.878f28 | MG-SI | CPM | 613.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NDS7G2BINE.e8d779 | MG-SI | CPM | 613.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NZ7AR4A2I3 | MG-SI | CPM | 523.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QMZJEX7BHD.50cf55 | MG-SI | CPM | 533.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QMZJEX7BHD.6ecd7a | MG-SI | CPM | 533.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SRXWDOPAEK | MG-SI | CPM | 483.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SZ27UHTPAP.732a05 | MG-SI | CPM | 473.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SZ27UHTPAP.774d35 | MG-SI | CPM | 473.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TKZQ4AI54G.d24650 | MG-SI | SM | 298.0 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-U32QJAYGET.07f50e | MG-SI | CPM | 633.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-U32QJAYGET.ace621 | MG-SI | CPM | 633.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UJBRTZBL7N | MG-SI | SM | 298.0 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UYNHHAUDDP | MG-SI | CPM | 603.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UZZUDONX6Y.c8049b | MG-SI | CPM | 793.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UZZUDONX6Y.c96a13 | MG-SI | CPM | 793.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VTFFMX56E5 | MG-SI | CPM | 463.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-X2BVFNH6ZV | MG-SI | CPM | 663.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XJ7UZ36IHH.567998 | MG-SI | CPM | 713.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XJ7UZ36IHH.917efb | MG-SI | CPM | 713.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XSTB7FDDSL.65d38c | MG-SI | CPM | 753.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XSTB7FDDSL.771649 | MG-SI | CPM | 753.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XUN66SPZKV | MG-SI | CPM | 763.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XWHBO6WRRY | MG-SI | CPM | 643.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZIUDPR7GD4 | MG-SI | CPM | 723.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2ATZQOQRCH | ND-ZN | GM_MIX | 1173.15 | NdZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3JVNQE5B23 | ND-ZN | GM_MIX | 773.15 | NdZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5S524GOI3E | ND-ZN | GM_MIX | 1173.15 | Nd13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6CSAUODHKB | ND-ZN | GM_MIX | 973.15 | NdZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7BIOCWCKPS | ND-ZN | GM_MIX | 973.15 | Nd2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B2EKXUYWTF | ND-ZN | GM_MIX | 1173.15 | Nd2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B4M5M7NQAG | ND-ZN | GM_MIX | 1173.15 | NdZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BXJ4QZGWMU | ND-ZN | GM_MIX | 973.15 | NdZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CKSZCOWR27 | ND-ZN | GM_MIX | 773.15 | Nd2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DHFHJXYE6K | ND-ZN | GM_MIX | 773.15 | NdZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IAC6RDXQYL | ND-ZN | GM_MIX | 773.15 | Nd3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-K2QCSVOTRD | ND-ZN | GM_MIX | 773.15 | Nd13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KDVU6VQ47C | ND-ZN | GM_MIX | 773.15 | NdZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KWF4CVF4JV | ND-ZN | GM_MIX | 973.15 | Nd3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MZ5UATJ747 | ND-ZN | GM_MIX | 973.15 | NdZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NAJNSOPOZH | ND-ZN | GM_MIX | 1173.15 | Nd3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NHAXCP7Q64 | ND-ZN | GM_MIX | 1173.15 | NdZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PXOL3HMSSA | ND-ZN | GM_MIX | 1173.15 | NdZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QCPK3FIRBC | ND-ZN | GM_MIX | 973.15 | Nd3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SGI7ACYPEG | ND-ZN | GM_MIX | 773.15 | NdZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TQ7SUM7POQ | ND-ZN | GM_MIX | 1173.15 | Nd3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VUJTPRAOJY | ND-ZN | GM_MIX | 973.15 | Nd13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-W4A6Z3CVZQ | ND-ZN | GM_MIX | 773.15 | Nd3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-X464TN5H34 | ND-ZN | GM_MIX | 973.15 | NdZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WR54NXQDJY | P-SI | SM | 298.15 | SiP | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2UVFZKE7S2.510392 | PB-Y | CPM | 743.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2UVFZKE7S2.a5a14d | PB-Y | CPM | 743.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2UVFZKE7S2.cd3079 | PB-Y | CPM | 743.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2UVFZKE7S2.fda0b4 | PB-Y | CPM | 743.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3V3AFPPIIQ.146193 | PB-Y | CPM | 373.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3V3AFPPIIQ.63a4a7 | PB-Y | CPM | 373.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3V3AFPPIIQ.d594a1 | PB-Y | CPM | 373.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3V3AFPPIIQ.e43852 | PB-Y | CPM | 373.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4AGDIUIHWP.6adfc9 | PB-Y | CPM | 723.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4AGDIUIHWP.70eda2 | PB-Y | CPM | 723.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4AGDIUIHWP.a5bbc9 | PB-Y | CPM | 723.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4AGDIUIHWP.f1a5b2 | PB-Y | CPM | 723.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-56S56YXJ73.47d53d | PB-Y | CPM | 563.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-56S56YXJ73.9782f8 | PB-Y | CPM | 563.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-56S56YXJ73.da8b6e | PB-Y | CPM | 563.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-56S56YXJ73.e07247 | PB-Y | CPM | 563.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5BPLUW7ES2.0b79ec | PB-Y | CPM | 633.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5BPLUW7ES2.494782 | PB-Y | CPM | 633.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5BPLUW7ES2.8247a0 | PB-Y | CPM | 633.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5BPLUW7ES2.eba1b4 | PB-Y | CPM | 633.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5MXHP4D6WD.63c302 | PB-Y | CPM | 643.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5MXHP4D6WD.9f0270 | PB-Y | CPM | 643.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5MXHP4D6WD.bf0c9d | PB-Y | CPM | 643.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5MXHP4D6WD.d6d540 | PB-Y | CPM | 643.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6D2T7TMSUF.559572 | PB-Y | CPM | 673.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6D2T7TMSUF.b9c7e4 | PB-Y | CPM | 673.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6D2T7TMSUF.ee611c | PB-Y | CPM | 673.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6D2T7TMSUF.fe8a18 | PB-Y | CPM | 673.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6OYVJ4ODS2.2e735d | PB-Y | CPM | 443.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6OYVJ4ODS2.77af9f | PB-Y | CPM | 443.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6OYVJ4ODS2.c74916 | PB-Y | CPM | 443.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6OYVJ4ODS2.d1d819 | PB-Y | CPM | 443.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AB2QFWBVCI.0330d1 | PB-Y | CPM | 773.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AB2QFWBVCI.6358a9 | PB-Y | CPM | 773.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AB2QFWBVCI.7f9ea3 | PB-Y | CPM | 773.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AB2QFWBVCI.f454f7 | PB-Y | CPM | 773.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ASFGPTUZ5U.0efdcf | PB-Y | CPM | 483.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ASFGPTUZ5U.9ab983 | PB-Y | CPM | 483.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ASFGPTUZ5U.c9ed31 | PB-Y | CPM | 483.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ASFGPTUZ5U.e45066 | PB-Y | CPM | 483.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B2OSMGVCMW.6555cd | PB-Y | CPM | 763.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B2OSMGVCMW.7e60f1 | PB-Y | CPM | 763.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B2OSMGVCMW.de311c | PB-Y | CPM | 763.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B2OSMGVCMW.e42dfe | PB-Y | CPM | 763.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CSTGN2PRBA.3a40a1 | PB-Y | CPM | 523.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CSTGN2PRBA.487545 | PB-Y | CPM | 523.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CSTGN2PRBA.bed531 | PB-Y | CPM | 523.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CSTGN2PRBA.ff1be9 | PB-Y | CPM | 523.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-D47435RAC4.166eff | PB-Y | CPM | 693.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-D47435RAC4.201ae0 | PB-Y | CPM | 693.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-D47435RAC4.491ee3 | PB-Y | CPM | 693.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-D47435RAC4.c6fbd6 | PB-Y | CPM | 693.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EFK7HAMWYJ.25b079 | PB-Y | CPM | 423.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EFK7HAMWYJ.5ccb15 | PB-Y | CPM | 423.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EFK7HAMWYJ.9f69f0 | PB-Y | CPM | 423.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EFK7HAMWYJ.cf77a5 | PB-Y | CPM | 423.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FJLOV5SYCP.1cb268 | PB-Y | CPM | 403.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FJLOV5SYCP.215a15 | PB-Y | CPM | 403.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FJLOV5SYCP.39ca79 | PB-Y | CPM | 403.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FJLOV5SYCP.6c3546 | PB-Y | CPM | 403.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GEF33U3Q4W.832df7 | PB-Y | CPM | 603.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GEF33U3Q4W.d5d22f | PB-Y | CPM | 603.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GEF33U3Q4W.f466ff | PB-Y | CPM | 603.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GEF33U3Q4W.fdddb8 | PB-Y | CPM | 603.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HU7KJ4VCJP.0bd4c6 | PB-Y | CPM | 653.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HU7KJ4VCJP.3217ba | PB-Y | CPM | 653.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HU7KJ4VCJP.3f8c4a | PB-Y | CPM | 653.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HU7KJ4VCJP.e8fbfc | PB-Y | CPM | 653.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IIFV7FRLN3.20db1d | PB-Y | CPM | 583.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IIFV7FRLN3.74ce78 | PB-Y | CPM | 583.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IIFV7FRLN3.75f713 | PB-Y | CPM | 583.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IIFV7FRLN3.8618f3 | PB-Y | CPM | 583.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ILL6EZDC7G.3fd4cd | PB-Y | CPM | 543.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ILL6EZDC7G.43c6e5 | PB-Y | CPM | 543.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ILL6EZDC7G.5e8efc | PB-Y | CPM | 543.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ILL6EZDC7G.ba8b23 | PB-Y | CPM | 543.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVX5MFRAPQ.280fae | PB-Y | CPM | 703.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVX5MFRAPQ.2f0716 | PB-Y | CPM | 703.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVX5MFRAPQ.7af8d3 | PB-Y | CPM | 703.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVX5MFRAPQ.bb90e7 | PB-Y | CPM | 703.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVZ4T4MJTO.3d15bb | PB-Y | CPM | 663.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVZ4T4MJTO.47c307 | PB-Y | CPM | 663.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVZ4T4MJTO.50be95 | PB-Y | CPM | 663.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JVZ4T4MJTO.86484a | PB-Y | CPM | 663.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-L2BHBMLURG.0531c6 | PB-Y | CPM | 463.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-L2BHBMLURG.da7982 | PB-Y | CPM | 463.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-L2BHBMLURG.e3dc54 | PB-Y | CPM | 463.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-L2BHBMLURG.e90aee | PB-Y | CPM | 463.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LCRQB6WCRG.0f3562 | PB-Y | CPM | 713.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LCRQB6WCRG.24e005 | PB-Y | CPM | 713.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LCRQB6WCRG.3886a8 | PB-Y | CPM | 713.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LCRQB6WCRG.b7dd8e | PB-Y | CPM | 713.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LMOHF4ZOKC.455ee5 | PB-Y | CPM | 553.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LMOHF4ZOKC.7c395d | PB-Y | CPM | 553.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LMOHF4ZOKC.b9be39 | PB-Y | CPM | 553.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LMOHF4ZOKC.ff2dab | PB-Y | CPM | 553.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MESF76VLLW.6fa06f | PB-Y | CPM | 433.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MESF76VLLW.7b0357 | PB-Y | CPM | 433.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MESF76VLLW.91de36 | PB-Y | CPM | 433.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MESF76VLLW.b97fac | PB-Y | CPM | 433.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MXTJKCGSD4.49f4fa | PB-Y | CPM | 493.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MXTJKCGSD4.4ae72b | PB-Y | CPM | 493.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MXTJKCGSD4.89f2cf | PB-Y | CPM | 493.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MXTJKCGSD4.e0786e | PB-Y | CPM | 493.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NVHMMDCMQJ.06fe90 | PB-Y | CPM | 453.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NVHMMDCMQJ.37956a | PB-Y | CPM | 453.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NVHMMDCMQJ.8043fa | PB-Y | CPM | 453.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NVHMMDCMQJ.ac157a | PB-Y | CPM | 453.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-P5YSPTBEAX.016f36 | PB-Y | CPM | 573.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-P5YSPTBEAX.5311ed | PB-Y | CPM | 573.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-P5YSPTBEAX.77aba7 | PB-Y | CPM | 573.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-P5YSPTBEAX.eae585 | PB-Y | CPM | 573.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PQCJRLBNTH.3bed55 | PB-Y | CPM | 613.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PQCJRLBNTH.417cf0 | PB-Y | CPM | 613.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PQCJRLBNTH.61dfd4 | PB-Y | CPM | 613.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PQCJRLBNTH.c8290a | PB-Y | CPM | 613.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RBGL5CIGGT.8c08a4 | PB-Y | CPM | 733.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RBGL5CIGGT.97cf57 | PB-Y | CPM | 733.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RBGL5CIGGT.9a4664 | PB-Y | CPM | 733.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RBGL5CIGGT.fc026e | PB-Y | CPM | 733.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T7OLBGQ2QC.26f433 | PB-Y | CPM | 623.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T7OLBGQ2QC.546c80 | PB-Y | CPM | 623.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T7OLBGQ2QC.c9f8ec | PB-Y | CPM | 623.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T7OLBGQ2QC.ee00f6 | PB-Y | CPM | 623.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSTKVGYMOO.06b6ee | PB-Y | CPM | 533.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSTKVGYMOO.2ea602 | PB-Y | CPM | 533.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSTKVGYMOO.4b313d | PB-Y | CPM | 533.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSTKVGYMOO.e20c1c | PB-Y | CPM | 533.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UMAE4EIHTV.146fdf | PB-Y | CPM | 413.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UMAE4EIHTV.384b04 | PB-Y | CPM | 413.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UMAE4EIHTV.61f081 | PB-Y | CPM | 413.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UMAE4EIHTV.fb3f59 | PB-Y | CPM | 413.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UO2AYCKTDJ.03f8eb | PB-Y | CPM | 753.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UO2AYCKTDJ.51bb34 | PB-Y | CPM | 753.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UO2AYCKTDJ.5e59d5 | PB-Y | CPM | 753.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UO2AYCKTDJ.fcb90d | PB-Y | CPM | 753.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VAZZN6UPVN.28dee1 | PB-Y | CPM | 593.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VAZZN6UPVN.987163 | PB-Y | CPM | 593.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VAZZN6UPVN.d20287 | PB-Y | CPM | 593.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VAZZN6UPVN.fd8d97 | PB-Y | CPM | 593.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WRZSZVX7CY.0cb732 | PB-Y | CPM | 393.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WRZSZVX7CY.45ee43 | PB-Y | CPM | 393.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WRZSZVX7CY.c2ddaa | PB-Y | CPM | 393.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WRZSZVX7CY.ca835b | PB-Y | CPM | 393.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XNLDIIZ3NX.10c40d | PB-Y | CPM | 683.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XNLDIIZ3NX.8f5cf7 | PB-Y | CPM | 683.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XNLDIIZ3NX.d14504 | PB-Y | CPM | 683.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XNLDIIZ3NX.dd2867 | PB-Y | CPM | 683.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z2MTCTP547.2aed20 | PB-Y | CPM | 473.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z2MTCTP547.8bd428 | PB-Y | CPM | 473.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z2MTCTP547.a794ce | PB-Y | CPM | 473.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z2MTCTP547.b6ac33 | PB-Y | CPM | 473.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z6HAQ2EFR6.42e33e | PB-Y | CPM | 513.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z6HAQ2EFR6.5c61e4 | PB-Y | CPM | 513.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z6HAQ2EFR6.6ce22e | PB-Y | CPM | 513.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-Z6HAQ2EFR6.714c34 | PB-Y | CPM | 513.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZIQQRRTWAT.1e3a5c | PB-Y | CPM | 503.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZIQQRRTWAT.2f126e | PB-Y | CPM | 503.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZIQQRRTWAT.d74fa0 | PB-Y | CPM | 503.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZIQQRRTWAT.e0a536 | PB-Y | CPM | 503.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZW2RBRTRQQ.2315dd | PB-Y | CPM | 383.0 | YPb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZW2RBRTRQQ.3d3f39 | PB-Y | CPM | 383.0 | YPb2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZW2RBRTRQQ.89d534 | PB-Y | CPM | 383.0 | Y5Pb4 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZW2RBRTRQQ.b8fa0d | PB-Y | CPM | 383.0 | Y5Pb3 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2UZJC3N6JJ | PR-ZN | GM_MIX | 773.15 | αPr2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-33FDTG6NVN | PR-ZN | GM_MIX | 773.15 | Pr3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3UC2XEIAVB | PR-ZN | GM_MIX | 773.15 | PrZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-D3LXCAMZ7F | PR-ZN | GM_MIX | 773.15 | PrZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DX5UMN4EJ2 | PR-ZN | GM_MIX | 773.15 | αPrZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MZ323ESQJ7 | PR-ZN | GM_MIX | 773.15 | Pr13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MZETKMPROX | PR-ZN | GM_MIX | 773.15 | PrZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RVGYCWUQHI | PR-ZN | GM_MIX | 773.15 | PrZn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-X2C2KWPUJS | PR-ZN | GM_MIX | 773.15 | Pr3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VURWOO5JZR.a2b842 | RE-TA | GM_FORM | 298.15 | TaRe1.5 (σ or χ) | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VURWOO5JZR.d36f92 | RE-TA | GM_FORM | 298.15 | TaRe1.5 (σ or χ) | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-345NTR6DDL.0c5f20 | SI-TA | SM | 2045.0 | Si0.3333Ta0.6667 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GIH62I4VZW.20f2dc | SI-TA | SM | 1027.0 | Si0.3333Ta0.6667 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-K6GMSBONRZ.3fe8b5 | SI-TA | SM | 2087.5 | Si0.25Ta0.75 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-OLNLWPIRLP.c37eb0 | SI-TA | SM | 1760.5 | Si0.6667Ta0.3333 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-32RUX5I6LW | SM-ZN | GM_MIX | 973.15 | Sm3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-34PUB3JLDB | SM-ZN | GM_MIX | 973.15 | Sm13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3GSTV6FR7O | SM-ZN | GM_MIX | 973.15 | SmZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3WWXG3KLXW | SM-ZN | GM_MIX | 1173.15 | SmZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-44DYV436VP | SM-ZN | GM_MIX | 973.15 | SmZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5SGYRKTL4Z | SM-ZN | GM_MIX | 1173.15 | SmZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CCKH2ZC3OC | SM-ZN | GM_MIX | 773.15 | SmZn2 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CSB4QY535P | SM-ZN | GM_MIX | 773.15 | SmZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DZZVET53KI | SM-ZN | GM_MIX | 973.15 | Sm3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ENYC5DGVKJ | SM-ZN | GM_MIX | 973.15 | Sm2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IOXMXKWJEN | SM-ZN | GM_MIX | 1173.15 | Sm3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KJUINFJ4PN | SM-ZN | GM_MIX | 973.15 | SmZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MIGPL255DV | SM-ZN | GM_MIX | 773.15 | Sm2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NO76GSQUOM | SM-ZN | GM_MIX | 773.15 | SmZn3 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QICZWTTHCR | SM-ZN | GM_MIX | 1173.15 | SmZn | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RPTA4PZEF7 | SM-ZN | GM_MIX | 773.15 | Sm3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RSMAR3WZAH | SM-ZN | GM_MIX | 1173.15 | Sm3Zn22 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SJLG4VVRQL | SM-ZN | GM_MIX | 773.15 | Sm3Zn11 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T2W7HHQI4L | SM-ZN | GM_MIX | 1173.15 | Sm2Zn17 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XHOHAWLLOO | SM-ZN | GM_MIX | 1173.15 | Sm13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZTYQWQQDBR | SM-ZN | GM_MIX | 773.15 | Sm13Zn58 | compound_property_not_fittable | GM_MIX of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JUCGQY5M4A | CO-TH | INVARIANT_TEMPERATURE | 695.15 | αCo, εCo, L | liquid_impossible_at_T | liquid at 695.15 K, below 987 K (calculated_sgte_diagram) |
| ORC-W4VI3EMFMR | CO-TH | INVARIANT_TEMPERATURE | 695.15 | αCo, εCo, L | liquid_impossible_at_T | liquid at 695.15 K, below 987 K (calculated_sgte_diagram) |
| ORC-3KJCNBMBQI | HF-MN | PHASE_COMPOSITION | 973.15 | liquid | liquid_impossible_at_T | liquid at 973.15 K, below 1185 K (calculated_sgte_diagram) |
| ORC-OI6UCVJ5NJ | HF-MN | PHASE_COMPOSITION | 973.15 | liquid | liquid_impossible_at_T | liquid at 973.15 K, below 1185 K (calculated_sgte_diagram) |
| ORC-ZC773CVD62 | HF-MN | PHASE_COMPOSITION | 973.15 | liquid | liquid_impossible_at_T | liquid at 973.15 K, below 1185 K (calculated_sgte_diagram) |
| ORC-CIPJAZEEG7 | MO-O | INVARIANT_TEMPERATURE | 1053.15 | L, Mo8O23, Mo9O26 | liquid_impossible_at_T | liquid at 1053.15 K, below 1985 K (calculated_sgte_diagram) |
| ORC-DUVVS2WS3I | MO-O | INVARIANT_TEMPERATURE | 1051.15 | L, Mo9O26, MoO3 | liquid_impossible_at_T | liquid at 1051.15 K, below 1985 K (calculated_sgte_diagram) |
| ORC-UUOU4YRKZL | MO-O | INVARIANT_TEMPERATURE | 1091.15 | L, MoO2, Mo4O11 | liquid_impossible_at_T | liquid at 1091.15 K, below 1985 K (calculated_sgte_diagram) |
| ORC-H3GLAFRIM7 | AL-HF | HM_FORM | 298.15 | HfAl3 | phase_label_ambiguous | label 'HfAl3' |
| ORC-UVWYIQWC3J | AL-HF | HM_FORM | 298.15 | HfAl3 | phase_label_ambiguous | label 'HfAl3' |
| ORC-7X7QCYYHAV | AL-Y | HM_FORM | 298.0 | YAl3 | phase_label_ambiguous | label 'YAl3' |
| ORC-QQHP64NZUS | AL-Y | HM_FORM | 763.0 | YAl3 | phase_label_ambiguous | label 'YAl3' |
| ORC-XPGR46OSAB.1518c7 | BA-PB | HM_FORM | 300.0 | αBa0.375Pb0.625 | phase_label_ambiguous | label 'αBa0.375Pb0.625' |
| ORC-K4G26RVS4P.4000e4 | BI-K | GM_FORM | 848.0 | BiK3 | phase_label_ambiguous | label 'BiK3' |
| ORC-K4G26RVS4P.72381c | BI-K | HM_FORM | 848.0 | BiK3 | phase_label_ambiguous | label 'BiK3' |
| ORC-K4G26RVS4P.ff46e0 | BI-K | SM_FORM | 848.0 | BiK3 | phase_label_ambiguous | label 'BiK3' |
| ORC-HSK6QNTTOF.428513 | BI-LI | SM_FORM | 298.15 | BiLi | phase_label_ambiguous | label 'BiLi' |
| ORC-HSK6QNTTOF.8f631f | BI-LI | HM_FORM | 298.15 | BiLi | phase_label_ambiguous | label 'BiLi' |
| ORC-WDMJMMR37T | BI-LI | HM_FORM | 298.15 | BiLi | phase_label_ambiguous | label 'BiLi' |
| ORC-5Q5G5NGQUV.61e74c | BI-RB | HM_FORM | 0.0 | αBiRb3 | phase_label_ambiguous | label 'αBiRb3' |
| ORC-R23YOSUSUV.26edee | BI-RB | HM_FORM | 0.0 | αBiRb3 | phase_label_ambiguous | label 'αBiRb3' |
| ORC-RZXTTI2S6E.218093 | BI-RB | HM_FORM | 298.15 | αBiRb3 | phase_label_ambiguous | label 'αBiRb3' |
| ORC-RZXTTI2S6E.2246b1 | BI-RB | SM_FORM | 298.15 | αBiRb3 | phase_label_ambiguous | label 'αBiRb3' |
| ORC-V7JKB5ZQ5Q.2c27ee | BI-RB | HM_FORM | 0.0 | ßBiRb3 | phase_label_ambiguous | label 'ßBiRb3' |
| ORC-YVCSYC5JGI.8913b4 | BI-RB | HM_FORM | 0.0 | ßBiRb3 | phase_label_ambiguous | label 'ßBiRb3' |
| ORC-CHVOY6D4FJ.422766 | CO-GE | HM_FORM | 1060.0 | α(Co)+βCo5Ge3 | phase_label_ambiguous | label 'α(Co)+βCo5Ge3' |
| ORC-FA37UICRO3.df5d89 | CO-GE | HM_FORM | 1060.0 | α(Co)+βCo5Ge3 | phase_label_ambiguous | label 'α(Co)+βCo5Ge3' |
| ORC-4IKMXI5UTB.3dd9ab | CS-TE | HM_FORM | 298.15 | Cs2Te | phase_label_ambiguous | label 'Cs2Te' |
| ORC-LEVZKAYSFQ.3928ec | CS-TE | SM | 298.15 | Cs2Te | phase_label_ambiguous | label 'Cs2Te' |
| ORC-3ZQFHDEH6W.183131 | CU-ZR | HM_FORM | 0.0 | CuZr2-C11b | phase_label_ambiguous | label 'CuZr2-C11b' |
| ORC-L4LH5UJX5O | FE-GD | HM_FORM | 298.0 | Fe17Gd2 | phase_label_ambiguous | label 'Fe17Gd2' |
| ORC-QJ56PUEUMY | FE-HF | HM_FORM | 1373.0 | Fe2Hf-HT | phase_label_ambiguous | label 'Fe2Hf-HT' |
| ORC-U33KIRTKYB | FE-HF | HM_FORM | 1723.0 | Fe2Hf-HT | phase_label_ambiguous | label 'Fe2Hf-HT' |
| ORC-FQDLRJYDWH | GA-Y | HM_FORM | 298.15 | Ga3Y5 | phase_label_ambiguous | label 'Ga3Y5' |
| ORC-KW3VBQ6QZL | GA-Y | HM_FORM | 298.15 | Ga3Y5 | phase_label_ambiguous | label 'Ga3Y5' |
| ORC-J54C6AXT5M | GE-RU | HM_FORM | 1173.0 | Ru2Ge3 | phase_label_ambiguous | label 'Ru2Ge3' |
| ORC-STEFK5VKOZ | GE-RU | HM_FORM | 298.0 | Ru2Ge3 | phase_label_ambiguous | label 'Ru2Ge3' |
| ORC-4KBCL5U4BH.046030 | LI-SB | SM_FORM | 686.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-4KBCL5U4BH.342b48 | LI-SB | HM_FORM | 686.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-4KBCL5U4BH.5cf9aa | LI-SB | HM_FORM | 686.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-4KBCL5U4BH.83f318 | LI-SB | SM_FORM | 686.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-L3ZY532BLT.85a76f | LI-SB | HM_FORM | 700.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-L3ZY532BLT.a91cd1 | LI-SB | HM_FORM | 700.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-L3ZY532BLT.f04169 | LI-SB | SM_FORM | 700.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-L3ZY532BLT.fa1aab | LI-SB | SM_FORM | 700.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-4ID3VNUSY5.45dd63 | MG-NI | GM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-4ID3VNUSY5.ba10f5 | MG-NI | HM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-4ID3VNUSY5.e2a598 | MG-NI | SM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-5PCDUQPPMY.4cb693 | MG-NI | HM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-KARWEPEIDM.4ac245 | MG-NI | HM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-KARWEPEIDM.4ecbac | MG-NI | GM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-KARWEPEIDM.9997a1 | MG-NI | SM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-QVTPLSNWR4.05710d | MG-NI | HM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-ZUOAQ2M7RC.026af2 | MG-NI | HM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-ZUOAQ2M7RC.58e75d | MG-NI | GM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-ZUOAQ2M7RC.8cd579 | MG-NI | SM_FORM | 298.15 | Mg2Ni | phase_label_ambiguous | label 'Mg2Ni' |
| ORC-7EFEZK2TDU.32710c | N-SI | HM_FORM | 298.0 | α-Si3N4 | phase_label_ambiguous | label 'α-Si3N4' |
| ORC-7Y3UKOYUWX.ff192f | N-SI | SM | 298.0 | α-Si3N4 | phase_label_ambiguous | label 'α-Si3N4' |
| ORC-K3LQZVOONG.1b4e3e | NI-SI | HM_FORM | 298.0 | αNiSi2 | phase_label_ambiguous | label 'αNiSi2' |
| ORC-LDP5O2JGT6.cde3eb | PD-SN | HM_FORM | 320.0 | α-Pd3Sn2 | phase_label_ambiguous | label 'α-Pd3Sn2' |
| ORC-7VPUF5XRGG.1e6b0e | SB-ZN | GM_FORM | 806.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-7VPUF5XRGG.2a862c | SB-ZN | HM_FORM | 806.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-LJ7NTT3MZM.0521f9 | SB-ZN | HM_FORM | 826.0 | δ′-Sb3Zn4 | phase_label_ambiguous | label 'δ′-Sb3Zn4' |
| ORC-LJ7NTT3MZM.f6971e | SB-ZN | GM_FORM | 826.0 | δ′-Sb3Zn4 | phase_label_ambiguous | label 'δ′-Sb3Zn4' |
| ORC-NNBDCYEADO.2a8dfa | SB-ZN | GM_FORM | 800.0 | ξ-Sb2Zn3 | phase_label_ambiguous | label 'ξ-Sb2Zn3' |
| ORC-NNBDCYEADO.98dc51 | SB-ZN | HM_FORM | 800.0 | ξ-Sb2Zn3 | phase_label_ambiguous | label 'ξ-Sb2Zn3' |
| ORC-NZUTUZNKYH.3f1124 | SB-ZN | HM_FORM | 800.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-NZUTUZNKYH.b1f117 | SB-ZN | GM_FORM | 800.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-2CEFS6VVEV.afeb02 | SE-SN | HM_FORM | 298.0 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-OTLJ2QNFR6 | SE-SN | HM_FORM | 298.0 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-SXCESCRLPN.a39dda | SE-SN | HM_FORM | 298.0 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-TZ4OR4CMJG | SE-SN | HM_FORM | 298.0 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-V7VHHJ5GSB.b91536 | SE-SN | HM_FORM | 298.0 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-5O7BBL2ZS5.6cd718 | SI-TA | HM_FORM | 1473.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-GCYCOHJVMK.b0dbf6 | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-HO7JT6JFYO.6095fb | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-OEWHAHTIO4.06dce4 | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-OVSTHRO2TO.ad70dc | SI-TA | HM_FORM | 1027.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-OVSTHRO2TO.cff80a | SI-TA | SM | 1027.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-RBNDQYDXRA.5f2d77 | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-WLRX6KX33K.3c6241 | SI-TA | SM | 1900.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-WLRX6KX33K.5fec23 | SI-TA | HM_FORM | 1900.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-FSYVSAZKHR | SI-U | HM_FORM | 298.0 | U3Si | phase_label_ambiguous | label 'U3Si' |
| ORC-C3QDI5675C | SN-TI | HM_FORM | 298.15 | Sn5Ti6-L | phase_label_ambiguous | label 'Sn5Ti6-L' |
| ORC-YTPULMUAG2.147391 | SN-TI | HM_FORM | 298.15 | Sn5Ti6-L | phase_label_ambiguous | label 'Sn5Ti6-L' |
| ORC-3QIK7OVINP.90029a | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
| ORC-4AIGKIGSRZ.f2f361 | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
| ORC-4T6PPMNMVH.c19ed3 | AL-CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-56LEO63NHI.173bf6 | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
| ORC-6WOBDFQDT6.aa92cb | AL-CA | HM_FORM | 298.15 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-7WTP4LTZGH.dc5f91 | AL-CA | HM_FORM | 298.15 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-AJBLYDVVJ7.a01f20 | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-BIBOWE6FPC.9d438f | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-CUGQ3IS253.0c760d | AL-CA | HM_FORM | 0.0 | C15-Ca2Al | phase_label_not_mapped | label 'C15-Ca2Al' |
| ORC-FHBP4YQMQO.3fd5f4 | AL-CA | HM_FORM | 298.15 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-H3W2VXUOCC.dc7e94 | AL-CA | HM_FORM | 0.0 | C15-Ca2Al | phase_label_not_mapped | label 'C15-Ca2Al' |
| ORC-HH5P332BD5.027576 | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-LDRKSJQLLM.0b304d | AL-CA | HM_FORM | 0.0 | C15-Ca2Al | phase_label_not_mapped | label 'C15-Ca2Al' |
| ORC-OHVOHPTKPU.3d337a | AL-CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-RBRLISTFX3.c24d82 | AL-CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-RRTXNAEBFG.4b59a8 | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-RU5SWY7JGW.072bed | AL-CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-SGGMA66RLQ.98325d | AL-CA | HM_FORM | 0.0 | C15-Ca2Al | phase_label_not_mapped | label 'C15-Ca2Al' |
| ORC-TCPC77DHKK.452f64 | AL-CA | HM_FORM | 298.15 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-WAZ6UJADGF.8da616 | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-ZKD74CCMXO.fb87dd | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
| ORC-4GEM5JXZRL | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-52RX4KJCDS | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-5DVIFPHSFN | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-65JDHAPWG3 | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-66QDO5IYIG | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-67RITL3LR6 | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-6G3EKW4XCM | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-6OYLJDF5W6 | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-7LWVQ5UDUI | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-A4YFGUJQFA | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-E7AOQYLW7C | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-F6V7ZTZOXE | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-IGICY273VQ | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-IGTLLSONGK | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-L4FSTSSWWM | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-LBNVYX7MKG | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-LMPO46BMIF | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-MVK4ZWOCGE | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-OVPAV4MJMS | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-UQKZUDGG6O | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-UT62E76MOR | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-Y4J4UL4PVK | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-YLKF46ZAQF | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-326E3OHRXX | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-32GMQ4UZPY | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-3D4W5TGD42 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-3TOSQGHNGM | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-3UZ3TZACIU | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-3VAP5U3PYE | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-4AVGOLDRYY.862ddc | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-4AVGOLDRYY.d5c876 | AL-CO-CR-NI | HM_FORM | 0.0 | B2-β | phase_label_not_mapped | label 'B2-β' |
| ORC-4EGJ77QJYM | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-4EP7XRAXPS | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-4NPP2JSIVO.14743d | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-4NPP2JSIVO.147cf7 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-4NPP2JSIVO.f9d281 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-4RXVDM6W2U | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-56UQQ3KDZU | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-5I6MP4KN2N | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-5SQ6ZVI24R.5bc4e5 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-5SQ6ZVI24R.983bd0 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-5SQ6ZVI24R.c2f5af | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-5WMXIEWM4J | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-74RBDPJKYV | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-7BZ4YFYJFR | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-7GQJDWDHJQ | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-BJCC23KTCK.568105 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-BJCC23KTCK.7c92d8 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-BJCC23KTCK.cb1de8 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-BQZ45U6GCO.1a056d | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-BQZ45U6GCO.1a17bc | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-BQZ45U6GCO.c1d891 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-BSYOVSRLCW | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-BZVTAKWUEV | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-CG6B7EHP2R.127230 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-CG6B7EHP2R.be88a2 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-CG6B7EHP2R.d87371 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-CJF25RA3S4.641cc6 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-CJF25RA3S4.a678d8 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-CJF25RA3S4.eb269c | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-COMWLLIR2L.35ebd5 | AL-CO-CR-NI | HM_FORM | 298.0 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-COMWLLIR2L.4ebb85 | AL-CO-CR-NI | HM_FORM | 298.0 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-CWVXPYGUEK | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-DDS6WWAX23 | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-DES3Y567OU | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-DOSQLG6EWU | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-E3SGIIH26O | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-EAJVUJJ3L3 | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-ECXY5ARLCL | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-ETBNSP746Y | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-FCRRH4IFTR | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-G4BGOQUI73 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-GEAL46TYRL.6162b9 | AL-CO-CR-NI | HM_FORM | 298.0 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-GEAL46TYRL.c8a88f | AL-CO-CR-NI | HM_FORM | 298.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-GEKREDAI23 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-GFVKETY64Q | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-GJY57XUCBP | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-HJBML33MP4 | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-HRT7A33QUN | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-I5JKIVXLI4 | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-IAB2LXFNOY.55268e | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-IAB2LXFNOY.62a949 | AL-CO-CR-NI | HM_FORM | 298.15 | CoAl (B2) | phase_label_not_mapped | label 'CoAl (B2)' |
| ORC-KO4O6TOD2C.48eff7 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-KO4O6TOD2C.73cada | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-KO4O6TOD2C.cb06e3 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-LOZBGVYVAU.2e0361 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-LOZBGVYVAU.4ec080 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-LOZBGVYVAU.895373 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-M2X72TAQEQ.0c03a2 | AL-CO-CR-NI | SM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-M2X72TAQEQ.114efe | AL-CO-CR-NI | GM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-M2X72TAQEQ.2c7755 | AL-CO-CR-NI | SM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-M2X72TAQEQ.387a00 | AL-CO-CR-NI | GM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-M2X72TAQEQ.8a1e5a | AL-CO-CR-NI | GM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-M2X72TAQEQ.aca4b7 | AL-CO-CR-NI | GM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-M2X72TAQEQ.ad4d3f | AL-CO-CR-NI | GM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-M2X72TAQEQ.b8e202 | AL-CO-CR-NI | HM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-M2X72TAQEQ.c95868 | AL-CO-CR-NI | HM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-M2X72TAQEQ.d019cc | AL-CO-CR-NI | GM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-M2X72TAQEQ.ecef70 | AL-CO-CR-NI | GM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-M2X72TAQEQ.fc7f7b | AL-CO-CR-NI | GM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-M7BUHEGWBV | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-MIQXBA63Y6 | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-MRYCPD3MGU | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-MZSAEGOTBR | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-NLD4Z6JLS6 | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-NNQH4SF765 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-OS5IVTXPX6 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-P4ZSEXFBEG | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-PWPIZMRW2O | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-QL67TSGS6J | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-R4JVCNQOUL.88a673 | AL-CO-CR-NI | HM_FORM | 0.0 | B2-β | phase_label_not_mapped | label 'B2-β' |
| ORC-R4JVCNQOUL.d14830 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-RBFFWS6ZQH.85819f | AL-CO-CR-NI | HM_FORM | 298.0 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-RBFFWS6ZQH.8da9a7 | AL-CO-CR-NI | HM_FORM | 298.0 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-RNMZLTA3EG | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-RUQIJPW7LX | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-S77VZEGXQ3 | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-SHRYIPOXBJ | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-T4USAJZHMV | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-TJ27BEONTE.3fade8 | AL-CO-CR-NI | HM_FORM | 0.0 | B2-β | phase_label_not_mapped | label 'B2-β' |
| ORC-TJ27BEONTE.492673 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-TLQAOJDQI2 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-TVEF5FPR33.0f9888 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-TVEF5FPR33.1e3809 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-TVEF5FPR33.27003d | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-UDK532NRBY.74c81e | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-UDK532NRBY.7eb3d3 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-UDK532NRBY.adad6e | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-UHOV5ETA3J | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-UWBYNJLERZ | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-VKJQHODF5T.6af9f4 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-VKJQHODF5T.d051e4 | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-VKJQHODF5T.d1c4e1 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-VTB72Y5OXM.0759bb | AL-CO-CR-NI | HM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-VTB72Y5OXM.1bf611 | AL-CO-CR-NI | HM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-VTB72Y5OXM.41a8b4 | AL-CO-CR-NI | HM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-VTB72Y5OXM.690228 | AL-CO-CR-NI | HM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-VTB72Y5OXM.6dd106 | AL-CO-CR-NI | HM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-VTB72Y5OXM.6feba1 | AL-CO-CR-NI | HM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-VTB72Y5OXM.71c30c | AL-CO-CR-NI | HM_FORM | 298.15 | Ni3Al (γ'-L12) | phase_label_not_mapped | label "Ni3Al (γ'-L12)" |
| ORC-VTB72Y5OXM.d37d98 | AL-CO-CR-NI | HM_FORM | 298.15 | γ'-L12 | phase_label_not_mapped | label "γ'-L12" |
| ORC-VUZ7SP4VUX | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-WSKLBJ7O6R | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-WT7PXP52PW | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-X7EHOUKTPD | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-XMHR27DSFK | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-XYCE5GPHM6 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-YFI3VYJ3UQ | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-YNUBAUOYL6 | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-Z6W4NXL7QJ.2614d7 | AL-CO-CR-NI | HM_FORM | 0.0 | L12-γ’ | phase_label_not_mapped | label 'L12-γ’' |
| ORC-Z6W4NXL7QJ.80139e | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-Z6W4NXL7QJ.e093bd | AL-CO-CR-NI | HM_FORM | 0.0 | γ' | phase_label_not_mapped | label "γ'" |
| ORC-Z7PJJFOXX3 | AL-CO-CR-NI | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZDUO6PKZ3H | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-ZE6LY3IVHZ | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-ZMIZRHWGHR | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-ZOPMVSLEXO.0e91fe | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZOPMVSLEXO.47e6a8 | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZOPMVSLEXO.799248 | AL-CO-CR-NI | HM_FORM | 298.15 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-ZOPMVSLEXO.8d90bb | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZOPMVSLEXO.b07d0a | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZOPMVSLEXO.b7b39d | AL-CO-CR-NI | HM_FORM | 298.15 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-ZOPMVSLEXO.bce74c | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZOPMVSLEXO.cf2f53 | AL-CO-CR-NI | HM_FORM | 298.15 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-ZOPMVSLEXO.e779fd | AL-CO-CR-NI | HM_FORM | 298.15 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-ZOPMVSLEXO.e80675 | AL-CO-CR-NI | HM_FORM | 298.15 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ZOPMVSLEXO.ef07bb | AL-CO-CR-NI | HM_FORM | 298.15 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-ZOPMVSLEXO.f476c0 | AL-CO-CR-NI | HM_FORM | 298.15 | NiAl (B2) | phase_label_not_mapped | label 'NiAl (B2)' |
| ORC-ZRJTZFU5YP | AL-CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-PDPECKEWAL.dcee83 | AL-CR | HM_FORM | 1273.15 | Al9Cr4 (l) | phase_label_not_mapped | label 'Al9Cr4 (l)' |
| ORC-X2WBMXYDLJ | AL-LA | HM_FORM | 0.0 | Al | phase_label_not_mapped | label 'Al' |
| ORC-5N5TJPYRTK.a04419 | AL-MG | HM_FORM | 0.0 | Al2Mg-C15 | phase_label_not_mapped | label 'Al2Mg-C15' |
| ORC-RNUDMKJN4F.a61040 | AL-MG | HM_FORM | 0.0 | Al2Mg-C36 | phase_label_not_mapped | label 'Al2Mg-C36' |
| ORC-YZTJPJLSUX.2fae14 | AL-MG | HM_FORM | 0.0 | Al2Mg-C14 | phase_label_not_mapped | label 'Al2Mg-C14' |
| ORC-GW6JIXCRKE.98752e | AL-MN | HM_FORM | 298.15 | Al8Mn5(b) | phase_label_not_mapped | label 'Al8Mn5(b)' |
| ORC-73AFUKLQWD.19ba40 | AL-NI-PT | HM_FORM | 0.0 | L10 | phase_label_not_mapped | label 'L10' |
| ORC-C2W3AMCQSL.64b0a5 | AL-NI-PT | HM_FORM | 0.0 | L10 | phase_label_not_mapped | label 'L10' |
| ORC-PB5REKFWHW.351d43 | AL-NI-PT | HM_FORM | 0.0 | L10 | phase_label_not_mapped | label 'L10' |
| ORC-BCJLH5QZP3.d8e17e | AL-NI-Y | HM_FORM | 298.15 | τ7 NiAl2Y | phase_label_not_mapped | label 'τ7 NiAl2Y' |
| ORC-ERGDTKCCNO.dbe85d | AL-NI-Y | HM_FORM | 298.15 | τ2 Ni3Al9Y | phase_label_not_mapped | label 'τ2 Ni3Al9Y' |
| ORC-HPNGKBHL7Q.7e48ad | AL-NI-Y | HM_FORM | 298.15 | τ10 Ni6Al2Y3 | phase_label_not_mapped | label 'τ10 Ni6Al2Y3' |
| ORC-PIKWTIFFLT.28e733 | AL-NI-Y | HM_FORM | 298.15 | τ1 Ni6Al23Y4 | phase_label_not_mapped | label 'τ1 Ni6Al23Y4' |
| ORC-QBXP4WN4EH.1119f0 | AL-NI-Y | HM_FORM | 298.15 | τ12 Ni8AlY3 | phase_label_not_mapped | label 'τ12 Ni8AlY3' |
| ORC-RIU6VQODTD.ff9f9c | AL-NI-Y | HM_FORM | 298.15 | τ9 Ni2AlY2 | phase_label_not_mapped | label 'τ9 Ni2AlY2' |
| ORC-SCXLN5PW5J.1fb030 | AL-NI-Y | HM_FORM | 298.15 | τ3 NiAl4Y | phase_label_not_mapped | label 'τ3 NiAl4Y' |
| ORC-UAONAY6USS.6eaf6c | AL-NI-Y | HM_FORM | 298.15 | τ8 NiAlY | phase_label_not_mapped | label 'τ8 NiAlY' |
| ORC-UGHIJTFJXQ.d60bca | AL-NI-Y | HM_FORM | 298.15 | τ6 Ni2Al3Y | phase_label_not_mapped | label 'τ6 Ni2Al3Y' |
| ORC-3HPITLRFFC.237487 | AL-RU | HM_FORM | 298.15 | RuAl | phase_label_not_mapped | label 'RuAl' |
| ORC-2R3RSFLVML | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-ANTPBC2LYC | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-BLE5GGHL7A | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-FFQKM5UWR6 | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-PHBWW54AYA | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-QCFMJ36AAG | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-SVJTYZQSOO | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-YWMCF3MY3L | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-HV5YWBUZLU.7c0cf1 | AU-HO-TM | HM_FORM | 298.0 | αAuHo | phase_label_not_mapped | label 'αAuHo' |
| ORC-3LPA54QJQD | B-MG | HM_FORM | 298.15 | MgB6 | phase_label_not_mapped | label 'MgB6' |
| ORC-7PI7ACDB6X | B-MG | HM_FORM | 298.15 | MgB12 | phase_label_not_mapped | label 'MgB12' |
| ORC-KIP2CJSBMK | B-MG | HM_FORM | 298.15 | MgB6 | phase_label_not_mapped | label 'MgB6' |
| ORC-N2BPBLFSN3 | B-MG | HM_FORM | 298.15 | Mg2B | phase_label_not_mapped | label 'Mg2B' |
| ORC-TDP6IBGSN3 | B-MG | HM_FORM | 298.15 | Mg4B | phase_label_not_mapped | label 'Mg4B' |
| ORC-5VUGUVM3S2 | B-U | CPM | 348.31 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-C6N5EOAVSR | B-U | CPM | 320.84 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-F6SG6DC6YS | B-U | CPM | 340.91 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-ID2CY4V6EX | B-U | CPM | 310.6 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-SX6ETL5J4Y | B-U | CPM | 300.4 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-XK3PPBGLE7 | B-U | CPM | 298.15 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-ZDI62FNVY5 | B-U | CPM | 330.94 | B2U | phase_label_not_mapped | label 'B2U' |
| ORC-S3QCHLIENU | BI-ER-TE | HM_FORM | 0.0 | ErTe2 | phase_label_not_mapped | label 'ErTe2' |
| ORC-J2S6FP3OPD.12abf9 | C-MN | HM_FORM | 298.15 | MnCa | phase_label_not_mapped | label 'MnCa' |
| ORC-NB2ABT2NJP.1a66e9 | C-MN | HM_FORM | 298.15 | Mn2C | phase_label_not_mapped | label 'Mn2C' |
| ORC-NB2ABT2NJP.e70760 | C-MN | HM_FORM | 298.15 | Mn2Cb | phase_label_not_mapped | label 'Mn2Cb' |
| ORC-5P2WKOP3S6 | C-NB | HM_FORM | 0.0 | Nb3C | phase_label_not_mapped | label 'Nb3C' |
| ORC-BDWBO3XXDG | C-NB | HM_FORM | 0.0 | Nb7C3 | phase_label_not_mapped | label 'Nb7C3' |
| ORC-YX7DW62EWY | C-NB | HM_FORM | 0.0 | Nb5C2 | phase_label_not_mapped | label 'Nb5C2' |
| ORC-24U66SUY3P.8ca50f | C-PU | CPM | 298.15 | C₀.₈₂Pu | phase_label_not_mapped | label 'C₀.₈₂Pu' |
| ORC-2TJONUSJBC.80f06f | C-PU | SM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-2TJONUSJBC.81481c | C-PU | CPM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-4ZUW262ENE.4af561 | C-PU | CPM | 298.15 | C₀.₈₇Pu | phase_label_not_mapped | label 'C₀.₈₇Pu' |
| ORC-ICTO4YCG3I.755cf3 | C-PU | SM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-ICTO4YCG3I.be37c6 | C-PU | CPM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-3E7T6VEXR2 | C-SI-Y | HM_FORM | 0.0 | Y3Si5 (R) | phase_label_not_mapped | label 'Y3Si5 (R)' |
| ORC-3F4IKD7X5A | C-SI-Y | HM_FORM | 0.0 | Y5Si4 | phase_label_not_mapped | label 'Y5Si4' |
| ORC-3KKWBH2XDZ.b64d86 | C-SI-Y | HM_FORM | 298.15 | Y5Si4 | phase_label_not_mapped | label 'Y5Si4' |
| ORC-3KKWBH2XDZ.b73182 | C-SI-Y | SM_FORM | 298.15 | Y5Si4 | phase_label_not_mapped | label 'Y5Si4' |
| ORC-4GRDKBOGIM.4fa341 | C-SI-Y | HM_FORM | 298.15 | YSi2 | phase_label_not_mapped | label 'YSi2' |
| ORC-4OKQZZFQ5L | C-SI-Y | HM_FORM | 0.0 | YC2 | phase_label_not_mapped | label 'YC2' |
| ORC-5J5H3KGZYE.5184e3 | C-SI-Y | HM_FORM | 298.15 | YC2 | phase_label_not_mapped | label 'YC2' |
| ORC-6S6FJDBDPS.361c7d | C-SI-Y | HM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-6S6FJDBDPS.5c9f32 | C-SI-Y | SM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-AYWJZHYTRS.aeb0ce | C-SI-Y | HM_FORM | 298.15 | YSi | phase_label_not_mapped | label 'YSi' |
| ORC-AYWJZHYTRS.b60942 | C-SI-Y | SM_FORM | 298.15 | YSi | phase_label_not_mapped | label 'YSi' |
| ORC-BFAMJ2DIA5.917539 | C-SI-Y | HM_FORM | 298.15 | Y3Si5 | phase_label_not_mapped | label 'Y3Si5' |
| ORC-BFAMJ2DIA5.f3bc8b | C-SI-Y | SM_FORM | 298.15 | Y3Si5 | phase_label_not_mapped | label 'Y3Si5' |
| ORC-BUO7XSPB2I | C-SI-Y | HM_FORM | 0.0 | Y3Si2C2 | phase_label_not_mapped | label 'Y3Si2C2' |
| ORC-BXE4DG4MGE | C-SI-Y | HM_FORM | 0.0 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-DI7K5WNBQD.9f1700 | C-SI-Y | HM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-DSMEXZLUVF.79fcd5 | C-SI-Y | HM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-FFDZZDXLP6 | C-SI-Y | HM_FORM | 0.0 | Y15Si9C | phase_label_not_mapped | label 'Y15Si9C' |
| ORC-HXREVNZHBF | C-SI-Y | HM_FORM | 0.0 | YSi | phase_label_not_mapped | label 'YSi' |
| ORC-IGXZ3PKXEP | C-SI-Y | HM_FORM | 0.0 | Y1.8Si0.2C2.7 | phase_label_not_mapped | label 'Y1.8Si0.2C2.7' |
| ORC-K47LECRQ4P | C-SI-Y | HM_FORM | 0.0 | YSi2 (H) | phase_label_not_mapped | label 'YSi2 (H)' |
| ORC-M5W5YRWCXR.cc9321 | C-SI-Y | HM_FORM | 298.15 | YSi | phase_label_not_mapped | label 'YSi' |
| ORC-MV6VDIBSCZ | C-SI-Y | HM_FORM | 0.0 | Y2C3 (R) | phase_label_not_mapped | label 'Y2C3 (R)' |
| ORC-PXWJTJAKXJ | C-SI-Y | HM_FORM | 0.0 | YSi2 (R) | phase_label_not_mapped | label 'YSi2 (R)' |
| ORC-RHK3CZSOYD.f4ddb9 | C-SI-Y | HM_FORM | 298.15 | YC2 | phase_label_not_mapped | label 'YC2' |
| ORC-URIPMRCZ3I.8cc05d | C-SI-Y | HM_FORM | 298.15 | YSi2 | phase_label_not_mapped | label 'YSi2' |
| ORC-URIPMRCZ3I.d59230 | C-SI-Y | SM_FORM | 298.15 | YSi2 | phase_label_not_mapped | label 'YSi2' |
| ORC-W37THFZ6PU.4c9892 | C-SI-Y | HM_FORM | 298.15 | YC2 | phase_label_not_mapped | label 'YC2' |
| ORC-XAWUXWICRX | C-SI-Y | HM_FORM | 0.0 | Y3Si5 (H) | phase_label_not_mapped | label 'Y3Si5 (H)' |
| ORC-ZQPMERZ45A.425703 | C-SI-Y | HM_FORM | 298.15 | YC2 | phase_label_not_mapped | label 'YC2' |
| ORC-23LMFZEDJ3.b8462d | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-23LMFZEDJ3.e74a63 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-23ZIGYN2CV.7c099c | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-23ZIGYN2CV.7ebd39 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-242GA7RIKL.112092 | C-U | SM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-242GA7RIKL.80d20a | C-U | SM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-2D5S4G5EI4.e27a79 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-2EKKOMMM6P.6d27c7 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-2GHVHLBELH.318ec9 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-2HLE6UO57R.313321 | C-U | CPM | 2393.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-33GIIPQBST.42a541 | C-U | CPM | 1878.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-35WTM76WD5.0b8b03 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-35WTM76WD5.5dd804 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-3RZ6TU34RS.1137ac | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-3RZ6TU34RS.cc2905 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-47ONJBEWJ2.a6fe81 | C-U | CPM | 2086.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-4CFQMJELGT.2ff41b | C-U | CPM | 2016.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-5NWPLLHV2M.31e06b | C-U | CPM | 2200.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-5UIZAXQC3L.2a2fb9 | C-U | CPM | 2500.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-5UIZAXQC3L.8f8efb | C-U | SM | 2500.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-5UIZAXQC3L.924daf | C-U | CPM | 2500.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-5UIZAXQC3L.d895e6 | C-U | SM | 2500.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-6RITSJBAJZ.3e3d91 | C-U | CPM | 1689.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-6S64DRZH3J.3522d3 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-7HC4TSOM3T.353f05 | C-U | CPM | 1300.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-7HC4TSOM3T.3b50fb | C-U | SM | 1300.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-7HC4TSOM3T.ba5223 | C-U | SM | 1300.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-7HC4TSOM3T.c203e3 | C-U | CPM | 1300.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-7KVA7TIPRJ.496333 | C-U | CPM | 2300.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-7NYE2G6FHN.acbd39 | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-7NYE2G6FHN.eb35fa | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-7R46RRKEII.73ca96 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-7WUCDPAEKW.41207d | C-U | SM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-7WUCDPAEKW.83bfaa | C-U | SM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-AMBA2N3OEV.0a0b35 | C-U | CPM | 2021.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-ASKM5EDP34.8598fe | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-ASKM5EDP34.8fa1f1 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-AUIGU4S7VE.2b76ff | C-U | CPM | 900.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-AUIGU4S7VE.4886cd | C-U | SM | 900.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-AUIGU4S7VE.55d6e6 | C-U | CPM | 900.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-AUIGU4S7VE.ca32e4 | C-U | SM | 900.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-AXZOODW34P.0f22dc | C-U | CPM | 1300.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-B67LEUD767.24c645 | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-B67LEUD767.635a04 | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-BA4U3STZDG.0f65b8 | C-U | CPM | 1900.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-BGLQZKVJ3B.1e09f7 | C-U | SM | 1700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-BGLQZKVJ3B.617ffe | C-U | CPM | 1700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-BGLQZKVJ3B.9b8228 | C-U | SM | 1700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-BGLQZKVJ3B.e6a57f | C-U | CPM | 1700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-BJB7UAJ4FW.1de5fc | C-U | SM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-BJB7UAJ4FW.9e14c1 | C-U | SM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-BNLQRWAFZA.a595c8 | C-U | CPM | 2000.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-BO7VM5FH4F.0b54c2 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-C3JCZQJ27X.de19c3 | C-U | CPM | 1000.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-CVTNZ7W4CW.36702a | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-DLPIODCAG2.125005 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-DLPIODCAG2.d57aee | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-E5HDC2FLZT.203df8 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-ERCRJRRYFQ.19fa3b | C-U | SM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-ERCRJRRYFQ.6059fe | C-U | SM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-ERUUNHKLGD.64cfa7 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-ES37M7DMUN.b78494 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-FCF7WKQFEH.470641 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-FCF7WKQFEH.f6f8d2 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-FF63YFFYO3.45ee3a | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-FF63YFFYO3.b8001b | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-FQQ72T5BVR.1c87a1 | C-U | SM | 1100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-FQQ72T5BVR.21ff0d | C-U | SM | 1100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-FQQ72T5BVR.5f4e2c | C-U | CPM | 1100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-FQQ72T5BVR.a31510 | C-U | CPM | 1100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-FTQTR7ALWZ.02b0d4 | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-FTQTR7ALWZ.135171 | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-FV55AJCSM7.aaa5b0 | C-U | CPM | 2277.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-GHYX64I4DB.ba7abb | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-GHYX64I4DB.ef723e | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-GLBOSZMY2N.c68743 | C-U | CPM | 2600.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-HRMZYM7VPM.700fbe | C-U | CPM | 1800.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-I4XPE6VQ6O.e57e1f | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-I4XPE6VQ6O.fe9113 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-IDV2HJJECD.0560a2 | C-U | SM | 2700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-IDV2HJJECD.733ce7 | C-U | CPM | 2700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-IDV2HJJECD.bc073e | C-U | CPM | 2700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-IFVF5O65HA.7601ad | C-U | SM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-IFVF5O65HA.b43fd6 | C-U | SM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-IQKO6FH2Q3.7fe11f | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-IQKO6FH2Q3.8b87bf | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-IRAA2SNWE5.cd1c77 | C-U | CPM | 2800.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-IT2MHOE4W4.887ab0 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-JBX7HQDS7G.48afb6 | C-U | CPM | 2400.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-JEPXUPFBD7.dea7af | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-JEPXUPFBD7.fe4138 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-JMWXRWYCEH.350576 | C-U | CPM | 2581.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-JPXGWKLMR5.6405f9 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-JRXWAA3IRP.fc8bf0 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-JT4YWMQ7GU.a06b05 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-K64YEXIHRW.95596f | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-K64YEXIHRW.a75974 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-KFBOAZXLU2.d3e191 | C-U | CPM | 1500.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-KISHC7YH3P.1ce44a | C-U | CPM | 2300.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KISHC7YH3P.1eb510 | C-U | SM | 2300.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KISHC7YH3P.2e23a9 | C-U | SM | 2300.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KISHC7YH3P.b9846d | C-U | CPM | 2300.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KJAT56SYAN.06bb1b | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-KJAT56SYAN.8478bf | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-KNYQSCZWFT.11a862 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-KNYQSCZWFT.b18900 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-KOAT4GY3FO.2445a8 | C-U | SM | 700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KOAT4GY3FO.4545b9 | C-U | SM | 700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KOAT4GY3FO.9a68a6 | C-U | CPM | 700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KOAT4GY3FO.c6474f | C-U | CPM | 700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KPJGMBKYYD.d487e9 | C-U | CPM | 2081.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-KXWIXRF7I6.b1f9ef | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-L4EOA2SNCV.a9c9ea | C-U | HM_FORM | 298.0 | C0.600U0.400 | phase_label_not_mapped | label 'C0.600U0.400' |
| ORC-LFAO5SSXMK.234b29 | C-U | SM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-LFAO5SSXMK.be0345 | C-U | SM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-LRPJNWXWY5.def10a | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-LRPJNWXWY5.e8ad5b | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-LSSFSIWPPD.4155ca | C-U | CPM | 900.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-LV4SGXSJXS.c02e76 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-LV4SGXSJXS.c70eb3 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-LWYUALS5RO.8cd5ea | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-LWYUALS5RO.bea7f0 | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-MNSGFN7TUF.62673d | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-MNSGFN7TUF.bcaf6e | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-MRZIID7CXJ.1ae8ce | C-U | CPM | 1587.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-MS3CBROHJH.4fbc53 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-MS3CBROHJH.5353b8 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-MTKWY57AVO.10c9ca | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-MTKWY57AVO.5be157 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-MUHBNJIVW3.707150 | C-U | CPM | 2500.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-N3WRTWYLYG.53767b | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-N3WRTWYLYG.c35e87 | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-N5YTMMR3NQ.a08881 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-N5YTMMR3NQ.ed91bf | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-O56OVTZ7KS.3c6ad0 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-O5VIMRM6X4.0e7d4b | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-O5VIMRM6X4.55aa73 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-O7DR3NZX3M.b72d9c | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-OBDHR3TCXP.36f004 | C-U | CPM | 1484.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-OIY4EEX2ZX.3024a9 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-OYSX326MRK.700a2f | C-U | SM | 298.0 | C0.600U0.400 | phase_label_not_mapped | label 'C0.600U0.400' |
| ORC-OZSIMP67VN.9c5fc2 | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-OZSIMP67VN.b5aa7e | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-P33O5JHCBK.cd3443 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-P43WX2TIGN.28230e | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-P43WX2TIGN.e82059 | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-PCEUZHWZY7.5cdbb8 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-QJSGS6MCWV.40b6d7 | C-U | CPM | 1100.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-QNLMTGUXXD.901fd5 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-QQIEZQENJI.1f384e | C-U | SM | 2038.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-QQIEZQENJI.71a836 | C-U | CPM | 2038.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-QS2KNZFWMZ.ec20d3 | C-U | CPM | 2483.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-QZSYJRMFIN.794f2e | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-R52GGL2JEK.03cd08 | C-U | SM | 500.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-R52GGL2JEK.46478a | C-U | CPM | 500.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-R52GGL2JEK.afd5ac | C-U | SM | 500.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-R52GGL2JEK.c04d42 | C-U | CPM | 500.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RARAKZATTG.6e9660 | C-U | CPM | 2038.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RARAKZATTG.afb9f7 | C-U | SM | 2038.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RCN7VNES7I.5820e9 | C-U | CPM | 298.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-RCN7VNES7I.8e1a3a | C-U | SM | 298.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RCN7VNES7I.aca4c8 | C-U | CPM | 298.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RCN7VNES7I.b50b63 | C-U | SM | 298.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-RR5E2GXHHR.a73a52 | C-U | SM | 2823.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-RR5E2GXHHR.f7fd0d | C-U | CPM | 2823.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-RUMWCHNNFN.ccc741 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-RXAWUFODBQ.c8cd08 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-RXRF5YYKI2.5eefab | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-SDR3RG5JRW.9c3703 | C-U | CPM | 2100.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-SZI2ZFQWIT.0efb6f | C-U | SM | 1500.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-SZI2ZFQWIT.5d58fd | C-U | SM | 1500.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-SZI2ZFQWIT.a19cd2 | C-U | CPM | 1500.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-SZI2ZFQWIT.a59f2f | C-U | CPM | 1500.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-T7MNBZZVXK.2b6e43 | C-U | HM_FORM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-T7MNBZZVXK.3f37c8 | C-U | HM_FORM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-TEEZ6BI35F.284b3a | C-U | SM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-TEEZ6BI35F.d8f82b | C-U | SM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-TILXAUAOFV.4b9521 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-TQAI7JI233.681089 | C-U | SM | 298.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-TQAI7JI233.b1f192 | C-U | SM | 298.0 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-U2FVIYX4LQ.1c24c1 | C-U | SM | 2800.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-U2FVIYX4LQ.84fb4f | C-U | CPM | 2800.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-U4A6PGMXIO.13e647 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-U7PC23R5WQ.7f3d32 | C-U | CPM | 1200.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-UNOU4VZYYJ.08ffe6 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-UNOU4VZYYJ.86604e | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-UQQOVF2DGH.af465e | C-U | CPM | 1490.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-UVTDLRXYEZ.77aa87 | C-U | CPM | 2213.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-V5HTCHAXS3.970e9d | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-V5HTCHAXS3.f6db42 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-V6DLUQK6M5.d5abc5 | C-U | CPM | 1700.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-VCL6LMCTP7.61c7ac | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-VCL6LMCTP7.bb4335 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-VDPK37734P.2e33e0 | C-U | SM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-VDPK37734P.95297c | C-U | SM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-WDZEJ6KIOW.7378d7 | C-U | CPM | 1600.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-X6FNNMPFMR.5199ec | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-X6FNNMPFMR.a7d252 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-X6FQXSGJHQ.3a6d75 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-X6FQXSGJHQ.b2b226 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-XGUHSXJE72.368816 | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-XGUHSXJE72.8e66e3 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-XJ75CNS7EI.37e936 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-XPCVX2GVQA.4c8015 | C-U | HM_FORM | 298.0 | C0.600U0.400 | phase_label_not_mapped | label 'C0.600U0.400' |
| ORC-XPXBHUS5OY.a832da | C-U | SM | 298.15 | UC1.9 (U0.345C0.655) | phase_label_not_mapped | label 'UC1.9 (U0.345C0.655)' |
| ORC-XPXBHUS5OY.ff5c08 | C-U | SM | 298.15 | UC1.9 | phase_label_not_mapped | label 'UC1.9' |
| ORC-XRQGUG57XK.61c146 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-XS7NDN5RPG.681976 | C-U | SM | 1900.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-XS7NDN5RPG.ac7179 | C-U | SM | 1900.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-XS7NDN5RPG.d1d832 | C-U | CPM | 1900.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-XS7NDN5RPG.db20f2 | C-U | CPM | 1900.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-YCHQNZYXKU.a54b21 | C-U | CPM | 700.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-YJYDDSN6UR.c1e671 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-YNTMMRGIXG.f8db02 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-YNUXUOK4LI.29cfc7 | C-U | CPM | 1794.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-YQIUKCZIML.290028 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-YR6GSXQZOM.7dfeaf | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-YR6GSXQZOM.b7a12f | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-Z64QWWQJ3A.ba938b | C-U | CPM | 1400.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-Z7I2LHDDPD.55ad90 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-ZDYH7IJLFP.48de5c | C-U | SM | 298.0 | C0.600U0.400 | phase_label_not_mapped | label 'C0.600U0.400' |
| ORC-ZJQCPK4WVI.0b386a | C-U | CPM | 2100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-ZJQCPK4WVI.0f82e6 | C-U | CPM | 2100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-ZJQCPK4WVI.7178fc | C-U | SM | 2100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-ZJQCPK4WVI.ef7d05 | C-U | SM | 2100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-ZS6L6RA7WP.0a4ae6 | C-U | CPM | 2700.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-ZT5QUPW7FY.270847 | C-U | CPM | 800.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-ZZ6XETLP3U.623533 | C-U | HM_FORM | 298.0 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-ZZ6XETLP3U.f8f921 | C-U | HM_FORM | 298.0 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-D5OBI4CF5M | CA-IN-SB | HM_FORM | 0.0 | Ca5Sb3 | phase_label_not_mapped | label 'Ca5Sb3' |
| ORC-JMPRIJBETK.134036 | CA-IN-SB | HM_FORM | 1078.0 | Ca5Sb3 | phase_label_not_mapped | label 'Ca5Sb3' |
| ORC-PQUJF6BZJW | CA-IN-SB | HM_FORM | 0.0 | Ca2Sb | phase_label_not_mapped | label 'Ca2Sb' |
| ORC-TLXXDM6ZUO | CA-IN-SB | HM_FORM | 0.0 | CaSb2 | phase_label_not_mapped | label 'CaSb2' |
| ORC-377G72NYL5.16f26c | CE-GA | HM_FORM | 298.15 | Ce0.21Ga0.79 | phase_label_not_mapped | label 'Ce0.21Ga0.79' |
| ORC-KVCKXHNYOJ.35506d | CE-GA | HM_FORM | 298.15 | CeGa2 with x(Ga) = 0.79 at.% Ga | phase_label_not_mapped | label 'CeGa2 with x(Ga) = 0.79 at.% Ga' |
| ORC-P74KIVIPMK.138e01 | CE-GA | HM_FORM | 298.15 | Ce0.21Ga0.79 | phase_label_not_mapped | label 'Ce0.21Ga0.79' |
| ORC-2J4IQSP6P5.455370 | CR-GE | GM_FORM | 1530.0 | Cr0.63Ge0.37 | phase_label_not_mapped | label 'Cr0.63Ge0.37' |
| ORC-5DSEUH4NK2.4030f3 | CR-GE | GM_FORM | 1530.0 | Cr0.75Ge0.25 | phase_label_not_mapped | label 'Cr0.75Ge0.25' |
| ORC-D4GO4RDBQ3.0b66ef | CR-GE | GM_FORM | 1530.0 | Cr0.8Ge0.2 | phase_label_not_mapped | label 'Cr0.8Ge0.2' |
| ORC-D6O6WD7FEM.41ccc1 | CR-GE | GM_FORM | 1530.0 | Cr0.8Ge0.2 | phase_label_not_mapped | label 'Cr0.8Ge0.2' |
| ORC-SHBHPLOWRZ.b6ec88 | CR-GE | GM_FORM | 1530.0 | Cr0.75Ge0.25 | phase_label_not_mapped | label 'Cr0.75Ge0.25' |
| ORC-SQKDM2MIIO.7c252f | CR-GE | GM_FORM | 1530.0 | Cr0.8Ge0.2 | phase_label_not_mapped | label 'Cr0.8Ge0.2' |
| ORC-ZDS7SVJW37.6c99b2 | CR-GE | GM_FORM | 1530.0 | Cr0.75Ge0.25 | phase_label_not_mapped | label 'Cr0.75Ge0.25' |
| ORC-GQNFWJEWL3.467cc7 | CR-NB | ACR_CR | 1472.0 | C15 Cr2Nb + (Nb) | phase_label_not_mapped | label 'C15 Cr2Nb + (Nb)' |
| ORC-ZKE56KTRWC.a2311b | CR-NB | ACR_CR | 1472.0 | C15 Cr2Nb + (Nb) | phase_label_not_mapped | label 'C15 Cr2Nb + (Nb)' |
| ORC-2DC2JED7OP.95d3f8 | CR-RE | HM_FORM | 0.0 | sigma CrReCrReRe | phase_label_not_mapped | label 'sigma CrReCrReRe' |
| ORC-2DC2JED7OP.adf266 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-2G5X7WUZNV.3b5553 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-2G5X7WUZNV.f3ad86 | CR-RE | HM_FORM | 0.0 | sigma CrReCrCrCr | phase_label_not_mapped | label 'sigma CrReCrCrCr' |
| ORC-3BBKXWFDLX.9b2614 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-3BBKXWFDLX.db9632 | CR-RE | HM_FORM | 0.0 | sigma ReCrCrReRe | phase_label_not_mapped | label 'sigma ReCrCrReRe' |
| ORC-3SL7ENTGNY.3e7c35 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-3SL7ENTGNY.4a82b7 | CR-RE | HM_FORM | 0.0 | sigma ReReReReRe | phase_label_not_mapped | label 'sigma ReReReReRe' |
| ORC-6C6U4O32PW.5e7bac | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-6C6U4O32PW.7a5458 | CR-RE | HM_FORM | 0.0 | sigma CrCrCrReCr | phase_label_not_mapped | label 'sigma CrCrCrReCr' |
| ORC-7Q67Y5AAUP.18e762 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-7Q67Y5AAUP.c0b705 | CR-RE | HM_FORM | 0.0 | sigma ReReCrCrRe | phase_label_not_mapped | label 'sigma ReReCrCrRe' |
| ORC-7U3QE7COIV.262b3f | CR-RE | HM_FORM | 0.0 | sigma ReCrCrCrRe | phase_label_not_mapped | label 'sigma ReCrCrCrRe' |
| ORC-7U3QE7COIV.67d82f | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-7V5ZKCLAPY.1099e3 | CR-RE | HM_FORM | 0.0 | sigma CrCrCrCrCr | phase_label_not_mapped | label 'sigma CrCrCrCrCr' |
| ORC-7V5ZKCLAPY.f87588 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-ABAFGO6RFJ.48cd42 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-ABAFGO6RFJ.fb2ccd | CR-RE | HM_FORM | 0.0 | sigma ReCrReReCr | phase_label_not_mapped | label 'sigma ReCrReReCr' |
| ORC-CPDKPV5EPK.65a4bd | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-CPDKPV5EPK.fb522a | CR-RE | HM_FORM | 0.0 | sigma CrCrReCrRe | phase_label_not_mapped | label 'sigma CrCrReCrRe' |
| ORC-ECFNA3MRAU.17b53d | CR-RE | HM_FORM | 0.0 | sigma ReReCrReCr | phase_label_not_mapped | label 'sigma ReReCrReCr' |
| ORC-ECFNA3MRAU.81ba7e | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-ERTEHM4ZHT.1872bb | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-ERTEHM4ZHT.a27526 | CR-RE | HM_FORM | 0.0 | sigma ReReCrCrCr | phase_label_not_mapped | label 'sigma ReReCrCrCr' |
| ORC-G7JPHP6Q3Y.11a3a0 | CR-RE | HM_FORM | 0.0 | sigma ReCrReCrCr | phase_label_not_mapped | label 'sigma ReCrReCrCr' |
| ORC-G7JPHP6Q3Y.e84036 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-HHWZQT4ZRW.389d7e | CR-RE | HM_FORM | 0.0 | sigma CrCrCrReRe | phase_label_not_mapped | label 'sigma CrCrCrReRe' |
| ORC-HHWZQT4ZRW.83b3c8 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-HJCE7FJDVI.a9cde8 | CR-RE | HM_FORM | 0.0 | sigma ReCrReCrRe | phase_label_not_mapped | label 'sigma ReCrReCrRe' |
| ORC-HJCE7FJDVI.b26a3c | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-IUFI6L23AQ.4e3220 | CR-RE | HM_FORM | 0.0 | sigma CrReReCrRe | phase_label_not_mapped | label 'sigma CrReReCrRe' |
| ORC-IUFI6L23AQ.c86c27 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-LYRS4S5UV4.99aa28 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-LYRS4S5UV4.9c501c | CR-RE | HM_FORM | 0.0 | sigma ReCrCrCrCr | phase_label_not_mapped | label 'sigma ReCrCrCrCr' |
| ORC-MTKKNK4CPD.b7e214 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-MTKKNK4CPD.d27d84 | CR-RE | HM_FORM | 0.0 | sigma ReReReCrCr | phase_label_not_mapped | label 'sigma ReReReCrCr' |
| ORC-MWAOBM7KVD.54ca63 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-MWAOBM7KVD.fd6509 | CR-RE | HM_FORM | 0.0 | sigma CrCrReCrCr | phase_label_not_mapped | label 'sigma CrCrReCrCr' |
| ORC-NXV5MZWYVZ.25e91a | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-NXV5MZWYVZ.40e4df | CR-RE | HM_FORM | 0.0 | sigma CrReCrReCr | phase_label_not_mapped | label 'sigma CrReCrReCr' |
| ORC-OUHRIRWERS.0cb1fb | CR-RE | HM_FORM | 0.0 | sigma ReReCrReRe | phase_label_not_mapped | label 'sigma ReReCrReRe' |
| ORC-OUHRIRWERS.9344b3 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-PQJLJRX26T.54fe29 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-PQJLJRX26T.8fc573 | CR-RE | HM_FORM | 0.0 | sigma ReCrCrReCr | phase_label_not_mapped | label 'sigma ReCrCrReCr' |
| ORC-RT5WBW3IRF.b68fc7 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-RT5WBW3IRF.ba4c68 | CR-RE | HM_FORM | 0.0 | sigma CrCrReReCr | phase_label_not_mapped | label 'sigma CrCrReReCr' |
| ORC-SQ3Z2MJJCO.265c77 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-SQ3Z2MJJCO.391690 | CR-RE | HM_FORM | 0.0 | sigma CrCrReReRe | phase_label_not_mapped | label 'sigma CrCrReReRe' |
| ORC-SVCJWLU7O4.425a26 | CR-RE | HM_FORM | 0.0 | sigma CrCrCrCrRe | phase_label_not_mapped | label 'sigma CrCrCrCrRe' |
| ORC-SVCJWLU7O4.c7de4a | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-THGOOTZYOQ.3c07ac | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-THGOOTZYOQ.a5c0dd | CR-RE | HM_FORM | 0.0 | sigma CrReReCrCr | phase_label_not_mapped | label 'sigma CrReReCrCr' |
| ORC-TKEA3B5XJN.323dab | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-TKEA3B5XJN.ffffff | CR-RE | HM_FORM | 0.0 | sigma ReReReCrRe | phase_label_not_mapped | label 'sigma ReReReCrRe' |
| ORC-WCPWMTQK3N.2f50e3 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-WCPWMTQK3N.910b1c | CR-RE | HM_FORM | 0.0 | sigma CrReReReRe | phase_label_not_mapped | label 'sigma CrReReReRe' |
| ORC-XCCOLQZ2PE.1f3f90 | CR-RE | HM_FORM | 0.0 | sigma CrReCrCrRe | phase_label_not_mapped | label 'sigma CrReCrCrRe' |
| ORC-XCCOLQZ2PE.c1fe7b | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-XL547PLTFS.060120 | CR-RE | HM_FORM | 0.0 | sigma ReCrReReRe | phase_label_not_mapped | label 'sigma ReCrReReRe' |
| ORC-XL547PLTFS.d68057 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-XVKAXI6VI3.611a81 | CR-RE | HM_FORM | 0.0 | sigma CrReReReCr | phase_label_not_mapped | label 'sigma CrReReReCr' |
| ORC-XVKAXI6VI3.f23eb3 | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-ZTNMA6TSUQ.418ae0 | CR-RE | HM_FORM | 0.0 | sigma ReReReReCr | phase_label_not_mapped | label 'sigma ReReReReCr' |
| ORC-ZTNMA6TSUQ.4ac90b | CR-RE | HM_FORM | 0.0 | sigma | phase_label_not_mapped | label 'sigma' |
| ORC-FDJUNXIPO3.53d3e9 | CS-MO-O | SM | 298.15 | α-Cs2MoO4 | phase_label_not_mapped | label 'α-Cs2MoO4' |
| ORC-SBRG56PJJC.e589da | CS-MO-O | SM | 298.15 | α-Cs2Mo2O7 | phase_label_not_mapped | label 'α-Cs2Mo2O7' |
| ORC-43ZXOO6TFO.5bfa0b | CS-O | HM_FORM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-43ZXOO6TFO.9a5ff5 | CS-O | SM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-636TFSTTTX.9fd6f2 | CS-O | HM_FORM | 298.15 | CsO2 | phase_label_not_mapped | label 'CsO2' |
| ORC-636TFSTTTX.fadc13 | CS-O | SM | 298.15 | CsO2 | phase_label_not_mapped | label 'CsO2' |
| ORC-FTGB7HG7ZE.3a3f9f | CS-O | SM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-FTGB7HG7ZE.9b3869 | CS-O | HM_FORM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-FTGB7HG7ZE.e76623 | CS-O | CPM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-LF2XK4HKT2.58f977 | CS-O | SM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-LF2XK4HKT2.754378 | CS-O | CPM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-SVOB5GY4NR.1b1e5a | CS-O | CPM | 298.15 | CsO2 | phase_label_not_mapped | label 'CsO2' |
| ORC-SVOB5GY4NR.a00d38 | CS-O | HM_FORM | 298.15 | CsO2 | phase_label_not_mapped | label 'CsO2' |
| ORC-SVOB5GY4NR.a974c5 | CS-O | SM | 298.15 | CsO2 | phase_label_not_mapped | label 'CsO2' |
| ORC-VICVK7W5MI.4eb1cb | CS-O | HM_FORM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-VICVK7W5MI.87e1e2 | CS-O | SM | 298.15 | Cs2O | phase_label_not_mapped | label 'Cs2O' |
| ORC-43XXWNSX7A.90f41f | CU-HF | HM_FORM | 0.0 | Cu54Hf14 | phase_label_not_mapped | label 'Cu54Hf14' |
| ORC-CSUTXAAKBW.5d83f6 | CU-HF | HM_FORM | 0.0 | Cu54Hf14 | phase_label_not_mapped | label 'Cu54Hf14' |
| ORC-2KBA7NMGGX.1f473d | DY-GD-LA-ND-RU | HM_FORM | 0.0 | Nd3Ru | phase_label_not_mapped | label 'Nd3Ru' |
| ORC-GCTRSE5LJP.8a76a6 | DY-GD-LA-ND-RU | HM_FORM | 0.0 | Dy3Ru | phase_label_not_mapped | label 'Dy3Ru' |
| ORC-N2B42IOD2X.1ce4aa | DY-GD-LA-ND-RU | HM_FORM | 0.0 | Nd3Ru | phase_label_not_mapped | label 'Nd3Ru' |
| ORC-O5DYYRMDTC.45de04 | DY-GD-LA-ND-RU | HM_FORM | 0.0 | Dy3Ru | phase_label_not_mapped | label 'Dy3Ru' |
| ORC-2QKXLHGQBF | FE-GD-MO | CPM | 450.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-4AQVX33PV2 | FE-GD-MO | CPM | 600.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-AHZAQMSQKA | FE-GD-MO | CPM | 681.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-F3LMR7C6IR | FE-GD-MO | CPM | 400.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-FJLRGIALAZ | FE-GD-MO | CPM | 320.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-IDDITI6LVF.6e00f0 | FE-GD-MO | CPM | 298.15 | τ | phase_label_not_mapped | label 'τ' |
| ORC-IDDITI6LVF.82ccc0 | FE-GD-MO | SM | 298.15 | τ | phase_label_not_mapped | label 'τ' |
| ORC-L7ACQQIE5N | FE-GD-MO | CPM | 320.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-LIUXLMOIZV | FE-GD-MO | CPM | 756.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-MPEHHAMLNR.9072ad | FE-GD-MO | CPM | 298.15 | τ | phase_label_not_mapped | label 'τ' |
| ORC-MPEHHAMLNR.b5c58b | FE-GD-MO | SM | 298.15 | τ | phase_label_not_mapped | label 'τ' |
| ORC-NQZWZSPMOL | FE-GD-MO | CPM | 769.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-PGJ65AQOLK.be5cfa | FE-GD-MO | SM | 298.15 | τ | phase_label_not_mapped | label 'τ' |
| ORC-PGJ65AQOLK.d41af0 | FE-GD-MO | CPM | 298.15 | τ | phase_label_not_mapped | label 'τ' |
| ORC-WWNO6R2V2L | FE-GD-MO | CPM | 591.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-YVI2HT7DYI | FE-GD-MO | CPM | 591.0 | τ | phase_label_not_mapped | label 'τ' |
| ORC-6IKR5YU54W | FE-MO | CPM | 1000.0 | μ | phase_label_not_mapped | label 'μ' |
| ORC-A4LBLOWYZW | FE-MO | CPM | 800.0 | μ | phase_label_not_mapped | label 'μ' |
| ORC-EBN6Y6M7Y5 | FE-MO | CPM | 900.0 | μ | phase_label_not_mapped | label 'μ' |
| ORC-G4JA4HEZ4T | FE-MO | CPM | 1100.0 | μ | phase_label_not_mapped | label 'μ' |
| ORC-XPGGSZISDA | FE-MO | CPM | 1300.0 | μ | phase_label_not_mapped | label 'μ' |
| ORC-ZYBG4T3PSO | FE-MO | CPM | 1200.0 | μ | phase_label_not_mapped | label 'μ' |
| ORC-BXGGLN5PDE.020c47 | FE-PT | HM_FORM | 0.0 | Fe3Pt | phase_label_not_mapped | label 'Fe3Pt' |
| ORC-BXGGLN5PDE.6608bd | FE-PT | HM_FORM | 0.0 | FePt3 | phase_label_not_mapped | label 'FePt3' |
| ORC-BXGGLN5PDE.db380e | FE-PT | HM_FORM | 0.0 | FePt | phase_label_not_mapped | label 'FePt' |
| ORC-A23QJB2WN2 | FE-TA | HM_FORM | 0.0 | Fe1Ta12 | phase_label_not_mapped | label 'Fe1Ta12' |
| ORC-ADB5HMRQKR | FE-TA | HM_FORM | 0.0 | Fe9Ta4 | phase_label_not_mapped | label 'Fe9Ta4' |
| ORC-HZPR4ESTX6 | FE-TA | HM_FORM | 0.0 | Fe3Ta10 | phase_label_not_mapped | label 'Fe3Ta10' |
| ORC-TDPDNRKB6I | FE-TA | HM_FORM | 0.0 | Fe8Ta5 | phase_label_not_mapped | label 'Fe8Ta5' |
| ORC-U24HI3NZA2 | FE-TA | HM_FORM | 0.0 | Fe2Ta11 | phase_label_not_mapped | label 'Fe2Ta11' |
| ORC-VPO6TJUC6Z | FE-TA | HM_FORM | 0.0 | Ta13 | phase_label_not_mapped | label 'Ta13' |
| ORC-RYYYSEVZSO.c3a675 | FE-TI | HM_FORM | 0.0 | Fe₂Ti | phase_label_not_mapped | label 'Fe₂Ti' |
| ORC-AHPTQWMRMG.81cb95 | FE-ZR | HM_FORM | 1573.15 | Fe23Zr6 + Fe2Zr | phase_label_not_mapped | label 'Fe23Zr6 + Fe2Zr' |
| ORC-VDN6MXRL2P.4d25f4 | FE-ZR | HM_FORM | 1573.15 | Fe23Zr6, γ | phase_label_not_mapped | label 'γ' |
| ORC-VDN6MXRL2P.587aaa | FE-ZR | HM_FORM | 1573.15 | Fe23Zr6 + γ | phase_label_not_mapped | label 'Fe23Zr6 + γ' |
| ORC-YH7G2WPY74.c322d4 | GE-NI | HM_FORM | 0.0 | ε'Ni5Ge3 | phase_label_not_mapped | label "ε'Ni5Ge3" |
| ORC-36JRTTLT2M.c91987 | H-ZR | HM_FORM | 0.0 | δ-ZrH2 | phase_label_not_mapped | label 'δ-ZrH2' |
| ORC-LOEUZNK44H.0d74e1 | MG-SB | HM_FORM | 773.0 | Mg3Sb2 | phase_label_not_mapped | label 'Mg3Sb2' |
| ORC-762YX4YIBD.b779ea | MG-Y | HM_FORM | 298.15 | YMg | phase_label_not_mapped | label 'YMg' |
| ORC-CYC6AI774I.f54d0e | MG-Y | HM_FORM | 298.15 | YMg | phase_label_not_mapped | label 'YMg' |
| ORC-EX4LZX3VS4.3747c8 | MG-Y | HM_FORM | 298.15 | Y5Mg24 | phase_label_not_mapped | label 'Y5Mg24' |
| ORC-QHJH57VUHP.eeea42 | MG-Y | HM_FORM | 298.15 | Y5Mg24 | phase_label_not_mapped | label 'Y5Mg24' |
| ORC-2IE4CVLKVW | MN-O | HM_FORM | 298.0 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-5XFZM5QTXJ | MN-O | HM_FORM | 298.0 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-6MEP3VUEHP | MN-O | HM_FORM | 298.0 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-6YP2G43BAO | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-7LBOS3ZMGS | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-C672B4OYB3 | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-DIT7OPGPC6 | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-ED4AB7EXCW | MN-O | HM_FORM | 298.0 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-FODYDWIRAG | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-FR3Y2JBCSB | MN-O | HM_FORM | 298.0 | Bixbyite (Mn2O3) | phase_label_not_mapped | label 'Bixbyite (Mn2O3)' |
| ORC-IPRFS25TUD | MN-O | HM_FORM | 298.0 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-KWTNDMGT4W | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-LV2XM5E2UV | MN-O | HM_FORM | 298.0 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-NEDTVO5RID | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-PU4GVT75GB | MN-O | HM_FORM | 298.0 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-SCL3HUZ64I | MN-O | HM_FORM | 298.0 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-VH7ZWPJY45 | MN-O | HM_FORM | 298.0 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-VK3JCM3HZI | MN-O | HM_FORM | 298.0 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-VVCEA7QBGW | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-X6UOHCZYKT | MN-O | HM_FORM | 298.0 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-X7TRQ4WAKF | MN-O | HM_FORM | 298.0 | Bixbyite (Mn2O3) | phase_label_not_mapped | label 'Bixbyite (Mn2O3)' |
| ORC-Y3OF7NGIA4 | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-ZEYWTZTVRV | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-7TTNMCTCQJ | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-BQ4ED5A6YV | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-C5DD6ORKOW | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-ETNK6FZWRI | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-LMA2OLIQAJ | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-N4CTFGPF46 | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-NCSRLE3QHL | N-U | SM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-O3CAEECHC5 | N-U | SM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-Q57UMMJQGM | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-T7PRWSYLIO | N-U | SM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-TMDZWZQOW5 | N-U | HM_FORM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-TUA7HPPOZV | N-U | SM | 298.15 | N0.500U0.500(fcc_B1) | phase_label_not_mapped | label 'N0.500U0.500(fcc_B1)' |
| ORC-D53VJ4EBKD.65df80 | N-ZR | HM_FORM | 0.0 | ZrN3 | phase_label_not_mapped | label 'ZrN3' |
| ORC-HHS33ED37A.ee4215 | N-ZR | HM_FORM | 0.0 | ZrN0.5 | phase_label_not_mapped | label 'ZrN0.5' |
| ORC-I5LXTETNSJ.97ec1d | N-ZR | HM_FORM | 0.0 | ZrN0.5 | phase_label_not_mapped | label 'ZrN0.5' |
| ORC-LI75RO5UOF.0e04e4 | N-ZR | HM_FORM | 298.0 | (αZr) | phase_label_not_mapped | label '(αZr)' |
| ORC-LI75RO5UOF.b2865e | N-ZR | HM_FORM | 298.0 | αZr | phase_label_not_mapped | label 'αZr' |
| ORC-MEZEELF2S3.15e327 | N-ZR | HM_FORM | 0.0 | ZrN3 | phase_label_not_mapped | label 'ZrN3' |
| ORC-TDKQYWMQ63.00a265 | N-ZR | HM_FORM | 298.0 | αZr | phase_label_not_mapped | label 'αZr' |
| ORC-TDKQYWMQ63.42461c | N-ZR | HM_FORM | 298.0 | (αZr) | phase_label_not_mapped | label '(αZr)' |
| ORC-36VRI4S3TK.19086d | NA-O-U | CPM | 298.15 | β-Na2UO4 | phase_label_not_mapped | label 'β-Na2UO4' |
| ORC-36VRI4S3TK.a2a4b7 | NA-O-U | SM | 298.15 | β-Na2UO4 | phase_label_not_mapped | label 'β-Na2UO4' |
| ORC-B2U7BMSEFS.327693 | NA-O-U | CPM | 298.15 | β-Na2U2O7 | phase_label_not_mapped | label 'β-Na2U2O7' |
| ORC-B2U7BMSEFS.85759c | NA-O-U | SM | 298.15 | β-Na2U2O7 | phase_label_not_mapped | label 'β-Na2U2O7' |
| ORC-E7RN5GEMPQ.183f2c | NA-O-U | CPM | 298.15 | NaUO3 | phase_label_not_mapped | label 'NaUO3' |
| ORC-E7RN5GEMPQ.315c76 | NA-O-U | SM | 298.15 | NaUO3 | phase_label_not_mapped | label 'NaUO3' |
| ORC-IQUKA2ZQMW.0b6ffd | NA-O-U | CPM | 298.15 | Na4UO5 | phase_label_not_mapped | label 'Na4UO5' |
| ORC-IQUKA2ZQMW.804ad4 | NA-O-U | SM | 298.15 | Na4UO5 | phase_label_not_mapped | label 'Na4UO5' |
| ORC-KJVQY5PHBZ.37210f | NA-O-U | SM | 298.15 | NaUO3 | phase_label_not_mapped | label 'NaUO3' |
| ORC-KJVQY5PHBZ.39b1dd | NA-O-U | CPM | 298.15 | NaUO3 | phase_label_not_mapped | label 'NaUO3' |
| ORC-MAEM6HMSSE.95cd53 | NA-O-U | SM | 298.15 | α-Na3UO4 | phase_label_not_mapped | label 'α-Na3UO4' |
| ORC-MAEM6HMSSE.ef77a9 | NA-O-U | CPM | 298.15 | α-Na3UO4 | phase_label_not_mapped | label 'α-Na3UO4' |
| ORC-NBACGHOUKT.493dd6 | NA-O-U | SM | 298.15 | α-Na2UO4 | phase_label_not_mapped | label 'α-Na2UO4' |
| ORC-NBACGHOUKT.56be8c | NA-O-U | CPM | 298.15 | α-Na2UO4 | phase_label_not_mapped | label 'α-Na2UO4' |
| ORC-QRFJ7MF5HX.96ec3f | NA-O-U | SM | 298.15 | α-Na2U2O7 | phase_label_not_mapped | label 'α-Na2U2O7' |
| ORC-QRFJ7MF5HX.aea61c | NA-O-U | CPM | 298.15 | α-Na2U2O7 | phase_label_not_mapped | label 'α-Na2U2O7' |
| ORC-UAK72SN4IB.02a81e | NA-O-U | SM | 298.15 | Na4UO5 | phase_label_not_mapped | label 'Na4UO5' |
| ORC-UAK72SN4IB.c84ed4 | NA-O-U | CPM | 298.15 | Na4UO5 | phase_label_not_mapped | label 'Na4UO5' |
| ORC-WIXFGZYLZ5.90b033 | NA-O-U | SM | 298.15 | α-Na2U2O7 | phase_label_not_mapped | label 'α-Na2U2O7' |
| ORC-WIXFGZYLZ5.cb9e89 | NA-O-U | CPM | 298.15 | α-Na2U2O7 | phase_label_not_mapped | label 'α-Na2U2O7' |
| ORC-XS6Z6HN5SC.7e5399 | NA-O-U | SM | 298.15 | α-Na3UO4 | phase_label_not_mapped | label 'α-Na3UO4' |
| ORC-XS6Z6HN5SC.ea79c5 | NA-O-U | CPM | 298.15 | α-Na3UO4 | phase_label_not_mapped | label 'α-Na3UO4' |
| ORC-Z5TNUF2QYD.3b072f | NA-O-U | CPM | 298.15 | α-Na2UO4 | phase_label_not_mapped | label 'α-Na2UO4' |
| ORC-Z5TNUF2QYD.5e1c2a | NA-O-U | SM | 298.15 | α-Na2UO4 | phase_label_not_mapped | label 'α-Na2UO4' |
| ORC-GUSR4DRJTM.dce290 | NB-NI | HM_FORM | 298.15 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-J7U4WVA25P.53a2b3 | NB-NI | HM_FORM | 298.15 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-J7U4WVA25P.e730dc | NB-NI | HM_FORM | 298.15 | µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KDDHYBPV3V.1f1c2c | NB-NI | HM_FORM | 0.0 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KDDHYBPV3V.6408a0 | NB-NI | HM_FORM | 0.0 | µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KDDHYBPV3V.9e54ef | NB-NI | HM_FORM | 298.15 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KDDHYBPV3V.a679af | NB-NI | HM_FORM | 298.15 | µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KNMXYXBOEW.6c652d | NB-NI | HM_FORM | 298.15 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-LFR5XFEABG.91d157 | NB-NI | HM_FORM | 0.0 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-UZM6JPBUE2.ab8273 | NB-NI | HM_FORM | 298.15 | µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-UZM6JPBUE2.b2325a | NB-NI | HM_FORM | 298.15 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-UZM6JPBUE2.c22fe6 | NB-NI | HM_FORM | 0.0 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-UZM6JPBUE2.e00607 | NB-NI | HM_FORM | 0.0 | µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-V6DVVRGG5E.11e0a4 | NB-NI | HM_FORM | 600.15 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-MDJMCVRYSE.1f557a | NB-SI | HM_FORM | 273.15 | (NbSi2) | phase_label_not_mapped | label '(NbSi2)' |
| ORC-TJTQXRTTEQ | NI-PT | HM_FORM | 0.0 | NiPt | phase_label_not_mapped | label 'NiPt' |
| ORC-22FCDAQURR | NI-RU | HM_FORM | 0.0 | NiRu | phase_label_not_mapped | label 'NiRu' |
| ORC-EEJVYGIGY3 | NI-RU | HM_FORM | 0.0 | Ni3Ru | phase_label_not_mapped | label 'Ni3Ru' |
| ORC-UKEBJMLR64 | NI-RU | HM_FORM | 0.0 | Ni2Ru2 | phase_label_not_mapped | label 'Ni2Ru2' |
| ORC-ZC5QIC3EQM | NI-RU | HM_FORM | 0.0 | NiRu3 | phase_label_not_mapped | label 'NiRu3' |
| ORC-DJW67EF4ZM.2ce8e3 | NI-SI | HM_FORM | 298.0 | L12 | phase_label_not_mapped | label 'L12' |
| ORC-DJW67EF4ZM.f4dfa5 | NI-SI | HM_FORM | 298.0 | L1_2 | phase_label_not_mapped | label 'L1_2' |
| ORC-DYBIVMPQDE.17e4c5 | NI-SI | HM_FORM | 298.15 | Ni3Si(β1) | phase_label_not_mapped | label 'Ni3Si(β1)' |
| ORC-GD6EKDN36L.0c78bd | NI-SI | HM_FORM | 298.0 | ε | phase_label_not_mapped | label 'ε' |
| ORC-3VGEQTV6FF | NI-SI-TI | HM_FORM | 298.15 | Ni3Ti(D024) | phase_label_not_mapped | label 'Ni3Ti(D024)' |
| ORC-W2AEPF25IN | NI-SI-TI | HM_FORM | 298.15 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-2YDOIF7YWA | NI-TI | HM_FORM | 1460.0 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-4R2G2JJ6I6.0053d5 | NI-TI | HM_FORM | 0.0 | TiNi-B2 | phase_label_not_mapped | label 'TiNi-B2' |
| ORC-BEB5Y4LZT2 | NI-TI | HM_FORM | 999.0 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-HYPU3NBXDV | NI-TI | HM_FORM | 298.15 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-L2OPU6DDBU.b904a0 | NI-TI | HM_FORM | 0.0 | TiNi3 | phase_label_not_mapped | label 'TiNi3' |
| ORC-PEPGNW2DTY.86597c | NI-TI | HM_FORM | 298.15 | Ti2Ni | phase_label_not_mapped | label 'Ti2Ni' |
| ORC-YEW6RRQCYU.9b4e30 | NI-TI | HM_FORM | 298.15 | TiNi-B2 | phase_label_not_mapped | label 'TiNi-B2' |
| ORC-KXUDL7OM6F.6f0ea7 | NI-ZR | HM_FORM | 298.15 | Ni10Zr7 (Cmce) | phase_label_not_mapped | label 'Ni10Zr7 (Cmce)' |
| ORC-UNCLQ3XYUM.e16ebf | NI-ZR | HM_FORM | 298.15 | Ni10Zr7 (Cmce) | phase_label_not_mapped | label 'Ni10Zr7 (Cmce)' |
| ORC-YD4ZMVK7XT.3bcb4a | NI-ZR | HM_FORM | 298.15 | Ni10Zr7 (Cmce) | phase_label_not_mapped | label 'Ni10Zr7 (Cmce)' |
| ORC-AC5XP45GUD.931f48 | O-PB | SM | 298.15 | PbO-L | phase_label_not_mapped | label 'PbO-L' |
| ORC-CZYMM2JLMK.e610a8 | O-PB | SM | 298.15 | PbO2-I | phase_label_not_mapped | label 'PbO2-I' |
| ORC-GHCN4AU6KY.0f4f25 | O-PB | GM_FORM | 298.15 | PbO-L | phase_label_not_mapped | label 'PbO-L' |
| ORC-H6CAMZNZB6.9934b5 | O-PB | GM_FORM | 298.15 | Pb3O4-T | phase_label_not_mapped | label 'Pb3O4-T' |
| ORC-OMX5IAEZKZ.9bd070 | O-PB | HM_FORM | 298.15 | Pb3O4-T | phase_label_not_mapped | label 'Pb3O4-T' |
| ORC-RQM5UTYKXI.4dfee6 | O-PB | GM_FORM | 298.15 | PbO-L | phase_label_not_mapped | label 'PbO-L' |
| ORC-SRQYCLOPWT.a90ea0 | O-PB | GM_FORM | 298.15 | Pb3O4-T | phase_label_not_mapped | label 'Pb3O4-T' |
| ORC-TGORSEP3OM.7b6f68 | O-PB | HM_FORM | 298.15 | PbO2-I | phase_label_not_mapped | label 'PbO2-I' |
| ORC-RWSO6GJ6PB.31c653 | O-U | SM | 298.15 | UO2 | phase_label_not_mapped | label 'UO2' |
| ORC-T4WJT4BQP5.64d6b9 | O-U | SM | 298.15 | UO2 | phase_label_not_mapped | label 'UO2' |
| ORC-3IWLINAN5P.c6f340 | PD-SN | HM_FORM | 273.0 | PdSn | phase_label_not_mapped | label 'PdSn' |
| ORC-LQN7YN3PVS.aa54d7 | PD-SN | HM_FORM | 320.0 | PdSn | phase_label_not_mapped | label 'PdSn' |
| ORC-QBTBTA576Y.13bbfc | PD-SN | HM_FORM | 320.0 | Pd3Sn | phase_label_not_mapped | label 'Pd3Sn' |
| ORC-WQH6W53A6M.a387b3 | PD-SN | HM_FORM | 320.0 | Pd2Sn | phase_label_not_mapped | label 'Pd2Sn' |
| ORC-YQ6CITKJYH.eca9f0 | PD-SN | HM_FORM | 273.0 | PdSn4 | phase_label_not_mapped | label 'PdSn4' |
| ORC-ZLK2AFKPJQ.c4d86a | PD-SN | HM_FORM | 320.0 | PdSn4 | phase_label_not_mapped | label 'PdSn4' |
| ORC-2Z6HTHMIDZ.1076b3 | PD-ZN | HM_FORM | 0.0 | γ phase | phase_label_not_mapped | label 'γ phase' |
| ORC-I5ERKJ6ASU.0d9345 | PD-ZN | HM_FORM | 300.0 | γ phase | phase_label_not_mapped | label 'γ phase' |
| ORC-PYTXWNTXRJ.ae3d89 | PD-ZN | HM_FORM | 0.0 | γ phase | phase_label_not_mapped | label 'γ phase' |
| ORC-AZHIIJFVVN.0f8013 | PU-U | CPM | 773.0 | α | phase_label_not_mapped | label 'α' |
| ORC-K3HZTEHG2L.f8e0f3 | PU-U | CPM | 673.0 | α | phase_label_not_mapped | label 'α' |
| ORC-KSXPAH2RSB.4db829 | PU-U | CPM | 840.0 | α | phase_label_not_mapped | label 'α' |
| ORC-YQE3JLSV6E | RE-SI | HM_FORM | 298.15 | ReSi1.8 | phase_label_not_mapped | label 'ReSi1.8' |
| ORC-VURWOO5JZR.83958d | RE-TA | GM_FORM | 298.15 | TaRe1.85 (χ) | phase_label_not_mapped | label 'TaRe1.85 (χ)' |
| ORC-VURWOO5JZR.841657 | RE-TA | GM_FORM | 298.15 | TaRe1.85 (χ) | phase_label_not_mapped | label 'TaRe1.85 (χ)' |
| ORC-VURWOO5JZR.f2d89c | RE-TA | GM_FORM | 298.15 | TaRe3.6 (χ) | phase_label_not_mapped | label 'TaRe3.6 (χ)' |
| ORC-37FC3SIAD7.bccaa4 | SB-ZN | HM_FORM | 806.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-37FC3SIAD7.ecb149 | SB-ZN | GM_FORM | 806.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-HTTS63YOJG.2f0354 | SB-ZN | GM_FORM | 800.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-HTTS63YOJG.aceeb6 | SB-ZN | HM_FORM | 800.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-AVCIAILA5H | SI-U | HM_FORM | 298.0 | USi | phase_label_not_mapped | label 'USi' |
| ORC-CCGYQZRSVK | SI-U | HM_FORM | 298.0 | USi | phase_label_not_mapped | label 'USi' |
| ORC-MGA3VU6PIM | SI-U | HM_FORM | 298.0 | USi | phase_label_not_mapped | label 'USi' |
| ORC-PN7BWE5QAM | SI-U | HM_FORM | 298.0 | USi2 | phase_label_not_mapped | label 'USi2' |
| ORC-Q6OGIGUYRX | SI-U | HM_FORM | 298.0 | USi2 | phase_label_not_mapped | label 'USi2' |
| ORC-ZBLVBWLP4M | SI-U | HM_FORM | 298.0 | USi2 | phase_label_not_mapped | label 'USi2' |
| ORC-IMUKKQP2HM.58e758 | SI-YB | SM_FORM | 298.0 | Yb3Si11 | phase_label_not_mapped | label 'Yb3Si11' |
| ORC-IMUKKQP2HM.bab35b | SI-YB | HM_FORM | 298.0 | Yb3Si11 | phase_label_not_mapped | label 'Yb3Si11' |
| ORC-YTPULMUAG2.38164d | SN-TI | HM_FORM | 298.15 | SnTi2 | phase_label_not_mapped | label 'SnTi2' |
| ORC-YTPULMUAG2.3a933d | SN-TI | HM_FORM | 298.15 | Sn3Ti5 | phase_label_not_mapped | label 'Sn3Ti5' |
| ORC-YTPULMUAG2.da0b8e | SN-TI | HM_FORM | 298.15 | SnTi3 | phase_label_not_mapped | label 'SnTi3' |
| ORC-2ARHPO6ULI.9c5c44 | AG-PB | CPM | 680.646 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2ARHPO6ULI.f80d4a | AG-PB | CPM | 680.646 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2HZ4HO7VKQ.8d78c3 | AG-PB | CPM | 917.968 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2HZ4HO7VKQ.eca7c0 | AG-PB | CPM | 917.968 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DTAFVIJ57.14fb4f | AG-PB | CPM | 674.664 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DTAFVIJ57.24db24 | AG-PB | CPM | 674.664 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DTHACXC4T.7829d4 | AG-PB | CPM | 642.769 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DTHACXC4T.d9eb4c | AG-PB | CPM | 642.769 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3LN4ERBOIM.6a4804 | AG-PB | CPM | 728.523 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3LN4ERBOIM.c07bf5 | AG-PB | CPM | 728.523 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-44RRBDE2J3.127e38 | AG-PB | CPM | 686.632 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-44RRBDE2J3.b260d0 | AG-PB | CPM | 686.632 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4DHTNZ4RGV.74ef13 | AG-PB | CPM | 882.066 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4DHTNZ4RGV.d71f3e | AG-PB | CPM | 882.066 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4PVRTK5W6F.11db0b | AG-PB | CPM | 951.866 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4PVRTK5W6F.40a6ee | AG-PB | CPM | 951.866 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4QJKHOGSFE.8b7647 | AG-PB | CPM | 798.296 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4QJKHOGSFE.a70b53 | AG-PB | CPM | 798.296 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4QN3QJYDQA.78bec4 | AG-PB | CPM | 929.937 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4QN3QJYDQA.7a96f1 | AG-PB | CPM | 929.937 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4THI2UYU76.131cfc | AG-PB | CPM | 770.407 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4THI2UYU76.f00a6e | AG-PB | CPM | 770.407 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4ZMIAUXC6R.1fb3e3 | AG-PB | CPM | 900.015 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4ZMIAUXC6R.c046b4 | AG-PB | CPM | 900.015 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5G35LAPOWB.704587 | AG-PB | CPM | 684.636 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5G35LAPOWB.8d495e | AG-PB | CPM | 684.636 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5IQH544QDY.776b5c | AG-PB | CPM | 874.089 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5IQH544QDY.cd6539 | AG-PB | CPM | 874.089 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6SVBLFA6BT.845f73 | AG-PB | CPM | 872.094 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6SVBLFA6BT.a72bb3 | AG-PB | CPM | 872.094 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6WLYXL2FQA.20d5f6 | AG-PB | CPM | 808.271 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6WLYXL2FQA.7f3f0b | AG-PB | CPM | 808.271 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-73IVDAIKMQ.8a2be3 | AG-PB | CPM | 712.563 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-73IVDAIKMQ.e48566 | AG-PB | CPM | 712.563 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-76ZT2FWALX.62f32f | AG-PB | CPM | 953.859 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-76ZT2FWALX.d61cf5 | AG-PB | CPM | 953.859 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7BB4CKBGHU.20414f | AG-PB | CPM | 898.023 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7BB4CKBGHU.edf08e | AG-PB | CPM | 898.023 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7G2K4CJPY5.576e46 | AG-PB | CPM | 774.375 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7G2K4CJPY5.b74718 | AG-PB | CPM | 774.375 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7K6DEW2CLD.65a739 | AG-PB | CPM | 886.057 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7K6DEW2CLD.e6f93b | AG-PB | CPM | 886.057 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7KPULGBBA4.2d6291 | AG-PB | CPM | 778.359 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7KPULGBBA4.5ee390 | AG-PB | CPM | 778.359 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7MCNUQTPUQ.83179d | AG-PB | CPM | 935.923 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7MCNUQTPUQ.890fa0 | AG-PB | CPM | 935.923 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7OIUJD4DZG.24a84c | AG-PB | CPM | 664.696 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7OIUJD4DZG.70c423 | AG-PB | CPM | 664.696 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7XP3AX7IK2.32cb0d | AG-PB | CPM | 909.988 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7XP3AX7IK2.cdcdb1 | AG-PB | CPM | 909.988 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AB5MDPD4FL.4ae0da | AG-PB | CPM | 748.467 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AB5MDPD4FL.c1e1c7 | AG-PB | CPM | 748.467 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ANPS4KLMKO.6ff3bc | AG-PB | CPM | 692.614 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ANPS4KLMKO.c0dc7c | AG-PB | CPM | 692.614 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ANUGQC7BJO.0cc41f | AG-PB | CPM | 820.231 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ANUGQC7BJO.f599de | AG-PB | CPM | 820.231 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AWW23FBCHH.06e20e | AG-PB | CPM | 660.709 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AWW23FBCHH.86fd21 | AG-PB | CPM | 660.709 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-B7PCQBKCNB.7144e0 | AG-PB | CPM | 702.59 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-B7PCQBKCNB.d05837 | AG-PB | CPM | 702.59 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BIIJFGEOB5.94513d | AG-PB | CPM | 840.175 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BIIJFGEOB5.ae8679 | AG-PB | CPM | 840.175 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BNTYA7EMG3.9cff4c | AG-PB | CPM | 698.596 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BNTYA7EMG3.cfdf9f | AG-PB | CPM | 698.596 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BUHNMWLZCZ.1fd5d7 | AG-PB | CPM | 856.135 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BUHNMWLZCZ.63deda | AG-PB | CPM | 856.135 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BWHINBDKJR.55496a | AG-PB | CPM | 704.583 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BWHINBDKJR.914d42 | AG-PB | CPM | 704.583 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BX5FPVVQIV.480dfe | AG-PB | CPM | 961.838 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BX5FPVVQIV.c3e477 | AG-PB | CPM | 961.838 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-C2X4WAPT5Q.171c42 | AG-PB | CPM | 700.593 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-C2X4WAPT5Q.6b3efa | AG-PB | CPM | 700.593 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CFDTEF4RTJ.1eac58 | AG-PB | CPM | 720.543 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CFDTEF4RTJ.d8a47b | AG-PB | CPM | 720.543 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CMHLS3QI77.48271e | AG-PB | CPM | 750.461 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CMHLS3QI77.d5fc45 | AG-PB | CPM | 750.461 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CP5N3NWNTK.9640af | AG-PB | CPM | 925.946 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CP5N3NWNTK.c581fc | AG-PB | CPM | 925.946 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CPTWEBCT4N.661f09 | AG-PB | CPM | 848.155 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CPTWEBCT4N.aa8394 | AG-PB | CPM | 848.155 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CX2B7EYOFW.318d1c | AG-PB | CPM | 902.011 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CX2B7EYOFW.f2a50e | AG-PB | CPM | 902.011 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-D7G7L6WRQE.cd5c4a | AG-PB | CPM | 830.199 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-D7G7L6WRQE.dd6287 | AG-PB | CPM | 830.199 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DBSAYIEL4U.643b6c | AG-PB | CPM | 832.193 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DBSAYIEL4U.fddf9e | AG-PB | CPM | 832.193 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DEK6AYBJHT.120a24 | AG-PB | CPM | 931.931 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DEK6AYBJHT.43efd5 | AG-PB | CPM | 931.931 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DG2PEM2S2X.6e6130 | AG-PB | CPM | 941.902 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DG2PEM2S2X.761d49 | AG-PB | CPM | 941.902 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DPGBPT3V25.90b818 | AG-PB | CPM | 816.244 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DPGBPT3V25.d68bb2 | AG-PB | CPM | 816.244 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DR3BILJDS2.49b7af | AG-PB | CPM | 690.62 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DR3BILJDS2.8293df | AG-PB | CPM | 690.62 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DT3W5U462R.1a4b8c | AG-PB | CPM | 894.037 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DT3W5U462R.a0895c | AG-PB | CPM | 894.037 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DTG2NLHDOA.425856 | AG-PB | CPM | 955.852 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DTG2NLHDOA.50dcf6 | AG-PB | CPM | 955.852 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DVMRXMFPWW.341a8c | AG-PB | CPM | 740.495 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DVMRXMFPWW.ad413e | AG-PB | CPM | 740.495 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DW3WA5UZ2E.223222 | AG-PB | CPM | 746.473 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DW3WA5UZ2E.624362 | AG-PB | CPM | 746.473 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-E7J5DCWKP6.01269b | AG-PB | CPM | 868.103 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-E7J5DCWKP6.17ae45 | AG-PB | CPM | 868.103 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EOKHJKO32F.3e36bd | AG-PB | CPM | 760.435 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EOKHJKO32F.a06714 | AG-PB | CPM | 760.435 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ES52JMIQRA.26693f | AG-PB | CPM | 826.214 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ES52JMIQRA.5a9a84 | AG-PB | CPM | 826.214 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EVWFSM6URM.9494eb | AG-PB | CPM | 818.237 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EVWFSM6URM.f2783d | AG-PB | CPM | 818.237 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-F25SXBIYWD.29e35c | AG-PB | CPM | 734.507 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-F25SXBIYWD.a1f8c3 | AG-PB | CPM | 734.507 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-F43ZTPAGRR.71ed62 | AG-PB | CPM | 864.117 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-F43ZTPAGRR.c7551c | AG-PB | CPM | 864.117 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FD6ERMCM5M.8f7ef1 | AG-PB | CPM | 919.962 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FD6ERMCM5M.a1c831 | AG-PB | CPM | 919.962 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FEGVM5GGM4.152feb | AG-PB | CPM | 764.423 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FEGVM5GGM4.abb3f6 | AG-PB | CPM | 764.423 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FIMHIPPOLZ.7287c5 | AG-PB | CPM | 892.04 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FIMHIPPOLZ.f3cf8a | AG-PB | CPM | 892.04 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FJCKTDLWSS.69deb1 | AG-PB | CPM | 634.791 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FJCKTDLWSS.8c0d76 | AG-PB | CPM | 634.791 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FMO26DINAI.075ace | AG-PB | CPM | 696.603 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FMO26DINAI.ce78c4 | AG-PB | CPM | 696.603 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FWY2SEEVQ2.37a6b1 | AG-PB | CPM | 678.651 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FWY2SEEVQ2.c0e634 | AG-PB | CPM | 678.651 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FX5JGS2X4Z.a9c91d | AG-PB | CPM | 650.744 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FX5JGS2X4Z.fd9a12 | AG-PB | CPM | 650.744 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FXYTFJCBFB.443bd6 | AG-PB | CPM | 806.275 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FXYTFJCBFB.e74ee1 | AG-PB | CPM | 806.275 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-G26IFHJTTF.041b5d | AG-PB | CPM | 947.882 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-G26IFHJTTF.9e672d | AG-PB | CPM | 947.882 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-G47SYJZMSP.3ad3f8 | AG-PB | CPM | 772.403 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-G47SYJZMSP.aaa56b | AG-PB | CPM | 772.403 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GACCIRXF2N.a60fcd | AG-PB | CPM | 963.83 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GACCIRXF2N.cc64c4 | AG-PB | CPM | 963.83 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GCSXGCEUZY.26413d | AG-PB | CPM | 854.14 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GCSXGCEUZY.cc2480 | AG-PB | CPM | 854.14 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GO6SQI7PIT.da36f5 | AG-PB | CPM | 732.512 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GO6SQI7PIT.f2f306 | AG-PB | CPM | 732.512 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GYPW6QVUJV.3de26d | AG-PB | CPM | 822.225 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GYPW6QVUJV.d603b9 | AG-PB | CPM | 822.225 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-H5HXDBZOED.578fff | AG-PB | CPM | 718.549 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-H5HXDBZOED.afec55 | AG-PB | CPM | 718.549 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HICGZP6YMM.af8370 | AG-PB | CPM | 738.496 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HICGZP6YMM.b89e87 | AG-PB | CPM | 738.496 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HLLVOCEUYM.0f5111 | AG-PB | CPM | 644.761 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HLLVOCEUYM.a6cbeb | AG-PB | CPM | 644.761 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HORFYHR2KI.8c026c | AG-PB | CPM | 708.572 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HORFYHR2KI.b93920 | AG-PB | CPM | 708.572 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HQWLBCQIBY.a4cf3f | AG-PB | CPM | 654.732 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HQWLBCQIBY.a90b52 | AG-PB | CPM | 654.732 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-INNY76UX7G.d6246b | AG-PB | CPM | 943.897 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-INNY76UX7G.f92ff0 | AG-PB | CPM | 943.897 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IZ45Z5LUWX.25ad07 | AG-PB | CPM | 858.13 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IZ45Z5LUWX.8bf049 | AG-PB | CPM | 858.13 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J5GO7LZIPM.491b25 | AG-PB | CPM | 862.122 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J5GO7LZIPM.c94c61 | AG-PB | CPM | 862.122 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J6H4EQXXAS.01826f | AG-PB | CPM | 812.26 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J6H4EQXXAS.3f02c2 | AG-PB | CPM | 812.26 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J7GW2ZTWE2.ce9f7f | AG-PB | CPM | 896.032 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J7GW2ZTWE2.d1f409 | AG-PB | CPM | 896.032 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JBTX3RU756.5b1313 | AG-PB | CPM | 814.253 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JBTX3RU756.5b6904 | AG-PB | CPM | 814.253 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JMF7UEXZGW.bf1f0e | AG-PB | CPM | 834.189 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JMF7UEXZGW.e70d3a | AG-PB | CPM | 834.189 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JOJC77ELUW.1dc893 | AG-PB | CPM | 752.457 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JOJC77ELUW.4a1f57 | AG-PB | CPM | 752.457 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JQDOBITKUH.d6c083 | AG-PB | CPM | 937.917 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JQDOBITKUH.f2ad76 | AG-PB | CPM | 937.917 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JTIG6SA6N7.23e52d | AG-PB | CPM | 730.516 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JTIG6SA6N7.cbc285 | AG-PB | CPM | 730.516 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KDDUX3YVXS.ab7554 | AG-PB | CPM | 754.452 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KDDUX3YVXS.d433ed | AG-PB | CPM | 754.452 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KT473ORKEL.ae9b3b | AG-PB | CPM | 762.429 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KT473ORKEL.c08409 | AG-PB | CPM | 762.429 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KZ236DSTN3.888118 | AG-PB | CPM | 688.627 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KZ236DSTN3.bde1ff | AG-PB | CPM | 688.627 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-L7W2FWUUAG.7a28ac | AG-PB | CPM | 880.071 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-L7W2FWUUAG.daaf97 | AG-PB | CPM | 880.071 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LTM345PTHJ.09528e | AG-PB | CPM | 866.112 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LTM345PTHJ.b80697 | AG-PB | CPM | 866.112 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LUV7WT4PIM.ed894f | AG-PB | CPM | 878.076 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LUV7WT4PIM.f24786 | AG-PB | CPM | 878.076 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LW4YQECFOW.067678 | AG-PB | CPM | 888.052 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LW4YQECFOW.1d920c | AG-PB | CPM | 888.052 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-M3EMMXWKI5.5f07f4 | AG-PB | CPM | 776.366 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-M3EMMXWKI5.d59950 | AG-PB | CPM | 776.366 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-M3NHBGRPD3.496db3 | AG-PB | CPM | 768.411 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-M3NHBGRPD3.769e66 | AG-PB | CPM | 768.411 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MCRPXOH7QK.536c01 | AG-PB | CPM | 927.942 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MCRPXOH7QK.e9edec | AG-PB | CPM | 927.942 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MITYBTEMHY.4ec620 | AG-PB | CPM | 676.658 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MITYBTEMHY.fcc4f4 | AG-PB | CPM | 676.658 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MJ4OKSE2PO.9be3be | AG-PB | CPM | 915.974 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MJ4OKSE2PO.d25102 | AG-PB | CPM | 915.974 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MKTYSCGYUI.5125b7 | AG-PB | CPM | 846.161 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MKTYSCGYUI.a7c68e | AG-PB | CPM | 846.161 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MP5JWNP5WT.6613bc | AG-PB | CPM | 766.417 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MP5JWNP5WT.d1e4ff | AG-PB | CPM | 766.417 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MRURU6UP3U.34dc3d | AG-PB | CPM | 939.909 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MRURU6UP3U.d84dd6 | AG-PB | CPM | 939.909 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MTVLG7PHWW.7dddde | AG-PB | CPM | 876.081 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MTVLG7PHWW.aac8c7 | AG-PB | CPM | 876.081 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-N3Y4FECV2I.70085f | AG-PB | CPM | 758.439 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-N3Y4FECV2I.ae0ffd | AG-PB | CPM | 758.439 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-N5CR2YJPFK.5a56b0 | AG-PB | CPM | 824.22 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-N5CR2YJPFK.67c26b | AG-PB | CPM | 824.22 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NLWT6JLS3U.3092c3 | AG-PB | CPM | 672.669 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NLWT6JLS3U.4a5023 | AG-PB | CPM | 672.669 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NPKLDCXGQX.01716c | AG-PB | CPM | 670.673 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NPKLDCXGQX.391d22 | AG-PB | CPM | 670.673 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NPOEMECNIQ.059c2c | AG-PB | CPM | 726.53 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NPOEMECNIQ.dfb773 | AG-PB | CPM | 726.53 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NXN562PQJK.4d5010 | AG-PB | CPM | 710.567 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NXN562PQJK.82b699 | AG-PB | CPM | 710.567 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-O5GRRVAREL.a2d65d | AG-PB | CPM | 744.482 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-O5GRRVAREL.bb1e42 | AG-PB | CPM | 744.482 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OCVZNJN45Q.7cec6b | AG-PB | CPM | 724.534 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OCVZNJN45Q.eb7d68 | AG-PB | CPM | 724.534 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OIXPZTKC6J.34e196 | AG-PB | CPM | 965.825 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OIXPZTKC6J.47f1bf | AG-PB | CPM | 965.825 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OOJTOZE6NG.6f73bb | AG-PB | CPM | 714.558 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OOJTOZE6NG.bc679a | AG-PB | CPM | 714.558 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OPELXV3XPC.72670e | AG-PB | CPM | 790.318 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OPELXV3XPC.93308e | AG-PB | CPM | 790.318 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PHJBV4QMWD.17663e | AG-PB | CPM | 836.186 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PHJBV4QMWD.deda7e | AG-PB | CPM | 836.186 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PJD6DGUC2G.1d671c | AG-PB | CPM | 636.787 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PJD6DGUC2G.38984c | AG-PB | CPM | 636.787 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-POUB35V4H2.df5da9 | AG-PB | CPM | 666.69 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-POUB35V4H2.fe63de | AG-PB | CPM | 666.69 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PQORXAAKDA.201f64 | AG-PB | CPM | 933.927 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PQORXAAKDA.a44883 | AG-PB | CPM | 933.927 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PRQP2MPCBB.9a7973 | AG-PB | CPM | 800.291 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PRQP2MPCBB.b3a0e2 | AG-PB | CPM | 800.291 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PU7P3TBJPC.a0419c | AG-PB | CPM | 736.499 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PU7P3TBJPC.b3e359 | AG-PB | CPM | 736.499 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PUOQS2ITTA.77ec8d | AG-PB | CPM | 949.874 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PUOQS2ITTA.c947d9 | AG-PB | CPM | 949.874 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Q3OG23H5JP.aa4378 | AG-PB | CPM | 780.354 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Q3OG23H5JP.fb1be8 | AG-PB | CPM | 780.354 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Q3SAPDQ4BY.2b4755 | AG-PB | CPM | 782.349 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Q3SAPDQ4BY.c98efb | AG-PB | CPM | 782.349 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QLI5ATQBRP.3913f1 | AG-PB | CPM | 716.553 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QLI5ATQBRP.ffe8e9 | AG-PB | CPM | 716.553 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-R2SGFHFUJ4.4c9c4b | AG-PB | CPM | 646.753 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-R2SGFHFUJ4.8cad09 | AG-PB | CPM | 646.753 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RBS5T6XIB7.66bcd9 | AG-PB | CPM | 722.537 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RBS5T6XIB7.6e4439 | AG-PB | CPM | 722.537 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RGGOFP6WR6.b81676 | AG-PB | CPM | 794.308 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RGGOFP6WR6.c07d09 | AG-PB | CPM | 794.308 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RHTRM4DYHC.45e600 | AG-PB | CPM | 796.301 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RHTRM4DYHC.ec7d45 | AG-PB | CPM | 796.301 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RVEZT323R6.1c357c | AG-PB | CPM | 921.957 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RVEZT323R6.d0dd7f | AG-PB | CPM | 921.957 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RZBPECWZJL.0e07b2 | AG-PB | CPM | 852.144 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RZBPECWZJL.5a916a | AG-PB | CPM | 852.144 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SABGQAJGD7.434714 | AG-PB | CPM | 786.334 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SABGQAJGD7.f7587a | AG-PB | CPM | 786.334 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SKRKBZPI3V.242a51 | AG-PB | CPM | 802.285 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SKRKBZPI3V.f0b7e6 | AG-PB | CPM | 802.285 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SOM3EGJ5MP.2df624 | AG-PB | CPM | 844.17 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SOM3EGJ5MP.daa54c | AG-PB | CPM | 844.17 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SONTENM4OP.34e071 | AG-PB | CPM | 884.062 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SONTENM4OP.44ad06 | AG-PB | CPM | 884.062 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SYX7Q55QKO.0d0b8c | AG-PB | CPM | 788.326 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SYX7Q55QKO.c3e585 | AG-PB | CPM | 788.326 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SYZRQBCMDO.611576 | AG-PB | CPM | 923.952 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SYZRQBCMDO.d3ae3e | AG-PB | CPM | 923.952 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TTCXNTB3JN.1e072f | AG-PB | CPM | 860.127 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TTCXNTB3JN.e52b19 | AG-PB | CPM | 860.127 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TWVU6UDAHE.9ffbb1 | AG-PB | CPM | 890.044 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TWVU6UDAHE.ed4fd5 | AG-PB | CPM | 890.044 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U2SB3OMRQC.a4d2ca | AG-PB | CPM | 658.716 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U2SB3OMRQC.f8541c | AG-PB | CPM | 658.716 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U34WNUTREE.235e39 | AG-PB | CPM | 967.821 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U34WNUTREE.43f53d | AG-PB | CPM | 967.821 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U3AQJEJZZ2.c1c23d | AG-PB | CPM | 694.609 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U3AQJEJZZ2.fb77fd | AG-PB | CPM | 694.609 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UMQDJURRN5.247dd0 | AG-PB | CPM | 632.8 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UMQDJURRN5.f8ac24 | AG-PB | CPM | 632.8 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UOGOZHS3CR.2ff711 | AG-PB | CPM | 911.983 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UOGOZHS3CR.7e59f1 | AG-PB | CPM | 911.983 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-US4CZCJ2G3.89221a | AG-PB | CPM | 662.703 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-US4CZCJ2G3.d39aa2 | AG-PB | CPM | 662.703 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UVLNHUJXLJ.3839d3 | AG-PB | CPM | 969.817 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UVLNHUJXLJ.e62a6d | AG-PB | CPM | 969.817 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UZOADQR4I6.9ed416 | AG-PB | CPM | 656.725 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UZOADQR4I6.bccbaf | AG-PB | CPM | 656.725 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VDJVY6CKDP.1d951e | AG-PB | CPM | 957.846 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VDJVY6CKDP.88195a | AG-PB | CPM | 957.846 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VGYUCPDBMW.220f83 | AG-PB | CPM | 850.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VGYUCPDBMW.c1d04d | AG-PB | CPM | 850.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VIQFNOP7TZ.c209ad | AG-PB | CPM | 804.28 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VIQFNOP7TZ.d2d743 | AG-PB | CPM | 804.28 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VL2GH3SFHO.64ccb4 | AG-PB | CPM | 652.737 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VL2GH3SFHO.909385 | AG-PB | CPM | 652.737 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-W7STQPEGAT.294a52 | AG-PB | CPM | 628.812 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-W7STQPEGAT.fc7b8f | AG-PB | CPM | 628.812 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WAKQG5WET6.8bc51b | AG-PB | CPM | 906.003 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WAKQG5WET6.b7d372 | AG-PB | CPM | 906.003 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WII6TFN3VG.6dbf97 | AG-PB | CPM | 682.641 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WII6TFN3VG.84e2c7 | AG-PB | CPM | 682.641 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WM5GU4Y32R.5e7dea | AG-PB | CPM | 648.75 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WM5GU4Y32R.78dbe1 | AG-PB | CPM | 648.75 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WWOZG4LQIC.0c34da | AG-PB | CPM | 959.843 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WWOZG4LQIC.191017 | AG-PB | CPM | 959.843 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XJN35IPW72.a6073f | AG-PB | CPM | 810.264 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XJN35IPW72.fd6c2f | AG-PB | CPM | 810.264 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XQPB7D5SLT.6e5534 | AG-PB | CPM | 945.89 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XQPB7D5SLT.b431df | AG-PB | CPM | 945.89 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Y5KKYQB457.03aee5 | AG-PB | CPM | 870.097 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Y5KKYQB457.97de3b | AG-PB | CPM | 870.097 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YAZBBKJRDL.a5b45c | AG-PB | CPM | 842.173 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YAZBBKJRDL.da8ad1 | AG-PB | CPM | 842.173 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YBWUQOYJZN.01964b | AG-PB | CPM | 913.979 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YBWUQOYJZN.6b52fc | AG-PB | CPM | 913.979 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YC2BJ4UHYF.b8c37c | AG-PB | CPM | 638.78 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YC2BJ4UHYF.c2fcd8 | AG-PB | CPM | 638.78 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YCJ7TM6BXO.60a215 | AG-PB | CPM | 838.179 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YCJ7TM6BXO.f0d47a | AG-PB | CPM | 838.179 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YPAEL6HQ5X.bf7f84 | AG-PB | CPM | 742.489 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YPAEL6HQ5X.d0d3af | AG-PB | CPM | 742.489 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Z32GWFJIPN.e3dde6 | AG-PB | CPM | 756.444 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Z32GWFJIPN.f1eba2 | AG-PB | CPM | 756.444 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Z5NEOOITTB.a079f7 | AG-PB | CPM | 772.392 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Z5NEOOITTB.e8b692 | AG-PB | CPM | 772.392 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZDH3TQUW5V.cef4b5 | AG-PB | CPM | 828.205 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZDH3TQUW5V.d304d9 | AG-PB | CPM | 828.205 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZDINBQ4UML.6778e3 | AG-PB | CPM | 784.341 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZDINBQ4UML.700954 | AG-PB | CPM | 784.341 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZKF2XKEQJC.399073 | AG-PB | CPM | 792.314 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZKF2XKEQJC.b18eed | AG-PB | CPM | 792.314 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZLFZRAVKRJ.70f9a8 | AG-PB | CPM | 630.807 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZLFZRAVKRJ.95c9d2 | AG-PB | CPM | 630.807 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZNNIRNC3Z6.b814c4 | AG-PB | CPM | 706.577 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZNNIRNC3Z6.d692a1 | AG-PB | CPM | 706.577 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZREY6M73OS.54a0d2 | AG-PB | CPM | 668.68 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZREY6M73OS.606903 | AG-PB | CPM | 668.68 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZWUKVJQNMI.a4ad60 | AG-PB | CPM | 640.774 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZWUKVJQNMI.dc9c88 | AG-PB | CPM | 640.774 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3HNT2KROYM.2327c9 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3HNT2KROYM.fc350f | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DENBWB3K3C.0a754d | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DENBWB3K3C.9805cf | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DYLEZCG4HM.b90007 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DYLEZCG4HM.d2c55e | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EG4CZFRGL7.697286 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EG4CZFRGL7.8c720a | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FCNMFTUR4E.901fdd | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FCNMFTUR4E.d90e23 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FORFJG353E.0cea63 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FORFJG353E.18dd13 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-G2E5AOIVAY.bab2df | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-G2E5AOIVAY.bd6342 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IAHORPYKKP.4a3737 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IAHORPYKKP.c8c592 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IR25DWRF5G.165461 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IR25DWRF5G.fee548 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IYYBFJIDJR.9a13f7 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IYYBFJIDJR.e433be | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JFXIVMRCAO.047605 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JFXIVMRCAO.3f0c26 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-N7ZOMZ7UNS.352d88 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-N7ZOMZ7UNS.e9c9c9 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NOQDCUENTV.5695f3 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PJHC2KGG2M.159934 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PJHC2KGG2M.d50a74 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RMJA7ZD7GC.3990b7 | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RMJA7ZD7GC.fc193f | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-S7IJ2WTKZG.22e618 | AG-SE | GM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-S7IJ2WTKZG.4adf0e | AG-SE | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2KOSDBV2KV.de5c3c | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3QIK7OVINP.8dfa3e | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4AIGKIGSRZ.38aeaa | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4T6PPMNMVH.3e4d27 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-56LEO63NHI.7dbdc5 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6WOBDFQDT6.dd85fd | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-72BYE267EP.d2d345 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7WTP4LTZGH.d706cb | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AJBLYDVVJ7.b058a9 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ARDICSAW5Q.582e90 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BIBOWE6FPC.2730db | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CUGQ3IS253.4ae873 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DJDAA52VRM.53b551 | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EFRE3KLDTL.7caa40 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FHBP4YQMQO.76870b | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-H3W2VXUOCC.c5b16e | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-H5Q7XJZTLL.ba82c4 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HH5P332BD5.6dc594 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IGHKVCH3WK.c582ac | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J5T6TBKDML.27cda4 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LDRKSJQLLM.8e0b24 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LJMIPJOCL3.0c225c | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NEIOD6VMFX.794acb | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OHVOHPTKPU.cf7138 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PNDWNRMG4M.e93ef7 | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RBRLISTFX3.f41c25 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RRTXNAEBFG.b23cf4 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RU5SWY7JGW.ef4ed6 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SGGMA66RLQ.1795e9 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TCPC77DHKK.420946 | AL-CA | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WAZ6UJADGF.b41923 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZKD74CCMXO.b537d4 | AL-CA | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4OC5YD5B5T.6e4510 | AL-CR | HM_FORM | 1273.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LSLZ6CGKOQ.207e1f | AL-CR | HM_FORM | 1273.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PDPECKEWAL.51eaf8 | AL-CR | HM_FORM | 1273.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RL4XI5ZJPE.3dd98a | AL-CR | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TPSEVCXJ6T.bfccba | AL-CR | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BCJLH5QZP3.d32fe6 | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ERGDTKCCNO.264eef | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HPNGKBHL7Q.f40eee | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PIKWTIFFLT.0c987a | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QBXP4WN4EH.f2ff8b | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RIU6VQODTD.ec765d | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SCXLN5PW5J.1bdf6b | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UAONAY6USS.a6d089 | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UGHIJTFJXQ.dee5a9 | AL-NI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4LYM3FC7EW.ba70fc | AU-ND | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-APHPP3C3IL.0b882d | AU-ND | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JNZZAVNKJJ.49915b | AU-ND | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-262GCABU7L | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DMD7RF3IBZ | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EL4VDF662N | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NBCIEUTCHZ | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OZWB7UDBBD | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-R4DSGDB3W4 | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UY6NZBD3L7 | B-SI | ACR_B | 1850.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5MBL67NU55.5620c6 | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5VLZZSK2FU.079ecd | BI-K | SM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5VLZZSK2FU.399489 | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5VLZZSK2FU.a87d23 | BI-K | HM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-65FTHM43WD.d661d3 | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AP6PJYWU2A.14b173 | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AP6PJYWU2A.b4b400 | BI-K | HM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AP6PJYWU2A.f4e1b3 | BI-K | SM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GPYTLM7TMH.23591c | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JHECAZUR7A.527387 | BI-K | HM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JHECAZUR7A.751186 | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JHECAZUR7A.ac9bb7 | BI-K | SM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-K4G26RVS4P.18a8e8 | BI-K | HM_FORM | 848.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-K4G26RVS4P.3eff03 | BI-K | SM_FORM | 848.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-K4G26RVS4P.d612d4 | BI-K | GM_FORM | 848.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KEI2TY2L4J.003dd8 | BI-K | SM_FORM | 838.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KEI2TY2L4J.310176 | BI-K | GM_FORM | 838.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KEI2TY2L4J.ced61f | BI-K | HM_FORM | 838.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MVMC4LLIGK.deb7c0 | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OAM7DL5O44.0f9db3 | BI-K | HM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OAM7DL5O44.a1313c | BI-K | GM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OAM7DL5O44.db5826 | BI-K | SM_FORM | 523.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2MQEBRH4MW.53083f | BI-RB | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2MQEBRH4MW.7fce1e | BI-RB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3JGPW3I75H.79df58 | BI-RB | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3JGPW3I75H.d8dc51 | BI-RB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5OEWEA7JA4.0e62fc | BI-RB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5OEWEA7JA4.0f40fc | BI-RB | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5Q5G5NGQUV.a3c26f | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6SOWRE2DF4.43ed25 | BI-RB | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6SOWRE2DF4.eb809d | BI-RB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CICR2FUSVJ.5d0ce4 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CYOIAGTFBT.122505 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EGCH5YBO5T.03ad05 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JJASL6SBZV.20705f | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NJQHVOUU4B.d4aacb | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ODSRRXR4DB.041e13 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Q55RWEY7ZE.93dead | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-R23YOSUSUV.108eb5 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RZXTTI2S6E.066d6f | BI-RB | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RZXTTI2S6E.7086a3 | BI-RB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-V7JKB5ZQ5Q.3fc1d9 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VJRN7UJYRI.3344ce | BI-RB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VJRN7UJYRI.5a24cf | BI-RB | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WDCIWRCJKL.c59dd4 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YVCSYC5JGI.be63a9 | BI-RB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3KKWBH2XDZ.a50d24 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3KKWBH2XDZ.da1fa1 | C-SI-Y | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4GRDKBOGIM.e82b52 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5J5H3KGZYE.686fb4 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6S6FJDBDPS.2a7f92 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6S6FJDBDPS.833e67 | C-SI-Y | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AYWJZHYTRS.5bb1a2 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AYWJZHYTRS.c62495 | C-SI-Y | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BFAMJ2DIA5.63b8f1 | C-SI-Y | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BFAMJ2DIA5.dd461e | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DI7K5WNBQD.81f28b | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DSMEXZLUVF.ff4fc5 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-M5W5YRWCXR.430153 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RBLTNNPVR3.1458d7 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RHK3CZSOYD.ab3ff7 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-URIPMRCZ3I.873a14 | C-SI-Y | SM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-URIPMRCZ3I.c86db4 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-W37THFZ6PU.7829dc | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZQPMERZ45A.ac8ea8 | C-SI-Y | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2ALE6E3FVH.9cfe61 | CR-GE | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2J4IQSP6P5.6ab015 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-57NY3YXVJ7.f9f7d0 | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5DSEUH4NK2.275607 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5L35TGCFAL.3e96d3 | CR-GE | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-6HTTW5327W.8ad375 | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AET63ATDZX.30d5a8 | CR-GE | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-D4GO4RDBQ3.f911d1 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-D6O6WD7FEM.052b22 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JC43FO644N.5d5d8e | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JJU3CGVLU7.772065 | CR-GE | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JUOGYNLXX5.a35513 | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RRUITAEIYM.35c951 | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SHBHPLOWRZ.496f37 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SQKDM2MIIO.51bcd7 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VYDTBVQGR6.32fd53 | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WQZPJRIYBP.488bdc | CR-GE | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZDS7SVJW37.79f712 | CR-GE | GM_FORM | 1530.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7SDDUNMFWD | CR-NB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BKJI2BHPNQ | CR-NB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KDA4DDUPS3 | CR-NB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QSJGIAPGCT | CR-NB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XFMFG5NJ7G | CR-NB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CVGPP2EES2.280500 | CR-V | CPM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CVGPP2EES2.902166 | CR-V | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EPYUWME3S2.4b91f9 | CR-V | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EPYUWME3S2.d891c2 | CR-V | CPM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HLSQ32LD7W.813e3a | CR-V | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HLSQ32LD7W.9589eb | CR-V | CPM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HRCXWJ5ASY.680328 | CR-V | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HRCXWJ5ASY.fb9198 | CR-V | CPM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MFUTBPJ73V.867731 | CR-V | CPM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MFUTBPJ73V.a91205 | CR-V | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NKAWVPI72A.406946 | CR-V | SM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NKAWVPI72A.a2b053 | CR-V | CPM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-43ZXOO6TFO.c1da95 | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-43ZXOO6TFO.d25966 | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-636TFSTTTX.64e6ca | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-636TFSTTTX.a31e4b | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FTGB7HG7ZE.c1e902 | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FTGB7HG7ZE.e0fe5c | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FTGB7HG7ZE.fa678e | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IDEY4NU7GH.0ddf07 | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IDEY4NU7GH.3196e3 | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IDEY4NU7GH.aa996e | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LF2XK4HKT2.17a006 | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LF2XK4HKT2.7c05fe | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NGZLBXOCTJ.613025 | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NGZLBXOCTJ.6f1c6d | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NGZLBXOCTJ.ee8fe3 | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QEFWZ76HIE.18e71a | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QEFWZ76HIE.25d578 | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QEFWZ76HIE.844e24 | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RAE3344I7N.0a32c2 | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RAE3344I7N.a9a93b | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SVOB5GY4NR.734cec | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SVOB5GY4NR.85215a | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SVOB5GY4NR.d57558 | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TSATJTWL4X.4b9f2c | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TSATJTWL4X.842a3b | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TSATJTWL4X.9a4273 | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UCYL5M5YMQ.61e4c5 | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UCYL5M5YMQ.b53a6b | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UCYL5M5YMQ.c95b85 | CS-O | CPM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VICVK7W5MI.6cff0e | CS-O | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VICVK7W5MI.c96f7a | CS-O | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LEVZKAYSFQ.76f04c | CS-TE | SM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DJCHWQNF3R.a8739c | FE-TI | HM_FORM | 1413.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RYYYSEVZSO.6d6e7c | FE-TI | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DFCHE5IR2.a7aade | FE-TM | HM_FORM | 290.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DFCHE5IR2.d6a983 | FE-TM | SM_FORM | 290.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3DFCHE5IR2.dad4ef | FE-TM | CPM | 290.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NUHO6HHWO3.8d6938 | FE-TM | SM_FORM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NUHO6HHWO3.bb76c0 | FE-TM | CPM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NUHO6HHWO3.e1eca4 | FE-TM | HM_FORM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NETNWIDKUE.044cb9 | FE-ZR | HM_FORM | 1760.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RRX24TAHOT.400de0 | FE-ZR | HM_FORM | 1023.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2UHOWSMDDM.b7e4b7 | GA-HO | HM_FORM | 681.575 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QHNKBTS4T7.6f1e99 | GA-HO | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Y5TEVW6D4C.f58ae3 | GA-HO | HM_FORM | 681.575 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3LN5K7OCWU.2a56b0 | GE-HF | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EJJIXFDHZY.f0b9f8 | GE-HF | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-F6U6L6LQZN.c79ebf | GE-HF | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KL7IRCD7WF.dd55f8 | GE-HF | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MH3ZIMSBFC.ea378c | GE-HF | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PBO5HTNEEN.b6b6cd | GE-HF | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RD3CLV2FOT.fee459 | GE-HF | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RZGNU7RZXQ.4c1a19 | GE-HF | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UMF5FHBZ2R.6eda5e | GE-HF | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-Y7MO2KTGBD.8c92ae | GE-HF | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZO7V5BPXHS.df129d | GE-HF | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BITKOMNVUS.8c970c | GE-LI | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PSEXKKFKOW.574362 | GE-LI | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WZQAODEBEC.6a64ec | GE-LI | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GVZJCFBURB.ced65a | HF-SI | HM_FORM | 1473.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NSLZ5NLCAN.17527b | HF-SI | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SYPHVE2N5D.9720a9 | HF-SI | HM_FORM | 1473.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VWFCJHEUZJ.cbdee4 | HF-SI | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2XJVL52ZZS.8a49ec | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-324KCUAJTB.3c7513 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3UMK4HZRHK.4928c5 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5BEUS7NSSP.657f69 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-72TKN3UOG6.8e6d92 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-7DDF6Q6O6J.a13d6d | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-A23FUSO6HP.701cb7 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AD34SRG5AB.4e4eb1 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AUKWBMGA5C.ddb196 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-B3Q76Q3ZNH.3e8bee | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-B4MUY4LNTZ.6b353a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CXYDLQ5DZE.5e0076 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-DQJUDST43Z.23b999 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-F4A2JMFGJH.47c2b7 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FIQ7BNHLFU.2b0752 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FLDGSBRCAK.4cf0d5 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HP5KPJAVEK.9ecfe3 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-J3XQAQG2DV | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JPQRPXNF4U.9e674a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JSGTH7ITUZ.a20ce5 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-JWQOTXG67W.d3263a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KCYHXEXQUE.c6b756 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KLVT4YVNCO.525ff5 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KQZDNZX2AN.7d9243 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KSRPGL5RCD.08c1f4 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KUECU2UA5L.6cda4d | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LXN3IADT6Q.c6f1fe | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MMQ6QORTQE.0773c8 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NLSMYGH5C7.fc2d47 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-O57HKFBW6L.5a177a | LI-SB | HM_MIX | 1080.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OFFT32GZKH.eb17b8 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OGB5BHFJ44.96025e | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PCZK7MQCTV.e272ce | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PQYY3PUVQT.6a1839 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QWK44342WG | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RLTCUJXUAN.d9082c | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-RODXZPLBGU.d0b4d5 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-SCT4AX4CNS.161b8b | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TWOHK3267T.acff3c | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U46GIDWBAC.033dbe | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-U4AXTSYQAU.da0512 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UBFXLGUDF3.b80801 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VF4OBQG2UZ.338fcb | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-W7NAOHTXW5.edde5a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-W7XE3PEZ6P.21c0d6 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WLL5KIGXCE.bec4ac | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WNJNP47VAM.3fac9e | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YF5XFHR4R5.8a2c7a | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YFEPYD4OTH.790ebb | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZGOVESY4GA.9f76f9 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZOINEUQ6R5.fbd9e8 | LI-SB | HM_MIX | 979.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MEFBATBWAD.a50595 | MG-PB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MEFBATBWAD.e8a34c | MG-PB | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5CWK34HTUC.8cfd0c | NI-SC | HM_FORM | 1473.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CFKKFJWLEZ.915aea | NI-SC | HM_FORM | 1473.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-35KKCWXTVK.bdfc92 | NI-SM | HM_FORM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-C6LZ36ISCC.09c256 | NI-SM | HM_FORM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-EENBV6JOTY.a7d9ec | NI-SM | HM_FORM | 1473.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-H5OATTV4YI.99a5c9 | NI-SM | HM_FORM | 1473.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-TQH35NFF7E.fdae45 | NI-SM | HM_FORM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-UHMYIGYWKU.f02841 | NI-SM | HM_FORM | 300.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-4R2G2JJ6I6.1d4316 | NI-TI | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-L2OPU6DDBU.9ae0f2 | NI-TI | HM_FORM | 0.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-PEPGNW2DTY.12bb23 | NI-TI | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YEW6RRQCYU.864b86 | NI-TI | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-2VYYLCJG6B.fc601c | NI-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3NOZAMJ6QA.4def27 | NI-YB | HM_FORM | 990.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3NOZAMJ6QA.c063a9 | NI-YB | SM_FORM | 990.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5DLLBJSKHU.821a7b | NI-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ATWHHONLGM.201ce6 | NI-YB | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ATWHHONLGM.b5d4b2 | NI-YB | SM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BDP3R2S4AJ.45efe5 | NI-YB | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-BDP3R2S4AJ.e7767e | NI-YB | SM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CROH3CJWUG.38377e | NI-YB | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CROH3CJWUG.8b59de | NI-YB | SM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-FK52QONVEP.49d2b3 | NI-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KQAQJSXIUR.8d6ca1 | NI-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MAQJCN6KZA.97cc57 | NI-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QE7M3FV2JX.4f533a | NI-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-T6WAJSN2ID.111f82 | NI-YB | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-T6WAJSN2ID.e1a6fc | NI-YB | SM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XIHXMIOGKA.192321 | NI-YB | SM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-XIHXMIOGKA.43ccac | NI-YB | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-3IWLINAN5P.3739f4 | PD-SN | HM_FORM | 273.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IOZPT2WUPA.0a6d96 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-IRVRKYRVYA.463463 | PD-SN | HM_FORM | 273.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KGEHUOP3SH.ce8c47 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LDP5O2JGT6.334ca4 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-LQN7YN3PVS.efd894 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-QBTBTA576Y.dd4485 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WQH6W53A6M.7c73a7 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YQ6CITKJYH.fe0799 | PD-SN | HM_FORM | 273.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-ZLK2AFKPJQ.1de261 | PD-SN | HM_FORM | 320.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-AZHIIJFVVN.b7673e | PU-U | CPM | 773.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-K3HZTEHG2L.a59b0d | PU-U | CPM | 673.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KSXPAH2RSB.96e5b4 | PU-U | CPM | 840.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MBFNTRXGAI.f9d105 | SB-YB | HM_FORM | 298.15 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5BVWOE3YM2.eba333 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-5VW6EUBSRK.28fd2f | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-C4KDRUOFUL.e2ea1b | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CDZ7HLXDBU.aaa45b | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GBX5IRSDAR.880e53 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GNQ4UPZMQ2.3753c5 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-GOJ3G4HACO.48bc61 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HCFOJHG4OH.1b136d | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MF7LDLWXCM.e09079 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-NIY3C4KGUT.8bbb50 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-O4XZBZ3GQN.82bb37 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-R5R6OJDLAW.bde4e8 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VELCVCLWDK.09d35b | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-VFQ3MRKMJK.4536f9 | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-YNLI4WOAVZ.6bf51d | SI-SR | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OLNLWPIRLP.68d05f | SI-TA | SM | 1760.5 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-OLNLWPIRLP.d4d902 | SI-TA | HM_FORM | 1760.5 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-CYNYBUMDH2.1ce302 | TE-TL | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-HPF2C7PFZM.e5279b | TE-TL | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-KOZWZVEI53.9304b4 | TE-TL | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-MEYGLBV6G2.ca9876 | TE-TL | HM_FORM | 298.0 | UNKNOWN | phase_not_printed | no phase label printed and the caption does not name the liquid |
| ORC-WA3UP3Y5DA | AG-Y | INVARIANT_TEMPERATURE | 294.65 | L, Ag51Y14 | temperature_implausible | phase equilibrium at 294.65 K, below 0.25 x the lowest element melting point (1234.93 K) |
| ORC-Y7K62CLAB6 | AL-SR | INVARIANT_TEMPERATURE | 25.0 | SrAl4, L | temperature_implausible | phase equilibrium at 25 K, below 0.25 x the lowest element melting point (933.47 K) |
| ORC-54NIJNKQKM | B-TA | INVARIANT_TEMPERATURE | 22.5 | L, TaB(rt), Ta2B | temperature_implausible | phase equilibrium at 22.5 K, below 0.25 x the lowest element melting point (2348 K) |
| ORC-OEJI7W4XQX | B-TA | INVARIANT_TEMPERATURE | 18.0 | L, Ta2B, BCC | temperature_implausible | phase equilibrium at 18 K, below 0.25 x the lowest element melting point (2348 K) |
| ORC-OQGSFBFO3Y | MG-SI | INVARIANT_TEMPERATURE | 0.0 | L, Mg (hcp), Mg2Si | temperature_implausible | T = 0 K is not a temperature of a measured state (zero or a composition) |
| ORC-YUMIW22Y2P | MG-SI | INVARIANT_TEMPERATURE | 0.333 | L, Mg2Si | temperature_implausible | T = 0.333 K is not a temperature of a measured state (zero or a composition) |

