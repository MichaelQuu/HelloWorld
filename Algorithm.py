# -*- coding = utf-8 -*-
# @Time: 2022/7/14 2:04 PM
# @Author: Michael
# @File: Algorithm.py
list = [8.85, 8.85, 39.22, 98.06, 132.38, 132.74, 146.02, 150.44, 185.84, 196.12, 285.51, 343.20, 353.98, 386.14,
        442.48, 442.48, 496.38, 575.00, 628.32, 646.02, 701.12]

maxValue = 847.62
num = []
index = len(list)

for i in range(len(list)):
    for j in range(len(list)):
        for x in range(len(list)):
            if list[i] + list[j] + list[x] == maxValue:
                num.append(list[i])
                num.append(list[j])
                num.append(list[x])
                break
print(num)