from typing import Union


def is_int(a: str) -> Union[int, float, bool]:
    """
    Cheks is it int or float and returns float
    """
    try:
        a = float(a)
        return a
    except ValueError:
        return False


def is_operator(a: str) -> Union[str, bool]:
    """
    Cheks is it an operator and returns it
    """
    b = ['+', '-', '*', '/', '//', '%', '**']
    if a in b:
        return a
    else:
        return False
