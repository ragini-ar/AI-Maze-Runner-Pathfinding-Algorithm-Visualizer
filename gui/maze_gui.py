import tkinter as tk
import time

from maze.maze_generator import generate_maze
from algorithm.bfs import bfs
from algorithm.dfs import dfs
from algorithm.a_star import a_star


class MazeRunnerApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Maze Runner")

        self.maze_width = 15
        self.maze_height = 15

        self.cell_size = 20

        self.canvas_width = self.cell_size * (2*self.maze_width + 1)
        self.canvas_height = self.cell_size * (2*self.maze_height + 1)

        self.canvas = tk.Canvas(
            root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white"
        )

        self.canvas.pack()

        self.start = (0, 0)

        self.goal = (
            self.maze_width - 1,
            self.maze_height - 1
        )
    

        self.maze = generate_maze(
            self.maze_width,
            self.maze_height,
            self.start,
            self.goal
        )

        self.draw_maze()

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Button(
            frame,
            text="BFS",
            command=self.run_bfs
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame,
            text="DFS",
            command=self.run_dfs
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame,
            text="A*",
            command=self.run_astar
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
           frame,
           text="New Maze",
           command=self.generate_new_maze
        ).pack(side=tk.LEFT, padx=5)

    def draw_maze(self, path=None):

        self.canvas.delete("all")

        for y, row in enumerate(self.maze):

            for x, cell in enumerate(row):

                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if cell == '#':
                    color = "black"
                elif cell == 'S':
                    color = "green"
                elif cell == 'E':
                    color = "red"
                else:
                    color = "white"

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="gray"
                )

        if path:

            for x, y in path:

                self.canvas.create_rectangle(
                    x*self.cell_size,
                    y*self.cell_size,
                    x*self.cell_size+self.cell_size,
                    y*self.cell_size+self.cell_size,
                    fill="blue"
                )

    def get_start(self):

        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'S':
                    return (x, y)

    def get_goal(self):

        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 'E':
                    return (x, y)

    def run_bfs(self):

        start_time = time.perf_counter()

        path = bfs(
            self.maze,
            self.get_start(),
            self.get_goal()
        )

        end_time = time.perf_counter()
        
        print(f"Path Length: {len(path)}")

        print(
            f"BFS Time: {end_time-start_time:.6f} sec"
        )

        self.draw_maze(path)

    def run_dfs(self):

        start_time = time.perf_counter()

        path = dfs(
            self.maze,
            self.get_start(),
            self.get_goal()
        )

        end_time = time.perf_counter()
        
        print(f"Path Length: {len(path)}")

        print(
            f"DFS Time: {end_time-start_time:.6f} sec"
        )

        self.draw_maze(path)

    def run_astar(self):

        start_time = time.perf_counter()

        path = a_star(
            self.maze,
            self.get_start(),
            self.get_goal()
        )

        end_time = time.perf_counter()
        
        print(f"Path Length: {len(path)}")
        

        print(
            f"A* Time: {end_time-start_time:.6f} sec"
        )

        self.draw_maze(path)

    def generate_new_maze(self):
     self.maze = generate_maze(
        self.maze_width,
        self.maze_height,
        self.start,
        self.goal
    )

     self.draw_maze()
    