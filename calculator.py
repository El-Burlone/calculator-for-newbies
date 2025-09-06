#modules
import ast
import operator
import math
import tkinter as tk
from PIL import Image, ImageTk

#the operations that are allowed
ops = {ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        "sqrt": math.sqrt,
        #transforms degrees to radians for trig functions
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        }

#function to evaluate the expression
def eval_expr(expr):
    def _eval(node):
        if isinstance(node, ast.Constant):
                return node.value
        if isinstance(node, ast.BinOp):
            return ops[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return ops[type(node.op)](_eval(node.operand))
        elif isinstance(node, ast.Call):
                func = node.func.id
                args = [_eval(arg) for arg in node.args]
                if func in ops:
                        return ops[func](*args)
                else:
                        return str("Unsupported function: " + func)
        else:
            return str("Unsupported operation: " + str(node))
    return _eval(ast.parse(expr, mode='eval').body)

#function to calculate the result and display it in the entry box
def calculate():
    expr = box.get()
    try:
        result = eval_expr(expr)
        box.delete(0, tk.END)
        box.insert(0, str(result))
    except Exception as e:
        box.delete(0, tk.END)
        box.insert(0, str("Error"))

#so the backspace button deletes the character before the cursor position
def backspace_func():
    cursor_pos = box.index(tk.INSERT)
    if cursor_pos > 0:
        box.delete(cursor_pos - 1)

root = tk.Tk() #make the screen

root.title("Calculator") #title of the window
root.geometry("400x600") #size of the window
root.configure(bg="black") #background color
root.resizable(1, 1) #make the window resizable

# Set the icon - ensure you have an icon file named "Calculator.ico" in the same directory
try:
    root.iconbitmap("calculator.ico")
    # Also try with iconphoto for taskbar
    img = Image.open("calculator.ico")  # or use a PNG file
    photo = ImageTk.PhotoImage(img)
    root.iconphoto(True, photo)  # True makes it the default for all windows
except:
    pass

for row in range(7):
    root.grid_rowconfigure(row, weight=1)  # make row expandable
for col in range(4):
    root.grid_columnconfigure(col, weight=1)  # make col expandable

#Buttons and Entry Box        
box = tk.Entry(root, width=10, borderwidth=5, bg="white", fg="black", font=("Arial", 24))
box.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
box.focus_set() #focus on the entry box when the program starts

equal = tk.Button(root, text="=", bg="blue", fg="white", font=("Arial", 24), command=calculate) #the equal button and command to initiate calcula function
equal.grid(row=6, column=3, sticky="nsew", padx=5, pady=5)

plus = tk.Button(root, text="+", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "+")) #command to insert + in the entry box
plus.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

minus = tk.Button(root, text="-", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "-"))
minus.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

multiply = tk.Button(root, text="x", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "*"))
multiply.grid(row=3, column=3, sticky="nsew", padx=5, pady=5)

divide = tk.Button(root, text="÷", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "/"))
divide.grid(row=2, column=3, sticky="nsew", padx=5, pady=5)

one = tk.Button(root, text="1", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "1"))
one.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

two = tk.Button(root, text="2", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "2"))
two.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

three = tk.Button(root, text="3", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "3"))
three.grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

four = tk.Button(root, text="4", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "4"))
four.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

five = tk.Button(root, text="5", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "5"))
five.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

six = tk.Button(root, text="6", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "6"))
six.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

seven = tk.Button(root, text="7", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "7"))
seven.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

eight = tk.Button(root, text="8", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "8"))
eight.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

nine = tk.Button(root, text="9", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "9"))
nine.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)

zero = tk.Button(root, text="0", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "0"))
zero.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

decimal = tk.Button(root, text=".", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "."))
decimal.grid(row=6, column=2, sticky="nsew", padx=5, pady=5)

sin = tk.Button(root, text="sin", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "sin("))
sin.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

cos = tk.Button(root, text="cos", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "cos("))
cos.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

tan = tk.Button(root, text="tan", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "tan("))
tan.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

sqrt = tk.Button(root, text="√", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "sqrt("))
sqrt.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)

left_par = tk.Button(root, text="(", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "("))
left_par.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

right_par = tk.Button(root, text=")", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, ")"))
right_par.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

power = tk.Button(root, text="^", bg="black", fg="white", font=("Arial", 24), command=lambda: box.insert(tk.INSERT, "**"))
power.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

clear = tk.Button(root, text="C", bg="red", fg="white", font=("Arial", 24), command=lambda: box.delete(0, tk.END)) #command to clear the entry box
clear.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

backspace = tk.Button(root, text="⌫", bg="orange", fg="white", font=("Arial", 24), command=backspace_func)
backspace.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

#to calculate when Enter or = is pressed
box.bind('<Return>', lambda event: (equal.invoke(), "break")[1])
box.bind('=', lambda event: (equal.invoke(), "break")[1])

root.mainloop()