from tkinter import *
from tkinter import messagebox
import subprocess

# and that little one is setting a brand new Wi-Fi hotspot. Creating some sub-window with two "type-in"
# lines, two labels and a button.


def run():
    def do_smthng():
        try:
            a = message_entry.get()
            b = message_entry2.get()
            if len(a) < 1:
                raise Exception("Please type in SSID. SSID should contain at least 1 character")
            if len(b) < 8:
                raise Exception("Please type in Password. Password should contain at least 8 characters.")
            subprocess.run(f"netsh wlan set hostednetwork mode = allow ssid = \"{a}\" key = \"{b}\" "
                                    f"keyUsage = persistent")
            messagebox.showinfo("Success!", "Yay! A new Wi-Fi hotspot has been set up!")
            root5.destroy()
        except Exception as e:
            messagebox.showinfo("Oops! Something gone wrong...", e)

    root5 = Tk()
    root5.title("Set WiFi")
    root5.geometry("200x125+525+350")
    root5.resizable(height=False, width=False)

    message = StringVar()
    message2 = StringVar()

    label = Label(root5, text="Insert SSID")
    label.pack()

    message_entry = Entry(root5, textvariable=message)
    message_entry.place(relx=.5, rely=.3, anchor="c")

    label2 = Label(root5, text="Insert password",)
    label2.place(rely=0.4, relx=0.25)

    message_entry2 = Entry(root5, textvariable=message2)
    message_entry2.place(relx=.5, rely=.7, anchor="c")

    btn = Button(root5, text="Set WiFi", command=do_smthng)
    btn.pack(side=BOTTOM)

    root5.mainloop()
