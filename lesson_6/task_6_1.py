"""Реализовать обход в ширину"""
from collections import deque

def make_graph(): 
    graph = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [7, 9],
        4: [10],
        5: [],
        6: [],
        7: [8],
        8: [],
        9: [],
        10: []
    }
    return graph

def bfs(graph: dict, begin_vertex: int):
    print(begin_vertex)
    search_queue = deque()
    search_queue += graph[begin_vertex]
    searched = []
    while search_queue:
        vertex = search_queue.popleft()
        if vertex not in searched:
            print(vertex)
            search_queue += graph[vertex]
            searched.append(vertex)

if __name__ == "__main__":
    bfs(make_graph(), 1)

