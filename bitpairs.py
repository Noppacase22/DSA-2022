def pairs(s):
    summa = 0
    bitit = 0
    edellinen = 0
    pituus = 0
    for i in range(0, len(s)):
        pituus += 1
        if s[i] == "1":
            x = pituus * bitit + edellinen
            summa += x
            edellinen = x
            bitit += 1
            pituus = 0
    return summa

if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71
