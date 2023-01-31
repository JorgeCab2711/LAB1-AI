from abc import ABC, abstractmethod
from nodes import nodes

from collections import deque


class framework(ABC):
    @abstractmethod
    def __init__(self, matrix):
        pass

    # @abstractmethod
    # def find_start(self):
    #     pass

    # @abstractmethod
    # def actions(self, state):
    #     pass

    # @abstractmethod
    # def result(self, state, action):
    #     pass

    # @abstractmethod
    # def goalTest(self, state):
    #     pass

    # @abstractmethod
    # def stepCost(self, state, action):
    #     pass

    # @abstractmethod
    # def pathCost(self, path, begin, end):
    #     pass


class GraphSearch():
    def __init__(self):
        pass

    def dfs(matrix, start, end):
        stack = [start]
        visited = set()
        parent = {start: None}

        while stack:
            node = stack.pop()
            if node == end:
                path = []
                while node:
                    path.append(node)
                    node = parent[node]
                return path[::-1]

            visited.add(node)
            for neighbor in [(node[0]+1, node[1]), (node[0]-1, node[1]), (node[0], node[1]+1), (node[0], node[1]-1)]:
                if neighbor in matrix and neighbor not in visited:
                    parent[neighbor] = node
                    stack.append(neighbor)

        return None

    def find_path(self, start, end):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goalTest(self, state):
        pass

    def stepCost(self, state, action):
        pass

    def pathCost(self, path, begin, end):
        pass
