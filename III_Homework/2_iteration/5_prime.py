'''5.	迴圈的練習-prime
輸入一正整數，找出所有小於或等於的質數。
'''
n = eval(input('input:'))
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)






