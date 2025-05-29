import tkinter as tk
from tkinter import font
from tkinter import ttk  # Import ttk for themed widgets
import random
from quote_generator import get_random_quote
import tkinter
print(tkinter.TkVersion)

class QuoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Harry Potter Quote Generator")
        self.root.geometry("800x400")
        self.root.configure(bg="#641e1e")  # Main background


        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f5f5f7")  # Main container
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Title
        title_font = font.Font(family="Karla", size=24, weight="bold")
        self.title_label = tk.Label(
            self.main_frame,
            text="✨ Harry Potter Quote Generator ✨",
            font=title_font,
            fg="#D4AF37",  # Gold color
            bg="#f5f5f7"
        )
        self.title_label.pack(pady=(0, 20))

        # Quote display area
        self.quote_frame = tk.Frame(self.main_frame, bg="#f5f5f7")
        self.quote_frame.pack(expand=True, fill='both')

        # Quote text
        quote_font = font.Font(family="Times New Roman", size=16, slant="italic")
        self.quote_label = tk.Label(
            self.quote_frame,
            font=quote_font,
            fg="#740001",  # Initial color
            bg="#f5f5f7",
            wraplength=750,
            justify="center"
        )
        self.quote_label.pack(expand=True)

        # Button frame
        self.button_frame = tk.Frame(self.main_frame, bg="#f5f5f7")
        self.button_frame.pack(pady=20)

        # New quote button
        self.new_quote_btn = tk.Button(
            self.button_frame,
            text="🪄 Get New Quote",
            bg="#740001",  # Red background
            fg="#f0c75e",  # Gold text color
            font=("Times New Roman", 14, "bold"),
            activebackground="#7B3F00",  # Active red background
            activeforeground="#FAF3E0",  # Active gold text color
            command=self.display_new_quote
        )
        self.new_quote_btn.pack(side=tk.LEFT, padx=10)

        # Exit button
        self.exit_btn = tk.Button(
            self.button_frame,
            text="❌ Exit",
            bg="#740001",  # Red background
            fg="#f0c75e",  # Gold text color
            font=("Times New Roman", 14, "bold"),
            activebackground="#7B3F00",  # Active red background
            activeforeground="#FAF3E0",  # Active gold text color
            command=self.root.quit
        )
        self.exit_btn.pack(side=tk.LEFT, padx=10)

        # Display initial quote
        self.display_new_quote()

    def display_new_quote(self):
        try:
            quote = get_random_quote()
            house_colors = ["#740001", "#2A623D", "#222F5B", "#EBA937"]
            random_color = random.choice(house_colors)
            self.quote_label.config(text=quote, fg=random_color)
            self.quote_label.update_idletasks()  # Ensure the label is updated
            print(f"Displaying quote: {quote}")  # Debug statement
        except Exception as e:
            error_msg = f"Error loading quote: {str(e)}"
            self.quote_label.config(text=error_msg, fg="#FF0000")
            print(error_msg)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QuoteApp()
    app.run()

