from collections import deque

# Define the goal state
goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

# Define possible moves
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# Function to find the index of '0' in the state
def find_zero(state):
    return state.index(0)


# Function to generate successor states
def successors(state):
    zero_index = find_zero(state)
    for move in moves[zero_index]:
        new_state = list(state)
        new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
        yield tuple(new_state)


def bfs(initial_state):
    if initial_state == goal_state:
        return [], 0, 0  # Return empty path, explored nodes, and search depth of 0

    visited = set()
    queue = deque([(initial_state, [], 0)])  # Initialize depth to 0

    explored_nodes = 0
    max_depth = 0

    while queue:
        current_state, path, depth = queue.popleft()  # Extract depth from the queue

        if current_state == goal_state:
            return path, explored_nodes, depth

        if current_state in visited:
            continue

        visited.add(current_state)
        explored_nodes += 1
        max_depth = max(max_depth, depth)

        for successor_state in successors(current_state):
            queue.append((successor_state, path + [successor_state], depth + 1))  # Increment depth

    return None, explored_nodes, max_depth  # If no solution found, return None for path

