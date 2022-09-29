"""Реализовать хещ таблицу"""




def hash_func(arr, value):
    siple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                            43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
                            101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
                            151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    sum = 0
    for s in str(value):
        sum += siple_numbers[ord(s) % len(siple_numbers)]
    return sum % len(arr)

class HashTable:

    def __init__(self, size: int, hash_func: callable) -> None:
        self.values = [[] for _ in range(size)]
        self.__hash_func = hash_func


    def add(self, value: list[any, any]): 
        position = self.__hash_func(self.values, value[0])
        self.values[position].append(value[1])

    def delete(self, value: list[any, any]): 
        position = self.__hash_func(self.values, value[0]) 
        for i in range(len(self.values[position])):
            if self.values[position][i] == value[1]:
                del self.values[position][i]
                
    def search(self, value: list[any, any]): 
        position = self.__hash_func(self.values, value[0]) 
        for i in self.values[position]:
            if i == value[1]:
                return True
        return False


    def __str__(self) -> str:
        return f'{[f"{i}: {v}" for i, v in enumerate(self.values)]}'
            

def test_add():
    hash_table = HashTable(4, hash_func=hash_func)
    hash_table.add(['first', 15])
    assert str(hash_table) == "['0: []', '1: []', '2: []', '3: [15]']"


def test_search():
    hash_table = HashTable(4, hash_func=hash_func)
    hash_table.add(['first', 15])
    assert hash_table.search(['first', 15]) == True
    
def test_delete():
    hash_table = HashTable(4, hash_func=hash_func)
    hash_table.add(['first', 15])
    hash_table.delete(['first', 15])
    assert str(hash_table) == "['0: []', '1: []', '2: []', '3: []']"

if __name__ == "__main__":
    test_add()
    test_search()
    test_delete()

    