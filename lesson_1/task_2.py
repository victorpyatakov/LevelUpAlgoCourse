""" Дан массив целых числе. Требуется удалить из него все вхождения заданного числа;"""

def delete_number_in_arr(del_num: int, arr: list[int]) -> list[int]:
    if isinstance(del_num, int):
        i = 0
        while i < len(arr):
            if arr[i] == del_num:
                arr.pop(i)
                continue
            i += 1

        return arr
    else:
        raise TypeError("del_num must be int")
    
def test_correct():
    assert delete_number_in_arr(4, [1, 2, 3, 4, 4, 5]) == [1,2,3,5]

def test_wrong_format():
    try:
        delete_number_in_arr('1', [1, 2, 3, 4, 4, 5])
    except TypeError as te:
        assert str(te) == "del_num must be int"

def test_empty_arr():
    assert delete_number_in_arr(1, []) == []

def test_del_num_not_in_arr():
    assert delete_number_in_arr(1, [2,2,2]) == [2,2,2]

if __name__ == "__main__":
    test_correct()
    test_wrong_format()
    test_empty_arr()
    test_del_num_not_in_arr()