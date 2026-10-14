def count_min_days(n):
    count = 0
    for i in range(n):
        t = int(input())
        if i == 0 or t < minimum: 
            minimum = t
            count = 1
        elif t == minimum:       
            count += 1
    return count


print(count_min_days(int(input())))
