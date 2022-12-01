f = open("input.txt","r");
#print(f.read().split('\n'));
my_lit = f.read().split('\n')
max_v = 0;
cur = 0;
for i in my_lit:
	if (i != ''):
		cur += int(i)
	else:
		if (cur > max_v):
			max_v = cur
		cur = 0
print(max_v)
