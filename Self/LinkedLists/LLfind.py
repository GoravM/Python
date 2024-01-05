class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findLL(head, target):
    curr = head
    while curr != None:
        if curr.val == target:
            return True
        curr = curr.next
    return False

def recfindLL(head, target):
    if head == None:
        return False
    if head.val == target:
        return True
    return recfindLL(head.next, target) 

e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)

head = a

print(recfindLL(head, 5))