score_per_shape = {'A': 1, 'B': 2, 'C': 3}
translation = {'X': 'A', 'Y': 'B', 'Z': 'C'}

score_per_round = {
    ('A', 'B'): 6,
    ('A', 'C'): 0,
    ('B', 'A'): 0,
    ('B', 'C'): 6,
    ('C', 'A'): 6,
    ('C', 'B'): 0,
}

strat = {
    ('A', 'X'): 'C',
    ('A', 'Z'): 'B',
    ('B', 'X'): 'A',
    ('B', 'Z'): 'C',
    ('C', 'X'): 'B',
    ('C', 'Z'): 'A',
}



def part1():
    score = 0
    # read input.txt
    with open('input.txt') as f:
        for line in f:
            f, s = line.split()
            s = translation[s]

            score += score_per_shape[s]

            # Check for draw
            if f == s:
                score += 3
                continue

            score += score_per_round[(f, s)]

    print(score)

def part2():
    score = 0

    with open('input.txt') as f:
        for line in f:
            f, s, = line.split()

            # Score for winning
            d = {'X': 0, 'Y': 3, 'Z': 6}
            score += d[s]

            # Score for shape
            if s == 'Y':
                shape = f
            else:
                shape = strat[(f, s)]

            score += score_per_shape[shape]


    print(score)


if __name__ == '__main__':
    part2()