import re

with open("03_data.txt") as f:
    data = f.read()

def check_correct(inp:str):
    try:
        num1 = inp.split(",")[0].split("(")[1]
        num2 = inp.split(",")[1].split(")")[0]
    except:
        return False
    print(num1, num2)
    try:
        if int(num1) > 999 or int(num2) > 999:
            return False
    except:
        return False
    if inp[:4] == "mul(" and re.fullmatch("[0-999]+", num1) and re.fullmatch("[0-999]+", num2):
        return num1, num2
    else:
        return False
    
total = 0
recorded = ""
recording = False

print(re.fullmatch("[0-999]+", " 17 "))

for char in data:
    # Record everything from 'm' to ')'
    recorded += char
    if char == ")":
        #Check for correct mul function
        print("Success : " + recorded)
        res = check_correct(recorded)
        if res != False:
            total += int(res[0]) * int(res[1])
            print("Success, total at " + str(total))
        recorded = ""
    elif char == "m":
        recording = True
        recorded = "m"

print(re.fullmatch("[0-999]+", "17878"))