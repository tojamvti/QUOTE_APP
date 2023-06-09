import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser
from PIL import ImageTk, Image
from quotes import Quotes

class GridApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quote Generator")
        self.geometry("500x300")
        self.resizable(False, False)
        
        self.quotes = Quotes()
        
        self.configure(background="white")
        
        self.quote_label = tk.Label(self, wraplength=400)
        self.quote_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.icon_img = Image.open("icons/reset.png")
        self.icon_img = self.icon_img.resize((50, 50), Image.ANTIALIAS)
        self.icon_img = ImageTk.PhotoImage(self.icon_img)

        self.generate_button = tk.Button(self, image=self.icon_img, command=self.generate_quote)
        self.generate_button.pack(side=tk.BOTTOM, pady=10)

        self.settings_button = tk.Button(self, text="Settings", command=self.open_settings)
        self.settings_button.pack(side=tk.TOP, pady=10, anchor=tk.NE)

        self.quote_label.configure(text=self.generate_quote())

    def generate_quote(self):
        quote = self.quotes.get_random_quote()
        self.quote_label.configure(text=quote)

    def open_settings(self):
        settings_window = tk.Toplevel(self)
        settings_window.title("Settings")
        settings_window.geometry("300x200")
        

        add_quote_button = tk.Button(settings_window, text="Add Quote", command=self.add_quote)
        add_quote_button.pack(pady=10)

        display_all_button = tk.Button(settings_window, text="Display All Quotes", command=self.display_all_quotes)
        display_all_button.pack(pady=10)

        def change_background_color():
            _, color = colorchooser.askcolor()
            if color:
                self.configure(background=color)

        color_button = tk.Button(settings_window, text="Background Color", command=change_background_color)
        color_button.pack()

    def add_quote(self):
        quote = simpledialog.askstring("Add Quote", "Enter a new quote:")
        if quote:
            self.quotes.add_quote(quote)
            messagebox.showinfo("Quote Added", "The quote has been added successfully!")

    def display_all_quotes(self):
        all_quotes = self.quotes.quotes
        if all_quotes:
            self.quote_label.configure(text=all_quotes)
        else:
            messagebox.showinfo("No Quotes", "There are no quotes to display.")

