class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeatendindex(head, n):
    currL = head
    length = 0 # length of the original LL 
    while currL != None:
        length += 1
        currL = currL.next

    # index i want to remove at
    index = length - n
    curr = head
    count = 0
    while curr != None:
        prev = curr
        if count == index:
            print(curr.val, "removed")
            prev.next = curr.next
            curr = curr.next
            count += 1
        else:
            print(curr.val)
            curr = curr.next
            count += 1
    return head



e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)

n = 2
head = a
removeatendindex(head, 2)