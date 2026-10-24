# ORCHID uncertainty budget: method-floor calibration

Version: orchid-uncertainty-calibration 2026-10-24. Machine-readable: `UNCERTAINTY_CALIBRATION.json` (the same file is copied to `espei/experimental/CALIBRATION_EXPERIMENT.json`). Every record carries `uncertainty_budget` (SCHEMA.md).

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
| HM_FORM | combustion_calorimetry | 15 | 4 | prior (kubaschewski) |  |  | 1 | kJ/mol-atom |
| HM_FORM | dsc_dta | 2 | 2 | prior (kubaschewski) |  |  | 2 | kJ/mol-atom |
| HM_FORM | emf | 32 | 12 | calibrated | 8.072 | 3.879-14.36 | 8.1 | kJ/mol-atom |
| HM_FORM | experimental_unspecified | 35 | 13 | calibrated | 3.77 | 1.573-5.032 | 3.8 | kJ/mol-atom |
| HM_FORM | kems_vapour | 14 | 12 | prior (drowart2005) |  |  | 3 | kJ/mol-atom |
| HM_FORM | kems_vapour_second_law | 1 | 1 | prior (drowart2005) |  |  | 3 | kJ/mol-atom |
| HM_FORM | kems_vapour_third_law | 0 | 0 | prior (drowart2005) |  |  | 2 | kJ/mol-atom |
| HM_FORM | solution_reaction_calorimetry | 74 | 36 | calibrated | 3.428 | 1.932-5.902 | 3.5 | kJ/mol-atom |
| HM_FORM | unknown | 312 | 106 | calibrated | 4.035 | 2.568-4.414 | 4.1 | kJ/mol-atom |
| HM_FORM | model_calculated (vs experiment) | 2186 | 378 | calibrated | 3.271 | 2.858-4.16 | 3.3 | kJ/mol-atom |
| GM_FORM | emf | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol-atom |
| GM_FORM | experimental_unspecified | 2 | 2 | prior (kubaschewski) |  |  | 2 | kJ/mol-atom |
| GM_FORM | kems_vapour | 2 | 2 | prior (drowart2005) |  |  | 2 | kJ/mol-atom |
| GM_FORM | kems_vapour_third_law | 0 | 0 | prior (drowart2005) |  |  | 2 | kJ/mol-atom |
| GM_FORM | unknown | 38 | 18 | calibrated | 1.085 | 0.6605-2.097 | 1.1 | kJ/mol-atom |
| GM_FORM | model_calculated (vs experiment) | 192 | 146 | calibrated | 0.6375 | 0.5041-0.8006 | 0.7 | kJ/mol-atom |
| SM_FORM | emf | 1 | 1 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | heat_content_calorimetry | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol-atom |
| SM_FORM | kems_vapour | 2 | 2 | prior (drowart2005) |  |  | 2 | J/K/mol-atom |
| SM_FORM | kems_vapour_second_law | 0 | 0 | prior (drowart2005) |  |  | 3 | J/K/mol-atom |
| SM_FORM | solution_reaction_calorimetry | 1 | 1 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | unknown | 4 | 4 | prior (kubaschewski) |  |  | 1 | J/K/mol-atom |
| SM_FORM | model_calculated (vs experiment) | 116 | 51 | calibrated | 3.608 | 2.762-4.837 | 3.7 | J/K/mol-atom |
| H_MIX_PARTIAL | experimental_unspecified | 6 | 1 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| H_MIX_PARTIAL | solution_reaction_calorimetry | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol |
| H_MIX_PARTIAL | unknown | 1 | 1 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| H_MIX_PARTIAL | model_calculated (vs experiment) | 133 | 57 | prior |  |  | 1 | kJ/mol |
| G_MIX_PARTIAL | emf | 95 | 15 | calibrated | 3.166 | 1.384-6.091 | 3.2 | kJ/mol |
| G_MIX_PARTIAL | experimental_unspecified | 1 | 1 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| G_MIX_PARTIAL | kems_vapour | 3 | 3 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| G_MIX_PARTIAL | unknown | 15 | 15 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| G_MIX_PARTIAL | model_calculated (vs experiment) | 157 | 103 | prior |  |  | 1 | kJ/mol |
| S_MIX_PARTIAL | emf | 30 | 10 | calibrated | 3.879 | 2.097-14.94 | 3.9 | J/K/mol |
| S_MIX_PARTIAL | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | J/K/mol |
| S_MIX_PARTIAL | kems_vapour | 3 | 3 | prior (kubaschewski) |  |  | 1 | J/K/mol |
| S_MIX_PARTIAL | unknown | 1 | 1 | prior (kubaschewski) |  |  | 1 | J/K/mol |
| S_MIX_PARTIAL | model_calculated (vs experiment) | 27 | 13 | prior |  |  | 1 | J/K/mol |
| S_ABS | emf | 46 | 2 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_ABS | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_ABS | heat_content_calorimetry | 18 | 8 | prior (espei) |  |  | 0.2 | J/K/mol |
| S_ABS | kems_vapour | 3 | 3 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| S_ABS | unknown | 91 | 21 | calibrated | 0.4493 | 0.2621-0.9645 | 0.5 | J/K/mol |
| S_ABS | model_calculated (vs experiment) | 240 | 78 | prior |  |  | 1 | J/K/mol |
| CPM | dsc_dta | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| CPM | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| CPM | heat_content_calorimetry | 42 | 7 | prior (espei) |  |  | 0.2 | J/K/mol |
| CPM | unknown | 6 | 6 | prior (kubaschewski) |  |  | 0.5 | J/K/mol |
| CPM | model_calculated (vs experiment) | 227 | 89 | prior |  |  | 1 | J/K/mol |
| HEAT_CONTENT | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| HEAT_CONTENT | heat_content_calorimetry | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol |
| HEAT_CONTENT | unknown | 16 | 4 | prior (kubaschewski) |  |  | 1 | kJ/mol |
| HEAT_CONTENT | model_calculated (vs experiment) | 538 | 17 | prior |  |  | 1 | kJ/mol |
| ACTIVITY | emf | 0 | 0 | prior (espei) |  |  | 0.5 | kJ/mol (chemical potential) |
| ACTIVITY | experimental_unspecified | 0 | 0 | prior (kubaschewski) |  |  | 1 | kJ/mol (chemical potential) |
| ACTIVITY | unknown | 9 | 9 | prior (kubaschewski) |  |  | 1 | kJ/mol (chemical potential) |
| ACTIVITY | model_calculated (vs experiment) | 73 | 67 | prior |  |  | 1 | kJ/mol (chemical potential) |
| EMF | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 1 | mV |
| EMF | unknown | 0 | 0 | prior (orchid_assumed) |  |  | 1 | mV |
| EMF | model_calculated (vs experiment) | 0 | 0 | prior |  |  | 2 | mV |
| T_INVARIANT | emf | 1 | 1 | prior (orchid_assumed) |  |  | 10 | K |
| T_INVARIANT | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 10 | K |
| T_INVARIANT | thermal_analysis | 0 | 0 | prior (orchid_assumed) |  |  | 5 | K |
| T_INVARIANT | unknown | 4981 | 1688 | calibrated | 9.435 | 8.387-10.48 | 10 | K |
| T_INVARIANT | model_calculated (vs experiment) | 14188 | 5391 | calibrated | 3.707 | 3.113-4.448 | 4 | K |
| T_TRANSITION | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 10 | K |
| T_TRANSITION | thermal_analysis | 8 | 3 | prior (orchid_assumed) |  |  | 5 | K |
| T_TRANSITION | unknown | 220 | 43 | calibrated | 16.77 | 10.69-31.45 | 17 | K |
| T_TRANSITION | model_calculated (vs experiment) | 117 | 57 | prior |  |  | 10 | K |
| T_CONDITION | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 5 | K |
| T_CONDITION | unknown | 0 | 0 | prior (orchid_assumed) |  |  | 5 | K |
| T_CONDITION | model_calculated (vs experiment) | 0 | 0 | prior |  |  | 5 | K |
| X_PHASE | experimental_unspecified | 6 | 1 | prior (orchid_assumed) |  |  | 0.01 | mole fraction |
| X_PHASE | metallography_microscopy | 1 | 1 | prior (orchid_assumed) |  |  | 0.01 | mole fraction |
| X_PHASE | microanalysis | 0 | 0 | prior (orchid_assumed) |  |  | 0.005 | mole fraction |
| X_PHASE | thermal_analysis | 1 | 1 | prior (orchid_assumed) |  |  | 0.01 | mole fraction |
| X_PHASE | unknown | 3139 | 1453 | calibrated | 0.01048 | 0.01048-0.01258 | 0.011 | mole fraction |
| X_PHASE | model_calculated (vs experiment) | 16938 | 8871 | calibrated | 0.004448 | 0.003855-0.004448 | 0.005 | mole fraction |
| LATTICE_LENGTH | experimental_unspecified | 9 | 9 | prior (orchid_assumed) |  |  | 0.001 | relative (fraction of the value) |
| LATTICE_LENGTH | unknown | 603 | 194 | calibrated | 0.00222 | 0.00189-0.002664 | 0.0023 | relative (fraction of the value) |
| LATTICE_LENGTH | xrd | 24 | 22 | calibrated | 0.001082 | 0.000794-0.001837 | 0.0011 | relative (fraction of the value) |
| LATTICE_LENGTH | model_calculated (vs experiment) | 223 | 133 | calibrated | 0.01114 | 0.007225-0.01295 | 0.0112 | relative (fraction of the value) |
| LATTICE_ANGLE | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 0.05 | degree |
| LATTICE_ANGLE | unknown | 2 | 2 | prior (orchid_assumed) |  |  | 0.05 | degree |
| LATTICE_ANGLE | model_calculated (vs experiment) | 1 | 1 | prior |  |  | 0.1 | degree |
| VOLUME | experimental_unspecified | 0 | 0 | prior (orchid_assumed) |  |  | 0.003 | relative (fraction of the value) |
| VOLUME | unknown | 50 | 12 | calibrated | 0.01968 | 0.005248-0.0533 | 0.0197 | relative (fraction of the value) |
| VOLUME | model_calculated (vs experiment) | 5 | 4 | prior |  |  | 0.005 | relative (fraction of the value) |

