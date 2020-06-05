
def read_puzzle_file():
    with open("puzzles") as file:
        content = file.read().splitlines()
        return content

def convert_puzzle(string):
    puzzle = []
    for i in range(9):
        row = string[i*9 : i*9+9]
        row = list(row)
        row = list(map(int, row))
        puzzle.append(row)
    return puzzle

def print_puzzle(puzzle):
    output = "-" * 21 + "\n"
    for row in puzzle:
        output += "| "
        for n in row:
            if n == 0:
                output += " "
            else:
                output += str(n)
            output += " "
        output += "|\n"
    output += "-" * 21
    print(output)

def check_pos(puzzle, x, y, n):
    row = puzzle[y]
    column = [row[x] for row in puzzle]

    i = (x // 3) * 3
    j = (y // 3) * 3
    section = [n for row in puzzle[j : j+3] for n in row[i : i+3]]
    
    return not n in row and not n in column and not n in section


def solve(puzzle):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            number = puzzle[y][x]
            if number == 0:
                for n in range(1, 10):
                    # If the number fits
                    # If the heuristic looks true
                    if check_pos(puzzle, x, y, n):
                        puzzle[y][x] = n
                        print_puzzle(puzzle)
                        solve(puzzle)
                        # Forget the heuristic
                        puzzle[y][x] = 0

                # Dead-end. Start backtracking
                return None
    return


# heuristics
# backtracking


puzzles = read_puzzle_file()
puzzle = convert_puzzle(puzzles[18])

print_puzzle(puzzle)
solve(puzzle)

