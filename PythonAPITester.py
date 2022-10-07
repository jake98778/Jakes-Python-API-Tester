from tkinter import *
from pip._vendor import requests
import json

ws = Tk()
ws.title("Jakes API Tester")
ws.geometry('400x300')
ws['bg'] = '#4242f5'

#I'm an artist so this is where my art skills
def printValue():
    URL = api_url.get()
    Label(ws, text=f'"{URL}" Has been saved as API URL', pady=20, bg='#4242f5').pack()

def printApi():
    response = requests.get(api_url)
    Label(ws, text=f'Response:  {response}', pady=20, bg='#4242f5').pack()

api_url = Entry(ws)
api_url.pack(pady=30)

#First Button to save the API URL so we have it as a easy to mess with var
Button(
    ws,
    text="Enter URL to API test with", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

#another button to send the API
Button(
    ws,
    text="Send da API", 
    padx=20, 
    pady=10,
    command=printApi
    ).pack()

ws.mainloop()