# DFT formation-enthalpy uncertainty: calibration

Calibrated from ORCHID's own DFT-vs-experiment pairs (`literature/dft_parity.json`, default subset: experimental, accepted, signed, not magnitude-suspect; residual = DFT - experiment, kJ/mol-atom). Materials Project and OQMD are calibrated separately (different energy references). Literature DFT: each accepted literature DFT HM_FORM value (kJ/mol-atom, binary) paired with the median experimental value of the same compound (same reduced composition) in that subset.

## Method

- bias: mean and median residual (**recorded, not applied** to any value);
- robust sigma = 1.4826 x MAD (median absolute deviation about the median); 68 / 95 % quantiles of |residual|; RMSE;
- 95% confidence intervals: 1000 bootstrap resamples (fixed seeds), percentile intervals, two ways: resampling pairs (`ci95`) and resampling chemical systems with all their pairs (`ci95_cluster_system`, audit A4 E8; pairs cluster by compound and system, so the system-cluster interval is the one to quote);
- strata: match quality (`on_hull_single` DFT entry on the hull and the only entry at its composition; `polymorph_ambiguous` on the hull, several entries (polymorphs) at the composition; `above_hull` lowest DFT entry at the composition lies more than 1 meV/atom (0.0965 kJ/mol-atom, the numerical precision of the DFT energies) above the hull) x chemistry (`metal` all-metal intermetallic (none of the elements below); `pblock_anion` contains a p-block / anion element (H, B, C, N, O, F, Si, P, S, Se, Te, As, Sb, halogens); `magnetic_3d` contains Cr, Mn, Fe, Co or Ni (and no p-block / anion element)); chemistry precedence: p-block / anion, then magnetic 3d, then all-metal; single-factor strata are listed too;
- experimental-error-deconvolved sigma_DFT = sqrt(sigma_robust^2 - sigma_exp^2), sigma_exp = median printed experimental uncertainty of the matched records (reported, not used);
- weights use the plain robust sigma (conservative), **leave-system-out**: for each system the sigma of its stratum is recomputed without that system's pairs; a stratum with fewer than 30 pairs falls back to the source-level sigma (also leave-system-out);
- exported MP / OQMD values are on-hull vertices: stratum `on_hull_single` when the vertex is the only entry at its composition, else `polymorph_ambiguous`; literature DFT values use the chemistry stratum;
- ESPEI weight = 500 J/mol / sigma_DFT (J/mol-atom). 500 J/mol is ESPEI's reference sigma for experimental HM data; the ratio only makes ESPEI use the calibrated DFT sigma.

## Caveats

- Heavy tails: RMSE exceeds the robust sigma (column `RMSE/sigma`) and the 95 % quantile of |residual| is several robust sigmas; a Gaussian likelihood with the robust sigma treats the tail compounds as far less likely than they are, so a few outliers can pull a fit hard. Consider a Student-t or a wider sigma if your fit is sensitive to a few compounds.
- The point estimates treat pairs as independent; several experimental records of one compound and correlated errors within a chemistry are reflected only in the system-cluster confidence interval.
- The calibration is against literature experiments (machine-extracted, Version 1) and inherits their errors; sigma_deconvolved shows how much of the spread the printed experimental uncertainty explains.
- 0 K DFT energies are used as 298.15 K enthalpies.

## literature

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 477 | 82 | 3.992 | 1.131 | 7.162 [6.195, 8.328] | [5.435, 9.474] | 8.697 [7.425, 10.193] | 31.297 [26.868, 37.172] | 16.312 [13.495, 19.314] | 2.28 | 2.218 | 6.81 |  |
| magnetic_3d | 112 | 14 | 5.655 | 0.636 | 4.166 [3.15, 5.166] | [2.097, 5.782] | 4.304 [3.674, 4.763] | 50.653 [12.648, 102.255] | 23.181 [13.53, 31.634] | 5.56 | 1.3 | 3.958 |  |
| metal | 239 | 42 | 4.394 | 1.63 | 7.962 [6.671, 9.913] | [5.74, 11.489] | 9.573 [7.722, 11.147] | 25.709 [22.753, 30.94] | 12.344 [10.832, 13.907] | 1.55 | 2.3 | 7.623 |  |
| pblock_anion | 126 | 26 | 1.753 | 1.212 | 10.005 [7.132, 12.643] | [5.952, 15.11] | 11.75 [9.496, 14.65] | 32.254 [27.579, 46.139] | 15.515 [12.722, 18.004] | 1.55 | 3.6 | 9.335 |  |

