# Qn8_檢查數值是否有重複
test = input("輸入第一行正整數為: ")
#看不懂第一行數字要幹嘛

inplist = input("輸入數列: ")
numList = []
for i in range(0,len(inplist),2):
    numList.append((inplist[i]))

maxCount = 0
mostNum = 0
for k in range(len(numList)):
    if numList.count(numList[k]) > maxCount:
        maxCount = numList.count(numList[k])
        mostNum = numList[k]

if maxCount == 1:
    print("每個數字剛好只出現 1 次")
else:
    print(f"最大出現次數的數字為:{mostNum}")
    print(f"出現次數為:{maxCount}")
