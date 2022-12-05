f = open("input.txt", "r")

#print(f.read().split('\n'))

count = 0
score = 0
cal_obj =[]
obj=f.read().split('\n')
for sample in obj:
    if sample == "":
        break
    sub_obj = sample.split(',')
    #print(sub_obj)
    cal_obj = []
    for i in sub_obj:
        cal_obj.append(i.split('-'))
    a0 = int(cal_obj[0][0])
    a1 = int(cal_obj[0][1])
    b0 = int(cal_obj[1][0])
    b1 = int(cal_obj[1][1])

    # a0-a1 , b0-b1
    if a0 > b1:
        continue
    if b0 > a1:
        continue
    score += 1

print(score)
