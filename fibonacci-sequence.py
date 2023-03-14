#Fibonacci sequence : 0 1 1 2 3 5 8 13 21 34 55...

pn = 0
cn = 1
n = int(input("Enter the range: "))
if n<0:
    print("Invalid input")
    exit()
if n==0:
    print(0)
    exit()
if n==1:
    print(1)
    exit()
print (pn, end=' ')
print (cn, end=' ')
while cn<n:
    result = cn + pn
    pn = cn
    cn = result
    print (cn, end=' ')
