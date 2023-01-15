def split(T):
    n = len(T)
    m = n-1
    
    a = [0]*n
    b = [0]*n
    a[0] = T[0]
    b[n-1] = T[n-1]

    for i in range(1,n):
        a[i] = max(a[i-1], T[i])
        b[m-i] = min(b[m-i+1], T[m-i])

    summa = 0
    for i in range(n-1):
        if a[i] < b[i+1]: summa+=1

    return summa

if __name__ == "__main__":
    print(split([1,2,3,4,5])) # 4
    print(split([5,4,3,2,1])) # 0
    print(split([2,1,2,5,7,6,9])) # 3
    print(split([1,2,3,1])) # 0
