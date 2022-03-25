# Hw_Qn1_找出數字字串中最大質數
#取字串 (輸入)
num = input("請輸入正整數")
All_num = []
for p in range(len(num),0,-1):
    for u in range(p):
        All_num.append(int(num[u:p]))
# (處理)
all_prime = [] # 所有質數 list
count_prime = 0 # 質數計數變數
for k in range(len(All_num)):
    tmp = 1 # 被除數
    count = 0 # 因數計數變數
    while (All_num[k] >= tmp):
        if All_num[k] % tmp == 0: 
            count = count + 1 # 因數計數 +1
        tmp = tmp + 1 # 被除數 +1
    if count == 2: # if 是質數
        all_prime.append(All_num[k]) # 把此數加入 所有質數 list
        count_prime = count_prime + 1 # 質數計數  +1
# (輸出)
if count_prime == 0: # if 質數計數 = 0
    print("No prime found")
else:
    all_prime.sort(reverse=True) # 所有質數排大小
    print("子字串中最大的質數為 : ", end="")
    print(all_prime[0])
