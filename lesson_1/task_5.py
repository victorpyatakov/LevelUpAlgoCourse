"""Посчитать количество единиц в двоичной записи числа"""

def get_count_ones(num: int) -> int:
    if isinstance(num, int):
        count_ones = 0
        while num:
            count_ones += num & 1
            num = num >> 1
        return count_ones
    else:
        raise TypeError("Input atribute must be int")

def test_good():
    assert get_count_ones(5) == 2

def test_wrong_format():
    try:
        get_count_ones('9')
    except TypeError as te:
        assert str(te) == "Input atribute must be int"

if __name__ == "__main__":
    test_good()
    test_wrong_format()