"""Реализовать класс Stack с использованием массива и списка"""

class StackException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Stack:
    def __init__(self, size: int = None) -> None:
        self.size = size
        self.__items = []
    
    def push(self, value: int) -> None:
        if self.size:
            if len(self.__items) == self.size:
                raise StackException("You can't push in stack, stack is full size.")
        self.__items.append(value)
    
    def pop(self) -> int:
        if len(self.__items) > 0:
            return self.__items.pop()
        else:
            raise StackException("You can't pop stack, stack is empty!")
    
    def peek(self) -> int:
        if len(self.__items) > 0:
            return self.__items[-1]
        else:
            raise StackException("You can't peek stack, stack is empty!")

    @property
    def count(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        return f"{self.__items}"
    
def test_create_stack():
    stack = Stack()
    assert isinstance(stack, Stack) == True
    
def test_push():
    stack = Stack()
    assert str(stack) == '[]'
    stack.push(1)
    assert str(stack) == '[1]'
    
def test_pop():
    stack = Stack()
    stack.push(1)
    item = stack.pop()
    assert str(stack) == '[]'
    assert item == 1

def test_peek():
    stack = Stack()
    stack.push(1)
    item = stack.peek()
    assert str(stack) == '[1]'
    assert item == 1

def test_count():
    stack = Stack()
    assert stack.count == 0
    stack.push(1)
    assert stack.count == 1

def test_pop_empty():
    stack = Stack()
    try:
        stack.pop()
    except StackException as se:
        assert str(se) == "You can't pop stack, stack is empty!"

def test_peek_empty():
    stack = Stack()
    try:
        stack.peek()
    except StackException as se:
        assert str(se) == "You can't peek stack, stack is empty!"

def test_push_full_size():
    stack = Stack(1)
    try:
        stack.push(1)
        stack.push(2)
    except StackException as se:
        assert str(se) == "You can't push in stack, stack is full size."


if __name__ == "__main__":
    test_create_stack()
    test_push()
    test_pop()
    test_peek()
    test_count()
    test_pop_empty()
    test_peek_empty()
    test_push_full_size()