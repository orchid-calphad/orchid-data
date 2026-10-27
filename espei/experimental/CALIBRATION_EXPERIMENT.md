# ORCHID uncertainty budget: method-floor calibration

Version: orchid-uncertainty-calibration 2026-10-24 (audit round 2). Machine-readable: `UNCERTAINTY_CALIBRATION.json` (the same file is copied to `espei/experimental/CALIBRATION_EXPERIMENT.json`). Every record carries `uncertainty_budget` (SCHEMA.md).

## Rule

sigma_effective = max( sqrt( max(sigma_printed, sigma_reading, sigma_method)^2 + sigma_composition^2 + sigma_conversion^2 ), sigma_scatter ); absent components drop out. The method floor is a between-study scatter and already contains each study's statistical error, so it is not added to the printed sigma in quadrature (no double counting): the larger of the two is used. The composition offset and the conversion are independent of the measurement and are added in quadrature. The scatter of a page-checked mutually inconsistent group replaces the result when larger. The reading resolution alone is not an uncertainty estimate: without a printed sigma, a method floor or a group scatter, sigma_effective is null (with the reason).

## Calibration

- estimator: robust sigma = 1.4826 x median|d| / sqrt(2) over pairs of independent same-class measurements of one state (zero-mean differences); 95 % percentile bootstrap over states; every state carries the same weight (state-weighted median), so a compound measured by many studies does not dominate;
- independence: one value per primary source and state (origin.measured_in, else the single cited source, else the reporting paper for its own work, else the reporting paper marked unattributed; median of the source's values); identical values from different sources are counted once (one measurement re-listed);
- sample: experimental, extraction_accepted, no blocking flag (unsigned_in_print, magnitude_suspect, system_mismatch, source_disputed); values convertible to the value type's canonical unit; formation quantities on a per-atom basis only; formation-quantity pairs whose ratio is within 3 % of the formula's atom count are a per-formula / per-atom basis error of one reading and are left out;
- a class is calibrated with at least 20 pairs from at least 10 states; otherwise the documented prior (sources below) is used (basis `prior`);
- floor = robust sigma rounded up to the value type's step, never below the minimum (ESPEI's experimental default for energies, entropies and activities);
- model-calculated values: robust deviation of the model class from experiment for value types whose state key identifies one state (formation quantities, invariant temperatures and compositions, lattice parameters), else a prior; DFT values: the calibrated sigma_DFT of `espei/dft/CALIBRATION.json` (literature DFT, by chemistry stratum) for formation enthalpies, documented priors otherwise.

| value type | canonical unit | minimum | label |
|---|---|---:|---|
| HM_FORM | kJ/mol-atom | 0.5 | formation enthalpy |
| GM_FORM | kJ/mol-atom | 0.5 | formation Gibbs energy |
| SM_FORM | J/K/mol-atom | 0.2 | formation entropy |
| H_MIX_PARTIAL | kJ/mol | 0.5 | mixing / partial / transformation enthalpy |
| G_MIX_PARTIAL | kJ/mol | 0.5 | mixing / partial Gibbs energy, chemical potential |
| S_MIX_PARTIAL | J/K/mol | 0.2 | mixing / partial / excess entropy |
| S_ABS | J/K/mol | 0.2 | absolute entropy, entropy of fusion / transformation |
| CPM | J/K/mol | 0.2 | heat capacity |
| HEAT_CONTENT | kJ/mol | 0.5 | heat content H(T)-H(298) |
| ACTIVITY | kJ/mol (chemical potential) | 0.5 | activity (floor on mu = RT ln a) |
| EMF | mV | 0.1 | electromotive force |
| T_INVARIANT | K | 1 | invariant-reaction temperature |
| T_TRANSITION | K | 1 | transition / liquidus / solidus temperature |
| T_CONDITION | K | 1 | equilibration temperature of a phase-equilibrium observation |
| X_PHASE | mole fraction | 0.001 | phase composition (tie-line / boundary / invariant) |
| LATTICE_LENGTH | relative (fraction of the value) | 0.0002 | lattice parameter |
| LATTICE_ANGLE | degree | 0.01 | lattice angle |
| VOLUME | relative (fraction of the value) | 0.0005 | cell / molar volume |

