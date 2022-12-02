f=open("input.txt","r");
my_list = f.read().split('\n');

score = 0;
for i in my_list:
	if (i == ""):
		continue
	if (i[2] == 'X'):
		score += 0
	if (i[2] == 'Y'):
		score += 3
	if (i[2] == 'Z'):
		score += 6
	if (i[0] == 'A' and i[2] == 'X'):
		score += 3
	if (i[0] == 'A' and i[2] == 'Y'):
		score += 1
	if (i[0] == 'A' and i[2] == 'Z'):
		score += 2
	if (i[0] == 'B' and i[2] == 'X'):
		score += 1
	if (i[0] == 'B' and i[2] == 'Y'):
		score += 2
	if (i[0] == 'B' and i[2] == 'Z'):
		score += 3
	if (i[0] == 'C' and i[2] == 'X'):
		score += 2
	if (i[0] == 'C' and i[2] == 'Y'):
		score += 3
	if (i[0] == 'C' and i[2] == 'Z'):
		score += 1

print(score);

# A X rock 		1
# B Y paper  	2
# C Z scisor	3
# X need lose
# Y need draw
# Z need win
# won 6 draw 3 lose 1
