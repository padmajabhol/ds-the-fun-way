from hypothesis import given, example
from merasort import insertionSort
from hypothesis.strategies import lists, integers
from collections import Counter

def is_sorted(arr):
    return arr == sorted(arr)

@given(arr=lists(elements=integers()))
@example([3, 2, 1])
def test_insertion_sort(arr):
    unsorted_array = arr[:]
    insertionSort(arr)
    c_unsorted = Counter(unsorted_array)
    c_sorted = Counter(arr)
    assert is_sorted(arr)
    assert c_sorted == c_unsorted

if __name__ == "__main__":
    test_insertion_sort()
