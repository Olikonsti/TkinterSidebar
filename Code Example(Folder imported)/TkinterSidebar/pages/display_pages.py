from ..pages.page import *

"""
defualt widget color:

#201F1E
"""
def_bg = "#201F1E"
def_fg = "lightgrey"

class HomePage(Page):
    def __init__(self, parent):
        print("Showning home page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Home", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class SettingsPage(Page):
    def __init__(self, parent):
        print("Showning settings page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Label(self, text="Einstellungen", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)

class TestPage(Page):
    def __init__(self, parent):
        print("Showning test page")


        # init page/ delete old page
        Page.__init__(self, parent)

        t = Button(self, text="Test", bg=def_bg, fg=def_fg)
        t.place(x=100, y=100)