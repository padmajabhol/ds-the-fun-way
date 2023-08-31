def max_heapify(arr, heap_size, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap the values
        max_heapify(arr, heap_size, largest)  # Recursively max heapify the affected subtree

# Example usage
arr = [4, 10, 3, 5, 1]
heap_size = len(arr)

# Applying max_heapify to index 1 (0-based indexing)
max_heapify(arr, heap_size, 1)

print(arr)  # Output: [10, 5, 3, 4, 1]
