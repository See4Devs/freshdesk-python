#Importing the necessary libraries
import requests 
import json

#Set the API endpoint and API Key
base_url = "https://yourcompany.freshdesk.com/api/v2"
api_key = "your_api_key"
password = "your_freshdesk_password"
url = base_url + "/tickets"

headers = {
    "Content-Type": "application/json"
}

ticket = {
    'subject' : 'Tutorial Ticket',
    'description' : 'Ticket tutorial details',
    'email' : 'tutorial@python.com',
    'priority' : 1,
    'status' : 2
}

response = requests.post(url, auth = (api_key, password), data=json.dumps(ticket), headers = headers)

if response.status_code == 201:
    print("Ticket created successfully.")
else:
    print("Failed to create a ticket.")

