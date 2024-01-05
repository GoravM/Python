class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def SumLL(head):
    total = 0
    curr = head
    while curr != None:
        total += int(curr.val)
        curr = curr.next

    return total

def recSumLL(head):
    if head == None:
        return 0
    else:
        return head.val + recSumLL(head.next)

e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)


head = a

print(recSumLL(head))