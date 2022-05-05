# Qn22_提款機搜尋
Bank = {
    "000 000":1000,
    "111 111":2000,
    "222 222":3000
}

group = int(input("輸入查詢組數:"))
for i in range(group):
    id = input("XXX XXX")
    if id in Bank:
        print(f"帳戶餘額:{Bank[id]}")
    else:
        print("帳號或密碼有誤")
