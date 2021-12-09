import urllib.request
from bs4 import BeautifulSoup
import re

from bs4.dammit import encoding_res

'''URL to States of the world Wikipedia page'''
states_of_the_world = 'https://ro.wikipedia.org/wiki/Lista_statelor_lumii'

base_path = 'https://ro.wikipedia.org'
states_of_the_world_links = []

# //*[@id="mw-content-text"]/div[1]/table/tbody/tr[2]/td[1]/b/a


def main():
    # obtaining all states page content
    all_states_page = urllib.request.urlopen(states_of_the_world)

    # create a BeautifulSoup instance with html parser for easy manipulation of page content
    soup = BeautifulSoup(all_states_page, 'html.parser')

    # find all tds in the page table
    table = soup.find('table')
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    tds = tbody.find_all('td')

    # iterate through every 5th td to get href
    for i in range(0, len(trs), 5):
        states_of_the_world_links.append(
            tds[i].find_all('a')[0]['href'])

    print(states_of_the_world_links)


if __name__ == '__main__':
    main()
