#fahreinheat to celsius coverter
import tkinter


window=tkinter.Tk()
window.title("sample")

def ftoc():
    ce=int(e.get())
    f=ce*(9/5)+32
    lb=tkinter.Label(window,text=f"fahrenheit value of {ce}c is:{f}")
    lb.pack()

#label widget
lab=tkinter.Label(window,text="Enter temperature in centigrade",fg="blue",bg="white",font="Times 20")
lab.pack()#to create window

#entry widget
e=tkinter.Entry(window,fg="black",bg="white",font="times 10")
e.pack()


#button widget(creating button)
button=tkinter.Button(window,text="convert",fg="Green",font="Times 20",command=ftoc)# prints the text given in function when button is cliked
button.pack()

#event loop
window.mainloop()
