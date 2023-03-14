stack = []
stacksize = 4
for items in range(10):
    if len(stack) < stacksize:
        stack.append(int(input("Push:")))
else:
    print ("Stack overflow")

print ("Items in the stack:", stack)

for items in range(len(stack)+1):
    if not stack:
        print ("Stack underflow")
    else:
        print ("Pop:", stack.pop())
        print ("Current stack:", stack)
