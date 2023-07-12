class Node:
    def __init__(self, data):
        self.data: Node | None = data
        self.next: Node | None = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        #case-1 stack is empty
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("popped element is ", self.top.data)
            print("-----------------------")
            self.top = None
        else:
            temp = self.top
            print("Popped element is: ", self.top.data)
            print("------------------------")
            self.top = temp.next
            temp = None

    def display(self):
        if self.top is None:
            print("Empty")
        else:
            print("elements of stacks are: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
            print("TOP OF THE STACK IS: ", self.top.data)
            print("-------------------------------------")

if __name__ == "__main__":
    MyStack = Stack()

    MyStack.push(11)
    MyStack.push(12)
    MyStack.push(13)
    MyStack.push(15)

    MyStack.display()

    MyStack.pop()
    MyStack.pop()

