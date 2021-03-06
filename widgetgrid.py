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

        self.show_all()

    def temp_enable(function):
        """
        Decorator: temporarily enable editing the Text widget.

        It's tk.DISABLED by default to avoid accidentally entering something.

        :return:
        """
        def wrap(*args):
            args[0].content.configure(state=tk.NORMAL)
            function(*args)
            args[0].content.configure(state=tk.DISABLED)
        return wrap

    @temp_enable
    def append(self, widget):
        """
        Add a widget and a TAB at the end.
        """
        self.widgetlist.append(widget)

        self.content.window_create(tk.END, window=widget)
        self.content.insert(tk.END, "\t")

    @temp_enable
    def clear(self):
        """
        Purge self.widgetlist and self.content.

        :return:
        """
        self.widgetlist = []
        self.content.delete("1.0", tk.END)

    @temp_enable
    def delete(self, ndx):
        """
        Delete one element from both list and content.

        :param ndx: int
        :return:
        """
        del self.widgetlist[ndx]
        self.content.delete(self.textindex(2*ndx), self.textindex(2*ndx+1))

    @temp_enable
    def insert(self, ndx, wdg):
        """
        Insert widget wdg into list and content at index ndx.

        :param ndx: int
        :param wdg: Widget
        :return:
        """
        pass

    @temp_enable
    def show_all(self):
        """
        Update content to show changes to more than one element.

        :return:
        """
        self.content.delete("1.0", tk.END)

        for wdg in self.widgetlist:
            self.content.window_create(tk.END, window=wdg)
            self.content.insert(tk.END, "\t")

    @temp_enable
    def sort(self, sortkey):
        """
        Sort widgetlist by sortkey and show newly sorted content.

        :param sortkey:
        :return:
        """
        pass

    def textindex(self, ndx):
        """
        Turn list index into Text index.

        :param ndx: int
        :return: str
        """
        return f"1:{ndx}"
