Queue = [-100]*100
size_of_queue = 100
head = 0
tail = 0 

def push(x):
    global head , tail
    if queue_overflow():
        return "Queue is Full"
    else:
        Queue[tail]=x
        tail += 1
        
    return

def pop():
    global head , tail
    if queue_underflow():
        return "Queue is Empty"
    else:
        x = Queue[head]
        head += 1
    return x

def queue_overflow():
    global head ,tail
    if tail == size_of_queue:
        return True
    else:
        return False

def queue_underflow():
    global head, tail
    if tail == head:
        return True
    else:
        return False

def peek():
    global tail 
    if queue_underflow():
        return "Queue is empty"
    else:
        return Queue[head]

print(push(10))
print(push(20))
print(push(30))
print(peek())
print(pop())
print(pop())
print(peek())
print(pop())
print(pop()) 