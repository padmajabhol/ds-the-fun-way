class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        max_val = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max_val]:
                max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item

myQueue = PriorityQueue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
myQueue.insert(9)
print(myQueue)
while not myQueue.isEmpty():
    print(myQueue.delete())
