from number_types import CommonNumber, SimpleFraction, MixedFraction
def calculator():
    """Функция определяющая работу графического интерфейса калькулятора"""
    print("Калькулятор\n")
    while True:
        # Выводим сообщение какие действия есть
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Возвести в квадрат: ^\n"
              "Выйти: q\n")
        # Переменная для хранения действия
        action = input("Действие: ")

        # Если action равен q то
        if action == "q":
            # Выводим сообщение
            print("Выход из программы")
            # Выходим из цикла
            break

        # Если action равен +, -, *, /,^ то
        elif action in ('+', '-', '*', '/', '^'):

            # Выбор обычное число или дробь
            print("Выберите тип чисел:\n"
                  "Число: 1\n"
                  "Обычная дробь: 2\n"
                  "Смешаная дробь: 3\n")
            action_x = input("Тип первого числа: ")

            # Присваиваем значение переменной x
            if action_x == '1':
                x = CommonNumber(number=float(input("Целое число = "))).calc()
                print('')
            elif action_x == '2':
                x = SimpleFraction(numerator=int(input("Числитель = ")),
                                   denominator=int(input("Знаменатель = "))).calc()
                if x == 'error':
                    print('')
                    continue
            elif action_x == '3':
                x = MixedFraction(number=int(input("Целое число = ")),
                                  numerator=int(input("Числитель = ")),
                                  denominator=int(input("Знаменатель = "))).calc()
                print('')
                if x == 'error':
                    break

            # Присваиваем значение переменной y
            action_y = input("Тип второго числа: ")
            if action_y == '1':
                y = CommonNumber(number=float(input("Целое число = "))).calc()
                print('')
            elif action_y == '2':
                y = SimpleFraction(numerator=int(input("Числитель = ")),
                                   denominator=int(input("Знаменатель = "))).calc()
                print('')
            elif action_y == '3':
                y = MixedFraction(number=int(input("Целое число = ")),
                                  numerator=int(input("Числитель = ")),
                                  denominator=int(input("Знаменатель = "))).calc()
                print('')
            if y == 'error':
                continue

            # Если action равен + то
            if action == '+':
                print('Результат:', x + y, '\n')
            if action == '-':
                print('Результат:', x - y, '\n')
            if action == '*':
                print('Результат:', x * y, '\n')
            if action == '^':
                print('Результат:', x ** y, '\n')
            if action == '/':
                try:
                    x / y
                except ZeroDivisionError:
                    print("Деление на ноль!\n")
                    continue
                else:
                    print('Результат:', x / y, '\n')

        else:
            print('')
            continue

calculator()