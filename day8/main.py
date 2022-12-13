def part1():
    grid = []
    bool_grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append(list(map(int, list(line.strip()))))
            bool_grid.append([False] * len(line.strip()))

    vis_trees = 0

    # Left to right
    for i in range(len(grid)):
        highest = -1
        for j in range(len(grid[0])):
            if grid[i][j] > highest and not bool_grid[i][j]:
                vis_trees += 1
                bool_grid[i][j] = True
            highest = max(highest, grid[i][j])

    # Right to left
    for i in range(len(grid)):
        highest = -1
        for j in range(len(grid[0])-1, 0, -1):
            if grid[i][j] > highest and not bool_grid[i][j]:
                vis_trees += 1
                bool_grid[i][j] = True
            highest = max(highest, grid[i][j])

    # Top down
    for i in range(len(grid)):
        highest = -1
        for j in range(len(grid[0])):
            if grid[j][i] > highest and not bool_grid[j][i]:
                vis_trees += 1
                bool_grid[j][i] = True
            highest = max(highest, grid[j][i])

    # Bottom up
    for i in range(len(grid)):
        highest = -1
        for j in range(len(grid[0])-1, 0, -1):
            if grid[j][i] > highest and not bool_grid[j][i]:
                vis_trees += 1
                bool_grid[j][i] = True
            highest = max(highest, grid[j][i])

    print(vis_trees)

def part2():
    grid = []
    with open('input.txt') as f:
        for line in f:
            grid.append(list(map(int, list(line.strip()))))

    highest_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Look right
            s_right = 0
            for x_r in range(j+1, len(grid)):
                s_right += 1
                if grid[i][x_r] >= grid[i][j]:
                    break

            # Look left
            s_left = 0
            for x_r in range(j-1, -1, -1):
                s_left += 1
                if grid[i][x_r] >= grid[i][j]:
                    break

            # Look up
            s_up = 0
            for x_r in range(i-1, -1, -1):
                s_up += 1
                if grid[x_r][j] >= grid[i][j]:
                    break

            # Look down
            s_down = 0
            for x_r in range(i+1, len(grid)):
                s_down += 1
                if grid[x_r][j] >= grid[i][j]:
                    break

            score = s_right * s_left * s_up * s_down
            highest_score = max(highest_score, score)

    print(highest_score)


if __name__ == '__main__':
    part2()