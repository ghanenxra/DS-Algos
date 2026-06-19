stack = [-100]*100
size_of_stack = 100
top = -1

def push(x):
    global top
    if stack_overflow():
        return "Stack is full"
    
    else:
        top += 1
        stack[top]=x

        return

def pop():
    global top
    if stack_underflow():
        return "Stack is empty"
    else:
        x = stack[top]
        top -= 1
    return x

def peek():
    global top
    if stack_underflow():
        return "Stack Underflowed"

    else:
        return stack[top]

def stack_overflow():
    global top
    if top == size_of_stack-1:
        return True
    else:
        return False

def stack_underflow():
    global top
    if top==-1:
        return True
    else:
        return False


push(1)
push(3)
push(2)
pop()
print(peek())
