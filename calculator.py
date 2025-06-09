from tkinter import*

root = Tk()
root.configure(bg="lightblue")

Header1 = Label(root, text="Calculator", font="Papyrus")
Header1.grid(row = 0, column = 0, columnspan = 3)

e = Entry(root)
e.grid(row=1, column=0, columnspan=3, pady=5)

butt_num = 10

for row in range(2, 5):
    for col in range(3): 
        Button(root, text = butt_num-1, width = 5, height = 2).grid(row=row, column=col)
        butt_num -=1

root.mainloop()