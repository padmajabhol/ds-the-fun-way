class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Output: [1, 2, 3]

queue.dequeue()
queue.display() # Output [2, 3]
