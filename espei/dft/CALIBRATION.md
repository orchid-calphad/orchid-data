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
| all | 458 | 82 | 3.338 | 1.123 | 7.151 [6.092, 8.214] | [5.485, 9.133] | 8.323 [7.0, 9.633] | 29.711 [25.269, 33.464] | 14.811 [12.119, 17.887] | 2.07 | 2.3 | 6.771 |  |
| magnetic_3d | 105 | 14 | 3.083 | 0.611 | 3.929 [2.742, 4.87] | [2.002, 5.23] | 4.089 [3.4, 4.694] | 15.96 [6.743, 60.417] | 18.053 [6.546, 26.469] | 4.59 | 1.3 | 3.708 |  |
| metal | 230 | 42 | 4.497 | 1.995 | 8.395 [6.672, 9.877] | [5.889, 11.431] | 9.161 [7.59, 11.553] | 25.905 [22.873, 31.57] | 12.438 [10.813, 14.107] | 1.48 | 2.3 | 8.074 |  |
| pblock_anion | 123 | 26 | 1.389 | 1.078 | 9.966 [6.939, 13.23] | [6.006, 14.797] | 11.741 [9.21, 16.463] | 32.357 [27.65, 47.393] | 15.791 [12.958, 18.391] | 1.58 | 3.6 | 9.293 |  |

## mp

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1070 | 180 | 2.733 | 1.97 | 8.553 [7.557, 9.443] | [6.784, 10.813] | 10.629 [9.854, 11.76] | 31.156 [29.076, 32.813] | 14.01 [13.0, 15.05] | 1.64 | 2.0 | 8.316 |  |
| above_hull|magnetic_3d | 32 | 12 | 7.39 | 5.343 | 6.038 [3.393, 8.501] | [1.754, 8.765] | 7.942 [5.62, 11.887] | 22.852 [12.847, 31.424] | 10.609 [6.972, 14.085] | 1.76 | 1.05 | 5.946 |  |
| above_hull|metal | 113 | 40 | 8.227 | 6.318 | 7.283 [5.495, 8.725] | [4.552, 9.626] | 10.256 [7.809, 12.523] | 33.091 [21.551, 39.009] | 13.865 [11.25, 16.333] | 1.9 | 2.0 | 7.003 |  |
| above_hull|pblock_anion | 66 | 22 | 7.462 | 7.772 | 15.057 [12.336, 18.885] | [8.335, 23.329] | 18.579 [15.971, 23.434] | 31.903 [25.386, 44.709] | 17.924 [14.921, 21.1] | 1.19 | 2.5 | 14.848 |  |
| chem:magnetic_3d | 165 | 32 | 1.261 | 1.702 | 5.016 [3.985, 5.972] | [3.497, 7.044] | 5.657 [4.932, 7.017] | 14.396 [12.804, 20.304] | 7.539 [6.311, 8.738] | 1.5 | 1.5 | 4.786 |  |
| chem:metal | 407 | 77 | 7.325 | 5.487 | 8.245 [6.993, 9.06] | [6.083, 9.817] | 10.132 [9.027, 11.625] | 31.489 [25.772, 36.087] | 14.175 [12.505, 16.018] | 1.72 | 2.0 | 7.999 |  |
| chem:pblock_anion | 498 | 71 | -0.533 | 0.083 | 11.131 [8.871, 13.008] | [6.934, 16.805] | 13.919 [11.995, 15.235] | 32.728 [29.565, 35.589] | 15.448 [14.076, 17.026] | 1.39 | 2.08 | 10.935 |  |
| match:above_hull | 211 | 74 | 7.861 | 5.793 | 8.675 [7.091, 9.944] | [6.066, 11.114] | 13.121 [11.178, 15.179] | 31.479 [25.717, 37.218] | 14.85 [12.93, 16.5] | 1.71 | 2.0 | 8.441 |  |
| match:on_hull_single | 399 | 116 | 4.614 | 2.902 | 7.434 [6.384, 8.598] | [5.979, 10.033] | 9.096 [7.625, 10.735] | 28.556 [25.178, 31.489] | 12.382 [10.974, 13.732] | 1.67 | 2.0 | 7.16 |  |
| match:polymorph_ambiguous | 460 | 110 | -1.251 | -0.049 | 8.813 [7.482, 10.931] | [6.313, 13.168] | 10.895 [9.882, 12.804] | 31.568 [29.269, 36.094] | 14.913 [13.121, 16.957] | 1.69 | 2.0 | 8.583 |  |
| on_hull_single|magnetic_3d | 68 | 24 | 1.327 | 1.229 | 5.211 [3.887, 7.204] | [3.5, 7.632] | 5.56 [4.235, 6.507] | 12.741 [8.203, 14.396] | 5.895 [4.758, 7.15] | 1.13 | 1.65 | 4.943 |  |
| on_hull_single|metal | 216 | 62 | 6.336 | 5.028 | 9.231 [7.636, 10.405] | [6.66, 11.079] | 10.322 [9.099, 11.927] | 28.966 [25.471, 31.595] | 13.171 [11.225, 15.261] | 1.43 | 2.0 | 9.012 |  |
| on_hull_single|pblock_anion | 115 | 30 | 3.322 | 1.623 | 6.523 [4.566, 11.127] | [3.732, 16.257] | 10.999 [6.185, 14.218] | 30.229 [24.106, 36.588] | 13.623 [11.419, 15.958] | 2.09 | 2.25 | 6.123 |  |
| polymorph_ambiguous|magnetic_3d | 65 | 21 | -1.825 | 0.093 | 5.017 [3.25, 6.743] | [2.446, 10.664] | 5.053 [3.662, 7.974] | 18.804 [11.012, 20.314] | 7.247 [5.556, 8.913] | 1.44 | 1.6 | 4.755 |  |
| polymorph_ambiguous|metal | 78 | 37 | 8.755 | 4.828 | 5.989 [4.322, 9.604] | [3.615, 10.806] | 8.625 [6.315, 12.464] | 37.14 [20.638, 59.857] | 17.018 [11.153, 22.857] | 2.84 | 2.0 | 5.645 |  |
| polymorph_ambiguous|pblock_anion | 317 | 52 | -3.596 | -2.102 | 10.934 [9.133, 13.228] | [6.708, 17.018] | 13.45 [10.935, 14.882] | 32.949 [30.305, 36.189] | 15.515 [13.742, 17.624] | 1.42 | 2.0 | 10.75 |  |

