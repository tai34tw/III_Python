'''8.	迴圏的練習-password
出現”請輸入密碼”的提示，使用者有最多三次輸入的機會。
若輸入正確，則印出”密碼輸入正確，歡迎使用本系統！”。
若輸入不正確，再次出現”請輸入密碼”的提示。
若三次輸入不正確，則印出”密碼輸入超過三次！”，並結束程式的執行。
'''

n =1
pswd = 123

while True:
    paswd1 = eval(input('請輸入密碼:'))
    if paswd1 == pswd:
        print('密碼輸入正確，歡迎使用本系統！')
        break
    elif n >= 3:
        print ('密碼輸入超過三次！')
        break
    elif paswd1 != pswd:
        n +=1