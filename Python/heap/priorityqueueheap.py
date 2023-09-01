class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2*index + 1

    def right_child(self, index):
        return 2*index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        index = len(self.heap) - 1
        self.heapify_up(index)

    def extract_max(self):
        if not self.heap:
            return None
        max_item = self.heap[0]
        last_item = self.heap.pop()

        if self.heap:
            self.heap[0] = last_item
            self.heapify_down(0)
        return max_item

    def heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        max_index = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
        if index != max_index:
            self.swap(index, max_index)
            self.heapify_down(max_index)

pq = MaxPriorityQueue()
pq.insert(5)
pq.insert(4)
pq.insert(9)
pq.insert(10)
print(pq.extract_max())
