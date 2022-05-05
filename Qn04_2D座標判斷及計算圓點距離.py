# Qn4_2座標判斷及計算圓點距離
x = int(input("輸入X座標"))
y = int(input("輸入Y座標"))

if x == 0 and y != 0:
    print("該點在 Y 軸上",end="")
elif y == 0 and x != 0:
    print("該點在 X 軸上",end="")
elif y == 0 and x == 0:
    print("該點位於原點",end="")
elif x > 0:
    if y > 0:
        print("該點位於第一象限",end="")
    else:
        print("該點位於第四象限",end="")
else:
    if y > 0:
        print("該點位於第二象限",end="")
    else:
        print("該點位於第三象限",end="")
long = (x*x) + (y*y)
if  x != 0 or y != 0:
    print(f"，離原點距離 = 根號{long}")
