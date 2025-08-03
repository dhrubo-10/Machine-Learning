from collections import deque # deque is a fast double-ended queue

# graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}


def bfs(graph, start, goal):
	# to keep track of visited nodes
	visited = set() 
	# Queue of Paths, not just nodes
	queue = deque([start])

	while queue:
		# get the first path from the queue like i studied in Accounting First in First Out
		path = queue.popleft()
		# look at the last node of the path, gives us the current node to check
		node = path[-1]

		# skip if already visited //mrk1
		if node in visited:
			continue
		# If goal found return to path 
		# bcs im not just trying to know that gaol is found, i wanna know how it got there
		if node == goal:
			return path

		# Mark node as visited from //mrk1
		visited.add(node)

		# now exploring the neighbours, the loop helps to explore next neighbour
		# For example, if node is 'A', then graph['A'] gives ['B', 'C'].
		for neighbour in graph[node]:
			# we copy the current path, the path we crossed so far..
			# here we create a list bcs we dont want to modify it
			# Example: If current path is ['A', 'C'], new_path starts as ['A', 'C'].
			new_path = list(path)
			# thn we will add the neighbour to the path
			new_path.append(neighbour)
			# thn we will add the new path to the queue
			queue.append(new_path)

	# if the goal isnt found
	return None

result = bfs(graph, 'A', 'D')
print("BFS Path:", result)