from tkinter import *


f="Comic Sans MS"

def calculator():
    root=Tk()
    root.configure(background="honeydew")
    root.minsize(400,300)
    e = Entry(root,width=20,borderwidth=5,font=(f,22) )
    root.title("simple calculator")
    e.grid(row=0,column=0,columnspan=4,padx=1,pady=1)
    #cretaion of function 
    def clear():
        e.delete(0,END)
    def click(number):
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(number))
    def add():
        num=e.get()
        global fnum
        global math
        math="addition"
        fnum=float(num)
        e.delete(0,END)
    def equal():
        nume=e.get()
        e.delete(0,END)

        if math=="addition":
            e.insert(0,fnum+float(nume))
        elif math=="subtraction":
            e.insert(0,fnum-float(nume))
        elif math=="multiply":
            e.insert(0,fnum*float(nume))
        elif math=="division":
            e.insert(0,fnum/float(nume))
        elif math=="percentage":
            e.insert(0,fnum*(0.01*float(nume)))
        elif math=="root":
            if fnum<0:
                e.insert(0,"root of negative number is not defined")
            else:
                e.insert(0,fnum**0.5)                
    def subtract():
        num=e.get()
        global fnum
        global math
        math="subtratction"
        fnum=float(num)
        e.delete(0,END)
    def multiply():
        num=e.get()
        global fnum
        global math
        math="multiply"
        fnum=float(num)
        e.delete(0,END)
    def divide():
        num=e.get()
        global fnum
        global math
        math="division"
        fnum=float(num)
        e.delete(0,END)
    def percentage():
        num=e.get()
        global fnum
        global math
        math="percentage"
        fnum=float(num)
        e.delete(0,END)
    def back():
        a=e.get()
        e.delete(0,END)
        e.insert(0,a[:-1])      
    #genereating buttons
    
    button_back= Button(root,text="←",padx=36,pady=20,command =back ,bg="#FAEBD7",font=(f,13)) 
    button1=Button(root,text="1",padx=40,pady=20,command= lambda: click(1),bg="#FFFFF0",font=(f,13))    
    button2=Button(root,text="2",padx=40,pady=20,command= lambda: click(2),bg="#FFFFF0",font=(f,13))    
    button3=Button(root,text="3",padx=40,pady=20,command= lambda: click(3),bg="#FFFFF0",font=(f,13))    
    button4=Button(root,text="4",padx=40,pady=20,command= lambda: click(4),bg="#FFFFF0",font=(f,13))    
    button5=Button(root,text="5",padx=40,pady=20,command= lambda: click(5),bg="#FFFFF0",font=(f,13))    
    button6=Button(root,text="6",padx=40,pady=20,command= lambda: click(6),bg="#FFFFF0",font=(f,13))    
    button7=Button(root,text="7",padx=40,pady=20,command= lambda: click(7),bg="#FFFFF0",font=(f,13))    
    button8=Button(root,text="8",padx=40,pady=20,command= lambda: click(8),bg="#FFFFF0",font=(f,13))    
    button9=Button(root,text="9",padx=40,pady=20,command= lambda: click(9),bg="#FFFFF0",font=(f,13))    
    button0=Button(root,text="0",padx=40,pady=20,command= lambda: click(0),bg="#FFFFF0",font=(f,13)) 
    button_add=Button(root,text="+",padx=39,pady=20,command= add,bg="#FFFFF0",font=(f,13))   
    button_equal=Button(root,text="=",padx=98,pady=25,command= equal,bg="#ADFF2F")   
    button_clear=Button(root,text="Clear",padx=22,pady=20,command= clear,bg="#DC143C",font=(f,13)) 
    button_sub=Button(root,text="-",padx=39,pady=20,command= subtract,bg="#FFFFF0",font=(f,13))  
    button_mul=Button(root,text="*",padx=39,pady=20,command= multiply,bg="#FFFFF0",font=(f,13))  
    button_div=Button(root,text="/",padx=39,pady=20,command= divide,bg="#FFFFF0",font=(f,13))   
    button_percentage= Button(root,text="%",padx=35,pady=20,command=percentage,bg="#FFFFF0",font=(f,13))
    #arrangement of buttons
    button1.grid(row=3,column=0)
    button2.grid(row=3,column=1)
    button3.grid(row=3,column=2)
    button4.grid(row=2,column=0)
    button5.grid(row=2,column=1)
    button6.grid(row=2,column=2)
    button7.grid(row=1,column=0)
    button8.grid(row=1,column=1)
    button9.grid(row=1,column=2)
    button0.grid(row=4,column=0)
    button_add.grid(row=3,column=3)
    button_equal.grid(row=5,column=2,columnspan=2)
    button_clear.grid(row=5,column=0)
    button_mul.grid(row=4,column=2)
    button_div.grid(row=4,column=1)
    button_sub.grid(row=4,column=3)
    button_back.grid(row=5,column=1)
    button_percentage.grid(row=1,column=3,sticky="snew")
    mainloop()
