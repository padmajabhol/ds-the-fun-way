class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode | None = next

class LinkedList():

    def __init__(self):
        self.head = None

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        current = dummy
    
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
    
            if l1:
                current.next = l1
            if l2:
                current.next = l2
    
        return dummy.next

L = LinkedList()
n1 = ListNode(10)
#L.head = n1
n1.next = ListNode(20)
n1.next.next = ListNode(30)

n2 = ListNode(10)
n2.next = ListNode(40)
n2.next.next = ListNode(60)

merge_list = LinkedList.mergeTwoLists(n1, n2)



