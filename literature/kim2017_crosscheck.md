# Cross-check with Kim et al. 2017

Reference: G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162. doi:10.1038/sdata.2017.162 (Figshare dataset doi:10.6084/m9.figshare.7289723, MIT (Figshare dataset)).

ORCHID candidates: 1498 experimental, accepted, signed HM_FORM records (kJ/mol-atom) over 603 formulas.

**Status: not compared.** No local copy of the reference table (`formation_enthalpy_expt.csv`) was found and nothing was downloaded (no-network policy). Searched on 2026-10-22 without a match: the CANDIDATES paths; every file named *formation_enthalpy* or *expt_formation* under $HOME (excluding ~/Library; only an unrelated HEACalculator pair-enthalpy table was found); every *.csv / *.csv.gz / *.json.gz under ~/projects and ~/data (depth 6) for the SHA-256 prefix 694ba240c2b45da9 of formation_enthalpy_expt.csv recorded in open-tdb's benchmark intake (examples/thermo-extraction-benchmark/real-paper/kim2018-figshare-formation-enthalpy-intake-v1.json); no matminer dataset cache. The intake names the source file but the bytes are not on this machine.

To run the comparison, place the Figshare file at one of these paths (or pass `--kim-csv`) and rerun `python3 tools/kim2017_crosscheck.py`:

* `~/projects/open-tdb/build/kim2017/formation_enthalpy_expt.csv`
* `~/projects/open-tdb/examples/thermo-extraction-benchmark/real-paper/formation_enthalpy_expt.csv`
* `~/data/kim2017/formation_enthalpy_expt.csv`
* `~/data/PD-extraction/datasets/kim2017/formation_enthalpy_expt.csv`
