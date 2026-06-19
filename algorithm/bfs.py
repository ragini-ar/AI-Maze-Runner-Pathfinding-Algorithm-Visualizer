from collections import deque

def bfs(maze, start, end):

    queue = deque([start])

    visited = {start}

    parent = {}

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    while queue:

        x, y = queue.popleft()

        if (x, y) == end:

            path = []

            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]

            path.append(start)

            return path[::-1]

        for dx, dy in directions:

            nx, ny = x + dx, y + dy

            if (
                0 <= ny < len(maze)
                and 0 <= nx < len(maze[0])
                and maze[ny][nx] != '#'
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return []