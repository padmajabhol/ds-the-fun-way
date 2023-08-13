class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class Stack:
    def __init__(self):
        self.head = None

    def s_append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def s_pop(self):
        if self.head:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        return None

    def isEmpty(self):
        if self.head is None:
            return True

def isValidParenthesis(s):
    stack = Stack()
    closeToOpen = {")":"(", "}":"{", "]":"["}

    for c in s:
        if c in closeToOpen.values():
            stack.s_append(c)
        elif c in closeToOpen.keys():
            if stack.isEmpty() or closeToOpen[c] != stack.s_pop():
                return False
        else:
            return False
    return stack.isEmpty()

test_string = "(({}))"
print(isValidParenthesis(test_string))

test_string = "({[)]}"
print(isValidParenthesis(test_string))

test_string = "(){}[]"
print(isValidParenthesis(test_string))

test_string = "{)"
print(isValidParenthesis(test_string))
