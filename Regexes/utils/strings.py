import re
regexes = {
    "email": re.compile(
        r"[\w.+-]+@[\w-]+\.[\w.-]+",
        re.IGNORECASE,
    ),
    "ip": re.compile(
        r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
        re.IGNORECASE,
    ),
    "ipv6": re.compile(
        r"\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*",
        re.VERBOSE | re.IGNORECASE | re.DOTALL,
    ),
    "price": re.compile(
        r"[$]\s?[+-]?[0-9]{1,3}(?:(?:,?[0-9]{3}))*(?:\.[0-9]{1,2})?"
    ),
    "hex_color": re.compile(
        r"(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\b"
    ),
    "credit_card": re.compile(
        r"((?:(?:\d{4}[- ]?){3}\d{4}|\d{15,16}))(?![\d])"
    ),
    "btc_address": re.compile(
        r"(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])"
    ),
    "street_address": re.compile(
        r"\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)",
        re.IGNORECASE,
    ),
    "zip_code": re.compile(
        r"\b\d{5}(?:[-\s]\d{4})?\b"
    ),
    "po_box": re.compile(
        r"P\.? ?O\.? Box \d+",
        re.IGNORECASE,
    ),
    "ssn": re.compile(
        r"(?!000|666|333)0*(?:[0-6][0-9][0-9]|[0-7][0-6][0-9]|[0-7][0-7][0-2])[- ](?!00)[0-9]{2}[- ](?!0000)[0-9]{4}"
    ),
    # Yeni eklenen regex'ler:
    "nested_parentheses": re.compile(
        r"\([^()]*\)"
    ),
    "negative_lookahead": re.compile(
        r"^(?!.*forbidden).*$"
    ),
    "non_ascii": re.compile(
        r"[^\x00-\x7F]+"
    ),
    "multiline_comment": re.compile(
        r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/"
    ),
    "html_tags": re.compile(
        r"<(div|span|p)\b[^>]*>(.*?)</\1>"
    ),
    "palindrome": re.compile(
        r"\b(\w)(\w)?(\w)?\w?\3\2\1\b"
    ),
    # Diğer örnek regex'ler
    "date": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "time": re.compile(r"^\d{2}:\d{2}:\d{2}$"),
    "phone": re.compile(r"^\+?[\d\s\-]{7,15}$"),
}


