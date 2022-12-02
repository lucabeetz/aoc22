def main():
    cal_per_elf = []
    cur_elf_cal = 0
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                cal_per_elf.append(cur_elf_cal)
                cur_elf_cal = 0
                continue

            cur_elf_cal += int(line)

    # sum three largest nums of cal_per_elf
    cal_per_elf.sort(reverse=True)
    print(cal_per_elf[0] + cal_per_elf[1] + cal_per_elf[2])


if __name__ == '__main__':
    main()