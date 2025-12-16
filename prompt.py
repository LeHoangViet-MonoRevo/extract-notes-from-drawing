prompt = """
Extract ONLY designer instruction notes from the drawing.

Definition of "note":
A note is a sentence or phrase that:
- Contains keywords such as:
  注意, 注記, 注, 備考, NOTE, NOTES, NOTICE, REMARK
- Or clearly expresses instructions, cautions, or requirements written for humans

Do NOT extract:
- Dimensions, sizes, angles, tolerances
- Part numbers, quantities, material names
- Surface treatment names
- Table headers or section titles
- Any numeric-only values

Output rules (VERY IMPORTANT):
- Output MUST be a JSON array of strings
- Each string is ONE note
- Remove numbering like "1.", "注1)", "NOTE-1"
- Remove bullets, symbols, and markdown
- Preserve original language (do NOT translate)
- Do NOT add explanations
- If no notes are found, output an empty array []

Example output:
[
  "切断面ガエリ無きこと",
  "BとCの溝は角度位置が正確であること"
]
"""
