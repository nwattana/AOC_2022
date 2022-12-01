f = open("input.txt","r");
#print(f.read().split('\n'));
my_lit = f.read().split('\n')
my_list = []
max_v = 0;
cur = 0;
for i in my_lit:
	if (i != ''):
		cur += int(i)
	else:
		my_list.append(cur)
		cur = 0
my_list.sort(reverse = True)
print(my_list[0] + my_list[1] + my_list[2])
