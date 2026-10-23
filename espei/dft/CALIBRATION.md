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
| all | 254 | 3.565 | 1.09 | 5.46 [4.583, 6.524] | 6.09 [5.158, 6.761] | 34.771 [25.515, 49.28] | 18.441 [13.539, 22.934] | 3.38 | 1.5 | 5.25 |  |
| magnetic_3d | 94 | 7.04 | 1.415 | 3.253 [2.466, 4.577] | 4.249 [3.608, 4.996] | 55.869 [22.615, 104.388] | 25.525 [16.014, 34.839] | 7.85 | 1.3 | 2.982 |  |
| metal | 100 | 2.909 | 0.577 | 6.769 [5.381, 8.734] | 6.44 [5.312, 8.8] | 28.824 [21.463, 35.535] | 12.222 [9.557, 14.675] | 1.81 | 1.3 | 6.643 |  |
| pblock_anion | 60 | -0.785 | 0.989 | 7.058 [5.262, 11.505] | 10.448 [5.82, 12.488] | 32.524 [14.129, 39.39] | 13.035 [8.83, 16.864] | 1.85 | 3.6 | 6.071 |  |

## mp

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1231 | 4.201 | 2.534 | 9.143 [8.2, 10.094] | 11.463 [10.272, 11.998] | 34.013 [31.424, 36.408] | 18.709 [15.921, 21.69] | 2.05 | 2.0 | 8.922 |  |
| above_hull|magnetic_3d | 42 | 7.302 | 5.343 | 4.285 [2.402, 6.895] | 7.776 [5.62, 11.657] | 17.386 [13.096, 31.319] | 9.916 [6.934, 12.91] | 2.31 | 1.05 | 4.154 |  |
| above_hull|metal | 127 | 7.937 | 6.318 | 7.283 [5.606, 8.42] | 10.22 [7.848, 11.898] | 31.009 [21.522, 39.009] | 13.469 [10.942, 15.858] | 1.85 | 2.0 | 7.003 |  |
| above_hull|pblock_anion | 80 | 11.777 | 7.551 | 17.765 [13.634, 20.31] | 19.537 [16.398, 23.335] | 44.916 [26.714, 121.142] | 31.062 [17.131, 43.536] | 1.75 | 2.9 | 17.527 |  |
| chem:magnetic_3d | 190 | 1.045 | 1.748 | 5.039 [4.099, 6.103] | 5.608 [4.863, 6.746] | 15.659 [13.003, 20.309] | 7.697 [6.441, 8.988] | 1.53 | 1.5 | 4.811 |  |
| chem:metal | 484 | 7.46 | 5.681 | 8.876 [7.691, 9.453] | 10.473 [9.428, 11.799] | 30.819 [26.868, 34.634] | 13.959 [12.543, 15.612] | 1.57 | 2.0 | 8.648 |  |
| chem:pblock_anion | 557 | 2.446 | 0.298 | 12.228 [10.822, 14.261] | 14.822 [13.377, 16.873] | 37.052 [35.551, 45.801] | 24.167 [19.298, 29.044] | 1.98 | 2.092 | 12.048 |  |
| match:above_hull | 249 | 9.063 | 5.766 | 8.688 [6.934, 9.633] | 12.104 [10.22, 14.523] | 32.301 [25.92, 42.429] | 20.472 [14.495, 26.962] | 2.36 | 2.0 | 8.455 |  |
| match:on_hull_single | 474 | 4.878 | 3.096 | 8.419 [7.156, 9.624] | 10.728 [8.951, 11.77] | 31.489 [28.638, 35.134] | 13.755 [12.5, 14.955] | 1.63 | 2.0 | 8.178 |  |
| match:polymorph_ambiguous | 508 | 1.186 | 0.324 | 9.028 [7.604, 11.067] | 11.738 [10.03, 13.128] | 36.453 [31.508, 46.746] | 21.591 [16.517, 27.058] | 2.39 | 2.0 | 8.804 |  |
| on_hull_single|magnetic_3d | 70 | 1.196 | 0.942 | 4.765 [3.575, 6.73] | 5.515 [4.174, 6.529] | 12.441 [8.227, 14.396] | 5.82 [4.654, 7.022] | 1.22 | 1.5 | 4.523 |  |
| on_hull_single|metal | 259 | 6.77 | 5.187 | 9.575 [8.274, 10.688] | 11.046 [9.409, 11.96] | 29.341 [25.489, 31.489] | 13.335 [11.702, 15.099] | 1.39 | 2.0 | 9.364 |  |
| on_hull_single|pblock_anion | 145 | 3.277 | 1.305 | 9.973 [7.797, 14.08] | 13.314 [11.044, 20.778] | 36.588 [34.238, 40.665] | 16.867 [14.494, 19.088] | 1.69 | 2.15 | 9.738 |  |
| polymorph_ambiguous|magnetic_3d | 78 | -2.46 | -0.607 | 5.929 [3.974, 7.447] | 5.048 [4.097, 6.991] | 20.304 [11.608, 21.096] | 7.807 [5.783, 9.695] | 1.32 | 1.3 | 5.785 |  |
| polymorph_ambiguous|metal | 98 | 8.666 | 5.335 | 7.085 [5.461, 10.592] | 10.172 [6.93, 12.759] | 35.285 [20.301, 48.713] | 16.04 [11.328, 20.789] | 2.26 | 1.9 | 6.825 |  |
| polymorph_ambiguous|pblock_anion | 332 | -0.165 | -1.25 | 10.69 [9.234, 13.55] | 13.98 [11.765, 15.981] | 41.165 [34.65, 52.959] | 24.961 [18.605, 32.095] | 2.33 | 2.0 | 10.501 |  |

