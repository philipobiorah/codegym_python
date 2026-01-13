
#iterative approaach

n = 6
f = 1

for i in range(1, n+1):
    f *= i

print(f)



#recusive approach
def fact(n):
    return 1 if n <=1 else n * fact(n-1)


print(fact(6))