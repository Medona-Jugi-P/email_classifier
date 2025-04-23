import re

PII_PATTERNS = {
    "full_name": r"\bMy name is ([A-Z][a-z]+(?: [A-Z][a-z]+)*)",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone_number": r"\b(?:\+91[-\s]?)?[789]\d{9}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2})\b"
}

def mask_pii(text):
    masked_entities = []
    original_text = text

    for label, pattern in PII_PATTERNS.items():
        matches = list(re.finditer(pattern, text))
        for match in matches:
            original_value = match.group(0)
            start, end = match.start(), match.end()
            masked_entities.append({
                "position": [start, end],
                "classification": label,
                "entity": original_value
            })
            text = text.replace(original_value, f"[{label}]")
    
    return text, masked_entities, original_text
