n = int (input ("Enter the number:"))
for x in range (2,n):
    for i in range (2,x):
        if x%i == 0:
            break
    else:
        print (x)