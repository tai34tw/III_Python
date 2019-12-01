'''1.	迴圏的練習-expression
利用for迴圏計算1^2-2^2+3^2-4^2+…+49^2-50^2的值。
'''

total = 0
for n in range (1, 51, 2):
    total = total + n**2 - (n+1)**2
print (total)