"""Реализовать обходы бинарного дерева;"""
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


    def left_root_right(self) -> list[int]:
        def _left_root_right(root: NodeThreee, save_order: list[int]):
            if not root:
                return
            _left_root_right(root.left, save_order)
            save_order.append(root.value)
            _left_root_right(root.right, save_order)
        save_order = []
        _left_root_right(self.root, save_order)
        return save_order

def test_correct_order():
    bsf = BinarySearchThree()
    values = [5, 3, 2, 4 , 7, 6, 8]
    for value in values:
        bsf.insert(value)
    assert bsf.left_root_right() == [2, 3, 4, 5, 6, 7, 8]
    
if __name__ == "__main__":
    test_correct_order()


