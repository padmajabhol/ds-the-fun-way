class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

def is_valid_parentheses(s):
    stack = Stack()
    closeToOpen = {")":"(", "}":"{", "]":"["}

    for c in s:
        if c in closeToOpen.values():
            stack.push(c)
        elif c in closeToOpen.keys():
            if stack.is_empty() or closeToOpen[c] != stack.pop():
                return False
        else:
            return False

    return stack.is_empty()


test_string = "(({}))"
print(is_valid_parentheses(test_string))  # Output: True

test_string = "()"
print(is_valid_parentheses(test_string))
