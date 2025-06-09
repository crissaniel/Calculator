from tkinter import*

root = Tk()
root.configure(bg="lightblue")

Header1 = Label(root, text="Calculator", font="Papyrus")
Header1.grid(row=0, column=1, columnspan=3)

# i = 0
# Create buttons for numbers 1 to 12 in a grid layout
# for i in range(12):
#     if columns > 0 :
#         B = Button(root, text = i+1, width = 5, height = 2).grid(row=rows, column=columns)
#         columns -=1
#         if columns < 0:
#             rows -= 1
#             B = Button(root, text = i+1, width = 5, height = 2).grid(row=rows, column=columns)
#             columns -= 1

butt_num = 9
for row in range(1, 4):
    for col in range(3): 
        Button(root, text = butt_num, width = 5, height = 2).grid(row=row, column=col)
        butt_num -=1



# add row +1 for the header text visibility, so row for the buttons will start at 1

# B1 = Button(root, text = "1", width = 5, height = 5).grid(row=2, column=2)
# B2 = Button(root, text = "2", width = 5, height = 5).grid(row=2, column=1)
# B3 = Button(root, text = "3", width = 5, height = 5).grid(row=2, column=0)
# B4 = Button(root, text = "4", width = 5, height = 5).grid(row=1, column=2)
# B5 = Button(root, text = "5", width = 5, height = 5).grid(row=1, column=1)
# B6 = Button(root, text = "6", width = 5, height = 5).grid(row=1, column=0)
# B7 = Button(root, text = "7", width = 5, height = 5).grid(row=0, column=2)
# B8 = Button(root, text = "8", width = 5, height = 5).grid(row=0, column=1)
# B9 = Button(root, text = "9", width = 5, height = 5).grid(row=0, column=0)
# B0 = Button(root, text = "0", width = 5, height = 5).grid(row=3, column=3)

root.mainloop()