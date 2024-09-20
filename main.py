import requests
import os
from dotenv import load_dotenv
import datetime as dt
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
import webbrowser # to open new tab in browser with provided in url
import json # to convert json to dict

load_dotenv("C:/Python/Environmental variables/.env")
# Below two variables got after creating the account
PIXELA_TOKEN = os.getenv("pixela_token")
PIXELA_USER = os.getenv("pixela_user")
pixela_url = "https://pixe.la/v1/users"

def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    # cal.config(date_pattern="dd/MM/yyyy")
    return date

def reset_pixel():
    reset_url = f"{pixela_url}/{PIXELA_USER}/graphs/graph1/{format_date()}"
    response = requests.delete(url=reset_url,headers=headers)
    print(response.text)
    messagebox.showinfo(title="Reset/Delete Pixel",message="Reset Successful.")

def add_pixel():
    post_url = f"{pixela_url}/{PIXELA_USER}/graphs/graph1"
    input_field = hours_spent.get()
    pixel_parameters = {
        "date":format_date(),
        "quantity":input_field
    }
    response = requests.post(url=post_url, json=pixel_parameters, headers=headers)
    data = json.loads(response.text)
    is_success = data["isSuccess"]
    hours_spent.delete(0,END)

    if is_success:
        messagebox.showinfo(title="Post", message="Posted Successful.")
    else:
        messagebox.showinfo(title="Error", message="Field is empty (or) \nInvalid input (or) \nAPI rejects 25% times, so TRY AGAIN...")

def journey():
    webbrowser.open(url="https://pixe.la/v1/users/balaji3/graphs/graph1.html")
# Creating an account--------------------------------------------------------------------------
# the token will be what we type in the token field below
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
raw_date = dt.datetime.now()
formatted_date = raw_date.strftime("%Y%m%d")
# pixel_parameters = {
#     "date":formatted_date,
#     "quantity":input("Hours Python Studied Today --- ")
# }
# response = requests.post(url = f"{pixela_url}/{PIXELA_USER}/graphs/graph1",json=pixel_parameters,headers=headers)
# print(response.text)
#--------------------------------------------------------------------------------------------------------------------
window = Tk()
window.title("Python Journey")
window.config(padx=20,pady=20,bg = "#4B8BBE")
window.resizable(width=False,height=False)

today_date = int(raw_date.strftime("%d"))
this_month = int(raw_date.strftime("%m"))
this_year = int(raw_date.strftime("%Y"))


cal = Calendar(selectmode = 'day',
               day=today_date,
               month=this_month,
               year=this_year)
cal.grid(row=0,column = 0,columnspan = 3)

text = Label(text="Hours Spent:",bg="#646464",fg="white")
text.grid(row=1, column=0,pady = 20,sticky = "e")

hours_spent = Entry(width=10)
hours_spent.grid(row=1, column=1,pady = 20,sticky = "w")

reset = Button(text="Reset",command=reset_pixel,width=10)
reset.grid(row = 2, column = 0,sticky = "e",padx = 10)

# update = Button(text="Update")
# update.grid(row = 3, column = 1,sticky = "w",pady=10)
# no need of update because post works the same

post = Button(text="Post",command=add_pixel,width=10)
post.grid(row = 2, column = 1,sticky = "w")

show_info = Button(text="Show\nJourney",command=journey)
show_info.grid(row = 2, column = 2)
window.mainloop()

