"""Даны два упорядоченных массива. Требуется выполнить слияние этих массивов. 
Результат – упорядоченный массив;"""

def get_sorted_concat_arr(arr_1: list[int], arr_2: list[int]) -> list[int]:
    if len(arr_1) == 0 and len(arr_2) == 0:
        return []
    i = j = 0 # указатель на положение 1 и 2 массива
    result = []
    while i + j <  len(arr_1) + len(arr_2):
        if i < len(arr_1) and j < len(arr_2):
            if arr_1[i] >= arr_2[j]:
                result.append(arr_2[j])
                j += 1
            else:
                result.append(arr_1[i])
                i += 1
        else: # если длина разная
            if i >= len(arr_1):
                result.append(arr_2[j])
                j += 1
            else:
                result.append(arr_1[i])
                i += 1
    return result

def test_equal_size():
    assert get_sorted_concat_arr([1,3,5,7], [2,4,6,8]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_diff_size():
    assert get_sorted_concat_arr([1,3,5,7], [2,4,6]) == [1, 2, 3, 4, 5, 6, 7]

def test_empty_list():
    assert get_sorted_concat_arr([],[]) == []

def test_one_list_empty():
    assert get_sorted_concat_arr([1,2],[]) == [1,2]

def test_both_list_same():
    assert get_sorted_concat_arr([1,2],[1,2]) == [1,1,2,2]

if __name__ == "__main__":
    test_diff_size()
    test_empty_list()
    test_equal_size()
    test_one_list_empty()
    test_both_list_same()