def subsets(n: int) -> list:
    if n == 1:
        list = [[1]]
        return list
    else:
        lista = subsets(n-1)
        length = len(lista)
        newlist = [0]*((2**n)-1)
        i = 0
        for i in range(length):
            subset = lista[i]
            nset = []
            for item in subset:
                nset.append(item)
            nset.append(n)
            newlist[i] = subset
            newlist[i+length+1] = nset
        newlist[length] = [n]
        return newlist


if __name__ == "__main__":
    print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3],
                        #  [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4],
                        #  [2, 3, 4], [1, 2, 3, 4]]
    S = subsets(10)
    print(S[95])    # [6, 7]
    print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
    print(S[826])   # [1, 2, 4, 5, 6, 9, 10]