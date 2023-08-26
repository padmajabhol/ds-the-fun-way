class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size

    def push(self, data):
        self.top += 1
        self.arr[self.top] = data

    def pop(self):
        x = self.arr[self.top]
        self.top -= 1
        return x

    def Top(self):
        return self.arr[self.top]

    def size(self):
        return self.top + 1

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.Top())
s.pop()
print(s.Top())