## Floors per value type and method class

| value type | method class | pairs | states | basis | robust sigma | 95 % CI | floor | unit |
|---|---|---:|---:|---|---:|---|---:|---|
| HM_FORM | combustion_calorimetry | 15 | 4 | cleaned_below_threshold (kubaschewski) | 0.8806 | 0.08806-5.33 | 1 | kJ/mol-atom |
| HM_FORM | dsc_dta | 2 | 2 | prior (kubaschewski) |  |  | 2 | kJ/mol-atom |
| HM_FORM | emf | 17 | 8 | cleaned_below_threshold (kubaschewski) | 4.566 | 1.887-14.82 | 4.6 | kJ/mol-atom |
| HM_FORM | experimental_unspecified | 29 | 9 | cleaned_below_threshold (kubaschewski) | 4.026 | 1.992-9.33 | 4.1 | kJ/mol-atom |
| HM_FORM | kems_vapour | 20 | 15 | calibrated | 4.193 | 1.153-7.653 | 4.2 | kJ/mol-atom |
| HM_FORM | kems_vapour_second_law | 1 | 1 | prior (drowart2005) |  |  | 3 | kJ/mol-atom |
| HM_FORM | kems_vapour_third_law | 0 | 0 | prior (drowart2005) |  |  | 2 | kJ/mol-atom |
| HM_FORM | solution_reaction_calorimetry | 80 | 47 | calibrated | 3.145 | 2.202-4.602 | 3.2 | kJ/mol-atom |
| HM_FORM | unknown | 290 | 98 | calibrated | 3.46 | 2.411-4.298 | 3.5 | kJ/mol-atom |
| HM_FORM | model_calculated (vs experiment) | 2030 | 359 | calibrated | 3.855 | 3.158-4.581 | 3.9 | kJ/mol-atom |
| GM_FORM | emf | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol-atom |
| GM_FORM | experimental_unspecified | 2 | 2 | prior (kubaschewski) |  |  | 2 | kJ/mol-atom |
| GM_FORM | kems_vapour | 2 | 2 | prior (drowart2005) |  |  | 2 | kJ/mol-atom |
| GM_FORM | kems_vapour_third_law | 0 | 0 | prior (drowart2005) |  |  | 2 | kJ/mol-atom |
| GM_FORM | unknown | 37 | 17 | calibrated | 1.122 | 0.6605-2.097 | 1.2 | kJ/mol-atom |
| GM_FORM | model_calculated (vs experiment) | 211 | 153 | calibrated | 0.682 | 0.593-0.8896 | 0.7 | kJ/mol-atom |
| SM_FORM | emf | 3 | 1 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | equilibration_other | 1 | 1 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | heat_content_calorimetry | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol-atom |
| SM_FORM | kems_vapour | 1 | 1 | prior (drowart2005) |  |  | 2 | J/K/mol-atom |
| SM_FORM | kems_vapour_second_law | 0 | 0 | prior (drowart2005) |  |  | 3 | J/K/mol-atom |
| SM_FORM | unknown | 4 | 4 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | model_calculated (vs experiment) | 118 | 42 | calibrated | 3.232 | 1.938-4.144 | 3.3 | J/K/mol-atom |
| H_MIX_PARTIAL | experimental_unspecified | 6 | 1 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| H_MIX_PARTIAL | solution_reaction_calorimetry | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol |
| H_MIX_PARTIAL | unknown | 1 | 1 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| H_MIX_PARTIAL | model_calculated (vs experiment) | 133 | 57 | prior |  |  | 1 | kJ/mol |
| G_MIX_PARTIAL | emf | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol |
| G_MIX_PARTIAL | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| G_MIX_PARTIAL | unknown | 13 | 13 | cleaned_below_threshold (kubaschewski) | 1.319 | 1.086-1.697 | 1.4 | kJ/mol |
| G_MIX_PARTIAL | model_calculated (vs experiment) | 94 | 70 | prior |  |  | 1 | kJ/mol |
| S_MIX_PARTIAL | emf | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_MIX_PARTIAL | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | J/K/mol |
| S_MIX_PARTIAL | unknown | 0 | 0 | prior (kubaschewski) |  |  | 1 | J/K/mol |
| S_MIX_PARTIAL | model_calculated (vs experiment) | 14 | 8 | prior |  |  | 1 | J/K/mol |
| S_ABS | emf | 45 | 1 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_ABS | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_ABS | heat_content_calorimetry | 19 | 9 | cleaned_below_threshold (espei) | 0.9121 | 0.07339-1.929 | 1 | J/K/mol |
| S_ABS | kems_vapour | 4 | 4 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_ABS | unknown | 77 | 20 | calibrated | 0.6571 | 0.2851-1.174 | 0.7 | J/K/mol |
| S_ABS | model_calculated (vs experiment) | 260 | 80 | prior |  |  | 1 | J/K/mol |
| CPM | dsc_dta | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| CPM | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| CPM | heat_content_calorimetry | 43 | 8 | cleaned_below_threshold (espei) | 0.4193 | 0.1363-1.856 | 0.5 | J/K/mol |
| CPM | unknown | 6 | 6 | cleaned_below_threshold (kubaschewski) | 0.5776 | 0.2563-1.118 | 0.6 | J/K/mol |
| CPM | model_calculated (vs experiment) | 225 | 89 | prior |  |  | 1 | J/K/mol |
| HEAT_CONTENT | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| HEAT_CONTENT | heat_content_calorimetry | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol |
| HEAT_CONTENT | unknown | 161 | 76 | calibrated | 0.07967 | 0.04822-0.1326 | 0.5 | kJ/mol |
| HEAT_CONTENT | model_calculated (vs experiment) | 246 | 133 | prior |  |  | 1 | kJ/mol |
| ACTIVITY | emf | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol (chemical potential) |
| ACTIVITY | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol (chemical potential) |
| ACTIVITY | unknown | 9 | 9 | cleaned_below_threshold (kubaschewski) | 2.891 | 0.7333-4.29 | 2.9 | kJ/mol (chemical potential) |
| ACTIVITY | model_calculated (vs experiment) | 73 | 67 | prior |  |  | 1 | kJ/mol (chemical potential) |
| EMF | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 1 | mV |
| EMF | unknown | 0 | 0 | prior (orchid_assumed) |  |  | 1 | mV |
| EMF | model_calculated (vs experiment) | 0 | 0 | prior |  |  | 2 | mV |
| T_INVARIANT | emf | 1 | 1 | prior (orchid_assumed) |  |  | 10 | K |
| T_INVARIANT | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 10 | K |
| T_INVARIANT | thermal_analysis | 0 | 0 | prior (orchid_assumed) |  |  | 5 | K |
| T_INVARIANT | unknown | 4912 | 1680 | calibrated | 10.48 | 9.435-10.48 | 11 | K |
| T_INVARIANT | model_calculated (vs experiment) | 14146 | 5377 | calibrated | 3.707 | 3.113-4.3 | 4 | K |
| T_TRANSITION | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 10 | K |
| T_TRANSITION | thermal_analysis | 9 | 4 | cleaned_below_threshold (orchid_assumed) | 3.145 | 2.097-58.18 | 5 | K |
| T_TRANSITION | unknown | 274 | 53 | calibrated | 15.73 | 10.48-26.21 | 16 | K |
| T_TRANSITION | model_calculated (vs experiment) | 129 | 68 | prior |  |  | 10 | K |
| T_CONDITION | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 5 | K |
| T_CONDITION | unknown | 0 | 0 | prior (orchid_assumed) |  |  | 5 | K |
| T_CONDITION | model_calculated (vs experiment) | 0 | 0 | prior |  |  | 5 | K |
| X_PHASE | experimental_unspecified | 6 | 1 | prior (orchid_assumed) |  |  | 0.01 | mole fraction |
| X_PHASE | metallography_microscopy | 1 | 1 | prior (orchid_assumed) |  |  | 0.01 | mole fraction |
| X_PHASE | microanalysis | 0 | 0 | prior (orchid_assumed) |  |  | 0.005 | mole fraction |
| X_PHASE | thermal_analysis | 1 | 1 | prior (orchid_assumed) |  |  | 0.01 | mole fraction |
| X_PHASE | unknown | 3014 | 1426 | calibrated | 0.01048 | 0.01048-0.01153 | 0.011 | mole fraction |
| X_PHASE | model_calculated (vs experiment) | 16730 | 8821 | calibrated | 0.004448 | 0.004448-0.004448 | 0.005 | mole fraction |
| LATTICE_LENGTH | experimental_unspecified | 9 | 9 | cleaned_below_threshold (orchid_assumed) | 0.001249 | 0.000481-0.004794 | 0.0013 | relative (fraction of the value) |
| LATTICE_LENGTH | unknown | 597 | 196 | calibrated | 0.002277 | 0.002026-0.002664 | 0.0023 | relative (fraction of the value) |
| LATTICE_LENGTH | xrd | 23 | 21 | calibrated | 0.001206 | 0.000866-0.0022 | 0.0013 | relative (fraction of the value) |
| LATTICE_LENGTH | model_calculated (vs experiment) | 169 | 85 | calibrated | 0.008107 | 0.005703-0.01284 | 0.0082 | relative (fraction of the value) |
| LATTICE_ANGLE | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 0.05 | degree |
| LATTICE_ANGLE | unknown | 2 | 2 | prior (orchid_assumed) |  |  | 0.05 | degree |
| LATTICE_ANGLE | model_calculated (vs experiment) | 1 | 1 | prior |  |  | 0.1 | degree |
| VOLUME | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 0.003 | relative (fraction of the value) |
| VOLUME | unknown | 43 | 5 | cleaned_below_threshold (orchid_assumed) | 0.005326 | 0.003722-0.01968 | 0.0054 | relative (fraction of the value) |
| VOLUME | model_calculated (vs experiment) | 0 | 0 | prior |  |  | 0.005 | relative (fraction of the value) |

