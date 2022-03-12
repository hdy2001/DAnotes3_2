import os

f = open("/Users/don/Desktop/DAnotes3_2/模式识别/作业/第三周编程作业/mammographic.txt",
         "r+")
lines = f.readlines()
for line in lines:
    strlist = line.replace(",", " ")
    flag = 1
    for value in strlist:
        # print(value)
        if value == '?':
            flag = 0
            break
    if flag == 1:
        with open("/Users/don/Desktop/DAnotes3_2/模式识别/作业/第三周编程作业/new.txt",
                  "a") as file1:
            file1.write(strlist)
