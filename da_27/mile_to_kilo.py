from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    kilometer_result_lable.config(text=f'{km}')


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_lable = Label(text='Miles')
mile_lable.grid(column=2, row=0)

is_equal_lable = Label(text='is equal to')
is_equal_lable.grid(column=0, row=1)

kilometer_result_lable = Label(text='0')
kilometer_result_lable.grid(column=1, row=1)

kilometer_lable = Label(text='Km')
kilometer_lable.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)











window.mainloop()