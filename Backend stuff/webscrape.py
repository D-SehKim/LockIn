import requests

URL = "https://realpython.github.io/fake-jobs/"
URL = "https://www.spire.umass.edu/psc/heproda/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=UM_ACADEMICS_TILE_NC&PTPPB_GROUPLET_ID=UM_ACADEMICS_TILE_NC&CRefName=UM_ACADEMICS_TILE_NC"
page = requests.get(URL)

print(page.text)