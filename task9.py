# Задача 9. y1 = 1, y_n = 0.5 * (y_(n-1) + x / y_(n-1)); считаем, пока
# разница между соседними значениями не станет меньше eps
def y_loop(x, eps):
    prev = 1
    cur = 0.5 * (prev + x / prev)
    while abs(cur - prev) >= eps:
        prev = cur
        cur = 0.5 * (prev + x / prev)
    return cur


def y_rec(x, eps, prev=1):
    cur = 0.5 * (prev + x / prev)
    if abs(cur - prev) < eps:
        return cur
    return y_rec(x, eps, cur)


def solve(x, eps):
    print(y_loop(x, eps))
    print(y_rec(x, eps))


solve(float(input()), float(input()))
