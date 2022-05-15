from GoIT.lesson34 import validation, kalkulator
from typing import Union


def kalkulatorus(fir_num: Union[int, float], sec_num: Union[int, float], act: str) -> Union[int, float]:
    if act == '+':
        return kalkulator.plus(fir_num, sec_num)
    elif act == '-':
        return kalkulator.minus(fir_num, sec_num)
    elif act == '*':
        return kalkulator.umnozhit(fir_num, sec_num)
    elif act == '/':
        return kalkulator.podelit(fir_num, sec_num)
    elif act == '//':
        return kalkulator.podelit_celolochisleno(fir_num, sec_num)
    elif act == '%':
        return kalkulator.ostatok(fir_num, sec_num)
    elif act == '**':
        return kalkulator.stepen(fir_num, sec_num)


c = input("first number: ")
v = input("second number: ")
a = validation.is_int(c)
b = validation.is_int(v)
action = validation.is_operator(input("action: "))
if validation.is_operator(action) and validation.is_int(c) and validation.is_int(v):
    print(kalkulatorus(a, b, action))
else:
    print('error')
    