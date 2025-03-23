def ffact(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    return fact
a = int(input('Enter a number: '))
f = ffact(a)
print('factorial of',a,'=',f)