from tkinter import *
from tkinter import messagebox

s = "https://github.com/bpshz/my_projects"


def show_info_window():
    messagebox.showinfo("Info", "If by some miracle you got your hands on this program and you use it,\n"
                                " you know you make me happy.\n\nI wrote this program to learn the Python's"
                                " \"tkinter\" library.\n\nThe source code of this program, if you need it, you can find"
                                f" it on my GitHub at: \n{s}\n\n"
                                "If you have any suggestions or bug fixes you can write me on my mail"
                                " or VKontakte private messages:"
                                "\n\nbpshz@vk.com\nhttps://vk.com/bpshz")


def show_about_message():
    root_i = Tk()
    root_i.title("Info")
    label = Label(root_i, text="Just a little program which made from your laptop or PC\n "
                               "a Wireless Access Point(оf course, only if there is a network adapter on the device)\n"
                               " which uses \"cmd\" commands to manage & share Wi-Fi.\n\n"
                               "If this is the first time that you are running hotspot \n"
                               "go to the \"Settings\" menu, and choose \"Set New Wi-Fi\".\n"
                               "Then you should type in your hotspot's name (which is also called SSID)\n"
                               "and a password (which is also called Key).\n "
                               "Note that the SSID must be at least one character\n"
                               " long and the password must be at least 8 characters long.\n\nTo change the name"
                               " or password of an existing network, use the the drop-down menu's relevant buttons in\n"
                               "  \"Settings\".\n\nThe already created network is started from the main"
                               " window with the buttons \"Start Wi-Fi\" & \"Stop Wi-Fi\".\nThe currently active button"
                               " changes its color from gray to green for \"on\" status and \n"
                               "to red for \"off\" status.\n\n"
                               "  Also the Windows command line, which is accessed by the program, shows the current\n"
                               " status of the network and all possible errors.")
    label.pack()
