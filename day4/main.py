def part1():
    counter = 0
    with open('input.txt') as f:
        for line in f:
            a, b = line.strip().split(',')
            (a1, a2), (b1, b2) = a.split('-'), b.split('-')

            a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)

            set_a = set(range(a1, a2+1))
            set_b = set(range(b1, b2+1))

            if set_a & set_b:
                counter += 1

    print(counter)

if __name__ == '__main__':
    part1()