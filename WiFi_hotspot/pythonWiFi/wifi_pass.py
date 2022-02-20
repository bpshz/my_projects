from tkinter import *
from tkinter import messagebox
import subprocess


# This module creates a sub-window with "type-in" line & a button, which gets a text from the line and
# then setting that text as our Wi-Fi's password (Key).

def run():
    def do_smthng():
        try:
            a = message_entry.get()
            if len(message_entry.get()) < 8:
                raise Exception("Password should contain at least 8 characters")
            subprocess.run("netsh wlan set hostednetwork key=\"%s\"" % a)
            messagebox.showinfo("Success", "Yay! Password has been successfully changed!")
            root4.destroy()
        except Exception as e:
            messagebox.showinfo("Invalid password format", e)

    root4 = Tk()
    root4.title("Change Password")
    root4.geometry("200x50+525+350")
    root4.resizable(height=False, width=False)

    message = StringVar()
    message_entry = Entry(root4, textvariable=message)
    message_entry.place(relx=.5, rely=.3, anchor="c")
    btn = Button(root4, text="Change Password", command=do_smthng)
    btn.pack(side=BOTTOM)

    root4.mainloop()
