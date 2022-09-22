"""Реализовать сортировку выбором"""

def choice_sort(arr: list[int]) -> list[int]:
    if not len(arr):
        return []

    point = 0

    while point < len(arr) - 1:
        min_index = point

        for index in range(point + 1, len(arr)):
            if arr[index] < arr[min_index]:
                min_index = index
        
        tmp = arr[point]
        arr[point] = arr[min_index]
        arr[min_index] = tmp

        point += 1

    return arr

def test_correct():
    arr = [5, 3, 8, 16, 9, 1]
    arr = choice_sort(arr)
    assert arr == [1, 3, 5, 8, 9, 16]

if __name__ == "__main__":
    test_correct()
        