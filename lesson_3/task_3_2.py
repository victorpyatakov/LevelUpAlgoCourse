"""Реализовать сортировку вставками"""

def insert_sort(arr: list[int]) -> list[int]:
    if not len(arr):
        return []
    i = 0
    while i < len(arr) - 1:

        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
        i += 1
    return arr

def test_sort():
    assert  insert_sort([5, 4, 3, 6, 8, 1]) == [1, 3, 4, 5, 6, 8]

if __name__ == "__main__":
    test_sort()
