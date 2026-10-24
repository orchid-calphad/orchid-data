# ORCHID ESPEI bundle: uncertainty summary

Per folder and output: how many values carry a printed uncertainty, a calibrated DFT sigma, ESPEI's assumed experimental default (not printed), no sigma at all (no default exists, or model-calculated), or are ZPF (driving-force tolerance). Sigma distributions are over values with a printed or calibrated sigma, in the dataset's units (ESPEI units: J/mol-atom, J/mol-atom/K, activity). Rules: README.md, section "Uncertainties".

| folder | output | values | printed | dft calibrated | assumed ESPEI default | none | none (model) | ZPF | sigma unit | min | q25 | median | q75 | max |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| dft/literature | HM_FORM | 1051 | 0 | 1051 | 0 | 0 | 0 | 0 | J/mol-atom | 2793.0 | 3198.0 | 6282.0 | 6769.0 | 11564.0 |
| dft/mp | HM_FORM | 1218 | 0 | 1218 | 0 | 0 | 0 | 0 | J/mol-atom | 4222.0 | 7116.0 | 9575.0 | 9847.0 | 12436.0 |
| dft/oqmd | HM_FORM | 1218 | 0 | 1218 | 0 | 0 | 0 | 0 | J/mol-atom | 4377.0 | 6299.0 | 6549.0 | 9189.0 | 11501.0 |
| experimental | ACR_CD | 7 | 0 | 0 | 7 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CO | 10 | 0 | 0 | 10 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CR | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_CU | 40 | 0 | 0 | 40 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_GE | 10 | 0 | 0 | 10 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_MO | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_PB | 36 | 0 | 0 | 36 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_SI | 10 | 0 | 0 | 10 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_TL | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_YB | 13 | 0 | 0 | 13 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | ACR_ZR | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 1 (activity) |  |  |  |  |  |
| experimental | CPM | 552 | 0 | 0 | 552 | 0 | 0 | 0 | J/mol-atom/K |  |  |  |  |  |
| experimental | GMR | 38 | 16 | 0 | 0 | 22 | 0 | 0 | J/mol-atom | 70.0 | 298.0 | 717.5 | 1000.0 | 1000.0 |
| experimental | HMR | 519 | 230 | 0 | 289 | 0 | 0 | 0 | J/mol-atom | 11.0 | 200.0 | 483.5 | 1000.0 | 5100.0 |
| experimental | HM_FORM | 398 | 222 | 0 | 176 | 0 | 0 | 0 | J/mol-atom | 0.5 | 1000.0 | 2000.0 | 3460.0 | 19000.0 |
| experimental | SM | 14 | 3 | 0 | 11 | 0 | 0 | 0 | J/mol-atom/K | 0.08 | 0.165 | 0.25 | 0.325 | 0.4 |
| experimental | SMR | 15 | 1 | 0 | 14 | 0 | 0 | 0 | J/mol-atom/K | 1.3 | 1.3 | 1.3 | 1.3 | 1.3 |
| experimental | SM_FORM | 39 | 21 | 0 | 18 | 0 | 0 | 0 | J/mol-atom/K | 0.08 | 0.31 | 0.9 | 1.3 | 1.8 |
| experimental | ZPF | 1167 | 0 | 0 | 0 | 0 | 0 | 1167 |  |  |  |  |  |  |
| invariants | ZPF | 6086 | 0 | 0 | 0 | 0 | 0 | 6086 |  |  |  |  |  |  |
| model | ACR_CU | 21 | 0 | 0 | 0 | 0 | 21 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_MO | 11 | 0 | 0 | 0 | 0 | 11 | 0 | 1 (activity) |  |  |  |  |  |
| model | ACR_ZR | 21 | 0 | 0 | 0 | 0 | 21 | 0 | 1 (activity) |  |  |  |  |  |
| model | CPM | 5 | 0 | 0 | 0 | 0 | 5 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | GMR | 21 | 0 | 0 | 0 | 0 | 21 | 0 | J/mol-atom |  |  |  |  |  |
| model | HMR | 148 | 0 | 0 | 0 | 0 | 148 | 0 | J/mol-atom |  |  |  |  |  |
| model | HM_FORM | 250 | 0 | 0 | 0 | 0 | 250 | 0 | J/mol-atom |  |  |  |  |  |
| model | SM | 17 | 0 | 0 | 0 | 0 | 17 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | SMR | 15 | 0 | 0 | 0 | 0 | 15 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | SM_FORM | 64 | 0 | 0 | 0 | 0 | 64 | 0 | J/mol-atom/K |  |  |  |  |  |
| model | ZPF | 160 | 0 | 0 | 0 | 0 | 0 | 160 |  |  |  |  |  |  |

