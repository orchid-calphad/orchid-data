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
| all | 458 | 82 | 3.383 | 1.136 | 7.19 [6.175, 8.285] | [5.526, 9.251] | 8.36 [7.0, 9.653] | 29.711 [25.234, 33.601] | 14.834 [12.122, 17.941] | 2.06 | 2.3 | 6.812 |  |
| magnetic_3d | 105 | 14 | 3.088 | 0.66 | 3.856 [2.757, 4.871] | [1.99, 5.23] | 4.089 [3.4, 4.694] | 15.96 [6.743, 60.417] | 18.052 [6.546, 26.469] | 4.68 | 1.3 | 3.63 |  |
| metal | 230 | 42 | 4.497 | 1.995 | 8.395 [6.672, 9.877] | [5.889, 11.431] | 9.161 [7.59, 11.553] | 25.905 [22.873, 31.57] | 12.438 [10.813, 14.107] | 1.48 | 2.3 | 8.074 |  |
| pblock_anion | 123 | 26 | 1.551 | 1.08 | 10.046 [7.205, 13.326] | [6.123, 15.309] | 12.458 [9.488, 17.11] | 32.357 [27.776, 47.751] | 15.873 [13.06, 18.511] | 1.58 | 3.6 | 9.379 |  |

## mp

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1072 | 180 | 2.749 | 1.97 | 8.553 [7.574, 9.45] | [6.745, 10.813] | 10.653 [9.862, 11.765] | 31.148 [29.12, 32.813] | 14.012 [13.027, 14.959] | 1.64 | 2.0 | 8.316 |  |
| above_hull|magnetic_3d | 32 | 12 | 7.39 | 5.343 | 6.038 [3.393, 8.501] | [1.754, 8.765] | 7.942 [5.62, 11.887] | 22.852 [12.847, 31.424] | 10.609 [6.972, 14.085] | 1.76 | 1.05 | 5.946 |  |
| above_hull|metal | 113 | 40 | 8.227 | 6.318 | 7.283 [5.495, 8.725] | [4.552, 9.626] | 10.256 [7.809, 12.523] | 33.091 [21.551, 39.009] | 13.865 [11.25, 16.333] | 1.9 | 2.0 | 7.003 |  |
| above_hull|pblock_anion | 67 | 22 | 7.673 | 10.022 | 14.16 [12.589, 19.302] | [8.606, 23.683] | 19.381 [16.169, 23.127] | 31.721 [25.361, 44.709] | 17.984 [15.117, 20.757] | 1.27 | 2.9 | 13.86 |  |
| chem:magnetic_3d | 166 | 32 | 1.259 | 1.701 | 5.002 [3.877, 5.984] | [3.475, 7.044] | 5.634 [4.727, 6.996] | 14.396 [12.801, 20.304] | 7.517 [6.287, 8.737] | 1.5 | 1.5 | 4.772 |  |
| chem:metal | 407 | 77 | 7.325 | 5.487 | 8.245 [6.993, 9.06] | [6.083, 9.817] | 10.132 [9.027, 11.625] | 31.489 [25.772, 36.087] | 14.175 [12.505, 16.018] | 1.72 | 2.0 | 7.999 |  |
| chem:pblock_anion | 499 | 71 | -0.488 | 0.115 | 11.186 [9.061, 13.009] | [7.009, 16.874] | 13.94 [12.078, 15.304] | 32.723 [29.537, 35.639] | 15.463 [14.125, 16.953] | 1.38 | 2.085 | 10.99 |  |
| match:above_hull | 212 | 74 | 7.926 | 5.905 | 8.518 [7.139, 10.064] | [6.165, 11.164] | 13.166 [11.354, 15.364] | 31.473 [25.894, 37.402] | 14.889 [13.125, 16.718] | 1.75 | 2.0 | 8.28 |  |
| match:on_hull_single | 400 | 116 | 4.605 | 2.896 | 7.351 [6.369, 8.565] | [5.943, 9.982] | 9.073 [7.675, 10.837] | 28.539 [25.465, 31.489] | 12.367 [11.154, 13.647] | 1.68 | 2.0 | 7.074 |  |
| match:polymorph_ambiguous | 460 | 110 | -1.251 | -0.049 | 8.813 [7.482, 10.931] | [6.313, 13.168] | 10.895 [9.882, 12.804] | 31.568 [29.269, 36.094] | 14.913 [13.121, 16.957] | 1.69 | 2.0 | 8.583 |  |
| on_hull_single|magnetic_3d | 69 | 24 | 1.321 | 0.963 | 5.155 [3.752, 7.062] | [3.447, 7.579] | 5.534 [4.235, 6.48] | 12.591 [8.237, 14.396] | 5.854 [4.626, 7.03] | 1.14 | 1.8 | 4.831 |  |
| on_hull_single|metal | 216 | 62 | 6.336 | 5.028 | 9.231 [7.636, 10.405] | [6.66, 11.079] | 10.322 [9.099, 11.927] | 28.966 [25.471, 31.595] | 13.171 [11.225, 15.261] | 1.43 | 2.0 | 9.012 |  |
| on_hull_single|pblock_anion | 115 | 30 | 3.322 | 1.623 | 6.523 [4.566, 11.127] | [3.732, 16.257] | 10.999 [6.185, 14.218] | 30.229 [24.106, 36.588] | 13.623 [11.419, 15.958] | 2.09 | 2.25 | 6.123 |  |
| polymorph_ambiguous|magnetic_3d | 65 | 21 | -1.825 | 0.093 | 5.017 [3.25, 6.743] | [2.446, 10.664] | 5.053 [3.662, 7.974] | 18.804 [11.012, 20.314] | 7.247 [5.556, 8.913] | 1.44 | 1.6 | 4.755 |  |
| polymorph_ambiguous|metal | 78 | 37 | 8.755 | 4.828 | 5.989 [4.322, 9.604] | [3.615, 10.806] | 8.625 [6.315, 12.464] | 37.14 [20.638, 59.857] | 17.018 [11.153, 22.857] | 2.84 | 2.0 | 5.645 |  |
| polymorph_ambiguous|pblock_anion | 317 | 52 | -3.596 | -2.102 | 10.934 [9.133, 13.228] | [6.708, 17.018] | 13.45 [10.935, 14.882] | 32.949 [30.305, 36.189] | 15.515 [13.742, 17.624] | 1.42 | 2.0 | 10.75 |  |

