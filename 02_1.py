with open("02_data.txt") as f:
  data = f.readlines()

total = 0

for line in data:
  desc = False
  nums = []
  tmpStr = ""
  safe = True
  for char in line:
    if char == " ":
      nums.append(int(tmpStr))
      tmpStr = ""
    else:
      tmpStr = tmpStr + char
  nums.append(int(tmpStr))
  print(1 <= abs(9 - 7) <= 3)
  #Check Numbers
  print("===== New List ===== " + str(nums))
  for i in range(len(nums)):
    if i == 0:
      if nums[0] > nums[1]:
        desc = True
    elif i+1 == len(nums):
      break
    if not (1 <= abs(nums[i] - nums[i+1]) <= 3):
      safe = False
      break
    elif desc == False and nums[i] > nums[i+1]:
      safe = False
      break
    elif desc == True and nums[i] < nums[i+1]:
      safe = False
      break
  
  if safe:
    total += 1

print(total)
  