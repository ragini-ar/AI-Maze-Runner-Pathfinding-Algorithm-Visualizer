import tkinter as tk
from gui.maze_gui import MazeRunnerApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeRunnerApp(root)
    root.mainloop()