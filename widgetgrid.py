import tkinter as tk
from tkinter import ttk
"""
Display tkinter widgets in a resizable grid.

WidgetGrid returns a tkinter.Frame.

WidgetGrid.content is a tkinter.Text.
Its appearance can be configured with all the options of Text.
The tabs option controls the space between columns of widgets.
The spacing2 option controls the space between rows of widgets.
"""


class WidgetGrid(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.content = tk.Text(self, wrap=tk.CHAR, yscroll=self.scrollbar.set, state=tk.DISABLED)
        self.scrollbar.configure(command=self.content.yview)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.content.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

    def append(self, widget):
        """
        Add a widget and a TAB at the end.
        """
        self.content.configure(state=tk.NORMAL)
        self.content.window_create(tk.END, window=widget)
        self.content.insert(tk.END, "\t")
        self.content.configure(state=tk.DISABLED)
