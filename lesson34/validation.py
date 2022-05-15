from typing import Union


def is_int(a: str) -> Union[int, float, bool]:
    try:
        a = float(a)
        return a
    except ValueError:
        return False


def is_operator(a: str) -> Union[str, bool]:
    b = ['+', '-', '*', '/', '//', '%', '**']
    if a in b:
        return a
    else:
        return False
