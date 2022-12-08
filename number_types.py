from fractions import Fraction
class CommonNumber:
    '''Класс обычного числа'''
    def __init__(self, number=''):
        self.number = number
    def calc(self):
        return float(self.number)

class SimpleFraction(CommonNumber):
    '''Класс простой дроби,
    где numerator - числитель, а denominator - знаменатель'''
    def __init__(self,numerator='',denominator=''):
        self.numerator = numerator
        self.denominator = denominator
    def calc(self):
        '''Функция для проверки дроби на "Деление на ноль" и выведение результата расчета дроби'''
        try:
            2 / self.denominator
        except ZeroDivisionError:
            print("\nДеление на ноль!")
            return 'error'
        else:
            return float('%.2f' % (Fraction(self.numerator, self.denominator)))

class MixedFraction(CommonNumber):
    '''Класс смешанные дроби,
    где number - целое число, numerator - числитель, а denominator - знаменатель'''
    def __init__(self, number='', numerator='', denominator=''):
        super().__init__(number=number)
        self.numerator = numerator
        self.denominator = denominator
    def calc(self):
        '''Функция для проверки дроби на "Деление на ноль" и выведение результата расчета дроби'''
        try:
            2 / self.denominator
        except ZeroDivisionError:
            print("\nДеление на ноль!")
            return 'error'
        else:
            return float('%.2f' % (self.number * Fraction(self.numerator, self.denominator)))