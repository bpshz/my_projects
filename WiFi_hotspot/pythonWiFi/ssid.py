from tkinter import *
from tkinter import messagebox
import subprocess

# This module creates a sub-window with "type-in" line & a button, which gets a text from the line and
# then setting that text as our Wi-Fi's name (SSID).


def run():
    def do_smthng():
        try:
            a = message_entry.get()
            if len(message_entry.get()) < 1:
                raise Exception("SSID should contain at least 1 character")
            subprocess.run("netsh wlan set hostednetwork ssid=\"%s\"" % a)
            messagebox.showinfo("Success", "Yay! SSID has been successfully changed!")
            root3.destroy()
        except Exception as e:
            messagebox.showinfo("Invalid SSID format", e)

    root3 = Tk()
    root3.title("Change SSID")
    root3.geometry("200x50+525+350")
    root3.resizable(height=False, width=False)

    message = StringVar()
    message_entry = Entry(root3, textvariable=message)
    message_entry.place(relx=.5, rely=.3, anchor="c")
    btn = Button(root3, text="Change SSID", command=do_smthng)
    btn.pack(side=BOTTOM)

    root3.mainloop()
