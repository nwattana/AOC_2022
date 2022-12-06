f=open("input.txt", "r")
obj =f.read().split().pop()

list_a = []
for i in range(len(obj)):
    list_a.append(obj[i])
    if len(list_a) > 14:
        list_a = list_a[1:15]
    if len(list_a) > 13 :
        if len(set(list_a)) == 14:
            break;

print(len(obj))
print("this is an anwser i = " + str(i + 1))

