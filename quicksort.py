import time

def qsort(A, i, j):
    pivot = int((i+j)/2)
    #print(1)
    swap(A, pivot, j)
    k = part(A, i, j-1, A[j])
    swap(A, k, j)
    if (k-i > 1): qsort(A, i, k-1)
    if (j-k > 1): qsort(A, k+1, j)

def swap(A, i, j):
    a = A[i]
    A[i] = A[j]
    A[j] = a

def part(A, left, right, pivot):
    while left<= right:
        while A[left] < pivot: left+= 1
        while right>= left and A[right] >= pivot: right -= 1
        if right > left: swap(A, left, right)
    return left

if __name__ == "__main__":
    print("Quiz 7 Question 3")
    A = [14,1,2,6,11,8,5,9,4,3,10,7,12,13]
    qsort(A, 0, len(A)-1)

    # print("Original implementation")
    """ A = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    B = [9, 7, 1, 8, 5, 3, 6, 2, 4]
    print(A) 
    a1 = time.time()
    qsort(A, 0, len(A)-1)
    a2 = time.time() - a1
    print(A) 
    b1 = time.time()
    B = B.sort()
    b2 = time.time() - b1 """

    # print("Comparison vs sort() with pseudo-random sample size ")
    """
    a = 42
    size = 2000000
    rang = 10000000
    A = []
    B = []
    for i in range(size):
        a += 8467319514123
        a = a % rang
        A.append(a)
        B.append(a)
    a1 = time.time()
    qsort(A, 0, len(A)-1)
    a2 = time.time() - a1
    b1 = time.time()
    B = B.sort()
    b2 = time.time() - b1
    print(f"{size} samples in range {rang}")
    print(f"Quicksort: {a2}")
    print(f"Python sort: {b2}")
    """
    