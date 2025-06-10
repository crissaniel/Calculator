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

def calculate():
    operations = {'+','-','*','/'}
    expr = e.get()
    for element in expr:
        if isinstance(element, (int, float)):
            return
        elif element in operations:
            
        
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
Button(root, text = "=", width = 5, height = 2, command = calculate).grid(row=6, column = 2)
Button(root, text = "+", width = 5, height = 2, command = lambda: buttClick("+")).grid(row=6, column = 3)
Button(root, text = "-", width = 5, height = 2, command = lambda: buttClick("-")).grid(row=5, column = 3)
Button(root, text = "x", width = 5, height = 2, command = lambda: buttClick("*")).grid(row=4, column = 3)
Button(root, text = "/", width = 5, height = 2, command = lambda: buttClick("/")).grid(row=3, column = 3)
Button(root, text = "C", width = 5, height = 2, command = clear).grid(row=2, column = 2)
Button(root, text = "<=", width = 5, height = 2, command = backspace).grid(row=2, column = 3)


root.mainloop()