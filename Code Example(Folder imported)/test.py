from TkinterSidebar.sidebar import *
from TkinterSidebar.pages.display_pages import *

root = Tk()
root.resizable(False, False)
root.geometry("750x510")
main_frame = Frame(root, bg="grey", width=1000, height=1000)
main_frame.place(x=200, y=0)





sidebar = SideBar(root)
sidebar.add_spacer("Test_")
sidebar.add_button("Home", lambda: HomePage(main_frame), icon="home.png")
sidebar.add_button("Settings", lambda: SettingsPage(main_frame))
sidebar.add_spacer("Other")
sidebar.add_button("Test Page", lambda: TestPage(main_frame))
sidebar.add_button("Test", lambda: print("KundVWebsite"), icon="home.png", tab=False)
sidebar.finish()


root.mainloop()