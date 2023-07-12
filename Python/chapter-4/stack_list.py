def push():
    n = int(input("Enter the element to be inserted into the stack"))
    if len(stack) == 0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n, " is inserted into stack")

def pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print(stack[0], " is deleted from the stack")
        del stack[0]

stack = list()

