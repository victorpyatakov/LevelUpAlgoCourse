"""перевернуть строки в строке"""

def rev_sub_str_in_str(rev_str):
    def _swap(swap_str, i, j):
        begin = i
        end = j - 1
        while begin < end:
            tmp = swap_str[begin]
            swap_str[begin] = swap_str[end]
            swap_str[end] = tmp
            begin += 1
            end -= 1 

    i = 0
    j = 0

    while i < len(rev_str):
        if j == len(rev_str):
            _swap(rev_str, i , j)
            break
        if rev_str[j] == '_' :
            _swap(rev_str, i , j)
            i = j + 1
            j += 1
        else:
            j += 1

    _swap(rev_str, 0, len(rev_str))

    return "".join(rev_str)
    
def test_reverse():
    test_str = "ab_cde_fghj"
    assert rev_sub_str_in_str(list(test_str)) == "fghj_cde_ab"

if __name__ == "__main__":
    test_reverse()
    