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

Formation enthalpies (kJ/mol-atom, experimental / model / unspecified) whose single binary formula matches a Materials Project or OQMD entry and that differ from DFT by more than 50 kJ/mol-atom, or have the opposite sign with |DFT - lit| > 10 (228 records), classified in this order:

* `basis_corrected_from_formula`: removed in audit round 2 (2026-10-24). The rule accepted a per-formula / per-atom conversion only when the converted value landed within 15 kJ/mol-atom of DFT, and the converted values then calibrated the DFT error (circular). The basis is now read on the page, one decision per printed column (`tools/literature_r2_thermo.py`, ledger keys `table_basis:<asset>`; gate R2 in the gates section).
* `sign_from_heading` (0): printed without a minus sign, -lit within 15 of DFT, and the record's printed heading carries the minus (e.g. "-ΔfH"): sign applied, heading in `sign_heading_printed`.
* `unsigned_in_print` (31): printed without a minus sign, -lit within 15 of DFT (and lit itself more than twice that far, so small values near zero are not classified), no negated heading in the record: value kept as printed, flagged, excluded from the default parity set.
* `dft_outlier_unexplained` (197): no rule applies; flagged `flags.dft_outlier_unexplained`, value unchanged.

| id | class | formula | before | after | evidence |
|---|---|---|---:|---:|---|
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
| ORC-JDJTGHPS4K | dft_outlier_unexplained | HfB | -98.95 | -98.95 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-N2BPBLFSN3 | dft_outlier_unexplained | Mg2B | -0.01423 | -0.01423 | no deterministic rule applies (DFT OQMD 24.1) |
| ORC-2QS3QXVB7F | dft_outlier_unexplained | Re2Si | -19.367 | -19.367 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-FLO5GRSVGD | dft_outlier_unexplained | Re2Si | -22.7 | -22.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-LUJ7XZ7YH3 | dft_outlier_unexplained | Re2Si | -22.0 | -22.0 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-QRHLTLQTBM | dft_outlier_unexplained | Re2Si | -19.7 | -19.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-TGOMFDVI6F | dft_outlier_unexplained | Re2Si | -20.0 | -20.0 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-VN47E3AARD.9cef4e | dft_outlier_unexplained | Re2Si | -12.7 | -12.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-VN47E3AARD.f5a708 | dft_outlier_unexplained | Re2Si | -12.7 | -12.7 | no deterministic rule applies (DFT MP 12.8, OQMD -21.9) |
| ORC-7BRGOIHAWY | dft_outlier_unexplained | Ta3B2 | -13.5294 | -13.5294 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-JNRM625MX5 | dft_outlier_unexplained | Ta3B4 | -10.88742857 | -10.88742857 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-KM6Q5LMCOG | dft_outlier_unexplained | Ta3B4 | -11.43642857 | -11.43642857 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-VGMMQLZODX | dft_outlier_unexplained | Ta3B2 | -14.26 | -14.26 | per-formula reading would match DFT but the printed unit is explicitly per atom |
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
| ORC-2XXL6EGLXQ.a44990 | dft_outlier_unexplained | CaO2(cr) | -659.0 | -659.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-EONGZNVMF4.e5cd6e | dft_outlier_unexplained | CaO2(cr) | -648.1 | -648.1 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-FDK7VGPM2Z.234c60 | dft_outlier_unexplained | CaO(cr) | -635.1 | -635.1 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-IOMQXHHZHX.39b429 | dft_outlier_unexplained | CaO2(cr) | -652.7 | -652.7 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-MOABLTWFHR.fd3a6b | dft_outlier_unexplained | CaO(cr) | -634.0 | -634.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-N6RZ52LOV5.b9b0c1 | dft_outlier_unexplained | CaO(cr) | -634.6 | -634.6 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XQRAM3624L | dft_outlier_unexplained | CaO(cr) | -634.0 | -634.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-YHMSI6IKE4.81e7a6 | dft_outlier_unexplained | CaO(cr) | -635.1 | -635.1 | per-formula reading would match DFT but the printed unit is explicitly per atom |
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
| ORC-4TQ3RYV4BP | dft_outlier_unexplained | CuO | -152.3 | -152.3 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-AJGT674S4D.aad2e0 | dft_outlier_unexplained | CuO | -155.77 | -155.77 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-AJGT674S4D.b11196 | dft_outlier_unexplained | Cu2O | -170.83 | -170.83 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-ALFTX6OZRM.1e7619 | dft_outlier_unexplained | CuO | -161.71 | -161.71 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-ALFTX6OZRM.279a7f | dft_outlier_unexplained | Cu2O | -173.18 | -173.18 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-ALFTX6OZRM.b67909 | dft_outlier_unexplained | CuO | -157.07 | -157.07 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-C7MXYNKNHW | dft_outlier_unexplained | CuO | -156.06 | -156.06 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-GMNQNEO2HB | dft_outlier_unexplained | CuO | -155.48 | -155.48 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-I5UR2MQHUO | dft_outlier_unexplained | CuO | -157.07 | -157.07 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-J56QLHWYW7 | dft_outlier_unexplained | CuO | -161.08 | -161.08 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-LAWLJGIQGF | dft_outlier_unexplained | CuO | -154.03 | -154.03 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-LGOKEWXJHR.56dd6b | dft_outlier_unexplained | Cu2O | -164.85 | -164.85 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-LGOKEWXJHR.e36160 | dft_outlier_unexplained | CuO | -152.3 | -152.3 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-PYVAEHKD5K | dft_outlier_unexplained | CuO | -138.16 | -138.16 | no deterministic rule applies (DFT MP -91.0, OQMD -80.2) |
| ORC-QQXJ6OCZ6G | dft_outlier_unexplained | CuO | -155.77 | -155.77 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-QZDH5SGEEG | dft_outlier_unexplained | CuO | -155.19 | -155.19 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-SNTTKLS5GR.c8b64e | dft_outlier_unexplained | Cu2O | -170.26 | -170.26 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-SNTTKLS5GR.ce4045 | dft_outlier_unexplained | CuO | -155.19 | -155.19 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-T4WZFE2TJJ.006290 | dft_outlier_unexplained | CuO | -155.48 | -155.48 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-T4WZFE2TJJ.eef88f | dft_outlier_unexplained | Cu2O | -170.29 | -170.29 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-UDWXTWFN6Y.049c73 | dft_outlier_unexplained | CuO | -154.03 | -154.03 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-UDWXTWFN6Y.223526 | dft_outlier_unexplained | Cu2O | -172.48 | -172.48 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-UEENQAKLM2.5a9513 | dft_outlier_unexplained | Cu2O | -179.91 | -179.91 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-UEENQAKLM2.d6b8e9 | dft_outlier_unexplained | CuO | -138.16 | -138.16 | no deterministic rule applies (DFT MP -91.0, OQMD -80.2) |
| ORC-UQ5FDHCSKH | dft_outlier_unexplained | CuO | -161.71 | -161.71 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XCCWO6H7LI.d9fe69 | dft_outlier_unexplained | Cu2O | -170.71 | -170.71 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-XCCWO6H7LI.fa10e4 | dft_outlier_unexplained | CuO | -156.06 | -156.06 | per-formula reading would match DFT but the printed unit is explicitly per atom |
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
| ORC-2BKKRXR33O | dft_outlier_unexplained | Li2O2 | -632.62 | -632.62 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-6MGAPSXOS4 | dft_outlier_unexplained | Li2O | -597.0 | -597.0 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-AKI6NGQPUL | dft_outlier_unexplained | Li2O | -598.73 | -598.73 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-AZT4WLCRAM | dft_outlier_unexplained | Li2O | -597.902 | -597.902 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-C5DY6KUUTC | dft_outlier_unexplained | Li2O2 | -644.28 | -644.28 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-CBPWWARGVT | dft_outlier_unexplained | Li2O2 | -605.9 | -605.9 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-CLLKMPH32B | dft_outlier_unexplained | Li2O | -597.48 | -597.48 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-OCTG4OQW4X | dft_outlier_unexplained | Li2O2 | -632.62 | -632.62 | per-formula reading would match DFT but the printed unit is explicitly per atom |
| ORC-ZL6CQL3CB7 | dft_outlier_unexplained | Li2O | -596.5 | -596.5 | per-formula reading would match DFT but the printed unit is explicitly per atom |
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
| blocked_by_flag | 275 |
| blocked_by_flag_phase_identity_missing | 260 |
| blocked_by_flag_terminal_phase_mapping_unresolved | 15 |
| espei_certified | 1892 |
| espei_ready | 11161 |
| espei_ready_calphad_disagrees | 319 |
| espei_ready_no_prediction | 9348 |
| phase_rule_fail_compound_property_not_fittable | 407 |
| phase_rule_fail_liquid_impossible_at_T | 3 |
| phase_rule_fail_phase_label_ambiguous | 78 |
| phase_rule_fail_phase_label_not_mapped | 545 |
| phase_rule_pass | 11559 |

Values whose `espei_ready` the phase rule turned false:

