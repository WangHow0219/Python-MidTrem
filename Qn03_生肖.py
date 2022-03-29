# Qn3_西元年轉生肖
year = int(input("輸入西元年"))
year = year - 2010
K = year % 12
match K:
    case 0:
        print("虎年")
    case 1|-1:
        print("兔年")
    case 2|-2:
        print("龍年")
    case 3|-3:
        print("蛇年")
    case 4|-4:
        print("馬年")
    case 5|-5:
        print("羊年")
    case 6|-6:
        print("猴年")
    case 7|-7:
        print("雞年")
    case 8|-8:
        print("狗年")
    case 9|-9:
        print("豬年")
    case 10|-10:
        print("鼠年")
    case 11|-11:
        print("牛年")
