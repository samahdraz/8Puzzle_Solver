import heapq
import itertools
import math

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


# Define heuristic function (Euclidean distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i * 3 + j]
            if value != 0:
                goal_pos = divmod(value, 3)
                current_pos = divmod(i * 3 + j, 3)
                distance += math.sqrt((goal_pos[0] - current_pos[0]) ** 2 + (goal_pos[1] - current_pos[1]) ** 2)
    return distance


def astar_e(initial_state):
    if initial_state == goal_state:
        return [], 0, 0  # No path, 0 explored nodes, 0 depth

    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (heuristic(initial_state), 0, initial_state, []))

    explored_nodes = 0
    max_depth = 0

    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)

        if current_state == goal_state:
            return path, explored_nodes, max_depth

        if current_state in closed_set:
            continue

        closed_set.add(current_state)

        zero_index = current_state.index(0)
        for move in moves[zero_index]:
            new_state = list(current_state)
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            h = heuristic(new_state)
            heapq.heappush(open_list, (g + h, g + 1, tuple(new_state), path + [move]))

        explored_nodes += 1
        max_depth = max(max_depth, len(path))

    return None, explored_nodes, max_depth

# # A* search algorithm
# def astar_e(initial_state):
#     if initial_state == goal_state:
#         return []
#
#     open_list = []
#     closed_set = set()
#     # heuristic value, the cost-so-far (g), the current state, and the path taken to reach that state
#     heapq.heappush(open_list, (heuristic(initial_state), 0, initial_state, []))
#
#     while open_list:
#         _, g, current_state, path = heapq.heappop(open_list)
#
#         if current_state == goal_state:
#             return path
#
#         if current_state in closed_set:
#             continue
#
#         closed_set.add(current_state)
#
#         zero_index = current_state.index(0)
#         for move in moves[zero_index]:
#             new_state = list(current_state)
#             new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
#             h = heuristic(new_state)
#             heapq.heappush(open_list, (g + h, g + 1, tuple(new_state), path + [move]))
#
#     return None
#
