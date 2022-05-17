import datetime
from functools import wraps
from typing import Union


def time_logger(funk):
    import time

    @wraps(funk)
    def tim(*args, **kwargs):
        tim1 = time.time()
        result = funk(*args, **kwargs)
        tim2 = time.time()
        timerr = f'time of function is {tim2 - tim1} seconds'
        with open('../../py/log.txt', 'a') as log:
            log.write(timerr)
            log.write(' name is ')
            log.write(funk.__name__)
            log.write('\n')
        return result
    return tim


def info_loger(funk):
    def tim(*args, **kwargs):
        result = funk(*args, **kwargs)
        with open('../../py/logg.txt', 'a') as log:
            log.write(f' acction -- {funk.__name__}')
            nam = funk.__name__
        if nam == 'credit_to_card':
            with open('../../py/logg.txt', 'a') as log:
                log.write(f' number -- {Bancomat.nummm}  ')
                log.write(f'money -- {Bancomat.money}\n')
        if nam == 'withdraw':
            with open('../../py/logg.txt', 'a') as log:
                log.write(f' pin -- {Bancomat.pin}  ')
                log.write(f'money -- {Bancomat.money}\n')
        else:
            with open('../../py/logg.txt', 'a') as log:
                log.write(f' cvv -- {Bancomat.cvv}, date -- {Bancomat.date}, reciver -- {Bancomat.an_ac}\n')
        return result

    return tim


class BankAcount:
    nums = []

    @staticmethod
    def date() -> str:
        a = str(datetime.datetime.now()).split()
        a = a[0]
        a = a.split('-')
        a = f'{a[1]}/{a[2]}'
        return a

    def __init__(self, name: str, pin: int, number: int, cvv: int, money=0):
        for i in BankAcount.nums:
            if i == number:
                print('this number is already exists')
                return
        self.ame = name
        self.__pin = pin
        self.num = number
        self.__cvv = cvv
        self._dat = BankAcount.date()
        self.__money = money
        BankAcount.nums.append(number)

    @info_loger
    def print_money(self, pin: int) -> int:
        """prints money amount of account"""
        if self.__pin == pin:
            return self.__money

    @info_loger
    @time_logger
    def credit_to_card(self, num: int, money: int) -> Union[str, int]:
        """increaces amount of money """
        if not num:
            return num
        if self.num == num:
            self.__money += money
            return 'transacttion complited'
        else:
            return 'error'

    @info_loger
    @time_logger
    def withdraw(self, pin: int, money: int):
        """reduces amount of money"""
        if self.__pin == pin:
            self.__money += money
            return 'transacttion complited'
        else:
            return 'error'

    @info_loger
    @time_logger
    def trans_to_card(self, another_acount, cvv: int, date: int, money: int):
        """transfers money from one card to other"""
        if self.__cvv == cvv and self._dat == date:
            self.__money += money
            another_acount.__money -= money
            return 'transacttion complited'
        else:
            return 'error'


class Bancomat:
    date = 0
    nummm = 0
    cvv = 0
    pin = 0
    an_ac = 0
    money = 0

    @staticmethod
    def print_money(acount):
        """prints money amount of account"""
        try:
            pin = int(input('input a pin: '))
        except ValueError:
            return 'it is not number'
        return BankAcount.print_money(acount, pin)

    @staticmethod
    @time_logger
    def credit_to_card(acount):
        """increaces amount of money """
        try:
            num = int(input('input a number: '))
        except ValueError:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
        except ValueError:
            return 'it is not number'
        Bancomat.nummm = num
        Bancomat.money = money
        return acount.credit_to_card(num, money)

    @staticmethod
    @time_logger
    def withdraw(acount):
        """reduces amount of money"""
        try:
            pin = int(input('input a pin: '))
        except ValueError:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
            money = money * -1
        except ValueError:
            return 'it is not number'
        Bancomat.pin = pin
        Bancomat.money = money * -1
        return acount.withdraw(pin, money)

    @staticmethod
    @time_logger
    def trans_to_card(acount, another_ack):
        """transfers money from one card to other"""
        try:
            date = input('date: ')
            cvv = int(input('cvv: '))
        except ValueError:
            return 'it is not number'
        try:
            money = int(input('number of money: '))
            money = money * -1
        except ValueError:
            return 'it is not number'
        Bancomat.money = money * -1
        Bancomat.cvv = cvv
        Bancomat.date = date
        Bancomat.an_ac = another_ack.ame
        return acount.trans_to_card(another_ack, cvv, date, money)


def main(first_ac, second_ac):
    a = 0
    while a != 235.5:
        try:
            a = int(input('what do you want to do? (1 -- credit to card, 2 -- withdraw, 3 -- trans out of card,'
                          ' 4 -- chek balanse, 5 -- finish ) '))
        except ValueError:
            print('it is not a number')
        if a == 1:
            print(Bancomat.credit_to_card(first_ac))
        if a == 2:
            print(Bancomat.withdraw(first_ac))
        if a == 3:
            print(Bancomat.trans_to_card(first_ac, second_ac))
        if a == 4:
            print(Bancomat.print_money(first_ac))
        if a == 5:
            return


ded = BankAcount('ded', 2283, 8753267899876535, 478)
vnuk = BankAcount('vnuk', 2285, 9753267899876535, 487)
main(ded, vnuk)
