import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Test Label", bg="yellow", fg="blue", font=("Arial", 20)).pack()

root.mainloop()