# ORCHID ESPEI bundle: uncertainty summary

Per folder and output: how many values carry a printed uncertainty, how many have none printed (the method-class floor applies), model-calculated values (budget with the model-class component), calibrated DFT sigmas, and ZPF values (driving-force tolerance); whether the method floor is calibrated from ORCHID or a documented prior; how many values have sigma_effective above the printed sigma, and how many sigmas the weights use are larger than under the rule of 2026-10-23 (printed sigma, ESPEI default where none or below a tenth of it). Distributions are of sigma_effective (the sigma the weight uses), in ESPEI units (J/mol-atom, J/mol-atom/K, activities: J/mol on the chemical potential). Rules: README.md, section "Uncertainties"; floors: experimental/CALIBRATION_EXPERIMENT.md.

| folder | output | values | printed sigma | not printed (method floor) | model (budget) | dft calibrated | ZPF | floor calibrated | floor prior | sigma_eff > printed | sigma raised vs 2026-10-23 | sigma unit | min | q25 | median | q75 | max |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| dft/literature | HM_FORM | 1050 | 0 | 0 | 0 | 1050 | 0 | 0 | 0 | 0 | 0 | J/mol-atom | 3050.0 | 3794.0 | 6280.0 | 6624.0 | 11564.0 |
| dft/mp | HM_FORM | 1218 | 0 | 0 | 0 | 1218 | 0 | 0 | 0 | 0 | 0 | J/mol-atom | 4289.0 | 7506.0 | 9323.0 | 9323.0 | 13515.0 |
| dft/oqmd | HM_FORM | 1218 | 0 | 0 | 0 | 1218 | 0 | 0 | 0 | 0 | 0 | J/mol-atom | 5761.0 | 6537.0 | 6934.0 | 8435.0 | 11501.0 |
| experimental | ACR_CD | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 7 | 0 | 7 | 1 (activity) | 999.9393 | 1000.0036 | 1000.0258 | 1000.0486 | 1000.0718 |
| experimental | ACR_CO | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 10 | 0 | 10 | 1 (activity) | 999.904 | 999.9912 | 1000.0246 | 1000.0705 | 7525.2123 |
| experimental | ACR_CR | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 (activity) | 1000.0068 | 1000.0281 | 1000.0494 | 1000.0707 | 1000.0921 |
| experimental | ACR_CU | 40 | 0 | 40 | 0 | 0 | 0 | 0 | 40 | 0 | 40 | 1 (activity) | 999.8533 | 999.9459 | 999.9847 | 1000.0468 | 7525.2123 |
| experimental | ACR_GE | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 10 | 0 | 10 | 1 (activity) | 999.8974 | 999.9665 | 1000.0245 | 1000.0505 | 7162.9095 |
| experimental | ACR_MO | 11 | 0 | 11 | 0 | 0 | 0 | 0 | 11 | 0 | 11 | 1 (activity) | 999.8607 | 999.9538 | 1000.035 | 1000.1053 | 1000.1409 |
| experimental | ACR_PB | 36 | 0 | 36 | 0 | 0 | 0 | 0 | 36 | 0 | 36 | 1 (activity) | 999.6252 | 999.9438 | 999.9808 | 1000.0305 | 1000.3891 |
| experimental | ACR_SI | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 10 | 0 | 10 | 1 (activity) | 999.8974 | 999.9665 | 1000.0245 | 1000.0505 | 7162.9095 |
| experimental | ACR_TL | 21 | 0 | 21 | 0 | 0 | 0 | 0 | 21 | 0 | 21 | 1 (activity) | 999.9019 | 999.9598 | 999.9898 | 1000.0467 | 1000.0673 |
| experimental | ACR_YB | 13 | 0 | 13 | 0 | 0 | 0 | 0 | 13 | 0 | 13 | 1 (activity) | 999.5398 | 999.9555 | 1000.0073 | 1000.0428 | 1000.1051 |
| experimental | ACR_ZR | 21 | 0 | 21 | 0 | 0 | 0 | 0 | 21 | 0 | 21 | 1 (activity) | 999.5529 | 999.9064 | 999.9509 | 1000.0086 | 1000.071 |
| experimental | CPM | 552 | 0 | 552 | 0 | 0 | 0 | 0 | 552 | 0 | 552 | J/mol-atom/K | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| experimental | GMR | 52 | 16 | 36 | 0 | 0 | 0 | 22 | 30 | 16 | 16 | J/mol-atom | 1000.0 | 1000.0 | 1000.0 | 1100.0 | 2000.0 |
| experimental | HMR | 501 | 235 | 266 | 0 | 0 | 0 | 122 | 379 | 176 | 356 | J/mol-atom | 500.0 | 500.0 | 1000.0 | 3000.0 | 8100.0 |
| experimental | HM_FORM | 437 | 242 | 195 | 0 | 0 | 0 | 381 | 56 | 178 | 373 | J/mol-atom | 1000.0 | 3500.0 | 4100.0 | 4700.0 | 19000.0 |
| experimental | SM | 17 | 3 | 14 | 0 | 0 | 0 | 12 | 5 | 3 | 14 | J/mol-atom/K | 0.2 | 0.5 | 0.5 | 0.5 | 0.5 |
| experimental | SMR | 15 | 1 | 14 | 0 | 0 | 0 | 0 | 15 | 0 | 14 | J/mol-atom/K | 1.0 | 1.0 | 1.0 | 1.0 | 2.0 |
| experimental | SM_FORM | 45 | 19 | 26 | 0 | 0 | 0 | 0 | 45 | 7 | 33 | J/mol-atom/K | 0.5 | 1.0 | 1.0 | 1.3 | 5.4 |
| experimental | ZPF | 1164 | 0 | 0 | 0 | 0 | 1164 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |
| invariants | ZPF | 6019 | 0 | 0 | 0 | 0 | 6019 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |
| model | ACR_CU | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 21 | 0 | 21 | 1 (activity) | 999.9072 | 999.9634 | 1000.0181 | 1000.0375 | 1000.2979 |
| model | ACR_MO | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 11 | 0 | 11 | 1 (activity) | 999.8504 | 999.9157 | 1000.019 | 1000.082 | 1000.1402 |
| model | ACR_ZR | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 21 | 0 | 21 | 1 (activity) | 999.724 | 999.9108 | 999.9586 | 1000.0229 | 1000.2174 |
| model | CPM | 6 | 0 | 0 | 6 | 0 | 0 | 0 | 6 | 0 | 6 | J/mol-atom/K | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| model | GMR | 27 | 0 | 0 | 27 | 0 | 0 | 21 | 6 | 0 | 0 | J/mol-atom | 700.0 | 700.0 | 700.0 | 700.0 | 1000.0 |
| model | HMR | 161 | 0 | 0 | 161 | 0 | 0 | 123 | 38 | 1 | 161 | J/mol-atom | 1000.0 | 3300.0 | 3300.0 | 3300.0 | 3300.0 |
| model | HM_FORM | 295 | 0 | 0 | 295 | 0 | 0 | 295 | 0 | 0 | 295 | J/mol-atom | 3300.0 | 3300.0 | 3300.0 | 3300.0 | 3300.0 |
| model | SM | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 21 | 1 | 21 | J/mol-atom/K | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| model | SMR | 16 | 0 | 0 | 16 | 0 | 0 | 16 | 0 | 0 | 16 | J/mol-atom/K | 3.7 | 3.7 | 3.7 | 3.7 | 3.7 |
| model | SM_FORM | 90 | 0 | 0 | 90 | 0 | 0 | 90 | 0 | 0 | 90 | J/mol-atom/K | 3.7 | 3.7 | 3.7 | 3.7 | 3.7 |
| model | ZPF | 160 | 0 | 0 | 0 | 0 | 160 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |

