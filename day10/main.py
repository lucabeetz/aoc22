def part1():
    with open('input.txt') as f:
        lines = f.readlines()

    important_cycles = [20, 60, 100, 140, 180, 220]

    state = 1
    cycles_left = 0
    n = None

    line_index = 0
    collective_sum = 0

    for i in range(1, 221):
        line = lines[line_index].strip()

        # Check if we are in an important cycle
        if i in important_cycles:
            collective_sum += state * i

        # Go to next cycle if noop operation
        if line == 'noop':
            line_index += 1
            continue

        # Add command, either wait or start waiting
        if n is None:
            n = int(line.split(' ')[1])
            cycles_left = 1
        elif cycles_left == 0:
            state += n
            n = None
            line_index += 1

        cycles_left -= 1

    print(collective_sum)

def part2():
    with open('input.txt') as f:
        lines = f.readlines()

    canvas = [['.' for _ in range(40)] for _ in range(6)]

    state = 1
    cycles_left = 0
    n = None
    line_index = 0

    for i in range(0, 240):
        line = lines[line_index].strip()

        row = i // 40
        col = i % 40

        if abs(state - col) <= 1:
            canvas[row][col] = '#'

        # Go to next cycle if noop operation
        if line == 'noop':
            line_index += 1
            continue

        # Add command, either wait or start waiting
        if n is None:
            n = int(line.split(' ')[1])
            cycles_left = 1
        elif cycles_left == 0:
            state += n
            n = None
            line_index += 1

        cycles_left -= 1

    for row in canvas:
        print(' '.join(row))

if __name__ == '__main__':
    part2()