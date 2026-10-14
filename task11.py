# Задача 11*. Ханойские башни
# Переложить n дисков со стержня start на стержень end через стержень spare
def hanoi(n, start, spare, end):
    if n == 0:
        return
    hanoi(n - 1, start, end, spare)  # 1) верхние n-1 дисков - на запасной
    print(n, start, end)             # 2) самый большой диск - на место
    hanoi(n - 1, spare, start, end)  # 3) n-1 дисков с запасного - сверху


hanoi(int(input()), 1, 2, 3)
