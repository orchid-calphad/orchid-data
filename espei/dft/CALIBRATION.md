# DFT formation-enthalpy uncertainty: calibration

Calibrated from ORCHID's own DFT-vs-experiment pairs (`literature/dft_parity.json`, default subset: experimental, accepted, signed, not magnitude-suspect; residual = DFT - experiment, kJ/mol-atom). Materials Project and OQMD are calibrated separately (different energy references). Literature DFT: each accepted literature DFT HM_FORM value (kJ/mol-atom, binary) paired with the median experimental value of the same compound (same reduced composition) in that subset.

## Method

- bias: mean and median residual (**recorded, not applied** to any value);
- robust sigma = 1.4826 x MAD (median absolute deviation about the median); 68 / 95 % quantiles of |residual|; RMSE;
- 95% confidence intervals: 1000 bootstrap resamples of the pairs (fixed seeds), percentile intervals;
- strata: match quality (`on_hull_single` DFT entry on the hull and the only entry at its composition; `polymorph_ambiguous` on the hull, several entries (polymorphs) at the composition; `above_hull` lowest DFT entry at the composition lies above the hull) x chemistry (`metal` all-metal intermetallic (none of the elements below); `pblock_anion` contains a p-block / anion element (H, B, C, N, O, F, Si, P, S, Se, Te, As, Sb, halogens); `magnetic_3d` contains Cr, Mn, Fe, Co or Ni (and no p-block / anion element)); chemistry precedence: p-block / anion, then magnetic 3d, then all-metal; single-factor strata are listed too;
- experimental-error-deconvolved sigma_DFT = sqrt(sigma_robust^2 - sigma_exp^2), sigma_exp = median printed experimental uncertainty of the matched records (reported, not used);
- weights use the plain robust sigma (conservative), **leave-system-out**: for each system the sigma of its stratum is recomputed without that system's pairs; a stratum with fewer than 30 pairs falls back to the source-level sigma (also leave-system-out);
- exported MP / OQMD values are on-hull vertices: stratum `on_hull_single` when the vertex is the only entry at its composition, else `polymorph_ambiguous`; literature DFT values use the chemistry stratum;
- ESPEI weight = 500 J/mol / sigma_DFT (J/mol-atom). 500 J/mol is ESPEI's reference sigma for experimental HM data; the ratio only makes ESPEI use the calibrated DFT sigma.

## Caveats

- Heavy tails: RMSE exceeds the robust sigma (column `RMSE/sigma`) and the 95 % quantile of |residual| is several robust sigmas; a Gaussian likelihood with the robust sigma treats the tail compounds as far less likely than they are, so a few outliers can pull a fit hard. Consider a Student-t or a wider sigma if your fit is sensitive to a few compounds.
- Pairs are treated as independent; several experimental records of one compound and correlated errors within a chemistry are not modelled.
- The calibration is against literature experiments (machine-extracted, Version 1) and inherits their errors; sigma_deconvolved shows how much of the spread the printed experimental uncertainty explains.
- 0 K DFT energies are used as 298.15 K enthalpies.

## literature

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 258 | 3.748 | 1.123 | 5.411 [4.592, 6.488] | 6.098 [5.264, 6.982] | 34.559 [24.67, 49.573] | 18.211 [12.974, 23.294] | 3.37 | 1.5 | 5.199 |  |
| magnetic_3d | 94 | 7.359 | 1.415 | 3.253 [2.494, 4.312] | 4.133 [3.452, 4.902] | 55.869 [17.95, 104.388] | 25.299 [15.234, 34.605] | 7.78 | 1.3 | 2.982 |  |
| metal | 100 | 2.909 | 0.577 | 6.769 [5.381, 8.734] | 6.44 [5.312, 8.8] | 28.824 [21.463, 35.535] | 12.222 [9.557, 14.675] | 1.81 | 1.3 | 6.643 |  |
| pblock_anion | 64 | -0.246 | 1.215 | 6.883 [5.244, 11.298] | 10.278 [5.967, 11.755] | 31.223 [13.918, 38.767] | 12.789 [8.677, 16.341] | 1.86 | 3.6 | 5.866 |  |

