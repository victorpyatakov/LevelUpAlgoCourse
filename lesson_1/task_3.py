"""Дано неотрицательное число. Требуется перевернуть его;"""

def reverse_number(num: int) -> int:
    if isinstance(num, int) and num >= 0:
        if num // 10 == 0:
            return num

        res = num % 10 
        x = num // 10
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return res
    else:
        raise TypeError("Input atribute must be positive and int or float")
    
def test_int():
    assert reverse_number(123) == 321


def test_hundred():
    assert reverse_number(200) == 2

def test_one_digit():
    assert reverse_number(1) == 1

def test_equal_numbers():
    assert reverse_number(1111) == 1111

def test_wrong_format():
    try:
        reverse_number('123134')
    except TypeError as te:
        assert str(te) == "Input atribute must be positive and int or float"



if __name__ == "__main__":
    test_int()
    test_one_digit()
    test_equal_numbers()
    test_wrong_format()
    test_hundred()