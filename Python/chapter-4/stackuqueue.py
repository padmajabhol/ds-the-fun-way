class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.append(element)

    def pop(self):
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        result = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self):
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        result = self.q1.pop(0)
        self.q2.append(result)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def is_empty(self):
        return len(self.q1) == 0

    def size(self):
        return len(self.q1)