## oqmd

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1294 | 5.105 | 2.361 | 7.8 [7.084, 8.656] | 9.364 [8.484, 10.246] | 29.845 [27.468, 34.742] | 17.156 [14.68, 20.292] | 2.2 | 2.0 | 7.539 |  |
| above_hull|magnetic_3d | 106 | 2.687 | 2.413 | 5.415 [4.028, 8.523] | 8.011 [5.771, 10.618] | 24.983 [18.623, 25.855] | 10.468 [8.565, 11.983] | 1.93 | 1.4 | 5.231 |  |
| above_hull|metal | 222 | 6.749 | 4.795 | 8.604 [7.285, 10.075] | 10.203 [8.544, 11.767] | 27.569 [22.794, 29.923] | 12.881 [10.939, 14.568] | 1.5 | 2.0 | 8.368 |  |
| above_hull|pblock_anion | 169 | 3.876 | 3.742 | 9.026 [7.309, 11.139] | 11.346 [9.356, 14.957] | 34.45 [26.346, 41.652] | 15.616 [13.09, 18.123] | 1.73 | 2.3 | 8.728 |  |
| chem:magnetic_3d | 224 | 0.873 | 1.415 | 5.529 [4.499, 6.727] | 5.987 [5.423, 6.883] | 21.925 [16.147, 25.584] | 8.653 [7.516, 9.772] | 1.57 | 1.5 | 5.322 |  |
| chem:metal | 495 | 5.423 | 3.436 | 7.726 [6.606, 8.784] | 9.31 [8.246, 10.237] | 26.211 [22.526, 29.276] | 12.383 [10.908, 13.785] | 1.6 | 2.0 | 7.463 |  |
| chem:pblock_anion | 575 | 6.48 | 2.132 | 9.545 [8.251, 10.877] | 11.322 [10.248, 12.596] | 36.287 [32.563, 43.057] | 22.387 [17.625, 26.962] | 2.35 | 2.1 | 9.311 |  |
| match:above_hull | 497 | 4.905 | 3.732 | 8.439 [7.357, 9.434] | 10.213 [8.888, 11.494] | 27.761 [25.344, 31.166] | 13.431 [12.201, 14.67] | 1.59 | 2.0 | 8.199 |  |
| match:on_hull_single | 79 | 4.592 | 2.515 | 7.361 [4.384, 11.057] | 11.369 [5.471, 14.148] | 24.669 [19.153, 29.229] | 12.074 [9.632, 14.289] | 1.64 | 2.0 | 7.084 |  |
| match:polymorph_ambiguous | 718 | 5.3 | 1.213 | 7.672 [6.956, 8.385] | 8.426 [7.487, 9.926] | 34.667 [27.82, 36.287] | 19.736 [15.434, 24.23] | 2.57 | 2.0 | 7.407 |  |
| on_hull_single|magnetic_3d | 15 | 0.961 | 2.495 | 3.434 [0.786, 6.89] | 4.55 [2.515, 5.407] | 5.732 [4.99, 5.934] | 3.738 [2.834, 4.474] | 1.09 | 2.2 | 2.637 | < 30: falls back |
| on_hull_single|metal | 37 | 5.094 | 4.962 | 10.989 [5.696, 12.85] | 11.485 [5.998, 15.805] | 24.134 [17.676, 37.117] | 12.657 [9.155, 15.9] | 1.15 | 2.0 | 10.805 |  |
| on_hull_single|pblock_anion | 27 | 5.92 | 2.424 | 7.116 [1.92, 24.14] | 14.288 [6.104, 22.627] | 27.379 [19.488, 28.734] | 14.117 [10.519, 17.448] | 1.98 | 2.0 | 6.829 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 103 | -1.007 | -0.486 | 5.392 [3.929, 6.838] | 5.776 [4.329, 6.462] | 16.028 [8.269, 19.052] | 6.931 [5.397, 8.489] | 1.29 | 1.9 | 5.046 |  |
| polymorph_ambiguous|metal | 236 | 4.228 | 1.925 | 6.299 [4.989, 7.352] | 7.509 [6.64, 9.359] | 21.663 [17.06, 35.477] | 11.85 [9.319, 14.171] | 1.88 | 2.0 | 5.973 |  |
| polymorph_ambiguous|pblock_anion | 379 | 7.682 | 1.145 | 9.189 [7.958, 11.207] | 10.798 [9.381, 12.244] | 36.287 [34.648, 58.486] | 25.248 [19.275, 32.098] | 2.75 | 2.1 | 8.946 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 a4b72c282ebf7ac96a79d7d2107be820e0fe4369a7351759f8706d1a93390599.
