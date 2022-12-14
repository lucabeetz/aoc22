def part1():
    head_pos = (0, 0)
    tail_pos = (0, 0)
    tail_positions = [tail_pos]

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        direction, distance = line.split(' ')

        for _ in range(int(distance)):
            # Move head
            if direction == 'R':
                head_pos = (head_pos[0] + 1, head_pos[1])
            elif direction == 'L':
                head_pos = (head_pos[0] - 1, head_pos[1])
            elif direction == 'U':
                head_pos = (head_pos[0], head_pos[1] + 1)
            elif direction == 'D':
                head_pos = (head_pos[0], head_pos[1] - 1)

            # Calculate distance between head and tail
            dist_x = head_pos[0] - tail_pos[0]
            dist_y = head_pos[1] - tail_pos[1]

            # Check if we need to move tail
            if abs(dist_x) > 1 or abs(dist_y) > 1:
                # Check if we have to move diagonally
                if abs(dist_x) >= 1 and abs(dist_y) >= 1:
                    # Move diagonally
                    dx = dist_x // abs(dist_x)
                    dy = dist_y // abs(dist_y)

                    tail_pos = (tail_pos[0] + dx, tail_pos[1] + dy)
                else:
                    # Move straight
                    if direction == 'R':
                        tail_pos = (tail_pos[0] + 1, tail_pos[1])
                    elif direction == 'L':
                        tail_pos = (tail_pos[0] - 1, tail_pos[1])
                    elif direction == 'U':
                        tail_pos = (tail_pos[0], tail_pos[1] + 1)
                    elif direction == 'D':
                        tail_pos = (tail_pos[0], tail_pos[1] - 1)

                tail_positions.append(tail_pos)

    print(len(set(tail_positions)))

def part2():
    chain_links = [(0, 0)] * 10
    tail_positions = [chain_links[-1]]

    with open('input.txt') as f:
        lines = f.readlines()

    # Iterate directions
    for line in lines:
        direction, distance = line.split(' ')

        for _ in range(int(distance)):
            head = chain_links[0]

            # Move head
            if direction == 'R':
                chain_links[0] = (head[0] + 1, head[1])
            elif direction == 'L':
                chain_links[0] = (head[0] - 1, head[1])
            elif direction == 'U':
                chain_links[0] = (head[0], head[1] + 1)
            elif direction == 'D':
                chain_links[0] = (head[0], head[1] - 1)

            # Update position of each link
            for i in range(1, len(chain_links)):
                link = chain_links[i]
                head = chain_links[i-1]

                dist_x = head[0] - link[0]
                dist_y = head[1] - link[1]

                # Check if we need to move link
                if abs(dist_x) > 1 or abs(dist_y) > 1:
                    # Calculate movement
                    dx = dist_x // abs(dist_x) if dist_x != 0 else 0
                    dy = dist_y // abs(dist_y) if dist_y != 0 else 0

                    # Update position
                    chain_links[i] = (link[0] + dx, link[1] + dy)

            tail_positions.append(chain_links[-1])            

    print(len(set(tail_positions)))

if __name__ == '__main__':
    part2()