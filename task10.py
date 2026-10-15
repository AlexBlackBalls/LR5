def pay(n):
    nom = 64
    while nom >= 1:
        c = n // nom  
        if c > 0:
            print(f"{nom} — {c}")
        n = n % nom       
        nom = nom // 2


pay(int(input()))
