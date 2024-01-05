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

def getNodeVal(head, index):
    curr = head
    count = 0
    while curr != None:
        if count == index:
            return curr.val
        
        count +=1
        curr = curr.next
    return None


def recgetNodeVal(head, index):
    if head == None:
        return None
    if index == 0:
        return head.val
    return recgetNodeVal(head.next, index - 1)

e = ListNode(5,None)
d = ListNode(4,e)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)


head = a
index = 7
print(getNodeVal(head, index))
