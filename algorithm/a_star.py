import heapq

def heuristic(pos, end):

    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


def a_star(maze, start, end):

    open_list = []

    heapq.heappush(open_list, (0, start))

    g_costs = {start: 0}

    parent = {}

    directions = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == end:

            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)

            return path[::-1]

        for dx, dy in directions:

            nx = current[0] + dx
            ny = current[1] + dy

            if (
                0 <= ny < len(maze)
                and 0 <= nx < len(maze[0])
                and maze[ny][nx] != '#'
            ):

                tentative_g = g_costs[current] + 1

                if (
                    (nx, ny) not in g_costs
                    or tentative_g < g_costs[(nx, ny)]
                ):

                    parent[(nx, ny)] = current

                    g_costs[(nx, ny)] = tentative_g

                    f = tentative_g + heuristic(
                        (nx, ny),
                        end
                    )

                    heapq.heappush(
                        open_list,
                        (f, (nx, ny))
                    )

    return []