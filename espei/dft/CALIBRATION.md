# DFT formation-enthalpy uncertainty: calibration

Calibrated from ORCHID's own DFT-vs-experiment pairs (`literature/dft_parity.json`, default subset: experimental, accepted, signed, not magnitude-suspect; residual = DFT - experiment, kJ/mol-atom). Materials Project and OQMD are calibrated separately (different energy references). Literature DFT: each accepted literature DFT HM_FORM value (kJ/mol-atom, binary) paired with the median experimental value of the same compound (same reduced composition) in that subset.

## Method

- bias: mean and median residual (**recorded, not applied** to any value);
- robust sigma = 1.4826 x MAD (median absolute deviation about the median); 68 / 95 % quantiles of |residual|; RMSE;
- 95% confidence intervals: 1000 bootstrap resamples of the pairs (fixed seeds), percentile intervals;
- strata: match quality (`on_hull_single` DFT entry on the hull and the only entry at its composition; `polymorph_ambiguous` on the hull, several entries (polymorphs) at the composition; `above_hull` lowest DFT entry at the composition lies more than 1 meV/atom (0.0965 kJ/mol-atom, the numerical precision of the DFT energies) above the hull) x chemistry (`metal` all-metal intermetallic (none of the elements below); `pblock_anion` contains a p-block / anion element (H, B, C, N, O, F, Si, P, S, Se, Te, As, Sb, halogens); `magnetic_3d` contains Cr, Mn, Fe, Co or Ni (and no p-block / anion element)); chemistry precedence: p-block / anion, then magnetic 3d, then all-metal; single-factor strata are listed too;
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
| above_hull|magnetic_3d | 36 | 7.848 | 5.62 | 4.534 [2.463, 7.352] | 8.669 [5.62, 12.888] | 20.498 [13.166, 31.424] | 10.506 [7.164, 13.899] | 2.32 | 1.05 | 4.411 |  |
| above_hull|metal | 122 | 8.18 | 6.556 | 7.626 [6.064, 8.728] | 10.462 [8.391, 12.104] | 31.446 [21.551, 39.009] | 13.723 [11.41, 16.3] | 1.8 | 2.0 | 7.359 |  |
| above_hull|pblock_anion | 68 | 7.701 | 9.8 | 14.466 [12.115, 18.773] | 19.003 [16.06, 22.444] | 31.539 [25.335, 44.709] | 17.889 [15.094, 20.638] | 1.24 | 3.3 | 14.085 |  |
| chem:magnetic_3d | 191 | 1.125 | 1.748 | 4.993 [3.919, 6.019] | 5.433 [4.655, 6.49] | 14.396 [12.804, 20.304] | 7.345 [6.176, 8.559] | 1.47 | 1.5 | 4.762 |  |
| chem:metal | 480 | 7.434 | 5.639 | 8.861 [7.554, 9.338] | 10.423 [9.453, 11.734] | 30.857 [25.509, 33.618] | 13.939 [12.366, 15.532] | 1.57 | 2.0 | 8.632 |  |
| chem:pblock_anion | 528 | 2.053 | 0.277 | 12.216 [10.649, 14.512] | 14.729 [13.28, 16.494] | 39.039 [35.572, 48.082] | 24.409 [19.628, 29.677] | 2.0 | 2.1 | 12.034 |  |
| match:above_hull | 226 | 7.983 | 6.259 | 8.303 [6.913, 9.808] | 12.564 [11.104, 15.131] | 31.015 [25.799, 36.087] | 14.681 [13.007, 16.545] | 1.77 | 2.0 | 8.059 |  |
| match:on_hull_single | 461 | 4.194 | 2.889 | 7.911 [6.823, 9.033] | 9.649 [8.102, 11.2] | 29.476 [25.489, 31.911] | 13.115 [11.783, 14.437] | 1.66 | 2.0 | 7.654 |  |
| match:polymorph_ambiguous | 512 | 2.206 | 0.512 | 8.875 [7.538, 11.244] | 11.922 [10.099, 13.226] | 37.189 [33.912, 49.48] | 23.805 [18.674, 28.966] | 2.68 | 2.0 | 8.647 |  |
| on_hull_single|magnetic_3d | 73 | 1.128 | 0.92 | 4.727 [3.662, 6.869] | 5.486 [4.18, 6.477] | 11.991 [8.196, 14.396] | 5.736 [4.587, 6.938] | 1.21 | 2.0 | 4.283 |  |
| on_hull_single|metal | 259 | 6.643 | 5.075 | 9.323 [7.828, 10.47] | 10.648 [9.121, 11.872] | 29.341 [25.489, 31.489] | 13.195 [11.507, 14.945] | 1.42 | 2.0 | 9.106 |  |
| on_hull_single|pblock_anion | 129 | 1.013 | 0.955 | 9.188 [6.449, 12.414] | 12.097 [8.447, 14.036] | 36.17 [27.186, 41.407] | 15.701 [12.946, 18.438] | 1.71 | 2.25 | 8.908 |  |
| polymorph_ambiguous|magnetic_3d | 82 | -1.83 | -0.137 | 5.414 [3.61, 6.589] | 4.94 [3.849, 5.412] | 16.498 [10.939, 20.314] | 6.921 [5.372, 8.318] | 1.28 | 1.6 | 5.172 |  |
| polymorph_ambiguous|metal | 99 | 8.588 | 4.852 | 7.303 [5.391, 10.443] | 10.132 [7.271, 12.998] | 35.228 [20.436, 48.057] | 15.953 [11.724, 21.067] | 2.18 | 2.0 | 7.024 |  |
| polymorph_ambiguous|pblock_anion | 331 | 1.297 | -1.156 | 11.968 [9.546, 14.259] | 14.734 [12.169, 16.653] | 47.194 [36.138, 66.585] | 28.082 [21.616, 35.232] | 2.35 | 2.09 | 11.784 |  |

