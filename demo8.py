def cut1(p, n):
    if n == 0: return 0
    q = 0
    for i in range(n): q = max(q, p[i] + cut1(p, n-1))
    return q

def cut2(p, n):
    r = [0]*(n+1)
    for j in range(n):
        q = 0
        for i in range (j):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return r[n]

def main():
    p = [1, 5, 8, 9, 10]
    for i in [1,2,3,4,5]:
        print(f"Cut1: {cut1(p, i)}")
        print(f"Cut2: {cut2(p, i)}")

main()