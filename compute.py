from tkinter import messagebox
from main_options import add_digit, add_fraction, add_operation
from basic_func import work_window,clear,calc,fract,data_checking


def calculate(window):
    """
    This function calculates the value received from the "tkinter.Entry" window
    and adds the result to the "tkinter.Entry" window
    :param window: Entry
    :type window: class 'tkinter.Entry'
    """
    val = window.get()
    ch_1=data_checking(val,'(')
    ch_2 = data_checking(val, '+*-/^')
    if ch_1=='not':
        if ch_2=='not':
            pass
        else:
            first_number = val[:ch_2]
            second_number = val[(ch_2 + 1):]
            result = calc(first_number,second_number,val[ch_2])
            work_window(window,result)
    else:
        val = window.get()
        if ch_2 == 'not' and data_checking(val,'|') == 'not':
            pass
        else:
            ch_3 = data_checking(val,')')
            ch_4 = data_checking(val, '|')
            if ch_3=='not':
                if ch_4=='not':
                    pass
                else:
                    if len(val[ch_4 + 1:]) == 0:
                        first_number = val[:ch_2]
                        second_number = fract(val[ch_1 + 1:ch_4], 1, val[ch_2 + 1:ch_1])
                        result = calc(first_number, second_number, val[ch_2])
                        work_window(window, result)
                    else:
                        if ch_2 == 'not':
                            result = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:], val[:ch_1])
                            work_window(window, result)
                        else:
                            first_number = val[:ch_2]
                            second_number = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:], val[ch_2 + 1:ch_1])
                            result = calc(first_number, second_number, val[ch_2])
                            work_window(window, result)
            else:
                ch_5 = data_checking(val[ch_3:],'(')
                ch_6 = data_checking(val[ch_3:],'|')
                if ch_5=='not':
                    if ch_2=='not':
                        result = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:ch_3], val[:ch_1])
                        work_window(window, result)
                    else:
                        first_number = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:ch_3], val[:ch_1])
                        second_number = val[ch_2+1:]
                        result = calc(first_number, second_number, val[ch_2])
                        work_window(window, result)
                else:
                    if ch_6=='not':
                        pass
                    else:
                        ch_5 = ch_5 + ch_3
                        ch_6 = ch_6 + ch_3
                        if len(val[ch_6+1:])==0:
                            first_number = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:ch_3], val[:ch_1])
                            second_number = fract(val[ch_5 + 1:ch_6], 1, val[ch_2 + 1:ch_5])
                            result = calc(first_number, second_number, val[ch_2])
                            work_window(window, result)
                        else:
                            ch_7 = data_checking(val[ch_3+1:],')')
                            if ch_7=='not':
                                first_number = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:ch_3], val[:ch_1])
                                second_number = fract(val[ch_5 + 1:ch_6], val[ch_6 + 1:], val[ch_2 + 1:ch_5])
                                result = calc(first_number, second_number, val[ch_2])
                                work_window(window, result)
                            else:
                                ch_7 = ch_7 + ch_3 + 1
                                first_number = fract(val[ch_1 + 1:ch_4], val[ch_4 + 1:ch_3], val[:ch_1])
                                second_number = fract(val[ch_5 + 1:ch_6], val[ch_6 + 1:ch_7], val[ch_2 + 1:ch_5])
                                result = calc(first_number, second_number, val[ch_2])
                                work_window(window, result)