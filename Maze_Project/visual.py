def mark_path(maze, path):
    maze_copy = [row[:] for row in maze]
    for r, c in path:
        if maze_copy[r][c] not in ('S', 'G'):
            maze_copy[r][c] = '*'
    for row in maze_copy:
        print(' '.join(row))
