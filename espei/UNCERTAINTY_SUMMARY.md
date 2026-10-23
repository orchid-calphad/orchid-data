# ORCHID ESPEI bundle: uncertainty summary

Per folder and output: how many values carry a printed uncertainty, a calibrated DFT sigma, ESPEI's assumed experimental default (not printed), no sigma at all (no default exists, or model-calculated), or are ZPF (driving-force tolerance). Sigma distributions are over values with a printed or calibrated sigma, in the dataset's units (ESPEI units: J/mol-atom, J/mol-atom/K, activity). Rules: README.md, section "Uncertainties".

| folder | output | values | printed | dft calibrated | assumed ESPEI default | none | none (model) | ZPF | sigma unit | min | q25 | median | q75 | max |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| dft/literature | HM_FORM | 1092 | 0 | 1092 | 0 | 0 | 0 | 0 | J/mol-atom | 2793.0 | 3198.0 | 6282.0 | 6820.0 | 11564.0 |
| dft/mp | HM_FORM | 1290 | 0 | 1290 | 0 | 0 | 0 | 0 | J/mol-atom | 4222.0 | 8220.0 | 9575.0 | 9973.0 | 12436.0 |
| dft/oqmd | HM_FORM | 1290 | 0 | 1290 | 0 | 0 | 0 | 0 | J/mol-atom | 4377.0 | 6299.0 | 7708.0 | 9189.0 | 11501.0 |
| experimental | ACR_B | 7 | 0 | 0 | 7 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CD | 7 | 0 | 0 | 7 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CO | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CR | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CU | 41 | 0 | 0 | 41 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_GE | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_MO | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_PB | 36 | 0 | 0 | 36 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_SI | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_TI | 16 | 0 | 0 | 16 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_TL | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_YB | 13 | 0 | 0 | 13 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_ZR | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | CPM | 1241 | 29 | 0 | 1212 | 0 | 0 | 0 | J/mol-atom/K | 0.4 | 0.5 | 0.5 | 0.5 | 6.7 |
| experimental | GMR | 235 | 65 | 0 | 0 | 170 | 0 | 0 | J/mol-atom | 50.0 | 220.0 | 1000.0 | 1000.0 | 5500.0 |
| experimental | HMR | 1559 | 727 | 0 | 832 | 0 | 0 | 0 | J/mol-atom | 0.3 | 383.5 | 1138.0 | 2400.0 | 60000.0 |
| experimental | SM | 139 | 17 | 0 | 122 | 0 | 0 | 0 | J/mol-atom/K | 0.08 | 0.3347 | 0.5 | 0.7 | 6.2 |
| experimental | SMR | 103 | 36 | 0 | 67 | 0 | 0 | 0 | J/mol-atom/K | 0.07 | 0.71 | 1.25 | 1.725 | 6.3 |
| experimental | ZPF | 1323 | 0 | 0 | 0 | 0 | 0 | 1323 |  |  |  |  |  |  |
| invariants | ZPF | 7635 | 0 | 0 | 0 | 0 | 0 | 7635 |  |  |  |  |  |  |
| model | ACR_B | 7 | 0 | 0 | 0 | 0 | 7 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_CU | 21 | 0 | 0 | 0 | 0 | 21 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_MO | 11 | 0 | 0 | 0 | 0 | 11 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_TI | 16 | 0 | 0 | 0 | 0 | 16 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_ZR | 21 | 0 | 0 | 0 | 0 | 21 | 0 | 1 (activity) |  |  |  |  |  |
| model | CPM | 150 | 0 | 0 | 0 | 0 | 150 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | GMR | 215 | 0 | 0 | 0 | 0 | 215 | 0 | J/mol-atom |  |  |  |  |  |
| model | HMR | 737 | 0 | 0 | 0 | 0 | 737 | 0 | J/mol-atom |  |  |  |  |  |
| model | SM | 198 | 0 | 0 | 0 | 0 | 198 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | SMR | 129 | 0 | 0 | 0 | 0 | 129 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | ZPF | 162 | 0 | 0 | 0 | 0 | 0 | 162 |  |  |  |  |  |  |

