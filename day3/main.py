def part1():
    score = 0
    with open('input.txt') as f:
        for line in f:
            # split line in middle
            line = line.strip()
            a, b = line[:len(line)//2], line[len(line)//2:]
            a, b = set(a), set(b)

            l = (a & b).pop()

            if l.islower():
                score += ord(l) - ord('a') + 1
            else:
                score += ord(l) - ord('A') + 27

    print(score)

def part2():
    score = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for a, b, c in zip(lines[::3], lines[1::3], lines[2::3]):
            badge = set(a.strip()) & set(b.strip()) & set(c.strip())
            badge = badge.pop()

            if badge.islower():
                score += ord(badge) - ord('a') + 1
            else:
                score += ord(badge) - ord('A') + 27
    print(score)


if __name__ == '__main__':
    # part1()
    part2()