## DFT

Literature DFT formation enthalpies (from `espei/dft/CALIBRATION.json`): all n 459, robust sigma 7.14 kJ/mol-atom; strata: magnetic_3d n 105 sigma 4.003, metal n 231 sigma 8.243, pblock_anion n 123 sigma 10.05.

| value type | prior floor | basis |
|---|---:|---|
| GM_FORM | 7.2 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| H_MIX_PARTIAL | 7.2 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| G_MIX_PARTIAL | 7.2 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| HEAT_CONTENT | 7.2 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| SM_FORM | 1 | DFT (phonon / quasi-harmonic) entropies: ORCHID assumption, about 1 J/K/mol-atom |
| S_ABS | 1 | DFT (phonon / quasi-harmonic) entropies: ORCHID assumption, about 1 J/K/mol-atom |
| S_MIX_PARTIAL | 1 | DFT entropies: ORCHID assumption, about 1 J/K/mol |
| CPM | 1 | DFT (quasi-harmonic) heat capacities: ORCHID assumption, about 1 J/K/mol-atom |
| T_INVARIANT | 50 | temperatures calculated from DFT energies: ORCHID assumption, about 50 K |
| T_TRANSITION | 50 | temperatures calculated from DFT energies: ORCHID assumption, about 50 K |
| X_PHASE | 0.02 | compositions calculated from DFT energies: ORCHID assumption, about 0.02 |
| LATTICE_LENGTH | 0.01 | DFT lattice parameters: typically within about 1 % of experiment (semi-local functionals; ORCHID assumption) |
| VOLUME | 0.03 | DFT volumes: typically within about 3 % of experiment (ORCHID assumption) |
| LATTICE_ANGLE | 0.1 | ORCHID assumption, 0.1 degree |
| ACTIVITY | 7.2 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| EMF | 20 | ORCHID assumption, 20 mV |

