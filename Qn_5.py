#Hw_1 N!超過 M 的最小 N 值為何？
max = int(input("輸入最大值"))
toatl_1 = 1
n = 1
while (toatl_1 <= max):
    toatl_1 = toatl_1 * n
    n = n + 1
n = n - 1
print(f"{n}! = {toatl_1} , 大於 {max}")
