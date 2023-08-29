class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        self.s1.append(value)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop() if self.s2 else None

    def peek(self):
        if not self.s2:
            while self.s2:
                self.s2.append(self.s1.pop())
        return self.s2[-1] if self.s2 else None

    def empty(self):
        return not self.s1 and not self.s2


