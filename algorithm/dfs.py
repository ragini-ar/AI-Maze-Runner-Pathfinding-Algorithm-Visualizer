def is_valid(maze, x, y):

    return (
        0 <= y < len(maze)
        and 0 <= x < len(maze[0])
        and maze[y][x] != '#'
    )


def dfs(maze, start, goal):

    stack = [(start, [start])]

    visited = set()

    shortest_path = None

    while stack:

        current, path = stack.pop()

        if current == goal:

            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path

            continue

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]:

            nx = current[0] + dx
            ny = current[1] + dy

            if is_valid(maze, nx, ny) and (nx, ny) not in path:
                stack.append(
                    (
                        (nx, ny),
                        path + [(nx, ny)]
                    )
                )

    return shortest_path if shortest_path else []