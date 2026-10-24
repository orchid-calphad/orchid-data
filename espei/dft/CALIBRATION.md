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
| all | 247 | 3.895 | 1.078 | 5.244 [4.359, 6.753] | 6.1 [5.104, 7.978] | 35.143 [25.041, 49.954] | 18.597 [13.281, 23.646] | 3.55 | 2.0 | 4.848 |  |
| magnetic_3d | 90 | 7.613 | 1.27 | 3.522 [2.601, 4.595] | 4.311 [3.613, 5.3] | 57.89 [17.95, 105.607] | 25.852 [15.155, 35.125] | 7.34 | 1.5 | 3.187 |  |
| metal | 93 | 3.147 | 0.214 | 6.28 [4.783, 8.981] | 6.937 [5.567, 10.567] | 29.552 [22.49, 36.055] | 12.618 [9.818, 15.266] | 2.01 | 2.0 | 5.953 |  |
| pblock_anion | 64 | -0.246 | 1.215 | 6.883 [5.244, 11.298] | 10.278 [5.967, 11.755] | 31.223 [13.918, 38.767] | 12.789 [8.677, 16.341] | 1.86 | 3.6 | 5.866 |  |

## mp

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1199 | 4.059 | 2.532 | 8.937 [8.082, 9.973] | 11.213 [10.22, 11.985] | 32.886 [31.111, 36.197] | 18.675 [15.818, 21.755] | 2.09 | 2.0 | 8.71 |  |
| above_hull|magnetic_3d | 39 | 7.387 | 5.066 | 4.353 [2.448, 7.086] | 7.776 [5.62, 11.776] | 18.733 [13.166, 31.424] | 10.116 [7.02, 13.299] | 2.32 | 1.5 | 4.086 |  |
| above_hull|metal | 124 | 8.128 | 6.556 | 7.567 [5.732, 8.48] | 10.363 [8.089, 12.104] | 31.271 [21.537, 39.009] | 13.63 [10.978, 16.038] | 1.8 | 2.0 | 7.298 |  |
| above_hull|pblock_anion | 74 | 12.877 | 10.922 | 14.634 [12.339, 18.778] | 19.562 [16.589, 23.652] | 46.156 [27.059, 121.142] | 32.103 [17.842, 44.829] | 2.19 | 3.3 | 14.257 |  |
| chem:magnetic_3d | 191 | 1.125 | 1.748 | 4.993 [3.919, 6.019] | 5.433 [4.655, 6.49] | 14.396 [12.804, 20.304] | 7.345 [6.176, 8.559] | 1.47 | 1.5 | 4.762 |  |
| chem:metal | 480 | 7.434 | 5.639 | 8.861 [7.554, 9.338] | 10.423 [9.453, 11.734] | 30.857 [25.509, 33.618] | 13.939 [12.366, 15.532] | 1.57 | 2.0 | 8.632 |  |
| chem:pblock_anion | 528 | 2.053 | 0.277 | 12.216 [10.649, 14.512] | 14.729 [13.28, 16.494] | 39.039 [35.572, 48.082] | 24.409 [19.628, 29.677] | 2.0 | 2.1 | 12.034 |  |
| match:above_hull | 237 | 9.489 | 6.201 | 8.295 [6.964, 9.664] | 12.613 [11.104, 15.143] | 32.813 [26.071, 44.709] | 20.877 [14.452, 27.397] | 2.52 | 2.0 | 8.05 |  |
| match:on_hull_single | 456 | 4.206 | 2.889 | 8.079 [6.905, 9.154] | 9.813 [8.199, 11.422] | 29.515 [25.892, 31.93] | 13.18 [11.886, 14.565] | 1.63 | 2.0 | 7.828 |  |
| match:polymorph_ambiguous | 506 | 1.384 | 0.481 | 8.795 [7.492, 11.236] | 11.749 [9.994, 13.163] | 36.483 [31.447, 46.427] | 21.58 [16.524, 26.738] | 2.45 | 2.0 | 8.565 |  |
| on_hull_single|magnetic_3d | 70 | 1.097 | 0.903 | 4.97 [3.746, 7.047] | 5.515 [4.211, 6.525] | 12.441 [8.121, 14.396] | 5.836 [4.657, 7.029] | 1.17 | 1.65 | 4.688 |  |
| on_hull_single|metal | 257 | 6.656 | 5.075 | 9.496 [7.938, 10.506] | 10.77 [9.135, 11.933] | 29.374 [25.489, 31.489] | 13.237 [11.603, 14.876] | 1.39 | 2.0 | 9.283 |  |
| on_hull_single|pblock_anion | 129 | 1.013 | 0.955 | 9.188 [6.449, 12.414] | 12.097 [8.447, 14.036] | 36.17 [27.186, 41.407] | 15.701 [12.946, 18.438] | 1.71 | 2.25 | 8.908 |  |
| polymorph_ambiguous|magnetic_3d | 82 | -1.83 | -0.137 | 5.414 [3.61, 6.589] | 4.94 [3.849, 5.412] | 16.498 [10.939, 20.314] | 6.921 [5.372, 8.318] | 1.28 | 1.6 | 5.172 |  |
| polymorph_ambiguous|metal | 99 | 8.588 | 4.852 | 7.303 [5.391, 10.443] | 10.132 [7.271, 12.998] | 35.228 [20.436, 48.057] | 15.953 [11.724, 21.067] | 2.18 | 2.0 | 7.024 |  |
| polymorph_ambiguous|pblock_anion | 325 | 0.001 | -1.653 | 11.913 [9.469, 13.834] | 14.2 [12.337, 16.476] | 42.17 [34.089, 53.84] | 25.208 [18.827, 32.055] | 2.12 | 2.09 | 11.728 |  |

