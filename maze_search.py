maze = [
    ['S', '.', '.', '#'],
    ['#', '.', '#', '.'],
    ['.', '.', '.', 'G']
]
start = (0, 0)  # Row 0, Col 0
goal = (2, 3)   # Row 2, Col 3

def neighbours(maze, position):
    rows = len(maze)
    cols = len(maze[0])

    row, col = position
    neighbours = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r = row + dr
        c = col + dc
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#':
            neighbours.append((r, c))
    return neighbours

# in this small project we will use bfs first
from collections import deque

def bfs(maze, start, goal):
    q = deque([[start]])
    visited = set()

    while q:
        # FIFO
        path = q.popleft()
        node = path[-1]

        if node in visited:
            continue

        if node == goal:
            return path

        visited.add(node)

        for neighbour in neighbours(maze, node):
            new_path = path + [neighbour]
            q.append(new_path)

    return None


# now we will implement dfs

def dfs(maze, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        # LIFO
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        if node == goal:
            return path
        visited.add(node)

        for neighbour in reversed(neighbours(maze, node)):
            new_path = path + [neighbour]
            stack.append(new_path)

    return None


# now we will use greedy-bfs

from queue import PriorityQueue

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def gbfs(maze, start, goal):
    frontier = PriorityQueue()
    frontier.put((manhattan(start, goal), [start]))
    visited = set()

    while not frontier.empty():
        _, path = frontier.get()
        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)


        for neighbour in neighbours(maze, node):
            new_path = path + [neighbour]
            priority = manhattan(neighbour, goal)
            frontier.put((priority, new_path))

    return None


path_bfs = bfs(maze, start, goal)
path_dfs = dfs(maze, start, goal)
path_gbfs = gbfs(maze, start, goal)

print("BFS (Shortest Path):", path_bfs)
print("DFS (A path, not guaranteed shortest):", path_dfs)
print("GBFS (Heuristic-based path):", path_gbfs)
