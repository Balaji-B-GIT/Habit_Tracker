import requests
import os
from dotenv import load_dotenv
import datetime as dt
from tkinter import *
load_dotenv("C:/Python/Environmental variables/.env")
PIXELA_TOKEN = os.getenv("pixela_token")
PIXELA_USER = os.getenv("pixela_user")

pixela_url = "https://pixe.la/v1/users"

# Creating an account--------------------------------------------------------------------------
# parameters = {
#     "token":PIXELA_TOKEN,
#     "username":PIXELA_USER,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes",
# }

# response = requests.post(url = pixela_url,json=parameters)
# print(response.text)
#------------------------------------------------------------------------------------------------------------------

# Creating a Graph-------------------------------------------------------------------------------------------------
headers = {
    "X-USER-TOKEN":PIXELA_TOKEN
}
# graph_parameters = {
#     "id":"graph1",
#     "name": "Steps_walked",
#     "unit":"number",
#     "type":"int",
#     "color":"sora",
# }

# response = requests.post(url=f"{pixela_url}/{PIXELA_USER}/graphs",json=graph_parameters,headers=headers)
# print(response.text)
#---------------------------------------------------------------------------------------------------------------

# Updating the graph-----------------------------------------------------------------------------------------------
# update_parameters ={
#     "type":"float"
# }
# response = requests.put(url=f"{pixela_url}/{PIXELA_USER}/graphs/graph1",json=update_parameters,headers=headers)
# print(response.text)
#------------------------------------------------------------------------------------------------------------------

# Creating a pixel-------------------------------------------------------------------------------------------------
today = dt.datetime.now()
pixel_parameters = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("Hours Python Studied Today --- ")
}
response = requests.post(url = f"{pixela_url}/{PIXELA_USER}/graphs/graph1",json=pixel_parameters,headers=headers)
print(response.text)
#--------------------------------------------------------------------------------------------------------------------