| id | system | property | T (K) | printed labels | reason | detail |
|---|---|---|---:|---|---|---|
| ORC-2ARHPO6ULI.9c5c44 | AG-PB | CPM | 680.646 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-2HZ4HO7VKQ.eca7c0 | AG-PB | CPM | 917.968 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3DTAFVIJ57.14fb4f | AG-PB | CPM | 674.664 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3DTHACXC4T.d9eb4c | AG-PB | CPM | 642.769 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3LN4ERBOIM.6a4804 | AG-PB | CPM | 728.523 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-44RRBDE2J3.127e38 | AG-PB | CPM | 686.632 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-4DHTNZ4RGV.74ef13 | AG-PB | CPM | 882.066 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-4PVRTK5W6F.11db0b | AG-PB | CPM | 951.866 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-4QJKHOGSFE.8b7647 | AG-PB | CPM | 798.296 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-4QN3QJYDQA.78bec4 | AG-PB | CPM | 929.937 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-4THI2UYU76.f00a6e | AG-PB | CPM | 770.407 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-4ZMIAUXC6R.1fb3e3 | AG-PB | CPM | 900.015 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-5G35LAPOWB.8d495e | AG-PB | CPM | 684.636 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-5IQH544QDY.cd6539 | AG-PB | CPM | 874.089 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-6SVBLFA6BT.a72bb3 | AG-PB | CPM | 872.094 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-6WLYXL2FQA.20d5f6 | AG-PB | CPM | 808.271 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-73IVDAIKMQ.e48566 | AG-PB | CPM | 712.563 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-76ZT2FWALX.d61cf5 | AG-PB | CPM | 953.859 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7BB4CKBGHU.edf08e | AG-PB | CPM | 898.023 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7G2K4CJPY5.576e46 | AG-PB | CPM | 774.375 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7K6DEW2CLD.65a739 | AG-PB | CPM | 886.057 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7KPULGBBA4.5ee390 | AG-PB | CPM | 778.359 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7MCNUQTPUQ.890fa0 | AG-PB | CPM | 935.923 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7OIUJD4DZG.24a84c | AG-PB | CPM | 664.696 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7XP3AX7IK2.32cb0d | AG-PB | CPM | 909.988 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-AB5MDPD4FL.4ae0da | AG-PB | CPM | 748.467 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ANPS4KLMKO.6ff3bc | AG-PB | CPM | 692.614 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ANUGQC7BJO.f599de | AG-PB | CPM | 820.231 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-AWW23FBCHH.06e20e | AG-PB | CPM | 660.709 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-B7PCQBKCNB.7144e0 | AG-PB | CPM | 702.59 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-BIIJFGEOB5.ae8679 | AG-PB | CPM | 840.175 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-BNTYA7EMG3.9cff4c | AG-PB | CPM | 698.596 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-BUHNMWLZCZ.1fd5d7 | AG-PB | CPM | 856.135 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-BWHINBDKJR.914d42 | AG-PB | CPM | 704.583 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-BX5FPVVQIV.480dfe | AG-PB | CPM | 961.838 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-C2X4WAPT5Q.6b3efa | AG-PB | CPM | 700.593 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CFDTEF4RTJ.d8a47b | AG-PB | CPM | 720.543 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CMHLS3QI77.d5fc45 | AG-PB | CPM | 750.461 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CP5N3NWNTK.c581fc | AG-PB | CPM | 925.946 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CPTWEBCT4N.aa8394 | AG-PB | CPM | 848.155 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CX2B7EYOFW.318d1c | AG-PB | CPM | 902.011 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-D7G7L6WRQE.dd6287 | AG-PB | CPM | 830.199 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DBSAYIEL4U.643b6c | AG-PB | CPM | 832.193 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DEK6AYBJHT.43efd5 | AG-PB | CPM | 931.931 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DG2PEM2S2X.6e6130 | AG-PB | CPM | 941.902 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DPGBPT3V25.90b818 | AG-PB | CPM | 816.244 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DR3BILJDS2.49b7af | AG-PB | CPM | 690.62 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DT3W5U462R.1a4b8c | AG-PB | CPM | 894.037 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DTG2NLHDOA.425856 | AG-PB | CPM | 955.852 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DVMRXMFPWW.341a8c | AG-PB | CPM | 740.495 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DW3WA5UZ2E.223222 | AG-PB | CPM | 746.473 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-E7J5DCWKP6.01269b | AG-PB | CPM | 868.103 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-EOKHJKO32F.3e36bd | AG-PB | CPM | 760.435 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ES52JMIQRA.5a9a84 | AG-PB | CPM | 826.214 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-EVWFSM6URM.f2783d | AG-PB | CPM | 818.237 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-F25SXBIYWD.29e35c | AG-PB | CPM | 734.507 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-F43ZTPAGRR.c7551c | AG-PB | CPM | 864.117 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FD6ERMCM5M.8f7ef1 | AG-PB | CPM | 919.962 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FEGVM5GGM4.abb3f6 | AG-PB | CPM | 764.423 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FIMHIPPOLZ.f3cf8a | AG-PB | CPM | 892.04 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FJCKTDLWSS.8c0d76 | AG-PB | CPM | 634.791 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FMO26DINAI.075ace | AG-PB | CPM | 696.603 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FWY2SEEVQ2.c0e634 | AG-PB | CPM | 678.651 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FX5JGS2X4Z.a9c91d | AG-PB | CPM | 650.744 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FXYTFJCBFB.443bd6 | AG-PB | CPM | 806.275 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-G26IFHJTTF.041b5d | AG-PB | CPM | 947.882 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-G47SYJZMSP.3ad3f8 | AG-PB | CPM | 772.403 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-GACCIRXF2N.a60fcd | AG-PB | CPM | 963.83 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-GCSXGCEUZY.26413d | AG-PB | CPM | 854.14 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-GO6SQI7PIT.da36f5 | AG-PB | CPM | 732.512 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-GYPW6QVUJV.3de26d | AG-PB | CPM | 822.225 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-H5HXDBZOED.578fff | AG-PB | CPM | 718.549 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HICGZP6YMM.af8370 | AG-PB | CPM | 738.496 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HLLVOCEUYM.a6cbeb | AG-PB | CPM | 644.761 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HORFYHR2KI.8c026c | AG-PB | CPM | 708.572 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HQWLBCQIBY.a4cf3f | AG-PB | CPM | 654.732 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-INNY76UX7G.d6246b | AG-PB | CPM | 943.897 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-IZ45Z5LUWX.8bf049 | AG-PB | CPM | 858.13 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-J5GO7LZIPM.491b25 | AG-PB | CPM | 862.122 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-J6H4EQXXAS.01826f | AG-PB | CPM | 812.26 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-J7GW2ZTWE2.d1f409 | AG-PB | CPM | 896.032 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JBTX3RU756.5b1313 | AG-PB | CPM | 814.253 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JMF7UEXZGW.e70d3a | AG-PB | CPM | 834.189 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JOJC77ELUW.4a1f57 | AG-PB | CPM | 752.457 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JQDOBITKUH.d6c083 | AG-PB | CPM | 937.917 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JTIG6SA6N7.cbc285 | AG-PB | CPM | 730.516 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KDDUX3YVXS.d433ed | AG-PB | CPM | 754.452 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KT473ORKEL.c08409 | AG-PB | CPM | 762.429 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KZ236DSTN3.bde1ff | AG-PB | CPM | 688.627 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-L7W2FWUUAG.daaf97 | AG-PB | CPM | 880.071 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-LTM345PTHJ.09528e | AG-PB | CPM | 866.112 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-LUV7WT4PIM.ed894f | AG-PB | CPM | 878.076 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-LW4YQECFOW.067678 | AG-PB | CPM | 888.052 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-M3EMMXWKI5.5f07f4 | AG-PB | CPM | 776.366 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-M3NHBGRPD3.496db3 | AG-PB | CPM | 768.411 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MCRPXOH7QK.e9edec | AG-PB | CPM | 927.942 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MITYBTEMHY.fcc4f4 | AG-PB | CPM | 676.658 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MJ4OKSE2PO.d25102 | AG-PB | CPM | 915.974 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MKTYSCGYUI.5125b7 | AG-PB | CPM | 846.161 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MP5JWNP5WT.d1e4ff | AG-PB | CPM | 766.417 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MRURU6UP3U.d84dd6 | AG-PB | CPM | 939.909 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MTVLG7PHWW.aac8c7 | AG-PB | CPM | 876.081 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-N3Y4FECV2I.ae0ffd | AG-PB | CPM | 758.439 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-N5CR2YJPFK.67c26b | AG-PB | CPM | 824.22 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NLWT6JLS3U.3092c3 | AG-PB | CPM | 672.669 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NPKLDCXGQX.01716c | AG-PB | CPM | 670.673 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NPOEMECNIQ.059c2c | AG-PB | CPM | 726.53 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NXN562PQJK.4d5010 | AG-PB | CPM | 710.567 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-O5GRRVAREL.a2d65d | AG-PB | CPM | 744.482 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OCVZNJN45Q.7cec6b | AG-PB | CPM | 724.534 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OIXPZTKC6J.47f1bf | AG-PB | CPM | 965.825 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OOJTOZE6NG.bc679a | AG-PB | CPM | 714.558 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OPELXV3XPC.72670e | AG-PB | CPM | 790.318 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PHJBV4QMWD.deda7e | AG-PB | CPM | 836.186 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PJD6DGUC2G.38984c | AG-PB | CPM | 636.787 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-POUB35V4H2.df5da9 | AG-PB | CPM | 666.69 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PQORXAAKDA.a44883 | AG-PB | CPM | 933.927 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PRQP2MPCBB.9a7973 | AG-PB | CPM | 800.291 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PU7P3TBJPC.a0419c | AG-PB | CPM | 736.499 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PUOQS2ITTA.77ec8d | AG-PB | CPM | 949.874 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-Q3OG23H5JP.aa4378 | AG-PB | CPM | 780.354 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-Q3SAPDQ4BY.c98efb | AG-PB | CPM | 782.349 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-QLI5ATQBRP.ffe8e9 | AG-PB | CPM | 716.553 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-R2SGFHFUJ4.8cad09 | AG-PB | CPM | 646.753 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RBS5T6XIB7.66bcd9 | AG-PB | CPM | 722.537 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RGGOFP6WR6.b81676 | AG-PB | CPM | 794.308 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RHTRM4DYHC.ec7d45 | AG-PB | CPM | 796.301 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RVEZT323R6.d0dd7f | AG-PB | CPM | 921.957 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RZBPECWZJL.0e07b2 | AG-PB | CPM | 852.144 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SABGQAJGD7.434714 | AG-PB | CPM | 786.334 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SKRKBZPI3V.242a51 | AG-PB | CPM | 802.285 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SOM3EGJ5MP.daa54c | AG-PB | CPM | 844.17 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SONTENM4OP.34e071 | AG-PB | CPM | 884.062 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SYX7Q55QKO.0d0b8c | AG-PB | CPM | 788.326 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SYZRQBCMDO.d3ae3e | AG-PB | CPM | 923.952 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-TTCXNTB3JN.1e072f | AG-PB | CPM | 860.127 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-TWVU6UDAHE.9ffbb1 | AG-PB | CPM | 890.044 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U2SB3OMRQC.f8541c | AG-PB | CPM | 658.716 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U34WNUTREE.43f53d | AG-PB | CPM | 967.821 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U3AQJEJZZ2.fb77fd | AG-PB | CPM | 694.609 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-UMQDJURRN5.f8ac24 | AG-PB | CPM | 632.8 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-UOGOZHS3CR.2ff711 | AG-PB | CPM | 911.983 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-US4CZCJ2G3.89221a | AG-PB | CPM | 662.703 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-UVLNHUJXLJ.3839d3 | AG-PB | CPM | 969.817 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-UZOADQR4I6.9ed416 | AG-PB | CPM | 656.725 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-VDJVY6CKDP.88195a | AG-PB | CPM | 957.846 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-VGYUCPDBMW.220f83 | AG-PB | CPM | 850.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-VIQFNOP7TZ.c209ad | AG-PB | CPM | 804.28 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-VL2GH3SFHO.64ccb4 | AG-PB | CPM | 652.737 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-W7STQPEGAT.294a52 | AG-PB | CPM | 628.812 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-WAKQG5WET6.8bc51b | AG-PB | CPM | 906.003 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-WII6TFN3VG.84e2c7 | AG-PB | CPM | 682.641 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-WM5GU4Y32R.5e7dea | AG-PB | CPM | 648.75 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-WWOZG4LQIC.191017 | AG-PB | CPM | 959.843 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-XJN35IPW72.a6073f | AG-PB | CPM | 810.264 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-XQPB7D5SLT.b431df | AG-PB | CPM | 945.89 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-Y5KKYQB457.97de3b | AG-PB | CPM | 870.097 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YAZBBKJRDL.a5b45c | AG-PB | CPM | 842.173 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YBWUQOYJZN.6b52fc | AG-PB | CPM | 913.979 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YC2BJ4UHYF.c2fcd8 | AG-PB | CPM | 638.78 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YCJ7TM6BXO.f0d47a | AG-PB | CPM | 838.179 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YPAEL6HQ5X.bf7f84 | AG-PB | CPM | 742.489 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-Z32GWFJIPN.e3dde6 | AG-PB | CPM | 756.444 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-Z5NEOOITTB.e8b692 | AG-PB | CPM | 772.392 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZDH3TQUW5V.d304d9 | AG-PB | CPM | 828.205 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZDINBQ4UML.700954 | AG-PB | CPM | 784.341 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZKF2XKEQJC.b18eed | AG-PB | CPM | 792.314 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZLFZRAVKRJ.95c9d2 | AG-PB | CPM | 630.807 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZNNIRNC3Z6.b814c4 | AG-PB | CPM | 706.577 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZREY6M73OS.606903 | AG-PB | CPM | 668.68 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZWUKVJQNMI.dc9c88 | AG-PB | CPM | 640.774 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3MBBKU43D2 | AG-SM | INVARIANT_TEMPERATURE | 963.15 | Liquid, AgSm, (αSm) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-RUR57CXJV6 | AG-SM | INVARIANT_TEMPERATURE | 948.15 | Liquid, AgSm, (αSm) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-PQA2DGMCJG | AL-CO-MN | INVARIANT_TEMPERATURE | 1425.15 | L, fcc, bcc, β-Mn | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-P3EJ5KLZSF | B | INVARIANT_TEMPERATURE | 2347.15 | L, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-JZSC7PZKIF | B-CE | INVARIANT_TEMPERATURE | 2273.15 | L, B6Ce, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-LHIFK47D7S | B-CE | INVARIANT_TEMPERATURE | 2263.15 | L, B6Ce, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-OC4AQMOVYO | B-CE | INVARIANT_TEMPERATURE | 2273.15 | L, B6Ce, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-PRHT46B2YE | B-CE | INVARIANT_TEMPERATURE | 2263.15 | L, B6Ce, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-QRQSEPE5PI | B-CE | INVARIANT_TEMPERATURE | 2298.15 | L, B6Ce, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-W6AUHMUZZZ | B-CE | INVARIANT_TEMPERATURE | 2473.15 | L, B6Ce, β(B) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-262GCABU7L | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DMD7RF3IBZ | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-EL4VDF662N | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NBCIEUTCHZ | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OZWB7UDBBD | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-R4DSGDB3W4 | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-UY6NZBD3L7 | B-SI | ACR_B | 1850.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-R4NR3HT7Q5 | CO-GE | INVARIANT_TEMPERATURE | 1396.0 | L, α(Co), ε(Co) | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-GIKWBNVYZD | CO-TH | INVARIANT_TEMPERATURE | 1683.15 | L, Co17Th2, αCo | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-HPQQANFDLP | CO-TH | INVARIANT_TEMPERATURE | 1768.15 | L, αCo | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-QQXFHXO7DI | CO-TH | INVARIANT_TEMPERATURE | 1660.15 | L, Co17Th2, αCo | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-YYDEE5TVLQ | CO-TH | INVARIANT_TEMPERATURE | 1768.15 | L, αCo | blocked_by_flag | terminal_phase_mapping_unresolved |
| ORC-CVGPP2EES2.280500 | CR-V | CPM | 298.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-EPYUWME3S2.d891c2 | CR-V | CPM | 298.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HLSQ32LD7W.9589eb | CR-V | CPM | 298.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HRCXWJ5ASY.fb9198 | CR-V | CPM | 298.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MFUTBPJ73V.867731 | CR-V | CPM | 298.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NKAWVPI72A.a2b053 | CR-V | CPM | 298.15 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-27ENRZHFIH.bb8a88 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-2QGHJJNDFX.677f28 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-2XJVL52ZZS.8a49ec | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-324KCUAJTB.3c7513 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3BWGXP6SDT.52e3e9 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3UMK4HZRHK.4928c5 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-3YALOHDNR3.0de3fc | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-5BEUS7NSSP.657f69 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-5EULFO2SNI.7ff09c | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-72TKN3UOG6.8e6d92 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7CQZM6YFNQ.9b6728 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7DDF6Q6O6J.a13d6d | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-7IZSXRGLA5.1e62f8 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-A23FUSO6HP.701cb7 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-AD34SRG5AB.4e4eb1 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-AGU7ATIYGJ.57d46e | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ARISD7LQXQ.8f30cc | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-AUKWBMGA5C.ddb196 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-B3Q76Q3ZNH.3e8bee | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-B4MUY4LNTZ.6b353a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-C64TM3NLHR.d751c9 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CJLV4LOPNF.f82c71 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-CXYDLQ5DZE.5e0076 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DGXTGV74FJ.6ab7ef | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DQJUDST43Z.23b999 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-DSM7RNGM22.155939 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-EGWMVFTMZP.464734 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-EOL5JCK3PY.e00397 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-F4A2JMFGJH.47c2b7 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FIQ7BNHLFU.2b0752 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-FLDGSBRCAK.4cf0d5 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-HP5KPJAVEK.9ecfe3 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-J3XQAQG2DV | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JNPKE2TTDJ.4011b2 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JPQRPXNF4U.9e674a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JSGTH7ITUZ.a20ce5 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-JWQOTXG67W.d3263a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KCYHXEXQUE.c6b756 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KLVT4YVNCO.525ff5 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KQZDNZX2AN.7d9243 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KSRPGL5RCD.08c1f4 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-KUECU2UA5L.6cda4d | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-LXN3IADT6Q.c6f1fe | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-MMQ6QORTQE.0773c8 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-NLSMYGH5C7.fc2d47 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-O57HKFBW6L.5a177a | LI-SB | HM_MIX | 1080.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OFFT32GZKH.eb17b8 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-OGB5BHFJ44.96025e | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PCZK7MQCTV.e272ce | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PJ7QENEB33.439622 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PQYY3PUVQT.6a1839 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-PT3AK5E5VQ.f07da2 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-QWK44342WG | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-REX4O7CVVS.a62422 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RJVTZB7JFG.662ace | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RLTCUJXUAN.d9082c | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-RODXZPLBGU.d0b4d5 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-SCT4AX4CNS.161b8b | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-TSSLBQG7IF.0941a5 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-TWOHK3267T.acff3c | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U46GIDWBAC.033dbe | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U4AXTSYQAU.da0512 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U6YCP2D4CE.814b84 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-U76E3N3IBK.26f8f0 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-UBFXLGUDF3.b80801 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-VCFZCCR356.9b7115 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-VF4OBQG2UZ.338fcb | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-W7NAOHTXW5.edde5a | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-W7XE3PEZ6P.21c0d6 | LI-SB | HM_MIX | 1181.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-WLL5KIGXCE.bec4ac | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-WNJNP47VAM.3fac9e | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YF5XFHR4R5.8a2c7a | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YFEPYD4OTH.790ebb | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-YGRYUHWU3K.44ba39 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZGOVESY4GA.9f76f9 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-ZOINEUQ6R5.fbd9e8 | LI-SB | HM_MIX | 979.0 | UNKNOWN | blocked_by_flag | phase_identity_missing |
| ORC-XCFMJUUOJ7.a0179c | AL-CA | GM_FORM | 800.0 | Al4Ca | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-V7YJ5MPN3I | AL-NI | SM | 298.15 | Al3Ni | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IHDYFUIRSU | B-NB | SM | 298.15 | Nb3B4 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PC4VPHHPN2 | B-NB | SM | 298.15 | Nb3B2 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5VUGUVM3S2 | B-U | CPM | 348.31 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-C6N5EOAVSR | B-U | CPM | 320.84 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-F6SG6DC6YS | B-U | CPM | 340.91 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ID2CY4V6EX | B-U | CPM | 310.6 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SX6ETL5J4Y | B-U | CPM | 300.4 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XK3PPBGLE7 | B-U | CPM | 298.15 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZDI62FNVY5 | B-U | CPM | 330.94 | B2U | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KEI2TY2L4J.c69d64 | BI-K | GM_FORM | 838.0 | Bi2K | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BOPH4LJCD6 | C-SI | SM | 298.15 | αSiC(Hex) | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HHNIMW2TJQ | C-SI | SM | 298.15 | βSiC(Cubic) | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-OYSX326MRK.e94686 | C-U | SM | 298.15 | U2C3 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZDYH7IJLFP.b81126 | C-U | SM | 298.15 | U2C3 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-P5CQER2LTC | C-W | SM | 298.15 | WC | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4T5HFCFJIC | CE-ZN | GM_FORM | 773.15 | CeZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7IY7WMYAU7 | CE-ZN | GM_FORM | 773.15 | CeZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7NGCG5VXFB | CE-ZN | GM_FORM | 773.15 | CeZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BSC7LKZPK4 | CE-ZN | GM_FORM | 773.15 | Ce13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CU7XVBQ4U7 | CE-ZN | GM_FORM | 1173.15 | Ce3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DEWQ4KPVM3 | CE-ZN | GM_FORM | 1173.15 | Ce2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EKSC43ZMMO | CE-ZN | GM_FORM | 973.15 | Ce13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-G3TRTAFB47 | CE-ZN | GM_FORM | 773.15 | CeZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-G54IYE5ICU | CE-ZN | GM_FORM | 773.15 | Ce3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GM74XWMPQ7 | CE-ZN | GM_FORM | 1173.15 | CeZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-H7ZRAAMMEB | CE-ZN | GM_FORM | 773.15 | CeZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IKJIUSYEHO | CE-ZN | GM_FORM | 773.15 | Ce2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IWY6AENSQZ | CE-ZN | GM_FORM | 773.15 | CeZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KN7WUE6X2I | CE-ZN | GM_FORM | 973.15 | Ce3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LJJ4JGFPMB | CE-ZN | GM_FORM | 1173.15 | CeZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MCEDTP4U2B | CE-ZN | GM_FORM | 973.15 | CeZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MEI23J6GDL | CE-ZN | GM_FORM | 1173.15 | CeZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MFTVHE3OCF | CE-ZN | GM_FORM | 1173.15 | Ce13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MMXDAHEPYE | CE-ZN | GM_FORM | 1173.15 | CeZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NMQOH7S6Z4 | CE-ZN | GM_FORM | 1173.15 | CeZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NOZQYF5A46 | CE-ZN | GM_FORM | 973.15 | Ce3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QALMUYRVLZ | CE-ZN | GM_FORM | 973.15 | Ce2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QJSEAQ5IRX | CE-ZN | GM_FORM | 973.15 | CeZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-S763I5XRQE | CE-ZN | GM_FORM | 973.15 | CeZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SI3RIE5BNR | CE-ZN | GM_FORM | 973.15 | CeZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-USKX4LDIIG | CE-ZN | GM_FORM | 973.15 | CeZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UYVVGXTHP7 | CE-ZN | GM_FORM | 1173.15 | Ce3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VSDOYLEF2H | CE-ZN | GM_FORM | 1173.15 | CeZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WBPEYMXB56 | CE-ZN | GM_FORM | 973.15 | CeZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-YC57UPTDSC | CE-ZN | GM_FORM | 773.15 | Ce3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5L35TGCFAL.ec28c3 | CR-GE | SM | 298.15 | CrGe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JJU3CGVLU7.826061 | CR-GE | SM | 298.15 | Cr11Ge19 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IDEY4NU7GH.5fcb90 | CS-O | CPM | 298.15 | Cs4O | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IDEY4NU7GH.6d36ca | CS-O | SM | 298.15 | Cs4O | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NGZLBXOCTJ.51d7f5 | CS-O | CPM | 298.15 | Cs7O | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NGZLBXOCTJ.89404d | CS-O | SM | 298.15 | Cs7O | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SWEHTSC4LB.6455b7 | CS-O | SM | 298.15 | Cs7O2 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SWEHTSC4LB.f524bc | CS-O | CPM | 298.15 | Cs7O2 | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSATJTWL4X.de9739 | CS-O | SM | 298.15 | Cs3O | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TSATJTWL4X.f55708 | CS-O | CPM | 298.15 | Cs3O | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2T3W5BF2L4.4e597c | ER-GE | GM_FORM | 950.0 | LT_ErGe2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3Z7R6C4RJD.fc409f | ER-GE | GM_FORM | 950.0 | Er11Ge10 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AIUQQK7SCB.65be9e | ER-GE | GM_FORM | 950.0 | MT_ErGe2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CAIUJ7QU3I.af9293 | ER-GE | GM_FORM | 950.0 | Er3Ge4 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DQF45FYYVS.ab0d4a | ER-GE | GM_FORM | 950.0 | LT_Er2Ge3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EH46YZZVT7.7340ac | ER-GE | GM_FORM | 950.0 | ErGe | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-LPVBNOE2IG.61f1dc | ER-GE | GM_FORM | 950.0 | HT_Er2Ge3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-O4EBHRWJPH.2ba01d | ER-GE | GM_FORM | 950.0 | Er2Ge5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SJMNJSI46L.3a1910 | ER-GE | GM_FORM | 950.0 | Er5Ge4 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VL7CG4ITOP.fc705a | ER-GE | GM_FORM | 950.0 | HT_ErGe2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3CGZJZTPCB.875a26 | FE-GD | SM | 298.15 | Fe2Gd | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7XTBZMJVLP | FE-GD | SM | 298.15 | Fe2Gd | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XV3BI7QYUX.1323e3 | FE-GD | CPM | 298.15 | Fe2Gd | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6RGAKANZZY.b63bed | FE-LU | CPM | 300.0 | Fe2Lu | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6RGAKANZZY.e2bf9c | FE-LU | SM | 300.0 | Fe2Lu | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PIU2NHVH32.18f6d2 | FE-LU | CPM | 290.0 | Fe2Lu | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PIU2NHVH32.892683 | FE-LU | SM | 290.0 | Fe2Lu | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3DFCHE5IR2.0d65b1 | FE-TM | SM | 290.0 | Fe2Tm | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3DFCHE5IR2.11713e | FE-TM | CPM | 290.0 | Fe2Tm | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NUHO6HHWO3.8dcb77 | FE-TM | SM | 300.0 | Fe2Tm | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NUHO6HHWO3.b76be8 | FE-TM | CPM | 300.0 | Fe2Tm | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QI2OQCE5ZB | FE-TM | SM | 298.15 | Fe2Tm | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6LBYYMRF75.603efa | FE-Y | GM_FORM | 973.0 | Fe17Y2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KU7WUHD2V2.f6b958 | FE-Y | GM_FORM | 973.0 | Fe3Y | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-YIWT6AZWC6.d0b6b1 | FE-Y | GM_FORM | 895.0 | Fe17Y2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6OSRGYMQDQ | GA-SE | SM | 298.15 | β-Ga2Se3 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HG7LOTMMDU | GA-SE | SM | 298.15 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-I4YOLNDV4S | GA-SE | SM | 298.15 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MM6PA5TXHW | GA-SE | SM | 298.15 | β-Ga2Se3 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NYI2LSUD7M | GA-SE | SM | 298.15 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-O7KYJO5SNX | GA-SE | SM | 298.15 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RHIBFFNDTR | GA-SE | SM | 298.15 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-V3JJYGH5BO | GA-SE | SM | 298.15 | GaSe | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B7SZWQWZ6C | GE-P | SM | 298.15 | Ge1P1 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-FWLVF5XETV | LI-SB | GM_FORM | 630.0 | Li2Sb | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SGNKL2MPDJ | LI-SB | GM_FORM | 723.0 | Li2Sb | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3EP2RAVNHP.48e3a8 | MG-SI | SM | 298.15 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
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
| ORC-FLICYKGIIJ | MG-SI | SM | 298.15 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
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
| ORC-TKZQ4AI54G.d24650 | MG-SI | SM | 298.15 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-U32QJAYGET.07f50e | MG-SI | CPM | 633.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-U32QJAYGET.ace621 | MG-SI | CPM | 633.0 | Mg2Si | compound_property_not_fittable | CPM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UJBRTZBL7N | MG-SI | SM | 298.15 | Mg2Si | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
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
| ORC-2ATZQOQRCH | ND-ZN | GM_FORM | 1173.15 | NdZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3JVNQE5B23 | ND-ZN | GM_FORM | 773.15 | NdZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5S524GOI3E | ND-ZN | GM_FORM | 1173.15 | Nd13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-6CSAUODHKB | ND-ZN | GM_FORM | 973.15 | NdZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7BIOCWCKPS | ND-ZN | GM_FORM | 973.15 | Nd2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B2EKXUYWTF | ND-ZN | GM_FORM | 1173.15 | Nd2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-B4M5M7NQAG | ND-ZN | GM_FORM | 1173.15 | NdZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-BXJ4QZGWMU | ND-ZN | GM_FORM | 973.15 | NdZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CKSZCOWR27 | ND-ZN | GM_FORM | 773.15 | Nd2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DHFHJXYE6K | ND-ZN | GM_FORM | 773.15 | NdZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IAC6RDXQYL | ND-ZN | GM_FORM | 773.15 | Nd3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-K2QCSVOTRD | ND-ZN | GM_FORM | 773.15 | Nd13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KDVU6VQ47C | ND-ZN | GM_FORM | 773.15 | NdZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KWF4CVF4JV | ND-ZN | GM_FORM | 973.15 | Nd3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MZ5UATJ747 | ND-ZN | GM_FORM | 973.15 | NdZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NAJNSOPOZH | ND-ZN | GM_FORM | 1173.15 | Nd3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NHAXCP7Q64 | ND-ZN | GM_FORM | 1173.15 | NdZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-PXOL3HMSSA | ND-ZN | GM_FORM | 1173.15 | NdZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QCPK3FIRBC | ND-ZN | GM_FORM | 973.15 | Nd3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SGI7ACYPEG | ND-ZN | GM_FORM | 773.15 | NdZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TQ7SUM7POQ | ND-ZN | GM_FORM | 1173.15 | Nd3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VUJTPRAOJY | ND-ZN | GM_FORM | 973.15 | Nd13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-W4A6Z3CVZQ | ND-ZN | GM_FORM | 773.15 | Nd3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-X464TN5H34 | ND-ZN | GM_FORM | 973.15 | NdZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-2QTBGDKN7R.be139a | O-U | SM | 298.15 | U3O8 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7IP3Y4UNA3.6d7e2b | O-U | SM | 298.15 | U4O9 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GSUCRMLDTW | O-U | SM | 298.15 | U4O9 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-R7K6J2XEJJ | O-U | SM | 298.15 | U4O9 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WDLVUYG56E | O-U | SM | 298.15 | U4O9 | compound_property_not_fittable | SM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
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
| ORC-2UZJC3N6JJ | PR-ZN | GM_FORM | 773.15 | αPr2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-33FDTG6NVN | PR-ZN | GM_FORM | 773.15 | Pr3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3UC2XEIAVB | PR-ZN | GM_FORM | 773.15 | PrZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-D3LXCAMZ7F | PR-ZN | GM_FORM | 773.15 | PrZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DX5UMN4EJ2 | PR-ZN | GM_FORM | 773.15 | αPrZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MZ323ESQJ7 | PR-ZN | GM_FORM | 773.15 | Pr13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MZETKMPROX | PR-ZN | GM_FORM | 773.15 | PrZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RVGYCWUQHI | PR-ZN | GM_FORM | 773.15 | PrZn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-X2C2KWPUJS | PR-ZN | GM_FORM | 773.15 | Pr3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VURWOO5JZR.a2b842 | RE-TA | GM_FORM | 298.15 | TaRe1.5 (σ or χ) | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-VURWOO5JZR.d36f92 | RE-TA | GM_FORM | 298.15 | TaRe1.5 (σ or χ) | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EVZXBKPOLW.5b7b0c | SB-ZN | GM_FORM | 600.15 | β-Zn13Sb10 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-TIHVTPDIMR.f1d784 | SB-ZN | GM_FORM | 420.15 | β-Zn13Sb10 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-32RUX5I6LW | SM-ZN | GM_FORM | 973.15 | Sm3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-34PUB3JLDB | SM-ZN | GM_FORM | 973.15 | Sm13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3GSTV6FR7O | SM-ZN | GM_FORM | 973.15 | SmZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-3WWXG3KLXW | SM-ZN | GM_FORM | 1173.15 | SmZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-44DYV436VP | SM-ZN | GM_FORM | 973.15 | SmZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-5SGYRKTL4Z | SM-ZN | GM_FORM | 1173.15 | SmZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CCKH2ZC3OC | SM-ZN | GM_FORM | 773.15 | SmZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CSB4QY535P | SM-ZN | GM_FORM | 773.15 | SmZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-DZZVET53KI | SM-ZN | GM_FORM | 973.15 | Sm3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ENYC5DGVKJ | SM-ZN | GM_FORM | 973.15 | Sm2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-IOXMXKWJEN | SM-ZN | GM_FORM | 1173.15 | Sm3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KJUINFJ4PN | SM-ZN | GM_FORM | 973.15 | SmZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-MIGPL255DV | SM-ZN | GM_FORM | 773.15 | Sm2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-NO76GSQUOM | SM-ZN | GM_FORM | 773.15 | SmZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QICZWTTHCR | SM-ZN | GM_FORM | 1173.15 | SmZn | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RPTA4PZEF7 | SM-ZN | GM_FORM | 773.15 | Sm3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RSMAR3WZAH | SM-ZN | GM_FORM | 1173.15 | Sm3Zn22 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-SJLG4VVRQL | SM-ZN | GM_FORM | 773.15 | Sm3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T2W7HHQI4L | SM-ZN | GM_FORM | 1173.15 | Sm2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XHOHAWLLOO | SM-ZN | GM_FORM | 1173.15 | Sm13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZTYQWQQDBR | SM-ZN | GM_FORM | 773.15 | Sm13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-37FWLR52XC | Y-ZN | GM_FORM | 1173.15 | βYZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-4CV4EVXVXH | Y-ZN | GM_FORM | 773.15 | YZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-7NL4OM42MO | Y-ZN | GM_FORM | 773.15 | Y2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-AQQW4WZFCL | Y-ZN | GM_FORM | 773.15 | YZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-EAPMZ57DO4 | Y-ZN | GM_FORM | 773.15 | Y3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-G5Y45RZ6TD | Y-ZN | GM_FORM | 1173.15 | Y2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-GB2SIFVF6C | Y-ZN | GM_FORM | 1173.15 | YZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-H5FYP57CKH | Y-ZN | GM_FORM | 1173.15 | YZn12 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-HNF47QMGED | Y-ZN | GM_FORM | 773.15 | αYZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ISAX62FUFR | Y-ZN | GM_FORM | 773.15 | YZn12 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-JP3WERVVDX | Y-ZN | GM_FORM | 773.15 | YZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-KURJIRUXMN | Y-ZN | GM_FORM | 773.15 | αYZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-OWLHFM4GOR | Y-ZN | GM_FORM | 773.15 | Y3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QNRWY44J53 | Y-ZN | GM_FORM | 773.15 | Y13Zn58 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-QQSGPEZY6Y | Y-ZN | GM_FORM | 973.15 | αYZn2 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-RKWBI757VK | Y-ZN | GM_FORM | 773.15 | YZn12 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-T3VGUK7VNP | Y-ZN | GM_FORM | 773.15 | Y2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UAWE4UXNVE | Y-ZN | GM_FORM | 773.15 | YZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-UMASVPDMZM | Y-ZN | GM_FORM | 1173.15 | YZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WIJNHVWWPC | Y-ZN | GM_FORM | 973.15 | YZn12 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-WN3VMHD2O3 | Y-ZN | GM_FORM | 973.15 | Y3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-XRQ7EIS5PR | Y-ZN | GM_FORM | 973.15 | Y2Zn17 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-YGB6DF2VIF | Y-ZN | GM_FORM | 973.15 | YZn3 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZAGX362XDV | Y-ZN | GM_FORM | 973.15 | YZn5 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-ZDY5VS3FGO | Y-ZN | GM_FORM | 1173.15 | Y3Zn11 | compound_property_not_fittable | GM_FORM of a stoichiometric compound (ESPEI 0.9.1 fits only HM_FORM/SM_FORM of compound endmembers) |
| ORC-CIPJAZEEG7 | MO-O | INVARIANT_TEMPERATURE | 1053.15 | L, Mo8O23, Mo9O26 | liquid_impossible_at_T | liquid at 1053.15 K, below 1985 K (calculated_sgte_diagram) |
| ORC-DUVVS2WS3I | MO-O | INVARIANT_TEMPERATURE | 1051.15 | L, Mo9O26, MoO3 | liquid_impossible_at_T | liquid at 1051.15 K, below 1985 K (calculated_sgte_diagram) |
| ORC-UUOU4YRKZL | MO-O | INVARIANT_TEMPERATURE | 1091.15 | L, MoO2, Mo4O11 | liquid_impossible_at_T | liquid at 1091.15 K, below 1985 K (calculated_sgte_diagram) |
| ORC-H3GLAFRIM7 | AL-HF | HM_FORM | 298.15 | HfAl3 | phase_label_ambiguous | label 'HfAl3' |
| ORC-UVWYIQWC3J | AL-HF | HM_FORM | 298.15 | HfAl3 | phase_label_ambiguous | label 'HfAl3' |
| ORC-7X7QCYYHAV | AL-Y | HM_FORM | 298.15 | YAl3 | phase_label_ambiguous | label 'YAl3' |
| ORC-QQHP64NZUS | AL-Y | HM_FORM | 763.0 | YAl3 | phase_label_ambiguous | label 'YAl3' |
| ORC-HV5YWBUZLU.7c0cf1 | AU-HO | HM_FORM | 298.15 | αAuHo | phase_label_ambiguous | label 'αAuHo' |
| ORC-ERUWHO6TNF.7818e1 | BA-PB | HM_FORM | 300.0 | βBa0.375Pb0.625 | phase_label_ambiguous | label 'βBa0.375Pb0.625' |
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
| ORC-LEVZKAYSFQ.3928ec | CS-TE | SM | 298.15 | Cs2Te | phase_label_ambiguous | label 'Cs2Te' |
| ORC-3ZQFHDEH6W.183131 | CU-ZR | HM_FORM | 0.0 | CuZr2-C11b | phase_label_ambiguous | label 'CuZr2-C11b' |
| ORC-L4LH5UJX5O | FE-GD | HM_FORM | 298.15 | Fe17Gd2 | phase_label_ambiguous | label 'Fe17Gd2' |
| ORC-QJ56PUEUMY | FE-HF | HM_FORM | 1373.0 | Fe2Hf-HT | phase_label_ambiguous | label 'Fe2Hf-HT' |
| ORC-U33KIRTKYB | FE-HF | HM_FORM | 1723.0 | Fe2Hf-HT | phase_label_ambiguous | label 'Fe2Hf-HT' |
| ORC-FQDLRJYDWH | GA-Y | HM_FORM | 298.15 | Ga3Y5 | phase_label_ambiguous | label 'Ga3Y5' |
| ORC-KW3VBQ6QZL | GA-Y | HM_FORM | 298.15 | Ga3Y5 | phase_label_ambiguous | label 'Ga3Y5' |
| ORC-J54C6AXT5M | GE-RU | HM_FORM | 1173.0 | Ru2Ge3 | phase_label_ambiguous | label 'Ru2Ge3' |
| ORC-STEFK5VKOZ | GE-RU | HM_FORM | 298.15 | Ru2Ge3 | phase_label_ambiguous | label 'Ru2Ge3' |
| ORC-4KBCL5U4BH.046030 | LI-SB | SM_FORM | 686.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-4KBCL5U4BH.342b48 | LI-SB | HM_FORM | 686.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-L3ZY532BLT.85a76f | LI-SB | HM_FORM | 700.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
| ORC-L3ZY532BLT.f04169 | LI-SB | SM_FORM | 700.65 | Li3Sb | phase_label_ambiguous | label 'Li3Sb' |
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
| ORC-7EFEZK2TDU.32710c | N-SI | HM_FORM | 298.15 | α-Si3N4 | phase_label_ambiguous | label 'α-Si3N4' |
| ORC-7Y3UKOYUWX.ff192f | N-SI | SM | 298.15 | α-Si3N4 | phase_label_ambiguous | label 'α-Si3N4' |
| ORC-LDP5O2JGT6.cde3eb | PD-SN | HM_FORM | 320.0 | α-Pd3Sn2 | phase_label_ambiguous | label 'α-Pd3Sn2' |
| ORC-7VPUF5XRGG.1e6b0e | SB-ZN | GM_FORM | 806.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-7VPUF5XRGG.2a862c | SB-ZN | HM_FORM | 806.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-LJ7NTT3MZM.0521f9 | SB-ZN | HM_FORM | 826.0 | δ′-Sb3Zn4 | phase_label_ambiguous | label 'δ′-Sb3Zn4' |
| ORC-LJ7NTT3MZM.f6971e | SB-ZN | GM_FORM | 826.0 | δ′-Sb3Zn4 | phase_label_ambiguous | label 'δ′-Sb3Zn4' |
| ORC-NNBDCYEADO.2a8dfa | SB-ZN | GM_FORM | 800.0 | ξ-Sb2Zn3 | phase_label_ambiguous | label 'ξ-Sb2Zn3' |
| ORC-NNBDCYEADO.98dc51 | SB-ZN | HM_FORM | 800.0 | ξ-Sb2Zn3 | phase_label_ambiguous | label 'ξ-Sb2Zn3' |
| ORC-NZUTUZNKYH.3f1124 | SB-ZN | HM_FORM | 800.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-NZUTUZNKYH.b1f117 | SB-ZN | GM_FORM | 800.0 | δ-Sb3Zn4 | phase_label_ambiguous | label 'δ-Sb3Zn4' |
| ORC-O44M4ZW6TJ.030335 | SB-ZN | GM_FORM | 800.15 | β-Zn3Sb2 | phase_label_ambiguous | label 'β-Zn3Sb2' |
| ORC-O44M4ZW6TJ.25c16b | SB-ZN | HM_FORM | 800.15 | β-Zn3Sb2 | phase_label_ambiguous | label 'β-Zn3Sb2' |
| ORC-2CEFS6VVEV.afeb02 | SE-SN | HM_FORM | 298.15 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-OTLJ2QNFR6 | SE-SN | HM_FORM | 298.15 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-SXCESCRLPN.a39dda | SE-SN | HM_FORM | 298.15 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-TZ4OR4CMJG | SE-SN | HM_FORM | 298.15 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-V7VHHJ5GSB.b91536 | SE-SN | HM_FORM | 298.15 | SnSe | phase_label_ambiguous | label 'SnSe' |
| ORC-5O7BBL2ZS5.6cd718 | SI-TA | HM_FORM | 1473.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-GCYCOHJVMK.b0dbf6 | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-HO7JT6JFYO.6095fb | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-OEWHAHTIO4.06dce4 | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-OVSTHRO2TO.ad70dc | SI-TA | HM_FORM | 1027.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-OVSTHRO2TO.cff80a | SI-TA | SM_FORM | 1027.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-RBNDQYDXRA.5f2d77 | SI-TA | HM_FORM | 298.15 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-WLRX6KX33K.3c6241 | SI-TA | SM_FORM | 1900.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-WLRX6KX33K.5fec23 | SI-TA | HM_FORM | 1900.0 | Si0.375Ta0.625_HT | phase_label_ambiguous | label 'Si0.375Ta0.625_HT' |
| ORC-FSYVSAZKHR | SI-U | HM_FORM | 298.15 | U3Si | phase_label_ambiguous | label 'U3Si' |
| ORC-3E7T6VEXR2 | SI-Y | HM_FORM | 0.0 | Y3Si5 (R) | phase_label_ambiguous | label 'Y3Si5 (R)' |
| ORC-BFAMJ2DIA5.917539 | SI-Y | HM_FORM | 298.15 | Y3Si5 | phase_label_ambiguous | label 'Y3Si5' |
| ORC-BFAMJ2DIA5.f3bc8b | SI-Y | SM_FORM | 298.15 | Y3Si5 | phase_label_ambiguous | label 'Y3Si5' |
| ORC-XAWUXWICRX | SI-Y | HM_FORM | 0.0 | Y3Si5 (H) | phase_label_ambiguous | label 'Y3Si5 (H)' |
| ORC-C3QDI5675C | SN-TI | HM_FORM | 298.15 | Sn5Ti6-L | phase_label_ambiguous | label 'Sn5Ti6-L' |
| ORC-YTPULMUAG2.147391 | SN-TI | HM_FORM | 298.15 | Sn5Ti6-L | phase_label_ambiguous | label 'Sn5Ti6-L' |
| ORC-UR7LCFHVIW.276c54 | AL | HM_FORM | 0.0 | fcc-Al | phase_label_not_mapped | label 'fcc-Al' |
| ORC-X2WBMXYDLJ | AL | HM_FORM | 0.0 | Al | phase_label_not_mapped | label 'Al' |
| ORC-3QIK7OVINP.90029a | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
| ORC-4AIGKIGSRZ.f2f361 | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
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
| ORC-RRTXNAEBFG.4b59a8 | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-SGGMA66RLQ.98325d | AL-CA | HM_FORM | 0.0 | C15-Ca2Al | phase_label_not_mapped | label 'C15-Ca2Al' |
| ORC-TCPC77DHKK.452f64 | AL-CA | HM_FORM | 298.15 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-WAZ6UJADGF.8da616 | AL-CA | HM_FORM | 0.0 | C15-Al2Ca | phase_label_not_mapped | label 'C15-Al2Ca' |
| ORC-ZKD74CCMXO.fb87dd | AL-CA | HM_FORM | 0.0 | C15-Al2Al | phase_label_not_mapped | label 'C15-Al2Al' |
| ORC-3VAP5U3PYE | AL-CO | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-4EGJ77QJYM | AL-CO | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-E7AOQYLW7C | AL-CO | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-ETBNSP746Y | AL-CO | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-KO4O6TOD2C.cb06e3 | AL-CO | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-VKJQHODF5T.d1c4e1 | AL-CO | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-4EP7XRAXPS | AL-CO-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-65JDHAPWG3 | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-66QDO5IYIG | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-6G3EKW4XCM | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-E3SGIIH26O | AL-CO-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-F6V7ZTZOXE | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-IGICY273VQ | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-L4FSTSSWWM | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-LBNVYX7MKG | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-LMPO46BMIF | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-MVK4ZWOCGE | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-OVPAV4MJMS | AL-CO-CR | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-PWPIZMRW2O | AL-CO-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-SHRYIPOXBJ | AL-CO-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-UT62E76MOR | AL-CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-YNUBAUOYL6 | AL-CO-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-ZDUO6PKZ3H | AL-CO-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-3TOSQGHNGM | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-3UZ3TZACIU | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-4RXVDM6W2U | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-GFVKETY64Q | AL-CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-OS5IVTXPX6 | AL-CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-3D4W5TGD42 | AL-CO-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-56UQQ3KDZU | AL-CO-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-7GQJDWDHJQ | AL-CO-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-HRT7A33QUN | AL-CO-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-MZSAEGOTBR | AL-CO-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-P4ZSEXFBEG | AL-CO-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-RNMZLTA3EG | AL-CO-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-XMHR27DSFK | AL-CO-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-ZRJTZFU5YP | AL-CO-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-A4YFGUJQFA | AL-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-CJF25RA3S4.a678d8 | AL-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-DDS6WWAX23 | AL-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-PDPECKEWAL.dcee83 | AL-CR | HM_FORM | 1273.15 | Al9Cr4 (l) | phase_label_not_mapped | label 'Al9Cr4 (l)' |
| ORC-QL67TSGS6J | AL-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-UWBYNJLERZ | AL-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-Z6W4NXL7QJ.80139e | AL-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-5N5TJPYRTK.a04419 | AL-MG | HM_FORM | 0.0 | Al2Mg-C15 | phase_label_not_mapped | label 'Al2Mg-C15' |
| ORC-RNUDMKJN4F.a61040 | AL-MG | HM_FORM | 0.0 | Al2Mg-C36 | phase_label_not_mapped | label 'Al2Mg-C36' |
| ORC-YZTJPJLSUX.2fae14 | AL-MG | HM_FORM | 0.0 | Al2Mg-C14 | phase_label_not_mapped | label 'Al2Mg-C14' |
| ORC-4NPP2JSIVO.147cf7 | AL-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-5SQ6ZVI24R.5bc4e5 | AL-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-M7BUHEGWBV | AL-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-TJ27BEONTE.3fade8 | AL-NI | HM_FORM | 0.0 | B2-β | phase_label_not_mapped | label 'B2-β' |
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
| ORC-FFQKM5UWR6 | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-PHBWW54AYA | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-QCFMJ36AAG | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-SVJTYZQSOO | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-YWMCF3MY3L | AL-TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-3LPA54QJQD | B-MG | HM_FORM | 298.15 | MgB6 | phase_label_not_mapped | label 'MgB6' |
| ORC-7PI7ACDB6X | B-MG | HM_FORM | 298.15 | MgB12 | phase_label_not_mapped | label 'MgB12' |
| ORC-KIP2CJSBMK | B-MG | HM_FORM | 298.15 | MgB6 | phase_label_not_mapped | label 'MgB6' |
| ORC-N2BPBLFSN3 | B-MG | HM_FORM | 298.15 | Mg2B | phase_label_not_mapped | label 'Mg2B' |
| ORC-TDP6IBGSN3 | B-MG | HM_FORM | 298.15 | Mg4B | phase_label_not_mapped | label 'Mg4B' |
| ORC-5P2WKOP3S6 | C-NB | HM_FORM | 0.0 | Nb3C | phase_label_not_mapped | label 'Nb3C' |
| ORC-BDWBO3XXDG | C-NB | HM_FORM | 0.0 | Nb7C3 | phase_label_not_mapped | label 'Nb7C3' |
| ORC-YX7DW62EWY | C-NB | HM_FORM | 0.0 | Nb5C2 | phase_label_not_mapped | label 'Nb5C2' |
| ORC-24U66SUY3P.8ca50f | C-PU | CPM | 298.15 | C₀.₈₂Pu | phase_label_not_mapped | label 'C₀.₈₂Pu' |
| ORC-2TJONUSJBC.80f06f | C-PU | SM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-2TJONUSJBC.81481c | C-PU | CPM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-4ZUW262ENE.4af561 | C-PU | CPM | 298.15 | C₀.₈₇Pu | phase_label_not_mapped | label 'C₀.₈₇Pu' |
| ORC-ICTO4YCG3I.755cf3 | C-PU | SM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-ICTO4YCG3I.be37c6 | C-PU | CPM | 298.15 | C₀.₈Pu | phase_label_not_mapped | label 'C₀.₈Pu' |
| ORC-BUO7XSPB2I | C-SI-Y | HM_FORM | 0.0 | Y3Si2C2 | phase_label_not_mapped | label 'Y3Si2C2' |
| ORC-FFDZZDXLP6 | C-SI-Y | HM_FORM | 0.0 | Y15Si9C | phase_label_not_mapped | label 'Y15Si9C' |
| ORC-IGXZ3PKXEP | C-SI-Y | HM_FORM | 0.0 | Y1.8Si0.2C2.7 | phase_label_not_mapped | label 'Y1.8Si0.2C2.7' |
| ORC-23ZIGYN2CV.7c099c | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-242GA7RIKL.112092 | C-U | SM | 298.15 | UC | phase_label_not_mapped | label 'UC' |
| ORC-2D5S4G5EI4.e27a79 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-2EKKOMMM6P.6d27c7 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-2GHVHLBELH.318ec9 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-2HLE6UO57R.313321 | C-U | CPM | 2393.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-33GIIPQBST.42a541 | C-U | CPM | 1878.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-35WTM76WD5.0b8b03 | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
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
| ORC-7NYE2G6FHN.acbd39 | C-U | HM_FORM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-7R46RRKEII.73ca96 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-7WUCDPAEKW.41207d | C-U | SM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-AMBA2N3OEV.0a0b35 | C-U | CPM | 2021.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-AUIGU4S7VE.2b76ff | C-U | CPM | 900.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-AUIGU4S7VE.4886cd | C-U | SM | 900.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-AUIGU4S7VE.55d6e6 | C-U | CPM | 900.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-AUIGU4S7VE.ca32e4 | C-U | SM | 900.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-AXZOODW34P.0f22dc | C-U | CPM | 1300.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-B67LEUD767.24c645 | C-U | HM_FORM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-BA4U3STZDG.0f65b8 | C-U | CPM | 1900.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-BGLQZKVJ3B.1e09f7 | C-U | SM | 1700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-BGLQZKVJ3B.617ffe | C-U | CPM | 1700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-BGLQZKVJ3B.9b8228 | C-U | SM | 1700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-BGLQZKVJ3B.e6a57f | C-U | CPM | 1700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-BJB7UAJ4FW.1de5fc | C-U | SM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-BNLQRWAFZA.a595c8 | C-U | CPM | 2000.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-BO7VM5FH4F.0b54c2 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-C3JCZQJ27X.de19c3 | C-U | CPM | 1000.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-CVTNZ7W4CW.36702a | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-DLPIODCAG2.125005 | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-E5HDC2FLZT.203df8 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-ERCRJRRYFQ.19fa3b | C-U | SM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-ERUUNHKLGD.64cfa7 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-ES37M7DMUN.b78494 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-FCF7WKQFEH.470641 | C-U | HM_FORM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-FQQ72T5BVR.1c87a1 | C-U | SM | 1100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-FQQ72T5BVR.21ff0d | C-U | SM | 1100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-FQQ72T5BVR.5f4e2c | C-U | CPM | 1100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-FQQ72T5BVR.a31510 | C-U | CPM | 1100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-FTQTR7ALWZ.02b0d4 | C-U | HM_FORM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-FV55AJCSM7.aaa5b0 | C-U | CPM | 2277.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-GHYX64I4DB.ba7abb | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-GLBOSZMY2N.c68743 | C-U | CPM | 2600.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-HRMZYM7VPM.700fbe | C-U | CPM | 1800.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-IDV2HJJECD.0560a2 | C-U | SM | 2700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-IDV2HJJECD.733ce7 | C-U | CPM | 2700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-IDV2HJJECD.bc073e | C-U | CPM | 2700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-IFVF5O65HA.7601ad | C-U | SM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-IQKO6FH2Q3.7fe11f | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-IRAA2SNWE5.cd1c77 | C-U | CPM | 2800.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-IT2MHOE4W4.887ab0 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-JBX7HQDS7G.48afb6 | C-U | CPM | 2400.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-JMWXRWYCEH.350576 | C-U | CPM | 2581.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-JPXGWKLMR5.6405f9 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-JRXWAA3IRP.fc8bf0 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-JT4YWMQ7GU.a06b05 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-K64YEXIHRW.95596f | C-U | HM_FORM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-KFBOAZXLU2.d3e191 | C-U | CPM | 1500.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-KISHC7YH3P.1ce44a | C-U | CPM | 2300.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KISHC7YH3P.1eb510 | C-U | SM | 2300.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KISHC7YH3P.2e23a9 | C-U | SM | 2300.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KISHC7YH3P.b9846d | C-U | CPM | 2300.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KOAT4GY3FO.2445a8 | C-U | SM | 700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KOAT4GY3FO.4545b9 | C-U | SM | 700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KOAT4GY3FO.9a68a6 | C-U | CPM | 700.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-KOAT4GY3FO.c6474f | C-U | CPM | 700.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-KPJGMBKYYD.d487e9 | C-U | CPM | 2081.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-KXWIXRF7I6.b1f9ef | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-LFAO5SSXMK.234b29 | C-U | SM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-LSSFSIWPPD.4155ca | C-U | CPM | 900.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-LV4SGXSJXS.c02e76 | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-LWYUALS5RO.8cd5ea | C-U | HM_FORM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-MNSGFN7TUF.62673d | C-U | HM_FORM | 298.15 | UC | phase_label_not_mapped | label 'UC' |
| ORC-MRZIID7CXJ.1ae8ce | C-U | CPM | 1587.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-MS3CBROHJH.4fbc53 | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-MTKWY57AVO.10c9ca | C-U | HM_FORM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-MUHBNJIVW3.707150 | C-U | CPM | 2500.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-N3WRTWYLYG.53767b | C-U | HM_FORM | 298.15 | UC | phase_label_not_mapped | label 'UC' |
| ORC-N5YTMMR3NQ.a08881 | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-O56OVTZ7KS.3c6ad0 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-O7DR3NZX3M.b72d9c | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-OBDHR3TCXP.36f004 | C-U | CPM | 1484.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-OIY4EEX2ZX.3024a9 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-OZSIMP67VN.9c5fc2 | C-U | HM_FORM | 298.15 | UC | phase_label_not_mapped | label 'UC' |
| ORC-P33O5JHCBK.cd3443 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-P43WX2TIGN.28230e | C-U | HM_FORM | 298.15 | UC | phase_label_not_mapped | label 'UC' |
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
| ORC-RCN7VNES7I.5820e9 | C-U | CPM | 298.15 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-RCN7VNES7I.8e1a3a | C-U | SM | 298.15 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RCN7VNES7I.aca4c8 | C-U | CPM | 298.15 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-RCN7VNES7I.b50b63 | C-U | SM | 298.15 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
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
| ORC-T7MNBZZVXK.2b6e43 | C-U | HM_FORM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-TEEZ6BI35F.284b3a | C-U | SM | 298.15 | C0.500U0.500 | phase_label_not_mapped | label 'C0.500U0.500' |
| ORC-TILXAUAOFV.4b9521 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-TQAI7JI233.681089 | C-U | SM | 298.15 | UC | phase_label_not_mapped | label 'UC' |
| ORC-U2FVIYX4LQ.1c24c1 | C-U | SM | 2800.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-U2FVIYX4LQ.84fb4f | C-U | CPM | 2800.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-U4A6PGMXIO.13e647 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-U7PC23R5WQ.7f3d32 | C-U | CPM | 1200.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-UQQOVF2DGH.af465e | C-U | CPM | 1490.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-UVTDLRXYEZ.77aa87 | C-U | CPM | 2213.0 | UC1.93 | phase_label_not_mapped | label 'UC1.93' |
| ORC-V5HTCHAXS3.970e9d | C-U | HM_FORM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-V6DLUQK6M5.d5abc5 | C-U | CPM | 1700.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-VDPK37734P.2e33e0 | C-U | SM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-WDZEJ6KIOW.7378d7 | C-U | CPM | 1600.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-X6FQXSGJHQ.3a6d75 | C-U | HM_FORM | 298.15 | C0.655U0.345 | phase_label_not_mapped | label 'C0.655U0.345' |
| ORC-XJ75CNS7EI.37e936 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
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
| ORC-YR6GSXQZOM.7dfeaf | C-U | HM_FORM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-Z64QWWQJ3A.ba938b | C-U | CPM | 1400.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-Z7I2LHDDPD.55ad90 | C-U | HM_FORM | 298.15 | UCx | phase_label_not_mapped | label 'UCx' |
| ORC-ZJQCPK4WVI.0b386a | C-U | CPM | 2100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-ZJQCPK4WVI.0f82e6 | C-U | CPM | 2100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-ZJQCPK4WVI.7178fc | C-U | SM | 2100.0 | U0.500C0.500 | phase_label_not_mapped | label 'U0.500C0.500' |
| ORC-ZJQCPK4WVI.ef7d05 | C-U | SM | 2100.0 | U0.345C0.655 | phase_label_not_mapped | label 'U0.345C0.655' |
| ORC-ZS6L6RA7WP.0a4ae6 | C-U | CPM | 2700.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-ZT5QUPW7FY.270847 | C-U | CPM | 800.0 | UC | phase_label_not_mapped | label 'UC' |
| ORC-ZZ6XETLP3U.623533 | C-U | HM_FORM | 298.15 | UC1.90 | phase_label_not_mapped | label 'UC1.90' |
| ORC-MV6VDIBSCZ | C-Y | HM_FORM | 0.0 | Y2C3 (R) | phase_label_not_mapped | label 'Y2C3 (R)' |
| ORC-4T6PPMNMVH.c19ed3 | CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-OHVOHPTKPU.3d337a | CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-RBRLISTFX3.c24d82 | CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-RU5SWY7JGW.072bed | CA | HM_FORM | 0.0 | C15-Ca2Ca | phase_label_not_mapped | label 'C15-Ca2Ca' |
| ORC-377G72NYL5.16f26c | CE-GA | HM_FORM | 298.15 | Ce0.21Ga0.79 | phase_label_not_mapped | label 'Ce0.21Ga0.79' |
| ORC-P74KIVIPMK.138e01 | CE-GA | HM_FORM | 298.15 | Ce0.21Ga0.79 | phase_label_not_mapped | label 'Ce0.21Ga0.79' |
| ORC-5I6MP4KN2N | CO-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-6OYLJDF5W6 | CO-CR | HM_MIX | 0.0 | B2 | phase_label_not_mapped | label 'B2' |
| ORC-BQZ45U6GCO.c1d891 | CO-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-I5JKIVXLI4 | CO-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-RUQIJPW7LX | CO-CR | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-TVEF5FPR33.0f9888 | CO-CR | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-BZVTAKWUEV | CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-DES3Y567OU | CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-EAJVUJJ3L3 | CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-FCRRH4IFTR | CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-GEKREDAI23 | CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-MRYCPD3MGU | CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-WSKLBJ7O6R | CO-CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-X7EHOUKTPD | CO-CR-NI | HM_MIX | 0.0 | A2 | phase_label_not_mapped | label 'A2' |
| ORC-YFI3VYJ3UQ | CO-CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-5WMXIEWM4J | CO-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-LOZBGVYVAU.4ec080 | CO-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-NLD4Z6JLS6 | CO-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-R4JVCNQOUL.88a673 | CO-NI | HM_FORM | 0.0 | B2-β | phase_label_not_mapped | label 'B2-β' |
| ORC-UDK532NRBY.74c81e | CO-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-UHOV5ETA3J | CO-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-7V5ZKCLAPY.1099e3 | CR | HM_FORM | 0.0 | sigma CrCrCrCrCr | phase_label_not_mapped | label 'sigma CrCrCrCrCr' |
| ORC-2J4IQSP6P5.455370 | CR-GE | GM_FORM | 1530.0 | Cr0.63Ge0.37 | phase_label_not_mapped | label 'Cr0.63Ge0.37' |
| ORC-5DSEUH4NK2.4030f3 | CR-GE | GM_FORM | 1530.0 | Cr0.75Ge0.25 | phase_label_not_mapped | label 'Cr0.75Ge0.25' |
| ORC-D4GO4RDBQ3.0b66ef | CR-GE | GM_FORM | 1530.0 | Cr0.8Ge0.2 | phase_label_not_mapped | label 'Cr0.8Ge0.2' |
| ORC-D6O6WD7FEM.41ccc1 | CR-GE | GM_FORM | 1530.0 | Cr0.8Ge0.2 | phase_label_not_mapped | label 'Cr0.8Ge0.2' |
| ORC-SHBHPLOWRZ.b6ec88 | CR-GE | GM_FORM | 1530.0 | Cr0.75Ge0.25 | phase_label_not_mapped | label 'Cr0.75Ge0.25' |
| ORC-SQKDM2MIIO.7c252f | CR-GE | GM_FORM | 1530.0 | Cr0.8Ge0.2 | phase_label_not_mapped | label 'Cr0.8Ge0.2' |
| ORC-ZDS7SVJW37.6c99b2 | CR-GE | GM_FORM | 1530.0 | Cr0.75Ge0.25 | phase_label_not_mapped | label 'Cr0.75Ge0.25' |
| ORC-4AVGOLDRYY.d5c876 | CR-NI | HM_FORM | 0.0 | B2-β | phase_label_not_mapped | label 'B2-β' |
| ORC-7BZ4YFYJFR | CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-BJCC23KTCK.7c92d8 | CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-BSYOVSRLCW | CR-NI | HM_MIX | 0.0 | γ’ | phase_label_not_mapped | label 'γ’' |
| ORC-CG6B7EHP2R.127230 | CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-XYCE5GPHM6 | CR-NI | HM_MIX | 0.0 | γ | phase_label_not_mapped | label 'γ' |
| ORC-2DC2JED7OP.95d3f8 | CR-RE | HM_FORM | 0.0 | sigma CrReCrReRe | phase_label_not_mapped | label 'sigma CrReCrReRe' |
| ORC-2G5X7WUZNV.f3ad86 | CR-RE | HM_FORM | 0.0 | sigma CrReCrCrCr | phase_label_not_mapped | label 'sigma CrReCrCrCr' |
| ORC-3BBKXWFDLX.db9632 | CR-RE | HM_FORM | 0.0 | sigma ReCrCrReRe | phase_label_not_mapped | label 'sigma ReCrCrReRe' |
| ORC-6C6U4O32PW.7a5458 | CR-RE | HM_FORM | 0.0 | sigma CrCrCrReCr | phase_label_not_mapped | label 'sigma CrCrCrReCr' |
| ORC-7Q67Y5AAUP.c0b705 | CR-RE | HM_FORM | 0.0 | sigma ReReCrCrRe | phase_label_not_mapped | label 'sigma ReReCrCrRe' |
| ORC-7U3QE7COIV.262b3f | CR-RE | HM_FORM | 0.0 | sigma ReCrCrCrRe | phase_label_not_mapped | label 'sigma ReCrCrCrRe' |
| ORC-ABAFGO6RFJ.fb2ccd | CR-RE | HM_FORM | 0.0 | sigma ReCrReReCr | phase_label_not_mapped | label 'sigma ReCrReReCr' |
| ORC-CPDKPV5EPK.fb522a | CR-RE | HM_FORM | 0.0 | sigma CrCrReCrRe | phase_label_not_mapped | label 'sigma CrCrReCrRe' |
| ORC-ECFNA3MRAU.17b53d | CR-RE | HM_FORM | 0.0 | sigma ReReCrReCr | phase_label_not_mapped | label 'sigma ReReCrReCr' |
| ORC-ERTEHM4ZHT.a27526 | CR-RE | HM_FORM | 0.0 | sigma ReReCrCrCr | phase_label_not_mapped | label 'sigma ReReCrCrCr' |
| ORC-G7JPHP6Q3Y.11a3a0 | CR-RE | HM_FORM | 0.0 | sigma ReCrReCrCr | phase_label_not_mapped | label 'sigma ReCrReCrCr' |
| ORC-HHWZQT4ZRW.389d7e | CR-RE | HM_FORM | 0.0 | sigma CrCrCrReRe | phase_label_not_mapped | label 'sigma CrCrCrReRe' |
| ORC-HJCE7FJDVI.a9cde8 | CR-RE | HM_FORM | 0.0 | sigma ReCrReCrRe | phase_label_not_mapped | label 'sigma ReCrReCrRe' |
| ORC-IUFI6L23AQ.4e3220 | CR-RE | HM_FORM | 0.0 | sigma CrReReCrRe | phase_label_not_mapped | label 'sigma CrReReCrRe' |
| ORC-LYRS4S5UV4.9c501c | CR-RE | HM_FORM | 0.0 | sigma ReCrCrCrCr | phase_label_not_mapped | label 'sigma ReCrCrCrCr' |
| ORC-MTKKNK4CPD.d27d84 | CR-RE | HM_FORM | 0.0 | sigma ReReReCrCr | phase_label_not_mapped | label 'sigma ReReReCrCr' |
| ORC-MWAOBM7KVD.fd6509 | CR-RE | HM_FORM | 0.0 | sigma CrCrReCrCr | phase_label_not_mapped | label 'sigma CrCrReCrCr' |
| ORC-NXV5MZWYVZ.40e4df | CR-RE | HM_FORM | 0.0 | sigma CrReCrReCr | phase_label_not_mapped | label 'sigma CrReCrReCr' |
| ORC-OUHRIRWERS.0cb1fb | CR-RE | HM_FORM | 0.0 | sigma ReReCrReRe | phase_label_not_mapped | label 'sigma ReReCrReRe' |
| ORC-PQJLJRX26T.8fc573 | CR-RE | HM_FORM | 0.0 | sigma ReCrCrReCr | phase_label_not_mapped | label 'sigma ReCrCrReCr' |
| ORC-RT5WBW3IRF.ba4c68 | CR-RE | HM_FORM | 0.0 | sigma CrCrReReCr | phase_label_not_mapped | label 'sigma CrCrReReCr' |
| ORC-SQ3Z2MJJCO.391690 | CR-RE | HM_FORM | 0.0 | sigma CrCrReReRe | phase_label_not_mapped | label 'sigma CrCrReReRe' |
| ORC-SVCJWLU7O4.425a26 | CR-RE | HM_FORM | 0.0 | sigma CrCrCrCrRe | phase_label_not_mapped | label 'sigma CrCrCrCrRe' |
| ORC-THGOOTZYOQ.a5c0dd | CR-RE | HM_FORM | 0.0 | sigma CrReReCrCr | phase_label_not_mapped | label 'sigma CrReReCrCr' |
| ORC-TKEA3B5XJN.ffffff | CR-RE | HM_FORM | 0.0 | sigma ReReReCrRe | phase_label_not_mapped | label 'sigma ReReReCrRe' |
| ORC-WCPWMTQK3N.910b1c | CR-RE | HM_FORM | 0.0 | sigma CrReReReRe | phase_label_not_mapped | label 'sigma CrReReReRe' |
| ORC-XCCOLQZ2PE.1f3f90 | CR-RE | HM_FORM | 0.0 | sigma CrReCrCrRe | phase_label_not_mapped | label 'sigma CrReCrCrRe' |
| ORC-XL547PLTFS.060120 | CR-RE | HM_FORM | 0.0 | sigma ReCrReReRe | phase_label_not_mapped | label 'sigma ReCrReReRe' |
| ORC-XVKAXI6VI3.611a81 | CR-RE | HM_FORM | 0.0 | sigma CrReReReCr | phase_label_not_mapped | label 'sigma CrReReReCr' |
| ORC-ZTNMA6TSUQ.418ae0 | CR-RE | HM_FORM | 0.0 | sigma ReReReReCr | phase_label_not_mapped | label 'sigma ReReReReCr' |
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
| ORC-CRKNTRUNLX.931c23 | CU | HM_FORM | 0.0 | fcc-Cu | phase_label_not_mapped | label 'fcc-Cu' |
| ORC-43XXWNSX7A.90f41f | CU-HF | HM_FORM | 0.0 | Cu54Hf14 | phase_label_not_mapped | label 'Cu54Hf14' |
| ORC-CSUTXAAKBW.5d83f6 | CU-HF | HM_FORM | 0.0 | Cu54Hf14 | phase_label_not_mapped | label 'Cu54Hf14' |
| ORC-S3QCHLIENU | ER-TE | HM_FORM | 0.0 | ErTe2 | phase_label_not_mapped | label 'ErTe2' |
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
| ORC-RYYYSEVZSO.c3a675 | FE-TI | HM_FORM | 0.0 | Fe₂Ti | phase_label_not_mapped | label 'Fe₂Ti' |
| ORC-VDN6MXRL2P.4d25f4 | FE-ZR | HM_FORM | 1573.15 | Fe23Zr6, γ | phase_label_not_mapped | label 'γ' |
| ORC-4JQQ3TFAUG | GE-NI | HM_FORM | 0.0 | βNi3Ge | phase_label_not_mapped | label 'βNi3Ge' |
| ORC-YH7G2WPY74.c322d4 | GE-NI | HM_FORM | 0.0 | ε'Ni5Ge3 | phase_label_not_mapped | label "ε'Ni5Ge3" |
| ORC-36JRTTLT2M.c91987 | H-ZR | HM_FORM | 0.0 | δ-ZrH2 | phase_label_not_mapped | label 'δ-ZrH2' |
| ORC-O62YLDXJZW | LA | HM_FORM | 0.0 | La | phase_label_not_mapped | label 'La' |
| ORC-FJ27JVPBJZ.0796f2 | MG | HM_FORM | 0.0 | hcp-Mg | phase_label_not_mapped | label 'hcp-Mg' |
| ORC-YKAUVRLVC3.a77c6d | MG | HM_FORM | 0.0 | γ-Mg5Mg12Mg12 | phase_label_not_mapped | label 'γ-Mg5Mg12Mg12' |
| ORC-LOEUZNK44H.0d74e1 | MG-SB | HM_FORM | 773.0 | Mg3Sb2 | phase_label_not_mapped | label 'Mg3Sb2' |
| ORC-762YX4YIBD.b779ea | MG-Y | HM_FORM | 298.15 | YMg | phase_label_not_mapped | label 'YMg' |
| ORC-CYC6AI774I.f54d0e | MG-Y | HM_FORM | 298.15 | YMg | phase_label_not_mapped | label 'YMg' |
| ORC-EX4LZX3VS4.3747c8 | MG-Y | HM_FORM | 298.15 | Y5Mg24 | phase_label_not_mapped | label 'Y5Mg24' |
| ORC-QHJH57VUHP.eeea42 | MG-Y | HM_FORM | 298.15 | Y5Mg24 | phase_label_not_mapped | label 'Y5Mg24' |
| ORC-2IE4CVLKVW | MN-O | HM_FORM | 298.15 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-5XFZM5QTXJ | MN-O | HM_FORM | 298.15 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-6MEP3VUEHP | MN-O | HM_FORM | 298.15 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-6YP2G43BAO | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-7LBOS3ZMGS | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-C672B4OYB3 | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-DIT7OPGPC6 | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-ED4AB7EXCW | MN-O | HM_FORM | 298.15 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-FODYDWIRAG | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-FR3Y2JBCSB | MN-O | HM_FORM | 298.15 | Bixbyite (Mn2O3) | phase_label_not_mapped | label 'Bixbyite (Mn2O3)' |
| ORC-IPRFS25TUD | MN-O | HM_FORM | 298.15 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-KWTNDMGT4W | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-LV2XM5E2UV | MN-O | HM_FORM | 298.15 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-NEDTVO5RID | MN-O | SM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-PU4GVT75GB | MN-O | HM_FORM | 298.15 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-SCL3HUZ64I | MN-O | HM_FORM | 298.15 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-VH7ZWPJY45 | MN-O | HM_FORM | 298.15 | Hausmannite (Mn3O4) | phase_label_not_mapped | label 'Hausmannite (Mn3O4)' |
| ORC-VK3JCM3HZI | MN-O | HM_FORM | 298.15 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-VVCEA7QBGW | MN-O | HM_FORM | 298.15 | Mn3O4 | phase_label_not_mapped | label 'Mn3O4' |
| ORC-X6UOHCZYKT | MN-O | HM_FORM | 298.15 | Pyrolusite (MnO2) | phase_label_not_mapped | label 'Pyrolusite (MnO2)' |
| ORC-X7TRQ4WAKF | MN-O | HM_FORM | 298.15 | Bixbyite (Mn2O3) | phase_label_not_mapped | label 'Bixbyite (Mn2O3)' |
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
| ORC-LI75RO5UOF.0e04e4 | N-ZR | HM_FORM | 298.15 | (αZr) | phase_label_not_mapped | label '(αZr)' |
| ORC-MEZEELF2S3.15e327 | N-ZR | HM_FORM | 0.0 | ZrN3 | phase_label_not_mapped | label 'ZrN3' |
| ORC-TDKQYWMQ63.00a265 | N-ZR | HM_FORM | 298.15 | αZr | phase_label_not_mapped | label 'αZr' |
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
| ORC-KDDHYBPV3V.1f1c2c | NB-NI | HM_FORM | 0.0 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KDDHYBPV3V.9e54ef | NB-NI | HM_FORM | 298.15 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-KNMXYXBOEW.6c652d | NB-NI | HM_FORM | 298.15 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-LFR5XFEABG.91d157 | NB-NI | HM_FORM | 0.0 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-UZM6JPBUE2.b2325a | NB-NI | HM_FORM | 298.15 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-UZM6JPBUE2.c22fe6 | NB-NI | HM_FORM | 0.0 | μ-Nb7Ni6, µ-Nb7Ni6 | phase_label_not_mapped | label 'µ-Nb7Ni6' |
| ORC-V6DVVRGG5E.11e0a4 | NB-NI | HM_FORM | 600.15 | Nb7Ni6 | phase_label_not_mapped | label 'Nb7Ni6' |
| ORC-MDJMCVRYSE.1f557a | NB-SI | HM_FORM | 273.15 | (NbSi2) | phase_label_not_mapped | label '(NbSi2)' |
| ORC-2KBA7NMGGX.1f473d | ND-RU | HM_FORM | 0.0 | Nd3Ru | phase_label_not_mapped | label 'Nd3Ru' |
| ORC-N2B42IOD2X.1ce4aa | ND-RU | HM_FORM | 0.0 | Nd3Ru | phase_label_not_mapped | label 'Nd3Ru' |
| ORC-TJTQXRTTEQ | NI-PT | HM_FORM | 0.0 | NiPt | phase_label_not_mapped | label 'NiPt' |
| ORC-22FCDAQURR | NI-RU | HM_FORM | 0.0 | NiRu | phase_label_not_mapped | label 'NiRu' |
| ORC-EEJVYGIGY3 | NI-RU | HM_FORM | 0.0 | Ni3Ru | phase_label_not_mapped | label 'Ni3Ru' |
| ORC-UKEBJMLR64 | NI-RU | HM_FORM | 0.0 | Ni2Ru2 | phase_label_not_mapped | label 'Ni2Ru2' |
| ORC-ZC5QIC3EQM | NI-RU | HM_FORM | 0.0 | NiRu3 | phase_label_not_mapped | label 'NiRu3' |
| ORC-DJW67EF4ZM.2ce8e3 | NI-SI | HM_FORM | 298.15 | L12 | phase_label_not_mapped | label 'L12' |
| ORC-DYBIVMPQDE.17e4c5 | NI-SI | HM_FORM | 298.15 | Ni3Si(β1) | phase_label_not_mapped | label 'Ni3Si(β1)' |
| ORC-GD6EKDN36L.0c78bd | NI-SI | HM_FORM | 298.15 | ε | phase_label_not_mapped | label 'ε' |
| ORC-2YDOIF7YWA | NI-TI | HM_FORM | 1460.0 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-3VGEQTV6FF | NI-TI | HM_FORM | 298.15 | Ni3Ti(D024) | phase_label_not_mapped | label 'Ni3Ti(D024)' |
| ORC-4R2G2JJ6I6.0053d5 | NI-TI | HM_FORM | 0.0 | TiNi-B2 | phase_label_not_mapped | label 'TiNi-B2' |
| ORC-BEB5Y4LZT2 | NI-TI | HM_FORM | 999.0 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-HYPU3NBXDV | NI-TI | HM_FORM | 298.15 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-L2OPU6DDBU.b904a0 | NI-TI | HM_FORM | 0.0 | TiNi3 | phase_label_not_mapped | label 'TiNi3' |
| ORC-PEPGNW2DTY.86597c | NI-TI | HM_FORM | 298.15 | Ti2Ni | phase_label_not_mapped | label 'Ti2Ni' |
| ORC-W2AEPF25IN | NI-TI | HM_FORM | 298.15 | NiTi(B2) | phase_label_not_mapped | label 'NiTi(B2)' |
| ORC-YEW6RRQCYU.9b4e30 | NI-TI | HM_FORM | 298.15 | TiNi-B2 | phase_label_not_mapped | label 'TiNi-B2' |
| ORC-AC5XP45GUD.931f48 | O-PB | SM | 298.15 | PbO-L | phase_label_not_mapped | label 'PbO-L' |
| ORC-GHCN4AU6KY.0f4f25 | O-PB | GM_FORM | 298.15 | PbO-L | phase_label_not_mapped | label 'PbO-L' |
| ORC-H6CAMZNZB6.9934b5 | O-PB | GM_FORM | 298.15 | Pb3O4-T | phase_label_not_mapped | label 'Pb3O4-T' |
| ORC-OMX5IAEZKZ.9bd070 | O-PB | HM_FORM | 298.15 | Pb3O4-T | phase_label_not_mapped | label 'Pb3O4-T' |
| ORC-SRQYCLOPWT.a90ea0 | O-PB | GM_FORM | 298.15 | Pb3O4-T | phase_label_not_mapped | label 'Pb3O4-T' |
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
| ORC-AZHIIJFVVN.0f8013 | PU-U | CPM | 773.0 | α | phase_label_not_mapped | label 'α' |
| ORC-K3HZTEHG2L.f8e0f3 | PU-U | CPM | 673.0 | α | phase_label_not_mapped | label 'α' |
| ORC-KSXPAH2RSB.4db829 | PU-U | CPM | 840.0 | α | phase_label_not_mapped | label 'α' |
| ORC-3SL7ENTGNY.4a82b7 | RE | HM_FORM | 0.0 | sigma ReReReReRe | phase_label_not_mapped | label 'sigma ReReReReRe' |
| ORC-YQE3JLSV6E | RE-SI | HM_FORM | 298.15 | ReSi1.8 | phase_label_not_mapped | label 'ReSi1.8' |
| ORC-VURWOO5JZR.83958d | RE-TA | GM_FORM | 298.15 | TaRe1.85 (χ) | phase_label_not_mapped | label 'TaRe1.85 (χ)' |
| ORC-VURWOO5JZR.841657 | RE-TA | GM_FORM | 298.15 | TaRe1.85 (χ) | phase_label_not_mapped | label 'TaRe1.85 (χ)' |
| ORC-VURWOO5JZR.f2d89c | RE-TA | GM_FORM | 298.15 | TaRe3.6 (χ) | phase_label_not_mapped | label 'TaRe3.6 (χ)' |
| ORC-37FC3SIAD7.bccaa4 | SB-ZN | HM_FORM | 806.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-37FC3SIAD7.ecb149 | SB-ZN | GM_FORM | 806.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-5XSEGZQBR3.c07b17 | SB-ZN | HM_FORM | 826.15 | β-Zn9Sb7 | phase_label_not_mapped | label 'β-Zn9Sb7' |
| ORC-5XSEGZQBR3.c2c961 | SB-ZN | GM_FORM | 826.15 | β-Zn9Sb7 | phase_label_not_mapped | label 'β-Zn9Sb7' |
| ORC-HTTS63YOJG.2f0354 | SB-ZN | GM_FORM | 800.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-HTTS63YOJG.aceeb6 | SB-ZN | HM_FORM | 800.15 | α-Zn9Sb7 | phase_label_not_mapped | label 'α-Zn9Sb7' |
| ORC-AVCIAILA5H | SI-U | HM_FORM | 298.15 | USi | phase_label_not_mapped | label 'USi' |
| ORC-CCGYQZRSVK | SI-U | HM_FORM | 298.15 | USi | phase_label_not_mapped | label 'USi' |
| ORC-MGA3VU6PIM | SI-U | HM_FORM | 298.15 | USi | phase_label_not_mapped | label 'USi' |
| ORC-PN7BWE5QAM | SI-U | HM_FORM | 298.15 | USi2 | phase_label_not_mapped | label 'USi2' |
| ORC-Q6OGIGUYRX | SI-U | HM_FORM | 298.15 | USi2 | phase_label_not_mapped | label 'USi2' |
| ORC-ZBLVBWLP4M | SI-U | HM_FORM | 298.15 | USi2 | phase_label_not_mapped | label 'USi2' |
| ORC-4GRDKBOGIM.4fa341 | SI-Y | HM_FORM | 298.15 | YSi2 | phase_label_not_mapped | label 'YSi2' |
| ORC-6S6FJDBDPS.361c7d | SI-Y | HM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-BXE4DG4MGE | SI-Y | HM_FORM | 0.0 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-DI7K5WNBQD.9f1700 | SI-Y | HM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-DSMEXZLUVF.79fcd5 | SI-Y | HM_FORM | 298.15 | Y5Si3 | phase_label_not_mapped | label 'Y5Si3' |
| ORC-K47LECRQ4P | SI-Y | HM_FORM | 0.0 | YSi2 (H) | phase_label_not_mapped | label 'YSi2 (H)' |
| ORC-PXWJTJAKXJ | SI-Y | HM_FORM | 0.0 | YSi2 (R) | phase_label_not_mapped | label 'YSi2 (R)' |
| ORC-URIPMRCZ3I.8cc05d | SI-Y | HM_FORM | 298.15 | YSi2 | phase_label_not_mapped | label 'YSi2' |
| ORC-URIPMRCZ3I.d59230 | SI-Y | SM_FORM | 298.15 | YSi2 | phase_label_not_mapped | label 'YSi2' |
| ORC-YTPULMUAG2.38164d | SN-TI | HM_FORM | 298.15 | SnTi2 | phase_label_not_mapped | label 'SnTi2' |
| ORC-YTPULMUAG2.3a933d | SN-TI | HM_FORM | 298.15 | Sn3Ti5 | phase_label_not_mapped | label 'Sn3Ti5' |
| ORC-YTPULMUAG2.da0b8e | SN-TI | HM_FORM | 298.15 | SnTi3 | phase_label_not_mapped | label 'SnTi3' |
| ORC-VPO6TJUC6Z | TA | HM_FORM | 0.0 | Ta13 | phase_label_not_mapped | label 'Ta13' |
| ORC-BLE5GGHL7A | TI | HM_FORM | 0.0 | Laves C14 | phase_label_not_mapped | label 'Laves C14' |
| ORC-RGTIP2LC4R.8f3744 | ZR | HM_FORM | 0.0 | hcp-Zr | phase_label_not_mapped | label 'hcp-Zr' |


