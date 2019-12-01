'''4.	迴圏的練習-amstrong
Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
找出所有的Amstrong數。
說明：153=13+53+33，故153為Amstrong數。
'''


for n in range (100, 1000):
    if n == ((n // 100)**3 + (n//10%10)**3 + (n%10)**3):
        print (n)
        n += 1
    else:
        n += 1
