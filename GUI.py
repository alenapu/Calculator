from tkinter import Button, Entry, Tk, RIGHT
from compute import calculate
from main_options import add_digit, add_fraction, add_operation
from basic_func import work_window,clear,calc,fract,data_checking


def btn_make(window, row, column, size_x=1, size_y=1, size=3, trans=0, \
             digit=None, operation=None, condition=None, fracton=None, enter=None):
    """
    This function creates buttons with specific functions: adding a number, operations, fractions,
    deleting an element, performing a calculation
    :param window: Entry
    :type window: class 'tkinter.Entry
    :param row: use cell identified with given row
    :type row: int
    :param column: use cell identified with given column
    :type column: int
    :param size_x: this widget will span several columns
    :type size_x: int
    :param size_y: his widget will span several rows sticky
    :type size_y: int
    :param size: widget width
    :type size: int
    :param trans: if set to positive, lines of text will wrap to fit in the widget's space
    :type trans: int
    :param digit: creating a button with the function of adding a number
    :type digit: str
    :param operation: creating a button with the function of adding an operation
    :type operation: str
    :param condition: creating a button with delete function
    :type condition: int
    :param fracton: creating a button with the function of adding a fraction
    :type fracton: str
    :param enter: creating a button with the function of performing a calculation
    :type enter: str
    """
    if digit != None:
        btn = Button(text=digit, bd=3, font=('Times New Roman', 14), wraplength=trans, width=size,
                     command=lambda: add_digit(window, digit))
    elif operation != None:
        btn = Button(text=operation, bd=3, font=('Times New Roman', 14), wraplength=trans, width=size,
                     command=lambda: add_operation(window, operation))
    elif condition == 0:
        btn = Button(text='C', bd=3, font=('Times New Roman', 14), wraplength=trans, width=size,
                     command=lambda: clear(window, 0))
    elif condition == 1:
        btn = Button(text='<', bd=3, font=('Times New Roman', 14), wraplength=trans, width=size,
                     command=lambda: clear(window, 1))
    elif fracton != None:
        btn = Button(text=fracton, bd=3, font=('Times New Roman', 14), wraplength=trans, width=size,
                     command=lambda: add_fraction(window))
    elif enter != None:
        btn = Button(text=enter, bd=3, font=('Times New Roman', 14), wraplength=trans, width=size,
                     command=lambda: calculate(window))
    btn.grid(row=row, column=column, rowspan=size_y, columnspan=size_x, padx=2, pady=2)

class GUI:

    def __init__(self, title='Калькулятор', geometr='287x205+500+150', color='#cce5dc'):

        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometr)
        self.root.resizable(width=False, height=False)
        self.root.config(bg=color)

        self.window = Entry(self.root, justify=RIGHT, font=('Times New Roman', 15), width=14)
        work_window(self.window, '0')
        self.window.grid(row=0, column=0, sticky='wens', columnspan=6, rowspan=3, padx=2, pady=2)

    def make(self):

        btn_1 = btn_make(window=self.window, row=3, column=1, size=3, digit='1')
        btn_2 = btn_make(window=self.window, row=3, column=2, size=3, digit='2')
        btn_3 = btn_make(window=self.window, row=3, column=3, size=3, digit='3')
        btn_4 = btn_make(window=self.window, row=4, column=1, size=3, digit='4')
        btn_5 = btn_make(window=self.window, row=4, column=2, size=3, digit='5')
        btn_6 = btn_make(window=self.window, row=4, column=3, size=3, digit='6')
        btn_7 = btn_make(window=self.window, row=5, column=1, size=3, digit='7')
        btn_8 = btn_make(window=self.window, row=5, column=2, size=3, digit='8')
        btn_9 = btn_make(window=self.window, row=5, column=3, size=3, digit='9')
        btn_0 = btn_make(window=self.window, row=6, column=2, size=8, size_x=2, digit='0')
        btn_dot = btn_make(self.window, row=6, column=0, size=8, size_x=2, digit='.')

        btn_degree = btn_make(window=self.window, row=3, column=0, size=3, operation='^')
        btn_division = btn_make(window=self.window, row=3,column=4, size=3, operation='/')
        btn_multiplication = btn_make(window=self.window, row=4,column=4, size=3, operation='*')
        btn_subtraction = btn_make(window=self.window, row=5,column=4, size=3, operation='-')
        btn_addition = btn_make(window=self.window, row=6, column=4, size=3, operation='+')

        btn_fraction = btn_make(window=self.window, row=4,column=0,size_y=2, trans=1, fracton='.-.')

        btn_clear1 = btn_make(window=self.window, row=3,column=5,condition=1)
        btn_clear = btn_make(window=self.window, row=4,column=5,condition=0)

        btn_enter = btn_make(window=self.window,row=5,column=5,size_y=2,trans=1,enter='ent')

        self.root.mainloop()
