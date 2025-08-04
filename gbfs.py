# we use PriorityQueue that lets us to pick the path with lowest heuristic value
from queue import PriorityQueue

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 7,
    'F': 2,
    'G': 1,
    'H': 0  # Goal
}

def h(n):
    return heuristic[n]


def gbfs(start, goal, graph, h):
	# frontier is a PriorityQueue that stores paths to explore
	frontier = PriorityQueue()
	# each item is a tuple
	frontier.put((h(start), [start]))
	# Initially, it holds the path [start], 
	# and its priority is h(start) how far we estimate it is from the goal.		
	visited = set()
	# visited is just like the others

	# loops keep running as long as the path there is to explore
	while not frontier.empty():
		# get the path the lowest heuristic value
		_, path = frontier.get()
		# keeping track of path
		node = path[-1]

		if node == goal:
			return path

		if node in visited:
			continue
		visited.add(node)


		for neighbour in graph[node]:
			# copy the current path and add to neighbours			
			new_path = path + [neighbour]
			# push the new path into the frontier
			# its priority is only on h(neighbour)
			frontier.put((h(neighbour), new_path))
			# ignores the path that costs more
	return None

result = gbfs('A', 'F', graph, h)
print("Path found:", result)