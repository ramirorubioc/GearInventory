from bs4 import BeautifulSoup
import requests

URL = "https://www.bg-wiki.com/ffxi/Category:Artifact_Armor"
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
    gearTable = (tables[GEAR_TABLE_OFFSET].find_all("td"))
    gearList = []
    for line in gearTable:
        for string in line.find("a"):
            gearList.append(string)
    return(gearList)

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
