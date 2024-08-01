import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=300 , height=150)
window.config(padx=20,pady=20)
lable1 = tkinter.Label(text="Miles", font=["Ariel",24,"bold"])
lable2 = tkinter.Label(text="KMs",font=["Ariel",24,"bold"])
input1 = tkinter.Entry()
Label3= tkinter.Label(text="00",font=["Ariel",24, "bold"])
def buttonClick():
    i = int(input1.get())*1.60934
    Label3.config(text=f"{i}")


button= tkinter.Button(text="calculate", command=buttonClick)

lable1.grid(column=1,row=2)
input1.grid(column=3,row=2)
lable2.grid(column=1,row=3)
Label3.grid(column=3,row=3)
button.grid(columnspan=5,row=4)


window.mainloop()
