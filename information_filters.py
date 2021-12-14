import utils


def filter_country_names(soup):
    country_names = list()

    country_names_divs = soup.find_all("div", {"class": "fn org country-name"})

    for country in country_names_divs:
        country_names.append(
            utils.clean_text(
                utils.remove_unicode_chars(re.sub(r"<.+?>", "", country.text))
            )
        )

    return country_names
