from tkinter import *
import os
# Create the main window
st=Tk()
st.title("shutdown app")
st.geometry("500x500")
st.config(bg="lightblue")

from tkinter import messagebox

def restart():
    answer = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the computer?")
    if answer:
        os.system("shutdown /r /t 1")

def shutdown():
    answer = messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown the computer?")
    if answer:
        os.system("shutdown /s /t 1")

def logoff():
    answer = messagebox.askyesno("Confirm Log off", "Are you sure you want to log off?")
    if answer:
        os.system("shutdown /l")

r_button=Button(st, text="Restart", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command=restart)
r_button.place(x=200, y=60, height=50, width=150)

s_button=Button(st, text="Shutdown", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command=shutdown)
s_button.place(x=200, y=140, height=50, width=180)

l_button=Button(st, text="Log off", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command=logoff)
l_button.place(x=200, y=220, height=50, width=150)






st.mainloop()



