from tkinter import *
import sys

root = Tk()
root.geometry('350x550')
root.resizable(False,False)
root.title('TO DO LIST')
root.configure(background ='pink',relief=SUNKEN)

def add_task():
    task = entry_box.get()
    if task:
        Listbox.insert(END, task)
        entry_box.delete(0, END)

def delete_task():
    selected_task = Listbox.curselection()
    if selected_task:
        Listbox.delete(selected_task)

def exit():
    sys.exit()


input = StringVar()
label1= Label(root,text='TO DO LIST',font='italic 20 bold',bg='pink',fg='brown').pack(pady=3)
label2= Label(text='Enter the task',bg='olive',fg='white',font='quadrat 15 bold').pack(fill=X,pady=5)

entry_box = Entry(root ,textvariable=input,font= 'quadrat 10 bold')
entry_box.pack(fill=X,pady=5,ipady=8)

listbox_font =('quadrant',20)
Listbox = Listbox(root,height=8,width=70,font=listbox_font)
Listbox.pack(fill=Y)

button1 = Button(root,text='Add Task',command=add_task,font='quadrat 15 bold',bg ='olive' , fg = 'white', width=12,relief=SUNKEN).pack(fill=X,pady=3)
button2 = Button(root,text='Delete Task',command=delete_task,font='quadrat 15 bold',bg ='olive' , fg = 'white', width=12,relief=SUNKEN).pack(fill=X,pady=3)
button4 = Button(root,text='Exit',command=exit,font='quadrat 15 bold',bg ='olive' , fg = 'white', width=12,relief=SUNKEN).pack(fill=X,pady=3)


root.mainloop()