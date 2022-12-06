def part1():
    with open('input.txt') as f:
        line = f.readline()

        d = {}
        count = 0
        for i, c in enumerate(line):
            if c in d and d[c] >= i - count:
                count = i - d[c]

            if count >= 14:
                print(i+1)
                break

            d[c] = i
            count += 1

if __name__ == '__main__':
    part1()
