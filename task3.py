def find(x):
    S = x * (x + 1) // 2 
    for i in range(x - 1):
        S -= int(input())
    return S  


print(find(int(input())))
