import re
from typing import List




def parse_notes_content_only(raw_text: str) -> list[str]:
    if not raw_text:
        return []

    # Remove LLM header
    text = re.sub(
        r"^Here are the notes extracted from.*?:\s*",
        "",
        raw_text.strip(),
        flags=re.IGNORECASE | re.DOTALL,
    )

    results = []

    lines = text.splitlines()
    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Skip numbered titles like "1. **General Notes:**"
        if re.match(r"\d+\.\s*\*\*.*\*\*:?", line):
            continue

        # Skip incomplete titles without bullets
        if re.match(r"\d+\.\s*\*\*.*$", line):
            continue

        # Capture bullet content
        m = re.match(r"[-•]\s*(.+)", line)
        if m:
            results.append(m.group(1).strip())
            continue

        # Capture standalone numbered content (for other samples)
        m = re.match(r"\d+\.\s*(.+)", line)
        if m:
            results.append(m.group(1).strip())

    return results


print(parse_notes_content_only(raw_text))
