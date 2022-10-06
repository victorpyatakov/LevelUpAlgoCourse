"""перевернуть строки в строке"""

def rev_sub_str_in_str(rev_str):
    def _swap(swap_str, i, j):
        while i < j:
            swap_str[i], swap_str[j] = swap_str[j], swap_str[i]
            i , j =  i + 1, j - 1

    def _get_next_char(rev_str, index) -> int:
        while index < len(rev_str) and rev_str[index] == '_':
            index += 1
        return index

    if not rev_str: return ""

    i, j = 0, 0

    while i < len(rev_str):
        i = _get_next_char(rev_str, i)
        if i == len(rev_str): break
        if i > j: j = i
        if j == len(rev_str):
            _swap(rev_str, i , j - 1)
            break
        if rev_str[j] == '_' :
            _swap(rev_str, i , j - 1)
            j, i = j + 1, j + 1
        else: j += 1

    _swap(rev_str, 0, len(rev_str) - 1)

    return "".join(rev_str)
    
def test_reverse():
    test_str = "ab_cde_fghj"
    assert rev_sub_str_in_str(list(test_str)) == "fghj_cde_ab"

def test_spaces():
    test_str = "___ab____cde___fghj___"
    assert rev_sub_str_in_str(list(test_str)) == "___fghj___cde____ab___"

def test_all_space():
    test_str = "_____________"
    assert rev_sub_str_in_str(list(test_str)) == "_____________"

def test_all_char():
    test_str = "abgd"
    assert rev_sub_str_in_str(list(test_str)) == "abgd"

def test_epty():
    test_str = ""
    assert rev_sub_str_in_str(list(test_str)) == ""

if __name__ == "__main__":
    test_reverse()
    test_spaces()
    test_all_space()
    test_all_char()
    test_epty()
    