def primes(N):
    a = 0
    for i in range(2,N+1):
        p = True
        for j in range(2,i-1):
            if i % j == 0:
                p = False
                continue
        if p == True:
            a+=1
    return a

if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15
