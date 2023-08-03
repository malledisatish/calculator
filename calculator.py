import tkinter
from tkinter import*

root=Tk()
root.title("calculator")
root.geometry("550x600+100+200")
root.resizable(False,False)
root.configure(bg="#693c49")

equation=""
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)


label_result=Label(root,width=25,height=2,text="",font=("Times New Roman",30))
label_result.pack()

Button(root,text="C",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#e8646a",command=lambda: clear()).place(x=10,y=110)
Button(root,text="/",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: show("/")).place(x=150,y=110)
Button(root,text="%",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: show("%")).place(x=290,y=110)
Button(root,text="*",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: show("*")).place(x=430,y=110)

Button(root,text="7",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#0a0a0a",command=lambda: show("7")).place(x=10,y=205)
Button(root,text="8",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#0a0a0a",command=lambda: show("8")).place(x=150,y=205)
Button(root,text="9",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#0a0a0a",command=lambda: show("9")).place(x=290,y=205)
Button(root,text="-",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: show("-")).place(x=430,y=205)

Button(root,text="4",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#0a0a0a",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#0a0a0a",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#0a0a0a",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#0a0a0a",bg="#51cbdb",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#0a0a0a",bg="#51cbdb",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#0a0a0a",bg="#51cbdb",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0",width=9,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#0a0a0a",bg="#51cbdb",command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".",width=4,height=1,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=4,height=3,font=("Arial Rounded MT Bold",30,"bold"),bd=1,fg="#fff",bg="#05d4f0",command=lambda: calculate()).place(x=430,y=400)

root.mainloop()