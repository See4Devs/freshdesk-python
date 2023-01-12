#Importing the necessary libraries
import requests 
import json

#Set the API endpoint and API Key
base_url = "https://yourcompany.freshdesk.com/api/v2"
api_key = "your_api_key"
password = "your_freshdesk_password"
#ticket ID - You get this ID from the freshdesk portal
ticketID="your_ticket_id"
url = base_url + "/tickets/"+ticketID

headers = {
    "Content-Type": "application/json"
}

ticket = {
    'description' : 'This is a new updated description',
}

response = requests.put(url, auth = (api_key, password), data=json.dumps(ticket), headers = headers)

if response.status_code == 200:
    print("Ticket updated successfully.")
else:
    print("Failed to update a ticket.")

