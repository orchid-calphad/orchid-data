# Pr–Si phases

> Pr–Si system: 12 phases (tier A 7, tier C 3, liquid 1, needs_review 1); 10 stable in a calculated diagram in the ORCHID phase registry, with names, structure type when certain, calculated stability, verbatim TDB PHASE/CONSTITUENT statements and example references.

HTML: https://data.orchid-project.org/phases/pages/PR-SI.html · Markdown: https://data.orchid-project.org/phases/pages/PR-SI.md

12 phases (tier A 7, tier C 3, liquid 1, needs_review 1); 10 stable in a calculated diagram. Structure types are assigned only when certain (tier A: standard phase name; tier B: unique Materials Project + OQMD on-hull match, DFT-supported; tier C: one structure stated by the assessment's crystallographic table, assessor-stated); other phases list candidates and are marked needs_review. Stability is from phase diagrams calculated with pycalphad from the SGTE binary collection (evidence class: model).

Data: [interactive registry](https://orchid-project.org/phases/?q=PR-SI) · [full JSON](https://data.orchid-project.org/phases/systems/PR-SI.json) · [Pr–Si system page](https://data.orchid-project.org/systems/PR-SI.html) · [Markdown](https://data.orchid-project.org/phases/pages/PR-SI.md) · [field reference](https://data.orchid-project.org/phases/SCHEMA.md)

Table: Phases of the Pr–Si system (12)

| Phase | Structure | Basis | Stability (calculated) | Literature values | TDB models |
|---|---|---|---|---:|---:|
| [DIAMOND_A4](#phase-pr-si-a4-diamond); _phase:pr-si:a4-diamond_ | C (diamond) · A4 · cF8 · Fd-3m (227) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1687 K, x(Si) 1–1 | 0 | 1 |
| [BCC_A2](#phase-pr-si-bcc-a2); _phase:pr-si:bcc-a2_ | W · A2 · cI2 · Im-3m (229) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 1063.88–1208.88 K, x(Si) 0–0.00135 | 0 | 1 |
| [DHCP](#phase-pr-si-dhcp-a3); _phase:pr-si:dhcp-a3_ | alpha-La · A3' · hP4 · P6_3/mmc (194) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1136.75 K, x(Si) 0–0 | 0 | 1 |
| [FCC_A1](#phase-pr-si-fcc-a1); _phase:pr-si:fcc-a1_ | Cu · A1 · cF4 · Fm-3m (225) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [HCP_A3](#phase-pr-si-hcp-a3); _phase:pr-si:hcp-a3_ | Mg · A3 · hP2 · P6_3/mmc (194) | tier A: standard phase name | not stable in 1 calculated diagram(s) | 0 | 1 |
| [LIQUID](#phase-pr-si-liquid); _phase:pr-si:liquid_ | liquid | liquid | stable in 1 of 1 calculated diagram(s): 1003.93–2500 K, x(Si) 0–1 | 0 | 1 |
| [PR3SI4](#phase-pr-si-pr3si4); _phase:pr-si:pr3si4_ | V2B3 · oC20 · Cmcm (63) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1618.25 K, x(Si) 0.57143–0.57143 | 1 | 1 |
| [PR5SI3_D8L](#phase-pr-si-pr5si3-d8l); _phase:pr-si:pr5si3-d8l_ | Cr5B3 · D8_l · tI32 · I4/mcm (140) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1670.8 K, x(Si) 0.375–0.375 | 0 | 1 |
| [PR5SI4](#phase-pr-si-pr5si4); _phase:pr-si:pr5si4_ | Si4Zr5 · tP36 · P4_12_12 (92) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–1795.19 K, x(Si) 0.44444–0.44444 | 1 | 1 |
| [PR5SI9_ALPHA](#phase-pr-si-pr5si9-alpha); _phase:pr-si:pr5si9-alpha_ | Gd5Si4 · oP36 · Pnma (62) | tier C: assessor-stated (Hallstedt 2025 crystallographic table) | stable in 1 of 1 calculated diagram(s): 300–305.34 K, x(Si) 0.64286–0.64286 | 0 | 1 |
| [PR5SI9_CC](#phase-pr-si-pr5si9-cc); _phase:pr-si:pr5si9-cc_ |  | needs_review | stable in 1 of 1 calculated diagram(s): 305.34–1972.55 K, x(Si) 0.64286–0.64286 | 0 | 1 |
| [PRSI_B27](#phase-pr-si-prsi-b27); _phase:pr-si:prsi-b27_ | FeB · B27 · oP8 · Pnma (62) | tier A: standard phase name | stable in 1 of 1 calculated diagram(s): 300–1933.48 K, x(Si) 0.5–0.5 | 0 | 1 |

## DIAMOND_A4 (Pr–Si)

- Id: `phase:pr-si:a4-diamond`; status `assigned`
- Structure: C (diamond) · A4 · cF8 · Fd-3m (227); type `st:a4-c-diamond-cf8`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1687 K, x(Si) 1–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:a4-diamond)

Names (2): _corpus: _corpus:phase:pr-si:a4-diamond  
_tdb: _tdb:PrSi-20Xu.tdb:DIAMOND_A4  


### TDB models of DIAMOND_A4 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): DIAMOND_A4, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
45: PHASE DIAMOND_A4 % 1 1 !
46: CONST DIAMOND_A4 : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## BCC_A2 (Pr–Si)

- Id: `phase:pr-si:bcc-a2`; status `assigned`
- Structure: W · A2 · cI2 · Im-3m (229); type `st:a2-w-ci2`; tier A: standard phase name; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1063.88–1208.88 K, x(Si) 0–0.00135
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:bcc-a2)

Names (2): _corpus: _corpus:phase:pr-si:bcc-a2  
_tdb: _tdb:PrSi-20Xu.tdb:BCC_A2  


### TDB models of BCC_A2 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): BCC_A2, type code %B, sha256 `5164e34ad4f5ccca…`

~~~~text
30: PHASE BCC_A2 %B 2 1 3 !
31: CONST BCC_A2 : PR% SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## DHCP (Pr–Si)

- Id: `phase:pr-si:dhcp-a3`; status `assigned`
- Structure: alpha-La · A3' · hP4 · P6_3/mmc (194); type `st:a3-alpha-la-hp4`; tier A: standard phase name; confidence high
- Stoichiometry: Pr 1.0000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1136.75 K, x(Si) 0–0
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:dhcp-a3)

Names (2): _corpus: _corpus:phase:pr-si:dhcp-a3  
_tdb: _tdb:PrSi-20Xu.tdb:DHCP  


### TDB models of DHCP (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): DHCP, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
40: PHASE DHCP % 1 1 !
41: CONST DHCP : PR : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## FCC_A1 (Pr–Si)

- Id: `phase:pr-si:fcc-a1`; status `assigned`
- Structure: Cu · A1 · cF4 · Fm-3m (225); type `st:a1-cu-cf4`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:fcc-a1)

Names (2): _corpus: _corpus:phase:pr-si:fcc-a1  
_tdb: _tdb:PrSi-20Xu.tdb:FCC_A1  


### TDB models of FCC_A1 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): FCC_A1, type code %A, sha256 `5164e34ad4f5ccca…`

~~~~text
25: PHASE FCC_A1 %A 2 1 1 !
26: CONST FCC_A1 : SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## HCP_A3 (Pr–Si)

- Id: `phase:pr-si:hcp-a3`; status `assigned`
- Structure: Mg · A3 · hP2 · P6_3/mmc (194); type `st:a3-mg-hp2`; tier A: standard phase name; confidence high
- Stoichiometry: Si 1.0000
- Stability: not stable in 1 calculated diagram(s)
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:hcp-a3)

Names (2): _corpus: _corpus:phase:pr-si:hcp-a3  
_tdb: _tdb:PrSi-20Xu.tdb:HCP_A3  


### TDB models of HCP_A3 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): HCP_A3, type code %A, sha256 `5164e34ad4f5ccca…`

~~~~text
35: PHASE HCP_A3 %A 2 1 0.5 !
36: CONST HCP_A3 : SI : VA : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## LIQUID (Pr–Si)

- Id: `phase:pr-si:liquid`; status `assigned`
- Structure: liquid; type `st:liquid`; liquid; confidence high
- Stability: stable in 1 of 1 calculated diagram(s): 1003.93–2500 K, x(Si) 0–1
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:liquid)

Names (2): _corpus: _corpus:phase:pr-si:liquid  
_tdb: _tdb:PrSi-20Xu.tdb:LIQUID  


### TDB models of LIQUID (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): LIQUID, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
20: PHASE LIQUID:L % 1 1 !
21: CONST LIQUID:L : PR SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## PR3SI4 (Pr–Si)

- Id: `phase:pr-si:pr3si4`; status `assigned`
- Structure: V2B3 · oC20 · Cmcm (63); type `st:v2b3-oc20`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pr 0.4286, Si 0.5714
- Stability: stable in 1 of 1 calculated diagram(s): 300–1618.25 K, x(Si) 0.57143–0.57143
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:pr3si4)

Names (3): _corpus: _corpus:phase:pr-si:pr3si4  
_paper: _paper:10.1111/jace.17031:Pr3Si4  
_tdb: _tdb:PrSi-20Xu.tdb:PR3SI4  


### TDB models of PR3SI4 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): PR3SI4, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
65: PHASE PR3SI4 % 2 3 4 !
66: CONST PR3SI4 : PR : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase; reports values for this phase_

## PR5SI3_D8L (Pr–Si)

- Id: `phase:pr-si:pr5si3-d8l`; status `assigned`
- Structure: Cr5B3 · D8_l · tI32 · I4/mcm (140); type `st:d8-l-cr5b3-ti32`; tier A: standard phase name; confidence high
- Stoichiometry: Pr 0.6250, Si 0.3750
- Stability: stable in 1 of 1 calculated diagram(s): 300–1670.8 K, x(Si) 0.375–0.375
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:pr5si3-d8l)

Names (2): _corpus: _corpus:phase:pr-si:pr5si3-d8l  
_tdb: _tdb:PrSi-20Xu.tdb:PR5SI3_D8L  


### TDB models of PR5SI3_D8L (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): PR5SI3_D8L, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
50: PHASE PR5SI3_D8L % 2 5 3 !
51: CONST PR5SI3_D8L : PR : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## PR5SI4 (Pr–Si)

- Id: `phase:pr-si:pr5si4`; status `assigned`
- Structure: Si4Zr5 · tP36 · P4_12_12 (92); type `st:si4zr5-tp36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_on_hull_entry_in_both, no_structure_token); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pr 0.5556, Si 0.4444
- Stability: stable in 1 of 1 calculated diagram(s): 300–1795.19 K, x(Si) 0.44444–0.44444
- Literature: 1 values (1 accepted) from 1 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:pr5si4)

Names (3): _corpus: _corpus:phase:pr-si:pr5si4  
_paper: _paper:10.1111/jace.17031:Pr5Si4  
_tdb: _tdb:PrSi-20Xu.tdb:PR5SI4  


### TDB models of PR5SI4 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): PR5SI4, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
55: PHASE PR5SI4 % 2 5 4 !
56: CONST PR5SI4 : PR : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase; reports values for this phase_

## PR5SI9_ALPHA (Pr–Si)

- Id: `phase:pr-si:pr5si9-alpha`; status `assigned`
- Structure: Gd5Si4 · oP36 · Pnma (62); type `st:gd5si4-op36`; tier C: assessor-stated (Hallstedt 2025 crystallographic table); confidence assessor-stated
- Structure source: B. Hallstedt, The SGTE collection of binary datasets, Calphad 89 (2025) 102833, supplementary crystallographic table (mmc2) [doi:10.1016/j.calphad.2025.102833](https://doi.org/10.1016/j.calphad.2025.102833)
- Caveat: not certain from the name or DFT alone (no_structure_token, polymorph_family:other phases of this system have the same composition); structure as stated in the SGTE crystallographic table for this phase name and system
- Stoichiometry: Pr 0.3571, Si 0.6429
- Stability: stable in 1 of 1 calculated diagram(s): 300–305.34 K, x(Si) 0.64286–0.64286
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:pr5si9-alpha)

Names (2): _corpus: _corpus:phase:pr-si:pr5si9-alpha  
_tdb: _tdb:PrSi-20Xu.tdb:PR5SI9_ALPHA  


### TDB models of PR5SI9_ALPHA (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): PR5SI9_ALPHA, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
70: PHASE PR5SI9_ALPHA % 2 5 9 !
71: CONST PR5SI9_ALPHA : PR : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## PR5SI9_CC (Pr–Si)

- Id: `phase:pr-si:pr5si9-cc`; status `needs_review`
- No structure assigned. Why: assessment_declared_blocked_by:stoichiometry_contradicts_C_c; stoichiometry_contradicts_C_c:PrSi-20Xu.tdb
- Candidate (name_token): Si2Th · C_c · tI12 · I4_1/amd (141) — Strukturbericht/word 'CC' in the TDB name
- Candidate (sgte_mmc2): Si2Th · C_c · tI12 · I4_1/amd (141) — Hallstedt 2025 mmc2 row for PR5SI9_CC: Pr5Si9 (high T)
- Candidate (tdb_comment): Si2Th · tI12 · I4_1/amd — PrSi-20Xu.tdb: 'Prototype Si2Th (tI12, I4_1/amd)'
- Stoichiometry: Pr 0.3571, Si 0.6429
- Stability: stable in 1 of 1 calculated diagram(s): 305.34–1972.55 K, x(Si) 0.64286–0.64286
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:pr5si9-cc)

Names (2): _corpus: _corpus:phase:pr-si:pr5si9-cc  
_tdb: _tdb:PrSi-20Xu.tdb:PR5SI9_CC  


### TDB models of PR5SI9_CC (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): PR5SI9_CC, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
75: PHASE PR5SI9_CC % 2 5 9 !
76: CONST PR5SI9_CC : PR : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
_assessment that models this phase_

## PRSI_B27 (Pr–Si)

- Id: `phase:pr-si:prsi-b27`; status `assigned`
- Structure: FeB · B27 · oP8 · Pnma (62); type `st:b27-feb-op8`; tier A: standard phase name; confidence high
- Caveat: DFT agrees: on-hull mp-aaaaaotk and oqmd-7935, space group 62
- Stoichiometry: Pr 0.5000, Si 0.5000
- Stability: stable in 1 of 1 calculated diagram(s): 300–1933.48 K, x(Si) 0.5–0.5
- Literature: 0 values (0 accepted) from 0 papers
- Interactive: [phase registry entry](https://orchid-project.org/phases/#phase:pr-si:prsi-b27)

Names (4): _corpus: _corpus:phase:pr-si:prsi-b27  
_mp: _mp:mp-aaaaaotk  
_oqmd: _oqmd:oqmd-7935  
_tdb: _tdb:PrSi-20Xu.tdb:PRSI_B27  


### TDB models of PRSI_B27 (1): PHASE and CONSTITUENT statements as written

[PrSi-20Xu.tdb](https://orchid-project.org/data/databases/sgte-binary/PrSi-20Xu.tdb): PRSI_B27, type code %, sha256 `5164e34ad4f5ccca…`

~~~~text
60: PHASE PRSI_B27 % 2 1 1 !
61: CONST PRSI_B27 : PR : SI : !
~~~~

Example references (1 of 1; assessments first): 

- [doi:10.1111/jace.17031](https://doi.org/10.1111/jace.17031) Kai Xu, Keke Chang, Xiaobing Zhou, Leilei Chen, Junwen Liu, Zixuan Deng et al., Thermodynamic descriptions of the light rare‐earth elements in silicon carbide ceramics, J Am Ceram Soc 103, 3812-3825 (2020).  
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