## oqmd

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1251 | 4.947 | 2.364 | 7.655 [6.947, 8.536] | 9.094 [8.388, 10.074] | 28.955 [26.007, 34.19] | 17.172 [14.402, 19.965] | 2.24 | 2.0 | 7.389 |  |
| above_hull|magnetic_3d | 98 | 1.967 | 2.266 | 5.512 [3.623, 8.374] | 7.606 [5.303, 10.558] | 23.169 [17.162, 25.853] | 9.967 [8.192, 11.677] | 1.81 | 1.5 | 5.304 |  |
| above_hull|metal | 212 | 7.005 | 4.806 | 8.494 [7.162, 10.059] | 10.22 [8.647, 11.774] | 28.046 [22.952, 30.497] | 13.099 [11.136, 14.873] | 1.54 | 2.0 | 8.255 |  |
| above_hull|pblock_anion | 167 | 4.187 | 3.745 | 9.031 [6.929, 10.975] | 11.241 [9.009, 14.609] | 34.565 [25.614, 41.652] | 15.507 [13.037, 18.091] | 1.72 | 2.3 | 8.733 |  |
| chem:magnetic_3d | 220 | 0.629 | 1.238 | 5.062 [4.329, 6.368] | 5.902 [5.281, 6.402] | 19.061 [15.668, 23.168] | 7.989 [6.884, 8.968] | 1.58 | 1.6 | 4.802 |  |
| chem:metal | 485 | 5.541 | 3.469 | 7.669 [6.596, 8.644] | 9.329 [8.259, 10.244] | 26.556 [22.752, 29.387] | 12.435 [11.033, 13.921] | 1.62 | 2.0 | 7.404 |  |
| chem:pblock_anion | 546 | 6.16 | 2.087 | 9.424 [8.045, 10.883] | 11.081 [10.052, 12.244] | 36.287 [31.685, 47.347] | 22.639 [17.608, 27.702] | 2.4 | 2.1 | 9.187 |  |
| match:above_hull | 477 | 4.983 | 3.732 | 8.172 [7.104, 9.143] | 10.203 [8.809, 11.611] | 27.826 [25.279, 31.947] | 13.448 [12.122, 14.776] | 1.65 | 2.0 | 7.923 |  |
| match:on_hull_single | 78 | 4.15 | 2.607 | 7.365 [4.549, 10.835] | 11.358 [5.452, 13.967] | 24.121 [17.996, 29.229] | 11.495 [9.145, 13.642] | 1.56 | 2.0 | 7.088 |  |
| match:polymorph_ambiguous | 696 | 5.012 | 1.213 | 7.555 [6.726, 8.236] | 8.294 [7.405, 9.361] | 32.271 [26.007, 36.307] | 19.78 [15.587, 24.141] | 2.62 | 2.09 | 7.26 |  |
| on_hull_single|magnetic_3d | 14 | 0.852 | 1.747 | 3.818 [1.315, 6.73] | 4.724 [2.515, 5.607] | 5.746 [5.02, 5.934] | 3.811 [2.888, 4.645] | 1.0 | 2.2 | 3.12 | < 30: falls back |
| on_hull_single|metal | 39 | 5.251 | 4.962 | 10.989 [5.948, 13.108] | 11.581 [6.73, 14.245] | 23.497 [17.635, 37.117] | 12.536 [9.111, 15.829] | 1.14 | 2.0 | 10.805 |  |
| on_hull_single|pblock_anion | 25 | 4.28 | 1.404 | 3.44 [1.717, 21.88] | 13.861 [3.724, 17.141] | 24.194 [16.0, 28.734] | 12.608 [8.801, 15.778] | 3.67 | 2.0 | 2.799 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 108 | -0.614 | -0.012 | 4.829 [3.847, 6.542] | 5.551 [4.235, 6.378] | 14.369 [8.257, 18.189] | 6.162 [5.087, 7.328] | 1.28 | 1.9 | 4.44 |  |
| polymorph_ambiguous|metal | 234 | 4.263 | 1.955 | 6.04 [4.843, 7.282] | 7.429 [6.503, 9.09] | 21.765 [16.872, 36.123] | 11.784 [9.384, 14.183] | 1.95 | 2.0 | 5.699 |  |
| polymorph_ambiguous|pblock_anion | 354 | 7.224 | 1.076 | 9.291 [7.984, 11.298] | 10.797 [9.378, 12.244] | 39.839 [32.506, 60.529] | 25.804 [19.164, 32.346] | 2.78 | 2.1 | 9.051 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 25f304d75c818f3e728a656787873cad6ec9c9bf32dddd1f59ea6dbfb76cdfc7.
