# Задача 10. Выплата суммы наименьшим числом купюр (1, 2, 4, 8, 16, 32, 64)
def pay(n):
    nominal = 64
    while nominal >= 1:
        count = n // nominal  # сколько купюр этого достоинства влезает
        if count > 0:
            print(f"{nominal} — {count}")
        n = n % nominal       # остаток, который выплачиваем дальше
        nominal = nominal // 2


pay(int(input()))
