with open("01_data.txt") as f:
    data = f.readlines()
    
list1 = []
list2 = []

for line in data:
    numstr = ""
    numstr2 = ""
    onl2 = False
    for char in line:
        if char != " " and onl2 == False:
            numstr += char
        elif char != " " and onl2:
            numstr2 += char
        else:
            onl2 = True
    list1.append(int(numstr))
    list2.append(int(numstr2))

#print(list1, list2)

total = 0

for i in range(len(list1)):
    nownum = list1[i]
    counter = 0
    for elm in list2:
        if elm == list1[i]:
            counter += 1
    total = total + (counter * list1[i])

print(total)