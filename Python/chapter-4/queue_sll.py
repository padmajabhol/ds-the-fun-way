class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueu(self):
        data=int(input("Enter element to be inserted in the queueu."))
        new=Node(data)
        if self.front is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeu(self):
        if self.front = None:
            print("Queue is empty")
        elif self.front.next is None:
            print("Popped element is :", self.front.data)
            print("---------------------------------")
            self.front = None
        else:
            temp = self.front
            print("Popped element is :", self.front.data)
            print("---------------------------------")
            self.front = temp.next
            temp = None

        def display(self):
            if self.front is None:
                print("Queue is empty")
             else:
                 print("Elements of queue are:")
                 temp = self.front
                 while temp:
                     print(temp.data, end=" ")
                     temp = temp.next
                print("Front of queue is :", self.front.data)
                print("Rear of queue is :", self.rear.data)

q = Queue()

