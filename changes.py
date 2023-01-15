def changes(A):
    n = 0
    sarja = 1
    for i in range(1,len(A)):
        if A[i] == A[i-1]:
            sarja += 1
        else:
            n += int(sarja/2)
            sarja = 1
    n += int(sarja/2)
    return n

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2
    print(changes([1, 2, 5, 5, 4, 2]))  # 1
