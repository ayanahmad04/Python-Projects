
from tkinter import *

def add_task():
    task = entry.get()
    if task:
        task_list.insert(END, task)
        entry.delete(0, END)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

def mark_done():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.itemconfig(selected_task_index, {'bg': 'light green'})

def clearall():
    task_list.delete(0, END)

is_dark = False

def dark():
    global is_dark
    if is_dark:
        # Dark mode
        root['bg'] = 'white'
        entry['bg'] = 'white'
        task_list['bg'] = 'white'
        entry['fg'] = 'black'
        task_list['fg'] = 'black'
        x['bg'] = 'white'    
        y['bg'] = 'white'    
        q['bg'] = 'white'    
        w['bg'] = 'white'  
        x['fg'] = 'black'  
        y['fg'] = 'black'
        q['fg'] = 'black'  
        w['fg'] = 'black'  
        d['bg'] = 'white'
        d['fg'] = 'black'
        a['fg'] = 'white'
        entry['insertbackground'] = 'black'
        d.config(image=b)
        
        is_dark = False
    else:
        # Light mode
        root['bg'] = 'black'
        entry['bg'] = 'black'
        task_list['bg'] = 'black'
        entry['fg'] = 'white'
        task_list['fg'] = 'white'
        x['bg'] = 'black' 
        y['bg'] = 'black' 
        q['bg'] = 'black'  
        w['bg'] = 'black'
        x['fg'] = 'white'  
        y['fg'] = 'white'  
        q['fg'] = 'white'  
        w['fg'] = 'white'  
        d['bg'] = 'black'
        d['fg'] = 'white'
        a['fg'] = 'black'
        entry['insertbackground'] = 'white'
        d.config(image=c)
       
        is_dark = True

root = Tk()
root.title("To-Do List")
root.geometry('420x450')
root.resizable(False, False)
icon = PhotoImage(file='4697260.png')
root.iconphoto(False, icon)
a = Label(root, text='To-do List', font='Calibri 20 bold italic', bg='blue', fg='black', width=10)
a.pack(pady=15)
b = PhotoImage(file='1664849-200.png')
b = b.subsample(4, 4)
c = PhotoImage(file='download (1).png')
c = c.subsample(8, 8)

entry = Entry(root, width=30, font='Calibri 12 ')
entry.place(x=80, y=65)

frame = Frame(root)
frame.place(x=30, y=100)

w = Button(root, text="Add Task", font='Calibri 12 bold italic', command=add_task)
x = Button(root, text="Remove Task", font='Calibri 12 bold italic', command=remove_task)
y = Button(root, text="Mark as Done", font='Calibri 12 bold italic', command=mark_done)
q = Button(root, text='Clear all', font='Calibri 12 bold italic', command=clearall)
d = Button(root, image=b, height=33, width=35, command=dark)
w.place(x=300, y=100)
x.place(x=300, y=160)
y.place(x=300, y=220)
q.place(x=300, y=280)
d.place(x=370, y=10)

task_list = Listbox(frame, selectmode=SINGLE, selectbackground="light blue", width=40, height=20)
task_list.pack(side=LEFT)

f = Scrollbar(frame, orient=VERTICAL)
f.pack(side=RIGHT, fill=Y)

task_list.config(yscrollcommand=f.set)
f.config(command=task_list.yview)

root.mainloop()

