from genericpath import getctime
import urllib.request
from bs4 import BeautifulSoup
import os
from time import time

# URL to States of the world Wikipedia page
states_of_the_world = "https://en.wikipedia.org/wiki/List_of_sovereign_states"

base_path = "https://en.wikipedia.org"

states_of_the_world_links = []


def get_and_write_URLs():
    """

    get_and_write_URLs() function obtains the URLs of each state located on
    Wikipedia 'List of states' page with BeautifulSoup library and saves content
    on states_of_the_world.txt file. File is renewed only if there are more than
    3 days past from file creation.

    """

    if (
        not os.path.exists("states_of_the_world.txt")
        or time() - os.path.getctime("states_of_the_world.txt") >= 259200
    ):
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


def main():
    get_and_write_URLs()


if __name__ == "__main__":
    main()
