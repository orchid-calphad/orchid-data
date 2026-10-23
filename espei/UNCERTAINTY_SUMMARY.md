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
| experimental | ACR_CR | 4 | 0 | 0 | 4 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CU | 62 | 0 | 0 | 62 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_GE | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_MO | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_PB | 72 | 0 | 0 | 72 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_SI | 22 | 0 | 0 | 22 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_TI | 24 | 0 | 0 | 24 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_TL | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_YB | 13 | 0 | 0 | 13 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_ZR | 42 | 0 | 0 | 42 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | CPM | 1247 | 29 | 0 | 1218 | 0 | 0 | 0 | J/mol-atom/K | 0.4 | 0.5 | 0.5 | 0.5 | 6.7 |
| experimental | GMR | 274 | 74 | 0 | 0 | 200 | 0 | 0 | J/mol-atom | 50.0 | 226.0 | 1000.0 | 1000.0 | 5500.0 |
| experimental | HMR | 2049 | 1033 | 0 | 1016 | 0 | 0 | 0 | J/mol-atom | 0.3 | 380.0 | 1149.0 | 2400.0 | 60000.0 |
| experimental | SM | 185 | 17 | 0 | 168 | 0 | 0 | 0 | J/mol-atom/K | 0.08 | 0.3347 | 0.5 | 0.7 | 6.2 |
| experimental | SMR | 122 | 42 | 0 | 80 | 0 | 0 | 0 | J/mol-atom/K | 0.07 | 0.785 | 1.3 | 4.4 | 6.3 |
| experimental | ZPF | 1355 | 0 | 0 | 0 | 0 | 0 | 1355 |  |  |  |  |  |  |
| invariants | ZPF | 7888 | 0 | 0 | 0 | 0 | 0 | 7888 |  |  |  |  |  |  |
| model | ACR_B | 7 | 0 | 0 | 0 | 0 | 7 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_CU | 42 | 0 | 0 | 0 | 0 | 42 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_MO | 11 | 0 | 0 | 0 | 0 | 11 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_TI | 24 | 0 | 0 | 0 | 0 | 24 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_ZR | 42 | 0 | 0 | 0 | 0 | 42 | 0 | 1 (activity) |  |  |  |  |  |
| model | CPM | 230 | 0 | 0 | 0 | 0 | 230 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | GMR | 248 | 0 | 0 | 0 | 0 | 248 | 0 | J/mol-atom |  |  |  |  |  |
| model | HMR | 1058 | 0 | 0 | 0 | 0 | 1058 | 0 | J/mol-atom |  |  |  |  |  |
| model | SM | 300 | 0 | 0 | 0 | 0 | 300 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | SMR | 182 | 0 | 0 | 0 | 0 | 182 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | ZPF | 166 | 0 | 0 | 0 | 0 | 0 | 166 |  |  |  |  |  |  |

