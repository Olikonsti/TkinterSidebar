from tkinter import *
import tkinter.ttk as ttk

ScrollOnItemsList = []

class ScrollBar(Frame):
    def __init__(self, parent):
        self.height = 518
        self.width = 200

        Frame.__init__(self, parent, width=self.width, height=self.height, bg="grey")
        self.place(x=0, y=-2)

        self.last_delta = 0
        parent.update()


        print("scrollframe init")
        self.c_frame = Frame(self, width=self.width, height=self.height, bg="grey")
        self.c_frame.place(x=0, y=0)
        self.c_Canvas = Canvas(self.c_frame, width=self.width, height=self.height, bd=-2, bg="red")
        scrollbar = Scrollbar(self.c_frame, orient="vertical", command=self.c_Canvas.yview, bg="grey")
        self.scrollframe = Frame(self.c_Canvas)
        self.scrollframe.place(x=0, y=0)

        self.scrollframe.bind(
            "<Configure>",
            lambda e: self.c_Canvas.configure(
                scrollregion=self.c_Canvas.bbox("all")
            )
        )
        self.c_Canvas.create_window((0, 0),
                               window=self.scrollframe, anchor="nw")

        self.c_Canvas.configure(yscrollcommand=scrollbar.set)
        self.c_Canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.c_Canvas.bind("<MouseWheel>", self.OnMouseWheel)

        parent.after(1, self.add_binds)

    def add_binds(self):

        for i in ScrollOnItemsList:
            i.bind("<MouseWheel>", self.OnMouseWheel)
            i.text.bind("<MouseWheel>", self.OnMouseWheel)
            print("binding added")




    def OnMouseWheel(self, event):
        self.threashold = 1
        if event.delta > self.last_delta:
            event.delta =- self.threashold
        else:
            event.delta = + self.threashold

        self.c_Canvas.yview("scroll", event.delta, "units")
        return "break"

    def move_down(self):
        self.c_Canvas.yview("scroll", 10, "units")
