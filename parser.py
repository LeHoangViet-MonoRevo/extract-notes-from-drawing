from typing import List
import re

class DrawingNotesParser:
    """
    1. Remove duplicates.
    2. Keep the results in the correct format.
    """
    
    @staticmethod
    def run(raw_text: str) -> List[str]:
        if not raw_text or not isinstance(raw_text, str):
            return []

        # 1. Extract quoted strings safely (even from broken JSON)
        #    This avoids json.loads crashing on malformed input
        candidates = re.findall(r'"([^"\n]+)"', raw_text)

        # 2. Normalize & clean
        cleaned = []
        for text in candidates:
            text = text.strip()

            # drop clearly broken fragments
            if len(text) < 2:
                continue

            cleaned.append(text)

        # 3. Deduplicate while preserving order
        seen = set()
        result = []
        for text in cleaned:
            if text not in seen:
                seen.add(text)
                result.append(text)

        return result



if __name__ == "__main__":
    from test_data import *

    raw_texts = [
        raw_text1, raw_text2, raw_text3, raw_text4, raw_text5,
        raw_text6, raw_text7, raw_text8, raw_text9, raw_text10,
        raw_text11, raw_text12, raw_text13, raw_text14, raw_text15,
        raw_text16, raw_text17, raw_text17, raw_text18, raw_text19,
        raw_text20
    ]

    output_file = "parsed_drawing_notes.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for idx, text in enumerate(raw_texts):
            processed = DrawingNotesParser.run(text)

            f.write(f"==============================\n")
            f.write(f"INDEX: {idx}\n")
            f.write(f"RAW TEXT:\n{text}\n\n")
            f.write(f"PARSED OUTPUT:\n{processed}\n\n")

    print(f"✅ Parsing completed. Results written to {output_file}")