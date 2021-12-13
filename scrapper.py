from genericpath import getctime
import urllib.request
from bs4 import BeautifulSoup
import os
from time import time

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

    # obtaining 'List of states' page content

    req = urllib.request.urlopen(states_of_the_world)
    all_states_page = req.read().decode("utf-8")

    # create a BeautifulSoup instance with html parser for easy manipulation of page content
    soup = BeautifulSoup(all_states_page, "html.parser")

    # select all anchor tags from states table
    anchorTags = soup.select("table > tbody > tr > td > b > a")

    # get the url of each state and save it to a list
    for a in anchorTags:
        states_of_the_world_links.append(a["href"])

    # remove old file if it exists
    if os.path.exists("states_of_the_world.txt"):
        os.remove("states_of_the_world.txt")

    # open and write to file full URL of each state
    file = open("states_of_the_world.txt", "a", encoding="utf-8")

    for url in states_of_the_world_links:
        file.write(base_path + url + "\n")

    file.close()


def get_site_infos():
    links_file = open("states_of_the_world.txt", "r", encoding="utf-8")

    links_file_content = links_file.read()

    # remove old file if it exists
    if os.path.exists("wiki_states_infos.txt"):
        os.remove("wiki_states_infos.txt")

    # create or open .txt file containing informations about countries
    wiki_state_info = open("wiki_states_infos.txt", "a")

    counter = 0

    for link in links_file_content.split():
        print(link)

        req = urllib.request.urlopen(link)
        wiki_page_content = req.read().decode("utf-8")

        soup = BeautifulSoup(wiki_page_content, "html.parser")

        table = soup.find("table", {"class": "infobox"})

        wiki_state_info.write(str(str(table.encode("utf-8")) + delimiter))

    links_file.close()
    wiki_state_info.close()


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
    get_site_infos()


if __name__ == "__main__":
    main()
