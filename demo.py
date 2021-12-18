import tkinter as tk
from tkinter import ttk

from icongrid import IconGrid


class MainWidget(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        root = root
        root.title("IconGrid Demo")
        root.geometry("600x400")

        ig = IconGrid(self)
        ig.content.configure(
            borderwidth=0,
            bg="grey",
            highlightthickness=0,
            padx=40,
            spacing1=20,
            spacing2=10,
            tabs="0.2c"
        )
        ig.pack(expand=True, fill=tk.BOTH)

        for i in range(200):
            ig.add(tk.Label(self, text=f"{i}", width=4))

        self.pack()


if __name__ == "__main__":
    app = tk.Tk()
    MainWidget(app)
    app.mainloop()
