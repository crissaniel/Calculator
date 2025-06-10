from tkinter import*

root = Tk()
root.title("Calculator")
root.configure(bg="lightblue")

Header1 = Label(root, text="Calculator", font="Papyrus")
Header1.grid(row = 0, column = 0, columnspan = 5)

e = Entry(root, borderwidth = 5, font = ("Papyrus", 10))
e.grid(row=1, column=0, columnspan=5)

butt_num = 11

def buttClick(value):
    e.insert(END, str(value))

def backspace():
    current = e.get()
    e.delete(0, END) #Clears entire entry widget
    e.insert(0, current[:-1]) #Insert the text back into th entry display

def clear():
    e.delete(0, END)

def evaluate_pemdas():
    expression = e.get()
    def apply_operator(operators, values):
        operator = operators.pop()
        b = values.pop()
        a = values.pop()
        if operator == '+':
            values.append(a+b)
        elif operator == '-':
            values.append(a-b)
        elif operator == '*':
            values.append(a*b)
        elif operator == '/':
            values.append(a/b)
        elif operator == '-':
            values.append(a**b)

    def precedence(op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op in ('**'):
            return 3
        return 0
    
    operators = []
    values = []
    i = 0
    n = len(expression)
    while i < n:
        if expression[i].isdigit() or expression[i] == '.':
            num_str = ''
            while i < n and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i+=1
            values.append(float(num_str) if '.' in num_str else int(num_str))
            continue
        elif expression[i] == '(':
            operators.append(expression[i])
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        else:
            if expression[i] =='*' and i+1 < n and expression[i+1] == '*':
                op ='**'
                i += 1
            else:
                op = expression[i]
            while (operators and operators[-1] != '(' and precedence(operators[-1]) >= precedence(op)):
                apply_operator(operators, values)
            operators.append(expression[i])
        i+=1

    while operators:
        apply_operator(operators, values)
    
    e.delete(0, END)
    e.insert(0, str(values[0]))

                   
# Numeric buttons 1-9
for row in range(3, 6):
    for col in range(3): 
        Button(root, 
               text = butt_num-2, 
               width = 5, height = 2, 
               command = lambda num = butt_num-2: buttClick(num)
               ).grid(row=row, column=col)
        butt_num -=1

Button(root, text = 0, width =5, height = 2, command = lambda: buttClick(0)).grid(row=6, column=1)

# Operation buttons
Button(root, text = ".", width = 5, height = 2, command = lambda: buttClick(".")).grid(row=6, column = 0)
Button(root, text = "=", width = 5, height = 2, command = evaluate_pemdas).grid(row=6, column = 2)
Button(root, text = "+", width = 5, height = 2, command = lambda: buttClick("+")).grid(row=6, column = 3)
Button(root, text = "-", width = 5, height = 2, command = lambda: buttClick("-")).grid(row=5, column = 3)
Button(root, text = "x", width = 5, height = 2, command = lambda: buttClick("*")).grid(row=4, column = 3)
Button(root, text = "/", width = 5, height = 2, command = lambda: buttClick("/")).grid(row=3, column = 3)
Button(root, text = "C", width = 5, height = 2, command = clear).grid(row=2, column = 2)
Button(root, text = "<=", width = 5, height = 2, command = backspace).grid(row=2, column = 3)


root.mainloop()