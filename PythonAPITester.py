from tkinter import *
from pip._vendor import requests
import json

ws = Tk()
ws.title("Jakes API Tester")
ws.geometry('400x300')
ws['bg'] = '#4242f5'

def printValue():
    URL = api_url.get()
    Label(ws, text=f'{URL}, Has been saved as API URL', pady=20, bg='#4242f5').pack()

    response = requests.get(URL)

    Label(ws, text=f'Response:  {response}', pady=20, bg='#4242f5').pack()


api_url = Entry(ws)
api_url.pack(pady=30)

Button(
    ws,
    text="Register Player", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()