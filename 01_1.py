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
            

list1.sort()
list2.sort()

#print(list1, list2)

total = 0

for i in range(len(list1)):
    total = total + abs(list1[i] - list2[i])

print(total)