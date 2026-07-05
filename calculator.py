from tkinter import *
from tkinter import messagebox

# =========================
# MATHEMATICAL CALCULATOR
# =========================

root = Tk()
root.title("Mathematical Calculator")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="lightgray")

expression = ""
equation = StringVar()


# -------------------------
# Functions
# -------------------------

def press(value):
    global expression
    expression += str(value)
    equation.set(expression)


def equal():
    global expression

    try:
        result = str(eval(expression.replace("^", "**")))
        equation.set(result)
        expression = result
    except ZeroDivisionError:
        equation.set("Cannot divide by zero")
        expression = ""
    except:
        equation.set("Invalid Expression")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def off():
    answer = messagebox.askyesno(
        "Exit",
        "Do you want to turn OFF the calculator?"
    )

    if answer:
        root.destroy()


# -------------------------
# Display Screen
# -------------------------

Entry(
    root,
    textvariable=equation,
    font=("Arial", 22),
    bd=10,
    relief=RIDGE,
    justify="right"
).grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=10, ipady=15)


# -------------------------
# Buttons
# -------------------------

buttons = [

    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),

    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),

    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),

    ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3),

    ('(',5,0), (')',5,1), ('^',5,2), ('=',5,3)
]


for (text, row, col) in buttons:

    if text == "=":
        Button(
            root,
            text=text,
            width=8,
            height=3,
            font=("Arial",12,"bold"),
            command=equal
        ).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(
            root,
            text=text,
            width=8,
            height=3,
            font=("Arial",12,"bold"),
            command=lambda t=text: press(t)
        ).grid(row=row, column=col, padx=5, pady=5)


# Bottom Buttons

Button(
    root,
    text="C",
    width=12,
    height=2,
    font=("Arial",12,"bold"),
    bg="orange",
    command=clear
).grid(row=6, column=0, columnspan=2, padx=5, pady=10)


Button(
    root,
    text="DEL",
    width=12,
    height=2,
    font=("Arial",12,"bold"),
    bg="gold",
    command=delete
).grid(row=6, column=2, columnspan=2, padx=5, pady=10)


Button(
    root,
    text="OFF",
    width=28,
    height=2,
    font=("Arial",12,"bold"),
    bg="red",
    fg="white",
    command=off
).grid(row=7, column=0, columnspan=4, padx=5, pady=10)


root.mainloop()