## 7. Literature-level consistency gates (literature-gates 2026-10-24 (cleanup))

Every value was checked against its table, its paper, the physics of its quantity and the calculated SGTE diagrams of its system (tools/literature_gates.py; tests tools/tests/test_literature_gates.py). No record is deleted and no printed value or quote is altered. A correction is made only when it is deterministic and evidenced (a printed header, caption or heading, or the internal consistency of a whole table) and, for table-level unit / sign / scale changes and system reassignments, confirmed on the rendered PDF page (`visual_check` {page, image sha256, verdict, what was seen}; tools/literature_visual_checks.json). The stored value is kept (`value_stored`, `temperature_K_stored`, `system_stored`, `property_code_before_gates`, `evidence_class_before_gates`, `phases_stored`) and the record carries `corrections`. Otherwise the record is demoted or flagged: `gate_failures` [{gate, code, effect, detail}] (codes also in `flags.gate_failures`); effect `not_accepted` sets `extraction_accepted` false, `not_espei_ready` sets `espei_ready` and `espei_certified` false, `flag_only` changes nothing else.

| | before | after |
|---|---:|---:|
| records | 77540 | 73542 |
| extraction_accepted | 76600 | 65284 |
| espei_ready (after the gates, before the ESPEI phase rule and blocking flags; released count in `espei.espei_ready`) | 14205 | 12980 |
| records with corrections | | 15528 |
| records with gate failures | | 12067 |
| page-check ledger entries (tools/literature_visual_checks.json) | | 3152 |
| page-check keys looked up by the gates (table entries expanded to rows) | | 3193 |

