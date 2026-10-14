# Задача 8. Факториал: for, while, рекурсия
def fact_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fact_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


def fact_rec(n):
    if n <= 1:  # 0! = 1 и 1! = 1
        return 1
    return n * fact_rec(n - 1)


def solve(n):
    print(fact_for(n))
    print(fact_while(n))
    print(fact_rec(n))


solve(int(input()))
