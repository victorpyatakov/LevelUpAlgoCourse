"""Реализовать обход в ширину"""
from collections import deque

def make_graph(): 
    graph = {
        0: [1, 2, 3],
        1: [4, 5],
        2: [6, 8],
        3: [9],
        4: [],
        5: [],
        6: [7],
        7: [],
        8: [],
        9: []
    }
    return graph

def bfs(graph: dict, start_vertex: int, end_vertex: int):
    N = len(graph)
    search_queue = deque([start_vertex])
    distances = [None] * N
    distances[start_vertex] = 0
    parents = [None] * N
    while search_queue:
        u = search_queue.popleft()
        for v in graph[u]:
            if distances[v] is None:
                distances[v] = distances[u] + 1
                parents[v] = u
                search_queue.append(v)
    path = [end_vertex]
    parent = parents[end_vertex]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    
    return path[::-1]

def test_bfs():
    assert bfs(make_graph(), 0, 9) == [0, 3, 9]

if __name__ == "__main__":
    test_bfs()

