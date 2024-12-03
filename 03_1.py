import re

with open("03_data.txt") as f:
    data = f.read()

def check_correct(inp:str):
    if inp[:4] == "mul(" and re.fullmatch("[0-999]+", inp.split("(")[1].split(",")[0]):
        print("yesss!")
    
total = 0
recorded = ""
recording = False

print("mul(45,67)"[:4])

for char in data:
    # Record everything from 'm' to ')'
    recorded += char
    if char == ")":
        #Check for correct mul function
        print("Success : " + recorded)
            
    elif char == "m":
        recording = True
        recorded = "m"