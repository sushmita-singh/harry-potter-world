import sys
import os
import tkinter as tk
from tkinter import font
import json
from PIL import Image, ImageTk
import webbrowser


class BookApp:
    def __init__(self, master):
        self.root = tk.Toplevel(master)
        self.root.title("Harry Potter Book Explorer")
        self.root.geometry("800x400")
        self.root.configure(bg="#641e1e")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="#f5f5f7")
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Header 
        self.header_frame = tk.Frame(self.main_frame, bg="#f5f5f7")
        self.header_frame.pack(fill='x')

        title_font = font.nametofont("TkHeadingFont")
        self.title_label = tk.Label(
            self.header_frame,
            text="📚 Harry Potter Book Explorer 📚",
            font=title_font,
            fg="#D4AF37",
            bg="#f5f5f7"
        )
        self.title_label.pack(pady=(0, 20))

        # Content frame
        self.content_frame = tk.Frame(self.main_frame, bg="#f5f5f7")
        self.content_frame.pack(expand=True, fill='both')

        # Scrollable book display area
        self.canvas = tk.Canvas(self.content_frame, bg="#f5f5f7", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f5f5f7")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        with open("books/books.json", "r", encoding="utf-8") as f:
            self.books_data = json.load(f)


        # Book display area

        for book in self.books_data:
            self.create_book_frame(self.scrollable_frame, book)

    def create_book_frame(self, parent, book):
        frame = tk.Frame(parent, bd=2, relief="groove", padx=10, pady=10, bg="#f5f5f7")
        frame.pack(fill='x', pady=8)

        # Load image
        try:
            image_path = os.path.join("books", "images", book["image"])  # Assuming your images are inside books/images/
            img = Image.open(image_path)
            img = img.resize((120, 180))  # Resize image to fixed size
            photo = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image for {book['title']}: {e}")
            photo = None

        img_label = tk.Label(frame, image=photo, bg="#f5f5f7")
        img_label.image = photo  # keep reference to prevent garbage collection
        img_label.pack(side="left")

        # Text container
        text_frame = tk.Frame(frame, bg="#f5f5f7")
        text_frame.pack(side="left", fill="both", expand=True, padx=15)

        title_label = tk.Label(
            text_frame, 
            text=book["title"], 
            font=("Times New Roman", 18, "bold"), 
            bg="#f5f5f7", 
            fg="#740001"
        )
        title_label.pack(anchor="w")

        info_label = tk.Label(
            text_frame, 
            text=book["summary"], 
            wraplength=500, 
            justify="left", 
            font=("Arial", 12),
            bg="#f5f5f7"
        )
        info_label.pack(anchor="w", pady=5)

        # Goodreads link label
        link_label = tk.Label(
            text_frame, 
            text="📖 View on Goodreads", 
            fg="#D4AF37", 
            cursor="hand2", 
            font=("Arial", 12, "underline"), 
            bg="#f5f5f7"
        )
        link_label.pack(anchor="w", pady=(5, 0))
        link_label.bind("<Button-1>", lambda e, url=book["goodreads_url"]: webbrowser.open(url))


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QuoteApp()
    app.run()