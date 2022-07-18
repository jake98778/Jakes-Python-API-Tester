#This is Jake's Python API tester. 

#Visual programming with tkinter
import tkinter as tk
import tkinter.font as tkFont
#Adding API import

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_102=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_102["font"] = ft
        GLabel_102["fg"] = "#333333"
        GLabel_102["justify"] = "center"
        GLabel_102["text"] = "Jakes API Tester"
        GLabel_102.place(x=210,y=70,width=179,height=36)

        GLineEdit_650=tk.Entry(root)
        GLineEdit_650["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_650["font"] = ft
        GLineEdit_650["fg"] = "#333333"
        GLineEdit_650["justify"] = "center"
        GLineEdit_650["text"] = "Entry"
        GLineEdit_650.place(x=180,y=150,width=395,height=102)

        GLabel_413=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_413["font"] = ft
        GLabel_413["fg"] = "#333333"
        GLabel_413["justify"] = "center"
        GLabel_413["text"] = "Enter API Here:"
        GLabel_413.place(x=70,y=150,width=99,height=31)

        GMessage_297=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_297["font"] = ft
        GMessage_297["fg"] = "#333333"
        GMessage_297["justify"] = "center"
        GMessage_297["text"] = "Message"
        GMessage_297.place(x=180,y=290,width=392,height=164)

        GLabel_87=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_87["font"] = ft
        GLabel_87["fg"] = "#333333"
        GLabel_87["justify"] = "center"
        GLabel_87["text"] = "API Output:"
        GLabel_87.place(x=80,y=280,width=70,height=25)

        GButton_481=tk.Button(root)
        GButton_481["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_481["font"] = ft
        GButton_481["fg"] = "#000000"
        GButton_481["justify"] = "center"
        GButton_481["text"] = "Send it!"
        GButton_481.place(x=510,y=250,width=70,height=25)
        GButton_481["command"] = self.GButton_481_command

        GButton_472=tk.Button(root)
        GButton_472["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_472["font"] = ft
        GButton_472["fg"] = "#000000"
        GButton_472["justify"] = "center"
        GButton_472["text"] = "WIP Clear"
        GButton_472.place(x=500,y=450,width=70,height=25)
        GButton_472["command"] = self.GButton_472_command

        GRadio_997=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_997["font"] = ft
        GRadio_997["fg"] = "#333333"
        GRadio_997["justify"] = "center"
        GRadio_997["text"] = "GET"
        GRadio_997.place(x=0,y=40,width=85,height=25)
        GRadio_997["command"] = self.GRadio_997_command

        GRadio_360=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_360["font"] = ft
        GRadio_360["fg"] = "#333333"
        GRadio_360["justify"] = "center"
        GRadio_360["text"] = "POST"
        GRadio_360.place(x=0,y=60,width=85,height=25)
        GRadio_360["command"] = self.GRadio_360_command

        GRadio_382=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_382["font"] = ft
        GRadio_382["fg"] = "#333333"
        GRadio_382["justify"] = "center"
        GRadio_382["text"] = "PUT"
        GRadio_382.place(x=0,y=80,width=85,height=25)
        GRadio_382["command"] = self.GRadio_382_command

    def GButton_481_command(self):
        print("Command")


    def GButton_472_command(self):
        print("Command")


    def GRadio_997_command(self):
        print("Get Button")


    def GRadio_360_command(self):
        print("Post Button")


    def GRadio_382_command(self):
        print("Put Button")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
