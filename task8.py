def fact_for(n):
    S = 1
    for i in range(1, n + 1):
        S *= i
    return S


def fact_while(n):
    S = 1
    i = 1
    while i <= n:
        S *= i
        i += 1
    return S


def fact_rec(n):
    if n <= 1:  
        return 1
    return n * fact_rec(n - 1)


n = int(input())
print("for", fact_for(n))
print("while", fact_while(n))
print("рекурсия", fact_rec(n))


