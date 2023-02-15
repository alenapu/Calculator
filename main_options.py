from tkinter import messagebox
from fractions import Fraction
from compute import *
from basic_func import work_window,clear,calc,fract,data_checking


def add_digit(window, digit):
    """
    This function adds a value to the 'tkinter.Entry' window
    :param window: Entry
    :type window: class 'tkinter.Entry'
    :param digit: new value
    :type digit: str
    """
    val = window.get()
    ch_1 = data_checking(val, ')')
    if val[0]=='0' and len(val)==1:
        value = val[1:]
        work_window(window,value+digit)
    elif ch_1!='not':
        ch_2 = data_checking(val,'(')
        if len(val)-1==ch_1 and data_checking(val[ch_2+1:ch_1],'.')!='not':
            messagebox.showinfo('Ошибка', 'В значении дроби нельзя вводить десятичное число!')
            work_window(window,'0')
        elif len(val)-1!=ch_1 and data_checking(val[ch_2+1:ch_1],'.')!='not':
            messagebox.showinfo('Ошибка', 'В значении дроби нельзя вводить десятичное число!')
            work_window(window,'0')
        elif len(val)-1!=ch_1 and data_checking(val[ch_1+1:],')')!='not' and data_checking(val[ch_1+1:])!= 'not':
            messagebox.showinfo('Ошибка', 'В значении дроби нельзя вводить десятичное число!')
            work_window(window,'0')
        else:
            work_window(window,val+digit)
    else:
        ch_2 = data_checking(val,'+-/*^')
        if ch_2=='not':
            if data_checking(val,'.')!='not' and digit=='.':
                messagebox.showinfo('Ошибка', 'Десятичное чило вводится с одной запятой!')
                work_window(window,'0')
            else:
                work_window(window,val+digit)
        else:
            if data_checking(val[ch_2:],'.')!='not' and digit=='.':
                messagebox.showinfo('Ошибка', 'Десятичное чило вводится с одной запятой!')
                work_window(window,'0')
            else:
                work_window(window, val+digit)


def add_fraction(window):
    """
    This function adds a fraction construct to the "tkinter.Entry" window
    :param window: Entry
    :type window: class 'tkinter.Entry'
    """
    val = window.get()
    ch_1 = data_checking(val,'(')
    if ch_1=='not':
        if data_checking(val[-1],'+-/*^')!='not' or data_checking(val[-1],'0')=='not' or \
                data_checking(val[-1],'0')!='not' and len(val)>1:
            work_window(window,val+'(')
        else:
            work_window(window,val[1:]+'(')
    else:
        if data_checking(val[ch_1+1:],'(')=='not':
            if data_checking(val[-1],')')!='not':
                pass
            else:
                if data_checking(val[ch_1:],'|')=='not':
                    if data_checking(val[-1],'(')=='not':
                        work_window(window,val+'|')
                    else:
                        work_window(window,val+'1|')
                else:
                    if data_checking(val[-1],'|')=='not' and data_checking(val,'-+*/^') !='not':
                        work_window(window,val+'(')
                    elif data_checking(val[-1],'|')=='not' and data_checking(val,'-+*/^') =='not':
                        work_window(window, val + ')')
                    else:
                        work_window(window,val+'1)')
        else:
            ch_2 = data_checking(val,')')
            if data_checking(val[ch_2+1:],')')!='not':
                pass
            else:
                if data_checking(val[-1],'(')!='not':
                    work_window(window,val+'1|')
                else:
                    if data_checking(val[ch_2:],'|')!='not':
                        if data_checking(val[-1],'|')!='not':
                            work_window(window,val+'1)')
                        else:
                            work_window(window,val+')')
                    else:
                        work_window(window,val+'|')


def add_operation(window, operation):
    """
    This function adds an operation to the "tkinter.Entry" window
    :param window: Entry
    :type window: class 'tkinter.Entry'
    :param operation: new operation
    :type operation: str
    """
    value = window.get()
    c = data_checking(value,'(')
    d = data_checking(value,')')
    if data_checking(value,'(')!='not' and data_checking(value,')')!='not' or c=='not':
        if data_checking(value,'-+/*^')=='not':
            work_window(window,value+ operation)
        elif data_checking(value[-1],'-+/*^')!='not':
            work_window(window,value[:-1]+ operation)
        else:
            calculate(window)
            work_window(window, window.get() + operation)
    else:
        work_window(window,value)