#attempted to use tkcalendar but kept getting an error 'get_date()' not an attribute of cal

from calendar import day_name
from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Wash Wonders")
root.iconbitmap()
root.geometry("600x400")

cal = Calendar(root, selectmode="day", year=2021, month=7, day=29)
cal.pack(pady=20)

def grab_date():
    my_label.config(text="Scheduled date is: " + cal.get_date())

my_button = Button(root, text ="Select a Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text ="")
my_label.pack(pady=20)

root.mainloop()
