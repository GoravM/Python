class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def zipperlist(head1, head2):
    tail = head1
    curr1 = head1.next
    curr2 = head2
    count = 0

    while curr1 != None and curr2 != None:
        if count % 2 == 0:
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1
    
    if curr1 != None:
        tail.next = curr1

    if curr2 != None:
        tail.next = curr2
    
    return tail.val


e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)
head1 = a

z = ListNode(3,None)
y = ListNode(2,z)
x = ListNode(1,y)

head2 = x

print(zipperlist(head1, head2))