#Importing the necessary libraries
import requests 
import json

#Set the API endpoint and API Key
base_url = "https://yourcompany.freshdesk.com/api/v2"
api_key = "your_api_key"
password = "your_freshdesk_password"
url = base_url + "/tickets"

#Http request to freshdesk
response = requests.get(url, auth = (api_key, password))

if response.status_code == 200:
    tickets = json.loads(response.content)
    for ticket in tickets:
        print(ticket)

else:
    print("Failed to fetch tickets.")


