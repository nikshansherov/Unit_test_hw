
def even_odd_number(n: int) -> bool:
    if type(n) != int:
        raise ValueError('Введеное значение должно быть целым числом')
    return n % 2 == 0
