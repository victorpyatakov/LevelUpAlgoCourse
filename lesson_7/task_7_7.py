"""проверка симметричности бинарного дерева"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class NodeThreee:
    value: int
    left: NodeThreee | None = None
    right: NodeThreee | None = None

class BinarySearchThree:
    def __init__(self) -> None:
        self.root: NodeThreee = None
    
    def insert(self, value: int) -> None:
        def _insert(curent_root: NodeThreee, new_node: NodeThreee):
            if new_node.value < curent_root.value:
                if not curent_root.left:
                    curent_root.left = new_node
                else:
                    _insert(curent_root.left, new_node)
            else:
                if not curent_root.right:
                    curent_root.right = new_node
                else:
                    _insert(curent_root.right, new_node)

        new_node = NodeThreee(value=value)

        if not self.root:
            self.root = new_node
            return
        
        _insert(self.root, new_node)

    
    def is_symetric(self) -> bool:
        def _is_symetric(left: NodeThreee, right: NodeThreee) -> bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return  _is_symetric(left.left, right.right) and \
                    _is_symetric(left.right, right.left)

        if self.root is None:
            return True

        return _is_symetric(self.root.left, self.root.right)
        


def test_is_symetric():
    bsf = BinarySearchThree()
    values = [5, 3, 2, 4 , 7, 6, 8]
    for value in values:
        bsf.insert(value)
    assert bsf.is_symetric()

def test_is_not_symetric():
    bsf = BinarySearchThree()
    values = [5, 3, 4, 7, 8 ]
    for value in values:
        bsf.insert(value)
    assert bsf.is_symetric() == False
    
    
if __name__ == "__main__":
    test_is_symetric()
    test_is_not_symetric()




