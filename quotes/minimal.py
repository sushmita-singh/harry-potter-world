import tkinter as tk

def on_click():
    print("Button clicked!")

root = tk.Tk()
root.geometry("200x100")

button = tk.Button(
    root,
    text="Test Button",
    bg="red",  # Background color
    fg="white",  # Text color
    activebackground="blue",  # Active background color
    activeforeground="yellow",  # Active text color
    command=on_click
)
button.pack(pady=20)

root.mainloop()