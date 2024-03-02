from tkinter import *

FONT = ("Arial", 12, "normal")

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=100)

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

miles = Label(text="miles", font=FONT)
miles.grid(column=2, row=0)

km = Label(text="km", font=FONT)
km.grid(column=2, row=1)

converted_value = Label(text="0", font=FONT)
converted_value.grid(column=1, row=1)


def calculator():
    mile = float(mile_input.get())
    km_v = round(mile * 1.609)
    converted_value.config(text=f"{km_v}")


button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)

mile_input = Entry()
mile_input.grid(column=1, row=0)
mile_input.get()

window.mainloop()
