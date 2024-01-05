class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def lenghtLL(head):
    curr = head
    count = 0
    while curr != None:
        count += 1
        curr = curr.next

    return count

e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)


head = a
index = 2
mycount = lenghtLL(head)
print(mycount, "my count")
