f = open("test2", "r")

obj = f.read().split("\n")


size = 60

"""
up - y + 1
down - y + 1
right - x + 1
lefy - x - 1

"""

mx = size // 2 - 1 
my = size // 2 - 1


snake_po = []
tmp=[]
for po in range(9):
	for i in range(2):
		tmp.append(mx)
	snake_po.append(tmp)
	tmp = []

"""
for i in range(9):
	for j in range(2):
		print(snake_po[i][j])
"""

def	get_po(x,y, xi, yi):
	if abs(mx - xi ) > 1 or abs(my - yi) > 1:
		if abs(x - xi) > 0:
			xi = xi + (x - xi)//abs(x-xi)
		else:
			xi = xi + (x - xi)
		if abs(y - yi) > 0:
			yi = yi + (y - yi)//abs(y-yi)
		else:
			yi = yi + (y - yi)
	return (xi, yi)

my_map = []
tmp = []
for i in range(size):
	for i in range(size):
		tmp.append(" ")
	my_map.append(tmp)
	tmp = []

my_map[mx][my] = "#"
# only head runing

for i in obj:
	if i == "":
		break
	print(">> ", i)
	i = i.split()

	move = 0
	for j in range(int(i[1])):
		if i[0] == 'R':
			mx += 1
		if i[0] == 'L':
			mx -= 1
		if i[0] == 'U':
			my -= 1
		if i[0] == 'D':
			my += 1

		## mx and my ad just


	for ii in range(len(snake_po)):
		if ii == 0:
			snake_po[ii] = get_po(mx,my,snake_po[ii][0], snake_po[ii][1])
		else:
			snake_po[ii] = get_po(mx,my,snake_po[ii-1][0], snake_po[ii-1][1])
		
	for iii in snake_po:
			my_map[iii[0]][iii[1]] = "#"
	for io in my_map:
		print("".join(io))


score = 0
for i in range(len(my_map)):
	for j in range(len(my_map[0])):
		if my_map[i][j] == "#":
			score += 1
for io in my_map:
	print("".join(io))
print("="*10)
print(score)
