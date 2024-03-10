from tkinter import *

window = Tk()
window.title("Převod měn z CZK na Eura")
window.geometry("300x200")
window.resizable(False,False)

# 1 euro 23,80

def count_currency():
    final_amout = float(input_1.get()) / 23.80
    input_1.delete(0,END)
    result_label["text"] = round(final_amout,2)

input_1 = Entry(width=10, font=("Helvetica", 15))
input_1.focus()
input_1.grid(row=0,column=0)


CZKlabel = Label(text="CZK", font=("Helvetica", 15))
CZKlabel.grid(row=0, column=1)

result_label = Label(text="0", font=("Helvetica", 15))
result_label.grid(row=1,column=0)


EURlabel = Label(text="EUR",font=("Helvetica", 15))
EURlabel.grid(row=1,column=1)


count_button = Button(text="Převést", font=("Helvetica", 15), command=count_currency)
count_button.grid(row=0,column=2)


window.mainloop()