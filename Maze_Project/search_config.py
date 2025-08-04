from collections import deque
from queue import PriorityQueue

def neighbours(maze, position):
	rows = len(maze)
	cols = len(maze[0])

	row,col = position
	neighbours = []

	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	for dr, dc  in directions:
		r = row + dr
		c = col + dc

		if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#':
			neighbours.append((r,c))
	return neighbours

def bfs(maze, start, goal):
	q = deque([[start]])
	visited = set()

	while q:
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

def dfs(maze, start, goal):
	stack = [[start]]
	visited = set()

	while stack:

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

def manhattan(a,b):
	return abs(a[0] - b[0]) + abs(a[1] + b[1])


def gbfs(maze, start, goal):
	frontier = PriorityQueue()
	visited = set()
	frontier.put((manhattan(start, goal), [start]))

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
			frontier.put((manhattan(neighbour, goal), new_path))

	return None


	