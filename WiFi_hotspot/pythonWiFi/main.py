from tkinter import *  # python's built-in GUI
import subprocess  # this one let us to work with Windows' terminal (cmd)
import ssid  # our self-made modules
import wifi_pass
import set_wifi
import info

clicks = 0  # counter which indicates hotspot's current status


def click_btn1():
    global clicks
    clicks += 1
    if clicks > 0:
        # we can also not to use variable here and my PyCharm actually says that we shouldn't but IDC :)
        run_wifi = subprocess.run("netsh wlan start hostednetwork")
        root.title("WiFi is ON")
        btn1.config(bg="green3")
        btn2.config(bg="#555")


def click_btn2():
    global clicks
    clicks = 0
    if clicks == 0:
        # same thing with variable here
        stop_wifi = subprocess.run("netsh wlan stop hostednetwork")
        root.title("WiFi is OFF")
        btn2.config(bg="red")
        btn1.config(bg="#555")


def click_btn3():
    ssid.run()


def click_btn4():
    wifi_pass.run()


root = Tk()     # creating a window
root.title("WiFi Manager")  # giving a name to that window
root.geometry("250x350+500+200")  # size & position (if you want to fix the size use .resizable() )

main_menu = Menu()  # creating a main cascade menu

settings_menu = Menu()  # and some submenu list to call our sub-menus
settings_menu.add_command(label="Set New WiFi", command=set_wifi.run)
settings_menu.add_separator()
settings_menu.add_command(label="Change SSID", command=click_btn3)
settings_menu.add_command(label="Change password", command=click_btn4)

about_menu = Menu()  # also a submenu with some info
about_menu.add_command(label="Info", command=info.show_info_window)
about_menu.add_command(label="How to use", command=info.show_about_message)

main_menu.add_cascade(label="Settings", menu=settings_menu)  # associating submenu 1
main_menu.add_cascade(label="About", menu=about_menu)  # associating submenu 2


# creating some buttons to turn ON/OFF our hotspot
btn1 = Button(root, text="Start WiFi", background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", activebackground="green3", command=click_btn1)

# placing our button. if random place is OK use .pack() method to place&show it
btn1.place(relx=.5, rely=.4, anchor="c", height=30, width=130, bordermode=OUTSIDE)
btn2 = Button(root, text="Stop WiFi", background="#555", foreground="#ccc",
              padx="20", pady="8", font="16", activebackground="red", command=click_btn2)
btn2.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

# associate our menu with our "root" window
root.config(menu=main_menu)
# and finally giving a command to show our main windows
root.mainloop()