## oqmd

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1109 | 187 | 3.9 | 1.98 | 7.503 [6.704, 8.235] | [6.341, 8.852] | 8.681 [8.115, 9.69] | 26.006 [24.217, 28.999] | 12.42 [11.436, 13.426] | 1.66 | 2.0 | 7.232 |  |
| above_hull|magnetic_3d | 60 | 19 | 2.435 | 2.54 | 7.506 [4.285, 10.206] | [2.634, 17.227] | 10.813 [6.971, 15.531] | 25.597 [17.117, 25.928] | 11.704 [9.38, 13.594] | 1.56 | 1.3 | 7.393 |  |
| above_hull|metal | 102 | 39 | 7.232 | 4.86 | 6.867 [5.083, 8.418] | [4.615, 9.645] | 9.976 [7.704, 12.241] | 29.835 [17.379, 42.489] | 14.056 [10.813, 17.206] | 2.05 | 2.2 | 6.505 |  |
| above_hull|pblock_anion | 72 | 27 | 9.675 | 9.593 | 13.707 [8.807, 15.606] | [5.81, 15.507] | 13.994 [11.242, 19.281] | 29.156 [23.394, 33.759] | 14.827 [12.41, 17.153] | 1.08 | 2.3 | 13.513 |  |
| chem:magnetic_3d | 186 | 34 | 0.728 | 1.069 | 5.4 [4.453, 6.711] | [3.966, 7.522] | 5.93 [5.122, 6.495] | 19.185 [15.54, 23.047] | 8.219 [7.041, 9.292] | 1.52 | 1.55 | 5.173 |  |
| chem:metal | 415 | 80 | 5.373 | 3.049 | 7.331 [6.17, 8.353] | [5.38, 9.471] | 8.995 [8.115, 10.229] | 27.978 [21.72, 35.262] | 12.704 [10.962, 14.353] | 1.73 | 2.0 | 7.053 |  |
| chem:pblock_anion | 508 | 73 | 3.858 | 1.504 | 8.561 [7.632, 10.038] | [6.782, 11.522] | 10.274 [8.83, 11.136] | 28.677 [24.99, 32.749] | 13.424 [11.976, 14.904] | 1.57 | 2.091 | 8.302 |  |
| match:above_hull | 234 | 85 | 6.753 | 4.804 | 8.079 [6.781, 9.678] | [5.763, 10.951] | 11.81 [9.954, 13.617] | 27.041 [24.897, 33.759] | 13.744 [12.093, 15.51] | 1.7 | 2.0 | 7.828 |  |
| match:on_hull_single | 78 | 39 | 4.745 | 2.872 | 5.758 [3.66, 9.392] | [3.113, 10.776] | 7.318 [5.256, 13.792] | 24.121 [18.087, 29.229] | 11.096 [8.777, 13.268] | 1.93 | 2.15 | 5.342 |  |
| match:polymorph_ambiguous | 797 | 170 | 2.979 | 1.077 | 7.413 [6.731, 7.82] | [6.225, 8.659] | 8.147 [7.237, 8.773] | 25.981 [22.528, 29.217] | 12.13 [10.86, 13.295] | 1.64 | 2.0 | 7.138 |  |
| on_hull_single|magnetic_3d | 16 | 8 | 0.777 | 0.879 | 3.211 [1.22, 6.67] | [0.698, 7.004] | 4.377 [2.515, 5.455] | 5.717 [4.811, 5.934] | 3.567 [2.594, 4.32] | 1.11 | 3.0 | 1.145 | < 30: falls back |
| on_hull_single|metal | 36 | 21 | 5.141 | 5.239 | 9.072 [5.642, 12.046] | [4.949, 12.257] | 11.358 [6.963, 14.24] | 24.452 [15.096, 37.117] | 12.342 [8.548, 15.753] | 1.36 | 2.0 | 8.849 |  |
| on_hull_single|pblock_anion | 26 | 10 | 6.639 | 2.561 | 3.317 [1.416, 13.62] | [1.717, 16.98] | 13.671 [3.393, 19.488] | 24.189 [18.195, 28.734] | 12.272 [8.418, 15.684] | 3.7 | 2.1 | 2.568 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 110 | 31 | -0.21 | 0.083 | 4.829 [3.954, 6.284] | [3.598, 6.915] | 5.432 [4.174, 5.982] | 14.2 [8.27, 19.052] | 6.136 [4.999, 7.33] | 1.27 | 1.9 | 4.44 |  |
| polymorph_ambiguous|metal | 277 | 74 | 4.719 | 1.885 | 7.082 [5.48, 8.167] | [4.94, 9.552] | 8.42 [7.338, 9.883] | 26.904 [19.939, 31.166] | 12.216 [10.136, 14.438] | 1.72 | 2.0 | 6.794 |  |
| polymorph_ambiguous|pblock_anion | 410 | 65 | 2.66 | 0.725 | 8.062 [7.469, 9.158] | [6.346, 10.945] | 9.239 [7.711, 10.477] | 28.903 [24.674, 34.812] | 13.233 [11.626, 15.396] | 1.64 | 2.09 | 7.786 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 8457a05b94243c7b435a508af09b45cb062dfbad5ece0473a4d17d4468fdcf01.
