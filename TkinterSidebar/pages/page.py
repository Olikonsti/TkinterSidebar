from tkinter import *

active_page = []

class Page(Frame):
    def __init__(self, parent):
        self.width = 600
        self.height = 600
        # remove old page
        try:
            active_page[0].delete()
        except:
            pass

        # create new tab
        Frame.__init__(self, parent, bg="#201F1E", height=self.height, width=self.width)

        # place page
        self.place(x=0, y=0)

        active_page.append(self)

    def delete(self):
        print("destroying previous tab")
        global active_page
        active_page.remove(self)
        self.destroy()