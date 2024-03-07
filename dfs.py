class Stack:
    def __init__(self):
        self.stack_set = set()

    def push(self, item):
        if isinstance(item, tuple):  # Ensure the item is hashable
            self.stack_set.add(item)
        else:
            raise ValueError("Item must be hashable")

    def pop(self):
        if self.is_empty():
            return None
        else:
            item = self.peek()
            self.stack_set.remove(item)
            return item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return next(iter(self.stack_set))

    def is_empty(self):
        return len(self.stack_set) == 0

    def size(self):
        return len(self.stack_set)


# a tuple
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
# 0 1 2
# 3 4 5
# 6 7 8


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


def count_inversions(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversions += 1
    return inversions


def dfs(initial_state):
    inversions = count_inversions(initial_state)
    if inversions % 2 != 0:
        return None, 0, 0  # Unsolvable initial state
    stack = Stack()
    stack.push((initial_state, 0))  # Include depth along with the state
    visited = set()
    path = {initial_state: [initial_state]}

    explored_nodes = 0
    max_depth = 0

    while not stack.is_empty():
        current_state, depth = stack.pop()

        if current_state == goal_state:
            return path[current_state], explored_nodes, max_depth

        if current_state in visited:
            continue

        visited.add(current_state)
        explored_nodes += 1
        max_depth = max(max_depth, depth)

        for successor_state in successors(current_state):
            if successor_state not in visited:
                stack.push((successor_state, depth + 1))
                path[successor_state] = path[current_state] + [successor_state]

    return None, explored_nodes, max_depth


# def dfs(initial_state):
#     stack = Stack()
#     stack.push(initial_state)
#     visited = set()
#     path = {initial_state: [initial_state]}
#
#     while not stack.is_empty():
#         current_state = stack.pop()
#         if current_state == goal_state:
#             return path[current_state]
#
#         visited.add(current_state)
#
#         for successor_state in successors(current_state):
#             if successor_state not in visited:
#                 stack.push(successor_state)
#                 path[successor_state] = path[current_state] + [successor_state]
#
#     return None

