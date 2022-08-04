from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# labels

my_label = Label(text="Iam a label", font=('Arial', 24))
my_label.grid(column=0, row=0)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text='click me', command=button_clicked)
button.grid(column=1, row=1)


# entry
input = Entry()
print(input.get())
input.grid(column=3, row=2)

# text entory
















window.mainloop()