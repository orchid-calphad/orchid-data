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
| all | 459 | 82 | 3.36 | 1.116 | 7.14 [6.255, 8.2] | [5.545, 9.145] | 8.348 [7.0, 9.634] | 29.711 [25.448, 33.46] | 14.818 [12.201, 17.723] | 2.08 | 2.218 | 6.787 |  |
| magnetic_3d | 105 | 14 | 3.008 | 0.6 | 4.003 [2.944, 4.979] | [2.098, 5.242] | 4.089 [3.4, 4.694] | 15.96 [6.743, 60.417] | 18.05 [6.527, 26.472] | 4.51 | 1.3 | 3.786 |  |
| metal | 231 | 42 | 4.483 | 1.86 | 8.243 [6.532, 9.785] | [5.856, 11.387] | 9.054 [7.55, 11.74] | 25.883 [22.788, 31.5] | 12.411 [10.753, 14.002] | 1.51 | 2.3 | 7.916 |  |
| pblock_anion | 123 | 26 | 1.551 | 1.08 | 10.046 [7.205, 13.326] | [6.123, 15.309] | 12.458 [9.488, 17.11] | 32.357 [27.776, 47.751] | 15.873 [13.06, 18.511] | 1.58 | 3.6 | 9.379 |  |

## mp

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1077 | 181 | 2.745 | 1.987 | 8.473 [7.53, 9.424] | [6.767, 10.748] | 10.614 [9.832, 11.692] | 31.126 [29.095, 32.733] | 13.986 [12.987, 15.069] | 1.65 | 2.0 | 8.234 |  |
| above_hull|magnetic_3d | 32 | 12 | 7.39 | 5.343 | 6.038 [3.393, 8.501] | [1.754, 8.765] | 7.942 [5.62, 11.887] | 22.852 [12.847, 31.424] | 10.609 [6.972, 14.085] | 1.76 | 1.05 | 5.946 |  |
| above_hull|metal | 113 | 40 | 8.227 | 6.318 | 7.283 [5.495, 8.725] | [4.552, 9.626] | 10.256 [7.809, 12.523] | 33.091 [21.551, 39.009] | 13.865 [11.25, 16.333] | 1.9 | 2.0 | 7.003 |  |
| above_hull|pblock_anion | 67 | 22 | 7.673 | 10.022 | 14.16 [12.589, 19.302] | [8.606, 23.683] | 19.381 [16.169, 23.127] | 31.721 [25.361, 44.709] | 17.984 [15.117, 20.757] | 1.27 | 2.9 | 13.86 |  |
| chem:magnetic_3d | 169 | 32 | 1.215 | 1.7 | 4.99 [3.747, 5.931] | [3.486, 7.084] | 5.637 [4.73, 7.017] | 14.396 [12.393, 20.304] | 7.477 [6.183, 8.824] | 1.5 | 1.5 | 4.759 |  |
| chem:metal | 408 | 77 | 7.313 | 5.482 | 8.146 [6.987, 9.08] | [6.061, 9.808] | 10.11 [9.018, 11.524] | 31.489 [25.752, 36.087] | 14.158 [12.482, 15.93] | 1.74 | 2.0 | 7.897 |  |
| chem:pblock_anion | 500 | 72 | -0.465 | 0.135 | 11.216 [9.04, 12.832] | [7.177, 16.619] | 13.93 [12.022, 15.339] | 32.718 [29.523, 35.544] | 15.456 [14.093, 17.007] | 1.38 | 2.08 | 11.021 |  |
| match:above_hull | 212 | 74 | 7.926 | 5.905 | 8.518 [7.139, 10.064] | [6.165, 11.164] | 13.166 [11.354, 15.364] | 31.473 [25.894, 37.402] | 14.889 [13.125, 16.718] | 1.75 | 2.0 | 8.28 |  |
| match:on_hull_single | 405 | 117 | 4.573 | 2.889 | 7.268 [6.371, 8.588] | [5.928, 9.866] | 9.045 [7.625, 10.728] | 28.426 [25.134, 31.489] | 12.311 [10.921, 13.683] | 1.69 | 2.0 | 6.987 |  |
| match:polymorph_ambiguous | 460 | 110 | -1.251 | -0.049 | 8.813 [7.482, 10.931] | [6.313, 13.168] | 10.895 [9.882, 12.804] | 31.568 [29.269, 36.094] | 14.913 [13.121, 16.957] | 1.69 | 2.0 | 8.583 |  |
| on_hull_single|magnetic_3d | 72 | 24 | 1.216 | 0.946 | 4.97 [3.801, 6.927] | [3.447, 7.454] | 5.538 [4.235, 6.494] | 12.141 [8.205, 14.396] | 5.814 [4.631, 6.963] | 1.17 | 2.0 | 4.55 |  |
| on_hull_single|metal | 217 | 62 | 6.319 | 4.989 | 9.157 [7.628, 10.399] | [6.529, 11.075] | 10.247 [9.018, 11.826] | 28.943 [25.47, 31.573] | 13.142 [11.256, 15.156] | 1.44 | 2.0 | 8.936 |  |
| on_hull_single|pblock_anion | 116 | 31 | 3.391 | 1.729 | 6.499 [4.581, 10.84] | [3.904, 15.914] | 11.105 [6.185, 14.023] | 30.104 [24.078, 36.588] | 13.604 [11.269, 15.596] | 2.09 | 2.2 | 6.115 |  |
| polymorph_ambiguous|magnetic_3d | 65 | 21 | -1.825 | 0.093 | 5.017 [3.25, 6.743] | [2.446, 10.664] | 5.053 [3.662, 7.974] | 18.804 [11.012, 20.314] | 7.247 [5.556, 8.913] | 1.44 | 1.6 | 4.755 |  |
| polymorph_ambiguous|metal | 78 | 37 | 8.755 | 4.828 | 5.989 [4.322, 9.604] | [3.615, 10.806] | 8.625 [6.315, 12.464] | 37.14 [20.638, 59.857] | 17.018 [11.153, 22.857] | 2.84 | 2.0 | 5.645 |  |
| polymorph_ambiguous|pblock_anion | 317 | 52 | -3.596 | -2.102 | 10.934 [9.133, 13.228] | [6.708, 17.018] | 13.45 [10.935, 14.882] | 32.949 [30.305, 36.189] | 15.515 [13.742, 17.624] | 1.42 | 2.0 | 10.75 |  |

