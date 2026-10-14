def num(a,b):
    low = min(a, b)
    high = max(a, b)
    while True:
        x = int(input())
        if low <= x <= high:
            break
    print("Число корректно")
num(int(input()),int(input()))    

        