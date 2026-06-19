import random

def generate_maze(width, height, start=(0, 0), goal=None):

    width = max(2, width)
    height = max(2, height)

    if goal is None:
        goal = (width - 1, height - 1)

    maze = [['#' for _ in range(2 * width + 1)]
            for _ in range(2 * height + 1)]

    def carve_passages(cx, cy, visited):
        stack = [(cx, cy)]
        visited.add((cx, cy))

        while stack:
            x, y = stack[-1]
            maze[2 * y + 1][2 * x + 1] = ' '

            neighbors = []

            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy

                if (0 <= nx < width and
                    0 <= ny < height and
                    (nx, ny) not in visited):
                    neighbors.append((nx, ny))

            if neighbors:
                nx, ny = random.choice(neighbors)

                visited.add((nx, ny))

                maze[y + ny + 1][x + nx + 1] = ' '

                stack.append((nx, ny))

            else:
                stack.pop()

    visited = set()

    carve_passages(
        random.randint(0, width - 1),
        random.randint(0, height - 1),
        visited
    )

    extra_walls = (width * height) // 4

    for _ in range(extra_walls):
        x = random.randint(1, 2 * width - 1)
        y = random.randint(1, 2 * height - 1)

        if maze[y][x] == '#':
            maze[y][x] = ' '

    sx, sy = 2 * start[0] + 1, 2 * start[1] + 1
    gx, gy = 2 * goal[0] + 1, 2 * goal[1] + 1

    maze[sy][sx] = 'S'
    maze[gy][gx] = 'E'

    return maze