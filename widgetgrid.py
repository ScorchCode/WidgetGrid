import tkinter as tk
from tkinter import ttk
"""
Display tkinter widgets in a resizable grid.

WidgetGrid.content is derived from tkinter.Text.
Its appearance can be configured with all the options of Text.
The tabs option controls the space between columns of widgets.
The spacing2 option controls the space between rows of widgets.
"""


class WidgetGrid(ttk.Frame):
    def __init__(self, parent, widgets=None):
        """
        :param parent:
            The containing widget
        :param widgets:
            Initial list of widgets
        """
        super().__init__(parent)
        self.widgetlist = widgets if widgets else []

        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.content = tk.Text(self, wrap=tk.CHAR, yscroll=self.scrollbar.set)
        self.scrollbar.configure(command=self.content.yview)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.content.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.update()

    def append(self, widget):
        """
        Add a widget and a TAB at the end.
        """
        self.widgetlist.append(widget)

        self.content.configure(state=tk.NORMAL)
        self.content.window_create(tk.END, window=widget)
        self.content.insert(tk.END, "\t")
        self.content.configure(state=tk.DISABLED)

    def clear(self):
        pass

    def delete(self, ndx):
        pass

    def insert(self, ndx):
        pass

    def sort(self, sortkey):
        pass

    def textindex(self, ndx):
        """
        Turn list index into Text index.

        :param ndx: int
        :return: str
        """
        return f"1:{ndx}"

    def update(self):
        """
        Show changes to more than one element.
        :return:
        """
        self.content.configure(state=tk.NORMAL)
        self.content.delete("1.0", tk.END)

        for wdg in self.widgetlist:
            self.content.window_create(tk.END, window=wdg)
            self.content.insert(tk.END, "\t")

        self.content.configure(state=tk.DISABLED)  # prevent accidental editing
