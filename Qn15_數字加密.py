# Qn15_數字加密
inp = input("輸入一組四位數字為:")
numlist = []
for i in range(4):
    numlist.append((int(inp[i])+7)*0.1)

newlist = [0,0,0,0]
newlist[0] = numlist[2]
newlist[1] = numlist[3]
newlist[2] = numlist[0]
newlist[3] = numlist[1]

print("輸出加密後的數字為:",end="")
for k in range(4):
    if newlist[k] >= 1:
        newlist[k] = newlist[k] - 1
    newlist[k] = int(newlist[k] * 10)
    print(newlist[k],end="")