## Prior sources

- `espei`: ESPEI 0.9.1 experimental reference sigmas (500 J/mol for enthalpies and the chemical potential of activities, 0.2 J/mol/K for entropies and heat capacities; espei/error_functions, 'estimated from NIST TRC uncertainties')
- `kubaschewski`: O. Kubaschewski, C.B. Alcock, P.J. Spencer, Materials Thermochemistry, 6th ed., Pergamon, 1993 (chapter 2, accuracy of experimental methods: calorimetric formation enthalpies typically +-1-2 kJ/mol-atom, EMF and vapour-pressure-derived values less accurate, entropies from the temperature coefficient of EMF or second-law vapour-pressure evaluation the least)
- `drowart2005`: J. Drowart, C. Chatillon, J. Hastie, D. Bonnell, High-temperature mass spectrometry: instrumental techniques, ionization cross-sections, pressure measurements, and thermodynamic data (IUPAC Technical Report), Pure Appl. Chem. 77 (2005) 683-737, doi:10.1351/pac200577040683 (second-law enthalpies less accurate than third-law; systematic errors dominate the stated precision)
- `kirklin2015`: S. Kirklin et al., The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies, npj Comput. Mater. 1 (2015) 15010, doi:10.1038/npjcompumats.2015.10 (mean absolute difference between independent experimental formation enthalpies 0.082 eV/atom, about 8 kJ/mol-atom, over compounds with more than one experimental value)
- `orchid_assumed`: ORCHID assumption (PI decision 2026-10-24), stated so that it can be replaced; not fitted