| gate | code | action | n |
|---|---|---|---:|
| A1 elements, chemical systems, compositions (audit round 2) | `c1_double_division_cell` | corrected | 19 |
| A1 elements, chemical systems, compositions (audit round 2) | `c1_double_division_table` | corrected | 410 |
| A1 elements, chemical systems, compositions (audit round 2) | `c1_genuinely_dilute_on_page` | kept | 10 |
| A1 elements, chemical systems, compositions (audit round 2) | `c2_axis_flipped_row` | corrected | 10 |
| A1 elements, chemical systems, compositions (audit round 2) | `c2_axis_flipped_table` | corrected | 60 |
| A1 elements, chemical systems, compositions (audit round 2) | `c3_composition_phase_permutation` | corrected | 28 |
| A1 elements, chemical systems, compositions (audit round 2) | `c3_composition_read_from_page` | corrected | 65 |
| A1 elements, chemical systems, compositions (audit round 2) | `c4_system_of_the_state` | corrected | 7779 |
| A1 elements, chemical systems, compositions (audit round 2) | `c6_page_fix` | corrected | 6 |
| A1 elements, chemical systems, compositions (audit round 2) | `c6_stale_zero_dropped` | corrected | 52 |
| A1 elements, chemical systems, compositions (audit round 2) | `c7_basis_resolved_on_page` | corrected | 15 |
| A1 elements, chemical systems, compositions (audit round 2) | `composition_axis_suspect_row` | flagged | 2 |
| A1 elements, chemical systems, compositions (audit round 2) | `composition_basis_unresolved` | flagged | 103 |
| A1 elements, chemical systems, compositions (audit round 2) | `composition_outside_unit_interval` | demoted | 36 |
| A1 elements, chemical systems, compositions (audit round 2) | `label_conflicts_composition` | flagged | 238 |
| A1 elements, chemical systems, compositions (audit round 2) | `r3_overall_composition_conflicts_label` | flagged | 74 |
| A1 elements, chemical systems, compositions (audit round 2) | `r3_overall_composition_from_formula` | corrected | 419 |
| A1 elements, chemical systems, compositions (audit round 2) | `r3_reference_state_outside_system_dropped` | corrected | 3031 |
| G1 temperatures | `liquid_below_physical_minimum` | demoted | 10 |
| G1 temperatures | `liquid_below_physical_minimum` | flagged | 24 |
| G1 temperatures | `liquid_temperature_corrected_from_page` | corrected | 2 |
| G1 temperatures | `non_temperature_corrected_from_page` | corrected | 4 |
| G1 temperatures | `sibling_row_celsius_corrected` | corrected | 5 |
| G1 temperatures | `standard_reference_temperature_298.15` | corrected | 2790 |
| G1 temperatures | `table_temperature_unit_confirmed_as_stored` | checked | 6 |
| G1 temperatures | `table_temperature_unit_corrected` | corrected | 132 |
| G1 temperatures | `temperature_not_a_temperature` | demoted | 7 |
| G1 temperatures | `temperature_range_stored_as_point` | flagged | 2 |
| G10 reader tier / agreement | `reader_agreement_derived_multi_reader` | derived | 31439 |
| G10 reader tier / agreement | `reader_agreement_derived_single_reader` | derived | 451 |
| G10 reader tier / agreement | `reader_agreement_derived_single_reader_text_layer` | derived | 162 |
| G11 CALPHAD plausibility fields | `fail_small_dT_composition` | explained | 198 |
| G11 CALPHAD plausibility fields | `fail_small_dT_composition_pure_element_label` | explained | 88 |
| G11 CALPHAD plausibility fields | `fail_small_dT_unexplained` | explained | 1 |
| G12 pressure basis | `pressure_basis_relabelled` | relabelled | 77535 |
| G2 energies, entropies, heat capacities, activities | `mass_basis_unit_relabelled` | corrected | 171 |
| G2 energies, entropies, heat capacities, activities | `per_formula_divided` | corrected | 1 |
| G2 energies, entropies, heat capacities, activities | `table_unit_scale_applied` | corrected | 289 |
| G2 energies, entropies, heat capacities, activities | `table_unit_scale_suspect` | demoted | 8 |
| G2 energies, entropies, heat capacities, activities | `unit_not_printed` | corrected | 13 |
| G2 energies, entropies, heat capacities, activities | `unit_not_read_value_out_of_range` | flagged | 21 |
| G2 energies, entropies, heat capacities, activities | `value_corrected_from_page` | corrected | 3 |
| G2 energies, entropies, heat capacities, activities | `value_out_of_physical_range` | demoted | 34 |
| G2 energies, entropies, heat capacities, activities | `value_out_of_physical_range` | flagged | 1 |
| G2 energies, entropies, heat capacities, activities | `value_outside_typical_range_as_printed` | flagged | 71 |
| G3 signs | `formation_positive_check_sign` | flagged | 1 |
| G3 signs | `positive_formation_confirmed_on_page` | checked | 50 |
| G3 signs | `sign_corrected_from_page` | corrected | 10 |
| G3 signs | `sign_from_heading_applied` | corrected | 31 |
| G3 signs | `sign_heading_not_applied` | flagged | 1 |
| G3 signs | `unsigned_in_print_blocks_espei` | flagged | 43 |
| G4 system assignment | `magnitude_suspect_blocks_espei` | flagged | 17 |
| G4 system assignment | `system_confirmed_label_typo` | flagged | 50 |
| G4 system assignment | `system_mismatch` | demoted | 3 |
| G4 system assignment | `system_reassigned` | corrected | 147 |
| G4 system assignment | `system_reassigned_from_page` | corrected | 180 |
| G5 property semantics | `entropy_increment` | corrected | 30 |
| G5 property semantics | `formation_code_in_unary_system` | demoted | 4 |
| G5 property semantics | `formation_on_liquid` | flagged | 22 |
| G5 property semantics | `liquid_property_at_room_temperature` | flagged | 20 |
| G5 property semantics | `mix_to_form` | corrected | 286 |
| G5 property semantics | `model_parameter_not_property` | demoted | 185 |
| G5 property semantics | `printed_entropy_of_formation` | corrected | 26 |
| G5 property semantics | `printed_excess_entropy` | corrected | 1 |
| G5 property semantics | `printed_magnetic_contribution` | corrected | 16 |
| G5 property semantics | `unary_fusion_quantity` | corrected | 12 |
| G5 property semantics | `unary_lattice_stability` | corrected | 21 |
| G6 invariant phase lists | `binary_degenerate_reaction_as_printed` | flagged | 20 |
| G6 invariant phase lists | `binary_more_than_three_phases` | flagged | 5 |
| G6 invariant phase lists | `phase_added_on_page` | corrected | 162 |
| G6 invariant phase lists | `phase_list_corrected_on_page` | corrected | 182 |
| G6 invariant phase lists | `phase_list_normalized` | corrected | 572 |
| G6 invariant phase lists | `reaction_liquid_count_inconsistent` | flagged | 107 |
| G6 invariant phase lists | `reaction_liquid_count_inconsistent_as_printed` | flagged | 126 |
| G6 invariant phase lists | `reaction_phase_count_inconsistent` | flagged | 15 |
| G6 invariant phase lists | `reaction_phase_count_inconsistent_as_printed` | flagged | 14 |
| G6 invariant phase lists | `reaction_type_corrected_on_page` | corrected | 17 |
| G6 invariant phase lists | `ternary_more_than_four_phases` | flagged | 89 |
| G7 duplicates | `cosmetic_duplicate_merged` | merged | 3983 |
| G7 duplicates | `phase_label_readings_disagree` | flagged | 509 |
| G7 duplicates | `records_removed` | merged | 3998 |
| G8 evidence class | `assessed_source_not_experimental` | corrected | 1 |
| G8 evidence class | `evidence_change_rejected_on_check` | checked | 31 |
| G8 evidence class | `from_evaluation_paper_flagged` | flagged | 734 |
| G8 evidence class | `model_to_dft` | corrected | 5 |
| G8 evidence class | `model_to_experimental` | corrected | 47 |
| G9 compositions | `activity_rounded_to_zero` | flagged | 9 |
| G9 compositions | `composition_copied_across_rows` | flagged | 10 |
| G9 compositions | `composition_from_formula` | corrected | 4 |
| G9 compositions | `composition_label_mismatch` | flagged | 183 |
| G9 compositions | `overall_composition_sum_not_one` | flagged | 40 |
| G9 compositions | `phase_composition_sum_not_one` | flagged | 27 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `absolute_entropy_labelled_formation` | corrected | 130 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `column_property_read_from_page` | corrected | 51 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `experimental_value_from_0K_caption` | corrected | 197 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `expression_coefficient` | corrected | 623 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `first_principles_row_of_mixed_table` | corrected | 101 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `formation_entropy_out_of_range` | demoted | 24 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `formation_from_compounds` | corrected | 21 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `heat_content_row_temperature` | corrected | 901 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `heat_content_temperature_missing` | demoted | 35 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `non_crystalline_state` | flagged | 16 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `own_first_principles_row_labelled_experimental` | corrected | 13 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `per_atom_unit_printed_mol_per_at` | corrected | 25 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `quantity_printed_at_298` | corrected | 47 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `reference_state_text_not_a_phase` | corrected | 43 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `sigma_rescaled_with_value` | corrected | 172 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `standard_enthalpy_at_calorimeter_temperature` | corrected | 14 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `table_basis_value` | corrected | 125 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `table_sign_value` | corrected | 4 |
| R2 audit round 2 (2026-10-24): per-column basis and sign read on the page, printed sigma rescaled with its value, absolute entropies, heat-content and expression temperatures, 298-subscript and calorimeter temperatures, first-principles rows, formation from compounds, reference-state text (tools/literature_r2_thermo.py) | `temperature_printed_in_quantity_label` | corrected | 69 |
| R3  | `assessed_database_values` | corrected | 262 |
| R3  | `comma_decimal_formula_atoms` | corrected | 12 |
| R3  | `contribution_stored_as_total` | corrected | 116 |
| R3  | `defect_energy_stored_as_formation` | corrected | 12 |
| R3  | `emf_intercept_stored_as_emf` | corrected | 84 |
| R3  | `emf_slope_stored_as_emf` | corrected | 2 |
| R3  | `first_principles_value_coded_model` | corrected | 197 |
| R3  | `formation_below_0p1_kJ_not_page_checked` | flagged | 2 |
| R3  | `formation_value_printed_misprint` | flagged | 1 |
| R3  | `heat_content_base_temperature` | corrected | 142 |
| R3  | `printed_range_read_from_page` | corrected | 7 |
| R3  | `state_phases_from_quote` | corrected | 264 |
| R3  | `state_phases_missing` | demoted | 8944 |
| R3  | `state_phases_read_from_page` | corrected | 16 |
| R3  | `temperature_printed_not_stored` | corrected | 14 |
| R3  | `temperature_range_printed_not_stored` | corrected | 21 |
| R3  | `three_term_expression_coefficient` | corrected | 10 |
| R3  | `unit_prefix_lost_k` | corrected | 11 |
| R3I  | `duplicate_invariant_same_page` | flagged | 179 |
| R3I  | `invariant_temperature_needs_page_check` | flagged | 5 |
| R3I  | `phase_rule_count_mismatch` | flagged | 303 |
| R3I  | `phases_from_printed_reaction` | corrected | 219 |
| R3I  | `reaction_class_conflicts_printed_reaction` | flagged | 67 |
| R3I  | `reaction_class_from_printed_reaction` | corrected | 3022 |
| R3I  | `system_includes_printed_reaction_partners` | corrected | 18 |
| page page checks (visual) | `ambient_value_stored_at_0K` | flagged | 5 |
| page page checks (visual) | `bounded_temperature_not_exact_observation` | flagged | 1 |
| page page checks (visual) | `composition_attribution_ambiguous_on_page` | flagged | 2 |
| page page checks (visual) | `composition_inconsistent_with_phase_on_page` | flagged | 4 |
| page page checks (visual) | `composition_misread_on_page` | flagged | 26 |
| page page checks (visual) | `composition_printed_as_range` | flagged | 16 |
| page page checks (visual) | `composition_printed_value_garbled` | flagged | 2 |
| page page checks (visual) | `conflicting_printed_end_member_pair` | flagged | 1 |
| page page checks (visual) | `defect_energy_not_a_formation_property` | flagged | 42 |
| page page checks (visual) | `derived_at_high_temperature_from_bcc_zr` | flagged | 6 |
| page page checks (visual) | `duplicate_reading_cell_ambiguous` | flagged | 1 |
| page page checks (visual) | `duplicate_source_row` | flagged | 241 |
| page page checks (visual) | `end_member_requires_sublattice_mapping` | flagged | 6 |
| page page checks (visual) | `energy_basis_not_printed_rows_inconsistent` | flagged | 11 |
| page page checks (visual) | `expression_coefficient_not_a_value` | flagged | 119 |
| page page checks (visual) | `expression_term_missing` | flagged | 8 |
| page page checks (visual) | `filed_under_wrong_system` | flagged | 1 |
| page page checks (visual) | `glass_transition_not_an_equilibrium_state` | flagged | 2 |
| page page checks (visual) | `heat_treatment_not_equilibrium_observation` | flagged | 24 |
| page page checks (visual) | `locator_table_label_wrong` | flagged | 44 |
| page page checks (visual) | `measurement_temperature_not_stated` | flagged | 138 |
| page page checks (visual) | `measurement_temperature_various` | flagged | 20 |
| page page checks (visual) | `metastable_state` | flagged | 16 |
| page page checks (visual) | `misread_on_page` | demoted | 88 |
| page page checks (visual) | `molar_basis_unverified` | flagged | 9 |
| page page checks (visual) | `mutually_inconsistent` | flagged | 10 |
| page page checks (visual) | `oxygen_stoichiometry_unspecified` | flagged | 30 |
| page page checks (visual) | `pa_molar_basis_requires_confirmation` | flagged | 5 |
| page page checks (visual) | `pa_solution_drop_heat_not_integral_mixing` | flagged | 11 |
| page page checks (visual) | `page_fix_cited_sources` | corrected | 30 |
| page page checks (visual) | `page_fix_elements` | corrected | 178 |
| page page checks (visual) | `page_fix_evidence_class` | corrected | 180 |
| page page checks (visual) | `page_fix_overall_composition` | corrected | 254 |
| page page checks (visual) | `page_fix_overall_composition_basis` | corrected | 254 |
| page page checks (visual) | `page_fix_phases` | corrected | 8 |
| page page checks (visual) | `page_fix_property` | corrected | 238 |
| page page checks (visual) | `page_fix_property_expression` | corrected | 119 |
| page page checks (visual) | `page_fix_property_group` | corrected | 125 |
| page page checks (visual) | `page_fix_quote_page` | corrected | 2 |
| page page checks (visual) | `page_fix_reference_state` | corrected | 44 |
| page page checks (visual) | `page_fix_source_system` | corrected | 175 |
| page page checks (visual) | `page_fix_system` | corrected | 178 |
| page page checks (visual) | `page_fix_temperature_K` | corrected | 219 |
| page page checks (visual) | `page_fix_temperature_basis` | corrected | 218 |
| page page checks (visual) | `page_fix_temperature_bound` | corrected | 10 |
| page page checks (visual) | `page_fix_temperature_range_K` | corrected | 10 |
| page page checks (visual) | `page_fix_temperature_uncertainty` | corrected | 12 |
| page page checks (visual) | `page_fix_uncertainty` | corrected | 15 |
| page page checks (visual) | `page_fix_unit` | corrected | 211 |
| page page checks (visual) | `page_fix_unit_basis` | corrected | 42 |
| page page checks (visual) | `page_fix_value` | corrected | 108 |
| page page checks (visual) | `partial_property_requires_explicit_fitting_support` | flagged | 32 |
| page page checks (visual) | `phase_label_misassigned_on_page` | flagged | 2 |
| page page checks (visual) | `phase_label_not_the_value_phase` | flagged | 42 |
| page page checks (visual) | `phase_label_questionable` | flagged | 6 |
| page page checks (visual) | `phase_list_misread_corrected` | corrected | 28 |
| page page checks (visual) | `pressure_1_atm_withdrawn` | corrected | 5 |
| page page checks (visual) | `pressure_not_1_atm_on_page` | flagged | 5 |
| page page checks (visual) | `record_not_on_page` | flagged | 2 |
| page page checks (visual) | `reference_state_converted_to_ser` | flagged | 6 |
| page page checks (visual) | `row_basis_contradicts_column_header` | flagged | 15 |
| page page checks (visual) | `same_measurement_listed_in_other_paper` | flagged | 6 |
| page page checks (visual) | `source_marks_value_unreliable` | flagged | 1 |
| page page checks (visual) | `stoichiometry_mismatch` | flagged | 7 |
| page page checks (visual) | `temperature_belongs_to_other_column` | flagged | 2 |
| page page checks (visual) | `temperature_misread_from_text` | flagged | 18 |
| page page checks (visual) | `temperature_not_printed` | flagged | 20 |
| page page checks (visual) | `temperature_range_midpoint_stored_as_kelvin` | flagged | 18 |
| page page checks (visual) | `transformation_enthalpy_requires_reaction_basis` | flagged | 6 |
| page page checks (visual) | `unit_inconsistent_with_figure_on_page` | flagged | 9 |
| page page checks (visual) | `unit_scale_inconsistent_on_page` | flagged | 5 |
| page page checks (visual) | `unsigned_magnitude_in_print` | flagged | 15 |
| page page checks (visual) | `value_not_the_stated_property` | flagged | 19 |
| page page checks (visual) | `value_row_misattributed` | flagged | 2 |
| page page checks (visual) | `value_shared_by_several_compositions` | flagged | 6 |

