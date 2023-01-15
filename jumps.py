def jumps(n, a, b):
    list = [0]*(n+1)
    for i in range(1, len(list)):
        a1 = 0
        b1 = 0
        if i == a: a1 = 1
        elif i > a: a1 = list[i-a]
        if i == b: b1 = 1
        elif i > b: b1 = list[i-b]
        list[i] = a1 + b1
    return(list[n])

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937