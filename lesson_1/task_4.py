""" Дан массив чисел. Требуется найти такое число, которое равномерно 
удаленно от минимума и максимума;
func([1,2,3,4,5] -> 3)
"""

def find_medium_number(arr: list[int | float]) -> int | float | None:
    if len(arr) == 0:
        raise Exception("len arr must be > 0")

    if len(arr) < 3:
        raise Exception("count of arr elements must be > 2") 
        
    min = max = arr[0]
    all_int = True
    for i in arr[1:]:
        if min > i:
            min = i
        if i > max:
            max = i
        # если предположить, что массив может хранить только одного типа данные,
        # то я бы написал две функции для инта и для флоата
        if isinstance(i, float):
            all_int = False

    if min == max:
        raise Exception("elements of arr must be defferent")

    medium_number = float(min + max) / 2

    if all_int:
        medium_number = int(medium_number)

    # я бы написал medium_number in arr, но я не знаю, как это под капотом
    for el in arr:
        if el == medium_number: 
            return el
    
def test_empty_list():
    try:
        find_medium_number([])
    except Exception as e:
        assert str(e) == "len arr must be > 0"

def test_not_enough_numbers():
    try:
        find_medium_number([1])
    except Exception as e:
        assert str(e) == "count of arr elements must be > 2"

def test_same_elements():
    try:
        find_medium_number([1,1,1,1,1,1])
    except Exception as e:
        assert str(e) == "elements of arr must be defferent"

def test_integer():
    assert find_medium_number([1,2,3,4,5]) == 3

def test_float():
    assert find_medium_number([1.1, 2.2, 3.3, 4.4, 5.5]) == 3.3

if __name__ == "__main__":
    test_empty_list()
    test_not_enough_numbers()
    test_same_elements()
    test_integer()
    test_float()