raw_text1 = """
Here are the notes extracted from the drawing:

1. 注記：指示無き各技は糸面取り(C0.2以下)の事
   - バリ、カエリ無き事
   - 指示無きタップは全て転造タップの事
   - 外観美を要す
   - 表面に色むら無き事

2. 165×149.5 mm²

3. 20×179×222

4. 納期：1/7

5. 個数：1

6. 仕様：SRⅢ200

7. 材質：NIN20A-15-0003

8. 白アルマイト

9. 12

10. 作業
"""

raw_text2 = """
Here are the notes extracted from the drawing:

1. 注1) BとCの溝は、角度位置が正確であること。
2. また、3XM4も角度位置が正確であること。
3. 注2) 切断面ガエリ無きこと。
4. 注3) 元図面: RW40-S-1613 中間ツメガイド

These notes provide additional information about the dimensions and tolerances of the part, as well as instructions for manufacturing and inspection.
"""

raw_text3 = """
Here are the notes extracted from the given drawing:

1. **General Notes:**
   - 4-M5通L
   - 30
   - 042 R20
   - 030H8
   - S.P (XZ5.0/18.0)
   - 106
   - 81
   - 18
   - 25
   - 50
   - 7.5
   - 35
   - 2-M6深さ12
   - 20°
   - φ11.5 (20°穴)
   - 18分
   - 7-169
   - 6F

2. **Surface Treatment:**
   - SS400FD-t16*50

3. **Material and Surface Finish
"""

raw_text4 = """
The notes in the drawing are as follows:

1. **General Notes:**
   - H7穴はタフラム不可 (H7 hole is not allowed to use a taphole.)

2. **Specific Notes:**
   - 4箇所被線R0.2のこと (Four places with a line of R0.2.)
   - 2-3.4±9,6.5座り限3.3 (2-3.4 ± 9, 6.5 limit 3.3)
   - R11.81~R11.83 (R11.81~R11.83)
   - S.P (S.P)
   - 25×35.5×37 (25×35.5×37)
   - 3/5 (3/5)
   -
"""


raw_text5 = """
The notes in the drawing are as follows:

1. **尺寸标注**:
   - 43.3 mm
   - 63.5 mm
   - 20.5 mm
   - 7.54 mm

2. **公差**:
   - ±0.3 mm
   - ±0.2 mm
   - ±0.1 mm

3. **材料**:
   - SS400

4. **表面处理**:
   - 镀锌

5. **规格**:
   - 63.5 x 43.3 x 19 mm

6. **重量**:
   - 1 kg

7. **编号**:
   - 100410866V00

These notes provide detailed information about the dimensions, tolerances, material, surface treatment, specifications, weight, and identification
"""


raw_text6 = """
Here are the notes extracted from the given drawing:

1. **Material**: SUS304F
2. **Surface Treatment**: None (空白)
3. **Drawing Number**: SKA27410102
4. **Part Name**: L八一
5. **Scale**: 1:1
6. **Quantity**: 1
7. **Drawing Number**: DWG.NO
8. **Part Number**: PART NO
9. **Material**: SUS304F
10. **Surface Treatment**: None (空白)
11. **Drawing Number**: SKA27410102
12. **Part Name**: L八一
13. **Scale**: 1:1
14. **Quantity**: 1
15. **Drawing Number**: DWG.NO
16. **Part Number**: PART NO

These notes provide details about
"""

raw_text7 = """

"""

raw_text8 = """
Here are the notes extracted from the drawing:

1. **R3** - Indicates a radius of 3mm at the corner.
2. **65 x 57 x 62 同一元杆** - Indicates a dimension of 65x57x62 mm for the same rod.
3. **納期 9/12 1600 個数 16+(1)** - Indicates the delivery date is September 12, 2022, with 1600 pieces and an additional piece.
4. **この面の角の上もR3でなめらかな事** - Indicates that the corners on this face should also be rounded to a smooth finish.
5. **S.P** - Indicates a specific point or measurement.
6. **R3** - Indicates another radius of 3mm.
7. **R3** -
"""

