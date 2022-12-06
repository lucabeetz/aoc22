def part1():
    with open('input.txt') as f:
        lines = f.readlines()
        break_index = 0

        # Find empty line
        for i, l in enumerate(lines):
            if l.strip() == '':
                break_index = i

        # Split lines into two lists
        crates, instructions = lines[:break_index], lines[break_index+1:]

        num_stacks = int(crates[-1][-3])
        stacks = [[] for _ in range(num_stacks)]

        for l in crates[:-1]:
            for i in range(num_stacks):
                crate_i = i * 4 + 1
                if len(l) >= crate_i and l[crate_i] != ' ':
                    stacks[i].insert(0, l[crate_i])

        for inst in instructions:
            inst = inst.strip()
            parts = inst.split(' ')

            count, fro, to = int(parts[1]), int(parts[3])-1, int(parts[5])-1

            # for i in range(count):
            #     stacks[to].append(stacks[fro].pop())

            stacks[to].extend(stacks[fro][-count:])
            del stacks[fro][-count:]

        print(''.join([s[-1] for s in stacks]))

if __name__ == '__main__':
    part1()