Visual checks (rendered PDF pages inspected one by one: every table-level group, every system reassignment, and samples of at least 50 per demotion category where the category is larger; `verdict_reader` keeps the reader's verdict where a decision was curated):

| kind | verdict | n |
|---|---|---:|
| class_rule | rule_confirmed | 23 |
| composition_row | as_printed | 2 |
| composition_row | confirmed | 57 |
| composition_row | corrected | 65 |
| composition_row | rejected | 10 |
| composition_table | confirmed | 27 |
| composition_table | corrected | 1 |
| composition_table | rejected | 2 |
| dft_pairing | exact | 8 |
| dft_pairing | formula_parse_corrected | 2 |
| dft_pairing | no_structure_printed_offstoichiometric | 1 |
| evidence | confirmed | 56 |
| evidence | rejected | 31 |
| evidence_table | experimental_cited | 25 |
| evidence_table | experimental_own | 2 |
| evidence_table | mixed | 4 |
| evidence_table | model | 2 |
| flag | confirmed | 900 |
| flag_precision_sample | false_positive | 5 |
| flag_precision_sample | true_positive | 15 |
| invariant_table | checked | 160 |
| page_fix | corrected | 849 |
| page_flag | confirmed | 93 |
| page_flag | flagged | 2 |
| per_formula | corrected | 1 |
| phase_alias | confirmed | 15 |
| record_T | as_stored | 28 |
| record_T | corrected | 11 |
| record_T | misread | 16 |
| record_comp | as_stored | 50 |
| record_composition | confirmed | 1 |
| record_composition | corrected | 2 |
| record_flag | flagged | 41 |
| record_phases | as_stored | 5 |
| record_phases | corrected | 16 |
| record_phases | higher_order | 50 |
| record_phases | misread | 34 |
| record_range | corrected | 7 |
| record_system | confirmed | 5 |
| record_system | corrected | 4 |
| record_system | misread | 39 |
| record_value | as_stored | 169 |
| record_value | confirmed | 90 |
| record_value | corrected | 27 |
| record_value | misread | 96 |
| system | confirmed | 85 |
| system | misread | 9 |
| table_T_unit | as_stored | 3 |
| table_T_unit | confirmed | 8 |
| table_T_unit_sibling | confirmed | 2 |
| table_basis | decided | 8 |
| table_property | confirmed | 2 |
| table_property | decided | 2 |
| table_scale | as_stored | 1 |
| table_scale | confirmed | 14 |
| table_scale | rejected | 2 |
| table_scale | unit_not_printed | 3 |
| table_sign | confirmed | 1 |
| table_sign | decided | 1 |
| table_sign | rejected | 1 |
| table_unit | confirmed | 1 |
| table_unit | corrected | 1 |

Gate rules:

* G1 temperatures. (a) Per table, the stored temperatures (as K, or converted from °C) are compared with the table's own numbers: rows describing a pure element against its melting point in K and °C, invariant rows against the system's SGTE invariants and melting points (median distance, K vs °C reading), and the readers' unit votes. A table whose stored convention disagrees with that evidence is converted as a whole from the printed numbers once the page confirms the header unit; unconfirmed: `temperature_unit_table_suspect`. The CALPHAD cross-check of a corrected value was computed on the old temperature and is moved to `flags.plausibility_before_correction`. (b) A temperature printed as a dash, T <= 1 K for a phase equilibrium, or a temperature equal to a printed composition: `temperature_not_a_temperature` (not accepted). (c) A liquid-bearing value below the lowest temperature a liquid can have (SGTE diagram of the system minus twice the phase-rule margin; binary subsystems for higher orders; else 0.40 x the lowest melting point): `liquid_below_physical_minimum` (not ESPEI-ready; not accepted below 0.25 x the lowest melting point). (d) A printed range stored as one temperature: `temperature_range_stored_as_point`.
* G2 magnitudes. Physical ranges (kJ/mol-atom unless stated): formation enthalpy / Gibbs energy [-200, 60] (metallic) or [-650, 120] (with O, N, halogens, chalcogens, pnictogens, C, B, Si, Ge); mixing [-150, 60]; partial [-450, 250]; entropy of formation [-60, 60] J/(mol-atom K); absolute entropy [0, 150]; heat capacity [0, 120]; activity (0, 1]. Values of unstated basis are tested per atom of their single printed formula. Corrections: a printed x10^3 activity header (values divided by 1000 when the page confirms the header); a J value under a printed J unit stored as kJ; a per-formula value under a printed per-formula unit labelled per atom; a per-gram unit relabelled. Unexplained values out of range: `value_out_of_physical_range` (not accepted; relative DFT energies only not ESPEI-ready); no unit read: `unit_not_read_value_out_of_range`.
* G3 signs. A positive value under a printed (-Δ...) heading is negated when the page confirms the heading (`sign_from_heading`); `unsigned_in_print` blocks ESPEI; a positive formation enthalpy / Gibbs energy above +10 kJ/mol-atom of a compound is flagged `formation_positive_check_sign` unless the page confirms it.
* G4 system. A phase formula naming an element outside the system (or cement notation C-S = CaO-SiO2) moves the value to the system named by its phase formulas and caption when the page confirms it; otherwise `system_mismatch` (not accepted). system_mismatch, magnitude_suspect and source_disputed block ESPEI. A system element that is a pressure unit (Pa in kPa / MPa), a cover or flow gas (Ar, He) or a garbled phase prefix is never a component: such records are reassigned from the rendered page (record checks of 2026-10-24) or, without a page check, not accepted (`system_element_from_unit_or_gas`).
* G5 semantics. A mixing code whose printed quantity is a formation quantity becomes the formation code; formation / mixing codes in one-element systems become fusion or lattice-stability codes when printed as such, otherwise are not accepted; S(T)-S(298) becomes `SM_INCREMENT`; formation quantities of a liquid are flagged; Redlich-Kister parameters stored as properties are not accepted.
* G6 invariants. Phase lists drop non-phase labels (composition points, 'liquidus', 'eutectic', 'UNKNOWN' beside a named phase) and repeated phases (`phases_dropped`, `phases_stored`); binary three-phase reactions must have three phases with the right number of liquids, congruent melting two phases with one liquid, solid-state reactions no liquid; a binary row with four or more phases is flagged (likely a higher-order system). Repeats are found with a spelling-independent key (`phase_key`: subscripts, LaTeX and spelled Greek letters, prime glyphs, separators, outer parentheses); numbered liquids (L1, L2, Liquid#2) count as liquids. Page checks of whole tables (cleanup 2026-10-24, key `invariant_table:<asset>`): labels that are not phases of the row (column headers such as 'Phase 2', 'X^M', 'T/K', composition labels, a phase from a neighbouring column) are dropped (compositions printed under them move to `phase_compositions_dropped`); a phase the printed reaction names but the reading missed is added (`label_source: page_check`); the reaction type is set to the printed one (`transition_kind_stored`); a row of a higher-order system moves to the system the page names (else not accepted); a row whose odd phase count or type is printed so stays accepted and not ESPEI-ready (`*_as_printed`, `binary_degenerate_reaction_as_printed`).
* G7 duplicates. Values identical in paper, property, value, unit, temperature, table and row (or quote) that differ only cosmetically (UNKNOWN beside a named phase, glyph variants, reader lists) are merged into the most specified record (`merged_ids`). Labels are compared with `phase_key`, by contained words ('Fe3O4' / 'Magnetite (Fe3O4)') and by formula composition ('UC1.90' / 'C0.655U0.345'); two readings of one printed value with different phases are kept apart and flagged `phase_label_readings_disagree` (not ESPEI-ready).
* Display fix (2026-10-24, not a data change): the compound pages' DFT table labelled the energy above hull 'eV/atom', but `dft_parity.json` stores it in kJ/mol-atom (`ehull`; Parquet `ehull_kJ_per_mol_atom`). The column now reads 'E above hull (kJ/mol-atom)' with an eV/atom column beside it; the MCP server's `e_above_hull_eV` is now converted (and `e_above_hull_kJ_per_mol_atom` added).
* Standard reference temperature (PI rule 2026-10-24: '298 K is 298.15 K'). A temperature stored as 298 / 298.1 / 298.2 K and printed as 298 K (or read from a '298' subscript) is stored as 298.15 K, printed string kept (`standard_reference_temperature`).
* Page fixes (cleanup 2026-10-24, keys `page_fix:<id>`, `flag:<id>`): a value, unit, temperature, property code or evidence class read on the rendered page replaces the stored one (kept in `*_stored` / `*_before_gates`, `corrections` with the page check) before the other gates run; values the page prints as stored but outside the physical range stay accepted and are not ESPEI-ready (`value_outside_typical_range_as_printed`).
* G8 evidence class. Running-text model values whose sentence names only first-principles methods become `dft`; those whose sentence names only experimental methods (and cite a source) become `experimental` (cited); both only when the page check confirms the sentence context (otherwise `evidence_class_review`). Values read from ASM / JPE phase-diagram evaluations (title '<A>-<B> (<Name>-<Name>)') carry `flags.from_evaluation_paper`; an evaluation's own value labelled experimental becomes `unspecified` with `flags.assessed_source` (cited measurements stay experimental). CALPHAD 'thermodynamic assessment' papers with their own experiments are not evaluations in this sense.
* G9 compositions. Compositions not summing to 1, printed compositions far from the printed formula (and compositions repeated from another row) are flagged; recomputed from the printed formula when the page confirms the formula; activities stored as 0 are not ESPEI-ready. A printed composition far from its label's formula is, on the page sample, a real solubility / homogeneity range as printed: flag only (`composition_label_mismatch`); compositions copied across rows block ESPEI.
* G10 readers. `reader_tier` is the pipeline status of the table or passage (which reader passes ran), not a claim about the value; a row read only by a later reader can carry the table's earlier tier. The agreement claim is `reader_agreement`; where the record builder did not classify a value (invariant tables, running text) it is derived from `readers` (`reader_agreement_basis: derived_from_readers`; settled rows only).
* G11 plausibility. `flags.plausibility` carries dx (mole-fraction differences per phase) and the calculation; fails with |dT| < 5 K have `fail_reason` (composition; pure-element label compared on the other axis).
* G12 pressure. 1 atm defaults (stated_default_1_atm, unstated_assumed) are relabelled `assumed_default_1_atm_not_printed` (`pressure_basis_stored` kept).


## Model-phase mapping check (audit round 2, A2 class 1)

`tools/phase_label_check.py` (phase-label-check 2026-10-24 (audit round 2, A2 class 1)). A model phase attached by the corpus mapping is removed when the printed label cannot name it; the printed label is unchanged, the removed model phase, its Pearson symbol / prototype and the reason are kept in `phases[].model_phase_rejected`, and the record gets a `corrections` entry (gate `PL`). Pearson symbols and prototypes that remain come from the mapped model phase, not from the page: `phases[].structure_basis = mapped_model_phase`.

Rules: (a rejected mapping is removed; the model phase, its structure and the reason are kept in `model_phase_rejected`; the printed label is never changed): R1 element-structure model (FCC_A1, BCC_A2, HCP_A3, DIAMOND_A4 ... GRAPHITE_A9, DHCP, A1_FCC ...): kept only when the printed label names a terminal solution or pure element ("(Fe)", "(alphaTi)", "gamma-Fe", "(Cu,Ni)"), names the structure itself ("beta (bcc)", "A2", "fcc"), or is an interstitial compound M X_n (X = C, N, H, O, B) that the target model holds on an interstitial (X, VA) sublattice (SGTE convention, e.g. TiC -> FCC_A1, V2C -> HCP_A3). A bare Greek letter is kept only when it is the conventional name of a polymorph of one of the system's elements with that structure (no other Greek -> structure fallback; Hume-Rothery names such as beta brass are left unmapped) (alpha-Ti hcp, beta-Zr bcc, gamma-Fe fcc, delta-Pu fcc ...; POLYMORPH); a Greek-prefixed compound, a primed / numbered Greek label or any other compound is never mapped to an element structure; an element label whose Greek polymorph contradicts the model (beta-B -> BCC_A2) is rejected. R2 a structure word in the label that contradicts the model (label "bcc", model FCC_A1) rejects the mapping. R3 a label that names a liquid ("L(phi2)", "L + ...") is never mapped to a non-liquid model. R3b a Greek / compound label mapped to the same model as a terminal-solution label of the same row ("(deltaMn)" and "eps" both BCC_A2) is rejected: two printed phases of one equilibrium are not one model phase. R4 a printed mole-fraction composition of the phase must lie inside the model phase's calculated stability range in the system (data/phases stability rows, any assessment) +- 0.1; otherwise the mapping is rejected. Per-system aliases (tools/phase_aliases.py, tools/phase_aliases.json; 2026-10-24) are applied BEFORE these rules: a printed label that is a conventional name of a phase of the record's binary system (beta brass -> BCC_A2 in Cu-Zn, eps -> Cu3Sn in Cu-Sn, kappa -> HCP_A3 in Cu-Si ...) is mapped to that system's TDB phase when the printed composition / temperature agree with the alias; the phase gets `model_phase_basis: system_alias:<id>` (a changed mapping also a `corrections` entry, rule `system_alias:<id>`) and is not re-checked by the Greek rule. Two printed phases of one row are never put on one model phase by an alias.

| result | phase mentions |
|---|---:|
| alias_applied | 673 |
| alias_applied:no_corpus_mapping | 184 |
| alias_applied:replaced_corpus_mapping | 489 |
| alias_confirms_corpus_mapping | 607 |
| alias_not_applied:alias_excluded_in_record_tdb | 10 |
| alias_not_applied:composition_outside_alias_range | 37 |
| alias_not_applied:printed_formula_differs_from_alias | 2 |
| alias_not_applied:same_model_as_another_phase_of_the_row | 36 |
| alias_not_applied:temperature_outside_alias_range | 5 |
| kept | 75176 |
| kept_by_system_alias | 1280 |
| rejected | 2397 |
| rejected:composition_outside_model_phase_range | 244 |
| rejected:element_polymorph_contradicts_model | 379 |
| rejected:greek_label_not_an_element_polymorph_of_this_structure | 327 |
| rejected:greek_or_compound_label_mapped_to_element_structure | 954 |
| rejected:label_not_a_solution_or_structure_name | 205 |
| rejected:liquid_label_mapped_to_non_liquid_model | 52 |
| rejected:same_model_as_another_phase_of_the_row | 19 |
| rejected:structure_word_contradicts_model | 45 |
| rejected:terminal_element_absent_from_model_endmembers | 145 |
| rejected:variable_formula_label_not_a_fixed_compound | 27 |
| terminal_mapping_corrected | 369 |

Per-system aliases (`tools/phase_aliases.json`, 64 aliases in 32 systems) applied before the rules: a conventional phase name of the record's binary system is mapped to that system's TDB phase when the printed composition / temperature agree (`model_phase_basis: system_alias:<id>`).

| alias | label | model phase | phase mentions mapped |
|---|---|---|---:|
| al-fe:epsilon | ε | AL8FE5_D82 | 122 |
| fe-ta:epsilon | ε | C14_LAVES | 52 |
| mn-zn:epsilon | ε | HCP_IM_A3 | 49 |
| ni-zn:beta | β | NIZN_B2 | 39 |
| cu-sn:epsilon | ε | CU3SN_L | 35 |
| ni-zn:beta1 | β1 | NIZN_L10 | 25 |
| al-mn:epsilon | ε | HCP_A3 | 24 |
| co-ga:beta | β | COGA_B2 | 22 |
| al-nb:epsilon | ε | AL3NB_D022 | 21 |
| c-zr:gamma | γ | FCC_A1 | 19 |
| cu-si:epsilon | ε | CU15SI4 | 19 |
| al-ni:gammaprime | γ′ (Ni3Al) | L12_FCC | 18 |
| al-ta:epsilon | ε | AL3TA_D022 | 17 |
| cu-in:delta | δ | CU7IN3 | 16 |
| al-cd:alpha | α(Al) | FCC_A1 | 14 |
| cu-zn:delta | δ | BCC_A2 | 13 |
| cu-zn:epsilon | ε | HCP_IM_A3 | 12 |
| al-ni:gammaprime | γ' | L12_FCC | 10 |
| cu-sn:beta | β | BCC_A2 | 9 |
| fe-zn:Gamma1 | Γ1 | FEZN4 | 9 |
| mo-pd:epsilon | ε | HCP_A3 | 9 |
| c-zr:alpha | α | HCP_A3 | 8 |
| cu-sn:alpha | α | FCC_A1 | 8 |
| ni-zn:beta | beta | NIZN_B2 | 7 |
| ag-sb:epsilon | ε | AG3SB | 6 |
| al-fe:epsilon | ε | AL5FE4 | 6 |
| al-mg:epsilon | ε | ALMG_EPS | 6 |
| cu-sn:epsilon | ε (Cu3Sn) | CU3SN_L | 6 |
| cu-zn:epsilon | ϵ | HCP_IM_A3 | 6 |
| fe-zn:zeta | ζ | FEZN13 | 6 |
| pd-zn:beta1 | β1 | PDZN_L2A | 6 |
| ag-al:zeta | ζ | HCP_A3 | 5 |
| ag-in:alphaprime | α' | AG3IN_L12 | 4 |
| ag-zn:epsilon | ε | HCP_IM_A3 | 4 |
| cr-ir:epsilon | ε | HCP_A3 | 4 |
| fe-zn:delta | δ | FEZN10 | 4 |
| ni-zn:beta1 | β1 | NIZN_B11 | 4 |
| pd-zn:beta | β | B2_BCC | 4 |
| pd-zn:beta1 | β1 phase | PDZN_L2A | 4 |
| al-ni:gamma | γ | FCC_A1 | 3 |
| b-ni:beta | β | BETA_RHOMBO_B | 3 |
| ni-zn:beta1 | beta1 | NIZN_L10 | 3 |
| al-mg:epsilon | ε-Al30Mg23 | ALMG_EPS | 2 |
| au-zn:betaprime | β' | AUZN_B2 | 2 |
| au-zn:betaprime | β’ | AUZN_B2 | 2 |
| fe-zn:Gamma | Γ | FE3ZN7_D82 | 2 |
| al-ni:gammaprime | γ’ | L12_FCC | 1 |
| cu-fe:epsilon | ε | FCC_A1 | 1 |
| cu-sb:beta | β (Cu3Sb) | BCC_A2 | 1 |
| cu-si:epsilon | ε-Cu15Si4 | CU15SI4 | 1 |

Most frequent rejected mappings:

| system | label | model phase | reason | n |
|---|---|---|---|---:|
| C-U | φ1 | GRAPHITE_A9 | greek_or_compound_label_mapped_to_element_structure | 97 |
| C-U | φ2 | GRAPHITE_A9 | greek_or_compound_label_mapped_to_element_structure | 97 |
| GE-NI | βNi3Ge | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 38 |
| NI-SB | (βNi5Sb2) | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 34 |
| C-U | L(φ1) | GRAPHITE_A9 | liquid_label_mapped_to_non_liquid_model | 34 |
| AU-CE | βCeAu | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 31 |
| AL-MO | AlMo | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 30 |
| CU-FE | ε | BCC_A2 | greek_label_not_an_element_polymorph_of_this_structure | 30 |
| AL-TI | ε(h) | BCC_A2 | label_not_a_solution_or_structure_name | 28 |
| AL-SM | β | BCC_A2 | greek_label_not_an_element_polymorph_of_this_structure | 27 |
| CO-SB | (βCoSb) | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 26 |
| SB-ZN | β-Zn3Sb2 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 26 |
| SB-ZN | β-Zn9Sb7 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 23 |
| AL-NB-TI | α2 | DIAMOND_A4 | greek_or_compound_label_mapped_to_element_structure | 22 |
| AL-MN | γ | A2_BCC | greek_label_not_an_element_polymorph_of_this_structure | 20 |
| AL-NB-TI | ε | BCC_A2 | greek_label_not_an_element_polymorph_of_this_structure | 20 |
| SB-ZN | β-Zn13Sb10 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 20 |
| FE-SB | β(FeSb) | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 18 |
| AU-CE | βCe14Au51 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 17 |
| AL-CU | ε | BCC_A2 | greek_label_not_an_element_polymorph_of_this_structure | 16 |
| CO-GE | α(Co) | DIAMOND_A4 | terminal_element_absent_from_model_endmembers | 16 |
| AL-NI-W | α | DIAMOND_A4 | greek_label_not_an_element_polymorph_of_this_structure | 16 |
| PT-TI | βTiPt | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 15 |
| C-U | L(φ2) | GRAPHITE_A9 | liquid_label_mapped_to_non_liquid_model | 15 |
| AU-IN | α1 | DHCP | greek_or_compound_label_mapped_to_element_structure | 14 |
| GE-SC | (αSc) | DIAMOND_A4 | terminal_element_absent_from_model_endmembers | 14 |
| NI-SB | (βNi3Sb) | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 14 |
| AL-CR | βCr5Al8 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 13 |
| AU-CE | αCe14Au51 | AUCE_B27 | composition_outside_model_phase_range | 13 |
| AU-ND | βNdAu | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 13 |
| CO-GE | ε(Co) | BCC_A2 | element_polymorph_contradicts_model | 13 |
| CO-TI | β-Ti | HCP_A3 | element_polymorph_contradicts_model | 13 |
| SN-YB | βYb5Sn3 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 12 |
| FE-TA | λ, ε, TaFe2 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 12 |
| NI-SN | Ni3Sn_HT | BCC_A2 | label_not_a_solution_or_structure_name | 12 |
| AL-NB-TI | α | DIAMOND_A4 | greek_label_not_an_element_polymorph_of_this_structure | 11 |
| C-CO-W | M2C | HCP_A3 | greek_or_compound_label_mapped_to_element_structure | 11 |
| CR-GE | βCr5Ge3 | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 11 |
| IN-MN | β-Mn | BCC_A2 | element_polymorph_contradicts_model | 11 |
| SB-SN | β-SnSb | BCC_A2 | greek_or_compound_label_mapped_to_element_structure | 11 |
