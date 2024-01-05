class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverselist(head):
    prev = None
    curr = head

    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev.val

def recreverselist(head, prev = None):
    if head == None:
        return prev.val
    next = head.next
    head.next = prev
    return recreverselist(next, head)

e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)

head = a

print(recreverselist(head, None))