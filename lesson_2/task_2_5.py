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


    def traverse(self):
        def _traverse(root: NodeThreee):
            if not root:
                return
            _traverse(root.left)
            print(root.value)
            _traverse(root.right)
        _traverse(self.root)


    
if __name__ == "__main__":
    bsf = BinarySearchThree()
    values = [5, 3, 2, 4 , 7, 6, 8]
    for value in values:
        bsf.insert(value)
    bsf.traverse()

