def reverse(s):
    if len(s) == 0:
            return s
    else:
        return reverse(s[1:]) + s[0]

f=open("input.txt","r")

m_obj = f.read().split('\n')

stack0=""
stack1=""
stack2=""
stack3=""
stack4=""
stack5=""
stack6=""
stack7=""
stack8=""
stack9=""

for fi in m_obj:
    print(fi)
    if fi[1] == '1':
        break
    stack0 += fi[1]
    stack1 += fi[5]
    stack2 += fi[9]
    stack3 += fi[13]
    stack4 += fi[17]
    stack5 += fi[21]
    stack6 += fi[25]
    stack7 += fi[29]
    stack8 += fi[33]

my_st=[stack0, stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8]
for i in range(0,9):
    my_st[i] = list(reverse(my_st[i].split().pop()))

for i in my_st:
    print(i)
print("="*10 + "\n")
pop_val = []

"""  
for i in range(2):
    pop_val.append(my_st[0].pop())
for i in pop_val:
    my_st[2].append(i)
"""

f2 = open("slic.txt", "r")
c = 0
command_list = f2.read().split("\n")
for i in command_list:
    if (i==""):
        break
    tmp = i.split(" ")
    #print(tmp)
    size = int(tmp[1])
    src = int(tmp[3])
    dst = int(tmp[5])
    for i in range(size):
        pop_val.insert(0,my_st[src  - 1].pop())
    for i in pop_val:
        my_st[dst - 1].append(i)
    pop_val = []

stre=""
for i in my_st:
    stre += str(i[-1])
print(stre)
print("="*10 + "\n")

