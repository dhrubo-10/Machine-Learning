from maze_map import maze, start, goal
from search_config import bfs, dfs, gbfs
from visual import mark_path

path_bfs = bfs(maze, start, goal)
path_dfs = dfs(maze, start, goal)
path_gbfs = gbfs(maze, start, goal)

print("BFS (Shortest Path):", path_bfs)
mark_path(maze, path_bfs)
print("DFS (A path, not guaranteed shortest):", path_dfs)
mark_path(maze, path_dfs)
print("GBFS (Heuristic-based path):", path_gbfs)
mark_path(maze, path_gbfs)
