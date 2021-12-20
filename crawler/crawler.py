from genericpath import getctime
import urllib.request
from bs4 import BeautifulSoup
import os
from time import time
import information_filters as if_filter

# URL to States of the world Wikipedia page
states_of_the_world = "https://en.wikipedia.org/wiki/List_of_sovereign_states"

base_path = "https://en.wikipedia.org"

delimiter = "###08sept###\n\n"


def get_and_write_URLs():
    """

    get_and_write_URLs() function obtains the URLs of each state located on
    Wikipedia 'List of states' page with BeautifulSoup library and saves content
    on states_of_the_world.txt file.

    """

    states_of_the_world_links = list()

    try:
        # obtaining 'List of states' page content
        req = urllib.request.urlopen(states_of_the_world)
        all_states_page = req.read().decode("utf-8")
    except Exception as e:
        print(
            "Something went wrong requesting '"
            + states_of_the_world
            + "' link. Error message: "
            + str(e)
        )

    try:
        # create a BeautifulSoup instance with html parser for easy manipulation of page content
        soup = BeautifulSoup(all_states_page, "html.parser")

        # select all anchor tags from states table
        anchorTags = soup.select("table > tbody > tr > td > b > a")

        # get the url of each state and save it to a list
        for a in anchorTags:
            states_of_the_world_links.append(a["href"])

    except Exception as e:
        print(
            "Something went wrong obtaing links with BeautifulSoup. Error message: "
            + str(e)
        )

    # remove old file if it exists
    if os.path.exists("Informations/states_of_the_world.txt"):
        os.remove("Informations/states_of_the_world.txt")

    # open and write to file full URL of each state
    try:
        file = open("Informations/states_of_the_world.txt", "a", encoding="utf8")
    except Exception as e:
        print(
            "Something went wrong creating/opening 'states_of_the_world.txt'. Error message: "
            + str(e)
        )
        return None

    for url in states_of_the_world_links:
        file.write(base_path + url + "\n")

    file.close()


def get_raw_site_infos():
    """

    This function read 'states_of_the_world.txt' file and iterate through all links
    and obtains informations for a specific state.
    Informations are written in 'wiki_states_infos.txt' file.

    """
    try:
        links_file = open("Informations/states_of_the_world.txt", "r", encoding="utf8")
        links_file_content = links_file.read()
    except Exception as e:
        print(
            "Something went wrong creating/opening/reading 'states_of_the_world.txt'. Error message: "
            + str(e)
        )

    # remove old file if it exists
    if os.path.exists("Informations/wiki_states_infos.txt"):
        os.remove("Informations/wiki_states_infos.txt")

    try:
        # create or open .txt file containing informations about countries
        wiki_state_info = open(
            "Informations/wiki_states_infos.txt", "a", encoding="utf8"
        )
    except Exception as e:
        print(
            "Something went wrong creating/opening 'wiki_states_infos.txt'. Error message: "
            + str(e)
        )

    # iterate through all links
    for link in links_file_content.split():
        print(link)
        try:
            # obtain full html page of a specific country
            req = urllib.request.urlopen(link)
            wiki_page_content = req.read().decode("utf8")
        except Exception as e:
            print(
                "Something went wrong requesting '"
                + states_of_the_world
                + "' link. Error message: "
                + str(e)
            )

        soup = BeautifulSoup(wiki_page_content, "html.parser")

        # obtain table with all informations about a country
        table = soup.find("table", {"class": "infobox"})

        # write to file table with a delimiter for easy future search
        wiki_state_info.write(str(str(table)) + delimiter)

    links_file.close()
    wiki_state_info.close()


def filter_raw_information():
    """

    Read 'wiki_states_info.txt' file and filter each information using BeautifulSoup4.

    """

    try:
        # read file and split information via delimiter
        file = open("Informations/wiki_states_infos.txt", "r", encoding="utf8")
        raw_content = file.read()
        raw_content_list = raw_content.split(delimiter)
        raw_content_list.pop()

    except Exception as e:
        print(
            "Something went wrong opening/reading 'wiki_states_infos.txt' file. Error message: "
            + str(e)
        )

    country_names = list()
    capital_names = list()
    country_population = list()
    country_density = list()
    country_surface = list()
    country_language = list()
    country_timezone = list()
    country_regime = list()
    country_currency = list()

    for content in raw_content_list:
        soup = BeautifulSoup(content, "html.parser")

        country_names.append(if_filter.filter_country_names(soup))
        capital_names.append((if_filter.filter_country_capital(soup)))
        country_population.append(if_filter.filter_country_population(soup))
        country_density.append(if_filter.filter_country_density(soup))
        country_surface.append(if_filter.filter_country_surface(soup))
        country_language.append(if_filter.filter_country_language(soup))
        country_timezone.append(if_filter.filter_country_timezone(soup))
        country_regime.append(if_filter.filter_country_political_regime(soup))
        country_currency.append(if_filter.filter_country_currency(soup))

    # remove old file if it exists
    if os.path.exists("../Database/clear_countries_information.txt"):
        os.remove("../Database/clear_countries_information.txt")

    try:
        # create or open .txt file containing informations about countries
        final_file = open(
            "../Database/clean_countries_information.txt", "a", encoding="utf8"
        )
    except Exception as e:
        print(
            "Something went wrong creating/opening 'clean_countries_information.txt'. Error message: "
            + str(e)
        )

    for i in range(0, len(country_names)):
        line = (
            country_names[i]
            + "|"
            + capital_names[i]
            + "|"
            + country_population[i]
            + "|"
            + country_density[i]
            + "|"
            + country_surface[i]
            + "|"
            + country_language[i]
            + "|"
            + country_timezone[i]
            + "|"
            + country_regime[i]
            + "|"
            + country_currency[i]
            + "\n"
        )

        final_file.write(line)

    file.close()
    final_file.close()


def main():
    """

    The main function, starting the crawling. The informations of each state is
    renewed only if there are more than 3 days past from last crawl.

    """

    # functions inside below 'if' are called when there are 3 days past from them creation.
    if (
        not os.path.exists("Informations/states_of_the_world.txt")
        or time() - os.path.getctime("Informations/states_of_the_world.txt") >= 259200
    ):
        get_and_write_URLs()
        get_raw_site_infos()
    filter_raw_information()


if __name__ == "__main__":
    main()
