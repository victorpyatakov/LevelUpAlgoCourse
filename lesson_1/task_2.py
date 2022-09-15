""" Дан массив целых числе. Требуется удалить из него все вхождения заданного числа;"""

def delete_number_in_arr(del_num: int, arr: list[int]) -> list[int]:
    if isinstance(del_num, int):
        j = 0
        for i in range(len(arr)):
            if arr[i] != del_num:
                arr[j] = arr[i]
                j += 1
        return arr[:j]
    else:
        raise TypeError("del_num must be int")
    
def test_correct():
    assert delete_number_in_arr(4, [1, 2, 3, 4, 4, 5, 4]) == [1,2,3,5]

def test_wrong_format():
    try:
        delete_number_in_arr('1', [1, 2, 3, 4, 4, 5])
    except TypeError as te:
        assert str(te) == "del_num must be int"

def test_empty_arr():
    assert delete_number_in_arr(1, []) == []

def test_del_num_not_in_arr():
    assert delete_number_in_arr(1, [2,2,2]) == [2,2,2]

def test_all_el_deleted():
        assert delete_number_in_arr(2, [2,2,2]) == []

if __name__ == "__main__":
    test_correct()
    test_all_el_deleted()
    test_wrong_format()
    test_empty_arr()
    test_del_num_not_in_arr()