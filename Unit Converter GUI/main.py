from tkinter import *

window = Tk()
window.title("First GUI")
window.minsize(500,300)

reference_label = Label(text="                               ")
reference_label.grid(column=0, row=0)
first_label = Label(text="Choose the conversion" , font=("Arial", 24, "bold"))
first_label.grid(column=1, row=0, columnspan=4)



def do_something():
   choice = radio_used()
   new_value = float(value.get())
   multiplier = 1
   if choice == 1:
        multiplier = 1.609344
   elif choice == 2:
        multiplier = 0.62137119
   elif choice == 3:
        multiplier = 0.393701
   elif choice == 4:
        multiplier = 2.54
   elif choice == 5:
        multiplier = 0.083
   elif choice == 6:
        multiplier = 12                              
   answer = round(new_value * multiplier, 2)
   label = Label(text = f"Converted value is {answer}")
   label.grid(column=2,row=5)        
def radio_used(): 
    choice = radio_state.get()
    return choice
       
radio_state = IntVar()
radiobutton1 = Radiobutton(text="miles to km", value=1, variable=radio_state)
radiobutton2 = Radiobutton(text="km to miles", value=2, variable=radio_state)
radiobutton3 = Radiobutton(text="cm to inches", value=3, variable=radio_state)
radiobutton4 = Radiobutton(text="inches to cm", value=4, variable=radio_state)
radiobutton5 = Radiobutton(text="inches to feet", value=5, variable=radio_state)
radiobutton6 = Radiobutton(text="feet to inches", value=6, variable=radio_state)
radiobutton1.grid(column=0, row=2)
radiobutton2.grid(column=1, row=2)
radiobutton3.grid(column=2, row=2)
radiobutton4.grid(column=3, row=2)
radiobutton5.grid(column=4, row=2)
radiobutton6.grid(column=5, row=2)

value = Entry()
print(value.get())
value.grid(column=2, row=3)
button = Button(text = "Convert", command=do_something)
button.grid(column=3, row=3)

window.mainloop()