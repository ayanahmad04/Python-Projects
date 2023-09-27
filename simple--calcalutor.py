from tkinter import *

root = Tk()
root.title('SIMPLE CALCULATOR')
root.geometry('330x450')
root.minsize(200, 250)
root.maxsize(1100, 2550)

eq = StringVar()
def show(value):
    eq.set(eq.get() + value)
    screen.config(text=eq.get())
def clear():
    eq.set('')
    screen.config(text='')
def calculate():
    try:
        res = eval(eq.get())  
        eq.set(str(res))      
        screen.config(text=eq.get())
    except Exception as e:
        eq.set('Error')
        screen.config(text='Error')

screen = Label(root, text='', font=('arial 25 bold'))
screen.pack(fill=X, ipadx=5, pady=15, padx=10)

Button( root,text='C', height=1, width=3,bd=1,bg='blue',fg='white',command=lambda:clear(),font='arial 20 bold').place(x=10,y=75)
Button( root,text='/', height=1, width=3,  font='arial 20 bold',command=lambda:show('/')).place(x=90,y=75)
Button( root,text='*', height=1, width=3, font='arial 20 bold',command=lambda:show('*')).place(x=170,y=75)
Button( root,text='-', height=1,width=3, font='arial 20 bold',command=lambda:show('-')).place(x=250,y=75)


Button( root,text='7', height=1, width=3,font='arial 20 bold',command=lambda:show('7')).place(x=10,y=150)
Button( root,text='8', height=1, width=3,  font='arial 20 bold',command=lambda:show('8')).place(x=90,y=150)
Button( root,text='9', height=1, width=3, font='arial 20 bold',command=lambda:show('9')).place(x=170,y=150)
Button( root,text='+', height=3, width=3, font='arial 20 bold',command=lambda:show('+')).place(x=250,y=160)

Button( root,text='4', height=1, width=3,font='arial 20 bold',command=lambda:show('4')).place(x=10,y=225)
Button( root,text='5', height=1, width=3,  font='arial 20 bold',command=lambda:show('5')).place(x=90,y=225)
Button( root,text='6', height=1, width=3, font='arial 20 bold',command=lambda:show('6')).place(x=170,y=225)


Button( root,text='1', height=1, width=3,  font='arial 20 bold',command=lambda:show('1')).place(x=10,y=300)
Button( root,text='2', height=1, width=3,  font='arial 20 bold',command=lambda:show('2')).place(x=90,y=300)
Button( root,text='3', height=1, width=3, font='arial 20 bold',command=lambda:show('3')).place(x=170,y=300)
Button( root,text='=', height=3, width=3, font='arial 20 bold',command=lambda:calculate()).place(x=250,y=310)



Button( root,text='0', height=1, width=8,  font='arial 20 bold',command=lambda:show('0')).place(x=10,y=375)
Button( root,text='.', height=1, width=3, font='arial 20 bold',command=lambda:show('.')).place(x=170,y=375)
root['bg'] = 'black'
root.mainloop()