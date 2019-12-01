'''2.	迴圏的練習-factor
輸入一正整數，求其所有的因數。
說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。
'''

n = 1
fctr= eval(input('type number:'))
while n <= fctr:
    if fctr % n == 0:
        print(n, end =',')
        n += 1
    elif True:
        n += 1
    else:
        print('輸入錯誤')
print()

n = eval(input('type number:'))
for i in range(1,(n+1)):
    if n % i ==0 :
        print(i)