## oqmd

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1107 | 187 | 3.89 | 1.98 | 7.503 [6.7, 8.248] | [6.328, 8.844] | 8.653 [8.152, 9.679] | 26.006 [24.104, 29.081] | 12.419 [11.416, 13.477] | 1.66 | 2.0 | 7.232 |  |
| above_hull|magnetic_3d | 60 | 19 | 2.435 | 2.54 | 7.506 [4.285, 10.206] | [2.634, 17.227] | 10.813 [6.971, 15.531] | 25.597 [17.117, 25.928] | 11.704 [9.38, 13.594] | 1.56 | 1.3 | 7.393 |  |
| above_hull|metal | 102 | 39 | 7.232 | 4.86 | 6.867 [5.083, 8.418] | [4.615, 9.645] | 9.976 [7.704, 12.241] | 29.835 [17.379, 42.489] | 14.056 [10.813, 17.206] | 2.05 | 2.2 | 6.505 |  |
| above_hull|pblock_anion | 71 | 27 | 9.553 | 9.507 | 13.678 [8.812, 15.677] | [5.723, 15.58] | 13.677 [11.242, 19.384] | 29.408 [23.29, 33.759] | 14.772 [12.36, 17.0] | 1.08 | 2.0 | 13.531 |  |
| chem:magnetic_3d | 185 | 34 | 0.729 | 1.126 | 5.463 [4.618, 6.703] | [3.957, 7.533] | 5.934 [5.407, 6.602] | 19.194 [15.538, 23.048] | 8.241 [6.953, 9.347] | 1.51 | 1.5 | 5.253 |  |
| chem:metal | 415 | 80 | 5.373 | 3.049 | 7.331 [6.17, 8.353] | [5.38, 9.471] | 8.995 [8.115, 10.229] | 27.978 [21.72, 35.262] | 12.704 [10.962, 14.353] | 1.73 | 2.0 | 7.053 |  |
| chem:pblock_anion | 507 | 73 | 3.829 | 1.461 | 8.544 [7.572, 9.947] | [6.714, 11.489] | 10.235 [8.896, 11.071] | 28.685 [25.194, 32.02] | 13.412 [12.005, 15.043] | 1.57 | 2.09 | 8.284 |  |
| match:above_hull | 233 | 85 | 6.704 | 4.792 | 8.022 [6.789, 9.61] | [5.709, 10.908] | 11.764 [9.678, 13.401] | 27.062 [24.39, 33.759] | 13.721 [11.932, 15.36] | 1.71 | 2.0 | 7.769 |  |
| match:on_hull_single | 77 | 39 | 4.801 | 3.045 | 5.821 [3.539, 9.321] | [3.219, 11.145] | 7.401 [5.307, 13.872] | 24.127 [17.676, 29.229] | 11.167 [8.743, 13.291] | 1.92 | 2.1 | 5.429 |  |
| match:polymorph_ambiguous | 797 | 170 | 2.979 | 1.077 | 7.413 [6.731, 7.82] | [6.225, 8.659] | 8.147 [7.237, 8.773] | 25.981 [22.528, 29.217] | 12.13 [10.86, 13.295] | 1.64 | 2.0 | 7.138 |  |
| on_hull_single|magnetic_3d | 15 | 8 | 0.799 | 0.998 | 3.035 [0.815, 7.05] | [0.786, 7.065] | 4.55 [2.515, 5.407] | 5.732 [4.99, 5.934] | 3.682 [2.777, 4.435] | 1.21 | 2.6 | 1.566 | < 30: falls back |
| on_hull_single|metal | 36 | 21 | 5.141 | 5.239 | 9.072 [5.642, 12.046] | [4.949, 12.257] | 11.358 [6.963, 14.24] | 24.452 [15.096, 37.117] | 12.342 [8.548, 15.753] | 1.36 | 2.0 | 8.849 |  |
| on_hull_single|pblock_anion | 26 | 10 | 6.639 | 2.561 | 3.317 [1.416, 13.62] | [1.717, 16.98] | 13.671 [3.393, 19.488] | 24.189 [18.195, 28.734] | 12.272 [8.418, 15.684] | 3.7 | 2.1 | 2.568 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 110 | 31 | -0.21 | 0.083 | 4.829 [3.954, 6.284] | [3.598, 6.915] | 5.432 [4.174, 5.982] | 14.2 [8.27, 19.052] | 6.136 [4.999, 7.33] | 1.27 | 1.9 | 4.44 |  |
| polymorph_ambiguous|metal | 277 | 74 | 4.719 | 1.885 | 7.082 [5.48, 8.167] | [4.94, 9.552] | 8.42 [7.338, 9.883] | 26.904 [19.939, 31.166] | 12.216 [10.136, 14.438] | 1.72 | 2.0 | 6.794 |  |
| polymorph_ambiguous|pblock_anion | 410 | 65 | 2.66 | 0.725 | 8.062 [7.469, 9.158] | [6.346, 10.945] | 9.239 [7.711, 10.477] | 28.903 [24.674, 34.812] | 13.233 [11.626, 15.396] | 1.64 | 2.09 | 7.786 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 06ad9a91e0aabb50d71685b26d60d3709b25cebbb9956c4da14d4ef3c4f4f8db.
