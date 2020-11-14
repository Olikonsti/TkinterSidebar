from TkinterSidebar.sidebar import *
from TkinterSidebar.pages.display_pages import *

root = Tk()
root.resizable(False, False)
root.geometry("750x510")
main_frame = Frame(root, bg="grey", width=1000, height=1000)
main_frame.place(x=200, y=0)





b = SideBar(root)
b.add_spacer("Allgemeines")
b.add_button("Home", lambda: HomePage(main_frame), icon="home.png")
b.add_button("Einstellungen", lambda: SettingsPage(main_frame))
b.add_spacer("Anderes")
b.add_button("Test Page", lambda: TestPage(main_frame))
b.add_button("KundV Website", lambda: print("KundVWebsite"), icon="home.png", tab=False)
b.finish()


root.mainloop()