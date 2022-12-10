# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cathode_ray.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nwattana <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/10 12:38:29 by nwattana          #+#    #+#              #
#    Updated: 2022/12/10 14:22:30 by nwattana         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

f = open("input.txt","r")
f_obj = f.read().split("\n")

"""
 creat sprit for plot
"""
def sprit_move(pos):
	buffer = ['.' for i in range (40)]
	for i in range(3):
		if i + pos < 40:
			buffer[pos+i] = "#"
	return (buffer)


"""
	monitor initialize
"""
monitor = [[' ' for i in range(40)] for j in range(6)]



"""
# sp = sprit_move(0)
# print sprit and monitor
print("="*40)
for line in monitor:
	print("".join(line))
print("="*40)
print("".join(sp))
print("="*40)
"""


"""
add x take 2 cycle -> after 2 cycle add x to data
noop  take 1 cycle

monitor wide 40
high 6

"""


data = 1
cycle = 0
clist_index = 0
plist=[]
sp = sprit_move(0)

for index, command in enumerate(f_obj):
		if command == "":
			break
		line = command.split()
		if line[0] == "noop":
			cycle += 1
			if cycle == 240:
				break
			monitor[cycle // 40][cycle % 40] = sp[cycle % 40]
			plist.append(data)
		else:
			for i in range(2):
				cycle += 1
				if cycle == 240:
					break
				monitor[cycle // 40][cycle % 40] = sp[cycle % 40]
				plist.append(data)
			data += int(line[1])
		sp = sprit_move(data)


"""
	Put monitor
"""
print("="*40)
for line in monitor:
	print("".join(line))
print("="*40)
print("".join(sp))
print("="*40)

