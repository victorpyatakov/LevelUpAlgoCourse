"""Сдвинуть массив циклически на k-позиций влево"""

def cycle_shift_arr(arr: list, k: int) -> list: 
    k = k % len(arr)
    if k == 0 or k == len(arr):
        return arr

    while k > 0:
        tmp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = tmp
        k -= 1

    return arr
    
def test_correct():
    assert cycle_shift_arr([1,2,3,4,5], 2) == [3, 4, 5, 1, 2]

def test_k_module_n():
    assert cycle_shift_arr([1,2,3,4,5], 142) == [3, 4, 5, 1, 2]

if __name__ == "__main__":
    test_correct()
    test_k_module_n()
