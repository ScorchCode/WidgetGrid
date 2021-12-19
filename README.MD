# WidgetGrid
A Python + tkinter module to display widgets in a resizable grid.

![widgetgrid](https://user-images.githubusercontent.com/47459835/146667281-c93a7d06-0b1e-488f-bd9d-66e89cdf5740.png)

WidgetGrid is a tkinter.Frame containing a `tkinter.Text` and a vertical `tkinter.ttk.Scrollbar`. Put any number of widgets in the `WidgetGrid.content`. They will be displayed in a grid-like pattern, especially when they are all of the same size. There will be an automatic soft line break, so that upon window resizing the grid will adapt.

# Requirements
Python 3

# Installation
Copy `widgetgrid.py` to an appropriate folder.

# Usage

    from widgetgrid import WidgetGrid
    ...
    wg = WidgetGrid(parent)
    wg.content.configure(**options)
    
    wg.add(tkinter.Label(self, text="Spam"))

Configure the appearence of `WidgetGrid.content` (the `tkinter.Text` widget) in your main program with all options available for `tkinter.Text`. 

* The `tabs=` option controls the space between columns of widgets.
* The `spacing2=` option controls the space between rows of widgets.

Use `WidgetGrid.append(widget)` to add `widget` at the end of the grid. Every widget will be followed by a TAB character.

See `demo.py` for example.

# MIT License
Copyright (c) 2021 ScorchCode @ Github

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

