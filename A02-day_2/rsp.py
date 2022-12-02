f=open("input.txt","r");
my_list = f.read().split('\n');

score = 0;
for i in my_list:
	if (i == ""):
		continue
	if (i[2] == 'X'):
		score += 1
	if (i[2] == 'Y'):
		score += 2
	if (i[2] == 'Z'):
		score += 3
	if (i[0] == 'A' and i[2] == 'X'):
		score += 3
	if (i[0] == 'A' and i[2] == 'Y'):
		score += 6
	if (i[0] == 'A' and i[2] == 'Z'):
		score += 0
	if (i[0] == 'B' and i[2] == 'X'):
		score += 0
	if (i[0] == 'B' and i[2] == 'Y'):
		score += 3
	if (i[0] == 'B' and i[2] == 'Z'):
		score += 6
	if (i[0] == 'C' and i[2] == 'X'):
		score += 6
	if (i[0] == 'C' and i[2] == 'Y'):
		score += 0
	if (i[0] == 'C' and i[2] == 'Z'):
		score += 3

print(score);

# A X rock A - 'A' X - X' = 0 1
# B Y paper2 0
# C Z scisor3
# won 6 draw 3 lose 1
