n = 5
included = [False]*n
numbers = [0,1,2,3,4]

def permutations(k):
    if k == n:
        print(numbers)
    else:
        for i in range(n):
            if not included[i]:
                included[i] = True
                numbers[k] = i+1
                permutations(k+1)
                included[i] = False

permutations(0)