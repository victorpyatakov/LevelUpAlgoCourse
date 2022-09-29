"""Реализовать хещ таблицу"""

class HashTable:

    def __init__(self, size: int) -> None:
        self.values = [[] for _ in range(size)]
        self.siple_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
                              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
                              151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]


    def __hash_func(self, value):
        sum = 0
        for s in str(value):
            sum += self.siple_numbers[ord(s) % len(self.siple_numbers)]
        return sum % len(self.values)

    def add(self, value): 
        self.values[self.__hash_func(value)].append(value)

    def delete(self, value): 
        position = self.__hash_func(value) 
        for i in range(len(self.values[position])):
            if self.values[position][i] == value:
                del self.values[position][i]
                
    def search(self, value): 
        position = self.__hash_func(value) 
        for i in self.values[position]:
            if i == value:
                return True
        return False


    def __str__(self) -> str:
        return f'{[f"{i}: {v}" for i, v in enumerate(self.values)]}'
            

def test_add():
    hash_table = HashTable(4)
    hash_table.add(15)
    assert str(hash_table) == "['0: []', '1: []', '2: [15]', '3: []']"


def test_search():
    hash_table = HashTable(4)
    hash_table.add(15)
    assert hash_table.search(15) == True
    
def test_delete():
    hash_table = HashTable(4)
    hash_table.add(15)
    hash_table.delete(15)
    assert str(hash_table) == "['0: []', '1: []', '2: []', '3: []']"

if __name__ == "__main__":
    test_add()
    test_search()
    test_delete()

    