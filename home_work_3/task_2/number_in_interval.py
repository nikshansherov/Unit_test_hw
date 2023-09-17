def  number_in_interval(n: float) -> bool:
    if type(n) != float and type(n) != int:
        raise ValueError('Введеное значение должно быть числом')
    return 25 <= n <= 100