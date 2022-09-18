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
    min = 0
    max = len(arr) - 1
    i = 0
    while i < len(arr) // 2:
        mid = (max + min) // 2
        if num > arr[mid]:
            min = mid
            i += 1
        elif num < arr[mid]:
            max = mid
            i += 1
        else:
            return mid
    return len(arr)

def test_find():
    assert get_binary_search_index([1,2,3,4,5,6,7,8], 6) == 5

def test_not_find():
    assert get_binary_search_index([1,2,3,4,5,6,7,8], 9) == 8

if __name__ == "__main__":
    test_find()
    test_not_find()

