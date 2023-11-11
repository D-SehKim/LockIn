from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Open the website in the browser
website_url = "https://www.spire.umass.edu/psc/heproda/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=UM_ACADEMICS_TILE_NC&PTPPB_GROUPLET_ID=UM_ACADEMICS_TILE_NC&CRefName=UM_ACADEMICS_TILE_NC"
driver.get(website_url)

# Find the textbox by its HTML attribute (for example, its 'id')
textbox = driver.find_element("id", "i0116")

# Input a string into the textbox
text_to_input = "imei@umass.edu"
textbox.send_keys(text_to_input)

# Submit the form if needed
# textbox.submit()

# Get the updated URL (optional)
updated_url = driver.current_url

# Use requests library to make a request with the updated URL
response = requests.get(updated_url)

# Print the response content
print(response.text)

# Close the browser window
driver.quit()