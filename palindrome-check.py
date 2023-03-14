x = input("Enter the word:")
y = x[0:len(x):1] == x[len(x)::-1]
print (x, "is a Palindrome word:", y )



#Output: Boolean (True/False)
