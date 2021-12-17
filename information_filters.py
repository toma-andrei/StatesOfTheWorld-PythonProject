import utils
import re


def filter_country_names(soup):
    """
    Filter information obtaining country name.
    @param soup: BeautifulSoup instance containing information about a country
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

    @param soup: BeautifulSoup instance containing information about a country
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
    """
    Filter information obtaining country's population.

    @param soup: BeautifulSoup instance containing information about a country
    @returns: a string representing each country's population

    """

    # select all table rows
    trs = soup.select("table > tbody > tr")

    population = "0"

    for tr in trs:
        # check if tr contains population th
        trr = tr.select("th:-soup-contains(Population)")

        if trr:
            # format html to obtain population
            population = re.sub(
                r"<img.+?/>", "", str(tr.next_sibling.find_all("td")[0].text)
            )

            population = utils.clean_number(population.strip())

    return population


def filter_country_density(soup):
    """
    Filter information obtaining country's density.

    @param soup: BeautifulSoup instance containing information about a country
    @returns: a string representing each country's density

    """

    # select all table rows
    trs = soup.select("table > tbody > tr")

    density = "0"

    for tr in trs:
        # check if tr contains Density th
        if tr.select("th:-soup-contains(Density)"):
            td = tr.find_all("td")

            # filter density value
            density = utils.clear_density(td[0].text)
            break

    return density


def filter_country_surface(soup):
    """
    Filter information obtaining country's surface.

    @param soup: BeautifulSoup instance containing information about a country
    @returns: a string representing each country's area

    """

    # select all table rows
    trs = soup.select("table > tbody > tr")

    surface = "0"

    for tr in trs:
        if tr.select("th:-soup-contains(Area)"):
            surface = utils.remove_unicode_chars(
                utils.clear_surface((tr.next_sibling).find("td").text)
            )

    return surface


def filter_country_language(soup):

    language = ""
    not_a_language = ["None at the federal level", "federal level"]
    trs = soup.select("table > tbody > tr")

    for tr in trs:

        if tr.select("th:-soup-contains(language)"):
            td = tr.find("td")
            ul_li = td.find_all("li")

            if not ul_li:
                anchor = td.find_all("a")
                if not anchor:
                    language = utils.clear_language(str(td))
                else:
                    language = utils.clear_language(str(anchor[0].text))
                break
            else:
                language = utils.clear_language(str(ul_li[0].text))
                break

    if language.strip() in not_a_language:
        language = "English"

    if len(language) > 20:
        language = "Afar"

    return language


def filter_country_timezone(soup):
    pass


def filter_country_political_regime(soup):
    pass


def filter_country_neighbours(soup):
    pass
