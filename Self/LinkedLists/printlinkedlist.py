class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.next

def recprintLL(head):
    if head == None:
        return
    else:
        print(head.val)
        recprintLL(head.next)

e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)


head = a

print(printLinkedList(head))