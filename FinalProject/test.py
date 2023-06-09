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
        self.icon_img = ImageTk.PhotoImage(Image.open("icons/reset.png").resize((50, 50), Image.ANTIALIAS))
        self.generate_button = tk.Button(self, image=self.icon_img, command=self.generate_quote)
        self.settings_frame = tk.Frame(self, width=200, height=200, bg="white")
        self.settings_button = tk.Button(self.settings_frame, text="Settings", command=self.toggle_settings)
        self.add_quote_button = tk.Button(self.settings_frame, text="Add Quote", command=self.add_quote)
        self.display_all_button = tk.Button(self.settings_frame, text="Display All Quotes", command=self.display_all_quotes)
        self.color_label = tk.Label(self.settings_frame, text="Background Color:")
        self.color_button = tk.Button(self.settings_frame, text="Choose Color", command=self.change_background_color)

        self.quote_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.generate_button.pack(side=tk.BOTTOM, pady=10)
        self.settings_frame.place(relx=1.0, rely=0.0, anchor=tk.NE)
        self.settings_button.pack(pady=10, padx=10, anchor=tk.NE)
        self.add_quote_button.pack(pady=10, padx=10, anchor=tk.NW)
        self.display_all_button.pack(pady=10, padx=10, anchor=tk.NW)
        self.color_label.pack(pady=10, padx=10, anchor=tk.NW)
        self.color_button.pack(pady=10, padx=10, anchor=tk.NW)

        self.settings_visible = False

    def generate_quote(self):
        quote = self.quotes.get_random_quote()
        messagebox.showinfo("Random Quote", quote, icon="info")

    def toggle_settings(self):
        if self.settings_visible:
            self.settings_frame.place_forget()
            self.settings_visible = False
        else:
            self.settings_frame.place(relx=1.0, rely=0.0, anchor=tk.NE)
            self.settings_visible = True

    def add_quote(self):
        quote = simpledialog.askstring("Add Quote", "Enter a new quote:")
        if quote:
            self.quotes.add_quote(quote)
            messagebox.showinfo("Quote Added", "The quote has been added successfully!", icon="info")

    def display_all_quotes(self):
        all_quotes = self.quotes.quotes
        if all_quotes:
            messagebox.showinfo("All Quotes", "\n".join(all_quotes), icon="info")
        else:
            messagebox.showinfo("No Quotes", "There are no quotes to display.", icon="warning")

    def change_background_color(self):
        _, color = colorchooser.askcolor()
        if color:
            self.configure(background=color)

if __name__ == "__main__":
    app = GridApp()
    app.mainloop()
