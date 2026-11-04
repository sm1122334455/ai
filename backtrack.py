
N = 8  
def is_safe(board, row, col):
    for r, c in enumerate(board):
        if c == col:                        # same column
            return False
        if abs(c - col) == abs(r - row):    # same diagonal
            return False
    return True


def backtracking_search(board=(), find_all=False):
    row = len(board)
    if row == N:                            # all queens placed -> solution
        return [board]

    solutions = []
    for col in range(N):
        if is_safe(board, row, col):
           
            result = backtracking_search(board + (col,), find_all)
            if result:
                if not find_all:
                    return result
                solutions.extend(result)
    return solutions                        # empty list -> dead end


def print_board(board):
    for col in board:
        print(" ".join("Q" if c == col else "." for c in range(N)))
    print()


def print_solution(board):
    print("Solution found!\n")
    for row, col in enumerate(board):
        print(f"Row {row}: queen at column {col}")
    print()
    print_board(board)


def main():
    print(f"Solving the {N}-Queens problem using Backtracking Search\n")
    solutions = backtracking_search()
    if solutions:
        print_solution(solutions[0])
    else:
        print("No solution found.")
        return
    all_solutions = backtracking_search(find_all=True)
    print(f"Total number of solutions: {len(all_solutions)}")

if __name__ == "__main__":
    main()