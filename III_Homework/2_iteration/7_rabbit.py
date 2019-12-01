'''7.	迴圏的練習-rabbit
老王養了一群兔子，若三隻三隻一數，剩餘一隻；若五隻五隻一數，剩餘三隻；
若七隻七隻一數，剩餘二隻。試問兔子最少有幾隻。'''

n = 1
while True:
    if n % 3 == 1 and n % 5 == 3 and n % 7 == 2:
        break
    else:
        n += 1
print(n)


