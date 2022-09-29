"""Реализовать быструю сортировку"""

def get_pivot(arr): 
    return arr[0]

def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot = get_pivot(arr)
    less = [i for i in arr if i <= pivot]
    greater = [[i for i in arr if i > pivot]]

    return quick_sort(less) + [pivot] + quick_sort(greater)


def test_sort():
    assert  quick_sort([5, 4, 3, 6, 8, 1]) == [1, 3, 4, 5, 6, 8]


if __name__ == "__main__":
    test_sort()