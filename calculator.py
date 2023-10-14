from tkinter import *

#function for displaying values on screen
def click(event):
    global value
    text = event.widget.cget('text')
    print(text)
    if text=='=':
        try:
            newvalue  = str(eval(value.get()))
            value.set(newvalue)
        except Exception:
            value.set("Error")    
    elif text=="C":
        value.set("")
        screen_display.update() 
    else:
        value.set(value.get()+text)
        screen_display.update()          

    
root = Tk()
root.geometry('350x410')
root.configure(bg='aqua',relief=SOLID)
root.title('SIMPLE CALCULATOR')

value = StringVar()
value.set('')
screen_display = Entry(root,textvar = value , font = 'comicsans 35 bold')
screen_display.pack(fill=X, ipadx=6, padx=5, pady=5)

#BUTTONS FRAME
f1 = Frame(root,bg='aqua')

b1 = Button(f1, text='7',bg='grey',fg='white',font='lucida 20 bold',width=3)
b1.grid(row=1,column=1,padx=10,pady=6)
b1.bind('<Button-1>',click)

b2 = Button(f1, text='8',bg='grey',fg='white',font='lucida 20 bold',width=3)
b2.grid(row=1,column=2,padx=10,pady=6)
b2.bind('<Button-1>',click)

b3= Button(f1, text='9',bg='grey',fg='white',font='lucida 20 bold',width=3)
b3.grid(row=1,column=3,padx=10,pady=6)
b3.bind('<Button-1>',click)

b4= Button(f1, text='C',bg='grey',fg='white',font='lucida 20 bold',width=3)
b4.grid(row=1,column =4,padx=10,pady=6)
b4.bind('<Button-1>',click)

b5= Button(f1, text='6',bg='grey',fg='white',font='lucida 20 bold',width=3)
b5.grid(row=2,column=1,padx=10,pady=6)
b5.bind('<Button-1>',click)

b6= Button(f1, text='5',bg='grey',fg='white',font='lucida 20 bold',width=3)
b6.grid(row=2,column=2,padx=10,pady=6)
b6.bind('<Button-1>',click)

b7=Button(f1, text='4',bg='grey',fg='white',font='lucida 20 bold',width=3)
b7.grid(row=2,column=3,padx=10,pady=6)
b7.bind('<Button-1>',click)

b8= Button(f1, text='*',bg='grey',fg='white',font='lucida 20 bold',width=3)
b8.grid(row=2,column=4,padx=10,pady=7)
b8.bind('<Button-1>',click)

b9= Button(f1, text='3',bg='grey',fg='white',font='lucida 20 bold',width=3)
b9.grid(row=3,column=1,padx=10,pady=6)
b9.bind('<Button-1>',click)

b10= Button(f1, text='2',bg='grey',fg='white',font='lucida 20 bold',width=3)
b10.grid(row=3,column=2,padx=10,pady=6)
b10.bind('<Button-1>',click)

b11=Button(f1, text='1',bg='grey',fg='white',font='lucida 20 bold',width=3)
b11.grid(row=3,column=3,padx=10,pady=6)
b11.bind('<Button-1>',click)

b12= Button(f1, text='+',bg='grey',fg='white',font='lucida 20 bold',width=3)
b12.grid(row=3,column=4,padx=10,pady=6)
b12.bind('<Button-1>',click)

b13= Button(f1, text='0',bg='grey',fg='white',font='lucida 20 bold',width=3)
b13.grid(row=4,column=1,padx=10,pady=6)
b13.bind('<Button-1>',click)

b14= Button(f1, text='.',bg='grey',fg='white',font='lucida 20 bold',width=3)
b14.grid(row=4,column=2,padx=10,pady=6)
b14.bind('<Button-1>',click)

b15=Button(f1, text='/',bg='grey',fg='white',font='lucida 20 bold',width=3)
b15.grid(row=4,column=3,padx=10,pady=6)
b15.bind('<Button-1>',click)

b16= Button(f1, text='-',bg='grey',fg='white',font='lucida 20 bold',width=3)
b16.grid(row=4,column=4,padx=10,pady=6)
b16.bind('<Button-1>',click)

b17= Button(f1, text='(',bg='grey',fg='white',font='lucida 20 bold',width=3)
b17.grid(row=5,column=1,padx=10,pady=6)
b17.bind('<Button-1>',click)

b18= Button(f1, text=')',bg='grey',fg='white',font='lucida 20 bold',width=3)
b18.grid(row=5,column=2,padx=10,pady=6)
b18.bind('<Button-1>',click)

b19= Button(f1, text='%',bg='grey',fg='white',font='lucida 20 bold',width=3)
b19.grid(row=5,column=3,padx=10,pady=6)
b19.bind('<Button-1>',click)

b20= Button(f1, text='=',bg='grey',fg='white',font='lucida 20 bold',width=3)
b20.grid(row=5,column=4,padx=10,pady=6)
b20.bind('<Button-1>',click)
f1.pack()
root.mainloop()












