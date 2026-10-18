
# from tkinter import *


# # window = Tk()
# # window.title("Seance 13")
# # window.geometry("300x300")
# # window.minsize(100, 100)

# # k = ""
# # entry = Entry(window,textvariable=k)
# # entry.pack()


# # button = Button(window, text="Click me")
# # button.pack()



# # window.mainloop()

# from tkinter import *

# fenetre = Tk()
# fenetre.title("Calculator")
# fenetre.geometry("400×400")

# name_LabelA = Label(fenetre,text='Valeur de A: ')
# name_LabelA.grid(column=0,row=0,sticky='w')
# v1=StringVar()

# fenetre.mainloop()

from tkinter import *

def calculate1():
    a=int(v1.get())
    b=int(v2.get())  
    result.set(str(a+b))
def calculate2():
    a=int(v1.get())
    b=int(v2.get())  
    result.set(str(a-b))
def calculate3():
    a=int(v1.get())
    b=int(v2.get())  
    result.set(str(a/b))
def calculate4():
    a=int(v1.get())
    b=int(v2.get())  
    result.set(str(a*b))
def calculate():
    a=int(v1.get())
    b=int(v2.get())  
    result.set(str(a+b))

fenetre = Tk()
fenetre.title("Calculator")
fenetre.geometry("400x400")

v1=StringVar()
v2=StringVar()
result=StringVar()
# Box A 

name_LabelA = Label(fenetre, text="Valeur de A:") # consigne 
name_LabelA.grid(column=0, row=0, sticky="w")

entry_A = Entry(fenetre, textvariable=v1).grid(column=1, row=0,sticky='sw',padx=10) # enter 

# Box B

name_LabelB = Label(fenetre, text="Valeur de B:") # consigne 
name_LabelB.grid(column=0, row=1, sticky="w") # enter 

entry_B= Entry(fenetre, textvariable=v2).grid(column=1, row=1)

# Button : 

Button(fenetre, text="+", command=calculate1).grid(
    column=0, row=3, padx=10
)
Button(fenetre, text="-", command=calculate2).grid(
    column=1, row=3, padx=10
)
Button(fenetre, text="/", command=calculate3).grid(
    column=2, row=3, padx=10
)
Button(fenetre, text="*", command=calculate4).grid(
    column=3, row=3, padx=10
)

# BOX result 
Label(fenetre, text="Result:").grid(column=0, row=5)
Label(fenetre, textvariable=result).grid(column=1, row=5)


fenetre.mainloop()