raw_text9 = """
Here are the notes extracted from the given drawing:

1. **Designation**: SUS304
2. **Material**: SUS304P
3. **Surface Treatment**: None (空白)
4. **Part Name**: ス夕ソド
5. **Drawing Number**: MJ180107112A
6. **Scale**: 1:1
7. **Roughness**: 6.3
8. **Surface Treatment**: SURFACE TREATMENT
9. **Finish Tolerance**: FINISHING TOLERANCE
10. **Material**: SUS304P
11. **Roughness**: 6.3
12. **Surface Treatment**: SURFACE TREATMENT
13. **Part Name**: ス夕ソド
14. **Drawing Number**: MJ180107112A
15. **
"""

raw_text10 = """
Here are the notes extracted from the given drawing:

1. **Note 1:**
   - Location: Near the top right corner of the drawing.
   - Content: "12.5(3.2/6.3)"

2. **Note 2:**
   - Location: Near the bottom left corner of the drawing.
   - Content: "1.指示なき各様は糸面取りのこと。
   2.パリカエリ無こと。"

3. **Note 3:**
   - Location: Near the center of the drawing.
   - Content: "600100851車L-036"

4. **Note 4:**
   - Location: Near the bottom right corner of the drawing.
   - Content: "1/5~16"
   - Additional Note: "SUS304W01"

These notes
"""

raw_text11 = """
Here are the notes extracted from the drawing:

1. (注) 玉み無き事
2. (注) 指示無き角部は全てR0.5とする
3. (注) 端部ベーバー仕上げの事
4. (注) パリ無き事
"""

raw_text12 = """

"""

raw_text13 = """
Here are the notes extracted from the given drawing:

1. 注4) R1/2
2. 注3.5) NPT1/2
3. 注3) 29°0.33
4. 注2) 27.5
5. 注1) 普通公差 JIS B 0419-mH
6. 注1) 指示無き角部はC0.2orR0.4のこと
7. 注3) CAS-00742-P43とNPTネジ及び
8. 注4) φ21.6が異なる
9. 注5) Rおよびの測定はCIS-L-105-101による
10. 注5) NPTめれじの測定はCIS-L-105-104による
"""

raw_text14 = """
The notes in the drawing are as follows:

1. G3/4ネジとの直角度に注意 (Attention: Perpendicularity to G3/4 bolt)
2. 30° (30° angle)
3. 30° (30° angle)
4. G3/4 (G3/4 bolt)
5. G3/4ネジとの直角度に注意 (Attention: Perpendicularity to G3/4 bolt)
6. 3.5±0.25 (3.5 ± 0.25)
7. 16 (16)
8. 20.5 (20.5)
9. 17 (17)
10. 20.5 (20.5)
11. 36 (36)
12. 36 (36)
13. 16 (
"""

raw_text15 = """

"""

raw_text16 = """
Here are the notes extracted from the given drawing:

1. **Surface Finish:**
   - Ra 25 (for surface C0.1 to C0.2)

2. **Material:**
   - SCM435 (quenched and tempered)

3. **Title:**
   - Shaft Driver

4. **Approval:**
   - Date: 14.08.08
   - Name: 橋本サ (Higashimasa)
   - Signature: 市川 (Ichikawa)

5. **Drawing Number:**
   - 100-002-6549-00

6. **Scale:**
   - 1:1

7. **Note:**
   - Shall not exceed threshold of restricted substances in RoHS_D.
"""

raw_text17 = """
Here are the notes extracted from the given drawing:

1. **Note 1:**
   - **Location:** Top left corner of the drawing.
   - **Text:** "イメージ発行日：22/11/10 06:34"

2. **Note 2:**
   - **Location:** Near the top right corner of the drawing.
   - **Text:** "1) 端面C0.1～C0.2 デ面取り"

3. **Note 3:**
   - **Location:** Near the bottom center of the drawing.
   - **Text:** "60-0021-03 図卜勝手反対ノモノ"
   - **Additional Text:** "60-0020-00 本図通リノモノ"

4. **Note 4:**
   - **Location:**
"""
