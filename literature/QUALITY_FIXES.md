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

