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


x = float(input())
eps = float(input())
print("цикл", y_loop(x, eps))
print("рекурсия", y_rec(x, eps))


