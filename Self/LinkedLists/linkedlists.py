class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove(curr, prev):
    prev.next = curr.next


def LinkedListValues(head):
    values = []
    curr = head
    while curr != None:
        values.append(curr.val)
        curr = curr.next
    return values

def fillValues(head, values):
    if head == None:
        return
    else:
        values.append(head.val)
        fillValues(head.next, values)

def recLinkedListValues(head):
    values = []
    fillValues(head, values)
    return values


e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)

head = a

print(recLinkedListValues(head))