## mp

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1204 | 4.316 | 2.556 | 9.102 [8.173, 10.032] | 11.625 [10.372, 12.167] | 34.066 [31.412, 36.559] | 18.811 [16.002, 21.638] | 2.07 | 2.0 | 8.88 |  |
| above_hull|magnetic_3d | 41 | 7.24 | 5.066 | 4.018 [2.374, 6.653] | 7.776 [5.62, 11.681] | 17.556 [13.166, 31.424] | 9.918 [6.819, 12.918] | 2.47 | 1.05 | 3.878 |  |
| above_hull|metal | 122 | 8.061 | 6.371 | 7.43 [5.783, 8.812] | 10.282 [7.952, 12.104] | 31.446 [21.551, 39.009] | 13.682 [11.18, 16.091] | 1.84 | 2.0 | 7.156 |  |
| above_hull|pblock_anion | 74 | 12.877 | 10.922 | 14.634 [12.339, 18.778] | 19.562 [16.589, 23.652] | 46.156 [27.059, 121.142] | 32.103 [17.842, 44.829] | 2.19 | 3.3 | 14.257 |  |
| chem:magnetic_3d | 192 | 1.213 | 1.909 | 4.886 [3.829, 5.9] | 5.503 [4.72, 6.393] | 14.396 [12.799, 20.304] | 7.334 [6.148, 8.534] | 1.5 | 1.5 | 4.65 |  |
| chem:metal | 474 | 7.511 | 5.681 | 8.91 [7.758, 9.486] | 10.54 [9.496, 11.819] | 30.947 [27.111, 34.09] | 14.057 [12.546, 15.591] | 1.58 | 2.0 | 8.683 |  |
| chem:pblock_anion | 538 | 2.609 | 0.457 | 12.459 [11.075, 14.985] | 15.155 [13.494, 17.28] | 37.025 [35.679, 47.194] | 24.466 [19.771, 29.613] | 1.96 | 2.096 | 12.281 |  |
| match:above_hull | 237 | 9.422 | 5.793 | 8.647 [6.909, 9.725] | 12.41 [11.148, 15.131] | 32.813 [26.227, 44.709] | 20.861 [14.614, 27.463] | 2.41 | 2.0 | 8.413 |  |
| match:on_hull_single | 464 | 5.04 | 3.106 | 8.416 [7.149, 9.749] | 10.748 [8.755, 11.775] | 31.477 [28.725, 34.915] | 13.701 [12.436, 14.862] | 1.63 | 2.0 | 8.175 |  |
| match:polymorph_ambiguous | 503 | 1.243 | 0.457 | 8.904 [7.652, 11.158] | 11.748 [10.045, 13.226] | 36.529 [32.578, 46.746] | 21.652 [16.71, 26.759] | 2.43 | 2.0 | 8.676 |  |
| on_hull_single|magnetic_3d | 70 | 1.196 | 0.942 | 4.765 [3.575, 6.73] | 5.515 [4.174, 6.529] | 12.441 [8.227, 14.396] | 5.82 [4.654, 7.022] | 1.22 | 1.5 | 4.523 |  |
| on_hull_single|metal | 254 | 6.802 | 5.194 | 9.532 [8.022, 10.577] | 10.961 [9.411, 12.002] | 29.423 [25.489, 31.489] | 13.401 [11.788, 15.15] | 1.41 | 2.0 | 9.32 |  |
| on_hull_single|pblock_anion | 140 | 3.765 | 1.729 | 10.102 [7.985, 14.287] | 13.379 [11.06, 20.778] | 36.588 [32.132, 36.588] | 16.716 [14.387, 18.866] | 1.65 | 2.15 | 9.871 |  |
| polymorph_ambiguous|magnetic_3d | 81 | -1.823 | -0.068 | 5.361 [3.598, 6.547] | 4.974 [4.016, 5.61] | 16.692 [11.014, 20.314] | 6.959 [5.392, 8.423] | 1.3 | 1.45 | 5.161 |  |
| polymorph_ambiguous|metal | 98 | 8.666 | 5.335 | 7.085 [5.461, 10.592] | 10.172 [6.93, 12.759] | 35.285 [20.301, 48.713] | 16.04 [11.328, 20.789] | 2.26 | 1.9 | 6.825 |  |
| polymorph_ambiguous|pblock_anion | 324 | -0.236 | -1.724 | 11.474 [9.36, 13.871] | 14.14 [11.944, 16.471] | 42.313 [34.726, 52.959] | 25.256 [18.512, 32.073] | 2.2 | 2.0 | 11.298 |  |

