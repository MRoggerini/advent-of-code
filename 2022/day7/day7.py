with open('day7_input.txt') as f:
    data = f.read().splitlines()


class Blob:
    def __init__(self, path, dimension):
        # dimension: bytes occupied on filesystem
        # path: full path to the current file (with filename)
        self.dimension = dimension
        self.path = path
        self.depth = len(path.split('/')) - 1
        self.parent = '/'.join(path.split('/')[:-1])
        self.kind = 'blob'


class Dir(Blob):
    def __init__(self, path):
        super().__init__(path, 0)
        self.kind = 'dir'


class File(Blob):
    def __init__(self, path, dimension):
        super().__init__(path, dimension)
        self.kind = 'file'


class Root(Dir):
    # root is a special directory with no parent
    def __init__(self, path):
        super().__init__(path)
        self.root = None


def total_dir(l):
    # given a lis of blobs, return the number of dirs in the list
    tot_dir = 0
    for i in l:
        if i.kind == 'dir':
            tot_dir += 1
    return tot_dir


current_path = ['']
filesys = {}
depth_index = {}
dimension_index = {}

root = Root('/')
filesys[''] = root
depth_index[root.depth] = [root]

# read input
for i in data:
    current_out = i.split(' ')

    # read command
    if current_out[0] == '$':
        if current_out[1] == 'cd':
            if current_out[2] == '..':
                current_path.pop(-1)
            elif current_out[2] == '/':
                # set to work also for other absolute paths than '/'
                current_path = current_out[2][1:].split('/')
            else:
                current_path += current_out[2].split('/')
    # add element to file system
    else:
        elem_path = current_path+[current_out[1]]
        elem_path = '/'.join(elem_path)
        if current_out[0] == 'dir':
            curr_elem = Dir(elem_path)
        else:
            curr_elem = File(elem_path, int(current_out[0]))
        # index by path
        filesys[elem_path] = curr_elem
        # index by depth in tree
        try:
            depth_index[curr_elem.depth].append(curr_elem)
        except KeyError:
            depth_index[curr_elem.depth] = [curr_elem]

# update the dimension of parent nodes
# from lowest depth upward, we increase the dimension of the parent blob by the
# dimension of the child blob
for _, val in sorted(depth_index.items(), reverse=True):
    for j in val:
        try:
            filesys[j.parent].dimension += j.dimension
        except KeyError:
            pass
        # index each blob by its dimension
        try:
            dimension_index[j.dimension].append(j)
        except KeyError:
            dimension_index[j.dimension] = [j]

tot_space = 70_000_000
update_weight = 30_000_000
current_free = tot_space - root.dimension
space_needed = update_weight - current_free

tot_weight = 0
is_found = False

smaller_found = False
for w, val in sorted(dimension_index.items()):
    # we want to find the sum of all folders with weight less than 100.000
    if w < 100_000:
        tot_weight += total_dir(val) * w
    # we want to find the smaller element big enough to free enough space for
    # the update
    # if total_dir(val) = 0 we have no directories in the list by construction
    if w >= space_needed and total_dir(val) > 0 and not smaller_found:
        space_freed = w
        smaller_found = True

print(f'total weight of folders under 100.000:.....................{tot_weight}\n')

print(f'system memory (all):.......................................{tot_space}')
print(f'system memory (occupied):..................................{root.dimension}')
print(f'system memory (free):......................................{current_free}')
print(f'update dimension:..........................................{update_weight}')
print(f'space needed for update:...................................{space_needed}')

print(f'total weight of smaller folder that frees up enough space:.{space_freed}')