## Values per evidence class, value type and method class

| evidence class | value type | method class | quantities | with printed sigma | sigma_effective > printed | no sigma_effective |
|---|---|---|---:|---:|---:|---:|
| dft | CPM | dft | 21 | 0 | 0 | 0 |
| dft | GM_FORM | dft | 35 | 0 | 0 | 0 |
| dft | G_MIX_PARTIAL | dft | 135 | 0 | 0 | 0 |
| dft | HM_FORM | dft | 2293 | 11 | 11 | 42 |
| dft | H_MIX_PARTIAL | dft | 333 | 13 | 13 | 15 |
| dft | LATTICE_ANGLE | dft | 131 | 0 | 0 | 0 |
| dft | LATTICE_LENGTH | dft | 2518 | 2 | 2 | 0 |
| dft | SM_FORM | dft | 42 | 0 | 0 | 11 |
| dft | S_ABS | dft | 29 | 0 | 0 | 0 |
| dft | T_INVARIANT | dft | 27 | 0 | 0 | 0 |
| dft | T_TRANSITION | dft | 6 | 0 | 0 | 0 |
| dft | VOLUME | dft | 292 | 0 | 0 | 0 |
| dft | X_PHASE | dft | 171 | 0 | 0 | 0 |
| dft | none | none | 252 | 0 | 0 | 252 |
| experimental | ACTIVITY | emf | 35 | 0 | 0 | 3 |
| experimental | ACTIVITY | kems_vapour | 9 | 0 | 0 | 0 |
| experimental | ACTIVITY | unknown | 229 | 0 | 0 | 4 |
| experimental | CPM | dsc_dta | 201 | 2 | 0 | 0 |
| experimental | CPM | heat_content_calorimetry | 51 | 5 | 4 | 5 |
| experimental | CPM | unknown | 1348 | 34 | 29 | 178 |
| experimental | EMF | emf | 417 | 208 | 208 | 0 |
| experimental | EMF | unknown | 10 | 2 | 1 | 0 |
| experimental | GM_FORM | emf | 49 | 19 | 19 | 0 |
| experimental | GM_FORM | equilibration_other | 4 | 0 | 0 | 0 |
| experimental | GM_FORM | experimental_unspecified | 4 | 0 | 0 | 0 |
| experimental | GM_FORM | kems_vapour | 11 | 0 | 0 | 0 |
| experimental | GM_FORM | solution_reaction_calorimetry | 5 | 5 | 4 | 0 |
| experimental | GM_FORM | unknown | 218 | 58 | 33 | 21 |
| experimental | G_MIX_PARTIAL | emf | 107 | 6 | 0 | 0 |
| experimental | G_MIX_PARTIAL | equilibration_other | 9 | 2 | 1 | 0 |
| experimental | G_MIX_PARTIAL | experimental_unspecified | 11 | 0 | 0 | 0 |
| experimental | G_MIX_PARTIAL | kems_vapour | 4 | 1 | 0 | 0 |
| experimental | G_MIX_PARTIAL | unknown | 246 | 23 | 14 | 18 |
| experimental | HEAT_CONTENT | dsc_dta | 10 | 0 | 0 | 0 |
| experimental | HEAT_CONTENT | heat_content_calorimetry | 37 | 0 | 0 | 0 |
| experimental | HEAT_CONTENT | unknown | 485 | 50 | 4 | 6 |
| experimental | HM_FORM | combustion_calorimetry | 95 | 32 | 7 | 2 |
| experimental | HM_FORM | dsc_dta | 22 | 17 | 7 | 1 |
| experimental | HM_FORM | emf | 217 | 87 | 72 | 0 |
| experimental | HM_FORM | equilibration_other | 17 | 4 | 2 | 1 |
| experimental | HM_FORM | evaluated_compilation | 10 | 3 | 2 | 1 |
| experimental | HM_FORM | experimental_unspecified | 125 | 70 | 56 | 0 |
| experimental | HM_FORM | heat_content_calorimetry | 11 | 1 | 0 | 0 |
| experimental | HM_FORM | kems_vapour | 196 | 95 | 52 | 1 |
| experimental | HM_FORM | kems_vapour_second_law | 11 | 6 | 2 | 2 |
| experimental | HM_FORM | kems_vapour_third_law | 8 | 5 | 1 | 0 |
| experimental | HM_FORM | solution_reaction_calorimetry | 537 | 296 | 211 | 5 |
| experimental | HM_FORM | unknown | 1199 | 439 | 286 | 49 |
| experimental | H_MIX_PARTIAL | dsc_dta | 2 | 2 | 1 | 0 |
| experimental | H_MIX_PARTIAL | emf | 4 | 0 | 0 | 0 |
| experimental | H_MIX_PARTIAL | equilibration_other | 5 | 0 | 0 | 0 |
| experimental | H_MIX_PARTIAL | experimental_unspecified | 9 | 0 | 0 | 0 |
| experimental | H_MIX_PARTIAL | solution_reaction_calorimetry | 935 | 367 | 174 | 1 |
| experimental | H_MIX_PARTIAL | unknown | 551 | 85 | 37 | 2 |
| experimental | LATTICE_ANGLE | experimental_unspecified | 9 | 0 | 0 | 0 |
| experimental | LATTICE_ANGLE | unknown | 97 | 17 | 17 | 0 |
| experimental | LATTICE_ANGLE | xrd | 6 | 0 | 0 | 0 |
| experimental | LATTICE_LENGTH | experimental_unspecified | 146 | 32 | 32 | 0 |
| experimental | LATTICE_LENGTH | unknown | 2551 | 439 | 420 | 0 |
| experimental | LATTICE_LENGTH | xrd | 370 | 121 | 83 | 0 |
| experimental | SM_FORM | dsc_dta | 1 | 0 | 0 | 0 |
| experimental | SM_FORM | emf | 39 | 25 | 6 | 0 |
| experimental | SM_FORM | equilibration_other | 3 | 0 | 0 | 0 |
| experimental | SM_FORM | experimental_unspecified | 8 | 6 | 3 | 0 |
| experimental | SM_FORM | heat_content_calorimetry | 5 | 2 | 0 | 0 |
| experimental | SM_FORM | kems_vapour | 25 | 15 | 4 | 0 |
| experimental | SM_FORM | solution_reaction_calorimetry | 12 | 1 | 0 | 0 |
| experimental | SM_FORM | unknown | 93 | 34 | 6 | 14 |
| experimental | S_ABS | combustion_calorimetry | 1 | 1 | 0 | 0 |
| experimental | S_ABS | dsc_dta | 1 | 0 | 0 | 0 |
| experimental | S_ABS | emf | 21 | 5 | 0 | 0 |
| experimental | S_ABS | evaluated_compilation | 5 | 0 | 0 | 0 |
| experimental | S_ABS | experimental_unspecified | 7 | 2 | 2 | 0 |
| experimental | S_ABS | heat_content_calorimetry | 68 | 15 | 8 | 3 |
| experimental | S_ABS | kems_vapour | 27 | 4 | 0 | 0 |
| experimental | S_ABS | kems_vapour_second_law | 1 | 1 | 0 | 0 |
| experimental | S_ABS | kems_vapour_third_law | 1 | 1 | 0 | 0 |
| experimental | S_ABS | unknown | 195 | 20 | 11 | 6 |
| experimental | S_MIX_PARTIAL | emf | 4 | 2 | 0 | 0 |
| experimental | S_MIX_PARTIAL | unknown | 19 | 2 | 0 | 0 |
| experimental | T_CONDITION | diffusion_couple | 75 | 0 | 0 | 0 |
| experimental | T_CONDITION | dilatometry_resistivity | 16 | 3 | 0 | 0 |
| experimental | T_CONDITION | experimental_unspecified | 114 | 9 | 2 | 0 |
| experimental | T_CONDITION | metallography_microscopy | 341 | 10 | 1 | 0 |
| experimental | T_CONDITION | microanalysis | 616 | 20 | 20 | 0 |
| experimental | T_CONDITION | thermal_analysis | 611 | 68 | 21 | 0 |
| experimental | T_CONDITION | unknown | 2217 | 105 | 24 | 0 |
| experimental | T_CONDITION | xrd | 227 | 14 | 12 | 0 |
| experimental | T_INVARIANT | dilatometry_resistivity | 3 | 0 | 0 | 0 |
| experimental | T_INVARIANT | emf | 5 | 0 | 0 | 0 |
| experimental | T_INVARIANT | experimental_unspecified | 6 | 0 | 0 | 0 |
| experimental | T_INVARIANT | metallography_microscopy | 20 | 0 | 0 | 0 |
| experimental | T_INVARIANT | microanalysis | 1 | 0 | 0 | 0 |
| experimental | T_INVARIANT | thermal_analysis | 245 | 0 | 0 | 0 |
| experimental | T_INVARIANT | unknown | 11780 | 1678 | 1274 | 0 |
| experimental | T_INVARIANT | xrd | 5 | 0 | 0 | 0 |
| experimental | T_TRANSITION | diffusion_couple | 3 | 1 | 0 | 0 |
| experimental | T_TRANSITION | dilatometry_resistivity | 10 | 1 | 1 | 0 |
| experimental | T_TRANSITION | emf | 28 | 1 | 0 | 0 |
| experimental | T_TRANSITION | experimental_unspecified | 132 | 43 | 16 | 0 |
| experimental | T_TRANSITION | metallography_microscopy | 59 | 12 | 5 | 0 |
| experimental | T_TRANSITION | microanalysis | 3 | 0 | 0 | 0 |
| experimental | T_TRANSITION | thermal_analysis | 3038 | 266 | 137 | 0 |
| experimental | T_TRANSITION | unknown | 3942 | 324 | 140 | 0 |
| experimental | T_TRANSITION | xrd | 55 | 11 | 11 | 0 |
| experimental | VOLUME | experimental_unspecified | 4 | 0 | 0 | 0 |
| experimental | VOLUME | unknown | 105 | 13 | 13 | 0 |
| experimental | X_PHASE | diffusion_couple | 64 | 0 | 0 | 0 |
| experimental | X_PHASE | dilatometry_resistivity | 8 | 0 | 0 | 0 |
| experimental | X_PHASE | experimental_unspecified | 140 | 0 | 0 | 0 |
| experimental | X_PHASE | metallography_microscopy | 38 | 0 | 0 | 0 |
| experimental | X_PHASE | microanalysis | 909 | 0 | 0 | 0 |
| experimental | X_PHASE | thermal_analysis | 548 | 0 | 0 | 0 |
| experimental | X_PHASE | unknown | 12914 | 0 | 0 | 0 |
| experimental | X_PHASE | xrd | 17 | 0 | 0 | 0 |
| experimental | none | none | 844 | 26 | 0 | 818 |
| model | ACTIVITY | model_calculated | 222 | 0 | 0 | 0 |
| model | CPM | model_calculated | 637 | 23 | 12 | 23 |
| model | EMF | model_calculated | 2 | 0 | 0 | 0 |
| model | GM_FORM | model_calculated | 440 | 0 | 0 | 35 |
| model | G_MIX_PARTIAL | model_calculated | 387 | 0 | 0 | 18 |
| model | HEAT_CONTENT | model_calculated | 354 | 3 | 1 | 12 |
| model | HM_FORM | model_calculated | 3974 | 108 | 64 | 198 |
| model | H_MIX_PARTIAL | model_calculated | 416 | 0 | 0 | 39 |
| model | LATTICE_ANGLE | model_calculated | 28 | 1 | 1 | 0 |
| model | LATTICE_LENGTH | model_calculated | 1093 | 40 | 40 | 0 |
| model | SM_FORM | model_calculated | 587 | 18 | 10 | 24 |
| model | S_ABS | model_calculated | 990 | 65 | 25 | 100 |
| model | S_MIX_PARTIAL | model_calculated | 63 | 0 | 0 | 12 |
| model | T_CONDITION | model_calculated | 691 | 5 | 0 | 0 |
| model | T_INVARIANT | model_calculated | 12822 | 69 | 11 | 0 |
| model | T_TRANSITION | model_calculated | 2844 | 42 | 0 | 0 |
| model | VOLUME | model_calculated | 116 | 0 | 0 | 0 |
| model | X_PHASE | model_calculated | 12441 | 0 | 0 | 0 |
| model | none | none | 448 | 4 | 0 | 444 |
| unspecified | CPM | evaluated_compilation | 4 | 2 | 1 | 0 |
| unspecified | CPM | unknown | 55 | 6 | 1 | 4 |
| unspecified | GM_FORM | experimental_unspecified | 2 | 0 | 0 | 0 |
| unspecified | GM_FORM | unknown | 24 | 8 | 0 | 0 |
| unspecified | G_MIX_PARTIAL | unknown | 23 | 3 | 0 | 0 |
| unspecified | HEAT_CONTENT | unknown | 3 | 1 | 0 | 0 |
| unspecified | HM_FORM | equilibration_other | 2 | 0 | 0 | 0 |
| unspecified | HM_FORM | evaluated_compilation | 5 | 2 | 2 | 0 |
| unspecified | HM_FORM | experimental_unspecified | 19 | 0 | 0 | 0 |
| unspecified | HM_FORM | unknown | 396 | 26 | 16 | 0 |
| unspecified | H_MIX_PARTIAL | unknown | 22 | 0 | 0 | 0 |
| unspecified | LATTICE_ANGLE | unknown | 61 | 1 | 0 | 0 |
| unspecified | LATTICE_LENGTH | experimental_unspecified | 9 | 0 | 0 | 0 |
| unspecified | LATTICE_LENGTH | unknown | 1986 | 192 | 174 | 0 |
| unspecified | SM_FORM | unknown | 10 | 2 | 0 | 0 |
| unspecified | S_ABS | equilibration_other | 2 | 0 | 0 | 0 |
| unspecified | S_ABS | evaluated_compilation | 9 | 7 | 3 | 0 |
| unspecified | S_ABS | kems_vapour | 2 | 0 | 0 | 0 |
| unspecified | S_ABS | unknown | 84 | 14 | 5 | 0 |
| unspecified | S_MIX_PARTIAL | unknown | 4 | 0 | 0 | 0 |
| unspecified | T_CONDITION | dilatometry_resistivity | 2 | 0 | 0 | 0 |
| unspecified | T_CONDITION | experimental_unspecified | 5 | 0 | 0 | 0 |
| unspecified | T_CONDITION | metallography_microscopy | 3 | 0 | 0 | 0 |
| unspecified | T_CONDITION | unknown | 224 | 2 | 0 | 0 |
| unspecified | T_CONDITION | xrd | 3 | 0 | 0 | 0 |
| unspecified | T_INVARIANT | unknown | 1496 | 133 | 97 | 0 |
| unspecified | T_TRANSITION | unknown | 310 | 7 | 4 | 0 |
| unspecified | VOLUME | unknown | 46 | 0 | 0 | 0 |
| unspecified | X_PHASE | dilatometry_resistivity | 2 | 0 | 0 | 0 |
| unspecified | X_PHASE | experimental_unspecified | 5 | 0 | 0 | 0 |
| unspecified | X_PHASE | metallography_microscopy | 3 | 0 | 0 | 0 |
| unspecified | X_PHASE | unknown | 2068 | 0 | 0 | 0 |
| unspecified | X_PHASE | xrd | 3 | 0 | 0 | 0 |
| unspecified | none | none | 46 | 4 | 0 | 42 |