## mp

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1093 | 180 | 2.631 | 1.936 | 8.482 [7.42, 9.443] | [6.646, 10.748] | 10.481 [9.74, 11.644] | 31.143 [28.651, 32.813] | 14.014 [12.988, 15.131] | 1.65 | 2.0 | 8.243 |  |
| above_hull|magnetic_3d | 34 | 12 | 7.24 | 5.343 | 5.401 [3.011, 7.992] | [1.876, 8.765] | 7.776 [5.31, 12.321] | 21.675 [12.262, 31.424] | 10.361 [6.762, 13.874] | 1.92 | 1.05 | 5.298 |  |
| above_hull|metal | 111 | 39 | 8.268 | 6.318 | 7.312 [5.626, 8.988] | [4.817, 9.72] | 10.398 [7.839, 12.513] | 33.48 [21.503, 39.009] | 13.965 [11.115, 16.549] | 1.91 | 2.0 | 7.033 |  |
| above_hull|pblock_anion | 67 | 22 | 7.673 | 10.022 | 14.16 [12.589, 19.302] | [8.606, 23.683] | 19.381 [16.169, 23.127] | 31.721 [25.361, 44.709] | 17.984 [15.117, 20.757] | 1.27 | 2.9 | 13.86 |  |
| chem:magnetic_3d | 183 | 32 | 1.206 | 1.702 | 4.848 [3.819, 5.741] | [3.494, 6.854] | 5.49 [4.641, 6.382] | 14.372 [12.692, 20.304] | 7.257 [6.042, 8.513] | 1.5 | 1.5 | 4.61 |  |
| chem:metal | 405 | 76 | 7.347 | 5.487 | 8.245 [7.017, 9.044] | [6.073, 9.866] | 10.163 [9.025, 11.625] | 31.489 [25.892, 36.094] | 14.203 [12.453, 16.046] | 1.72 | 2.0 | 7.999 |  |
| chem:pblock_anion | 505 | 72 | -0.634 | 0.05 | 11.09 [9.198, 13.058] | [7.231, 16.587] | 13.91 [12.055, 15.413] | 32.793 [29.924, 35.589] | 15.626 [14.205, 17.153] | 1.41 | 2.04 | 10.901 |  |
| match:above_hull | 212 | 73 | 7.915 | 5.78 | 8.701 [7.026, 9.994] | [5.878, 11.471] | 13.166 [11.369, 15.234] | 31.473 [25.681, 37.039] | 14.884 [12.985, 16.565] | 1.71 | 2.0 | 8.468 |  |
| match:on_hull_single | 407 | 117 | 4.386 | 2.889 | 7.268 [6.328, 8.588] | [5.93, 10.086] | 9.135 [7.675, 10.791] | 28.753 [25.4, 31.784] | 12.645 [11.284, 14.181] | 1.74 | 2.0 | 6.987 |  |
| match:polymorph_ambiguous | 474 | 110 | -1.239 | -0.049 | 8.254 [7.359, 10.43] | [6.203, 12.629] | 10.347 [9.716, 12.431] | 31.417 [29.334, 36.089] | 14.713 [12.927, 16.448] | 1.78 | 2.0 | 8.008 |  |
| on_hull_single|magnetic_3d | 72 | 24 | 1.216 | 0.946 | 4.97 [3.801, 6.927] | [3.447, 7.454] | 5.538 [4.235, 6.494] | 12.141 [8.205, 14.396] | 5.814 [4.631, 6.963] | 1.17 | 2.0 | 4.55 |  |
| on_hull_single|metal | 216 | 61 | 6.365 | 5.028 | 9.154 [7.57, 10.231] | [6.63, 11.35] | 10.322 [9.155, 11.806] | 28.966 [25.471, 31.595] | 13.17 [11.3, 15.196] | 1.44 | 2.0 | 8.933 |  |
| on_hull_single|pblock_anion | 119 | 32 | 2.714 | 1.6 | 6.798 [4.721, 10.879] | [4.069, 17.978] | 11.11 [6.822, 14.083] | 32.279 [24.471, 36.588] | 14.545 [11.868, 17.315] | 2.14 | 2.15 | 6.449 |  |
| polymorph_ambiguous|magnetic_3d | 77 | 21 | -1.467 | 0.093 | 5.017 [3.312, 6.406] | [2.59, 10.083] | 4.861 [3.705, 5.412] | 14.304 [9.886, 20.314] | 6.795 [5.258, 8.332] | 1.35 | 1.6 | 4.755 |  |
| polymorph_ambiguous|metal | 78 | 37 | 8.755 | 4.828 | 5.989 [4.322, 9.604] | [3.615, 10.806] | 8.625 [6.315, 12.464] | 37.14 [20.638, 59.857] | 17.018 [11.153, 22.857] | 2.84 | 2.0 | 5.645 |  |
| polymorph_ambiguous|pblock_anion | 319 | 52 | -3.628 | -2.265 | 11.176 [9.066, 12.762] | [6.708, 16.833] | 13.287 [10.895, 14.816] | 32.831 [30.034, 36.099] | 15.482 [13.579, 17.545] | 1.39 | 2.0 | 10.996 |  |

## oqmd

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1130 | 187 | 3.8 | 1.978 | 7.383 [6.592, 8.014] | [6.237, 8.768] | 8.544 [7.915, 9.487] | 26.006 [24.22, 28.977] | 12.46 [11.561, 13.405] | 1.69 | 2.0 | 7.107 |  |
| above_hull|magnetic_3d | 62 | 19 | 2.507 | 2.723 | 7.533 [3.837, 9.78] | [2.672, 16.45] | 10.616 [6.522, 15.53] | 25.457 [16.781, 25.855] | 11.545 [9.39, 13.562] | 1.53 | 1.1 | 7.452 |  |
| above_hull|metal | 100 | 38 | 7.3 | 4.86 | 6.869 [5.352, 8.768] | [4.422, 10.167] | 10.203 [8.09, 12.466] | 30.577 [17.666, 42.689] | 14.184 [10.745, 17.315] | 2.06 | 2.15 | 6.524 |  |
| above_hull|pblock_anion | 72 | 27 | 9.675 | 9.593 | 13.707 [8.807, 15.606] | [5.81, 15.507] | 13.994 [11.242, 19.281] | 29.156 [23.394, 33.759] | 14.827 [12.41, 17.153] | 1.08 | 2.3 | 13.513 |  |
| chem:magnetic_3d | 203 | 34 | 0.678 | 1.126 | 5.265 [4.472, 6.439] | [3.908, 7.418] | 5.693 [4.804, 6.34] | 18.827 [15.473, 23.04] | 7.946 [6.766, 9.036] | 1.51 | 1.55 | 5.032 |  |
| chem:metal | 413 | 79 | 5.392 | 3.049 | 7.331 [6.096, 8.395] | [5.48, 9.408] | 9.132 [8.138, 10.223] | 28.056 [22.465, 35.262] | 12.731 [11.093, 14.332] | 1.74 | 2.0 | 7.053 |  |
| chem:pblock_anion | 514 | 74 | 3.755 | 1.504 | 8.524 [7.614, 9.94] | [6.658, 11.455] | 10.279 [8.888, 11.141] | 28.888 [25.26, 32.727] | 13.643 [12.133, 15.226] | 1.6 | 2.09 | 8.264 |  |
| match:above_hull | 234 | 84 | 6.761 | 4.804 | 8.079 [6.795, 9.722] | [5.887, 10.789] | 11.81 [9.909, 13.617] | 27.041 [24.624, 32.657] | 13.745 [12.115, 15.431] | 1.7 | 2.0 | 7.828 |  |
| match:on_hull_single | 80 | 39 | 4.669 | 2.872 | 5.099 [3.452, 8.848] | [3.159, 10.687] | 7.154 [5.112, 13.671] | 24.11 [18.026, 29.229] | 10.963 [8.523, 13.277] | 2.15 | 2.2 | 4.6 |  |
| match:polymorph_ambiguous | 816 | 171 | 2.866 | 1.082 | 7.406 [6.752, 7.774] | [6.086, 8.638] | 7.931 [7.259, 8.527] | 25.982 [22.528, 29.487] | 12.208 [10.968, 13.6] | 1.65 | 2.0 | 7.131 |  |
| on_hull_single|magnetic_3d | 17 | 8 | 0.946 | 0.998 | 3.035 [1.179, 6.457] | [0.786, 6.454] | 4.192 [2.515, 5.407] | 5.703 [4.927, 5.934] | 3.571 [2.702, 4.325] | 1.18 | 3.0 | 0.46 | < 30: falls back |
| on_hull_single|metal | 36 | 21 | 5.141 | 5.239 | 9.072 [5.642, 12.046] | [4.949, 12.257] | 11.358 [6.963, 14.24] | 24.452 [15.096, 37.117] | 12.342 [8.548, 15.753] | 1.36 | 2.0 | 8.849 |  |
| on_hull_single|pblock_anion | 27 | 10 | 6.385 | 2.424 | 3.113 [1.397, 10.77] | [1.817, 16.449] | 11.608 [3.171, 18.543] | 24.183 [16.534, 28.734] | 12.042 [8.258, 15.115] | 3.87 | 2.1 | 2.298 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 124 | 31 | -0.274 | 0.083 | 4.709 [3.941, 6.129] | [3.533, 6.798] | 5.071 [4.146, 5.913] | 12.975 [8.261, 18.616] | 5.915 [4.841, 6.98] | 1.26 | 1.9 | 4.309 |  |
| polymorph_ambiguous|metal | 277 | 73 | 4.735 | 1.912 | 7.042 [5.418, 8.138] | [4.95, 9.365] | 8.42 [7.338, 9.879] | 26.904 [20.015, 31.166] | 12.217 [10.247, 14.297] | 1.73 | 2.0 | 6.752 |  |
| polymorph_ambiguous|pblock_anion | 415 | 67 | 2.556 | 0.741 | 8.067 [7.457, 9.103] | [6.316, 11.039] | 9.255 [7.71, 10.478] | 29.359 [24.769, 34.806] | 13.527 [11.827, 15.338] | 1.68 | 2.09 | 7.792 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 d41485314acb8b51cd828035082a3a839b56f4b88d8f9b8a0376635b35b4e606.
