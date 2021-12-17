import re


def remove_unicode_chars(content):
    """

    Remove unicode characters by replacing them with ascii equivalent
    @param content: The content to be midified
    @returns: Same content as the input with modified unicode characters

    """

    content_clean = (
        content.replace("\\xe2\\x80\\x93", "-")
        .replace("\\xc3\\xa3", "ã")
        .replace("\\xc3\\xa9", "é")
        .replace("\\xc3\\xad", "í")
        .replace("\\xc3\\xb4", "ô")
        .replace("\\xc3\\xba", "ú")
        .replace("\\xc3\\xb3", "ó")
        .replace("\\xc3\\xa1", "á")
    )

    return str(content_clean)


def clean_text(content):
    """
    Replace some characters
    @param content: The content to be midified
    @returns: Same content as the input with deleted or modifed unusual characters
    """
    content_clean = re.sub(r"\\", "", content)
    content_clean = re.sub(r"\[.\]", "", content_clean)
    content_clean = re.sub(r"ofS", "of S", content_clean)
    content_clean = re.sub(r"Republicof", "Republic of", content_clean)

    return content_clean


def clean_number(content):
    content_clean = content.strip()
    content_clean = re.sub(r" million", "000000", content)
    content_clean = re.sub(r"[a-zA-Z]+|\.", "", content_clean)
    content_clean = re.sub(r"\\n", "", content_clean)
    content_clean = re.sub(r"\[\]|\\", "", content_clean)
    content_clean = re.sub(r"\(.+?\)", "", content_clean)
    content_clean = re.sub(r"\[.+?\]", "", content_clean)
    content_clean = re.sub(r",", "", content_clean)
    content_clean = re.sub(r"[0-9][0-9]-", "", content_clean)
    content_clean = re.sub(r"[0-9][0-9]-", "", content_clean)

    if " " in content_clean:
        content_clean = content_clean[: content_clean.index(" ")]

    return content_clean


def clear_density(content):
    content_clean = content.strip()
    content_clean = re.sub(r"/km.+?", "", content_clean)
    content_clean = re.sub(r"\(.+?\)", "", content_clean)
    content_clean = re.sub(r"\[.+?\]", "", content_clean)
    content_clean = re.sub(r"/sq\\xc2\\xa0mi  ", "", content_clean)
    content_clean = re.sub(r" or .*$", "", content_clean)
    content_clean = re.sub(r",", "", content_clean)

    return content_clean
