'''2.	選擇性敘述的練習-salary
輸入便利商店工讀生的工作時數，並計算其薪資。
'''
from typing import Any, Union

hr = eval(input('input working hours:'))
if   hr >= 81:
        print (120 * (60 * 1 + 20 * 1.25 + (hr-80) * 1.5))
elif 61 >= hr <= 81:
        print(120 * (60 * 1 + (hr - 61) * 1.25))
else:
     print(120 * (hr * 1))


hr = eval(input('input working hours:'))
if  hr >= 81:
    s1, s2 = 60, 20; s3 = hr - 80
elif 61 >= hr < 81:
    s1 = 60; s2 = hr - 61; s3 = 0
else:
    s1 = hr; s2, s3 = 0, 0
print(120 * (s1 * 1 + s2 * 1.25 + s3 * 1.5))
