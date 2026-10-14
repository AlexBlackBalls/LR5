import random

def guess_game(a, b):
    limit = random.randint(a, b)
    while True:
        x = int(input())
        if x > limit:
            print("Перелет")
        elif x < limit:
            print("Недолет")
        else:
            print("Число угадано")
            break

guess_game(int(input()), int(input()))
