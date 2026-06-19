class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(5)
node1.next = Node(10)
node1.next.next = Node(15)
node1.next.next.next = Node(20)
node1.next.next.next.next = Node(25)

head = node1

def insert(input_val, pointer, head):
    new_node = Node(input_val)
    length = 0
    while head != None:
        length += 1
        if head.next == None:
            last_node = head
        head = head.next
    head = perm_head    

    if pointer == 1:
        new_node.next = head
        head = new_node
        return head

    elif pointer == length:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return head

    else:
        temp = head
        for i in range(pointer-1):
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node
        return head

def delete(pointer, head):
    if pointer == 1:
        head = head.next
        return head

    temp = head

    for i in range(pointer -2):           #we can also write else here
        temp = temp.next                  #no need of else btw it can work without it  
    
    temp.next = temp.next.next
    return head

def display(head):
    while head is not None:
        print(head.data)
        head = head.next

    return head
        
head = delete(4, head)
display(head)










