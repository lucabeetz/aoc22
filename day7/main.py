def part1():
    structure = {'/': {'files': []}}
    dir_stack = []
    active_dir = None

    # Build directory structure
    with open('input.txt') as f:
        cur_files = []
        cur_dirs = []

        for line in f:
            line = line.strip()
            parts = line.split(' ')

            # Handle commands
            if parts[0] == '$':
                if cur_files or cur_dirs:
                    active_dir['files'] = cur_files

                    for dir in cur_dirs:
                        active_dir[dir] = {}

                    cur_files = []
                    cur_dirs = []

                if parts[1] == 'cd':
                    if parts[2] == '..':
                        dir_stack.pop()
                    else:
                        dir_stack.append(parts[2])

                    active_dir = nested_get(structure, dir_stack)

                continue

            # Handle files
            if parts[0] == 'dir':
                active_dir[parts[1]] = {'files': []}
            else:
                active_dir['files'].append((parts[0], parts[1]))

    total_size = 0

    def calc_size(dir):
        size = 0
        for file in dir['files']:
            size += int(file[0])

        for subdir in dir:
            if subdir != 'files':
                size += calc_size(dir[subdir])

        if size < 100_000:
            nonlocal total_size
            total_size += size

        dir['size'] = size
        return size

    active_dir = structure['/']
    calc_size(active_dir)

    # Part 2
    total_size = 70_000_000
    required_size = 30_000_000
    empty_space = total_size - structure['/']['size']

    min_dir_size = required_size - empty_space

    legit_dirs = []

    def find_dirs(dir, min_size):
        for subdir in dir:
            if subdir != 'files' and subdir != 'size' and dir[subdir]['size'] >= min_size:
                nonlocal legit_dirs
                legit_dirs.append((subdir, dir[subdir]['size']))
                find_dirs(dir[subdir], min_size)

    find_dirs(active_dir, min_dir_size)

    # sort legit_dirs by size
    legit_dirs.sort(key=lambda x: x[1], reverse=True)
    print(legit_dirs[-1])



def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


if __name__ == '__main__':
    part1()