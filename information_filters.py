import utils
import re


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


def filter_country_capital(soup):
    capital_names = list()

    trs = soup.select("table > tbody > tr")

    # th = [c for c in capital_names_divs.find_all("th", text="Capital")]
    capitals = list()

    for tr in trs:
        th = tr.find_all("th", text="Capital")
        if th != []:
            a = th[0].next_sibling.find_all("a")
            capitals.append(a)
            break
    print(len(capitals))


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
