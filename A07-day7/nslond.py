class dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.child = []
    
    def append_child(self, cname):
        self.child.append(cname)

    def increass_size(self, ssize):
        self.size += ssize

    def print_ch(self):
        for i in self.child:
            print(i.name)
        print("total size = " + str(self.size))
        print("Name = "+ self.name)
        print("Parent = "+ str(self.parent))

    def get_child(self, cname):
        for child in self.child:
            if child == cname:
                return child
        return None

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name




f = open("input.txt", "r")
comm_obj = f.read().split("\n")

g = 7
cur_dir = dir("/", None)
pre_dir = cur_dir

for i in comm_obj:
    if i == "":
        break
    tmp = i.split()
    if tmp[0] == '$':
        if tmp[1] == "cd":
            if tmp[2] == "..":
                print("back to parent")
            elif tmp[2] == "/":
                print("back to head")
            else:
                print("to child")
    if tmp[0].isnumeric():
        cur_dir.size += int(tmp[0])
    if g == 0:
        break
    g -= 1
cur_dir.print_ch()
