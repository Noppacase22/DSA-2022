def triangle(a, b, c):
    if min(a, b, c) <= 0: return False
    if max(a, b, c) >= (a+b+c)/2: return False
    return True

if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True
