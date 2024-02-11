from bs4 import BeautifulSoup
import requests
import re

URL = "https://www.bg-wiki.com/ffxi/Wakido_Armor_Set"
GEAR_TABLE_OFFSET = 2
SETS_TABLE_OFFSET = 7
BASE_URL = "https://www.bg-wiki.com/ffxi/"
def scrape_gear_names(url):
    """
    Finds the names of the gear pieces in url page.

    Parameters:
    url: URL for page where a gear set is found.

    Returns:
    gearList: List that contains the string name of the gear pieces
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    offset = 0
    gear = ""
    while offset < len(tables):
        header = str(tables[offset].find(string=re.compile("Set")))
        if header != "None":
            break
        offset += 1
    tables = tables[offset]
    for table in tables.find("th"):
        for string in table:
            if len(string)>1:
                header = string
    header = header[:header.find(" ")]
    gearList = []
    for table in tables.find_all("a"):
        for string in table:
            if (string.find(header)>=0):
                gearList.append(string)
    return gearList

def scrape_set_url(url):
    """
    Finds the url of the gear set in page.

    Parameters:
    url: URL for page where a several gear sets are located.

    Returns:
    urlList: List that contains the urls for the gear sets in page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
   # print(soup)
    tables = soup.find_all("table")
    tables = tables[SETS_TABLE_OFFSET:len(tables)]
    setLinksList = []

    for table in tables:
        for href in table.find("a"):
            setLinksList.append(BASE_URL + href.replace(" ", "_")
                                                .replace("'", "%27"))
    return setLinksList
