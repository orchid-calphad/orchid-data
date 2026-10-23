# Cross-check with Kim et al. 2017

Reference: G. Kim, S. V. Meschel, P. Nash, W. Chen, Experimental formation enthalpies for intermetallic phases and other inorganic compounds, Scientific Data 4 (2017) 170162. doi:10.1038/sdata.2017.162 (Figshare dataset doi:10.6084/m9.figshare.7289723, MIT (Figshare dataset)).

ORCHID candidates: 1503 experimental, accepted, signed HM_FORM records (kJ/mol-atom) over 603 formulas.

Reference file: `~/data/kim2017-expt-formation-enthalpy/formation_enthalpy_expt.csv` (1276 rows; complete file, SHA-256 matches).

| n formulas in common | MAE | median abs diff | sign agreement | differ > 10 |
|---:|---:|---:|---:|---:|
| 162 | 3.85 | 1.191 | 1.0 | 19 |

| formula | ORCHID median | Kim median | difference | ORCHID ids |
|---|---:|---:|---:|---|
| Ge2Hf3 | -30.16 | -74.602 | 44.442 | ORC-RD3CLV2FOT.cf6f65 |
| TaB2 | -20.967 | -53.298 | 32.332 | ORC-ENOMSME5IX, ORC-NWHOAUO467, ORC-PTU6CIJMOI |
| AlIr | -118.0 | -89.215 | -28.785 | ORC-V3S6RNGLPA.43a09d |
| Mn2Ti | -28.92 | -8.597 | -20.323 | ORC-TJIYWZ3M2H.09ad89 |
| LaPt2 | -108.2 | -90.001 | -18.199 | ORC-2RGYOAFBJD.b01966, ORC-3FY37MU6YR.8b64fe, ORC-EDPRXRW4WL.c8079d, ORC-LLMXKPCYVE.1b1145, ORC-MKO4SURWL3.1e9813, ORC-QA4MPPXEHV.34fa39 |
| LaMg | -3.7 | -20.358 | 16.658 | ORC-EQTOORKIKL.9c4590 |
| LaPt | -111.8 | -95.896 | -15.904 | ORC-5IECZBKP2B.a6b839 |
| NbNi3 | -31.715 | -16.798 | -14.917 | ORC-33IFFGWUUH.08e033, ORC-H6CHGHX5XI, ORC-MP75CMWX4X.7e46f8, ORC-VJ2BC6W776.4be015, ORC-ZI3WR77ALH.34226d |
| MgSm | -3.9 | -18.496 | 14.596 | ORC-YT6SCNYYX5.2a1cae |
| Al2Y | -65.65 | -51.952 | -13.698 | ORC-DDUCGWQENM, ORC-MMSUJPXEYZ |
| Fe2Hf | -25.85 | -12.302 | -13.548 | ORC-QJ56PUEUMY, ORC-U33KIRTKYB |
| Au2Ce | -70.6 | -57.495 | -13.105 | ORC-DHKTM2TLJO, ORC-FOOEYBCXYF.b7ce88, ORC-MDDDPLJSRA, ORC-PWC4XQVDFG, ORC-XLRYQNPQ34 |
| Sc5Si3 | -102.8 | -89.895 | -12.905 | ORC-2OWPACNVAE, ORC-GZV46W4OLK.30aa86, ORC-SB22WLDX3O.343415 |
| GaPd2 | -77.0 | -64.404 | -12.596 | ORC-ZACCS6JOUC |
| DyB2 | -42.32 | -30.2 | -12.12 | ORC-QXJEHWNYE2, ORC-RGYHX5NTA6 |
| AuCe | -74.0 | -62.802 | -11.198 | ORC-C37C5PYFBB, ORC-EYZKHB5PF6, ORC-FAAZ6UT4FO, ORC-NI6RI3T7HM.c26ff9, ORC-S6R7TXL4GL |
| ErFe2 | -12.5 | -1.901 | -10.599 | ORC-H5OLRJ7EH6 |
| Ru2Si3 | -50.3 | -60.699 | 10.399 | ORC-6O6ZZDCLP2, ORC-FBOT7E6AZD, ORC-RNRZJL6SW7, ORC-SYECQ5RETF, ORC-YBJAFCOK4E |
| Cu51Zr14 | -14.07 | -24.305 | 10.235 | ORC-24JPYAVIYR, ORC-IB2ZSUZN3N, ORC-JTZAQ5DB2I.28d5ac, ORC-QFC2QRP2ZY.17b92e, ORC-Z7KH7YPIS3.2fcf39 |
