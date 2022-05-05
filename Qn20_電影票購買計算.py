# Qn20_電影票購買計算
group = int(input("輸入組數:"))
inpList = []
for n in range(group):
    inpList.append(input(f"第{n+1}組:"))

fullList = []
halfList = []
for i in range(group):
    fullList.append(int(inpList[i][0]))
    halfList.append(int(inpList[i][2]))

fee = []
for k in range(group):
    fee.append(fullList[k]*250 + halfList[k]*175)
    print(f"第{k+1}組應收費用:{fee[k]}")
