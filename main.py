import requests
import os
from dotenv import load_dotenv
import datetime as dt
from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox

load_dotenv("C:/Python/Environmental variables/.env")
# Below two variables got after creating the account
PIXELA_TOKEN = os.getenv("pixela_token")
PIXELA_USER = os.getenv("pixela_user")
pixela_url = "https://pixe.la/v1/users"

def reset_pixel():
    reset_url = f"{pixela_url}/{PIXELA_USER}/graphs/graph1/{formatted_date}"
    response = requests.delete(url=reset_url,headers=headers)
    print(response.text)
    messagebox.showinfo(title="Reset/Delete Pixel",message="Reset Successful.")

def add_pixel():
    post_url = f"{pixela_url}/{PIXELA_USER}/graphs/graph1"
    pixel_parameters = {
        "date":formatted_date,
        "quantity":hours_spent
    }
    if hours_spent is None:
        messagebox.showinfo(title="Error", message="Field is empty.")
    elif hours_spent is int:
        response = requests.post(url=post_url,json=pixel_parameters,headers=headers)
        messagebox.showinfo(title="Post", message="Posted Successful.")
        print(response.text)

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
# formatted_date = raw_date.strftime("%Y%m%d")
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

today_date = int(raw_date.strftime("%d"))
this_month = int(raw_date.strftime("%m"))
this_year = int(raw_date.strftime("%Y"))


cal = Calendar(selectmode = 'day',
               day=today_date,
               month=this_month,
               year=this_year)
user_date_input = cal.get_date()

print(user_date_input)
cal.grid(row=0,column = 0,columnspan = 4,pady = 10)

text = Label(text="Hours Spent:",bg="#646464",fg="white")
text.grid(row=1, column=0, columnspan=2, pady=10, sticky="e")

hours_spent = Entry(width=10)
hours_spent.grid(row=1, column=2, sticky="w")

reset = Button(text="Reset",command=reset_pixel)
reset.grid(row = 3, column = 0,pady=10)

update = Button(text="Update")
update.grid(row = 3, column = 1,sticky = "w",pady=10)

post = Button(text="Post",command=add_pixel)
post.grid(row = 3, column = 2,sticky = "w",pady=10)

show_info = Button(text="Show\nJourney")
show_info.grid(row = 3, column = 3)
window.mainloop()

