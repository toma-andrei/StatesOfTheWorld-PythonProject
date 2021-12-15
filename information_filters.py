import utils
import re


def filter_country_names(soup):
    """
    Filter information obtaining country name.

    @returns: a list of strings representing each country name

    """

    country_names = list()

    country_names_divs = soup.find_all("div", {"class": "fn org country-name"})

    for country in country_names_divs:
        country_names.append(
            utils.clean_text(
                utils.remove_unicode_chars(re.sub(r"<.+?>", "", country.text))
            )
        )

    return country_names


def filter_country_capital(soup):
    """
    Filter information obtaining country's capital name.

    @returns: a list of strings representing each country name

    """

    capital_names = list()

    # select all table rows
    trs = soup.select("table > tbody > tr")

    capitals = list()
    # iterate through all table rows
    for tr in trs:
        # select all ths with the content "Capital"
        th = tr.select("*:-soup-contains(Capital)")

        # get first a from first sibling of the first th
        if th != []:
            if th[0].next_sibling.find_all("a")[0].text != "":
                a = th[0].next_sibling.find_all("a")
            else:
                a = th[0].next_sibling.find_all("a")
                a = a[1:]

            if a:
                capitals.append(
                    utils.clean_text(
                        utils.remove_unicode_chars(re.sub(r"<.+?>", "", str(a[0])))
                    )
                )
                break
    if capitals == []:
        return [""]
    return capitals


def filter_country_population(soup):
    pass


def filter_country_density(soup):
    pass


def filter_country_surface(soup):
    pass


def filter_country_neighbours(soup):
    pass


def filter_country_language(soup):
    pass


def filter_country_timezone(soup):
    pass


def filter_country_political_regime(soup):
    pass
