f=open("input.txt", "r")

obj = f.read().split()
height = len(obj)
width = len(obj[0])
print(height, width)
"""
for i,ch in enumerate(obj):
    for j,cha in enumerate(ch):
        print("  ",i,j,cha)
"""

def check_visible_right(old, x,y,hi,wd):
    if old >= obj[x][y]:
        return 0
    if x < wd:
        if check_visible_right(old,x + 1, y,hi, wd) == 0:
            return (0)
    return 1

def check_visible_left(old, x,y,hi,wd):
    if old <= obj[x][y]:
        return 0
    if x > 0:
        if check_visible_left(old,x - 1, y,hi, wd) == 0:
            return (0)
    return 1

def check_visible_top(old, x,y,hi,wd):
    if old <= obj[x][y]:
        return 0
    if y > 0:
        if check_visible_top(old, x,y-1,hi,wd) == 0:
            return 0
    return 1

def check_visible_bot(old, x,y,hi,wd):
    if old <= obj[x][y]:
        return 0
    if y < hi:
        if check_visible_bot(old, x,y+1,hi,wd) == 0:
            return 0
    return 1



def check_visible(obj, i ,j, hi=98, wd=98):
    if i == 0 or i == 98 or j == 0 or j == 98:
        return 0
    right = check_visible_right(obj,i+1,j,hi,wd):
    left =  check_visible_left(obj,i-1,j,hi,wd):
    top = check_visible_top(obj,i,j-1,hi,wd):
    bot = check_visible_bot(obj,i,j+1,hi,wd):
    return 0
sumt=0

for i,ch in enumerate(obj):
    for j,cha in enumerate(obj):
        sumt += check_visible(obj[i][j],i,j);

print(sumt)







