# ORCHID ESPEI bundle: uncertainty summary

Per folder and output: how many values carry a printed uncertainty, how many have none printed (the method-class floor applies), model-calculated values (budget with the model-class component), calibrated DFT sigmas, and ZPF values (driving-force tolerance); whether the method floor is calibrated from ORCHID or a documented prior; how many values have sigma_effective above the printed sigma, and how many sigmas the weights use are larger than under the rule of 2026-10-23 (printed sigma, ESPEI default where none or below a tenth of it). Distributions are of sigma_effective (the sigma the weight uses), in ESPEI units (J/mol-atom, J/mol-atom/K, activities: J/mol on the chemical potential). Rules: README.md, section "Uncertainties"; floors: experimental/CALIBRATION_EXPERIMENT.md.

| folder | output | values | printed sigma | not printed (method floor) | model (budget) | dft calibrated | ZPF | floor calibrated | floor prior | sigma_eff > printed | sigma raised vs 2026-10-23 | sigma unit | min | q25 | median | q75 | max |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| dft/literature | HM_FORM | 1886 | 0 | 0 | 0 | 1886 | 0 | 0 | 0 | 0 | 0 | J/mol-atom | 2901.0 | 4442.0 | 7726.0 | 8346.0 | 12165.0 |
| dft/mp | HM_FORM | 1251 | 0 | 0 | 0 | 1251 | 0 | 0 | 0 | 0 | 0 | J/mol-atom | 4397.0 | 6183.0 | 9154.0 | 9154.0 | 11468.0 |
| dft/oqmd | HM_FORM | 1251 | 0 | 0 | 0 | 1251 | 0 | 0 | 0 | 0 | 0 | J/mol-atom | 4386.0 | 7042.0 | 7379.0 | 8067.0 | 9524.0 |
| experimental | ACR_CD | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 (activity) | 2899.2272 | 2899.4808 | 2899.9191 | 2900.48 | 2900.6931 |
| experimental | ACR_CO | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 1 (activity) | 2899.0572 | 2899.3424 | 2899.7339 | 2900.1703 | 2900.8997 |
| experimental | ACR_CR | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 (activity) | 2900.0197 | 2900.0232 | 2900.0268 | 2900.0303 | 2900.0339 |
| experimental | ACR_CU | 40 | 0 | 40 | 0 | 0 | 0 | 0 | 0 | 0 | 40 | 1 (activity) | 2898.9489 | 2899.5199 | 2899.8817 | 2900.0733 | 2901.1674 |
| experimental | ACR_GE | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 1 (activity) | 2898.7804 | 2899.8961 | 2900.0219 | 2900.4478 | 2900.9784 |
| experimental | ACR_MO | 11 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 1 (activity) | 2899.8742 | 2899.9325 | 2899.9794 | 2900.0796 | 2901.2376 |
| experimental | ACR_PB | 36 | 0 | 36 | 0 | 0 | 0 | 0 | 0 | 0 | 36 | 1 (activity) | 2899.1479 | 2899.6688 | 2899.9744 | 2900.3949 | 2900.6493 |
| experimental | ACR_SI | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 1 (activity) | 2898.7804 | 2899.8961 | 2900.0219 | 2900.4478 | 2900.9784 |
| experimental | ACR_TL | 21 | 0 | 21 | 0 | 0 | 0 | 0 | 0 | 0 | 21 | 1 (activity) | 2898.9618 | 2899.4317 | 2900.0484 | 2900.3829 | 2900.8749 |
| experimental | ACR_YB | 13 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 1 (activity) | 2899.6401 | 2899.7278 | 2900.058 | 2900.2218 | 2900.7497 |
| experimental | ACR_ZR | 21 | 0 | 21 | 0 | 0 | 0 | 0 | 0 | 0 | 21 | 1 (activity) | 2899.1879 | 2899.9849 | 2900.1625 | 2900.3215 | 2900.9534 |
| experimental | CPM | 565 | 0 | 565 | 0 | 0 | 0 | 0 | 0 | 0 | 565 | J/mol-atom/K | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 |
| experimental | GMR | 40 | 8 | 32 | 0 | 0 | 0 | 14 | 9 | 8 | 8 | J/mol-atom | 1000.0 | 1200.0 | 1200.0 | 1400.0 | 2000.0 |
| experimental | HMR | 491 | 233 | 258 | 0 | 0 | 0 | 101 | 369 | 174 | 346 | J/mol-atom | 500.0 | 500.0 | 1000.0 | 1676.5 | 10000.0 |
| experimental | HM_FORM | 440 | 245 | 195 | 0 | 0 | 0 | 357 | 13 | 181 | 376 | J/mol-atom | 1000.0 | 3200.0 | 3500.0 | 4200.0 | 13200.0 |
| experimental | SM | 11 | 0 | 11 | 0 | 0 | 0 | 9 | 0 | 0 | 11 | J/mol-atom/K | 0.6 | 0.6 | 0.6 | 0.6 | 1.0 |
| experimental | SMR | 15 | 1 | 14 | 0 | 0 | 0 | 0 | 15 | 0 | 14 | J/mol-atom/K | 1.0 | 1.0 | 1.0 | 1.0 | 2.0 |
| experimental | SM_FORM | 42 | 19 | 23 | 0 | 0 | 0 | 0 | 42 | 7 | 30 | J/mol-atom/K | 0.5 | 1.0 | 1.0 | 1.55 | 5.4 |
| experimental | ZPF | 1145 | 0 | 0 | 0 | 0 | 1145 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |
| invariants | ZPF | 5589 | 0 | 0 | 0 | 0 | 5589 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |
| model | ACR_CU | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 21 | 0 | 21 | 1 (activity) | 999.9072 | 999.9634 | 1000.0181 | 1000.0375 | 1000.2979 |
| model | ACR_MO | 11 | 0 | 0 | 11 | 0 | 0 | 0 | 11 | 0 | 11 | 1 (activity) | 999.8504 | 999.9157 | 1000.019 | 1000.082 | 1000.1402 |
| model | ACR_ZR | 21 | 0 | 0 | 21 | 0 | 0 | 0 | 21 | 0 | 21 | 1 (activity) | 999.724 | 999.9108 | 999.9586 | 1000.0229 | 1000.2174 |
| model | CPM | 6 | 0 | 0 | 6 | 0 | 0 | 0 | 6 | 0 | 6 | J/mol-atom/K | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| model | GMR | 17 | 0 | 0 | 17 | 0 | 0 | 11 | 6 | 0 | 0 | J/mol-atom | 700.0 | 700.0 | 700.0 | 1000.0 | 1000.0 |
| model | HMR | 151 | 0 | 0 | 151 | 0 | 0 | 113 | 38 | 1 | 151 | J/mol-atom | 1000.0 | 2200.0 | 3400.0 | 3400.0 | 3400.0 |
| model | HM_FORM | 301 | 0 | 0 | 301 | 0 | 0 | 301 | 0 | 0 | 301 | J/mol-atom | 3400.0 | 3400.0 | 3400.0 | 3400.0 | 3400.0 |
| model | SM | 18 | 0 | 0 | 18 | 0 | 0 | 0 | 18 | 0 | 18 | J/mol-atom/K | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| model | SMR | 14 | 0 | 0 | 14 | 0 | 0 | 10 | 4 | 0 | 14 | J/mol-atom/K | 1.0 | 1.575 | 3.3 | 3.3 | 3.3 |
| model | SM_FORM | 62 | 0 | 0 | 62 | 0 | 0 | 62 | 0 | 0 | 62 | J/mol-atom/K | 3.3 | 3.3 | 3.3 | 3.3 | 3.3 |
| model | ZPF | 161 | 0 | 0 | 0 | 0 | 161 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |

