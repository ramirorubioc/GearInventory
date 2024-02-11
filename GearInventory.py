from GearSet import  *
from GearPiece import  GearPiece
from ScrapeSet import *
from bs4 import BeautifulSoup
import requests

#Artifact sets page
ARTIFACT_ARMOR = "https://www.bg-wiki.com/ffxi/Category:Artifact_Armor"
REFORGED_ARTIFACT_ARMOR = "https://www.bg-wiki.com/ffxi/Category:Reforged_Artifact_Armor"
#Relic sets page
RELIC_ARMOR = "https://www.bg-wiki.com/ffxi/Category:Relic_Armor"
REFORGED_RELIC_ARMOR = "https://www.bg-wiki.com/ffxi/Category:Reforged_Relic_Armor"
#Empyrean sets page
EMPYREAN_ARMOR = "https://www.bg-wiki.com/ffxi/Category:Empyrean_Armor"
REFORGED_EMPYREAN_ARMOR = "https://www.bg-wiki.com/ffxi/Category:Reforged_Empyrean_Armor"
#File exported using GearSwap
GAME_FILE_NAME = "ExportFromGame/export.lua"
#Jobs
WAR = 0
MNK = 1
WHM = 2
BLM = 3
RDM = 4
THF = 5

def find_in_inventory(GearPiece):
    """
    Checks if the given GearPiece is found in the game file.

    Parameters:
    GearPiece: The piece to be checked.

    Returns:
    bool: True if the GearPiece is found, False otherwise.
    """
    pieceStatus = GearPiece.get_status() #Get current piece Status
    gameFile = open(GAME_FILE_NAME, "r")
    contentsExportFile = gameFile.read()
    if str(GearPiece) in contentsExportFile:
        pieceStatus = True #Update piece Status if piece found
    gameFile.close()
    return pieceStatus

artifactSetsList =scrape_set_url(REFORGED_EMPYREAN_ARMOR)
print("0 WAR\n"
      "1 MNK\n"
      "2 WHM\n"
      "3 BLM\n"
      "4 RDM\n"
      "5 THF\n")
job = int(input("Pick a JOB using its ID number>"))
print(artifactSetsList[job])
warArtifact = populate_gearset(scrape_gear_names(artifactSetsList[job]))

#Update the status of the GearPieces in Gearset
warArtifact.update_GearSet_status(find_in_inventory(warArtifact.head),
                                  find_in_inventory(warArtifact.body),
                                  find_in_inventory(warArtifact.hands),
                                  find_in_inventory(warArtifact.legs),
                                  find_in_inventory(warArtifact.feet))
#Print GearSet
print(warArtifact)
