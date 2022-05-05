# Qn18_鋪克牌13點
print("請輸入五張鋪克卡牌")
numList = []
for k in range(1,6):
    card = input(f"輸入第{k}張卡牌:")
    numList.append(card)

point = 0
for i in range(5):
    match numList[i]:
        case "A":
            point = point + 1
        case "2":    
            point = point + 2
        case "3":    
            point = point + 3
        case "4":    
            point = point + 4
        case "5":    
            point = point + 5
        case "6":    
            point = point + 6
        case "7":    
            point = point + 7
        case "8":    
            point = point + 8
        case "9":    
            point = point + 9
        case "10" :   
            point = point + 10
        case "J":    
            point = point + 11
        case "Q":    
            point = point + 12
        case "K":    
            point = point + 13

print(f"卡片點數總合為:{point}點")
