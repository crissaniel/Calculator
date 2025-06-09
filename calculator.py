from tkinter import*

root = Tk()
root.configure(bg="lightblue")

Header1 = Label(root, text="Calculator", font=("Papyrus", 20))
Header1.grid(row = 0, column = 0, columnspan = 5)

e = Entry(root, font=("Papyrus", 20))
e.grid(row=1, column=0, columnspan=5, pady=5)

butt_num = 10

# Numeric buttons 1-9
for row in range(2, 5):
    for col in range(3): 
        Button(root, text = butt_num-1, width = 5, height = 2).grid(row=row, column=col)
        butt_num -=1
Button(root, text = 0, width =5, height = 2).grid(row=5, column=1)

# Operation buttons
Button(root, text = ".", width = 5, height = 2).grid(row=5, column = 0)
Button(root, text = "=", width = 5, height = 2).grid(row=5, column = 2)
Button(root, text = "+", width = 5, height = 2).grid(row=5, column = 4)
Button(root, text = "-", width = 5, height = 2).grid(row=4, column = 4)
Button(root, text = "x", width = 5, height = 2).grid(row=3, column = 4)
Button(root, text = "/", width = 5, height = 2).grid(row=2, column = 4)

root.mainloop()