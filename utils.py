import re


def remove_unicode_chars(content):
    content_clean = (
        content.replace("\\xe2\\x80\\x93", "-")
        .replace("\\xc3\\xa3", "ã")
        .replace("\\xc3\\xa9", "é")
        .replace("\\xc3\\xad", "í")
        .replace("\\xc3\\xb4", "ô")
    )

    return str(content_clean)


def clean_text(content):
    content_clean = re.sub(r"\\", "", content)
    content_clean = re.sub(r"\[.\]", "", content_clean)
    content_clean = re.sub(r"ofS", "of S", content_clean)
    content_clean = re.sub(r"Republicof", "Republic of", content_clean)

    return content_clean
