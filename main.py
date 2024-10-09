import requests
from datetime import datetime, timedelta

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "sdfsonofidnhmksd"
USERNAME = "szymonbryniak"
GRAPH_ID = "szymonsgraph"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}



graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# create user
def create_user():
    response = requests.post(url=pixela_endpoint, json=user_params)


# create graph definition
def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


# get graph
# https://pixe.la/v1/users/a-know/graphs/test-graph



today = datetime.now().strftime("%Y%m%d")
yesterday = datetime.now() - timedelta(days=1)
yesterday_strf = yesterday.strftime("%Y%m%d")

graph_data = {
    "date": today,
    "quantity": "7"
}
# Post value to the graph
def post_pixel():
    graph_value_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    response = requests.post(url=graph_value_post_endpoint, json=graph_data, headers=headers)
    print(response.text)

def delete_pixel():
    graph_value_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    response_val = requests.delete(url=graph_value_delete_endpoint, headers=headers)
    print(response_val.text)

def put_pixel():
    graph_value_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    response = requests.put(url=graph_value_put_endpoint, json=graph_data, headers=headers)
    print(response.text)