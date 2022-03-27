# Qn6_兩數差值
inp = input("輸入值為(ex:1,3,9,5,7) : ")
numList = []
for i in range(0,len(inp),2):
    numList.append((inp[i]))

numList.sort(reverse=True)
Max = ""
for k in range(0,len(numList)):
    Max = Max + numList[k]

numList.sort(reverse=False)
Min = ""
for u in range(0,len(numList)):
    Min = Min + numList[u]

ans = int(Max) - int(Min)
print(f"最大值數列與最小值數列差值為:{ans}")
