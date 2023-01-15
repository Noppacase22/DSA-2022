def sums(items):
    luvut = {0: 1}
    x = 0
    for i in items:
        new = {}
        for j in luvut:
            summa = i + j
            new.update({j: 1})
            if summa not in luvut:
                new.update({summa: 1})
                x += 1
        luvut = new
    return x


# Juho Heiskasen ratkaisu:
"""
def sums(items):
    seen_sums = set()

    for x in items:
        for u in list(seen_sums):
            seen_sums.add(x + u)
        seen_sums.add(x)

    return len(seen_sums)   """
# Tästä opin settien olemassaolon :)

# Oma hitaampi ratkaisu listalla:
"""
def sums(items):
    items.sort()
    luvut = [0]
    x = 0
    for i in items:
        for j in range(len(luvut)):
            summa = i + luvut[j]
            if summa not in luvut:
                luvut.append(summa)
                x += 1
    return x    """

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
