# Qn21_學生資料搜尋
studentList = {
    "123":["How","IC"],
    "456":["Cat","CSIE"],
    "789":["Nana","ASIE"],
    "321":["Lim","DAB"],
    "654":["Won","FDD"]
}

inp = input("輸入查詢學號:")

print(f"學生資料為:{inp} {studentList[inp][0]} {studentList[inp][1]}")
