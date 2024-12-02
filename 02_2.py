with open("02_data.txt") as f:
  data = f.readlines()


def is_safe(the_lst : list, tolerance : bool):
  lst = the_lst.copy()
  breakInd = 0
  desc = False
  safe = True
  for i in range(len(lst)):
    if i == 0:
      if lst[0] > lst[1]:
        desc = True
    elif i+1 == len(lst):
      breakInd = i
      break
    if not (1 <= abs(lst[i] - lst[i+1]) <= 3):
      safe = False
      breakInd = i
      break
    elif desc == False and lst[i] > lst[i+1]:
      safe = False
      breakInd = i
      break
    elif desc == True and lst[i] < lst[i+1]:
      safe = False
      breakInd = i
      break
  
  if safe:
    return True
  else:
    if tolerance:
      secLst = lst.copy()
      lst.pop(breakInd)
      secLst.pop(-1)
      return is_safe(lst, False) or is_safe(secLst, False)
    else:
      return False

total = 0

for line in data:
  nums = []
  tmpStr = ""
  for char in line:
    if char == " ":
      nums.append(int(tmpStr))
      tmpStr = ""
    else:
      tmpStr = tmpStr + char
  nums.append(int(tmpStr))
  #Check Numbers
  print("===== New List ===== " + str(nums))
  if is_safe(nums, True):
    total += 1
    print("True")
  else:
    print("False")
  

print(total)
  