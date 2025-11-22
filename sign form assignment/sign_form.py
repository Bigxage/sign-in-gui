from tkinter import *
import tkinter.messagebox as message
def Sign_in():
    username=put1.get()
    password=put2.get()
    if username=="" or password=="":
        message.showinfo("Come on!","Empty record is not allowed, fill the form!")
    else:
        message.showwarning("Great one!", "Record filled successfully")


xage=Tk()
xage.geometry("400x600+500+0")
xage.resizable(0,0)
xage.title("Sign Form")
xage.configure(background="#aaeeff")

lbl=Label(xage, text="Insert details", bg="#aaeeff", fg="black", 
          font=("sanserif", 20, "bold"))
lbl.pack(side="top")

lbl1=Label(xage, text="Username (email): ", bg="#aaeeff", fg="black",
           font=("sanserif", 14))
lbl1.pack()
put1=Entry(xage, width=50, relief="flat")
put1.pack()

lblp=Label(xage, text="Password: ", bg="#aaeeff", fg="black",
           font=("sanserif", 14))
lblp.pack()
put2=Entry(xage, width=50, relief="flat", show="*")
put2.pack()

btn=Button(xage, text="Sign in", width=20, fg="white", bg="black", command=Sign_in)
btn.pack(pady=20)
xage.mainloop()