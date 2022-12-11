
f = open("input.txt","r")

class Monkey:
    def __init__(self, name=0, test=1, taim=0, faim=0,oper="", item=[]):
        self.name = name
        self.item = item
        self.taim = taim
        self.faim = faim
        self.test = test
        self.oper = oper
        self.throw = []
        self.ins = 0

    def consider(self,func):
        for i,item in enumerate(self.item):
            self.item[i] = func(item)

    def recieve_item(self, item):
        self.item.append(item)

    def throw_item(self, index):
        return (self.item.pop(index))
    
    def print_item(self):
        print(self.item)

    def get_item(self, item):
        self.item.append(item)

    def cal_worry(self):
        new_item = []
        for index, item in enumerate(self.item):
            self.ins += 1
            a = int(item)
            if self.oper[2] == "old":
                b = a
            else:
                b = int(self.oper[2])
            if self.oper[1] == "+":
                res = (a + b) % 9699690
                new_item.append(res)
            else:
                res = (a * b) % 9699690
                new_item.append(res)
        self.item = new_item

# list thorw list 
    def list_throw(self):
        self.throw = []
        for i in self.item:
            if i % int(self.test) > 0:
                self.throw.append(self.faim)
            else:
                self.throw.append(self.taim)

    def get_throw(self):
        return self.throw

    def get_ins(self):
        return (self.ins)

    def __str__(self):
        sam = ""
        for i in self.item:
            sam += str(i) + " "
        sam2 = ""
        for i in self.oper:
            sam2 += i + ","
        sam3 = ""
        for i in self.throw:
            sam3 += i + " "
        str_a = "name:\t\t" + str(self.name) + "\nTrue aim:\t" + str(self.taim)
        str_b = "\nFalse aim:\t" + str(self.faim) + "\nitem list\t"
        str_c = sam + "\n" + sam2 + "\ndivisible by \t" + str(self.test)
        str_d = "\n" + sam3
        end = "\n" + "="*40 + "\n"
        return end + str_a + str_b + str_c + str_d +end


fobj=f.read().split("\n")

mklist = []
save = []
for tmp in fobj:
    if tmp == "":
        mklist.append(Monkey(name,save[2],save[3],save[4],save[1],save[0]))
        save = []
        continue
    if "Monkey" in tmp:
        ii = tmp.split()
        name = ii[1][0]
    if "items" in tmp:
        hold = []
        nums = tmp.replace(',','').split()[2:]
        for icu in nums:
            hold.append(int(icu))
        save.append(hold)
    if "Oper" in tmp:
        iii = tmp[19:].split()
        save.append(iii)
    if "divisible" in tmp:
        save.append(int(tmp.split()[-1]))
    if "true" in tmp:
        save.append(tmp.split()[-1])
    if "false" in tmp:
        save.append(tmp.split()[-1])

print("Before loop")
for i in mklist:
    i.print_item()

round1=1
for iq in range(10000):
    for i, mk in enumerate(mklist):
        tmp = []
        mk.cal_worry()
        mk.list_throw()
        tmp = mk.get_throw()
        for tlist in tmp:
            mklist[int(tlist)].get_item(mk.throw_item(0))
    print(iq)
t1=[]
for i in mklist:
    t1.append(int(i.get_ins()))
t1.sort()
print(t1[-1] * t1[-2])
