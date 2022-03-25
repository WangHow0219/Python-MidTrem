# Qn2_計算電費
degree = int(input("輸入用電度數 (正整數) : "))
s_cost = 0
us_cost = 0
if degree <= 120:
    s_cost = degree * 2.1
    us_cost = s_cost
elif degree <= 330:
    s_cost = 252 + (degree-120) * 3.02
    us_cost = 252 + (degree-120) * 2.68
elif degree <= 500:
    s_cost = 252 + 634.2 + (degree-330) * 4.39
    us_cost = 252 + 562.8 + (degree-330) * 3.61
elif degree <= 700:
    s_cost = 252 + 634.2 + 746.3 + (degree-500) * 4.97
    us_cost = 252 + 562.8 + 613.7 + (degree-500) * 4.01
else:
    s_cost = 252 + 634.2 + 746.3 + 994 + (degree-700) * 5.63
    us_cost = 252 + 562.8 + 613.7 + 802 + (degree-700) * 4.5
print(f"Summer months : {s_cost:.2f}")
print(f"Non-Summer months : {us_cost:.2f}")
