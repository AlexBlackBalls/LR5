def min_t(n):
    S = 0
    for i in range(n):
        t = int(input())
        if i == 0 or t < min: 
            min = t
            S = 1
        elif t == min:       
            S += 1
    return S


print(min_t(int(input())))
