class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def find_middle(head):
    if head is None:
        return None

    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.val

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle = find_middle(head)
    
        
