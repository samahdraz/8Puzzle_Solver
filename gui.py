import time
import tkinter as tk
from tkinter import messagebox
from bfs import bfs
from dfs import dfs
from a_manhattan import astar_m
from a_euclidean import astar_e


class EightPuzzleGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("8-Puzzle Solver")

        reset_button = tk.Button(self.master, text="Reset", command=self.reset_puzzle)
        reset_button.grid(row=3, column=0, padx=10, pady=10)

        self.initial_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
        # solvable (1, 2, 3, 4, 5, 6, 7, 8, 0)
        # unsolvable (1, 2, 3, 4, 5, 8, 0, 7, 6)
        self.goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

        self.selected_algorithm = tk.StringVar()
        self.selected_algorithm.set("BFS")  # Default selection

        self.create_widgets()

    def reset_puzzle(self):
        self.draw_puzzle(self.initial_state)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=300, height=300, borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        self.draw_puzzle(self.initial_state)

        algorithm_frame = tk.Frame(self.master)
        algorithm_frame.grid(row=1, column=0, padx=10, pady=10)

        algorithms = ["BFS", "DFS", "A* (Manhattan)", "A* (Euclidean)"]
        for algo in algorithms:
            rb = tk.Radiobutton(algorithm_frame, text=algo, variable=self.selected_algorithm, value=algo)
            rb.pack(side="left")

        solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        solve_button.grid(row=2, column=0, padx=10, pady=10)

    def draw_puzzle(self, state):
        self.canvas.delete("all")
        for i in range(3):
            for j in range(3):
                value = state[i*3 + j]
                if value != 0:
                    self.canvas.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill="lightgray", outline="black")
                    self.canvas.create_text(j*100 + 50, i*100 + 50, text=str(value), font=("Arial", 24))


    def solve(self):
        algorithm = self.selected_algorithm.get()
        start_time = time.time()
        end_time = 0
        solution = None
        expanded_nodes = 0
        search_depth = 0

        if algorithm == "BFS":
            search_function = bfs
            solution, expanded_nodes, search_depth = search_function(self.initial_state)
        elif algorithm == "DFS":
            search_function = dfs
            solution, expanded_nodes, search_depth = search_function(self.initial_state)
        elif algorithm == "A* (Manhattan)":
            search_function = astar_m
            solution, expanded_nodes, search_depth = search_function(self.initial_state)
        elif algorithm == "A* (Euclidean)":
            search_function = astar_e
            solution, expanded_nodes, search_depth = search_function(self.initial_state)

        end_time = time.time()

        if solution:
            time_taken = end_time - start_time
            depth = len(solution) - 1
            cost = depth  # Assuming each move has a cost of 1
            messagebox.showinfo("Solution Found",
                                    f"Solution found in {depth+1} moves with cost {cost+1}\n"
                                    f"Time taken: {time_taken:.4f} seconds\n"
                                    f"Nodes expanded: {expanded_nodes}\n"
                                    f"Search depth: {search_depth}")
            for state in solution:
                print(state)
                self.draw_puzzle(self.goal_state)
        else:
            messagebox.showinfo("No Solution", "No solution exists.")


def main():
    root = tk.Tk()
    app = EightPuzzleGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
