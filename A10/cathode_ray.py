# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cathode_ray.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nwattana <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/10 12:38:29 by nwattana          #+#    #+#              #
#    Updated: 2022/12/10 13:19:20 by nwattana         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

f = open("input.txt","r")
f_obj = f.read().split("\n")


"""
add x take 2 cycle -> after 2 cycle add x to data
noop  take 1 cycle

"""

data = 1
cycle = 0
power = 0
regis = 0

clist_index = 0
clist=[20, 60, 100, 140, 180, 220]
plist=[]

for index, command in enumerate(f_obj):
		if command == "":
			break
		print(index, command)
		line = command.split()
		
		if line[0] == "noop":
			cycle += 1
			plist.append(data)
		else:
			for i in range(2):
				cycle += 1
				plist.append(data)
			data += int(line[1])

plist.append(data)
print("total" ,plist[19]*20 + plist[59]*60 + plist[99]*100 + plist[139]*140 + plist[179]*180 + plist[219] * 220)
