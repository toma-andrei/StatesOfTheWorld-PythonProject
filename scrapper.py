import urllib.request
from bs4 import BeautifulSoup
import os

# URL to States of the world Wikipedia page
states_of_the_world = "https://en.wikipedia.org/wiki/List_of_sovereign_states"

base_path = "https://en.wikipedia.org"

states_of_the_world_links = []


def get_and_write_URLs():
    """
    getURLs function obtains the URLs of each state located on Wikipedia
    """

    if os.path.exists("states_of_the_world.txt"):
        pass

    # obtaining all states page content
    all_states_page = urllib.request.urlopen(states_of_the_world)

    # create a BeautifulSoup instance with html parser for easy manipulation of page content
    soup = BeautifulSoup(all_states_page, "html.parser")

    anchorTags = soup.select("table > tbody > tr > td > b > a")

    for a in anchorTags:
        states_of_the_world_links.append(a["href"])

    file = open("states_of_the_world.txt", "a")

    for url in states_of_the_world_links:
        file.write(base_path + url + "\n")

    file.close()


def obtain_infos():
    for link in states_of_the_world_links:
        url = base_path + link
        print(link)


def test_stuff():
    print(os.path.getctime("scrapper.py"))


def main():
    # get_and_write_URLs()
    test_stuff()


if __name__ == "__main__":
    main()