## oqmd

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1114 | 188 | 3.899 | 1.986 | 7.51 [6.68, 8.139] | [6.369, 8.812] | 8.647 [8.09, 9.561] | 26.005 [24.144, 28.734] | 12.41 [11.44, 13.406] | 1.65 | 2.0 | 7.239 |  |
| above_hull|magnetic_3d | 60 | 19 | 2.435 | 2.54 | 7.506 [4.285, 10.206] | [2.634, 17.227] | 10.813 [6.971, 15.531] | 25.597 [17.117, 25.928] | 11.704 [9.38, 13.594] | 1.56 | 1.3 | 7.393 |  |
| above_hull|metal | 102 | 39 | 7.232 | 4.86 | 6.867 [5.083, 8.418] | [4.615, 9.645] | 9.976 [7.704, 12.241] | 29.835 [17.379, 42.489] | 14.056 [10.813, 17.206] | 2.05 | 2.2 | 6.505 |  |
| above_hull|pblock_anion | 72 | 27 | 9.675 | 9.593 | 13.707 [8.807, 15.606] | [5.81, 15.507] | 13.994 [11.242, 19.281] | 29.156 [23.394, 33.759] | 14.827 [12.41, 17.153] | 1.08 | 2.3 | 13.513 |  |
| chem:magnetic_3d | 189 | 34 | 0.692 | 1.013 | 5.317 [4.548, 6.595] | [3.92, 7.624] | 5.931 [5.39, 6.503] | 19.158 [15.54, 23.04] | 8.176 [6.979, 9.275] | 1.54 | 1.6 | 5.071 |  |
| chem:metal | 416 | 80 | 5.366 | 3.039 | 7.238 [6.23, 8.384] | [5.357, 9.388] | 8.929 [8.095, 10.239] | 27.939 [22.423, 35.262] | 12.689 [11.082, 14.349] | 1.75 | 2.0 | 6.956 |  |
| chem:pblock_anion | 509 | 74 | 3.891 | 1.547 | 8.593 [7.637, 10.012] | [6.683, 11.532] | 10.292 [8.887, 11.071] | 28.669 [25.031, 32.034] | 13.441 [11.993, 15.009] | 1.56 | 2.09 | 8.335 |  |
| match:above_hull | 234 | 85 | 6.753 | 4.804 | 8.079 [6.781, 9.678] | [5.763, 10.951] | 11.81 [9.954, 13.617] | 27.041 [24.897, 33.759] | 13.744 [12.093, 15.51] | 1.7 | 2.0 | 7.828 |  |
| match:on_hull_single | 79 | 39 | 4.731 | 3.045 | 5.695 [3.509, 9.321] | [3.164, 10.738] | 7.234 [5.307, 13.967] | 24.115 [17.785, 29.229] | 11.033 [8.473, 13.326] | 1.94 | 2.2 | 5.253 |  |
| match:polymorph_ambiguous | 801 | 171 | 2.983 | 1.077 | 7.413 [6.775, 7.842] | [6.191, 8.763] | 8.115 [7.305, 8.761] | 25.974 [22.528, 29.387] | 12.125 [10.843, 13.264] | 1.64 | 2.0 | 7.138 |  |
| on_hull_single|magnetic_3d | 17 | 8 | 0.946 | 0.998 | 3.035 [1.179, 6.457] | [0.786, 6.454] | 4.192 [2.515, 5.407] | 5.703 [4.927, 5.934] | 3.571 [2.702, 4.325] | 1.18 | 3.0 | 0.46 | < 30: falls back |
| on_hull_single|metal | 36 | 21 | 5.141 | 5.239 | 9.072 [5.642, 12.046] | [4.949, 12.257] | 11.358 [6.963, 14.24] | 24.452 [15.096, 37.117] | 12.342 [8.548, 15.753] | 1.36 | 2.0 | 8.849 |  |
| on_hull_single|pblock_anion | 26 | 10 | 6.639 | 2.561 | 3.317 [1.416, 13.62] | [1.717, 16.98] | 13.671 [3.393, 19.488] | 24.189 [18.195, 28.734] | 12.272 [8.418, 15.684] | 3.7 | 2.1 | 2.568 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 112 | 31 | -0.28 | -0.222 | 5.128 [4.026, 6.36] | [3.572, 6.965] | 5.432 [4.188, 6.128] | 14.031 [8.27, 19.052] | 6.124 [4.973, 7.208] | 1.19 | 1.9 | 4.763 |  |
| polymorph_ambiguous|metal | 278 | 74 | 4.711 | 1.898 | 7.013 [5.396, 8.165] | [4.922, 9.505] | 8.417 [7.306, 9.906] | 26.851 [19.88, 31.181] | 12.195 [10.164, 14.341] | 1.74 | 2.0 | 6.722 |  |
| polymorph_ambiguous|pblock_anion | 411 | 66 | 2.704 | 0.741 | 8.067 [7.456, 9.206] | [6.302, 11.127] | 9.266 [7.797, 10.478] | 28.873 [24.473, 34.329] | 13.255 [11.423, 15.107] | 1.64 | 2.09 | 7.792 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 495d0b98db0fa867a5b92951216d553a6f22d8352e13a17a52769da5756ad044.
