import math

a = 10**9
b = 1440*60*a
c = 100*365*b

i = 1
n = 1
while n < a:
    i +=1
    n = i*i
print(i)

while n*math.log2(n) < a:
    n += 1
print(n)

#while 2**i < c:
#    i += 1
#    n = 2**i 
#    print(f"2^{i} = {n}")
#    if n >= c:
#        print(i, "over C")
#    elif n>= b:
#        print(i, "over B")
#    elif n>= a:
#        print(i, "over A")

