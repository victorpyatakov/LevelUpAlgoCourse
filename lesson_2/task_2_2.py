"""Дан упорядоченный массив. Требуется написать функцию бинарного поиска;"""

# def binary_search(arr: list[int], num: int) -> bool:
#     min = arr[0]
#     max = arr[-1]
#     i = 0
#     while i < len(arr) / 2:
#         print(i)
#         mid = (max + min) // 2
#         if num > mid:
#             min = mid
#             i += 1
#         elif num < mid:
#             max = mid
#             i += 1
#         else:
#             return True
#     return False

def get_binary_search_index(arr: list[int], num: int) -> int:
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    while left < mid:
        if num > arr[mid]:
            left = mid
        elif num < arr[mid]:
            right = mid
        else:
            return mid
        mid = (left + right) // 2
    return len(arr)

def test_find():
    assert get_binary_search_index([1,2,3,4,5,6,7,8], 6) == 5

def test_not_find():
    assert get_binary_search_index([1,2,3,4,5,6,7,8], 9) == 8

if __name__ == "__main__":
    test_find()
    test_not_find()

