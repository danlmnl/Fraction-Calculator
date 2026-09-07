from tkinter import *
from tkinter import messagebox
from math import gcd

root = Tk()
root.title("Калькулятор дробей")
root.geometry("200x200")

k1 = Entry(root, width=10)
k1.grid(row=3, column=1)

k2 = Entry(root, width=10)
k2.grid(row=4, column=1)

k3 = Entry(root, width=10)
k3.grid(row=3, column=5)

k4 = Entry(root, width=10)
k4.grid(row=4, column=5)

operation = StringVar()
operation.set("+")

menu = OptionMenu(root, operation, "+", "-", "*", "/")
menu.grid(row=3, column=3, rowspan=2)

res = Entry(root, width=10, state="readonly")
res.grid(row=8, column=3)

def check_numerator(entry, number_of_entry):
    try:
        return int(entry.get().strip())
    except ValueError:
        messagebox.showerror("Ошибка",f"Некорректные символы в {number_of_entry} поле")
        entry.delete(0, END)
        return None

def check_numerators():
    a = check_numerator(k1, "первом")
    if a is None:
        return None

    c = check_numerator(k3, "третьем")
    if c is None:
        return None

    if operation.get() == "/" and c == 0:
        messagebox.showerror("Ошибка", "Деление на ноль невозможно")
        k3.delete(0, END)
        return None

    return a, c
    
def check_denominator(entry, number_of_entry):
    try:
        denominator = abs(int(entry.get().strip()))
    except ValueError:
        messagebox.showerror("Ошибка", f"Некорректные символы в {number_of_entry} поле")
        entry.delete(0, END)
        return None

    if denominator == 0:
        messagebox.showerror("Ошибка", "В знаменателе не допускается 0")
        entry.delete(0, END)
        return None
        
    return denominator

def check_denominators():
    b = check_denominator(k2, "втором")
    if b is None:
        return None

    d = check_denominator(k4, "четвёртом")
    if d is None:
        return None

    return b, d

def show_result(ch, zn):
    res.config(state="normal")
    res.delete(0, END)
    res.insert(0, f"{ch}/{zn}")
    res.config(state="readonly")

def plus(a, b, c, d):
    ch = a * d + b * c
    zn = b * d
    return ch, zn

def minus(a, b, c, d):
    ch = a * d - b * c
    zn = b * d
    return ch, zn

def multiply(a, b, c, d):
    ch = a * c
    zn = b * d
    return ch, zn

def divide(a, b, c, d):
    ch = a * d
    zn = b * c
    return ch, zn

def calculate():
    numerators = check_numerators()
    if numerators is None:
        return

    denominators = check_denominators()
    if denominators is None:
        return

    a, c = numerators
    b, d = denominators

    operations = {"+":plus, "-":minus, "*":multiply, "/":divide}
    ch, zn = operations[operation.get()](a, b, c, d)
    finally_res(ch, zn)

def finally_res(ch, zn):
    gcd1 = gcd(ch, zn)
    ch //= gcd1
    zn //= gcd1
    if zn<0:
        ch*=-1
        zn*=-1
    show_result(ch, zn)

k5 = Button(root, text="calculate", command=calculate)
k5.grid(row=10, column=3)

root.mainloop()
