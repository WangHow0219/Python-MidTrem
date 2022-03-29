# Qn13_回文問題
Str = input("輸入字串")
unStr = Str[::-1]
if Str == unStr:
    print("YES")
else:
    print("NO")
