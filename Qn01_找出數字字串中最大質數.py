# Qn1_找出數字字串中最大質數
num = input("請輸入正整數")
All_num = []
for p in range(len(num),0,-1):
    for u in range(p):
        All_num.append(int(num[u:p]))

all_prime = []
count_prime = 0
for k in range(len(All_num)):
    tmp = 1
    count = 0
    while (All_num[k] >= tmp):
        if All_num[k] % tmp == 0: 
            count = count + 1
        tmp = tmp + 1
    if count == 2:
        all_prime.append(All_num[k])
        count_prime = count_prime + 1

if count_prime == 0:
    print("No prime found")
else:
    all_prime.sort(reverse=True)
    print("子字串中最大的質數為 : ", end="")
    print(all_prime[0])
