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

a = int(input())
b = int(input())
print("цикл", gcd_loop(a, b))
print("рекурсия", gcd_rec(a, b))



