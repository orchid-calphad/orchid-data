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
| all | 479 | 81 | 3.932 | 1.078 | 7.084 [6.114, 8.228] | [5.282, 9.754] | 8.69 [7.46, 9.702] | 31.241 [26.17, 37.058] | 16.264 [13.157, 19.503] | 2.3 | 2.218 | 6.728 |  |
| magnetic_3d | 113 | 14 | 5.813 | 0.85 | 3.884 [2.946, 4.848] | [2.133, 5.702] | 4.102 [3.608, 4.746] | 50.5 [12.7, 102.255] | 23.067 [13.058, 31.44] | 5.94 | 1.665 | 3.509 |  |
| metal | 241 | 41 | 4.19 | 1.113 | 8.472 [6.817, 10.008] | [5.715, 11.365] | 9.02 [7.815, 10.87] | 25.666 [21.878, 30.8] | 12.267 [10.62, 13.819] | 1.45 | 2.3 | 8.154 |  |
| pblock_anion | 125 | 26 | 1.735 | 1.08 | 10.185 [7.116, 13.21] | [6.115, 15.117] | 11.771 [9.496, 14.802] | 32.288 [27.665, 38.964] | 15.574 [12.957, 18.139] | 1.53 | 3.6 | 9.528 |  |

## mp

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1181 | 186 | 3.848 | 2.523 | 8.885 [7.898, 9.741] | [7.114, 11.066] | 11.09 [10.111, 11.91] | 31.424 [29.476, 33.936] | 18.077 [15.059, 21.361] | 2.03 | 2.0 | 8.657 |  |
| above_hull|magnetic_3d | 37 | 12 | 7.114 | 5.066 | 4.99 [2.885, 7.991] | [1.927, 8.755] | 7.776 [5.332, 11.714] | 19.91 [12.054, 31.424] | 10.084 [6.642, 13.387] | 2.02 | 1.05 | 4.878 |  |
| above_hull|metal | 123 | 41 | 8.382 | 6.686 | 7.812 [6.3, 9.117] | [4.665, 9.639] | 11.08 [8.728, 12.663] | 31.358 [21.551, 39.009] | 13.785 [11.34, 16.226] | 1.76 | 2.0 | 7.552 |  |
| above_hull|pblock_anion | 67 | 22 | 7.673 | 10.022 | 14.16 [12.589, 19.302] | [8.606, 23.683] | 19.381 [16.169, 23.127] | 31.721 [25.361, 44.709] | 17.984 [15.117, 20.757] | 1.27 | 2.9 | 13.86 |  |
| chem:magnetic_3d | 186 | 32 | 1.279 | 1.748 | 4.86 [3.828, 5.729] | [3.503, 6.814] | 5.494 [4.711, 6.355] | 14.336 [12.514, 20.304] | 7.241 [6.028, 8.46] | 1.49 | 1.5 | 4.623 |  |
| chem:metal | 463 | 81 | 7.696 | 5.766 | 8.716 [7.631, 9.45] | [6.722, 10.235] | 10.856 [9.463, 11.927] | 31.112 [26.949, 34.96] | 14.17 [12.602, 15.834] | 1.63 | 2.0 | 8.483 |  |
| chem:pblock_anion | 532 | 73 | 1.397 | 0.201 | 11.641 [10.351, 13.485] | [7.444, 16.878] | 13.923 [12.551, 15.247] | 35.197 [31.368, 36.792] | 23.072 [18.085, 28.553] | 1.98 | 2.0 | 11.468 |  |
| match:above_hull | 227 | 75 | 7.966 | 6.018 | 8.36 [7.391, 9.889] | [6.313, 10.822] | 13.095 [11.488, 14.946] | 30.933 [25.624, 36.087] | 14.663 [13.003, 16.376] | 1.75 | 2.0 | 8.117 |  |
| match:on_hull_single | 450 | 123 | 4.552 | 3.088 | 8.068 [6.907, 9.201] | [6.377, 10.732] | 9.695 [8.116, 11.222] | 28.975 [25.478, 31.489] | 12.814 [11.407, 14.121] | 1.59 | 2.0 | 7.816 |  |
| match:polymorph_ambiguous | 504 | 114 | 1.364 | 0.481 | 8.767 [7.371, 11.219] | [6.307, 12.839] | 11.048 [9.99, 13.081] | 35.073 [30.571, 37.409] | 22.853 [17.198, 28.244] | 2.61 | 2.0 | 8.536 |  |
| on_hull_single|magnetic_3d | 72 | 24 | 1.216 | 0.946 | 4.97 [3.801, 6.927] | [3.447, 7.454] | 5.538 [4.235, 6.494] | 12.141 [8.205, 14.396] | 5.814 [4.631, 6.963] | 1.17 | 2.0 | 4.55 |  |
| on_hull_single|metal | 248 | 66 | 6.913 | 5.671 | 9.382 [8.237, 10.692] | [7.075, 11.95] | 11.157 [9.46, 12.35] | 29.52 [25.489, 31.489] | 13.466 [11.716, 15.22] | 1.44 | 2.0 | 9.166 |  |
| on_hull_single|pblock_anion | 130 | 33 | 1.897 | 0.98 | 8.71 [6.269, 11.278] | [4.447, 17.745] | 11.366 [8.047, 13.377] | 30.856 [23.96, 36.588] | 14.273 [11.684, 16.869] | 1.64 | 2.092 | 8.455 |  |
| polymorph_ambiguous|magnetic_3d | 77 | 21 | -1.467 | 0.093 | 5.017 [3.312, 6.406] | [2.59, 10.083] | 4.861 [3.705, 5.412] | 14.304 [9.886, 20.314] | 6.795 [5.258, 8.332] | 1.35 | 1.6 | 4.755 |  |
| polymorph_ambiguous|metal | 92 | 41 | 8.89 | 5.052 | 6.574 [4.941, 10.146] | [3.95, 10.64] | 9.987 [6.419, 12.741] | 35.628 [20.364, 52.646] | 16.359 [11.146, 20.918] | 2.49 | 2.0 | 6.262 |  |
| polymorph_ambiguous|pblock_anion | 335 | 52 | -0.053 | -1.156 | 10.816 [9.395, 13.635] | [7.032, 17.343] | 13.668 [11.358, 15.699] | 36.3 [31.41, 45.479] | 26.488 [19.697, 33.624] | 2.45 | 2.0 | 10.629 |  |

