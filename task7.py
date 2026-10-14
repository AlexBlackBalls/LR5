# Задача 7. НОД по алгоритму Евклида (вычитанием): циклом и рекурсией
def gcd_loop(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd_rec(a, b):
    if a == b:
        return a
    if a > b:
        return gcd_rec(a - b, b)
    return gcd_rec(a, b - a)


def solve(a, b):
    print(gcd_loop(a, b))
    print(gcd_rec(a, b))


solve(int(input()), int(input()))
