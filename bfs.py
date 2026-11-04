
from collections import deque

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def find_blank(state):
    return state.index(0)


def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


def get_neighbors(state):
    neighbors = []
    blank = find_blank(state)
    row, col = divmod(blank, 3)

    moves = {
        "Up": (row - 1, col),
        "Down": (row + 1, col),
        "Left": (row, col - 1),
        "Right": (row, col + 1)
    }

    for move_name, (new_row, new_col) in moves.items():
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            state_list = list(state)

            state_list[blank], state_list[new_blank] = (
                state_list[new_blank],
                state_list[blank]
            )

            neighbors.append((tuple(state_list), move_name))

    return neighbors


def bfs(start_state, goal_state=GOAL_STATE):
    if start_state == goal_state:
        return [(start_state, "Start")]

    visited = {start_state}
    queue = deque([(start_state, [(start_state, "Start")])])

    while queue:
        current_state, path = queue.popleft()

        for next_state, move in get_neighbors(current_state):
            if next_state in visited:
                continue

            new_path = path + [(next_state, move)]

            if next_state == goal_state:
                return new_path

            visited.add(next_state)
            queue.append((next_state, new_path))

    return None


def print_state(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join(str(t) if t != 0 else "_" for t in row))
    print()


def print_solution(path):
    print(f"Solved in {len(path) - 1} moves!\n")

    for step, (state, move) in enumerate(path):
        print(f"Step {step}: {move}")
        print_state(state)


def main():
    start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)

    print("Start state:")
    print_state(start_state)

    if not is_solvable(start_state):
        print("This puzzle configuration is NOT solvable.")
        return

    solution_path = bfs(start_state, GOAL_STATE)

    if solution_path:
        print_solution(solution_path)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