## oqmd

| stratum | n | systems | bias mean | bias median | robust sigma [95% CI pairs] | 95% CI systems | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---:|---|---|---|---|---|---:|---:|---:|---|
| all | 1222 | 193 | 4.805 | 2.386 | 7.487 [6.86, 8.526] | [6.394, 9.323] | 9.042 [8.332, 10.137] | 27.578 [25.269, 29.942] | 16.562 [13.916, 19.703] | 2.21 | 2.0 | 7.215 |  |
| above_hull|magnetic_3d | 65 | 19 | 2.628 | 2.859 | 7.383 [3.621, 9.478] | [2.672, 15.318] | 9.939 [6.522, 14.51] | 25.077 [16.705, 26.974] | 11.34 [9.114, 13.492] | 1.54 | 1.3 | 7.268 |  |
| above_hull|metal | 109 | 40 | 7.72 | 5.148 | 7.302 [5.563, 8.992] | [5.284, 10.085] | 10.702 [8.501, 12.622] | 29.03 [22.249, 42.489] | 14.203 [11.065, 17.265] | 1.95 | 2.15 | 6.978 |  |
| above_hull|pblock_anion | 78 | 27 | 9.436 | 8.194 | 12.905 [8.16, 15.708] | [4.992, 15.999] | 15.067 [11.107, 19.514] | 27.645 [24.178, 33.759] | 14.674 [12.504, 16.831] | 1.14 | 2.6 | 12.64 |  |
| chem:magnetic_3d | 207 | 34 | 0.733 | 1.236 | 5.277 [4.377, 6.448] | [3.825, 7.418] | 5.688 [5.071, 6.348] | 18.378 [15.537, 23.04] | 7.899 [6.719, 9.015] | 1.5 | 1.6 | 5.029 |  |
| chem:metal | 468 | 84 | 5.748 | 3.748 | 7.922 [6.643, 8.826] | [5.746, 9.834] | 9.528 [8.339, 10.604] | 27.316 [22.808, 29.95] | 12.641 [11.259, 14.22] | 1.6 | 2.0 | 7.665 |  |
| chem:pblock_anion | 547 | 75 | 5.538 | 1.945 | 9.047 [7.828, 10.436] | [7.019, 11.553] | 10.624 [9.389, 11.406] | 31.854 [26.519, 36.036] | 21.271 [15.991, 26.718] | 2.35 | 2.09 | 8.802 |  |
| match:above_hull | 252 | 86 | 6.938 | 4.804 | 8.013 [6.524, 9.385] | [5.721, 10.515] | 11.771 [10.064, 13.56] | 26.806 [24.79, 32.02] | 13.678 [12.123, 15.127] | 1.71 | 2.0 | 7.759 |  |
| match:on_hull_single | 88 | 39 | 4.01 | 2.505 | 6.887 [4.401, 9.96] | [3.918, 11.318] | 9.471 [5.407, 13.861] | 23.669 [17.993, 29.056] | 11.141 [8.97, 13.156] | 1.62 | 2.05 | 6.575 |  |
| match:polymorph_ambiguous | 882 | 177 | 4.274 | 1.389 | 7.354 [6.886, 8.152] | [6.432, 9.207] | 8.39 [7.526, 9.372] | 28.236 [24.093, 31.151] | 17.725 [13.964, 21.242] | 2.41 | 2.0 | 7.077 |  |
| on_hull_single|magnetic_3d | 17 | 8 | 0.946 | 0.998 | 3.035 [1.179, 6.457] | [0.786, 6.454] | 4.192 [2.515, 5.407] | 5.703 [4.927, 5.934] | 3.571 [2.702, 4.325] | 1.18 | 3.0 | 0.46 | < 30: falls back |
| on_hull_single|metal | 44 | 21 | 4.796 | 4.909 | 10.148 [5.856, 12.274] | [5.324, 12.829] | 11.358 [5.706, 14.149] | 22.86 [17.057, 35.934] | 11.898 [8.668, 15.117] | 1.17 | 2.0 | 9.949 |  |
| on_hull_single|pblock_anion | 27 | 10 | 4.658 | 1.404 | 7.149 [1.957, 21.88] | [2.665, 17.886] | 13.862 [3.626, 18.543] | 24.183 [16.534, 28.734] | 12.877 [9.579, 15.837] | 1.8 | 2.0 | 6.864 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 125 | 31 | -0.28 | -0.127 | 4.962 [3.88, 6.002] | [3.516, 6.683] | 5.071 [4.135, 5.771] | 12.877 [8.261, 18.471] | 5.892 [4.78, 6.918] | 1.19 | 1.9 | 4.584 |  |
| polymorph_ambiguous|metal | 315 | 78 | 5.199 | 2.558 | 7.025 [5.871, 8.509] | [5.3, 9.74] | 8.84 [7.411, 10.213] | 25.069 [20.16, 29.387] | 12.158 [10.294, 13.873] | 1.73 | 2.0 | 6.734 |  |
| polymorph_ambiguous|pblock_anion | 442 | 68 | 4.904 | 1.076 | 8.208 [7.707, 9.705] | [6.799, 11.517] | 10.018 [8.505, 10.828] | 34.585 [27.512, 36.361] | 22.623 [16.397, 28.878] | 2.76 | 2.09 | 7.937 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 c1cb6e4361a3eb2c3d96092c62b98a5fbbd65aa746aa2bf71cd19c6c6cfe0c67.
