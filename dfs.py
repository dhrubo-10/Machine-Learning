# graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def dfs(graph, start, goal):
	# creating a set for storing the visited paths
	visited = set()
	stack = ([start])

	while stack:
		# last in first out, thats y we will use pop()
		path = stack.pop()
		node = path[-1]

		if node in visited:
			continue
		if node == goal:
			return path

		visited.add(node)

		# reversing to maintain the order
		# To keep the same order as BFS when using a stack 
		# (otherwise, DFS might always go right or left depending on how the list is structured).
		for neighbour in reversed(graph[node]):
			new_path = list(path)
			new_path.append(neighbour)
			stack.append(new_path)
	return None


result = dfs(graph, 'A', 'E')
print("DFS Path:", result)