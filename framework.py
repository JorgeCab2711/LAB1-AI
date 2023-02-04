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


class GraphSearch:
    def dfs(self, matrix, start, end):
        rows, cols = len(matrix), len(matrix[0])
        visited = set()
        stack = [start]
        path = []
        while stack:
            curr = stack.pop()
            path.append(curr)
            if curr == end:
                return path
            visited.add(curr)
            row, col = curr
            neighbors = [(row - 1, col), (row + 1, col),
                         (row, col - 1), (row, col + 1)]
            for neighbor in neighbors:
                r, c = neighbor
                if 0 <= r < rows and 0 <= c < cols and neighbor not in visited and matrix[r][c] != "#":
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
