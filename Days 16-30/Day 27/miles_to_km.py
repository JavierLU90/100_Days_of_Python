from tkinter import *

FONT = ("Arial", 12, "normal")

def calculate_button():
    miles = float(u_input.get())
    kms = round(miles * 1.60934, 2)
    label_3.config(text=f"{kms}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels
label_1 = Label(text="Miles", font=FONT)
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=FONT)
label_2.grid(column=0, row=1)

label_3 = Label(text="0", font=FONT)
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=FONT)
label_4.grid(column=2, row=1)

# Entry
u_input = Entry(font=FONT, width=10)
u_input.grid(column=1, row=0)

# Button
button = Button(text="Calculate", font=FONT, command=calculate_button)
button.grid(column=1, row=2)

window.mainloop()
