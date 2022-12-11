class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)

    def add_size(self, size):
        self.size += size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_child(self, name):
        for child in self.children:
            if child.get_name() == name:
                return child
        return None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

with open ("input.txt", "r") as f:
    lines = f.read().splitlines()

system = Directory("/", None)
current = system

for i in lines:
    if "$ cd " in i:
        for j in i.split()[2:]:
            if j == "..":
                current = current.get_parent()
            elif j == "/":
                current = system
            else:
                if current.get_child(j) is None:
                    current.add_child(Directory(j, current))
                current = current.get_child(j)
    elif "dir" in i:
        current.add_child(Directory(i.split()[1], current))
    elif "$ ls" not in i:
        current.add_size(int(i.split()[0]))

def get_total_size(directory):
    total = directory.get_size()
    for i in directory.get_children():
        total += get_total_size(i)
    return total

def get_all_sizes(directory):
    ret = []
    for i in directory.get_children():
        if i.get_children() is not None:
            ret += get_all_sizes(i)
        ret.append(get_total_size(i))
    return ret

size = get_all_sizes(system)
size = [i for i in size if i > 30000000 - (70000000 - get_total_size(system))]
print(min(size))