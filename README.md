# GUI:
1.	GUI Interface: The GUI is built using Tkinter, a standard Python library for creating graphical user interfaces.
2.	Puzzle Representation: The 8-puzzle is represented as a 3x3 grid of tiles, with numbers 1-8 representing the tiles and 0 representing the empty space. Each puzzle configuration is stored as a tuple, facilitating efficient manipulation and comparison of states during the solving process.
3.	Algorithm Selection: Users can choose the search algorithm (BFS, DFS, A* with Manhattan distance, A* with Euclidean distance) from radio buttons.
4.	Solve Button: Clicking the "Solve" button triggers the selected search algorithm to find a solution to the puzzle.
5.	Reset Button: There's a "Reset" button to reset the puzzle board to its initial state.
6.	Message Box: Upon finding a solution, a message box displays the solution path, the time taken to solve the puzzle, and other information like search depth and cost.
7.	Console Output: The solution path is also printed to the console.

   
# DFS:    
## Stack (Custom Implementation):  
•	The Stack class is implemented using a set data structure to store unique states encountered during the search process.  
•	States are stored as tuples to ensure they are hashable and can be efficiently stored and retrieved from the set.  
•	Operations:  
•	push(item): Adds a new state to the stack.  
•	pop(): Removes and returns the top state from the stack.  
•	peek(): Returns the top state without removing it.  
•	is_empty(): Checks if the stack is empty.  
•	size(): Returns the number of states in the stack.  
## Algorithm:  
•	Goal State Definition: The goal state is defined as a tuple representing the arrangement of tiles in the desired configuration.  
•	Possible Moves: The code defines a dictionary moves that maps each tile position to the possible moves (indices) that can be made from that position.  
•	Successor State Generation: The successors function generates successor states for a given state by swapping the position of the empty tile (0) with neighboring tiles based on the possible moves defined.  
•	Depth-First Search Algorithm:
  1.	The DFS algorithm is implemented to explore states in a depth-first manner. It utilizes a stack (implemented using a set) to maintain states to be explored.  
  2.	Starting from the initial state, DFS iteratively explores states by adding their successors to the stack. It continues to explore deeper into the search tree until reaching a leaf node (a state with no unvisited successors) or encountering the goal state.  
  3.	DFS backtracks when it reaches a dead-end or fully explores a branch of the search tree. This is achieved by popping states from the stack until it finds a state with unvisited successors.  
  4.	The search terminates when the goal state is found or when the entire search space has been explored.                


# BFS:    
## Algorithm:  
•	Goal State Definition: The goal state is defined as a tuple representing the arrangement of tiles in the desired configuration.  
•	Possible Moves: The code defines a dictionary moves that maps each tile position to the possible moves (indices) that can be made from that position.  
•	Successor State Generation: The successors function generates successor states for a given state by swapping the position of the empty tile (0) with neighboring tiles based on the possible moves defined.  
•	Breadth-First Search Algorithm:   
  1.	The BFS algorithm is implemented using a queue (deque) to explore states in a breadth-first manner.  
  2.	Similar to DFS, BFS starts from the initial state and iteratively expands states by adding their successors to the queue.  
  3.	Unlike DFS, BFS explores states level by level, ensuring that all states at a given depth are explored before moving to deeper levels.  
  4.	The search terminates when the goal state is reached or when all states have been explored.   


# A* with Manhattan:     
## 1.	Objective:  
•	The A* search algorithm with Manhattan distance heuristic aims to efficiently find the shortest path from the initial state to the goal state in a given problem space.   
## 2.	Goal State and Possible Moves:  
•	The goal state is defined as a tuple representing the arrangement of elements in the solved puzzle/board.  
•	Possible moves are predefined based on the position of the empty cell (represented by '0') in the current state. These moves determine the potential successor states.  
## 3.	Heuristic Function - Manhattan Distance:  
•	The heuristic function calculates the Manhattan distance for a given state, representing the sum of the horizontal and vertical distances of each tile from its goal position.  
•	This heuristic provides an estimate of the minimum number of moves required to reach the goal state from the current state.  
## 4.	A* Search Algorithm:  
•	The algorithm utilizes a priority queue (implemented using heapq) to explore states based on their estimated total cost (heuristic value + actual cost).  
•	Each state is represented by a tuple containing the estimated total cost, actual cost (g-value), current state configuration, and the path taken to reach that state.  
•	The algorithm iteratively explores states, considering the lowest cost states first, until the goal state is found.  
•	Closed states are tracked to avoid revisiting previously explored states.  
•	Successor states are generated based on possible moves and added to the priority queue with updated costs.  
## 5.	Conclusion:  
•	The A* search algorithm with Manhattan distance heuristic efficiently navigates through the search space, prioritizing states likely to lead to the goal while considering the actual cost of reaching each state.   
•	This approach enables finding the shortest path to the goal state while minimizing the number of states explored, making it suitable for solving puzzles and pathfinding problems efficiently.   


# A * with Euclidean:     
## 1.	Objective:  
•	The A* search algorithm with Euclidean distance heuristic is designed to efficiently find the shortest path from the initial state to the goal state in a given problem space.   
## 2.	Goal State and Possible Moves:   
•	The goal state is represented as a tuple denoting the arrangement of elements in the solved puzzle or board.  
•	Possible moves are predefined based on the position of the empty cell (represented by '0') in the current state. These moves determine the potential successor states.   
## 3.	Heuristic Function - Euclidean Distance:  
•	The heuristic function calculates the Euclidean distance for a given state, representing the geometric distance between each tile and its goal position.  
•	This heuristic provides an estimate of the minimum number of moves required to reach the goal state from the current state, considering both horizontal and vertical distances.  
## 4.	A* Search Algorithm:  
•	The algorithm employs a priority queue (implemented using heapq) to explore states based on their estimated total cost (heuristic value + actual cost).    
•	Each state is represented by a tuple containing the estimated total cost, actual cost (g-value), current state configuration, and the path taken to reach that state.  
•	The algorithm iteratively explores states, prioritizing those with the lowest estimated total cost, until the goal state is found.  
•	Closed states are tracked to prevent revisiting previously explored states.  
•	Successor states are generated based on possible moves and added to the priority queue with updated costs.  
## 5.	Conclusion:  
•	The A* search algorithm with Euclidean distance heuristic efficiently traverses the search space, favoring states likely to lead to the goal while considering the geometric distance of each tile from its goal position.   
•	This approach enables finding the shortest path to the goal state while minimizing the number of states explored, making it suitable for solving puzzles and pathfinding problems effectively.  
<br>
<br>
<br>
![image](https://github.com/samahdraz/8Puzzle_with_different_algorithms/assets/100757002/d3e265a2-15ae-4369-87d1-ff4419d601dc)





