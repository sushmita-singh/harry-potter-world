import tkinter as tk
from tkinter import font
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from quotes import quote_app
from quotes.quote_app import QuoteApp
from books.book_app import BookApp

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Harry Potter World")
        self.root.geometry("800x400")
        self.root.configure(bg="#641e1e")

        # === Set global fonts here ===
        default_font = font.nametofont("TkDefaultFont")
        default_font.config(family="Garamond", size=14)
        font.nametofont("TkTextFont").config(family="Verdana", size=16, slant = 'italic')
        font.nametofont("TkMenuFont").config(family="Verdana", size=12)
        font.nametofont("TkHeadingFont").config(family="Garamond", size=35, weight="bold")
        font.nametofont("TkFixedFont").config(family="Garamond", size=20)
        # ============================

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f5f5f7")
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title_font = font.nametofont("TkHeadingFont") 
        self.title_label = tk.Label(
            self.main_frame,
            text="❾¾ --- Harry Potter World --- ⚯ ͛",
            font = title_font,
            fg="#D4AF37",
            bg="#f5f5f7"
        )
        self.title_label.pack(pady=(10, 20))

        self.button_frame = tk.Frame(self.main_frame, bg='#f5f5f7')
        self.button_frame.pack(expand=True)

        menu_font = font.nametofont("TkMenuFont") 
        self.quote_app_btn = tk.Button(
            self.button_frame,
            text="Explore Famous Quotes",
            font = menu_font,
            bg="#740001",
            fg="#f0c75e",
            activebackground="#7B3F00",
            activeforeground="#FAF3E0",
            command=self.go_to_quote_app
        )
        self.quote_app_btn.pack(pady=10)

        menu_font = font.nametofont("TkMenuFont") 
        self.book_app_btn = tk.Button(
            self.button_frame,
            text="Find Your Favorite Book",
            font = menu_font,
            bg="#740001",
            fg="#f0c75e",
            activebackground="#7B3F00",
            activeforeground="#FAF3E0",
            command=self.go_to_book_app
        )
        self.book_app_btn.pack(pady=10)

    def go_to_quote_app(self):
        QuoteApp(self.root)

    def go_to_book_app(self):
        BookApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()