## DFT

Literature DFT formation enthalpies (from `espei/dft/CALIBRATION.json`): all n 247, robust sigma 5.244 kJ/mol-atom; strata: magnetic_3d n 90 sigma 3.522, metal n 93 sigma 6.28, pblock_anion n 64 sigma 6.883.

| value type | prior floor | basis |
|---|---:|---|
| GM_FORM | 5.3 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| H_MIX_PARTIAL | 5.3 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| G_MIX_PARTIAL | 5.3 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
| HEAT_CONTENT | 5.3 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
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
| ACTIVITY | 5.3 | prior by analogy: the calibrated DFT formation-enthalpy sigma of literature DFT values (all strata), used for other DFT energies because no DFT-vs-experiment calibration exists for them |
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
| dft | GM_FORM | dft | 19 | 0 | 0 | 0 |
| dft | G_MIX_PARTIAL | dft | 135 | 0 | 0 | 0 |
| dft | HM_FORM | dft | 2212 | 12 | 12 | 50 |
| dft | H_MIX_PARTIAL | dft | 310 | 13 | 13 | 0 |
| dft | LATTICE_ANGLE | dft | 131 | 0 | 0 | 0 |
| dft | LATTICE_LENGTH | dft | 2463 | 2 | 2 | 0 |
| dft | SM_FORM | dft | 14 | 0 | 0 | 11 |
| dft | S_ABS | dft | 28 | 0 | 0 | 0 |
| dft | T_INVARIANT | dft | 28 | 0 | 0 | 0 |
| dft | T_TRANSITION | dft | 6 | 0 | 0 | 0 |
| dft | VOLUME | dft | 283 | 0 | 0 | 0 |
| dft | X_PHASE | dft | 154 | 0 | 0 | 0 |
| dft | none | none | 121 | 0 | 0 | 121 |
| experimental | ACTIVITY | emf | 35 | 0 | 0 | 3 |
| experimental | ACTIVITY | kems_vapour | 9 | 0 | 0 | 0 |
| experimental | ACTIVITY | unknown | 229 | 0 | 0 | 4 |
| experimental | CPM | dsc_dta | 201 | 2 | 0 | 0 |
| experimental | CPM | heat_content_calorimetry | 51 | 5 | 0 | 7 |
| experimental | CPM | unknown | 1348 | 34 | 5 | 178 |
| experimental | EMF | emf | 503 | 208 | 208 | 2 |
| experimental | EMF | unknown | 10 | 2 | 1 | 0 |
| experimental | GM_FORM | emf | 47 | 9 | 9 | 0 |
| experimental | GM_FORM | equilibration_other | 4 | 0 | 0 | 0 |
| experimental | GM_FORM | experimental_unspecified | 12 | 1 | 1 | 0 |
| experimental | GM_FORM | kems_vapour | 12 | 0 | 0 | 0 |
| experimental | GM_FORM | solution_reaction_calorimetry | 5 | 5 | 0 | 0 |
| experimental | GM_FORM | unknown | 222 | 58 | 31 | 21 |
| experimental | G_MIX_PARTIAL | emf | 293 | 17 | 14 | 11 |
| experimental | G_MIX_PARTIAL | equilibration_other | 16 | 2 | 0 | 0 |
| experimental | G_MIX_PARTIAL | experimental_unspecified | 17 | 0 | 0 | 0 |
| experimental | G_MIX_PARTIAL | kems_vapour | 70 | 1 | 0 | 9 |
| experimental | G_MIX_PARTIAL | unknown | 310 | 23 | 10 | 22 |
| experimental | HEAT_CONTENT | dsc_dta | 10 | 0 | 0 | 0 |
| experimental | HEAT_CONTENT | heat_content_calorimetry | 37 | 0 | 0 | 0 |
| experimental | HEAT_CONTENT | unknown | 580 | 52 | 9 | 6 |
| experimental | HM_FORM | combustion_calorimetry | 95 | 32 | 3 | 2 |
| experimental | HM_FORM | dsc_dta | 22 | 17 | 6 | 1 |
| experimental | HM_FORM | emf | 240 | 101 | 85 | 0 |
| experimental | HM_FORM | equilibration_other | 20 | 6 | 3 | 1 |
| experimental | HM_FORM | experimental_unspecified | 132 | 72 | 50 | 1 |
| experimental | HM_FORM | heat_content_calorimetry | 11 | 1 | 0 | 0 |
| experimental | HM_FORM | kems_vapour | 165 | 80 | 25 | 1 |
| experimental | HM_FORM | kems_vapour_second_law | 11 | 6 | 0 | 2 |
| experimental | HM_FORM | kems_vapour_third_law | 8 | 5 | 0 | 0 |
| experimental | HM_FORM | solution_reaction_calorimetry | 540 | 300 | 188 | 5 |
| experimental | HM_FORM | unknown | 1205 | 439 | 278 | 49 |
| experimental | H_MIX_PARTIAL | dsc_dta | 2 | 2 | 1 | 0 |
| experimental | H_MIX_PARTIAL | emf | 4 | 0 | 0 | 0 |
| experimental | H_MIX_PARTIAL | equilibration_other | 5 | 0 | 0 | 0 |
| experimental | H_MIX_PARTIAL | experimental_unspecified | 9 | 0 | 0 | 0 |
| experimental | H_MIX_PARTIAL | solution_reaction_calorimetry | 930 | 362 | 174 | 1 |
| experimental | H_MIX_PARTIAL | unknown | 551 | 85 | 38 | 2 |
| experimental | LATTICE_ANGLE | experimental_unspecified | 9 | 0 | 0 | 0 |
| experimental | LATTICE_ANGLE | unknown | 97 | 17 | 17 | 0 |
| experimental | LATTICE_ANGLE | xrd | 6 | 0 | 0 | 0 |
| experimental | LATTICE_LENGTH | experimental_unspecified | 146 | 32 | 31 | 0 |
| experimental | LATTICE_LENGTH | unknown | 2550 | 438 | 419 | 0 |
| experimental | LATTICE_LENGTH | xrd | 370 | 121 | 79 | 0 |
| experimental | SM_FORM | dsc_dta | 1 | 0 | 0 | 0 |
| experimental | SM_FORM | emf | 41 | 27 | 6 | 0 |
| experimental | SM_FORM | equilibration_other | 3 | 0 | 0 | 0 |
| experimental | SM_FORM | experimental_unspecified | 16 | 6 | 2 | 0 |
| experimental | SM_FORM | heat_content_calorimetry | 15 | 2 | 0 | 2 |
| experimental | SM_FORM | kems_vapour | 18 | 13 | 2 | 0 |
| experimental | SM_FORM | solution_reaction_calorimetry | 12 | 1 | 0 | 0 |
| experimental | SM_FORM | unknown | 98 | 34 | 6 | 14 |
| experimental | S_ABS | combustion_calorimetry | 1 | 1 | 0 | 0 |
| experimental | S_ABS | dsc_dta | 1 | 0 | 0 | 0 |
| experimental | S_ABS | emf | 24 | 8 | 0 | 0 |
| experimental | S_ABS | experimental_unspecified | 5 | 2 | 2 | 0 |
| experimental | S_ABS | heat_content_calorimetry | 62 | 15 | 0 | 2 |
| experimental | S_ABS | kems_vapour | 24 | 1 | 0 | 0 |
| experimental | S_ABS | kems_vapour_second_law | 1 | 1 | 0 | 0 |
| experimental | S_ABS | kems_vapour_third_law | 1 | 1 | 0 | 0 |
| experimental | S_ABS | unknown | 192 | 20 | 6 | 6 |
| experimental | S_MIX_PARTIAL | emf | 120 | 2 | 2 | 0 |
| experimental | S_MIX_PARTIAL | equilibration_other | 6 | 0 | 0 | 0 |
| experimental | S_MIX_PARTIAL | experimental_unspecified | 5 | 0 | 0 | 0 |
| experimental | S_MIX_PARTIAL | kems_vapour | 35 | 0 | 0 | 0 |
| experimental | S_MIX_PARTIAL | unknown | 51 | 2 | 0 | 0 |
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
| experimental | T_INVARIANT | unknown | 11798 | 1680 | 945 | 0 |
| experimental | T_INVARIANT | xrd | 5 | 0 | 0 | 0 |
| experimental | T_TRANSITION | diffusion_couple | 3 | 1 | 0 | 0 |
| experimental | T_TRANSITION | dilatometry_resistivity | 10 | 1 | 1 | 0 |
| experimental | T_TRANSITION | emf | 28 | 1 | 0 | 0 |
| experimental | T_TRANSITION | experimental_unspecified | 132 | 43 | 16 | 0 |
| experimental | T_TRANSITION | metallography_microscopy | 59 | 12 | 5 | 0 |
| experimental | T_TRANSITION | microanalysis | 3 | 0 | 0 | 0 |
| experimental | T_TRANSITION | thermal_analysis | 3038 | 266 | 137 | 0 |
| experimental | T_TRANSITION | unknown | 3944 | 324 | 141 | 0 |
| experimental | T_TRANSITION | xrd | 79 | 11 | 11 | 0 |
| experimental | VOLUME | experimental_unspecified | 4 | 0 | 0 | 0 |
| experimental | VOLUME | unknown | 114 | 13 | 13 | 0 |
| experimental | X_PHASE | diffusion_couple | 64 | 0 | 0 | 0 |
| experimental | X_PHASE | dilatometry_resistivity | 8 | 0 | 0 | 0 |
| experimental | X_PHASE | experimental_unspecified | 140 | 0 | 0 | 0 |
| experimental | X_PHASE | metallography_microscopy | 38 | 0 | 0 | 0 |
| experimental | X_PHASE | microanalysis | 909 | 0 | 0 | 0 |
| experimental | X_PHASE | thermal_analysis | 548 | 0 | 0 | 0 |
| experimental | X_PHASE | unknown | 12959 | 0 | 0 | 0 |
| experimental | X_PHASE | xrd | 17 | 0 | 0 | 0 |
| experimental | none | none | 104 | 19 | 0 | 85 |
| model | ACTIVITY | model_calculated | 222 | 0 | 0 | 0 |
| model | CPM | model_calculated | 793 | 23 | 12 | 25 |
| model | EMF | model_calculated | 2 | 0 | 0 | 0 |
| model | GM_FORM | model_calculated | 432 | 0 | 0 | 35 |
| model | G_MIX_PARTIAL | model_calculated | 508 | 0 | 0 | 26 |
| model | HEAT_CONTENT | model_calculated | 436 | 3 | 1 | 12 |
| model | HM_FORM | model_calculated | 4152 | 108 | 50 | 209 |
| model | H_MIX_PARTIAL | model_calculated | 408 | 0 | 0 | 36 |
| model | LATTICE_ANGLE | model_calculated | 28 | 1 | 1 | 0 |
| model | LATTICE_LENGTH | model_calculated | 1147 | 40 | 40 | 0 |
| model | SM_FORM | model_calculated | 703 | 18 | 8 | 27 |
| model | S_ABS | model_calculated | 931 | 65 | 23 | 100 |
| model | S_MIX_PARTIAL | model_calculated | 96 | 0 | 0 | 12 |
| model | T_CONDITION | model_calculated | 691 | 5 | 0 | 0 |
| model | T_INVARIANT | model_calculated | 12523 | 69 | 11 | 0 |
| model | T_TRANSITION | model_calculated | 2833 | 42 | 0 | 0 |
| model | VOLUME | model_calculated | 116 | 0 | 0 | 0 |
| model | X_PHASE | model_calculated | 12184 | 0 | 0 | 0 |
| model | none | none | 110 | 4 | 0 | 106 |
| unspecified | CPM | experimental_unspecified | 4 | 2 | 1 | 0 |
| unspecified | CPM | unknown | 55 | 6 | 1 | 4 |
| unspecified | GM_FORM | experimental_unspecified | 2 | 0 | 0 | 0 |
| unspecified | GM_FORM | unknown | 24 | 8 | 0 | 0 |
| unspecified | G_MIX_PARTIAL | unknown | 27 | 3 | 0 | 0 |
| unspecified | HEAT_CONTENT | unknown | 4 | 2 | 0 | 0 |
| unspecified | HM_FORM | equilibration_other | 2 | 0 | 0 | 0 |
| unspecified | HM_FORM | experimental_unspecified | 24 | 2 | 0 | 0 |
| unspecified | HM_FORM | unknown | 397 | 26 | 6 | 0 |
| unspecified | H_MIX_PARTIAL | unknown | 22 | 0 | 0 | 0 |
| unspecified | LATTICE_ANGLE | unknown | 61 | 1 | 0 | 0 |
| unspecified | LATTICE_LENGTH | experimental_unspecified | 9 | 0 | 0 | 0 |
| unspecified | LATTICE_LENGTH | unknown | 1988 | 193 | 175 | 0 |
| unspecified | SM_FORM | unknown | 10 | 2 | 0 | 0 |
| unspecified | S_ABS | equilibration_other | 2 | 0 | 0 | 0 |
| unspecified | S_ABS | experimental_unspecified | 9 | 7 | 3 | 0 |
| unspecified | S_ABS | kems_vapour | 2 | 0 | 0 | 0 |
| unspecified | S_ABS | unknown | 84 | 14 | 5 | 0 |
| unspecified | S_MIX_PARTIAL | unknown | 8 | 0 | 0 | 0 |
| unspecified | T_CONDITION | dilatometry_resistivity | 2 | 0 | 0 | 0 |
| unspecified | T_CONDITION | experimental_unspecified | 5 | 0 | 0 | 0 |
| unspecified | T_CONDITION | metallography_microscopy | 3 | 0 | 0 | 0 |
| unspecified | T_CONDITION | unknown | 224 | 2 | 0 | 0 |
| unspecified | T_CONDITION | xrd | 3 | 0 | 0 | 0 |
| unspecified | T_INVARIANT | unknown | 1783 | 133 | 84 | 0 |
| unspecified | T_TRANSITION | unknown | 319 | 7 | 4 | 0 |
| unspecified | VOLUME | unknown | 46 | 0 | 0 | 0 |
| unspecified | X_PHASE | dilatometry_resistivity | 2 | 0 | 0 | 0 |
| unspecified | X_PHASE | experimental_unspecified | 5 | 0 | 0 | 0 |
| unspecified | X_PHASE | metallography_microscopy | 3 | 0 | 0 | 0 |
| unspecified | X_PHASE | unknown | 2380 | 0 | 0 | 0 |
| unspecified | X_PHASE | xrd | 3 | 0 | 0 | 0 |
| unspecified | none | none | 36 | 3 | 0 | 33 |