## oqmd

| stratum | n | bias mean | bias median | robust sigma [95% CI] | q68 |res| | q95 |res| | RMSE | RMSE/sigma | sigma_exp | sigma deconv. | note |
|---|---:|---:|---:|---|---|---|---|---:|---:|---:|---|
| all | 1251 | 4.947 | 2.364 | 7.655 [6.947, 8.536] | 9.094 [8.388, 10.074] | 28.955 [26.007, 34.19] | 17.172 [14.402, 19.965] | 2.24 | 2.0 | 7.389 |  |
| above_hull|magnetic_3d | 60 | 5.784 | 3.076 | 3.511 [2.1, 5.74] | 6.943 [4.337, 9.208] | 25.597 [15.949, 25.928] | 9.908 [7.353, 12.235] | 2.82 | 1.05 | 3.35 |  |
| above_hull|metal | 152 | 6.737 | 4.806 | 8.024 [6.514, 9.751] | 10.203 [8.519, 11.774] | 25.605 [18.906, 42.489] | 12.967 [10.519, 15.233] | 1.62 | 2.0 | 7.771 |  |
| above_hull|pblock_anion | 106 | 5.598 | 4.117 | 10.559 [7.698, 14.567] | 13.662 [10.287, 18.474] | 31.997 [25.059, 40.986] | 15.177 [12.932, 17.538] | 1.44 | 2.0 | 10.368 |  |
| chem:magnetic_3d | 220 | 0.629 | 1.238 | 5.062 [4.329, 6.368] | 5.902 [5.281, 6.402] | 19.061 [15.668, 23.168] | 7.989 [6.884, 8.968] | 1.58 | 1.6 | 4.802 |  |
| chem:metal | 485 | 5.541 | 3.469 | 7.669 [6.596, 8.644] | 9.329 [8.259, 10.244] | 26.556 [22.752, 29.387] | 12.435 [11.033, 13.921] | 1.62 | 2.0 | 7.404 |  |
| chem:pblock_anion | 546 | 6.16 | 2.087 | 9.424 [8.045, 10.883] | 11.081 [10.052, 12.244] | 36.287 [31.685, 47.347] | 22.639 [17.608, 27.702] | 2.4 | 2.1 | 9.187 |  |
| match:above_hull | 318 | 6.178 | 4.149 | 7.933 [6.565, 9.337] | 10.291 [8.899, 11.774] | 26.761 [25.092, 32.283] | 13.254 [11.737, 14.616] | 1.67 | 2.0 | 7.677 |  |
| match:on_hull_single | 86 | 4.035 | 2.505 | 7.171 [4.64, 10.01] | 10.041 [5.407, 13.861] | 23.793 [17.996, 29.105] | 11.256 [9.049, 13.269] | 1.57 | 2.1 | 6.857 |  |
| match:polymorph_ambiguous | 847 | 4.578 | 1.213 | 7.549 [6.977, 8.199] | 8.42 [7.55, 9.528] | 30.847 [26.689, 36.287] | 18.886 [15.318, 22.856] | 2.5 | 2.0 | 7.279 |  |
| on_hull_single|magnetic_3d | 17 | 0.946 | 0.998 | 3.035 [1.179, 6.457] | 4.192 [2.515, 5.407] | 5.703 [4.927, 5.934] | 3.571 [2.702, 4.325] | 1.18 | 3.0 | 0.46 | < 30: falls back |
| on_hull_single|metal | 42 | 4.885 | 4.909 | 10.627 [6.012, 12.829] | 11.358 [6.771, 14.131] | 22.86 [17.429, 36.723] | 12.152 [8.918, 15.086] | 1.14 | 2.0 | 10.437 |  |
| on_hull_single|pblock_anion | 27 | 4.658 | 1.404 | 7.149 [1.957, 21.88] | 13.862 [3.626, 18.543] | 24.183 [16.534, 28.734] | 12.877 [9.579, 15.837] | 1.8 | 2.0 | 6.864 | < 30: falls back |
| polymorph_ambiguous|magnetic_3d | 143 | -1.572 | -0.905 | 6.116 [4.424, 6.937] | 5.925 [4.8, 6.732] | 16.147 [13.27, 20.838] | 7.448 [6.273, 8.544] | 1.22 | 1.9 | 5.813 |  |
| polymorph_ambiguous|metal | 291 | 5.011 | 2.085 | 6.537 [5.429, 7.821] | 8.327 [6.939, 9.699] | 27.218 [21.403, 30.276] | 12.19 [10.271, 14.112] | 1.86 | 2.0 | 6.224 |  |
| polymorph_ambiguous|pblock_anion | 413 | 6.403 | 1.145 | 8.435 [7.816, 10.51] | 10.473 [9.025, 11.542] | 41.868 [34.258, 57.929] | 24.65 [18.702, 30.416] | 2.92 | 2.25 | 8.129 |  |

Values in kJ/mol-atom. Leave-system-out sigmas used for the weights: `CALIBRATION.json`, `lso` (`<source>|<stratum>|<system>`). Pairs file: dft_parity.json inputs literature sha256 befef97c22dd57323e16f2c3f392d9ca737645c71b70ca8b26b0fb9a6570337f.