## oqmd

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1258 | 5.21 | 2.455 | 7.842 [7.096, 8.661] | 9.351 [8.474, 10.23] | 30.001 [27.46, 34.92] | 17.287 [14.515, 20.024] | 2.2 | 2.0 | 7.583 |  |
| above_hull|magnetic_3d | 101 | 1.968 | 2.266 | 5.499 [3.631, 7.862] | 7.606 [5.303, 9.208] | 23.168 [16.806, 25.853] | 9.843 [8.158, 11.529] | 1.79 | 1.4 | 5.318 |  |
| above_hull|metal | 210 | 7.04 | 4.806 | 8.62 [7.321, 10.089] | 10.245 [8.7, 11.774] | 28.133 [23.352, 30.619] | 13.161 [11.338, 14.96] | 1.53 | 2.0 | 8.385 |  |
| above_hull|pblock_anion | 168 | 4.067 | 3.744 | 9.028 [7.224, 11.144] | 11.282 [9.137, 14.792] | 34.507 [25.513, 41.652] | 15.51 [12.916, 17.999] | 1.72 | 2.3 | 8.73 |  |
| chem:magnetic_3d | 222 | 0.697 | 1.4 | 5.011 [4.28, 6.156] | 5.811 [5.136, 6.397] | 19.009 [15.658, 23.116] | 7.958 [6.846, 9.002] | 1.59 | 1.5 | 4.781 |  |
| chem:metal | 480 | 5.586 | 3.516 | 7.766 [6.667, 8.781] | 9.423 [8.339, 10.343] | 26.742 [22.808, 29.415] | 12.51 [11.141, 13.985] | 1.61 | 2.0 | 7.504 |  |
| chem:pblock_anion | 556 | 6.687 | 2.363 | 9.741 [8.5, 11.192] | 11.413 [10.396, 13.007] | 36.287 [33.973, 45.213] | 22.711 [18.052, 27.838] | 2.33 | 2.1 | 9.512 |  |
| match:above_hull | 479 | 4.928 | 3.732 | 8.365 [7.139, 9.354] | 10.203 [8.781, 11.663] | 27.739 [25.274, 32.02] | 13.444 [12.103, 14.763] | 1.61 | 2.0 | 8.122 |  |
| match:on_hull_single | 78 | 4.645 | 2.607 | 7.498 [4.384, 11.095] | 11.453 [5.532, 14.074] | 24.895 [19.423, 29.229] | 12.151 [9.58, 14.352] | 1.62 | 2.0 | 7.226 |  |
| match:polymorph_ambiguous | 701 | 5.465 | 1.319 | 7.696 [6.996, 8.467] | 8.426 [7.516, 9.961] | 34.967 [28.262, 36.287] | 19.909 [15.559, 24.377] | 2.59 | 2.0 | 7.432 |  |
| on_hull_single|magnetic_3d | 15 | 0.961 | 2.495 | 3.434 [0.786, 6.89] | 4.55 [2.515, 5.407] | 5.732 [4.99, 5.934] | 3.738 [2.834, 4.474] | 1.09 | 2.2 | 2.637 | < 30: falls back |
| on_hull_single|metal | 36 | 5.222 | 5.135 | 11.245 [5.908, 13.654] | 11.57 [6.362, 16.929] | 24.452 [17.696, 37.117] | 12.831 [9.113, 16.243] | 1.14 | 2.0 | 11.066 |  |
| on_hull_single|pblock_anion | 27 | 5.92 | 2.424 | 7.116 [1.92, 24.14] | 14.288 [6.104, 22.627] | 27.379 [19.488, 28.734] | 14.117 [10.519, 17.448] | 1.98 | 2.0 | 6.829 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 106 | -0.552 | 0.444 | 4.444 [3.841, 6.553] | 5.605 [4.222, 6.364] | 14.538 [8.261, 18.189] | 6.193 [5.13, 7.318] | 1.39 | 1.9 | 4.017 |  |
| polymorph_ambiguous|metal | 234 | 4.336 | 1.955 | 6.339 [4.969, 7.315] | 7.482 [6.602, 9.388] | 21.765 [16.872, 35.577] | 11.844 [9.565, 14.205] | 1.87 | 2.0 | 6.015 |  |
| polymorph_ambiguous|pblock_anion | 361 | 7.963 | 1.153 | 9.578 [8.239, 11.585] | 11.084 [10.013, 12.758] | 36.287 [34.958, 58.486] | 25.837 [19.475, 32.456] | 2.7 | 2.1 | 9.345 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 56ab754e813a424ccc46eaf98e62fbf91bc90e9527bacbbefb907a598eb9800d.
