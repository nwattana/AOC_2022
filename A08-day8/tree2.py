f=open("input.txt", "r")

obj = f.read().split()
height = len(obj)
width = len(obj[0])
"""
for i,ch in enumerate(obj):
    for j,cha in enumerate(ch):
        print("  ",i,j,cha)
"""

def check_visible_right(old, x,y,hi,wd):
    sume = 1
    if old <= obj[x][y]:
        return 1
    if x < wd:
        sume = 1 + check_visible_right(old,x + 1, y,hi, wd)
    return sume

def check_visible_left(old, x,y,hi,wd):
    sume = 1
    if old <= obj[x][y]:
        return 1
    if x > 0:
        sume = 1 + check_visible_left(old,x - 1, y,hi, wd)
    return sume

def check_visible_top(old, x,y,hi,wd):
    sume = 1
    if old <= obj[x][y]:
        return 1
    if y > 0:
        sume = 1 + check_visible_top(old, x,y-1,hi,wd)
    return sume

def check_visible_bot(old, x,y,hi,wd):
    sume = 1
    if old <= obj[x][y]:
        return 1
    if y < hi:
        sume = 1 + check_visible_bot(old, x,y+1,hi,wd)
    return sume



def check_visible(obj, i ,j, hi=98, wd=98):
    if i == 0 or i == 98 or j == 0 or j == 98:
        return 0
    right = check_visible_right(obj,i+1,j,hi,wd)
    left =  check_visible_left(obj,i-1,j,hi,wd)
    top = check_visible_top(obj,i,j-1,hi,wd)
    bot = check_visible_bot(obj,i,j+1,hi,wd)
    return right * top * left * bot
sumt=[]

for i,ch in enumerate(obj):
    for j,cha in enumerate(obj):
        sumt.append(check_visible(obj[i][j],i,j))
        print("i = {} j = {} val={}".format(i, j, check_visible(obj[i][j],i,j)))

print(max(sumt))
