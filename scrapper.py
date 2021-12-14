from genericpath import getctime
import urllib.request
from bs4 import BeautifulSoup
import os
from time import time
import information_filters as ifilter

# URL to States of the world Wikipedia page
states_of_the_world = "https://en.wikipedia.org/wiki/List_of_sovereign_states"

base_path = "https://en.wikipedia.org"

states_of_the_world_links = []

delimiter = "###08sept###\n\n"


def get_and_write_URLs():
    """

    get_and_write_URLs() function obtains the URLs of each state located on
    Wikipedia 'List of states' page with BeautifulSoup library and saves content
    on states_of_the_world.txt file.

    """

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
    if os.path.exists("states_of_the_world.txt"):
        os.remove("states_of_the_world.txt")

    # open and write to file full URL of each state
    try:
        file = open("states_of_the_world.txt", "a", encoding="utf-8")
    except Exception as e:
        print(
            "Something went wrong creating/opening 'states_of_the_world.txt'. Error message: "
            + str(e)
        )

    for url in states_of_the_world_links:
        file.write(base_path + url + "\n")

    file.close()


def get_raw_site_infos():
    try:
        links_file = open("states_of_the_world.txt", "r", encoding="utf-8")
        links_file_content = links_file.read()
    except Exception as e:
        print(
            "Something went wrong creating/opening/reading 'states_of_the_world.txt'. Error message: "
            + str(e)
        )

    # remove old file if it exists
    if os.path.exists("wiki_states_infos.txt"):
        os.remove("wiki_states_infos.txt")

    try:
        # create or open .txt file containing informations about countries
        wiki_state_info = open("wiki_states_infos.txt", "a", encoding="utf-8")
    except Exception as e:
        print(
            "Something went wrong creating/opening 'wiki_states_infos.txt'. Error message: "
            + str(e)
        )

    for link in links_file_content.split():
        print(link)
        try:
            req = urllib.request.urlopen(link)
            wiki_page_content = req.read().decode("utf-8")
        except Exception as e:
            print(
                "Something went wrong requesting '"
                + states_of_the_world
                + "' link. Error message: "
                + str(e)
            )

        soup = BeautifulSoup(wiki_page_content, "html.parser")

        table = soup.find("table", {"class": "infobox"})

        wiki_state_info.write(str(str(table.encode("utf-8")) + delimiter))

    links_file.close()
    wiki_state_info.close()


def filter_raw_information():
    file = open("wiki_states_infos.txt", "r")

    raw_content = file.read()

    raw_content_list = raw_content.split(delimiter)
    raw_content_list.pop()

    country_names = list()

    soup = BeautifulSoup(raw_content, "html.parser")

    country_names = ifilter.filter_country_names(soup)


def main():
    """

    The main function, starting the crawling. The informations of each state is
    renewed only if there are more than 3 days past from last crawl.

    """

    # functions inside below 'if' are called when there are 3 days past from them creation.
    if (
        not os.path.exists("states_of_the_world.txt")
        or time() - os.path.getctime("states_of_the_world.txt") >= 259200
    ):
        get_and_write_URLs()
        get_raw_site_infos()
    filter_raw_information()


if __name__ == "__main__":
    main()
