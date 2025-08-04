# this is the heuristic h(n) that estimates how far the node is from the goal // for more check notes
def h(node):
	# Manhattan distance
	return abs(node.x - 5) + abs(node.y - 5)
# it uses manhattaN distance whch is total horizontal + vertical distance between two grids

