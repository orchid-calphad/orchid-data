# Co–Ga phases

> Co–Ga system: 7 phases (tier A 5, tier B 1, liquid 1); 6 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/CO-GA.html · Markdown: https://data.orchid-project.org/phases/pages/CO-GA.md

7 phases (tier A 5, tier B 1, liquid 1); 6 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=CO-GA) · [full JSON](https://data.orchid-project.org/phases/systems/CO-GA.json) · [Co–Ga system page](https://data.orchid-project.org/systems/CO-GA.html) · [Markdown](https://data.orchid-project.org/phases/pages/CO-GA.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Co–Ga system (7)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [ORTHORHOMBIC_A11](#phase-co-ga-a11-orthorhombic); _phase:co-ga:a11-orthorhombic_ | alpha-Ga · A11 · oC8 · Cmce (64) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–302.91 K, x(Ga) 1–1 | 2 | 3 |
| [BCC_A2](#phase-co-ga-bcc-a2); _phase:co-ga:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | not stable in 3 calculated diagram(s) | 0 | 3 |
| [COGA_B2](#phase-co-ga-coga-b2); _phase:co-ga:coga-b2_ | CsCl · B2 · cP2 · Pm-3m (221) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Ga) 0.22551–0.71442 | 0 | 3 |
| [COGA3](#phase-co-ga-coga3); _phase:co-ga:coga3_ | In3Ir · tP16 · P4_2/mnm (136) | tier B: DFT-supported (unique MP + OQMD match) | stable in 3 of 3 calculated diagram(s): 300–1132.33 K, x(Ga) 0.75–0.75 | 15 | 3 |
| [FCC_A1](#phase-co-ga-fcc-a1); _phase:co-ga:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–1768.99 K, x(Ga) 0–0.19684 | 12 | 3 |
| [HCP_A3](#phase-co-ga-hcp-a3); _phase:co-ga:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | stable in 3 of 3 calculated diagram(s): 300–701.98 K, x(Ga) 0–0.10938 | 0 | 3 |
| [LIQUID](#phase-co-ga-liquid); _phase:co-ga:liquid_ | liquid | liquid | stable in 3 of 3 calculated diagram(s): 302.91–2500 K, x(Ga) 0–1 | 20 | 3 |

## ORTHORHOMBIC_A11 (Co–Ga)

- Id: `phase:co-ga:a11-orthorhombic`; status `assigned`
- Structure: alpha-Ga · A11 · oC8 · Cmce (64); type `st:a11-alpha-ga-oc8`; tier A: standard phase name; confidence high
- Stoichiometry: Ga 1.0000
- Stability: stable in 3 of 3 calculated diagram(s): 300–302.91 K, x(Ga) 1–1
- Literature: 2 values (2 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:a11-orthorhombic)

Names (6): _corpus: _corpus:phase:co-ga:a11-orthorhombic, corpus:phase:co-ga:orthorhombic-a11  
_paper: _paper:10.1016/j.calphad.2010.02.004:Orthorhombic Ga  
_tdb: _tdb:CoGa-05Su.tdb:ORTHORHOMBIC_A11, tdb:CoGa-10Cha.tdb:ORTHORHOMBIC_A11, tdb:CoGa-99Gro.tdb:ORTHORHOMBIC_A11  


### TDB models of ORTHORHOMBIC_A11 (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d465d6a3ab86a311…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): ORTHORHOMBIC_A11, type code %, sha256 `d36d75154ff187ec…`

~~~~text
53: PHASE ORTHORHOMBIC_A11 % 1 1 !
54: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): ORTHORHOMBIC_A11, type code %, sha256 `119f21425d794516…`

~~~~text
43: PHASE ORTHORHOMBIC_A11 % 1 1 !
44: CONST ORTHORHOMBIC_A11 : GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## BCC_A2 (Co–Ga)

- Id: `phase:co-ga:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: not stable in 3 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:bcc-a2)

Names (4): _corpus: _corpus:phase:co-ga:bcc-a2  
_tdb: _tdb:CoGa-05Su.tdb:BCC_A2, tdb:CoGa-10Cha.tdb:BCC_A2, tdb:CoGa-99Gro.tdb:BCC_A2  


### TDB models of BCC_A2 (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): BCC_A2, type code %B, sha256 `d465d6a3ab86a311…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO GA : VA : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): BCC_A2, type code %B, sha256 `d36d75154ff187ec…`

~~~~text
43: PHASE BCC_A2 %B 2 1 3 !
44: CONST BCC_A2 : CO GA : VA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): BCC_A2, type code %B, sha256 `119f21425d794516…`

~~~~text
33: PHASE BCC_A2 %B 2 1 3 !
34: CONST BCC_A2 : CO GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## COGA_B2 (Co–Ga)

- Id: `phase:co-ga:coga-b2`; status `assigned`
- Structure: CsCl · B2 · cP2 · Pm-3m (221); type `st:b2-cscl-cp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–2500 K, x(Ga) 0.22551–0.71442
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:coga-b2)

Names (4): _corpus: _corpus:phase:co-ga:coga-b2  
_tdb: _tdb:CoGa-05Su.tdb:COGA_B2, tdb:CoGa-10Cha.tdb:COGA_B2, tdb:CoGa-99Gro.tdb:COGA_B2  


### TDB models of COGA_B2 (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): COGA_B2, type code %, sha256 `d465d6a3ab86a311…`

~~~~text
48: PHASE COGA_B2 % 2 0.5 0.5 !
49: CONST COGA_B2 : CO% VA : CO GA% : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): COGA_B2, type code %, sha256 `d36d75154ff187ec…`

~~~~text
58: PHASE COGA_B2 % 2 0.5 0.5 !
59: CONST COGA_B2 : CO GA% : CO% VA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): COGA_B2, type code %, sha256 `119f21425d794516…`

~~~~text
48: PHASE COGA_B2 % 2 0.5 0.5 !
49: CONST COGA_B2 : CO% VA : CO GA% : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## COGA3 (Co–Ga)

- Id: `phase:co-ga:coga3`; status `assigned`
- Structure: In3Ir · tP16 · P4_2/mnm (136); type `st:in3ir-tp16`; tier B: DFT-supported (unique MP + OQMD match); confidence high
- Stoichiometry: Co 0.2500, Ga 0.7500
- Stability: stable in 3 of 3 calculated diagram(s): 300–1132.33 K, x(Ga) 0.75–0.75
- Literature: 15 values (15 accepted) from 3 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:coga3)

Names (9): _corpus: _corpus:phase:co-ga:coga3  
_mp: _mp:mp-aaaabekt  
_oqmd: _oqmd:oqmd-29254  
_paper: _paper:10.1016/j.calphad.2010.02.004:CoGa3, paper:10.1016/j.intermet.2004.08.003:CoGa3, paper:10.1361/105497199770340608:CoGa3  
_tdb: _tdb:CoGa-05Su.tdb:COGA3, tdb:CoGa-10Cha.tdb:COGA3, tdb:CoGa-99Gro.tdb:COGA3  


### TDB models of COGA3 (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): COGA3, type code %, sha256 `d465d6a3ab86a311…`

~~~~text
53: PHASE COGA3 % 2 1 3 !
54: CONST COGA3 : CO : GA : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): COGA3, type code %, sha256 `d36d75154ff187ec…`

~~~~text
63: PHASE COGA3 % 2 1 3 !
64: CONST COGA3 : CO : GA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): COGA3, type code %, sha256 `119f21425d794516…`

~~~~text
53: PHASE COGA3 % 2 1 3 !
54: CONST COGA3 : CO : GA : !
~~~~

Example references (5 of 5; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/0040-6031(75)85065-9](https://doi.org/10.1016/0040-6031%2875%2985065-9) Bruno Predel, Wolfgang Vogelbein, Udo Schallner, Thermodynamische untersuchung des systems nickel-gallium, Thermochimica Acta 12, 367-375 (1975).  
_cited as the source of values for this phase_
- [doi:10.1016/s0925-8388(97)00223-5](https://doi.org/10.1016/s0925-8388%2897%2900223-5) H. Meyer, M. Ellner, On the solubility of aluminium in the intermetallic compound CoGa3, Journal of Alloys and Compounds 261, 250-253 (1997).  
_cited as the source of values for this phase_

## FCC_A1 (Co–Ga)

- Id: `phase:co-ga:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–1768.99 K, x(Ga) 0–0.19684
- Literature: 12 values (12 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:fcc-a1)

Names (6): _corpus: _corpus:phase:co-ga:fcc-a1  
_paper: _paper:10.1016/j.calphad.2010.02.004:fcc, paper:10.1016/j.intermet.2004.08.003:(αCo)  
_tdb: _tdb:CoGa-05Su.tdb:FCC_A1, tdb:CoGa-10Cha.tdb:FCC_A1, tdb:CoGa-99Gro.tdb:FCC_A1  


### TDB models of FCC_A1 (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): FCC_A1, type code %A, sha256 `d465d6a3ab86a311…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% GA : VA : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): FCC_A1, type code %A, sha256 `d36d75154ff187ec…`

~~~~text
38: PHASE FCC_A1 %A 2 1 1 !
39: CONST FCC_A1 : CO% GA : VA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): FCC_A1, type code %A, sha256 `119f21425d794516…`

~~~~text
28: PHASE FCC_A1 %A 2 1 1 !
29: CONST FCC_A1 : CO% GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## HCP_A3 (Co–Ga)

- Id: `phase:co-ga:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 300–701.98 K, x(Ga) 0–0.10938
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:hcp-a3)

Names (4): _corpus: _corpus:phase:co-ga:hcp-a3  
_tdb: _tdb:CoGa-05Su.tdb:HCP_A3, tdb:CoGa-10Cha.tdb:HCP_A3, tdb:CoGa-99Gro.tdb:HCP_A3  


### TDB models of HCP_A3 (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): HCP_A3, type code %A, sha256 `d465d6a3ab86a311…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% GA : VA : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): HCP_A3, type code %A, sha256 `d36d75154ff187ec…`

~~~~text
48: PHASE HCP_A3 %A 2 1 0.5 !
49: CONST HCP_A3 : CO% GA : VA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): HCP_A3, type code %A, sha256 `119f21425d794516…`

~~~~text
38: PHASE HCP_A3 %A 2 1 0.5 !
39: CONST HCP_A3 : CO% GA : VA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## LIQUID (Co–Ga)

- Id: `phase:co-ga:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 3 of 3 calculated diagram(s): 302.91–2500 K, x(Ga) 0–1
- Literature: 20 values (20 accepted) from 2 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:co-ga:liquid)

Names (6): _corpus: _corpus:phase:co-ga:liquid  
_paper: _paper:10.1016/j.calphad.2010.02.004:Liq., paper:10.1016/j.intermet.2004.08.003:Liq.  
_tdb: _tdb:CoGa-05Su.tdb:LIQUID, tdb:CoGa-10Cha.tdb:LIQUID, tdb:CoGa-99Gro.tdb:LIQUID  


### TDB models of LIQUID (3): PHASE and CONSTITUENT statements as written

[CoGa-05Su.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-05Su.tdb): LIQUID, type code %, sha256 `d465d6a3ab86a311…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO GA : !
~~~~

[CoGa-10Cha.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-10Cha.tdb): LIQUID, type code %, sha256 `d36d75154ff187ec…`

~~~~text
33: PHASE LIQUID:L % 1 1 !
34: CONST LIQUID:L : CO GA : !
~~~~

[CoGa-99Gro.tdb](https://orchid-project.org/data/databases/sgte-binary/CoGa-99Gro.tdb): LIQUID, type code %, sha256 `119f21425d794516…`

~~~~text
23: PHASE LIQUID:L % 1 1 !
24: CONST LIQUID:L : CO GA : !
~~~~

Example references (3 of 3; assessments first): 

- [doi:10.1016/j.calphad.2010.02.004](https://doi.org/10.1016/j.calphad.2010.02.004) Arpita Chari, Andres Garay, Raymundo Arróyave, Thermodynamic remodeling of the Co–Ga system, Calphad 34, 189-195 (2010).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1016/j.intermet.2004.08.003](https://doi.org/10.1016/j.intermet.2004.08.003) Xuping Su, Jean-Claude Tedenac, Thermodynamic modeling of the cobalt–gallium system, Intermetallics 13, 467-473 (2005).  
_assessment that models this phase; reports values for this phase_
- [doi:10.1361/105497199770340608](https://doi.org/10.1361/105497199770340608) J. Gröbner, R. Wenzel, G. G. Fischer, R. Schmid-Fetzer, Thermodynamic calculation of the binary systems M-Ga and investigation of ternary M-Ga-N phase equilibria (M=Ni, Co, Pd, Cr), JPE 20, 615-625 (1999).  
_assessment that models this phase_

## Please cite

- R. Arróyave, J. Saal, D. Shin, ORCHID phase registry (binary systems) (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-phase-registry
- R. Arróyave, J. Saal, D. Shin, ORCHID data (version 2026.10; Version 1, machine-extracted), Zenodo (2026). https://doi.org/10.5281/zenodo.PENDING-orchid-data

Also cite B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, https://doi.org/10.1016/j.calphad.2025.102833 (CC BY 4.0), and the original assessment named in each file; A. Jain et al., The Materials Project: A materials genome approach to accelerating materials innovation, APL Materials 1 (2013) 011002, https://doi.org/10.1063/1.4812323 (CC BY 4.0); J. E. Saal et al., JOM 65 (2013) 1501, https://doi.org/10.1007/s11837-013-0755-4 and S. Kirklin et al., npj Comput. Mater. 1 (2015) 15010, https://doi.org/10.1038/npjcompumats.2015.10 (CC BY 4.0); the original source of every value you use (paper_citation / paper_doi, and cited_dois for values the paper cites from earlier work).

Version 1, machine-extracted: values were read from papers by language-model readers constrained to quote their source and checked automatically (quote verification, field-placement rule, printed-page sign checks, DFT and Kim et al. 2017 cross-checks); a hand-checked precision sample is in progress.

```bibtex
@misc{orchid_phase_registry_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID phase registry (binary systems)}},
  version   = {2026.10},
  publisher = {Zenodo},
  year      = {2026},
  doi       = {10.5281/zenodo.PENDING-phase-registry},
  url       = {https://doi.org/10.5281/zenodo.PENDING-phase-registry},
  note      = {Version 1, machine-extracted}
}

@misc{orchid_data_2026,
  author    = {Arr{\'o}yave, Raymundo and Saal, James and Shin, Dongwon},
  title     = {{ORCHID data}},
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
