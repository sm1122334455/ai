
import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


def heuristic(state):
    distance = 0

    for value in range(1, 9):
        current_index = state.index(value)
        goal_index = goal.index(value)

        current_row, current_col = divmod(current_index, 3)
        goal_row, goal_col = divmod(goal_index, 3)

        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def neighbours(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    results = []

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            state_list = list(state)

            state_list[blank], state_list[new_blank] = state_list[new_blank], state_list[blank]

            results.append(tuple(state_list))

    return results


def print_state(state, g, h, f):
    print("-" * 32)
    print("Current State")
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print(f"g = {g}")
    print(f"h = {h}")
    print(f"f = {f}")


def a_star(start, goal):
    open_list = []

    heapq.heappush(
        open_list,
        (heuristic(start), 0, start, [start])
    )

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        print_state(current, g, heuristic(current), f)

        if current == goal:
            print("\nGoal Found!")
            print("Total Moves =", g)
            print("\nSolution path:")

            for step in path:
                print(step[0:3])
                print(step[3:6])
                print(step[6:9])
                print()

            return path

        if current in visited:
            continue

        visited.add(current)

        for nxt in neighbours(current):
            if nxt not in visited:
                new_g = g + 1
                new_h = heuristic(nxt)
                new_f = new_g + new_h

                heapq.heappush(
                    open_list,
                    (new_f, new_g, nxt, path + [nxt])
                )

    print("No solution found.")
    return None


if __name__ == "__main__":
    a_star(start, goal)
