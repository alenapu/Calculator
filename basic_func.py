from tkinter import messagebox, NORMAL, END, DISABLED
from fractions import Fraction



def data_checking(data,value):
    """
    This function searches for a value in the data and returns its index, if the value is not in the data returns 'not'
    :param data: array to search
    :type data: str
    :param value: desired value
    :type value: str
    :return: index value in data
    :rtype: int
    """
    for i in data:
        if i in value:
            check = data.index(i)
            break
        else:
            check = 'not'
    return check


def work_window(window, append):
    """
    This function updates the value of the window class 'tkinter.Entry' with the value of append
    :param window: Entry
    :type window: class 'tkinter.Entry'
    :param append: new window value
    :type append: str
    """
    window["state"] = NORMAL
    window.delete(0, END)
    append = str(append)
    window.insert(0, append)
    window['state'] = DISABLED


def fract(val_1,val_2,val_3):
    """
    This function calculates a fractional number with an integer part
    :param val_1: numerator
    :type val_1: str
    :param val_2: denominator
    :type val_2: str
    :param val_3: whole part
    :type val_3: str
    :return: val_3 * (val_1 / val_2)
    :rtype: float
    """
    result = 0
    if len(val_3)==0:
        try:
            result = Fraction(int(float(val_1)), int(float(val_2)))
        except ValueError:
            messagebox.showinfo('Ошибка', 'Неправильный ввод!')
    else:
        try:
            result = float(val_3) * Fraction(int(float(val_1)), int(float(val_2)))
        except ValueError:
            messagebox.showinfo('Ошибка', 'Неправильный ввод!')
    if type(result)==type(Fraction(5,10)):
        result= float(result)
    return result


def calc(numb_1,numb_2,operation):
    """
    This function calculates a value after performing an operation between number 1 and number 2
    :param numb_1: number 1
    :type numb_1: str
    :param numb_2:  number 2
    :type numb_21: str
    :param operation: /*-+^
    :type operation: str
    :return: numb_1 /(*/+/-/^) numb_2
    :rtype: str
    """
    try:
        number_1 = float(numb_1)
        number_2 = float(numb_2)
    except ValueError:
        messagebox.showinfo('Ошибка', 'Неправильный ввод!')
        result = '0'
    if operation == '/':
        try:
            result = str(number_1 / number_2)
        except ZeroDivisionError:
            messagebox.showinfo('Ошибка','Деление на ноль!')
            result = '0'
    elif operation == '*':
        result = str(number_1 * number_2)
    elif operation == '+':
        result = str(number_1 + number_2)
    elif operation == '-':
        result = str(number_1 - number_2)
    else:
        result = str(number_1 ** number_2)
    return result


def clear(window,condition):
    """
    This function removes the last value if condition = 1, and removes all if condition = 0
    :param window: Entry
    :type window: class 'tkinter.Entry'
    :param condition: 1 - deleting the last value; 2 - deleting everything
    :type condition: str
    """
    value = window.get()
    if condition==1:
        if value[0] != '0' and len(value) == 1:
            work_window(window,'0')
        elif len(value) != 1:
            window['state'] = NORMAL
            length = len(value) - 1
            window.delete(length, END)
            window['state'] = DISABLED
    else:
        work_window(window,'0')