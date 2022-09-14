"""Даны три числа a,b,c. Требуется найти среди них медиану (серединное значение в отсортированной последовательности);"""

def find_mediane(a: int | float, b: int | float, c: int | float) -> int | float:
    if isinstance(a, int | float) and isinstance(b, int | float) and isinstance(b, int | float):
        if a > b and a > c:
            if b > c: 
                return b
            else: 
                return c
        elif a < b and a < c:
            if b > c: 
                return c
            else: 
                return b
        else:
            return a
    else:
        raise TypeError("Input atributes must be int or float")

def test_integer():
    assert find_mediane(1, 2, 3) == 2

def test_all_equal():
    assert find_mediane(2, 2, 2) == 2

def test_float():
    assert find_mediane(2.011, 2.1, 2.0124) == 2.0124

def test_negative():
    assert find_mediane(-10, -100, -2) == -10

def test_two_equal():
    assert find_mediane(4, 4, 5) == 4

def test_wrong_format():
    try:
        find_mediane('a', 2, 3)
    except TypeError as te:
        assert str(te) == "Input atributes must be int or float"
    

if __name__ == "__main__":
    test_integer()
    test_all_equal()
    test_float()
    test_negative()
    test_two_equal()
    test_wrong_format()