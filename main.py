import tkinter
from  tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=350, height=250)
window.config(pady=50)

#weight
w_label = Label(text="Enter Your Weight (kg)")
w_label.config(fg="black")
w_label.pack()

w_entry = Entry(width=15)
w_entry.pack()



#height
h_label = Label(text="Enter Your Height (cm)")
h_label.config(fg="black")
h_label.pack()

h_entry = Entry(width=15)
h_entry.pack()



#calculate
def calculate():
    try:
        w_input = float(w_entry.get())
        h_input = float(h_entry.get())
        r = w_input / (h_input/100)**2

        bmi = ""
        if r < 18.5:
            bmi = "You are underwight."

        elif r < 24.9:
            bmi = "You are normal weight."

        elif r < 29.9:
            bmi = "You are pre-obesity."

        elif r < 34.9:
            bmi = "You are obesity class 1."

        elif r < 39.9:
            bmi = "You are obesity class 2."

        else:
            bmi = "Your are obesity class 3."

        r_label.config(text=f"Your BMI is {r}. {bmi}")
    except ValueError:
        r_label.config(text="Enter a valid number.")


#button
button = Button(text="Calculate", command=calculate)
button.config(bg="white")
button.pack()



r_label = Label(text="")
r_label.pack()





tkinter.mainloop()