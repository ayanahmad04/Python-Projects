from tkinter import *
import random
import string
from tkinter import messagebox 

root = Tk()
root.title("Password Generator")
root.geometry('330x330')
root.resizable(False, False)
root['bg'] = 'black'

def generate_password():
    length = entry.get()
    if length == '0':
        messagebox.showerror("Error", "Invalid length")
        return
    if  length.isdigit():
        length=int(entry.get()) 
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        messagebox.showinfo("Generated Password", f"Your Password: {password}")
        return
    if not length.isdigit():
        messagebox.showerror('Error','Enter Number Between 1-9')
        return
def clear_default_text(event):
    if entry.get() == default_text:
        entry.delete(0, "end") 
        entry.config(fg="black", font=user_font)
default_text="Enter Password Length:"
default_font = ("Calibri", 12,'bold')
user_font = ("Calibri", 12,'bold')
entry = Entry(root,width=22, font=default_font,fg='gray')
entry.insert(0,default_text)
entry.bind("<FocusIn>", clear_default_text)
entry.place(x=75, y=110)    
frame = Frame(root,borderwidth=3, relief="sunken")
frame.pack(padx=20, pady=20)
label1 =Label(frame, text="Password Generator ",font=' Calibri 13 bold italic ', fg ='yellow',bg='black', width=20,height=2)
label1.place(x=80,y=20)
label1.pack()
button = Button(root, text="Generate Password",bg='black',fg='yellow', command=generate_password)
button.place(x=110, y=150)

root.mainloop()
