# Cr–V phases

> Cr–V system: 4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CR-V.html · Markdown: https://data.orchid-project.org/phases/pages/CR-V.md

4 phases (tier A 3, liquid 1); 2 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CR-V) · [full JSON](https://data.orchid-project.org/phases/systems/CR-V.json) · [Cr–V system page](https://data.orchid-project.org/systems/CR-V.html) · [Markdown](https://data.orchid-project.org/phases/pages/CR-V.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Cr–V system (4)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [BCC_A2](#phase-cr-v-bcc-a2); _phase:cr-v:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 4 of 4 calculated diagram(s): 297.43–3999.25 K, x(V) 0–1 | 0 | 4 |
| [FCC_A1](#phase-cr-v-fcc-a1); _phase:cr-v:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [HCP_A3](#phase-cr-v-hcp-a3); _phase:cr-v:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 4 calculated diagram(s) | 0 | 4 |
| [LIQUID](#phase-cr-v-liquid); _phase:cr-v:liquid_ | liquid | liquid | stable in 4 of 4 calculated diagram(s): 2026.74–4000 K, x(V) 0–1 | 0 | 4 |

## BCC_A2 (Cr–V)

- Id: `phase:cr-v:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 297.43–3999.25 K, x(V) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-v:bcc-a2)

Names (5): _corpus: _corpus:phase:cr-v:bcc-a2  
_tdb: _tdb:CrV-02Gho.tdb:BCC_A2, tdb:CrV-24Ton.tdb:BCC_A2, tdb:CrV-82Smi.tdb:BCC_A2, tdb:CrV-92Lee-LB.tdb:BCC_A2  


### TDB models of BCC_A2 (4): PHASE and CONSTITUENT statements as written

[CrV-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-02Gho.tdb): BCC_A2, type code %B, sha256 `8130316cc4cd3cce…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% V% : VA : !
~~~~

[CrV-24Ton.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-24Ton.tdb): BCC_A2, type code %B, sha256 `46ece17e757be0b2…`

~~~~text
35: PHASE BCC_A2 %B 2 1 3 !
36: CONST BCC_A2 : CR% V% : VA : !
~~~~

[CrV-82Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-82Smi.tdb): BCC_A2, type code %B, sha256 `14d836240a40ddaf…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : CR% V% : VA : !
~~~~

[CrV-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-92Lee-LB.tdb): BCC_A2, type code %B, sha256 `5ef1eca3ead4a067…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CR% V% : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02876166](https://doi.org/10.1007/BF02876166) J.F. Smith, D.M. Bailey, O.N. Carlson, Bull. Alloy Phase Diag., 2, 469-73(1982).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2024.174011](https://doi.org/10.1016/j.jallcom.2024.174011) Beril Tonyali, Hui Sun, Brandon Bocklund, John Paul Borgonia, Richard A. Otis, Shun-Li Shang et al., Additively manufactured Ni-20Cr to V functionally graded material: Computational predictions and experimental verification of phase formations, Journal of Alloys and Compounds 985, 174011 (2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830502](https://doi.org/10.1515/ijmr-1992-830502) B.-J. Lee, Z. Metallkd., 83, 292-99(1992).  
_assessment that models this phase_

## FCC_A1 (Cr–V)

- Id: `phase:cr-v:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-v:fcc-a1)

Names (5): _corpus: _corpus:phase:cr-v:fcc-a1  
_tdb: _tdb:CrV-02Gho.tdb:FCC_A1, tdb:CrV-24Ton.tdb:FCC_A1, tdb:CrV-82Smi.tdb:FCC_A1, tdb:CrV-92Lee-LB.tdb:FCC_A1  


### TDB models of FCC_A1 (4): PHASE and CONSTITUENT statements as written

[CrV-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-02Gho.tdb): FCC_A1, type code %A, sha256 `8130316cc4cd3cce…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR V : VA : !
~~~~

[CrV-24Ton.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-24Ton.tdb): FCC_A1, type code %A, sha256 `46ece17e757be0b2…`

~~~~text
30: PHASE FCC_A1 %A 2 1 1 !
31: CONST FCC_A1 : CR V : VA : !
~~~~

[CrV-82Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-82Smi.tdb): FCC_A1, type code %A, sha256 `14d836240a40ddaf…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : CR V : VA : !
~~~~

[CrV-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-92Lee-LB.tdb): FCC_A1, type code %A, sha256 `5ef1eca3ead4a067…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CR V : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02876166](https://doi.org/10.1007/BF02876166) J.F. Smith, D.M. Bailey, O.N. Carlson, Bull. Alloy Phase Diag., 2, 469-73(1982).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2024.174011](https://doi.org/10.1016/j.jallcom.2024.174011) Beril Tonyali, Hui Sun, Brandon Bocklund, John Paul Borgonia, Richard A. Otis, Shun-Li Shang et al., Additively manufactured Ni-20Cr to V functionally graded material: Computational predictions and experimental verification of phase formations, Journal of Alloys and Compounds 985, 174011 (2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830502](https://doi.org/10.1515/ijmr-1992-830502) B.-J. Lee, Z. Metallkd., 83, 292-99(1992).  
_assessment that models this phase_

## HCP_A3 (Cr–V)

- Id: `phase:cr-v:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: not stable in 4 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-v:hcp-a3)

Names (5): _corpus: _corpus:phase:cr-v:hcp-a3  
_tdb: _tdb:CrV-02Gho.tdb:HCP_A3, tdb:CrV-24Ton.tdb:HCP_A3, tdb:CrV-82Smi.tdb:HCP_A3, tdb:CrV-92Lee-LB.tdb:HCP_A3  


### TDB models of HCP_A3 (4): PHASE and CONSTITUENT statements as written

[CrV-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-02Gho.tdb): HCP_A3, type code %A, sha256 `8130316cc4cd3cce…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR V : VA : !
~~~~

[CrV-24Ton.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-24Ton.tdb): HCP_A3, type code %A, sha256 `46ece17e757be0b2…`

~~~~text
40: PHASE HCP_A3 %A 2 1 0.5 !
41: CONST HCP_A3 : CR V : VA : !
~~~~

[CrV-82Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-82Smi.tdb): HCP_A3, type code %A, sha256 `14d836240a40ddaf…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : CR V : VA : !
~~~~

[CrV-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-92Lee-LB.tdb): HCP_A3, type code %A, sha256 `5ef1eca3ead4a067…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CR V : VA : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02876166](https://doi.org/10.1007/BF02876166) J.F. Smith, D.M. Bailey, O.N. Carlson, Bull. Alloy Phase Diag., 2, 469-73(1982).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2024.174011](https://doi.org/10.1016/j.jallcom.2024.174011) Beril Tonyali, Hui Sun, Brandon Bocklund, John Paul Borgonia, Richard A. Otis, Shun-Li Shang et al., Additively manufactured Ni-20Cr to V functionally graded material: Computational predictions and experimental verification of phase formations, Journal of Alloys and Compounds 985, 174011 (2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830502](https://doi.org/10.1515/ijmr-1992-830502) B.-J. Lee, Z. Metallkd., 83, 292-99(1992).  
_assessment that models this phase_

## LIQUID (Cr–V)

- Id: `phase:cr-v:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 4 of 4 calculated diagram(s): 2026.74–4000 K, x(V) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:cr-v:liquid)

Names (5): _corpus: _corpus:phase:cr-v:liquid  
_tdb: _tdb:CrV-02Gho.tdb:LIQUID, tdb:CrV-24Ton.tdb:LIQUID, tdb:CrV-82Smi.tdb:LIQUID, tdb:CrV-92Lee-LB.tdb:LIQUID  


### TDB models of LIQUID (4): PHASE and CONSTITUENT statements as written

[CrV-02Gho.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-02Gho.tdb): LIQUID, type code %, sha256 `8130316cc4cd3cce…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR V : !
~~~~

[CrV-24Ton.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-24Ton.tdb): LIQUID, type code %, sha256 `46ece17e757be0b2…`

~~~~text
25: PHASE LIQUID:L % 1 1 !
26: CONST LIQUID:L : CR V : !
~~~~

[CrV-82Smi.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-82Smi.tdb): LIQUID, type code %, sha256 `14d836240a40ddaf…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : CR V : !
~~~~

[CrV-92Lee-LB.tdb](https://orchid-project.org/data/databases/sgte-binary/CrV-92Lee-LB.tdb): LIQUID, type code %, sha256 `5ef1eca3ead4a067…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CR V : !
~~~~

Example references (4 of 4; assessments first): 

- [doi:10.1007/BF02876166](https://doi.org/10.1007/BF02876166) J.F. Smith, D.M. Bailey, O.N. Carlson, Bull. Alloy Phase Diag., 2, 469-73(1982).  
_assessment that models this phase_
- [doi:10.1016/j.jallcom.2024.174011](https://doi.org/10.1016/j.jallcom.2024.174011) Beril Tonyali, Hui Sun, Brandon Bocklund, John Paul Borgonia, Richard A. Otis, Shun-Li Shang et al., Additively manufactured Ni-20Cr to V functionally graded material: Computational predictions and experimental verification of phase formations, Journal of Alloys and Compounds 985, 174011 (2024).  
_assessment that models this phase_
- [doi:10.1361/105497102770331569](https://doi.org/10.1361/105497102770331569) G. Ghosh, Thermodynamic and kinetic modeling of the Cr-Ti-V system, JPE 23, 310-328 (2002).  
_assessment that models this phase_
- [doi:10.1515/ijmr-1992-830502](https://doi.org/10.1515/ijmr-1992-830502) B.-J. Lee, Z. Metallkd., 83, 292-99(1992).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID-Registry: phase registry of binary systems (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data: umbrella record of the ORCHID datasets (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID-Registry: phase registry of binary systems}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data: umbrella record of the ORCHID datasets}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-orchid-data},
  url       = {https://doi.org/10.5281/zenodo.PENDING-orchid-data},
  note      = {Version 1, machine-extracted}
}
```

---

Derived data CC BY 4.0 ([licence](https://creativecommons.org/licenses/by/4.0/)): cite the ORCHID phase registry and the sources named on the page (TDB assessments, Hallstedt 2025, Materials Project, OQMD). TDB statements are quoted as written; parameter expressions are not reproduced. Field reference: [SCHEMA.md](https://data.orchid-project.org/phases/SCHEMA.md). Machine-readable guide: [llms.txt](https://data.orchid-project.org/llms.txt).
