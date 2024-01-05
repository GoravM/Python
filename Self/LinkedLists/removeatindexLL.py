class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeatindex(head, n):
    curr = head
    count = 0
    while curr != None:
        prev = curr
        if count == n:
            prev.next = curr.next
            curr = curr.next
            count += 1
        else:
            curr = curr.next
            count += 1
            
    return count


e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)

head = a

removeatindex(head, 2)