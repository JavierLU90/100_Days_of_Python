# PIXELA HABIT TRACKER
import requests
from datetime import datetime

USERNAME = "javierlu"
TOKEN = "aljglsghloiausgh"
GRAPH_ID = "graph1"

# CREATE USER
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# PAINT PIXELS INTO GRAPH
paint_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

# response = requests.post(url=paint_graph_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# UPDATE EXISTING PIXEL
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",
}

# response = requests.post(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# DELETE PIXEL
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.post(url=delete_endpoint, headers=headers)
print(response.text)
